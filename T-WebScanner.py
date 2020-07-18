import platform
from colorama import init, Fore, Back, Style
init(autoreset=True)
from bs4 import BeautifulSoup
import argparse
import base64
import re

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
	print(Fore.GREEN + ' [+] Operating System: ' + platform.system() + ' ' + platform.release() + ' (Version: ' + platform.version() + ')' if platform.system() in ['Windows', 'Linux'] else Fore.RED + ' [-] Operating System: ' + Style.RESET_ALL + Back.RED + ' macOS ' + Style.RESET_ALL + Fore.RED + ' ' + platform.release() + ' (Version: ' + platform.version() + ')')
	print(Fore.GREEN + ' [+] Python Version: ' + platform.python_version() if platform.python_version()[0] == '3' else Fore.RED + ' [-] Python Version: ' + Style.RESET_ALL + Back.RED + ' ' + platform.python_version() + ' ')
	print('')

def main(BurpRequest):
	try:
		requests = dict()
		XML_BurpRequest = BeautifulSoup(open(BurpRequest).read(), 'html.parser')
		requests['Host'] = XML_BurpRequest.items.item.host.text 
		requests['Port'] = XML_BurpRequest.items.item.port.text
		requests['Protocol'] = XML_BurpRequest.items.item.protocol.text
		requests['Requests'] = list()
		for req in XML_BurpRequest.items.findAll('request'):
			headers = base64.b64decode(req.text).decode('utf-8').split('\r\n\r\n')[0]
			Method, RequestURI, ProtocolVersion = re.findall('([^\s]+) ([^\s]+) ([^\s]+)', headers.split('\r\n')[0])[0]
			RequestLine = {
				'Method': Method,
				'RequestURI': RequestURI,
				'ProtocolVersion': ProtocolVersion
			}

			RequestHeaders = dict()
			for i in headers.split('\r\n')[1:]:
				k, v = re.findall('([^:]+): (.*)', i)[0]
				RequestHeaders[k] = v

			MessageBody = base64.b64decode(req.text).decode('utf-8').split('\r\n\r\n')[1]

			requests['Requests'].append({
				'RequestLine': RequestLine,
				'RequestHeaders': RequestHeaders,
				'MessageBody': MessageBody
			})
	except Exception as e:
		raise
	print(requests)


if __name__ == '__main__':
	banner()
	if OS in ['Windows', 'Linux'] and PythonVersion[0] == '3':
		parser = argparse.ArgumentParser(description=' T-WebScanner ...')
		parser.add_argument("BurpRequest", help="Request list from Burp Suite")
		args = parser.parse_args()
		BurpRequest = args.BurpRequest
		main(BurpRequest)
	else:
		exit(Fore.RED + '==> Please use ' + Style.RESET_ALL + Back.RED + ' python 3.x.x ' + Style.RESET_ALL + Fore.RED + ' to run T-WebScanner and run on ' + Style.RESET_ALL + Back.RED + ' Windows ' + Style.RESET_ALL + Fore.RED + ' or ' + Style.RESET_ALL + Back.RED + ' Linux ' + Style.RESET_ALL + '\n')