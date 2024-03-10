from transformers import MarianMTModel, MarianTokenizer

# src_text = [
# "哈囉 我現在在素可泰",
# "我昨天搭晚上9點的車",
# "早上4點的時候到這邊的巴士站",
# "我在車上遇到一個很好的阿姨",
# "她幫我叫計程車 就是摩托車",
# "載我到現在我住的這裡",
# "我剛剛其實已經睡了一覺",
# "可能去找點東西吃",
# "然後再去古城那邊逛一逛",
# "我剛才洗了頭",]

def zh2en(src_text):
    model_name = "Helsinki-NLP/opus-mt-zh-en"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))
    res = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]
    return res
