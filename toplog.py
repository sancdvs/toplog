import datetime

log = ''
s = ''
def wlog(s):
    with open(log,'r+') as f:
        content = f.read()
        f.seek(0)
        s = str(datetime.datetime.now())+'\r'+s+'\r'
        f.write(s+'\n'+content)
