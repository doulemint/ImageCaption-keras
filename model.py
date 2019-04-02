import Dataloader
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import LSTM, Embedding, TimeDistributed, Dense, RepeatVector, merge, Activation, Flatten
from keras.layers.wrappers import Bidirectional
from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image
from keras.models import Model
import nltk
from tqdm import tqdm


def preprocess_input(x):
	x /= 255.
	x -= 0.5
	x *= 2.
	return x
def preprocess(image_path):
	img = image.load_img(imge_path,target_size=(299,299))
	x = image.img_to_array(img)
	x = np.expand_dims(x,axis=0)
def encode(image):
	image = preprocess(image)
	temp_enc = model_new.predict(image)
	temp_enc = np.reshape(temp_enc,temp_enc.shape[1])
	return temp_enc


images_dir,train_imgs, val_imgs, test_imgs = Dataloader.get_train_val_test()
img2captions = Dataloader.get_caption_img()


f = open('flickr8k_train_dataset.txt', 'w')
f.write("image_id\tcaptions\n")
for img in train_imgs:
    for cap in img2captions[img]:
        f.write(img + "\t" + "<start> " + cap +" <end>" + "\n")
f.close()

f = open('flickr8k_val_dataset.txt', 'w')
f.write("image_id\tcaptions\n")
for img in val_imgs:
    for cap in img2captions[img]:
        f.write(img + "\t" + "<start> " + cap +" <end>" + "\n")
f.close()

f = open('flickr8k_test_dataset.txt', 'w')
f.write("image_id\tcaptions\n")
for img in test_imgs:
    for cap in img2captions[img]:
        f.write(img + "\t" + "<start> " + cap +" <end>" + "\n")
f.close()


encoding_train = {}
for img in tqdm(train_img):
	encoding_train[img[len(images):]] = encode(img)
with open("encoded_images_train_inceptionV3.p","wb") as encoded_pickle:
	pickle.dump(encoding_train, encoded_pickle)

encoding_test = {}
for img in tqdm(test_img):
	encoding_test[img[len(images):]] = encode(img)
with open("encoded_images_test_inceptionV3.p","wb") as encoded_pickle:
	pickle.dump(encoding_test, encoded_pickle)

encoding_train = pickle.load(open('encoded_images_train_inceptionV3.p', 'rb'))
encoding_test = pickle.load(open('encoded_images_test_inceptionV3.p', 'rb'))

