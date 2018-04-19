import simplejson as json
import re
print('start updating user')
jfile='user.json'
a=0
b=0
use={}
review={}
out=open('user_2.json','w')
with open('review.json','r') as r:
	for line in r:
		line =json.loads(line)
		if line['user_id'] not in review:
			review[line['user_id']]=[0.00,0]
		if line['user_id'] in review:
			review[line['user_id']][0]+=line['stars']
			review[line['user_id']][1]+=1
with open('user.json','r') as u:
	for line in u:
		line=json.loads(line)
		s=0.00
		if line['user_id'] in review:
			s=review[line['user_id']][0]/review[line['user_id']][1]
			if line['average_stars']!=s:
				a=a+1
			out1=json.dumps({'user_id':line['user_id'],'average_stars':s,'review_count':review[line['user_id']][1]})
		else:
			b=b+1
			out1=json.dumps({'user_id':line['user_id'],'average_stars':0,'review_count':0})
		out.write(out1)
		out.write('\n')		
out.close()	
print "\n"
print "Numbers of users never made a review:",b
print "\n"
print "Numbers of users whose average_stars has changed:",a
print "\n"

print "Update finished:"
	