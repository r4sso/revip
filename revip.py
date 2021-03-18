Banner = """

██████╗░███████╗██╗░░░██╗  ██╗██████╗░
██╔══██╗██╔════╝██║░░░██║  ██║██╔══██╗
██████╔╝█████╗░░╚██╗░██╔╝  ██║██████╔╝
██╔══██╗██╔══╝░░░╚████╔╝░  ██║██╔═══╝░
██║░░██║███████╗░░╚██╔╝░░  ██║██║░░░░░
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ╚═╝╚═╝░░░░░  By r4sso|github.com

"""
import os, requests
os.system('clear')
print(Banner)

session = requests.session()

inip = input('Enter IP: ')
api = "http://api.hackertarget.com/reverseiplookup/?q="
apipun = api + inip
print(session.get(apipun).text)