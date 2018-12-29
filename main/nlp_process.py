# -*- coding: gbk -*-

import jieba
import re
from jieba import posseg
import nn


p = re.compile('<[^>]+>')
q = "[A~Z]"
model_path = "MODELS/ltp_data_v3.4.0/"


def rule_1(line,pos_list,rowQ):
    """
    以”参考手册“结尾，或者以问号结尾，比较容易获取的一些
    :param line:
    :param pos_list:
    :param rowQ
    :return q :
    """



    if (line.endswith("参考手册")):
        q  = "有哪些" + line.replace("参考手册", "")
        q = rowQ[-2] + q
        return q
    elif (line.endswith("？") or line.endswith("?") or line.endswith("吗")):
        q  = line
        q = rowQ[-2] + q
        return q
    return None



def rule_2(line,pos_list,rowQ):
    """

    :param line:
    :param pos_list:
    :param rowQ
    :return:
    """


    if(len(pos_list) == 1):
        if(rowQ[-2].lower().find(line.lower()) == -1):
            return rowQ[-2] + line
        else:
            return rowQ[-2]

    return None

def rule_3(line,pos_list,rowQ):
    """
    利用pyltp做一些基本的分析
    :param line:
    :param pos_list:
    :param rowQ:
    :return:
    """



    sentence = nn.nlp_(line)
    if(sentence == None):
        return None
    else:
        HED = None
        for i in sentence:
            if(i.arc_relation == 'HED'):
                HED = i

        if(HED.postag == 'v'):
            q = "如何"+line
        elif(HED.postag == 'n' or HED.postag == 'nz'):
            q = line
        else:
            q = line



    if(q.lower().replace(" ","").find(rowQ[-2].lower().replace(" ","")) != -1):
        return q
    elif(rowQ[-2].lower().replace(" ","").find(q.lower().replace(" ","")) != -1):
        return rowQ[-2]
    else:
        return rowQ[-2] + q




def get_question_by_rowQ1(rowQ):
    # print(rowQ)
    # print(rowQ)
    line = p.sub("",rowQ[-1]).replace("\n","")
    # line = rowQ[-2] + p.sub("",line).replace("\n","")
    pos_list = posseg.lcut(line)
    question = ""
    if(rule_1(line,pos_list,rowQ) != None):
        question = rule_1(line,pos_list,rowQ)
    elif(rule_2(line,pos_list,rowQ) != None):
        question = rule_2(line,pos_list,rowQ)
    else:
        # question = line
        # print(rowQ)
        # print("x")
        question = rule_3(line,pos_list,rowQ)

    question = question.lower()
    if(question.find(rowQ[0].lower()) == -1):
        question = rowQ[0].lower()+" "+question

    # print(question)
    # print("~~~"*30)


    return question

def get_question_by_rowQ(rowQ):
    question = []
    for i in rowQ:
        i = i.lower().replace("\n","")
        for j in jieba.lcut(i):
            if(j not in question):
                question.append(j)

    q = "".join(question).replace("参考书册","")


    return q

if __name__ == '__main__':
    with open("rowQ.txt","r") as f:
        for i in f.readlines():
            rowQ = i.split('^')
            get_question_by_rowQ(rowQ)