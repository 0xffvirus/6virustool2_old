def iplook():
    from clear import clear
    from start import virus
    import os
    def draw():
        clear()
        print("                  ████████████████████████            ")
        print("              ████████████████████      ██████        ")
        print("    ██      ████  ████████████    ██      ██████      ")
        print("      ████████  ██████████████      ██      ██████    ")
        print("  ██    ████    ████████████████    ██        ████████")
        print("    ██████      ██████████████████████        ██████  ")
        print("██    ████      ██▒▒▒▒██████████▒▒▒▒██        ████    ")
        print("  ████          ██▒▒▒▒██████████▒▒▒▒██        ██      ")
        print("                ██▒▒▒▒██████████▒▒▒▒██        ██      ")
        print("                ██▒▒▒▒▒▒██████▒▒▒▒▒▒██      ██        ")
        print("                ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                ")
        print("                  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ██            ")
        print("              ██████████████████████████              ")
        print("\n")

    def menu():
        print("\n")
        print("======================================")
        print("===========Coded by @1zsb=============")
        print("                                      ")
        print("  [1] Start            [99]Main Menu  ")
        print("                 ==                   ")
        print("======================================")
        print("\n")

    def menu2():
        print("\n")
        print("======================================")
        print("===========Coded by @1zsb=============")
        print("                                      ")
        print("  [1] Target IP           [2] My IP   ")
        print("                                      ")
        print("  [3] Whois lookup      [4] Port Scan ")
        print("                                      ")
        print("        [5] Reverse ip lookup         ")
        print("======================================")
        print("\n")

    draw()
    menu()
    option1 = input("root@root:~# ")
    if option1 == '1':
        clear()
        draw()
        menu2()
        option = input("root@root:~# ")
        if option == '1':
            ip = input("What Your Target IP : ")
            url = "https://ipapi.co/"
            r = requests.get(url + ip + "/json")
            query = str(r.json()['ip'])
            city = str(r.json()['city'])
            reg = str(r.json()['region'])
            regcode = str(r.json()['region_code'])
            contry = str(r.json()['country_name'])
            contry_cap = str(r.json()['country_capital'])
            contry_area = str(r.json()['country_area'])
            Continent = str(r.json()['continent_code'])
            time = str(r.json()['timezone'])
            currency = str(r.json()['currency'])
            Calling = str(r.json()['country_calling_code'])
            org = str(r.json()['org'])
            asn = str(r.json()['asn'])

            print("++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\r")
            print(" IP              :  " + query)
            print(" City            :  " + city)
            print(" Region          :  " + reg)
            print(" Region Code     :  " + regcode)
            print(" Country         :  " + contry)
            print(" Country Capital :  " + contry_cap)
            print(" Country Area    :  " + contry_area)
            print(" Location        :  " + str(r.json()['latitude']) + " " + str(r.json()['longitude']))
            print(" Continent       :  " + Continent)
            print(" Time Zone       :  " + time)
            print(" Currency        :  " + currency)
            print(" Calling Code    :  " + Calling)
            print(" Organisation    :  " + org)
            print(" ASN             :  " + asn)
            print("\r")
            input("Done .. Press Enter To Exit ..")
        elif option == '2':
            url = "https://ipapi.co/"
            url2 = "http://ipinfo.io/"
            r = requests.get(url + "json")
            r2 = requests.get(url2 + "json")
            query = str(r.json()['ip'])
            city = str(r.json()['city'])
            reg = str(r.json()['region'])
            regcode = str(r.json()['region_code'])
            contry = str(r.json()['country_name'])
            contry_cap = str(r.json()['country_capital'])
            contry_area = str(r.json()['country_area'])
            Continent = str(r.json()['continent_code'])
            time = str(r.json()['timezone'])
            currency = str(r.json()['currency'])
            Calling = str(r.json()['country_calling_code'])
            org = str(r.json()['org'])
            asn = str(r.json()['asn'])
            ip2 = str(r2.json()['ip'])
            print("++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\r")
            print(" Public IP       :  " + query)
            print(" Private IP      :  " + ip2)
            print(" City            :  " + city)
            print(" Region          :  " + reg)
            print(" Region Code     :  " + regcode)
            print(" Country         :  " + contry)
            print(" Country Capital :  " + contry_cap)
            print(" Country Area    :  " + contry_area)
            print(" Location        :  " + str(r.json()['latitude']) + " " + str(r.json()['longitude']))
            print(" Continent       :  " + Continent)
            print(" Time Zone       :  " + time)
            print(" Currency        :  " + currency)
            print(" Calling Code    :  " + Calling)
            print(" Organisation    :  " + org)
            print(" ASN             :  " + asn)
            print("\r")
            input("Done .. Press Enter To Exit ..")
        elif option == '3':
            d3 = input('Enter IP Or Domain : ')
            clear()
            os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
            print("")
            quit()
        elif option == '4':
            d3 = input('Enter IP Or Domain : ')
            clear()
            os.system("curl http://api.hackertarget.com/nmap/?q=" + d3)
            print("")
            quit()
        elif option == '5':
            d3 = input('Enter IP Or Domain : ')
            clear()
            os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + d3)
            clear()
            os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + d3)
            print("")
            print("\033[91m\033[1mFile Saved On : ")
            os.system("ls")
            print("File : index.html?q=" + d3)
            print("\033[0m")
            quit()
    elif option1 == '99':
        clear()
        virus()