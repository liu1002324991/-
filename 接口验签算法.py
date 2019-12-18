import hashlib
def signture(data):
    datalist = []
    for key in sorted(data):
        if data[key]:
            datalist.append('%s=%s' % (key, data[key]))
    i = '&'.join(datalist).strip()
    # print(i)
    i = i + 'SInsak45DIj'
    # print(i)
    sign = hashlib.md5(i.encode(encoding='UTF-8')).hexdigest()
    return hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()



