import simplejson as json
import re
print('start cleaning user')
ufile='yelp_academic_dataset_user.json'
rfile='yelp_academic_dataset_review.json'
count=0
c=0
d=0
elite={}
felite={}
out=open('user.json','w')
with open(ufile,'r') as a:
	for line in a:
		count=count+1
		line=json.loads(line)
		if eval(line['elite'][0]):
			big,small= max(line['elite']), min(line['elite'])
			if big<=str(2017) and line['yelping_since']>=str(2004)  :
				elite[line['user_id']]=small
			else:
				c=c+1
		else:
			d=d+1
			elite[line['user_id']]=0
with open(rfile,'r') as r:
	for line in r:
		line=json.loads(line)
		year=line['date'].split('-')[0]
		if elite[line['user_id']] ==0 or year <= elite[line['user_id']]:
			felite[line['user_id']]=line['user_id']
with open(ufile,'r') as u:
	for line in u:
		line=json.loads(line)
		if line['user_id'] in felite:
			out1=json.dumps({"user_id" : line['user_id'],"elite" : line['elite'],"average_stars" : line['average_stars'],"review_count" : line['review_count']})		
			out.write(out1)
			out.write('\n')			
print "\n"
print "cleaning finished"
print "\n"
print "Numbers of user before cleaning:",count
print "\n"
print "Numbers of user without elite:",d
print "\n"
print "Numbers of user whose elite is before 2004 or after 2017 :",c
print "\n"
print "Numbers of user who made review  after being an elite :",len(elite)-len(felite)
print "\n"
print "Numbers of user after cleaning:",len(felite)

out.close()

		
			
		