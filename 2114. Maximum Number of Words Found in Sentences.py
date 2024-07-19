sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]


max_word=0
for sentence in sentences:
    new_sentence= sentence.split(" ")
    new_length=len(new_sentence)
    if(new_length>max_word):
        max_word=new_length
    
print(max_word)