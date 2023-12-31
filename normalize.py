import re

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = dict()

for cyrillic, latin in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyrillic)] = latin
    TRANS[ord(cyrillic.upper())] = latin.upper()

def normalize(name: str) -> str:
    if '.' in name:
        position = name.index('.')
        translate_name = re.sub(r'\W', '_', name)
        translate_name = translate_name[:position]+'.'+translate_name[position+1:]
        translate_name = translate_name.translate(TRANS)
    else:
         translate_name = re.sub(r'\W', '_', name.translate(TRANS))
    return translate_name

