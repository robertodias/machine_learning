def count_words( word, count ):
	"""
	My First Python code :)
	This function receives word as text and count as a number
	It will group words by occurency and the count limit will be used to limit the words to return
	Return: [(word1, count1)..(wordN, countN)]
	"""
	word_array = word.split(" ")
	return_list = []
	word_count = 0
	word_array.sort()
	word_buffer = word_array[0]
	for text in word_array:
		if word_buffer != text:
			return_list.append((word_buffer,word_count))
			word_buffer = text
			word_count = 0
		word_count = word_count + 1
	return_list.append((word_buffer,word_count))
	return_list.sort(key=lambda t: t[1], reverse=True)
	index = 0
	return_final = []
	while index < count:
		return_final.append(return_list[index])
		index = index + 1
	return return_final;