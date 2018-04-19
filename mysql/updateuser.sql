DROP PROCEDURE IF EXISTS upuser;
DELIMITER @@
CREATE PROCEDURE upuser(in id varchar(26))
BEGIN	
if (select avg(stars) from review where user_id=id) is null then
	update user set average_stars=0 where user_id=id;
else
	update user set average_stars=(select avg(stars) from review where user_id=id) where user_id=id;
end if;
END@@
DELIMITER ;
DROP PROCEDURE IF EXISTS upda;
DELIMITER @@
CREATE PROCEDURE upda()
BEGIN	
DECLARE done BOOLEAN DEFAULT FALSE;
  DECLARE _id varchar(25);
  DECLARE cur CURSOR FOR (select user_id from user);
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done := TRUE;
    OPEN cur;
  testLoop: LOOP
    FETCH cur INTO _id;
    IF done THEN
      LEAVE testLoop;
    END IF;
    CALL upuser(_id);
  END LOOP testLoop;
  CLOSE cur;
END@@
DELIMITER ;