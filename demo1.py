import re
from string import punctuation as pun_en
from zhon.hanzi import punctuation as pun_zh
symbol = pun_zh + pun_en
line = '拜占庭式建筑讲的就是华丽丽！ '
line1 = ' '
line2 = ' '
print(ord(line1))
print(ord(line2))
a = list(line)
print(a[-1])

line = re.sub(r'\s+', ' ', line)
line = re.sub(r'[\s]$', '', line)

if line[-1] not in symbol:
    print('666666')
#line = re.sub("(?P<field1>[^%&',;=?$\x22])(?P<field2>\s)", r"\g<field1>", line)
#line = re.sub(r"""(?P<field1>[！|？|，|。|,|.|!|?])(?P<field2>\s)""", r"\g<field1>", line)

print(line)