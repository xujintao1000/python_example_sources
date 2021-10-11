"""创建一个从单词到其出现情况的映射"""

# 1 提取 word 出现的情况，如果还没有它的记录，返回 []。 2 把单词新出现的位置添加到列表的后面。
# 3 把新的列表放回字典中，这又牵扯到一次查询操作。
# 4 sorted 函数的 key= 参数没有调用 str.uppper，而是把这个方
# 法的引用传递给 sorted 函数，这样在排序的时候，单词会被规范成统
# 一格式

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            # this is ugly; coded like this to make a point
            occurrences = index.get(word, [])  # <1>
            occurrences.append(location)       # <2>
            index[word] = occurrences          # <3>

# print in alphabetical order
for word in sorted(index, key=str.upper):  # <4>
    print(word, index[word])
# END INDEX0

