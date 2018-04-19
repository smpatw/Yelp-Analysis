alter table business add index(business_id) using btree;
alter table user add index(user_id) using btree;
alter table review add index(review_id) using btree;
alter table review add index(business_id) using btree;
alter table review add index(user_id) using btree;