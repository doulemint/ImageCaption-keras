##final_model
#sequence
#idx2word

final_model.load_weights('saved_model.h5')
def predict_captions(image):
	start_word = ["<start>"]
	e = encode(image)
	while True:
		par_caps = [word2idx[i] for i in start_word]
		par_caps = sequence.pad_sequences([par_caps],maxlen=max_len,padding='post')
		
		preds = final_model.predict([np.array([e]),np.array(per_caps)])
		word_pred = idx2word[np.argmax(preds[0])]
		start_word.append(word_pred)

		if word_pred == "<end>" or len(start_word) > max_len:
			break
	return ''.join(start_word[1:-1])


