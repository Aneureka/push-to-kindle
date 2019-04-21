from googletrans import Translator


_translator = Translator(service_urls=[
      'translate.google.cn'
])

def translate(text, src='zh-CN', dest='en'):
    return _translator.translate(text, src=src, dest=dest).text