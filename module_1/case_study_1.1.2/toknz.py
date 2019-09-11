from pathlib import Path
from nltk import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import string

en_stopwords = set(stopwords.words('english'))

root = ".//case_topics//"
dir = Path(root + "abstracts")
for file in dir.iterdir():
    print('-------------------' + file.name + '-------------------')

    with open(file, 'r') as input_file:
        txt = input_file.read()

        word_tokens = word_tokenize(txt)

        word_counter = Counter()
        # stopword_counter = Counter()

        for word in word_tokens:
            if not word in en_stopwords and not word in string.punctuation:
                word_counter[word] += 1
            # else:
            #     stopword_counter[word] += 1
        
        # print (word_counter)
        #print ('stopword_counter:')
        #print (stopword_counter)
        
        with open(root + 'corpus\\'+file.name, 'w') as output_file:
            for k, v in word_counter.most_common(20):
                print(f'{k}: {v}\t')
                output_file.write(f'{k}: {v}\n')
    