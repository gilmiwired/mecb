import matplotlib
from wordcloud import WordCloud

# テキストファイル読み込み
text = open("test.txt", encoding="utf8").read()
 
print(matplotlib.matplotlib_fname())

# 画像作成
wordcloud = WordCloud(max_font_size=40).generate(text)
 
# 画像保存
wordcloud.to_file("result.png")