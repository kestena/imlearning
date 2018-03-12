#this is the codewars Get the shortest word challenge. Might help someone
def find_short(s):
	s_list = [] #create an empty list which will store the length of the each individual words in the str.
	for i in range (0, len(s.split())): #for loop for going through the str len
		get_len = (len(s.split()[i])) #get the len of each str item
		s_list.append(get_len) #append each item to the empty list
	l = min(s_list) # assign l to get the min of the newly created list
	return l #just return l