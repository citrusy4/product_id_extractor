"""
tmall: https://detail.tmall.com/item.htm?id=<product_id>
taobao: https://item.taobao.com/item.htm?id=<product_id>
jd: https://item.jd.com/<product_id>.html
suning: https://product.suning.com/<product_id>.html
amazon: https://www.amazon.co.uk/dp/<product_id>
"""
import re

from config import Config

rules = Config.RULES


def extract(url, platform=None):
    if not url:
        return None
    if not platform:
        return auto_extractor(url)
    elif platform in ["tmall", "taobao"]:
        return tmall_taobao_extractor(url)
    elif platform in ["jd", "suning"]:
        return jd_suning_extractor(url)
    elif platform == "amazon":
        return amazon_extractor(url)


def tmall_taobao_extractor(url):
    reg = re.search(rules["tmall_taobao"], url)
    return reg[0][3:] if reg else None


def jd_suning_extractor(url):
    reg = re.search(rules["jd_suning"], url)
    tail_len = len(reg[0]) - 5
    return reg[0][:tail_len] if reg else None


def amazon_extractor(url):
    reg = re.search(rules["amazon"], url)
    return reg[0][3:] if reg else None


def auto_extractor(url):
    for k, v in rules.items():
        reg = re.search(v, url)
        if reg and (k in ["tmall_taobao", "amazon"]):
            return reg[0][3:]
        elif reg and (k == "jd_suning"):
            tail_len = len(reg[0]) - 5
            return reg[0][:tail_len]
    return None


# print(
#     extract(
#         "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.36.2eb95890xw17AZ&id=631170154012&skuId=4491513952636&user_id=3015107655&cat_id=2&is_b=1&rn=a7d765eb30541ad8ac679098f60cd09b",
#         "tmall",
#     )
# )
# print(extract("https://detail.tmall.com/item.htm?id=631170154012", "tmall"))
# print(
#     extract(
#         "https://item.taobao.com/item.htm?spm=a230r.1.14.292.122424993PEmM9&id=633473711556&ns=1&abbucket=16#detail",
#         "taobao",
#     )
# )
# print(extract("https://item.taobao.com/item.htm?id=633473711556", "taobao"))
# print(
#     extract(
#         "https://product.suning.com/0000000000/12200002748.html#?srcpoint=shouji_phone2018_103808426459_prod03&safp=d488778a.phone2018.103808426459.3&safc=prd.0.0&safpn=10003.00006&ch=cu",
#         "suning",
#     )
# )
# print(extract("https://product.suning.com/12200002748.html", "suning"))
# print(extract("https://item.jd.com/68372477001.html#crumb-wrap", "jd"))
# print(extract("https://item.jd.com/68372477001.html", "jd"))
# print(
#     extract(
#         "https://www.amazon.co.uk/The-Secret-Garden-DVD/dp/B08L48FBLL/ref=tmm_dvd_swatch_0?_encoding=UTF8&qid=&sr=",
#         "amazon",
#     )
# )
# print(extract("https://www.amazon.co.uk/The-Secret-Garden-DVD/dp/B08L48FBLL", "amazon"))
# print(extract("https://www.amazon.co.uk/dp/B08L48FBLL", "amazon"))


# print(
#     extract(
#         "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.36.2eb95890xw17AZ&id=631170154012&skuId=4491513952636&user_id=3015107655&cat_id=2&is_b=1&rn=a7d765eb30541ad8ac679098f60cd09b",
#     )
# )
# print(extract("https://detail.tmall.com/item.htm?id=631170154012"))
# print(
#     extract(
#         "https://item.taobao.com/item.htm?spm=a230r.1.14.292.122424993PEmM9&id=633473711556&ns=1&abbucket=16#detail"
#     )
# )
# print(extract("https://item.taobao.com/item.htm?id=633473711556"))
# print(
#     extract(
#         "https://product.suning.com/0000000000/12200002748.html#?srcpoint=shouji_phone2018_103808426459_prod03&safp=d488778a.phone2018.103808426459.3&safc=prd.0.0&safpn=10003.00006&ch=cu",
#     )
# )
# print(extract("https://product.suning.com/12200002748.html"))
# print(extract("https://item.jd.com/68372477001.html#crumb-wrap"))
# print(extract("https://item.jd.com/68372477001.html"))
# print(
#     extract(
#         "https://www.amazon.co.uk/The-Secret-Garden-DVD/dp/B08L48FBLL/ref=tmm_dvd_swatch_0?_encoding=UTF8&qid=&sr="
#     )
# )
# print(extract("https://www.amazon.co.uk/The-Secret-Garden-DVD/dp/B08L48FBLL"))
# print(extract("https://www.amazon.co.uk/dp/B08L48FBLL"))