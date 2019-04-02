#ImageCaption


----------
####1.1 Data loader
Read the Flickr8k.token.text file. Extract img_name and description into a dictionary```img2Captions```.
(W: Each image not only has one description)
####1.2 Image loader
read image name line by line and split them by space ```stript()``` then store into three variations.

####2.1 Build Vocab
Utilize the Python's standard library ```Counter()``` to calculate how many times a word has been used.  Therefore we can establish a 'dictionary' ```word2idx```, and save it as Json date.

####2.2 Rewrite dataset
In order to avoid damaging original dataset and alter the text, we rebuild a file to store new form including ```<start>+<end>``` to tell machines where is the end and begin.

####3.1 Build model
We use google Inception V3 (this may take few hours for the download.)as CNN to extract high-level features and LSTM as language model to decode sentences.
 
#### 3.2 Training and Test
batch_size = 256, epoch = 30, 
#Acknowledge

TFT-xiaozu 

