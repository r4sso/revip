#Author: r4sso
#Github: https://github.com/r4sso

banner = '''

 ██████╗░███████╗██╗░░░██╗  ██╗██████╗░
 ██╔══██╗██╔════╝██║░░░██║  ██║██╔══██╗
 ██████╔╝█████╗░░╚██╗░██╔╝  ██║██████╔╝
 ██╔══██╗██╔══╝░░░╚████╔╝░  ██║██╔═══╝░
 ██║░░██║███████╗░░╚██╔╝░░  ██║██║░░░░░
 ╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ╚═╝╚═╝░░░░░  By r4sso|github.com

'''

P0 = "\033[0;35m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
G0 = "\033[0;32m"
G1 = "\033[1;32m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"


try:
    import os
    import requests,json
    import os.path

  

except:
    os.system("pip3 install requests")


os.system('clear')
print(banner)


def main():

    choice ='0'
    while choice =='0':
        print("Choose Method:")
        print("1. hackertarget.com      [LIMITED]")
        print("2. tools.hack.co.id      [COMING SOON]")
        print("3. yougetsignal.com      [COMING SOON]")


        choice = input ("\n\nPlease make a choice: ")

        if choice == "1":
            Hackertarget()
        elif choice == "2":
            print("Coming soon! use other else")
        elif choice == "3":
            print("Coming soon! use other else")
        else:
            print("I don't understand your choice.")


def Hackertarget():
    os.system("clear")
    print("""
█░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█ ▀█▀ ▄▀█ █▀█ █▀▀ █▀▀ ▀█▀
█▀█ █▀█ █▄▄ █░█ ██▄ █▀▄ ░█░ █▀█ █▀▄ █▄█ ██▄ ░█░
    """)
    session = requests.session()
    inip = input('Enter IP: ')
    print("\n=========== Output ===============")
    api = "http://api.hackertarget.com/reverseiplookup/?q="
    apipun = api + inip
    output = session.get(apipun).text
    print(output)
    file = input("Save output to txt? [Y/n]").lower()
    if file == 'y':
        fila = input("\nFilename: ")
        filename = fila + ".txt"
        file1 = open(filename, "w")
        file1.write(str(output))
    else:
        print("\nHAVE A GOOD DAY :)")


main()