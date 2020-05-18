import features
def get_features(text):
    return features.NLP_exist_arc(text).get_word_feature()

text = 'UBND thành phố hà nội'
print(get_features(text))