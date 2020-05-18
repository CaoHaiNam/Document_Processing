from pyvi import ViTokenizer
import os
import json

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_PATH = os.path.join(DIR_PATH, '_data/train')
STORE_WORD_NON_ARC_PATH = os.path.join(DIR_PATH, '_data/word_without_arc')
STORE_WORD_ARC_PATH = os.path.join(DIR_PATH, '_data/word_exist_arc')
STOP_WORD_PATH = os.path.join(DIR_PATH,'_data/vietnamese-stopwords-dash.txt')
ACRONYM_PATH = os.path.join(DIR_PATH,'_data/acronym_non_token.json')
special_string = ['www', 'http', 'https']
special_character = '0123456789%@$.,=+-!";/()*"&^:#|\n\t\'”“…[]{<}>`~'

class FileReader(object):
    def __init__(self, filePath, encoding = None):
        self.filePath = filePath
        self.encoding = encoding if encoding != None else 'utf-16'

    def content(self):
        with open(self.filePath, encoding=self.encoding) as f:
            return f.read()

class DataLoader(object):
    def __init__(self, dataPath):
        self.dataPath = dataPath

    def _get_file(self):
        class_titles = os.listdir(self.dataPath)
        dict_ = {}
        for titles in class_titles:
          folder = self.dataPath + '/'+ titles
          dict_[titles] = [folder + '/' + f for f in os.listdir(folder)]
        return class_titles, dict_

def token(text):
  text = ViTokenizer.tokenize(text).split(" ")
  words = []
  for word in text:
    words.append(word)
  return words

def check_special_char(word):
  for char in special_character:
    if char in word:
      return True
  return False

def check_special_string(word):
  for str_ in special_string:
    if str_ in word:
      return True
  return False

class NLP_without_arc(object):

  def __init__(self, text=None):
    self.text = text
 
  def segmentation(self):
    return ViTokenizer.tokenize(self.text)
 
  def set_redundant_words(self):
    self.stopwords = FileReader(filePath=STOP_WORD_PATH, encoding='utf-8').content().split('\n')

  def set_arconym(self):
    with open (ACRONYM_PATH,'r',encoding='utf8') as f:
        self.acronym = json.load(f)
 
  def split_word(self):
    text = self.segmentation()
    text = text.split(' ')
    split_word = []
    for word in text:
      split_word.append(word)
    return split_word
 
  def get_word_feature(self):
    split_word = self.split_word()
    result = []
    self.set_redundant_words()
    self.set_arconym()
    for word in split_word:
        word = word.lower()
        if word in self.stopwords:
          continue
        if word in self.acronym:
          non_arc = token(self.acronym[word])
          for w in non_arc:
            result.append(w)
          continue
        if check_special_char(word):
          continue
        if check_special_string(word):
          continue
        result.append(word)
    return result

class NLP_exist_arc(object):

  def __init__(self, text=None):
    self.text = text
 
  def segmentation(self):
    return ViTokenizer.tokenize(self.text)
 
  def set_redundant_words(self):
    self.stopwords = FileReader(filePath=STOP_WORD_PATH, encoding='utf-8').content().split('\n')
 
  def split_word(self):
    text = self.segmentation()
    text = text.split(' ')
    split_word = []
    for word in text:
      split_word.append(word)
    return split_word
 
  def get_word_feature(self):
    split_word = self.split_word()
    result = []
    self.set_redundant_words()
    for word in split_word:
        word = word.lower()
        if word in self.stopwords:
          continue
        if check_special_char(word):
          continue
        if check_special_string(word):
          continue
        result.append(word)
    return result

def build_dict_without_arc():
  total_file = DataLoader(DATA_PATH)
  class_titles, dict_url = total_file._get_file()

  dict_ = {}
  for title in class_titles:
    dict_[title] = {}
    for url in dict_url[title]:
      text = FileReader(url, encoding='utf-16').content()
      features = NLP_without_arc(text).get_word_feature()
      for feature_ in features:
        if feature_ in dict_[title]:
          dict_[title][feature_] += 1
        else:
          dict_[title][feature_] = 1

  for title in class_titles:
    with open(os.path.join(STORE_WORD_NON_ARC_PATH,title + '.json'), 'w', encoding='utf8') as f:
      f.seek(0)
      json.dump(dict_[title], f, ensure_ascii=False)

def build_dict_exist_arc():
  total_file = DataLoader(DATA_PATH)
  class_titles, dict_url = total_file._get_file()

  dict_ = {}
  for title in class_titles:
    dict_[title] = {}
    for url in dict_url[title]:
      text = FileReader(url, encoding='utf-16').content()
      features = NLP_exist_arc(text).get_word_feature()
      for feature_ in features:
        if feature_ in dict_[title]:
          dict_[title][feature_] += 1
        else:
          dict_[title][feature_] = 1

  for title in class_titles:
    with open(os.path.join(STORE_WORD_ARC_PATH,title + '.json'), 'w', encoding='utf8') as f:
      f.seek(0)
      json.dump(dict_[title], f, ensure_ascii=False)
