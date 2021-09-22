# coding = utf-8

import os
from ftplib import FTP


class Load_cfg:
    def __init__(self,file):
        f=open(file)
        self.host_name=f.readline().strip('\n').split(']')[1]
        self.host_port=f.readline().strip('\n').split(']')[1]
        self.host_user=f.readline().strip('\n').split(']')[1]
        self.host_password=f.readline().strip('\n').split(']')[1]
        self.local_path=f.readline().strip('\n').split(']')[1]
        self.remote_path=f.readline().strip('\n').split(']')[1]
        self.remote_file=f.readline().strip('\n').split(']')[1]

        f.close()


class MyFtp:

    ftp = FTP()

    def __init__(self,host,port=21):
        self.ftp.connect(host,port)

    def login(self,username,pwd):
        # self.ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
        self.ftp.login(username,pwd)
        # print(self.ftp.welcome)

    def downloadFile(self,localpath,remotepath,filename):
        os.chdir(localpath)   # 切换工作路径到下载目录
        self.ftp.cwd( remotepath)   # 要登录的ftp目录
        # self.ftp.nlst()  # 获取目录下的文件
        file_handle = open(filename,"wb").write   # 以写模式在本地打开文件
        self.ftp.retrbinary('RETR %s' % os.path.basename(filename),file_handle,blocksize=1024)  # 下载ftp文件
        # ftp.delete（filename）  # 删除ftp服务器上的文件

    def close(self):
        # self.ftp.set_debuglevel(0)  # 关闭调试
        self.ftp.quit()


if __name__ == '__main__':
    cfg=Load_cfg('config.ini')

    str_ORG = input('请输入机构号：')
    str_ID = input('请输入柜员号：')

    remote_file=str_ORG + str_ID


    ftp = MyFtp(cfg.host_name)
    ftp.login(cfg.host_user,cfg.host_password) 
    ftp.downloadFile(cfg.local_path,cfg.remote_path,remote_file)
    ftp.close()




