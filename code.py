import json

#Variablen
filename = 'programming.txt'
jasonfile = 'Liste.json'
name = input("Name : ")
age = input("Alter : ")

#File öffnen
with open(filename, 'a') as file_object:
	file_object.write("Name : " + name + "\n")
	file_object.write("Alter : " + age)
#	file_object.write("line 1 line 2")
	
with open(filename) as file_object:
	lines = file_object.readlines()
	
pi_string =''
for line in lines:
	pi_string += line.rstrip()
	
print(pi_string)
print(len(pi_string))

alter_unter = input("Alter bis : ")

with open(jasonfile) as f:
	data = json.load(f)

for dict in data:
	if dict['Alter'] == alter_unter:
	json_name = dict['Name']
	json_alter = dict['Alter']
	json_mail = dict['Mail']
	print(json_name + ": " + json_mail)
