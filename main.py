import os


def Release(ver) -> str:
    release = ver.split()
    return release[0]


def ubuntu():#wo qv zhao yi xia docker
    files = open('/etc/apt/sources.list', 'w')
    sou = files.read()
    sou = sou.replace('archive.ubuntu.com','mirrors.aliyun.com')
    files.write(sou)
    files.close()
    return os.popen('apt update').read()



def debian():
    files = open('/etc/apt/sources.list', 'w')
    files.write('''deb http://mirrors.ustc.edu.cn/debian stable main contrib non-free
# deb-src http://mirrors.ustc.edu.cn/debian stable main contrib non-free
deb http://mirrors.ustc.edu.cn/debian stable-updates main contrib non-free
# deb-src http://mirrors.ustc.edu.cn/debian stable-updates main contrib non-free
''')
    files.close()
    return os.popen('apt update').read()







if os.popen('whoami').read() == 'root\n':
    ver = os.popen('cat /etc/issue').read()
    if Release(ver) == 'Ubuntu':
        print(ubuntu())
    if Release(ver) == 'Debian':
        print(debian())
else:
    print('请用root用户运行此脚本(sudo亦可)')
