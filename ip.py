def ip():
    import socket
    from ketik import ketik

    
    print(" __  _______  ")
    print("/  |/       \ ")
    print("$$/ $$$$$$$  |")
    print("/  |$$ |__$$ |")
    print("$$ |$$    $$/ ")
    print("$$ |$$$$$$$/  ")
    print("$$ |$$ |      ")
    print("$$ |$$ |      ")
    print("$$/ $$/       ")
    print("\n")
    ketik("=== HOST IP By 6Virus ===")
    added = input("Domain Target: ")
    res = socket.gethostbyname(added)
    print("HOST IP : " + res)