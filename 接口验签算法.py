#导包
import hashlib
#定义函数
def signture(data):
    datalist = []
    #按照键名对关联数组进行升序排序
    for key in sorted(data):
        if data[key]:
            #datalist列表里添加'='号
            datalist.append('%s=%s' % (key, data[key]))
    #列表之间添加'&'并且删除左右边的空格
    i = '&'.join(datalist).strip()
    # print(i)
    #参数加盐  盐值为'SInsak45DIj'
    i = i + 'SInsak45DIj'
    # print(i)
    #第一次md5加密
    sign = hashlib.md5(i.encode(encoding='UTF-8')).hexdigest()
    #第二次md5加密，并且返回
    return hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()



