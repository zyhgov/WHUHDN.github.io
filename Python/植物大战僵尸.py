print("\t\t\t植物大战僵尸")
print("*"*45)
import time
incomplete_sign=50
print('='*23+'开始下载'+'='*25)
for i in range(incomplete_sign+1):
    completed="*"*i
    incomplete="."*(incomplete_sign-i)
    percentage=(i/incomplete_sign)*100
    print("\r{:.0f}%[{}{}]".format(percentage,completed,incomplete),end="")
    time.sleep(0.5)
print("\n"+'='*23+'下载完成'+'='*25)