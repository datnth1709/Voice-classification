import os
import csv

with open('voice_label_1_10.csv', 'w') as f:  # file voice.csv khoi tao
	csv_line = 'fname,label'
	writer = csv.writer(f)
	writer.writerows([csv_line.split(',')])
	for i in os.listdir('data1-10'): # nho dat ten folder chinh la '1-10' nha
		for n in os.listdir('data1-10/'+i): #truy cap vo tung folder con
			print(n)
			writer.writerow([n]+[str(i)])
	f.close()