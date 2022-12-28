#BY Z3R0          
import os
import requests 
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
os.system('clear')
print(RED)
os.system('sudo apt install figlet')
os.system('clear')
print(YELLOW+'''
 ___ ____            ___ _   _ _____ ___  
|_ _|  _ \          |_ _| \ | |  ___/ _ \ 
 | || |_) |  _____   | ||  \| | |_ | | | |
 | ||  __/  |_____|  | || |\  |  _|| |_| |
|___|_|             |___|_| \_|_|   \___/ 

''')

def info():
    r = input(PURPLE+'Type the ip address : ')
    os.system('clear')
    print(RED+'''
 ___ ____            ___ _   _ _____ ___  
|_ _|  _ \          |_ _| \ | |  ___/ _ \ 
 | || |_) |  _____   | ||  \| | |_ | | | |
 | ||  __/  |_____|  | || |\  |  _|| |_| |
|___|_|             |___|_| \_|_|   \___/ 

    ''')
    ip_address = r
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    print(YELLOW)
    data = {
        "ip": '[+]'+PURPLE+' ip ---->: '+ip_address+PURPLE+'\n',
        "city": YELLOW+'[+]'+PURPLE+' city ---->: '+YELLOW+response.get("city")+ '\n',
        "region": YELLOW+'[+]'+PURPLE+' region ---->: '+YELLOW+response.get("region")+'\n',
        "country2": YELLOW+'[+]'+PURPLE+' country name ---->: '+YELLOW+response.get("country_name")+'\n',
        "version": YELLOW+'[+]'+PURPLE+' version ---->: '+YELLOW+response.get('version')+'\n',
        "country": YELLOW+"[+]"+PURPLE+" country ---->: "+YELLOW+response.get("country")+'\n',
        "country_code": YELLOW+"[+]"+PURPLE+" country_code ---->: "+YELLOW+response.get("country_code")+'\n',
        "country_code_iso3": YELLOW+"[+]"+PURPLE+" country_code_iso3 ---->: "+YELLOW+response.get("country_code_iso3")+'\n',
        "country_capital": YELLOW+'[+]'+PURPLE+' country_capital ---->: '+YELLOW+response.get("country_capital")+'\n',
        "country_tld": YELLOW+"[+]"+PURPLE+" country_tld ---->: "+YELLOW+response.get("country_tld")+'\n',
        "continent_code": YELLOW+"[+]"+PURPLE+" continent_code ---->: "+YELLOW+response.get("continent_code")+'\n',
        "in_eu": YELLOW+"[+]"+PURPLE+" in_eu ---->: "+YELLOW+ str(response.get("in_eu"))+'\n',
        "postal": YELLOW+"[+]"+PURPLE+" postal ---->: "+YELLOW+str(response.get("postal"))+'\n',
        "latitude":YELLOW+"[+]"+PURPLE+" latitude ---->: "+YELLOW+str(response.get("latitude"))+'\n',
        "longitude": YELLOW+"[+]"+PURPLE+" longitude ---->: "+YELLOW+str(response.get("longitude"))+'\n',
        "timezone": YELLOW+"[+]"+PURPLE+" timezone ---->: "+YELLOW+response.get("timezone")+'\n',
        "utc_offset":YELLOW+"[+]"+PURPLE+" utc_offset ---->: "+YELLOW+response.get("utc_offset")+'\n',
        "country_calling_code":YELLOW+"[+]"+PURPLE+" country_calling_code ---->: "+YELLOW+response.get("country_calling_code")+'\n',
        "currency":YELLOW+  "[+]"+PURPLE+" currency ---->: "+YELLOW+response.get("currency")+PURPLE+'\n',
        "currency_name":YELLOW+ "[+]"+PURPLE+" currency_name ---->: "+YELLOW+response.get('currency_name')+'\n',
        "languages": YELLOW+"[+]"+PURPLE+" languages ---->: "+YELLOW+response.get("languages")+PURPLE+'\n',
        "country_area": YELLOW+"[+]"+PURPLE+" country_area ---->: "+YELLOW+str(response.get("country_area"))+PURPLE+'\n',
        "country_population":YELLOW+"[+]"+PURPLE+" country_population ---->: "+YELLOW+str(response.get("country_population"))+'\n',
        "asn":YELLOW+ "[+]"+PURPLE+" asn ---->: "+YELLOW+response.get("asn")+'\n',
        "org": YELLOW+"[+]"+PURPLE+" org ---->: "+YELLOW+response.get('org')
    }
    for x in data:
        print(data[x])
    r = 0
    while r == 0:
        i = r
info()

print(info())