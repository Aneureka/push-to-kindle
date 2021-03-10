import math

from googletrans import Translator

_translator = Translator(service_urls=["translate.google.cn"])


def translate(text, src="zh-CN", dest="en"):
    return _translator.translate(text, src=src, dest=dest).text


def convert_file_size_to_mb(size_bytes):
    return math.ceil(size_bytes / math.pow(1024, 2))
