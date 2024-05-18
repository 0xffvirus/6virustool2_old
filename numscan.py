def numscan():
    import requests 
    print("[ Only Saudi Numbers ]")
    print("[ Don't Write +966 example : 558832003 ]")
    usr = input("Number >> ")
    url = "http://146.148.112.105/caller/index.php/UserManagement/search_number?number="+usr+"&country_code=SA"
    r = requests.get(url)
    num = str(r.json()['result'][0]['number'])
    name = str(r.json()['result'][0]['name'])
    country = str(r.json()['result'][0]['country_code'])
    id = str(r.json()['result'][0]['id'])
    print("---- Coded By 6Virus ----")
    print("number : ",num)
    print("name : ",name)
    print("Country : ",country)
    print("id : ",id)