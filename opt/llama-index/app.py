from dotenv import load_dotenv
load_dotenv()

from llama_index import SimpleWebPageReader
from llama_index import Document
from llama_index import GPTListIndex, GPTVectorStoreIndex
import csv
import logging
import sys
import openai

# ログ出す時に使う
# logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


def getFromCsv():
    article_urls = []
    with open('./article.csv') as f:
      reader = csv.reader(f)
      for row in reader:
        article_urls.append(row[0])

    print(article_urls)
    return article_urls

def getHeaddingText():
   return [
"ChatGPTの概要とその技術的な特徴",
"ChatGPTがもたらす可能性とその活用例",
"AIチャットくんの紹介",
"AIチャットくんとは？",
"AIチャットくんが提供するサービスの概要",
"AIチャットくんの開発背景と目指すビジョン",
"AIチャットくんの特徴",
"ChatGPTを活用したAIチャットくんの特徴",
"AIチャットくんのユニークな機能とその利点",
"AIチャットくんの利用者数とその成長",
"AIチャットくんの使い方",
"AIチャットくんの登録方法と基本的な使い方",
"AIチャットくんの操作ガイドとヒント",
"AIチャットくんの活用シーン",
"AIチャットくんを活用する具体的なシーンと例"
"AIチャットくんを活用したユーザーの声",
"AIチャットくんの有料プランとそのメリット",
"AIチャットくんの有料プランの詳細",
"有料プランのメリットとその価値",
"AIチャットくんの音声入力機能",
"AIチャットくんの音声入力機能の紹介",
"音声入力機能を活用するメリット",
"AIチャットくんの専用アプリ",
"AIチャットくんの専用アプリの紹介",
"専用アプリの利用メリットとその特徴",
"ChatGPTとAIチャットくんの可能性についてのまとめ",
"ChatGPTとAIチャットくんの将来的な可能性",
"AIチャットくんの今後の展開予想",
"AIチャットくんについてのよくある質問とその回答",
"AIチャットくんに関するよくある質問とその回答",
]


# documents = SimpleWebPageReader(html_to_text=True).load_data(["https://www.businessinsider.jp/post-270018"])

documents = SimpleWebPageReader(html_to_text=True).load_data(getFromCsv())

index = GPTVectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

headdings = getHeaddingText()

for heading in headdings:
    response = query_engine.query(heading)
    print(heading)

    messageText = "system: You are a ai-savvy writer. Please use the following CONCEPT to write the answer of QUESTION with Japanese. CONCEPT: {} QUESTION: {} Answer:";

    messageContent = messageText.format(response.response, heading)


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": messageContent},
        ],
    )
    print(response.choices[0]["message"]["content"].strip())
