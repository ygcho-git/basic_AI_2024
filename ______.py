# 문제 : 함수 정의하기
# trans_lang("en", "hello") --> "안녕하세요" 리턴
# trans_lang("ko", "안녕하세요") --> "Hello" 리턴

from transformers import pipeline

# 번역 파이프라인
translator = pipeline("translation", model="facebook/m2m100_418M", tokenizer="facebook/m2m100_418M")

def trans_lang(src_lang, src_text) :
    if src_lang == "ko" :
        translated = translator(src_text, src_lang="ko", tgt_lang="en")
        return translated[0]['translation_text']
    else :
        translated = translator(src_text, src_lang="en", tgt_lang="ko")
        return translated[0]['translation_text']

lang = "ko"
text = "안녕하세요"
translated = trans_lang(lang, text)
translated
