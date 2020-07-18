import platform
from colorama import init, Fore, Back, Style
init(autoreset=True)

from vulnerabilities import *

OS = platform.system()
PythonVersion = platform.python_version()

def banner():
	print(Fore.YELLOW + """
=========================================================================
=========================================================================
          _______                      _____  _                 
         |__   __|                    |  __ \| |                
            | |_ __ _   _  ___   ___  | |__) | |__   __ _ _ __  
            | | '__| | | |/ _ \ / __| |  ___/| '_ \ / _` | '_ \ 
            | | |  | |_| | (_) | (__  | |    | | | | (_| | | | |
            |_|_|   \__,_|\___/ \___| |_|    |_| |_|\__,_|_| |_|
                                                       
 [+] Facebook: https://www.facebook.com/292706121240740
 [+] Github:   https://github.com/truocphan
 [+] Discord:  https://discord.gg/fuBe3af
 [+] Gmail:    truocphan112017@gmail.com

=========================================================================
=========================================================================
""")

def main():
	pass


if __name__ == '__main__':
	banner()
	print(Fore.GREEN + '[+] Your OS: ' + OS if OS in ['Windows', 'Linux'] else Fore.RED + '[-] Your OS: ' + OS)
	print(Fore.GREEN + '[+] Python Version: ' + PythonVersion if PythonVersion[0] == '3' else Fore.RED + '[-] Python Version: ' + PythonVersion)
	if OS in ['Windows', 'Linux'] and PythonVersion[0] == '3':
		main()
	else:
		pass