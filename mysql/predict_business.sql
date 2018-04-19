DROP PROCEDURE IF EXISTS trend;
DELIMITER @@
CREATE PROCEDURE trend(IN id varchar(25))
BEGIN	
set @longs=(select stars from business where business_id=id);
set @shorts=(select avg(stars) from review where business_id=id and date>'2016-01-01');
if @longs>@shorts then
	update business set trend ='better' where business_id=id;
else
	update business set trend ='worse' where business_id=id;
end if;	
END@@
DELIMITER ;
DROP PROCEDURE IF EXISTS predict;
DELIMITER @@
CREATE PROCEDURE predict()
BEGIN	
DECLARE done BOOLEAN DEFAULT FALSE;
  DECLARE _id varchar(25);
  DECLARE cur CURSOR FOR (select business_id from business where review_count>=50);
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done := TRUE;
  OPEN cur;
  testLoop: LOOP
    FETCH cur INTO _id;
    IF done THEN
      LEAVE testLoop;
    END IF;
    CALL trend(_id);
  END LOOP testLoop;

  CLOSE cur;
END@@
DELIMITER ;