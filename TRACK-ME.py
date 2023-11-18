import socket
import json
import os
import requests
from requests import get
import time
import phonenumbers 
from phonenumbers import carrier, geocoder, timezone



RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

print(f''' 
    {BLUE}
      __________  ___   ________ __             __  _________
     /_  __/ __ \/   | / ____/ //_/            /  |/  / ____/
      / / / /_/ / /| |/ /   / ,<     ______   / /|_/ / __/   
     / / / _, _/ ___ / /___/ /| |   /_____/  / /  / / /___   
    /_/ /_/ |_/_/  |_\____/_/ |_|           /_/  /_/_____/  {RESET}{RED}

                   ██════════════════════██                 
                   █████  By NOT YOU  █████                    
                   ██════════════════════██ {RESET}                                                     
                                ''')



print(f'''
    [{RED}1{RESET}] link to ip
    [{RED}2{RESET}] my ip address & host name 
    [{RED}3{RESET}] ip lockup
    [{RED}4{RESET}] number info
    [{RED}5{RESET}] about
    [{RED}0{RESET}] exit
''')



linp = input("select number : ")


def hip ():
    host = socket.gethostname()
    url = 'http://ipinfo.io/json'
    response = get(url)
    data = json.loads(response.text)
    ip = data['ip']
    print(f"{RED}ip:{RESET}", ip)
    print(f"{RED}host:{RESET}", host)
    
 
def pgh():
    User_phone = input(f"\n Enter phone number target Ex [+123xxxxxxxxx] : ") 
    default_region = "ID" 
    parsed_number = phonenumbers.parse(User_phone, default_region) 
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region, with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)
    print(f"\n{RED} Location          {RESET} :{location}")
    print(f"{RED} Region Code         {RESET} : {region_code}")
    print(f"{RED} Timezone            {RESET} : {timezoneF}")
    print(f"{RED} Operator            {RESET} : {jenis_provider}")
    print(f"{RED} Valid number        {RESET} : {is_valid_number}")
    print(f"{RED} Possible number     {RESET} : {is_possible_number}")
    print(f"{RED} International format{RESET} : {formatted_number}")
    print(f"{RED} Mobile format       {RESET} : {formatted_number_for_mobile}")
    print(f"{RED} Original number     {RESET} : {parsed_number.national_number}")
    print(f"{RED} E.164 format        {RESET} : {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f"{RED} Country code        {RESET} : {parsed_number.country_code}")
    print(f"{RED} Local number        {RESET} : {parsed_number.national_number}")


def frplp ():
            ip = input(f"\n Enter IP target : ")
            print()
            req_api = requests.get(f"http://ipwho.is/{ip}")
            ip_data = json.loads(req_api.text)
            time.sleep(2)
            print(f"\n{RED} IP target    {RESET}   :", ip)
            print(f"{RED} Type IP        {RESET} :", ip_data["type"])
            print(f"{RED} Country        {RESET} :", ip_data["country"])
            print(f"{RED} Country Code   {RESET} :", ip_data["country_code"])
            print(f"{RED} City           {RESET} :", ip_data["city"])
            print(f"{RED} Continent      {RESET} :", ip_data["continent"])
            print(f"{RED} Continent Code {RESET} :", ip_data["continent_code"])
            print(f"{RED} Region         {RESET} :", ip_data["region"])
            print(f"{RED} Region Code    {RESET} :", ip_data["region_code"])
            print(f"{RED} Latitude       {RESET} :", ip_data["latitude"])
            print(f"{RED} Longitude      {RESET} :", ip_data["longitude"])
            lat = int(ip_data['latitude'])
            lon = int(ip_data['longitude'])
            print(f"{RED} Maps           {RESET} :",f"https://www.google.com/maps/@{lat},{lon},8z")
            print(f"{RED} Calling Code   {RESET} :", ip_data["calling_code"])
            print(f"{RED} EU             {RESET} :", ip_data["is_eu"])
            print(f"{RED} Postal         {RESET} :", ip_data["postal"])
            print(f"{RED} Capital        {RESET} :", ip_data["capital"])
            print(f"{RED} Borders        {RESET} :", ip_data["borders"])
            print(f"{RED} Country Flag   {RESET} :", ip_data["flag"]["emoji"])
            print(f"{RED} ASN            {RESET} :", ip_data["connection"]["asn"])
            print(f"{RED} ORG            {RESET} :", ip_data["connection"]["org"])
            print(f"{RED} ISP            {RESET} :", ip_data["connection"]["isp"])
            print(f"{RED} Domain         {RESET} :", ip_data["connection"]["domain"])
            print(f"{RED} ID             {RESET} :", ip_data["timezone"]["id"])
            print(f"{RED} ABBR           {RESET} :", ip_data["timezone"]["abbr"])
            print(f"{RED} DST            {RESET} :", ip_data["timezone"]["is_dst"])
            print(f"{RED} Offset         {RESET} :", ip_data["timezone"]["offset"])
            print(f"{RED} UTC            {RESET} :", ip_data["timezone"]["utc"])
            print(f"{RED} Current Time   {RESET} :", ip_data["timezone"]["current_time"])

def gok():
    url = input('link : ')
    ip = socket.gethostbyname(url)
    print(ip)

def bou():
    print(f'''
        {MAGENTA}
███╗   ██╗ ██████╗ ████████╗    ██╗   ██╗ ██████╗ ██╗   ██╗
████╗  ██║██╔═══██╗╚══██╔══╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║
██╔██╗ ██║██║   ██║   ██║        ╚████╔╝ ██║   ██║██║   ██║
██║╚██╗██║██║   ██║   ██║         ╚██╔╝  ██║   ██║██║   ██║
██║ ╚████║╚██████╔╝   ██║          ██║   ╚██████╔╝╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝    ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ 
        {RESET}                                                 

         [{RED}+{RESET}] Github :
         [{RED}+{RESET}] discord :    
                                
   ''')
if linp == '1' :
    gok()
if linp == '2' :
    hip()


if linp == '3':
    frplp()

if linp == '4':
    pgh()

if linp == '5':
    bou()

if linp == '0':
    print(f"\n{YELLOW} THANK'S FOR USING TOOL !{RESET}")

