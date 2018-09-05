import re
import os
from string import punctuation as pun_en
from zhon.hanzi import punctuation as pun_zh
from langconv import *
path = './attraction.txt'




def html_encode(line):

    line = re.sub(r'&amp;', "&", line)
    line = re.sub(r'&#215;', "×", line)
    line = re.sub(r'&times;', "×", line)
    line = re.sub(r'&deg;', "°", line)
    line = re.sub(r'&hellip;', "…", line)
    line = re.sub(r'&#249;', "ù", line)
    line = re.sub(r'&yen;', "¥", line)
    line = re.sub(r'&#160;', " ", line)
    line = re.sub(r'&ndash;', "–", line)
    line = re.sub(r'&ang;', "∠", line)
    line = re.sub(r'&xi;', "ξ", line)
    line = re.sub(r'&oline;', "‾", line)
    line = re.sub(r'&#176;', "°", line)
    line = re.sub(r'&hearts;', "♥", line)
    line = re.sub(r'&rarr;', "→", line)
    line = re.sub(r'&mdash;', "—", line)
    line = re.sub(r'&zwj;', "", line)
    line = re.sub(r'&sigma;', "σ", line)
    line = re.sub(r'&#128522;', "😊", line)
    line = re.sub(r'&theta;', "θ", line)
    line = re.sub(r'&nabla;', "∇", line)
    line = re.sub(r'&forall;', "∀", line)
    line = re.sub(r'&#30528;', "着", line)
    line = re.sub(r'&prime;', "′", line)
    line = re.sub(r'&mu;', "μ", line)
    line = re.sub(r'&tau;', "τ", line)
    line = re.sub(r'&macr;', "¯", line)
    line = re.sub(r'&ldquo;', "“", line)
    line = re.sub(r'&gamma;', "γ", line)
    line = re.sub(r'&larr;', "←", line)
    line = re.sub(r'&or;', "∨", line)
    line = re.sub(r'&bull;', "•", line)
    line = re.sub(r'&#172;', "¬", line)
    line = re.sub(r'&uarr;', "↑", line)
    line = re.sub(r'&lambda;', "λ", line)
    line = re.sub(r'&zwnj;', "", line)
    line = re.sub(r'&kappa;', "κ", line)
    line = re.sub(r'&#173;', "­", line)
    line = re.sub(r'&ordm;', "º", line)
    line = re.sub(r'&chi;', "χ", line)
    line = re.sub(r'&#39;', "'", line)
    line = re.sub(r'&piv;', "ϖ", line)
    line = re.sub(r'&#225;', "á", line)
    line = re.sub(r'&#180;', "´", line)
    line = re.sub(r'&epsilon;', "ε", line)
    line = re.sub(r'&rho;', "ρ", line)
    line = re.sub(r'&alpha;', "α", line)
    line = re.sub(r'&sect;', "§", line)
    line = re.sub(r'&lsquo;', "‘", line)
    line = re.sub(r'&#183;', "·", line)
    line = re.sub(r'&beta;', "β", line)
    line = re.sub(r'&#128051;', "🐳", line)
    line = re.sub(r'&ograve;', "ò", line)
    line = re.sub(r'&rdquo;', "”", line)
    line = re.sub(r'&rsquo;', "’", line)
    line = re.sub(r'&acute;', "´", line)
    line = re.sub(r'&#128557;', "😭", line)
    line = re.sub(r'&lowast;', "∗", line)
    line = re.sub(r'&oacute;', "ó", line)
    line = re.sub(r'&pi;', "π", line)
    line = re.sub(r'&gt;', ">", line)
    line = re.sub(r'&nbsp;', " ", line)
    line = re.sub(r'&#186;', "º", line)
    line = re.sub(r'&frasl;', "⁄", line)
    line = re.sub(r'&cap;', "∩", line)
    line = re.sub(r'&lt;', "<", line)
    line = re.sub(r'&Omega;', "Ω", line)
    line = re.sub(r'&darr;', "↓", line)
    line = re.sub(r'&#175;', "¯", line)
    line = re.sub(r'&omicron;', "ο", line)
    line = re.sub(r'&#233;', "é", line)
    line = re.sub(r"&iota;", "ι", line)
    line = re.sub(r'&#243;', "ó", line)
    line = re.sub(r'&#165;', "¥", line)
    line = re.sub(r'&omega;', "ω", line)
    line = re.sub(r'&quot;', '"', line)
    line = re.sub(r'&#128024;', "🐘", line) 
    line = re.sub(r'&not;', "¬", line) 
    line = re.sub(r'&radic;', "√", line)
    return line

def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line


def clean_space(line):

    line = line.strip('')
    line = re.sub(r'\s+', ' ', line)
    line = re.sub(r'[\s]$', '', line)
    line = re.sub(r'^[\s]', '', line)
    line = re.sub(r'\u200b', '', line)
    line = re.sub(r'[\u00A0\u2000-\u200F\u2028-\u202F\u205F-\u206F]+', ' ', line)
    #line = re.sub(r"""(?P<field1>[！|？|，|。|,|.|!|?|])(?P<field2>\s+)""", r"\g<field1>", line)
    return line

def clean_html(line):
    line = re.sub(r"(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]", "<url>", line)
    line = re.sub(r"www.[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]", "<url>", line)
    return line


def strQ2B(line):

    rstring = ""
    for uchar in line:
        inside_code = ord(uchar)
        if inside_code == 12288:
            inside_code = 32
        elif inside_code >= 65281 and inside_code <= 65374:
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring


def strB2Q(line):

    rstring = ""
    for uchar in line:
        inside_code = ord(uchar)
        if inside_code == 32:  # 半角空格直接转化
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:  # 半角字符（除空格）根据关系转化
            inside_code += 65248

        rstring += chr(inside_code)
    return rstring

class Judge:
    def __init__(self):
        self.flag = -1

    def is_number(self, str):
        if str.isdigit():
            self.flag = 1


    def is_ssssss(self, str):

        if str == '<ssssssssssss>\n':
            self.flag = 0


output_file_final = "./clean_final.txt"
if os.path.exists(output_file_final):
    os.remove(output_file_final)
file_write = open(output_file_final, encoding="UTF-8", mode="w")


symbol = pun_zh + pun_en

flag = 0
with open(path, encoding = 'utf-8') as f:
    judge = Judge()
    for line in f.readlines():
        if flag == 1:
            judge.is_ssssss(line)
            if judge.flag == 0:
                file_write.write('\n' + line)
                flag = 0
                continue
            line = re.sub(r'\n', '', line)
            string = cht_to_chs(line)
            string = clean_html(string)
            string = strQ2B(string)
            string = html_encode(string)
            string = clean_space(string)
            file_write.write(string)
            if string:
                if string[-1] not in symbol:
                    file_write.write('。')
                continue
            continue
        line = re.sub(r'\n', '', line)
        judge.is_number(line)
        file_write.write(line + '\n')
        if judge.flag == 1:
            flag = 1

