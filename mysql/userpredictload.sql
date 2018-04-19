drop table if exists user_predict;
create table  user_predict(
user_id varchar(25) primary key,
rating_big float,
rating_small float,
count_big int,
count_small int
);
load data local infile 'c:\\python27\\scripts\\ece656\\scripts\\yelp\\user_predict.csv' 
into table user_predict
fields terminated by ',' 
enclosed by '"' 
escaped by '' 
lines terminated by '\r\n' 
ignore 1 lines ;