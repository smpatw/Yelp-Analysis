import json
import csv
column_names=['user_id','average_stars','review_count']
jfile='user_2.json'
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
with open('user_2.csv', 'wb+') as a:
        csv_file = csv.writer(a)
        csv_file.writerow(list(column_names))
        with open(jfile) as f1:
            for line in f1:
                line_contents = json.loads(line)
                csv_file.writerow(get_row(line_contents, column_names))
# with open('elite.csv', 'wb+') as c:
	# csv_file2 = csv.writer(c)
	# csv_file2.writerow(['user_id','elite'])
	# with open(jfile) as f3:
		# for line in f3:
			# line_contents = json.loads(line)
			# id=line_contents['user_id']
			# elites=line_contents['elite']
			# if elites is not None:
				# for year in elites:
					# csv_file2.writerow([id,year])
			# else:
				# csv_file2.writerow([id,'null'])		
