import requests, re


# parses website html for a phone number using the regex below.
def get_phone_number(url):
  r = requests.get(url, verify=False)
  content = str(r.content)
  phone_numbers = (re.findall(r"\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}",str(content)))
  return phone_numbers


# returns dictionary of phone numbers. key=website value=phone number
def get_numbers_from_list(sites_list):
  numbers_dict = {}
  for site in sites_list:
    if get_phone_number(site) != []:
      numbers_dict[site] = get_phone_number(site)[0]
  return numbers_dict


# reads file, assumes websites are newline-delimited and in full url format.
def get_numbers_from_file(filename):
    sites_file = open(filename, 'r')
    sites_list = sites_file.readlines()
    for i in range (0, len(sites_list)):
      sites_list[i] = sites_list[i][:-1] # removes newline
    return get_numbers_from_list(sites_list)
    
    
get_numbers_from_file("sites.txt")
