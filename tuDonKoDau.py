import json
import os
import check_dau_thanh
import features
# kiểm tra file Chinh trị xã hội
path = os.path.join(features.STORE_WORD_ARC_PATH, 'The thao.json')

with open (path, 'r', encoding = 'utf8') as f:
    dict_ = json.load(f)

words = []
for word in dict_:
    if '_' in word:
        continue
    if (check_dau_thanh.check_sign_ver1(word)):
        continue
    words.append(word)

print(words)