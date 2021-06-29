from prefixes_suffixes import prefixes, suffixes

def delim(x):
    x = str(x)
    
    start_string = ''
    delim_num_list = []
    
    while len(str(x))%3 != 0:
        start_string += x[0]
        x = x[1:]
        
    if len(start_string) > 0:
        delim_num_list.append(int(start_string))
        
    for i in range(0, len(x), 3):
        delim_num_list.append(int(x[i:i+3]))
        
    return(delim_num_list)

def text_num(arr):

	string = ''

	if len(arr) == 1:
		string+=(prefixes[arr[0]])
	else:

		for count, num in enumerate(arr):
			if num != 0 and count+1 != len(arr):
				string += prefixes[num]+suffixes[len(arr)-count-1]+' '
			elif num != 0:
				string += prefixes[num]+suffixes[len(arr)-count-1]

	return(string.strip())

def num_count(string):

	count = 0
	for i in string:
		if i in 'abcdefghijklmnopqrstuvwxyz':
			count += 1

	return count

def decay_num(num):
	i = 0
	l = []

	while True:
		if len(l) == 0:
			l.append(num)
			l.append(text_num(delim(num)))
		
		if num_count(text_num(delim(num))) == 4:
			i += 1
			l.append(i)
			break
		else:
			i += 1
			num = num_count(text_num(delim(num)))

	return(l)

def print_decay(num):

	while True:
		print((text_num(delim(num))+' equals '+str(num_count(text_num(delim(num))))))
		if num_count(text_num(delim(num))) == 4:
			print('four equals 4\n')
			break
		else:
			num = num_count(text_num(delim(num)))
			

def max_decay(x,y,z=1, pass_through=False):
	
	max_list=[]
	max_num = 0
	max_iter = 0


	for i in range(x,y,z):
		if decay_num(i)[2] > max_iter:
			max_num = i
			max_list.clear()
			max_list.append(max_num)
			max_iter = decay_num(i)[2]
		elif decay_num(i)[2] == max_iter:
			max_list.append(i)

	if pass_through == False:

		print('Range:({} : {})\nMaximum iterations: {}\nOrigin: {}\n'.format(x, y, max_iter, max_num))
		print_decay(max_num)
		print()

	else:
		return  max_iter, max_list