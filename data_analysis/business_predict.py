import simplejson as json
import re
use={}
review={}
out=open('business_predict.json','w')
with open('review.json','r') as r:
	for line in r:
		line =json.loads(line)
		if line['business_id'] not in review:
			if line['date'].split('-')[0]>=2016:
				review[line['business_id']]=[0.00+line['stars'],1]
		else:
			if line['date'].split('-')[0]>=2016:
				review[line['business_id']][0]+=line['stars']
				review[line['business_id']][1]+=1
		
with open('business_2.json','r') as u:
	for line in u:
		line=json.loads(line)
		s0=0.00
		if line['business_id']in review:
			if line['review_count'] >20:
				c=0
				s1=review[line['business_id']][1]
				s0=review[line['business_id']][0]/s1
				s=s0-line['stars']
				if s>0:
					c=1
				if s<0:
					c=-1
				if s==0:
					c=0
				s=s0-line['stars']
				out1=json.dumps({'business_id':line['business_id'],'rating_trend':c,'rating_increase':s})
				out.write(out1)
				out.write('\n')		
out.close()	