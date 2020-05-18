anphabet = ['a', 'ă', 'â', 'b', 'c', 'd', 
            'đ', 'e', 'ê', 'g', 'h', 'i', 
            'k', 'l','m', 'n', 'o', 'ô', 
            'ơ', 'p', 'q', 'r', 's', 't',
            't', 'u', 'ư', 'v', 'x', 'y',
            ]

def check_sign_ver1(word):
    word = word.lower()
    for char in  word:
        if char not in anphabet:
            return True
    return False


