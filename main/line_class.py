import pyltp
import jieba
import collections
from pyltp import SentenceSplitter # 分句
from pyltp import Segmentor # 分词
from pyltp import Postagger # 词性标注
from pyltp import NamedEntityRecognizer # 命名实体识别
from pyltp import Parser #依存句法分析
from pyltp import SementicRoleLabeller

Word = collections.namedtuple("Word","word postag netag arc")

class sentence():
    def __init__(self):
        self.Words = []
    def __add__(self, other):
        self.Words.append(other)
    def add(self,other):
        self.Words.append(other)
    def __repr__(self):
        return str(self.Words)+'\n'
    def __getitem__(self, item):
        return self.Words[item]
    def __len__(self):
        return len(self.Words)
    def index(self,obj):
        return self.Words.index(obj)

class paragraph():
    def __init__(self):
        self.Lines = []
    def __add__(self, other):
        self.Lines.append(other)
    def add(self, other):
        self.Lines.append(other)
    def __repr__(self):
        return str(self.Lines)
    def __getitem__(self, item):
        return self.Lines[item]
    def __len__(self):
        return len(self.Lines)


class Triad():
    def __init__(self,ner1,ner2,activity,addition):
        self.ner1 = ner1
        self.ner2 = ner2
        self.activity = activity
        self.addition = addition
    def __repr__(self):
        return "((%s, %s) %s,%s)"%[self.ner1, self.ner2,self.activity, self.addition]



def get_ner_tree(word, line):
    """
    获取一个词作为根在句子中的所有节点
    :param word:
    :param line:
    :return:
    """

    nodes = []
    nodes.append(line.index(word)+1)
    for i in nodes:
        for w in line:
            if(w.arc_head == i):
                nodes.append(line.index(w) + 1)

    nodes.sort()

    return nodes