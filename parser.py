global step


def Check_E(sentence):
	global step
	if(sentence[step]) =='e':
		step = step+1
		Check_B(sentence)
		if(sentence[step]=='a'):
			step = step+1
			Check_A(sentence)
	else:
		print('Unaccepted!')



def Check_B(sentence):
	global step
	if sentence[step] == 'd':
		step = step+1
		Check_E(sentence)
		if sentence[step] == 'd':
			step = step+1
	elif sentence[step] == 'a':
		step = step+1
		Check_C(sentence)

	else:
		print('Unaccepted')
def  Check_C(sentence):
	global step
	if(sentence[step] == 'e'):
		step = step+1
	elif(sentence[step] == 'd'):
		step = step+1
		Check_C(sentence)
	else:
		print('Unaccepted')

def Check_A(sentence):
	global step
	if sentence[step] =='a':
		step = step+1
	elif sentence[step] =='b':
		step = step+1
		Check_A(sentence)
		if sentence[step] =='c':
			step = step+1
			Check_B(sentence)
	else:
		pritn('Unaccepted')
if __name__ == '__main__':
	sentence1 = 'eadeaa#'
	sentence2 = 'edeaebd#'
	sentence3 = 'edeaeaadabacae#'
	sentence = [sentence1,sentence2,sentence3]

	for item in sentence:
		print(item)
		step = 0
		Check_E(item)
		if(item[step] == '#'):
				print('Accepted!')
		else:
				print('Unaccepted')