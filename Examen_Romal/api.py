import requests
import re
import yaml

url = 'https://api.domainsdb.info/v1/domains/search?domain=syntra.be'
response = requests.get(url)
data = response.text
uitkomst = []


dag = re.search(r"-(\d{2})+T", data).group(1)

maand = re.search(r"[-.\/](0[1-9]|1[012])", data).group(1)

jaar = re.search(r'(?P<jaar>\d{4})', data).group(0)

ip = re.search(r"(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", data).group(1)

land = re.search(r"(?P<land>BE)", data).group(1)

provider = re.search(r"(?P<provider>syntra)", data).group(1)

uitkomst.append({'dag': dag, 'jaar': jaar, 'maand': maand, 'ip': ip, 'land': land,
                'provider': provider})

if response.status_code == 200:
    data = response.json()
    yaml_data = yaml.dump({"created": uitkomst})

    with open('rapport.yaml', 'w') as yaml_file:
        yaml_file.write(yaml_data)

    print("output is uitgeschreven naar rapport.yaml")
else:
    print(f"Fout bij het ophalen van gegevens: {response.status_code} - {response.text}")
