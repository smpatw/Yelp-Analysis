drop table if exists business_predict;
create table  business_predict(
business_id varchar(25) primary key,
rating_trend int,
rating_increase float
);
load data local infile 'c:\\python27\\scripts\\ece656\\scripts\\yelp\\business_predict.csv' 
into table business_predict
fields terminated by ',' 
enclosed by '"' 
escaped by '' 
lines terminated by '\r\n' 
ignore 1 lines ;