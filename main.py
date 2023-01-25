# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import logging
import requests
import json
from fusion_solar_py.client import FusionSolarClient
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.DEBUG)

SERIAL_NUMBER = "<Serial_number>"
solcol_API_KEY = "-Ye4__z4Jdi6X87j1A5RccQYlu8Sihoh"
north_site_api = "https://api.solcast.com.au/rooftop_sites/89d6-ec2a-e484-60b6/forecasts?format=json"
south_site_api = "https://api.solcast.com.au/rooftop_sites/9c31-7c2e-c252-f8e0/forecasts?format=json"
pv_system_data_url = "https://region02eu5.fusionsolar.huawei.com/pvmswebsite/nologin/assets/build/index.html#/kiosk?kk=fk8m5wouvDDcmzFE3KGxufM8bKjPzhjl"
fs_user = "nathaniel"
fs_pass = "*****"

# will need these in the future
NIGHT_RATE = 17.239
DAY_RATE = 45.504

headers = {
    'Authorization': 'Bearer %s' % solcol_API_KEY,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}


class sites():
    north_site = north_site_api
    south_site = south_site_api


class siteJsons():
    nJson = 'north_site.json'
    sJson = 'south_site.json'


def get_forcast(site):
    response = requests.request('GET', site, headers=headers)
    logging.info(f"This site data is " + site)
    logging.debug(response)
    _response = response.json()
    if site == sites.north_site:
        filter_data(_response, siteJsons.nJson)
    else:
        filter_data(_response, siteJsons.sJson)


def filter_data(response, site):
    data = [x for x in response['forecasts'] if x['pv_estimate'] > 0]
    with open(site, 'w') as outfile:
        outfile.write(json.dumps(data, indent=4))


def show_data():
    northSite = []
    southSite = []
    with open(siteJsons.nJson, "r") as f:
        contents = json.loads(f.read())
        for jsonObj in contents:
            northSite.append(jsonObj)
    with open(siteJsons.sJson, "r") as f:
        contents = json.loads(f.read())
        for jsonObj in contents:
            southSite.append(jsonObj)



    # print("Printing North site")
    # for predict in northSite:
    #     print(predict["pv_estimate"], predict["period_end"])
    #
    # print("Printing South site")
    # for predict in southSite:
    #     print(predict["pv_estimate"], predict["period_end"])

    # combined_data = {}
    # for dat in (northSite, southSite):
    #     for key, value in dat.items():
    #         if key in combined_data:
    #             combined_data[key].extend(value)
    #         else:
    #             combined_data[key] = value
    # # Sort the combined data by time
    # combined_data = {k: sorted(v, key=lambda x: x['period_end']) for k, v in combined_data.items()}
    #
    # # Extract the times and values for each key
    # times = {}
    # values = {}
    # for key, data in combined_data.items():
    #     times[key] = [d['period_end'] for d in data]
    #     values[key] = [d['pv_estimate'] for d in data]
    # for key in combined_data.keys():
    #     plt.plot(times[key], values[key], label=key)
    #
    # plt.legend()
    # plt.show()


def open_json(site):
    info = open(site)
    res = json.load(info)
    data = [x for x in res['forecasts'] if x['pv_estimate10'] > 0]
    print(data)


def get_current_data():
    client = FusionSolarClient(fs_user, fs_pass)
    stats = client.get_power_status()
    print(f"Current power: {stats.current_power_kw} kW")
    print(f"Total power today: {stats.total_power_today_kwh} kWh")
    print(f"Total power: {stats.total_power_kwh} kWh")
    client.log_out()



if __name__ == '__main__':
    # get_forcast(sites.north_site)
    # get_forcast(sites.south_site)
    show_data()
    # get_current_data()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
