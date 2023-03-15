import os
import pandas as pd
import re
from collections import Counter
import pandas as pd

path=r"E:\TranslateWords_Challenge"

# Change the directory
os.chdir(path)

def read_files(file_path):
    #Open file
    with open(file_path, 'r',encoding='utf-8') as file:
        return file.read().split('\n')

def Read_df(file_path):
    #Read a comma-separated values (csv) file into DataFrame.
    df=pd.read_csv(file_path,names=('English_Word','French_Word'))
    return df
    

def Process(en,df,fw):
    Dict={eng:fra for eng,fra in zip(df['English_Word'].to_list(),df['French_Word'].to_list())}
    #Elements are stored as dictionary keys and their counts are stored as dictionary values.
    fw=Counter(fw)
    with open('t8.shakespeare.translated.txt','w+') as f:
        for line in en:
            for word in line.split():
                word=word.lower()
                spl_rem=re.sub('\W+','',word)
                if not(bool(re.search('^[a-zA-Z0-9]*$',word))==True) and spl_rem in Dict.keys():
                    spl=''
                    for char in word:     
                        if char.isalpha():
                            spl+='x'
                        else:
                            spl+=char
                    f.write(spl.replace('x'*spl.count('x'),Dict[spl_rem])+" ")    
                    fw.update([spl_rem])
                elif word in Dict.keys():
                    f.write(Dict[word]+" ")
                    fw.update([spl_rem])
                else:
                    f.write(word+" ")
            f.write('\n')
        f.close()
        print()
        df['Frequency']=list(dict(fw).values())
        df.to_csv('frequency.csv')
        
def All_method():
    find_word=read_files('find_words.txt')
    en=read_files('t8.shakespeare.txt')
    en_to_fr=read_files('french_dictionary.csv')
    df=Read_df('french_dictionary.csv')
    Process(en,df,find_word)

All_method()