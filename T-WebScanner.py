import platform
from colorama import init, Fore, Back, Style
init(autoreset=True)

from vulnerabilities import *

OS = platform.system()
PythonVersion = platform.python_version()

def banner():
	import platform
	from colorama import init, Fore, Back, Style
	init(autoreset=True)
	print(Fore.YELLOW + '''
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
''')
	print(Fore.GREEN + ' [+] Operating System: ' + platform.system() + ' ' + platform.release() + ' (Version: ' + platform.version() + ')' if platform.system() in ['Windows', 'Linux'] else Fore.RED + ' [-] Operating System: macOS ' + platform.release() + ' (Version: ' + platform.version() + ')')
	print(Fore.GREEN + ' [+] Python Version: ' + platform.python_version() if platform.python_version()[0] == '3' else Fore.RED + ' [-] Python Version: ' + platform.python_version())
	print('')

def main():
	pass


if __name__ == '__main__':
	banner()
	if OS in ['Windows', 'Linux'] and PythonVersion[0] == '3':
		main()
	else:
		exit(" Please use " + BACK.RED + "python 3.x.x" + Style.RESET_ALL + " to run T-WebScanner and run on " + BACK.RED + "Window" + Style.RESET_ALL + " or " + BACK.RED + "Linux" + Style.RESET_ALL)