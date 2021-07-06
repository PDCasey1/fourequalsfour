from prefixes_and_suffixes import prefixes, suffixes


# takes an integer and splits it into its decimal-separated groupings, e.g.'hundreds', 'thousands', 
# 'million's, etc., and places each group into a list of strings used as input by the
# numbers_spelled_out() function. Then creates a "written out" string of that number, concatenating
# the number itself with its suffix (1001 > 'one thousand one'). 

def number_spelled_out(num):
	if num == 0:
		return('zero')

	num = str(num)
	arr = ['']
	spelled_string = ''

	while len(num) %3 != 0:
		arr[0] += num[0]
		num = num[1:]

	for i in range(0, len(num), 3):
			arr.append(num[i:i+3])

	if arr[0]=='':
		arr.remove('')

	arr = [int(i) for i in arr]

	for num, i in enumerate(arr):

		if i == 0:
			pass
		elif i in prefixes:
			spelled_string += prefixes[i]+suffixes[len(arr)-num-1]+' '
		elif i not in prefixes:
			spelled_string += prefixes[int(str(i)[0])]+' hundred '+prefixes[int(str(i)[1:3])]+suffixes[len(arr)-num-1]+' '
		
	return(spelled_string.strip())

def letters_in_string(string):

	count = 0
	for i in string:
		if i in 'abcdefghijklmnopqrstuvwxyz':
			count += 1

	return(count)


def decay_num(num):
	cycles = 0

	while True:
		if letters_in_string(number_spelled_out(num))!= 4:
			cycles+=1
			num = letters_in_string(number_spelled_out(num))

		else:
			cycles+=1
			break

	return(num, cycles)

def print_decay(num):

	while True:
		print((number_spelled_out(num))+' equals '+str(letters_in_string(number_spelled_out(num))))

		if letters_in_string(number_spelled_out(num)) == 4:
			print('four equals 4\n')
			break
		else:
			num = letters_in_string(number_spelled_out(num))
			

def max_decay(x,y,z=1, pass_through=False):
	
	max_list=[]
	max_num = 0
	max_cycles = 0


	for i in range(x,y,z):
		if decay_num(i)[1] > max_cycles:
			max_num = i
			max_list.clear()
			max_list.append(max_num)
			max_cycles = decay_num(i)[1]
		elif decay_num(i)[1] == max_cycles:
			max_list.append(i)

	if pass_through == False:

		print('Range:({} : {})\nMaximum iterations: {}\nOrigin: {}\n'.format(x, y, max_cycles, max_num))
		print_decay(max_num)
		print()

	else:
		return  max_cycles, max_list