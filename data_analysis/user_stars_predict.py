import simplejson as json
import re
c=0
use={}
review={}
bus ={}
out=open('user_predict.json','w')
with open('business_2.json','r') as b:
	for line in b:
		line=json.loads(line)
		bus[line['business_id']]=line['stars']
with open('review.json','r') as r:
	for line in r:
		line =json.loads(line)
		if line['user_id'] not in review:
			review[line['user_id']]=[0.00,0,0.00,0]
		else:
			if bus[line['business_id']] >3:
				review[line['user_id']][0]+=line['stars']-bus[line['business_id']]
				review[line['user_id']][1]+=1
			else:
				review[line['user_id']][2]+=line['stars']-bus[line['business_id']]
				review[line['user_id']][3]+=1
		
with open('user_2.json','r') as u:
	for line in u:
		line=json.loads(line)
		s0=0.00
		s2=0.00
		if line['review_count'] >20:
			c=c+1
			print c
			s1=review[line['user_id']][1]
			s3=review[line['user_id']][3]
			if s1!=0:
				s0=review[line['user_id']][0]/review[line['user_id']][1]
				s0=round(s0 ,2)
			else:
				s1=0
			if s3!=0:
				s2=review[line['user_id']][2]/review[line['user_id']][3]
				s2=round(s2 ,2)
			else:
				s2=0
			out1=json.dumps({'user_id':line['user_id'],'rating_big':s0,'rating_small':s2,'count_big':s1,'count_small':s3})
			out.write(out1)
			out.write('\n')		
out.close()	
