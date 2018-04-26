import ftplib
import os
import os
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('172.23.135.126', username="pi", password="Delta123")
sftp = ssh.open_sftp()
localpath = '/home/pi/Downloads/vip.txt'
remotepath = '/home/pi/Downloads/vip.txt'
sftp.put(localpath, remotepath)
sftp.close()
ssh.close()
