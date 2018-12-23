# -*- coding: utf-8 -*-

#
# Wordless: Testing for POS Tagging
#
# Copyright (C) 2018 Ye Lei (叶磊) <blkserene@gmail.com>
#
# License Information: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#

import sys

from PyQt5.QtCore import *

import jpype
import pyhanlp

sys.path.append('E:/Wordless')

from wordless_text import wordless_text_processing
from wordless_settings import init_settings_default, init_settings_global

main = QObject()

init_settings_default.init_settings_default(main)
init_settings_global.init_settings_global(main)

main.settings_custom = main.settings_default

main.crf_analyzer = jpype.JClass('com.hankcs.hanlp.model.crf.CRFLexicalAnalyzer')()
main.perceptron_analyzer = jpype.JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')()

# Chinese (Simplified)
sentence_zho_cn = '作为语言而言，为世界使用人数最多的语言，目前世界有五分之一人口做为母语。'

print('Chinese / jieba:')

tokens_tagged = wordless_text_processing.wordless_pos_tag(main, [sentence_zho_cn], 'zho_cn',
                                                          pos_tagger = 'jieba')
tokens_tagged_universal = wordless_text_processing.wordless_pos_tag(main, [sentence_zho_cn], 'zho_cn',
                                                                    pos_tagger = 'jieba',
                                                                    tagset = 'Universal')

print(f"\t{tokens_tagged}")
print(f"\t{tokens_tagged_universal}")

print('Chinese / HanLP - CRF Lexical Analyzer:')

tokens_tagged = wordless_text_processing.wordless_pos_tag(main, [sentence_zho_cn], 'zho_cn',
                                                          pos_tagger = 'HanLP - CRF Lexical Analyzer')
tokens_tagged_universal = wordless_text_processing.wordless_pos_tag(main, [sentence_zho_cn], 'zho_cn',
                                                                    pos_tagger = 'HanLP - CRF Lexical Analyzer',
                                                                    tagset = 'Universal')

print(f"\t{tokens_tagged}")
print(f"\t{tokens_tagged_universal}")

print('Chinese / HanLP - Perceptron Lexical Analyzer:')

tokens_tagged = wordless_text_processing.wordless_pos_tag(main, [sentence_zho_cn], 'zho_cn',
                                                          pos_tagger = 'HanLP - Perceptron Lexical Analyzer')
tokens_tagged_universal = wordless_text_processing.wordless_pos_tag(main, [sentence_zho_cn], 'zho_cn',
                                                                    pos_tagger = 'HanLP - Perceptron Lexical Analyzer',
                                                                    tagset = 'Universal')

print(f"\t{tokens_tagged}")
print(f"\t{tokens_tagged_universal}")

# English
sentence_eng = 'English is a West Germanic language that was first spoken in early medieval England and eventually became a global lingua franca.'

print('English / NLTK - Perceptron POS Tagger:')

tokens_tagged = wordless_text_processing.wordless_pos_tag(main, [sentence_eng], 'eng',
                                                          pos_tagger = 'NLTK - Perceptron POS Tagger')
tokens_tagged_universal = wordless_text_processing.wordless_pos_tag(main, [sentence_eng], 'eng',
                                                                    pos_tagger = 'NLTK - Perceptron POS Tagger',
                                                                    tagset = 'Universal')

print(f"\t{tokens_tagged}")
print(f"\t{tokens_tagged_universal}")

# Japanese
sentence_jpn = '使用人口について正確な統計はないが、日本国内の人口、および日本国外に住む日本人や日系人、日本がかつて統治した地域の一部住民など、約1億3千万人以上と考えられている[7]。'

print('Japanese / nagisa:')

tokens_tagged = wordless_text_processing.wordless_pos_tag(main, [sentence_jpn], 'jpn',
                                                          pos_tagger = 'nagisa')
tokens_tagged_universal = wordless_text_processing.wordless_pos_tag(main, [sentence_jpn], 'jpn',
                                                                    pos_tagger = 'nagisa',
                                                                    tagset = 'Universal')

print(f"\t{tokens_tagged}")
print(f"\t{tokens_tagged_universal}")

# Russian
sentence_rus = 'Ру́сский язы́к ([ˈruskʲɪi̯ jɪˈzɨk] Информация о файле слушать)[~ 3][⇨] — один из восточнославянских языков, национальный язык русского народа. '

print('Russian / NLTK - Perceptron POS Tagger:')

tokens_tagged = wordless_text_processing.wordless_pos_tag(main, [sentence_rus], 'rus',
                                                          pos_tagger = 'NLTK - Perceptron POS Tagger')
tokens_tagged_universal = wordless_text_processing.wordless_pos_tag(main, [sentence_rus], 'rus',
                                                                    pos_tagger = 'NLTK - Perceptron POS Tagger',
                                                                    tagset = 'Universal')

print(f"\t{tokens_tagged}")
print(f"\t{tokens_tagged_universal}")