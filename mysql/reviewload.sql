drop table if exists review;
create table review(
review_id varchar(25),
business_id varchar(25),
user_id varchar(25),
stars float,
review_length int,
date date,
useful int,
cool int,
funny int
)ENGINE=INNODB;
load data local infile 'c:\\python27\\scripts\\ece656\\scripts\\yelp\\review.csv' 
into table review
fields terminated by ',' 
enclosed by '"' 
escaped by '' 
lines terminated by '\r\n' 
ignore 1 lines ;