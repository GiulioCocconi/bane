"""
  This script was proposed by my friend "S0U1" to hack Joomla and WordPress sites:
  
  https://github.com/HLoTW/wordpressscan
  
  Thank you for your help bro <3
"""
import json, re, os, time, random, socket
import sys

reload(sys)
sys.setdefaultencoding('utf8')

Version = '0.2.0'  

try:
    import requests
except ImportError:
    print '---------------------------------------------------'
    print '[*] pip install requests'
    print '   [-] you need to install requests Module'
    sys.exit()

try:
    from colorama import Fore, Back, Style

    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    b = Fore.BLUE
    y = Fore.YELLOW
    m = Fore.MAGENTA
    res = Style.RESET_ALL

except ImportError:
    print '---------------------------------------------------'
    print '[*] pip install colorama'
    print '   [-] you need to install colorama Module'
    sys.exit()


class S0u1wp():
    def __init__(self):
        try:
            self.url = sys.argv[1]
        except IndexError:
            self.cls()
            self.print_logo()
            self.__option()
            sys.exit()
        if self.url.startswith('http://'):
            self.url = self.url.replace('http://', '')
        elif self.url.startswith("https://"):
            self.url = self.url.replace('https://', '')
        else:
            pass
        __kill_ip = self.url
        try:
            ip = socket.gethostbyname(__kill_ip)
            self.CheckWordpress = requests.get('http://' + self.url, timeout=5)
            if '/wp-content/' in self.CheckWordpress.text:
                self.cls()
                self.print_logo()
                print r + '    [' + y + '+' + r + ']' + w + ' URL      : ' + m + self.url
                print r + '    [' + y + '+' + r + ']' + w + ' IP Server: ' + m + ip
                print r + '    [' + y + '+' + r + ']' + w + ' Server   : ' + m + self.CheckWordpress.headers[
                    'server']
                self.UserName_Enumeration()
                self.CpaNel_UserName_Enumeration()
                self.Version_Wp()
                self.GeT_Theme_Name()
                self.GeT_PluGin_Name()
            else:
                self.cls()
                self.print_logo()
                self.Worng2()
                sys.exit()
        except socket.gaierror:
            self.cls()
            self.print_logo()
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' Something worng! target.com without / in end ' + y + ']'
            sys.exit()
        except requests.exceptions.ReadTimeout:
            self.cls()
            self.print_logo()
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' ConnectionError! Maybe server Down, Or your ip is blocked! ' + y + ']'

    def __option(self):
        try:
            print y + '---------------------------------------------------'
            print r + '    [' + y + '+' + r + ']' + w + ' usage: ' + g + '    [ ' \
                  + w + ' Python S0u1wp.py Domain.com ' + g + ']'
        except:
            pass

    def Worng(self):
        try:
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' Enter Valid Domain, We Cant Connect to Server ' + y + ']'
        except:
            pass

    def Worng2(self):
        try:
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' This WebSite Not WordPress! ' + y + ']'
        except:
            pass

    def print_logo(self):
        clear = "\x1b[0m"
        colors = [36, 32, 34, 35, 31, 37, 30, 33, 38, 39]

        x = """
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

 _          __  _____   _____   _____       ___   __   _  
| |        / / |  _  \ /  ___/ /  ___|     /   | |  \ | | 
| |  __   / /  | |_| | | |___  | |        / /| | |   \| | 
| | /  | / /   |  ___/ \___  \ | |       / / | | | |\   | 
| |/   |/ /    | |      ___| | | |___   / /  | | | | \  | 
|___/|___/     |_|     /_____/ \_____| /_/   |_| |_|  \_| 

       Coded By: S0u1 http://github.com/HLoTW/     
       Beta Testers: Ala, Vince, Protoxic 
    """
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.01)

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def UserName_Enumeration(self):
        _cun = 1
        Flag = True
        __Check2 = requests.get('http://' + self.url + '/?author=1', timeout=10)
        try:
            while Flag:
                GG = requests.get('http://' + self.url + '/wp-json/wp/v2/users/' + str(_cun), timeout=5)
                __InFo = json.loads(GG.text)
                if 'id' not in __InFo:
                    Flag = False
                else:
                    Usernamez = __InFo['name']
                    print r + '    [' + y + '+' + r + ']' + w + ' Wordpress Username: ' + m + Usernamez
                _cun = _cun + 1
        except:
            try:
                if '/author/' not in __Check2.text:
                    print r + '    [' + y + '+' + r + ']' + w + ' Wordpress Username: ' + r + 'Not FOund'
                else:
                    find = re.findall('/author/(.*)/"', __Check2.text)
                    username = find[0].strip()
                    if '/feed' in username:
                        find = re.findall('/author/(.*)/feed/"', __Check2.text)
                        username2 = find[0].strip()
                        print r + '    [' + y + '+' + r + ']' + w + ' Wordpress Username: ' + m + username2
                    else:
                        print r + '    [' + y + '+' + r + ']' + w + ' Wordpress Username: ' + m + username

            except requests.exceptions.ReadTimeout:
                self.cls()
                self.print_logo()
                print y + '---------------------------------------------------'
                print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                      ' ConnectionError! Maybe server Down, Or your ip blocked! ' + y + ']'

    def CpaNel_UserName_Enumeration(self):
        try:
            Get_page = requests.get('http://' + self.url, timeout=10)
            if '/wp-content/' in Get_page.text:
                Hunt_path = requests.get('http://' + self.url + '/wp-includes/ID3/module.audio.ac3.php', timeout=10)

                def Hunt_Path_User():
                    try:
                        find = re.findall('/home/(.*)/public_html/wp-includes/ID3/module.audio.ac3.php', Hunt_path.text)
                        x = find[0].strip()
                        return x
                    except:
                        pass

                def Hunt_Path_Host():
                    try:
                        find = re.findall("not found in <b>(.*)wp-includes/ID3/module.audio.ac3.php", Hunt_path.text)
                        x = find[0].strip()
                        return x
                    except:
                        pass

                Cpanel_username = Hunt_Path_User()
                Path_Host = Hunt_Path_Host()
                if Cpanel_username == None:
                    print r + '    [' + y + '+' + r + ']' + w + ' Cpanel Username: ' + r + 'Not Found'

                else:
                    print r + '    [' + y + '+' + r + ']' + w + ' Cpanel Username: ' + m + Cpanel_username

                if Path_Host == None:
                    print r + '    [' + y + '+' + r + ']' + w + ' User Path Host : ' + r + 'Not Found'
                else:
                    print r + '    [' + y + '+' + r + ']' + w + ' User Path Host : ' + m + Path_Host

        except requests.exceptions.ReadTimeout:
            self.cls()
            self.print_logo()
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' ConnectionError! Maybe server Down, Or your ip is blocked! ' + y + ']'

    def Plugin_NamE_Vuln_TeST(self, Plugin_NaME):
        num = 1
        cal = 0
        Flag = True
        while Flag:
            if Plugin_NaME == 'revslider':
                Plugin_NaME = 'Slider Revolution'
            url = 'https://wpvulndb.com/searches?page=' + str(num) + '&text=' + Plugin_NaME
            aa = requests.get(url, timeout=5)
            if 'No results found.' in aa.text:
                Flag = False
                break
            else:
                az = re.findall('<td><a href="/vulnerabilities/(.*)">', aa.text)
                bb = (len(az) / 2)
                for x in range(int(bb)):
                    uz = 'www.wpvulndb.com/vulnerabilities/' + str(az[cal])
                    Get_title = requests.get('http://' + uz, timeout=5)
                    Title = re.findall('<title>(.*)</title>', Get_title.text.encode('utf-8'))
                    print r + '        [' + y + 'MiGhT bE VuLn' + r + '] ' + w + uz + ' --- ' + r + \
                          Title[0].encode('utf-8').split('-')[0]
                    cal = cal + 2
                cal = 0
                num = num + 1

    def Version_Wp(self):
        try:
            Check_oNe = requests.get('http://' + self.url + '/readme.html', timeout=10)
            find = re.findall('Version (.+)', Check_oNe.text)
            try:
                version = find[0].strip()
                if len(version) != None:
                    print r + '    [' + y + '+' + r + ']' + w + ' Wp Version: ' + m + version
                    self.Plugin_NamE_Vuln_TeST('Wordpress ' + version)
            except:
                print r + '    [' + y + '+' + r + ']' + w + ' Wp Version: ' + r + 'Not Found'

        except requests.exceptions.ReadTimeout:
            self.cls()
            self.print_logo()
            print y + '---------------------------------------------------'
            print g + '    [' + y + '+' + g + ']' + r + ' Error: ' + y + '    [ ' + w + \
                  ' ConnectionError! Maybe server Down, Or your ip is blocked! ' + y + ']'

    def GeT_PluGin_Name(self):
        plugin_NamEz = {}
        Dup_Remove_Plug = 'iran-cyber.net'
        a = re.findall('/wp-content/plugins/(.*)', self.CheckWordpress.text)
        s = 0
        bb = len(a)
        for x in range(int(bb)):
            name = a[s].split('/')[0]
            if '?ver=' in a[s]:
                verz = a[s].split('?ver=')[1]
                version = re.findall('([0-9].[0-9].[0-9])', verz)
                if len(version) ==0:
                    if '-' in str(name):
                        g = name.replace('-', ' ')
                        plugin_NamEz[g] = s
                    elif '_' in str(name):
                        h = name.replace('_', ' ')
                        plugin_NamEz[h] = s
                    else:
                        plugin_NamEz[name] = s
                else:
                    OK_Ver = name + ' ' + version[0]
                    Dup_Remove_Plug = name
                    if '-' in OK_Ver:
                        ff = OK_Ver.replace('-', ' ')
                        plugin_NamEz[ff] = s
                    elif '_' in OK_Ver:
                        ff = OK_Ver.replace('_', ' ')
                        plugin_NamEz[ff] = s
                    else:
                        plugin_NamEz[OK_Ver] = s
            else:
                if Dup_Remove_Plug in name:
                    pass
                else:
                    if '-' in str(name):
                        g = name.replace('-', ' ')
                        plugin_NamEz[g] = s
                    elif '_' in str(name):
                        h = name.replace('_', ' ')
                        plugin_NamEz[h] = s
                    else:
                        plugin_NamEz[name] = s
            s = s + 1
        for name_plugins in plugin_NamEz:
            print r + '    [' + y + '+' + r + ']' + w + ' Plugin Name: ' + m + name_plugins
            self.Plugin_NamE_Vuln_TeST(name_plugins)

    def GeT_Theme_Name(self):
        a = re.findall('/wp-content/themes/(.*)', self.CheckWordpress.text)
        Name_Theme = a[0].split('/')[0]
        if '?ver=' in a[0]:
            verz = a[0].split('?ver=')[1]
            version = re.findall('([0-9].[0-9].[0-9])', verz)
            OK_Ver = Name_Theme + ' ' + version[0]
            if '-' in OK_Ver:
                x2 = OK_Ver.replace('-', ' ')
                print r + '    [' + y + '+' + r + ']' + w + ' Themes Name: ' + m + x2
                self.Plugin_NamE_Vuln_TeST(x2)
            elif '_' in OK_Ver:
                x = OK_Ver.replace('_', ' ')
                print r + '    [' + y + '+' + r + ']' + w + ' Themes Name: ' + m + x
                self.Plugin_NamE_Vuln_TeST(x)
            else:
                print r + '    [' + y + '+' + r + ']' + w + ' Themes Name: ' + m + OK_Ver
                self.Plugin_NamE_Vuln_TeST(OK_Ver)
        else:
            if '-' in Name_Theme:
                x2 = Name_Theme.replace('-', ' ')
                print r + '    [' + y + '+' + r + ']' + w + ' Themes Name: ' + m + x2
                self.Plugin_NamE_Vuln_TeST(x2)
            elif '_' in Name_Theme:
                x = Name_Theme.replace('_', ' ')
                print r + '    [' + y + '+' + r + ']' + w + ' Themes Name: ' + m + x
                self.Plugin_NamE_Vuln_TeST(x)
            else:
                print r + '    [' + y + '+' + r + ']' + w + ' Themes Name: ' + m + Name_Theme
                self.Plugin_NamE_Vuln_TeST(Name_Theme)

def wp_scan():
 Rock = S0u1wp()
 Rock