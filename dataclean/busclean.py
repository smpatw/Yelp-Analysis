import simplejson as json
import re
print('start cleaning user')
print('\n')
bfile='yelp_academic_dataset_business.json'
count=0
c=0
d=0
count = 0
e=0
out=open('business.json','w')
with open(bfile, 'r') as f:
	for line in f:
		count += 1
		line = json.loads(line)
		if not line['is_open'] :
			c=c+1
		if not line['hours']:
			d=d+1
		if line['is_open'] and line['hours']:	
			out1=json.dumps({"business_id" : line['business_id'],"hours" : line['hours'],"stars" : line['stars']})	
			e=e+1
			out.write(out1)
			out.write('\n')

print "Number of business before cleaning:" , count
print "\n"
print "Number of business is not open:",c
print "\n"
print "Number of business don't have open hours:",d
print "\n"
print "Number of business after cleaning:",e
print "\n"
print "Business cleaning finished"
