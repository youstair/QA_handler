# -*- coding: gbk -*-

import jieba
import pyltp
from pyltp import SentenceSplitter # �־�
from pyltp import Segmentor # �ִ�
from pyltp import Postagger # ���Ա�ע
from pyltp import NamedEntityRecognizer # ����ʵ��ʶ��
from pyltp import Parser #����䷨����
from pyltp import SementicRoleLabeller
import collections
import line_class
import re
from jieba import posseg


model_path = "MODELS/ltp_data_v3.4.0/"


Word = collections.namedtuple("Word","word postag netag arc_head arc_relation")
Triad = collections.namedtuple("Triad", "Ner1 Ner2 Relation")

segmentor = Segmentor()
segmentor.load(model_path+'cws.model')
postagger = Postagger()
postagger.load(model_path+'pos.model')
recognizer = NamedEntityRecognizer()
recognizer.load(model_path+'ner.model')
parser  = Parser()
parser.load(model_path+'parser.model')
print("xxx")

pattern = re.compile(r'(��.*?��)')



def nlp_(text):
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


    seg_text = list(segmentor.segment(text.strip()))
    pos = postagger.postag(seg_text)
    netag = recognizer.recognize(seg_text, pos)
    arc = parser.parse(seg_text, pos)
    one_sentence = []
    for h, i, j, k in list(zip(seg_text, pos, netag, arc)):
        word = Word(h, i, j, k.head, k.relation)
        one_sentence.append(word)

    # print(one_sentence)
    return one_sentence

    print("\n" * 3)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




if __name__ == '__main__':
    line = "��վ��������"
    nlp_(line)





