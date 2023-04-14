import zipfile
import argparse
from unrar import rarfile
import threading


def Argparse_Option():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', dest='rar_file', help='The Rar File To Brute')
    parser.add_argument('-z', dest='zip_file', help='The Zip File To Brute')
    parser.add_argument('-p', dest='pass_word', help='The Password File To use')
    arg = parser.parse_args()
    return arg


def ZipBrute(zfile, pwd):
    try:
        zfile.extractall(pwd=pwd.encode('utf-8'))
        print('\033[41;1m[*] Passw0rd Founded: %s\033[0m' % pwd)
    except RuntimeError:
        pass
    except Exception as e:
        print("\033[41;1m" + e + "\033[0m")


def RarBrute(rfile, pwd):
    try:
        pwd = pwd.strip()
        rfile.extractall(pwd=pwd)
        print('\033[41;1m[*] Passw0rd Founded: %s\033[0m' % pwd)
    except rarfile.BadRarFile:
        pass
    except Exception as e:
        print("\033[41;1m" + e + "\033[0m")


def main():
    pwds = []
    try:
        passwords = open(pwd_file, 'r')
        for pwd in passwords:
            pwd = pwd.strip()
            pwds.append(pwd)
    except:
        print("\033[41;1mCan't use the password file %s\033[0m" %pwd_file)

    if zip_file:
        try:
            zfile = zipfile.ZipFile(zip_file, 'r')
            for pwd in pwds:
                t = threading.Thread(target=ZipBrute, args=(zfile, pwd))
                t.start()
                t.join()
        except Exception:
            print("\033[41;1mCan't use the zip file %s\033[0m" % zip_file)

    if rar_file:
        try:
            rfile = rarfile.RarFile(rar_file, 'r')
            for pwd in pwds:
                t = threading.Thread(target=RarBrute, args=(rfile, pwd))
                t.start()
                t.join()
        except:
            print("\033[41;1mCan't use the rar file %s\033[0m" % rar_file)

if __name__ == '__main__':
    print('''
         __  __      _____ __   ____             _       
        |  \/  |_   |_   _/ /_ | __ ) _ __ _   _| |_ ___ 
        | |\/| | | | || || '_ \|  _ \| '__| | | | __/ _ \\
        | |  | | |_| || || (_) | |_) | |  | |_| | ||  __/
        |_|  |_|\__,_||_| \___/|____/|_|   \__,_|\__\___|
    ''')
    print('   Author:%s' % __author__)
    cmd = Argparse_Option()
    rar_file = cmd.rar_file
    zip_file = cmd.zip_file
    if not rar_file and not zip_file:
        print('\033[41;1mUsage: MuT6Brute.py [-h] [-r RAR_FILE] [-z ZIP_FILE] [-p PASS_WORD]\033[0m')
        exit()
    pwd_file = cmd.pass_word
    main()
