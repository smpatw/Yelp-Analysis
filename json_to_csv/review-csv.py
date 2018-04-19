import json
import csv
column_names=['review_id','business_id','user_id','stars','review_length','date','useful','cool','funny']
jfile='review.json'
count=0
def get_row(line_contents, column_names):
    row = []
    for column_name in column_names:
        line_value = line_contents[column_name]
        if isinstance(line_value, unicode):
            row.append('{0}'.format(line_value.encode('utf-8')))
        elif line_value is not None:
            row.append('{0}'.format(line_value))
        else:
            row.append('')
    return row	
with open('review.csv', 'wb+') as a:
        csv_file = csv.writer(a)
        csv_file.writerow(list(column_names))
        with open(jfile) as f1:
            for line in f1:
                count+=1
                print count
                line_contents = json.loads(line)
                csv_file.writerow(get_row(line_contents, column_names))