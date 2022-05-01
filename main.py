import os


def Release(ver) -> str:
    release = ver.split()
    return release[0]


def ubuntu():
    files = open('/etc/apt/sources.list', 'w')
    files.write('''deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse
deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
# deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse
''')
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
