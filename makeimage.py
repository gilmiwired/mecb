import MeCab
import ipadic
from wordcloud import WordCloud
# 解析したい文章
text = "みかんは好きだけどオレンジを食べたいときもある。だけどみかんは栄養もあるし、みかんは小さいころから食べていたから、オレンジよりもみかんが好きだ。"

#単語の分割
m = MeCab.Tagger (ipadic.MECAB_ARGS)

# 形態素解析
node = m.parseToNode(text)
words=[]
word=""
while node:
    # node.feature：CSVで表記された素性情報を取得
    # print(node.feature)
    hinshi = node.feature.split(",")[0]
    print(hinshi)
    if hinshi in ["名詞","動詞","形容詞"]:
        origin = node.feature.split(",")[6]
        word = word + " " + origin   
    node = node.next  # 書き忘れると無限ループになるので注意

# wordcloudで可視化
fpath = "./ipaexg.ttf"
wordcloud = WordCloud(background_color="white",font_path="C:\Windows\Fonts\BIZ-UDGothicB.ttc", width=600,height=400,min_font_size=15)
wordcloud.generate(word)

wordcloud.to_file("./wordcloud.png")