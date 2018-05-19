import argparse
from ftplib import FTP
import csv

# LOCAL_FILE_PATH = "/home"
LOCAL_FILE_PATH = "/Users/oec/Documents/Icebox/data"


def ftp_handler():
    f = get_args()
    files = get_file_path(f)
    for f in files:
        get_file(f[0], f[1], f[2])


def get_args():
    parser = argparse.ArgumentParser('Define input file path.')
    # 位置引数'file'を定義
    parser.add_argument('file')
    args = parser.parse_args()
    return args.file


def get_file_path(files):
    lst = []
    with open(files, "r") as input_f:
        reader = csv.reader(input_f, delimiter=',')
        header = next(reader)
        for row in reader:
            lst.append(row)
    return lst


def get_file(url, path, name):
    print(url)
    ftp = FTP(url)
    ftp.login()
    ftp.cwd(path)

    with open(LOCAL_FILE_PATH + "/" + name, 'wb') as f:
        pass
        #ftp.retrbinary('RETR %s' % name, f.write)


ftp_handler()