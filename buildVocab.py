#todo collection not found
#todo segmentation fault
from collection import Counter,OrderedDict
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
        word_counter.updata(tokens)
print('number of sample = ' + str(n_sample))
print('max len = ' + str(maxlen))


word_counts = [x for x in word_counter.items()]
word_counts.sort(key=lambda x: x[1],reverse=True)
json.dump(word_counts, open('word_counts.json','w'),indent=2)



       
