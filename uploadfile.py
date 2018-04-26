from fileupload import *
ssh.connect('172.23.135.126', username="pi", password="Delta123")
ssh.connect('172.23.135.126', username="pi", password="Delta123")
sftp = ssh.open_sftp()
localpath = '/home/pi/Downloads/vip.txt'
remotepath = '/home/pi/Downloads/Project/vip.txt'
sftp.put(localpath, remotepath)
sftp.close()
ssh.close()
