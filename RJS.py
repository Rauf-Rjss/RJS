import os, platform 

try:
	import requests
except ImportError:
	os.system('pip install requests')
Main().menu()
