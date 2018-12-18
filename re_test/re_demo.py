import re
"""
a = "133、149、153、173、177、180、181、189、199、130、131、132、145、155、156、166、171、175、176、185、186、134(0-8)、135、136、137、138、139、147、150、151、152、157、158、159、172、178、182、183、184、187、188、198"
print(re.findall(r"18.",a))
print(re.findall(r"17.",a))
print(re.findall(r"16.",a))
print(re.findall(r"15.",a))
print(re.findall(r"14.",a))
print(re.findall(r"13.",a))
def judge_phone(phone):
    pat = "^1(([3578][0-9])|(47))\d{8}$"
    ret = re.search(pat,phone)
    return ret
print(judge_phone("17602515236"))
print(judge_phone("17502515236"))
print(judge_phone("147u2515236"))
print(judge_phone("1760251523"))
print(judge_phone("176025152f6"))
print(judge_phone("189623820955"))
"""
"""
def judge_qq(qq):
    return re.search(r"^\d{6,10}$",qq)

print(judge_qq("2993048475"))
print(judge_qq("29930asdfag8475"))
print(judge_qq("2475"))
print(judge_qq("2993048475134"))
print(judge_qq("29930484751241512q412"))
print(judge_qq("a299304847"))
"""
def judge_mail(mail):
    return re.search(r"^[0-9a-zA-Z]{1,16}@[0-9a-zA-Z]{1,8}\.[a-z]{2,3}$",mail)

print(judge_mail("2993048475@q.com@qq.com"))
print(judge_mail("2993#48475@qq.com"))
print(judge_mail("2993048475#qq.com"))
print(judge_mail("2993048475@qq."))
print(judge_mail("2993048475@.com"))
print(judge_mail("@qq.com"))
print(judge_mail("2993048475qq.com"))
