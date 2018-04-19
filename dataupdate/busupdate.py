import simplejson as json
import re
print('start updating business')
jfile='user.json'
c=0
a=0
b=0
use={}
review={}
out=open('business_2.json','w')
with open('review.json','r') as r:
	for line in r:
		line =json.loads(line)
		if line['business_id'] not in review:
			review[line['business_id']]=[0.00+line['stars'],1]
		if line['business_id'] in review:
			review[line['business_id']][0]+=line['stars']
			review[line['business_id']][1]+=1
with open('business.json','r') as u:
	for line in u:
		line=json.loads(line)
		s=0.00
		c=c+1
		if line['business_id'] in review:
			s=review[line['business_id']][0]/review[line['business_id']][1]
			print s
			if line['stars']!=s:
				a=a+1
			out1=json.dumps({"business_id" : line['business_id'],"hours" : line['hours'],"stars" :s,'review_count':review[line['business_id']][1]})	
		else:
			b=b+1
			out1=json.dumps({"business_id" : line['business_id'],"hours" : line['hours'],"stars" :0,'review_count':0})	
		out.write(out1)
		out.write('\n')		
out.close()	
print "\n"
print "Numbers of business never had a review:",b
print "\n"
print "Numbers of business whose average_stars has changed:",a
print "\n"
print "Update finished:"