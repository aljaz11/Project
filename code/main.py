import sys
import json

generated_dict = {}
def convert(data):
	converted = json.loads(data)	
	for key, value in converted.items():
		solve2(value, [key])
	global generated_dict	
	outpt = json.dumps(generated_dict)
	# clean global variable
	generated_dict = {}	
	return outpt


def solve2(json, generated_key):
	curr_val = json
	
	# if current value is not a dict or dict is empty -> finish this instance
	if ((isinstance(curr_val, dict) != True) or (isinstance(curr_val, dict) and not curr_val)):				
		generated_dict[generateKey(generated_key)] = curr_val
		return
	
	# else loop to the next level
	else:		
		for key, value in json.items():
			generated_key.append(key)			
			solve2(value, generated_key)
			# clen appended key
			generated_key = generated_key[:-1]
			
def generateKey(keys):
	string = ""
	for i in keys:
		if string == "":
			string = i
		else:
			string = string + "." + i 
	return string

# for testing
def removeWhitespaces(text):
	return ''.join([c for c in text if c not in [' ','\t','\n']])

if __name__ == '__main__':
   # for use from command line
   # cat test.json | python3 main.py
   file = sys.stdin.read()
   print(convert(file))