sentence =input("please write your sentence: ")
my_dict = {}
for i in set(sentence):    
    my_dict.update({i : sentence.count(i)})
print(my_dict)
