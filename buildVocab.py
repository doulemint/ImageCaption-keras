from collections import Counter,OrderedDict
import json  
import Dataloader 


word_counter = Counter() #just load the counter
n_sample = 0
maxlen = 0
img2captions = Dataloader.get_caption_img()
for img,captions in img2captions.items():
    for caption in captions:
        n_sample += 1
        caption = caption.lower() 
        caption = str(caption) # transform into string
        tokens = caption.split()
        maxlen = max([maxlen,len(tokens)])
        word_counter.update(tokens) #miaomiaomiao?
print('number of sample = ' + str(n_sample))
print('max len = ' + str(maxlen))


word_counts = [x for x in word_counter.items()]
word_counts.sort(key=lambda x: x[1],reverse=True)
json.dump(word_counts, open('word_counts.json','w'),indent=2)

vocab = [w for w, c in word_counts if c >= 1]
start_word = '<start>'
end_word = '<end>'
vocab = [start_word, end_word] + vocab
print('Vocabulary size = %d'%len(vocab))

word2idx = OrderedDict(zip(vocab,range(len(vocab))))
idx2word = OrderedDict(zip(range(len(vocab)),vocab))
json.dump(word2idx,open('word2dix.json','w'),indent=2)

