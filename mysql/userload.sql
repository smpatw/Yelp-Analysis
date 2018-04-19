drop table if exists user;
create table  user(
user_id varchar(25) primary key,
average_stars float
);
load data local infile 'c:\\python27\\scripts\\ece656\\scripts\\yelp\\user.csv' 
into table user
fields terminated by ',' 
enclosed by '"' 
escaped by '' 
lines terminated by '\r\n' 
ignore 1 lines ;