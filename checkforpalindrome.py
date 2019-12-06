def palindroom(text):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''
    text1 = text.lower()
    for punc in text1:
        if punc in punctuation:
            text1 = text1.replace(punc,'')
    
    if text1 == text1[::-1]:
        print('true')
        return True
    
    else:
        print('false')
        return False

palindroom('meetsysteem')
palindroom('En er is ananas, Irene')
