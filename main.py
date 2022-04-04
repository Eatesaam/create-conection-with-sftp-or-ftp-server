import pysftp
from ftplib import FTP_TLS
import os
import json

Host = ""
Username = ""
Password = ""
cnopts = pysftp.CnOpts() 
cnopts.hostkeys = None 

def get_sftp_connection():
    sftp = pysftp.Connection(host=Host,username=Username,password=Password,cnopts=cnopts)
    if(sftp):
        print("connection esatablished successfully")
    else:
        print("connection not established")

    return sftp



def get_ftp_connection():
    ftps = FTP_TLS(Host)
    ftps.login(Username, Password)
    ftps.prot_p()
    if(ftps):
        print("connection esatablished successfully")
    else:
        print("connection not established")

    return ftps


def main():
    conn = get_sftp_connection()
    print(conn)


if __name__ == '__main__':
    main()