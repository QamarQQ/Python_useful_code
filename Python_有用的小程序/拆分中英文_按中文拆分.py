In [7]: #coding=utf-8
   ...: import re
   ...: s = 'hi新手oh'
   ...: #举个栗子是字符串s，为了匹配下文的unicode形式，所以需要解码
   ...: p = re.compile(r'[\u4e00-\u9fa5]') #这里是精髓，[\u4e00-\u9fa5]是匹配所有中文的正则，因为是unicode形式，所以也
   ...: 要转为ur
   ...:
   ...: print(p.split(s)) #使用re库的split切割