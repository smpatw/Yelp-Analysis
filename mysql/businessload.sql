drop table if exists business;
create table business(
business_id varchar(25),
stars float,
review_count int
)ENGINE=INNODB;
load data local infile 'c:\\python27\\scripts\\ece656\\scripts\\yelp\\business.csv' 
into table business
fields terminated by ',' 
enclosed by '"' 
escaped by '' 
lines terminated by '\r\n' 
ignore 1 lines ;