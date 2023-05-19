import math
import sys
import lxml.html
import readability
import requests
import pprint

def main():
  val = float(sys.argv[1])
  print(math.radians(val))

def get_content(html):
  """
  HTMLの文字列から (タイトル, 本文) のタプルを取得する。
  """

  document = readability.Document(html)
  content_html = document.summary()
  # HTMLタグを除去して本文のテキストのみを取得する。
  content_text = lxml.html.fromstring(content_html).text_content().strip()
  # pprint.pprint(dir(document))
  # pprint.pprint(vars(obj))


  short_title = document.short_title()
  return short_title, content_text


if __name__ == "__main__":
  dummy_user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

  obj = requests.get(
    'https://www.fdic.gov/news/press-releases/2023/pr23034.html', 
    headers={"User-Agent": dummy_user_agent}
  )
  title,content = get_content(obj.content)
  print(title)
  print(content)
