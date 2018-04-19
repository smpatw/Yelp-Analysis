import simplejson as json
import re
print('start cleaning review')
print('\n')
rfile='yelp_academic_dataset_review.json'
bus={}
user={}
count=0
c=0
d=0
out=open('review.json','w')
with open('business.json', 'r') as f:
	for line in f:
		line=json.loads(line)['business_id']
		bus[line]=line
with open('user_2.json', 'r') as f:
	for line in f:
		line=json.loads(line)['user_id']
		user[line]=line	
with open(rfile,'r') as r:
	for line in r:
		line =json.loads(line)
		if line['user_id'] in user and line['business_id']in bus:
			c=c+1
			out1=json.dumps({'review_id':line['review_id'],'user_id':line['user_id'],'business_id':line['business_id'],'date':line['date'],'review_length':len(line['text']),'useful':line['useful'],'cool':line['cool'],'funny':line['funny'],'stars':line['stars']})
			out.write(out1)
			out.write('\n')
print "cleaning finished"
print "\n"
print "Numbers of review before cleaning:",count
print "\n"
print "Numbers of review whose user_id not in user or business_id not in business:",count-c
print "\n"
print "Numbers of reviews after cleaning:",c
print "\n"
print "reviews cleaning finish:"

out.close()