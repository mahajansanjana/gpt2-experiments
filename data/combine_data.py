import pandas as pd
import re
import gensim
import string
import nltk.data

df = pd.read_csv('reports.csv').dropna()

def remove_html(text):
    """Remove html tags from a string"""
    return re.sub(r'<.*?>', r'', text)

def remove_hex(text): 
    """Remove hex codes from a string""" 
    return re.sub(r'&.*?;', r'', text) 

def clean(text):
    text = remove_html(text)
    text = remove_hex(text)
    return text

df['text'] = df['text'].map(lambda text: clean(text))

# Combine all reports into one large corpus
combined = '' 
for text in df['text']:
    combined += text
    #combined += '\n' 

def save(s, filename):
    file = open(filename, 'w')
    file.write(s)
    file.close()
    
save(combined, 'reports.txt')