import matplotlib.pyplot as plt

def get_caption_img():
	caption_file = 'Flickr8k_text/Flickr8k.token.txt'
	img2captions = {}
	for row in open(caption_file):
	    row = row.strip()
	    row = row.split('\t')  #split image and description
	    img = row[0][:len(row[0])-2] #get image name and remove "#num'
	    cap = row[1].lower() #transform all capital to lower letter
	    if img not in img2captions:
	       img2captions[img] = [] # creat a set in dict
	    img2captions[img].append(cap) #add value to the key of img

	#test				  	  print(img2captions['1000268201_693b08cb0e.jpg'])
	return img2captions
#imageload path
def get_train_val_test():
	images_dir = 'Flickr8k_Dataset/'

	#imagename path for training
	train_images_file = 'Flickr8k_text/Flickr_8k.trainImages.txt'
	train_images = [line.strip() for line in open(train_images_file)]
	print(len(train_images),train_images[:3])

	#imagename path for val
	val_images_file = 'Flickr8k_text/Flickr_8k.devImages.txt'
	val_imgs = [line.strip() for line in open(val_images_file)]
	print(len(val_imgs), val_imgs[:3])

	#imagename path for testing
	test_images_file = 'Flickr8k_text/Flickr_8k.testImages.txt'
	test_imgs = [line.strip() for line in open(test_images_file)]
	print(len(test_imgs), test_imgs[:3])

	return train_images, val_imgs, test_imgs
	#test
	#img = train_imgs[0]
	#plt.imshow(Image.open(images_dir + '/' + img)) todo change to cv2
	#print('\n'.join(img2captions[img]))

if __name__ == '__main__':
   get_caption_img()
