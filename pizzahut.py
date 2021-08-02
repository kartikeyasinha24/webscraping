import requests
import pandas as pd


def get_final_value(crust, size, final_value):
    if crust == 'H':
        if size == 'L':
            final_value = 'L'
        elif size == 'M':
            final_value = 'M'
        elif size == 'P':
            final_value = ''

    elif crust == 'T':
        if size == 'L':
            final_value = 'LT'
        elif size == 'M':
            final_value = 'MT'
        elif size == 'P':
            final_value = ''

    elif crust == 'P':
        if size == 'L':
            final_value = 'LD'
        elif size == 'M':
            final_value = 'MD'
        elif size == 'P':
            final_value = 'PP'

    elif crust == 'S':
        if size == 'L':
            final_value = 'LS'

    return final_value


def remove_non_ascii(df):
    return ''.join(i for i in df if ord(i)<128) #ordinal function

try:
    print('execution started...')
    payload = {'customer_postal_code': "79606", 'limit': '5'}
    carry_out_download_headers = {
        'authority': 'www.pizzahut.com',
        'method': 'POST',
        'path': '/api.php/site/api_ajax/search/carryout',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '42',
        'content-type': 'application/json;',
        'charset': 'UTF-8',
        'origin': 'https://www.pizzahut.com',
        'referer': 'https://www.pizzahut.com/index.php?menu=pizza',
        'sec-ch-ua': "\"Chromium\";v=\"92\", \"Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        'x-sec-clge-req-type': 'ajax'
    }

    carry_out_download_cookies = {
        'cookie': "QOSESSID=b4s6smh9gg3d2t1hr950e1m5co; user_state=%7B%22menu%22%3A%5B%22pizza%22%2C%22wings%22%2C%22sides%22%2C%22pasta%22%2C%22desserts%22%2C%22drinks%22%5D%7D; PHPpoolSSL=!tlI5bmvoPTe9oI9kew+uhP1RVJNFfYH0jfPI0k82YC2JAXFvPdZFAeCFrBmZj6vkiChBrJn+hY44/zk=; akadcgtm=dc1; akadcgtm2=dc1; TS01bded03=01da65bfdd9637e9f9233a1fa553efe7a0da315e55cae735a12cf5be0f85b63506bfb92ea5f8697d991b6ce8c853954dcc64f8cf5af1fc0b117b2da796c7f543d84273db5547d993e4cfe126a0859bec3f0855924644966afa8408ce0115f384002e74c594; TS011d6839=01da65bfdde75d1557ec22a3b6e09815edf847dd36cae735a12cf5be0f85b63506bfb92ea5533f09bfc9954796668d0510b3dd38bba4d2d7596ef60d29ab7c2230eb04ce0ea7e7e19e1a255cba7659f4e52b503d2feba364e2312a2b296e047ad15dbbb0bc; SEGNUM=62; User-Experience=PH-WEB1; AKA_A2=A; bm_sz=4D68AB8970547C66F745C4893615EFE7~YAAQu/4xF/sH3fR6AQAAj0hpBgwmL19Di2wZxr/qv8Pbl0rMTwMWQr8AN6f3UzspzQPFvG4JBFrZ3SAwnb61IB9+hr02AMRgAUVjCPr3q46QyEqfaFrB2BJDSb0OVgTH7U9aBaxuau6wDdqVj/DTJIPkNV1H8W/yR2r8yJRychbM5fu9zSgwrb9hzWp/VDu2tdvka5jonPivkFNzJa8kADULYjBut9oK/TusdNsUqKm0HbtEuQ/Wot6N8/gBrTTqEtDYcZ4rLG40phmbZBxXILJKC2iMVHva9SHiien8f4EczUVzPA==~3424565~4272432; _abck=2DDF95B594F219A38F965361FCF7158A~-1~YAAQu/4xFxEI3fR6AQAAhFppBgaY33J0iNvuL3ePHLA2VphNLaycZWKKxEOR1o6TWL4sEc5LGRzMxAbadSVYt8G3+CQKbvejnnD9AfcJr1C/YViL8nKRxEz5ViiqBj0mBMLF6ERRhyc34pMX8p4RlDccuUohnJfHrBxz6b+Y1RBfFktIlWD7lR42UGpgOc12zMkMraFVgNP37dsFPQhXDYfaUV+vp7eDh0huZ4pnih3cEItXr2tlL6ztqVhn+bdy/w/QHZxIpHBNvEg2oOobyn6jhjEdnMYx7EHvDzEosfd+abztVjyicJE7RTxPvHo/c2PD2xqgaeH9izJ7qq/zRCrJ3vEyuusFnv2T8Gvfw2X7eFRFlemvc/q+xvibtdcu9B2JAbP8ARn/zRNW4XVGbN3un9OjwD0sQ96Ck7NVnETJipnNHGQ3ZfAZvnYfkIYQeY2BT18=~-1~-1~-1; ak_bmsc=B6EE9000E28A3A353342C69AF71CFFAE~000000000000000000000000000000~YAAQu/4xFxII3fR6AQAAclxpBgzTi58QftjOMKJFaIfSPJ1L4pwLnSuWU1mGdXJfuoP/wHkxjidl+EyGrOMnIfiYHZ4UDEwjWH79Pxorw4WTUDIvAd0KaLcrXz6p5KHf79qaVQIda7vpXS2KY18QwxUJyajTKppodXivIHAZ2P4qSgdNaURuL1e7uu6UuzzgriOPbBsDCCO7Z7Vfz7gneddYnhlCf+R1ye3MltbgCrCfIkZjJhhrKww1H3cCQXoRdc1FWe7O1rzI2QogVzuWpM/WHAUjP8JFxU5bd5lnBqKTLK1yL+y9Xhj9pOOd8CIDEVMO2yqEKnBBuuxVK5tev0hXIe9T0yuLVxO4yCvMWgRmcEwcaPl/mjlN2CSaMCJCOTZ6g6brMRIvz0IumEr9Ug91k2VSG+lwTar20tkAawj2SnjsTcbwJU4gJ02AA36ZpJWanT0/6IpmdaIt1/G5PE+MuPi7x5BXueNNweDZxb+vosfKgrVYnK+LCa54; gtm-session-start=1627900169333; _gcl_au=1.1.1336395229.1627900175; _scid=4495c9ce-e118-4eb8-aaba-e4eb550ecad0; _ga=GA1.2.401804774.1627900179; _gid=GA1.2.1508636216.1627900179; _rdt_uuid=1627900181319.1bad5a64-83a5-4439-a088-ff0a01602a68; __adroll_fpc=477c09be938a8db791cb58383ec05402-1627900181621; _gat_UA-34361514-2=1; _fbp=fb.1.1627900182259.284628160; __ar_v4=%7COTUCE2Z3VBGWFHOFWGQHTL%3A20210801%3A1%7CV5SJZXPENBCN7NX3FYVVIB%3A20210801%3A1%7CH6RSMMPK2BCVPNRJTV5AVK%3A20210801%3A1; _pin_unauth=dWlkPU1UYzVOVFJoWVRjdE4yTmhPQzAwTURka0xUaGtaVGt0TVRaaU4ySm1OMlZsTXpoag; _sctr=1|1627842600000; www-siteview=www; pizzabucket=101%7E91; TS0118ed69=01da65bfdd880711fbeeaf28e0d0712e1244578a9bcae735a12cf5be0f85b63506bfb92ea5f8697d991b6ce8c853954dcc64f8cf5af1fc0b117b2da796c7f543d84273db5547d993e4cfe126a0859bec3f085592464699f73a232032b73770adfc64bf013f0e523c04fa551201d7dc8ca5768a32834447906e254bb53d0549b58a59c32dd0; bm_sv=9C00186167FC1A901023253C2F751BF4~NIb6TJj0cpQZm5mLtU6Bk37qTJDwJqZ6vwCNyAmYJMhqk1Q+hoyRrdll2ouskkJsUH4R1QY7CwEqBQ7rqPUJ7Zzroyycx2Drie4CJ43mG4s72Bx3wtJ7r8AGs97lHZ+Du4MF5G56cv9El1Zc9dr0V4qHppFaXqXUujdA54knGjY=; at_check=true; mbox=session#9e9ff8f0cedb4568a9ddebe900496090#1627902074|PC#9e9ff8f0cedb4568a9ddebe900496090.34_0#1691145016; mboxEdgeCluster=34; optimizelyEndUserId=oeu1627900217248r0.976058334447053; optimizelySegments=%7B%22209642986%22%3A%22direct%22%2C%22209669694%22%3A%22gc%22%2C%22209692476%22%3A%22false%22%2C%22209740042%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; optimizelyPendingLogEvents=%5B%5D; utag_main=v_id:017b06695ed3000e4750e7bdcdfb03073001906b00978$_sn:1$_se:4$_ss:0$_st:1627902017627$ses_id:1627900174036%3Bexp-session$_pn:2%3Bexp-session$centro_sync_session:1627900174036%3Bexp-session$ispot_uid:v2%3A8096b2011e1eff67df89dc7540f597ad02c7fad86e5fcd88e1f6e54fe688e825%7Ce2003fb11006dbb6ef8264e8ae31a71563629124344f10e51fa91ec83b364c52%3Bexp-session$dc_visit:1$dc_event:1%3Bexp-session$dc_region:us-east-1%3Bexp-session"
    }

    with requests.session() as s:
        print('in session')
        home_page = 'https://www.pizzahut.com'
        response = s.get(home_page)

        print(response.url, response.status_code)

        print('--------------------------------------------------------------------------------')
        carryout_page = 'https://www.pizzahut.com/api.php/site/api_ajax/search/carryout'
        print('cursor in carry out page')
        carryout_page_url_response = s.post(carryout_page,
                                            headers=carry_out_download_headers,
                                            cookies=carry_out_download_cookies, data=payload)

        print('--------------------------------------------------------------------------------')
        confirm_location_download_headers = {
            'authority': 'www.pizzahut.com',
            'method': 'POST',
            'path': '/api.php/site/api_ajax/confirm_location',
            'scheme': 'https',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '47',
            'content-type': 'application/json;charset=UTF-8',
            'charset': 'UTF-8',
            'origin': 'https://www.pizzahut.com',
            'referer': 'https://www.pizzahut.com/index.php',
            'sec-ch-ua': "\"Chromium\";v=\"92\", \"Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            'x-sec-clge-req-type': 'ajax'
        }

        carry_out_download_cookies = {
            'cookie': "QOSESSID=b4s6smh9gg3d2t1hr950e1m5co; user_state=%7B%22menu%22%3A%5B%22pizza%22%2C%22wings%22%2C%22sides%22%2C%22pasta%22%2C%22desserts%22%2C%22drinks%22%5D%7D; PHPpoolSSL=!tlI5bmvoPTe9oI9kew+uhP1RVJNFfYH0jfPI0k82YC2JAXFvPdZFAeCFrBmZj6vkiChBrJn+hY44/zk=; akadcgtm=dc1; akadcgtm2=dc1; TS011d6839=01da65bfdde75d1557ec22a3b6e09815edf847dd36cae735a12cf5be0f85b63506bfb92ea5533f09bfc9954796668d0510b3dd38bba4d2d7596ef60d29ab7c2230eb04ce0ea7e7e19e1a255cba7659f4e52b503d2feba364e2312a2b296e047ad15dbbb0bc; SEGNUM=62; User-Experience=PH-WEB1; AKA_A2=A; bm_sz=4D68AB8970547C66F745C4893615EFE7~YAAQu/4xF/sH3fR6AQAAj0hpBgwmL19Di2wZxr/qv8Pbl0rMTwMWQr8AN6f3UzspzQPFvG4JBFrZ3SAwnb61IB9+hr02AMRgAUVjCPr3q46QyEqfaFrB2BJDSb0OVgTH7U9aBaxuau6wDdqVj/DTJIPkNV1H8W/yR2r8yJRychbM5fu9zSgwrb9hzWp/VDu2tdvka5jonPivkFNzJa8kADULYjBut9oK/TusdNsUqKm0HbtEuQ/Wot6N8/gBrTTqEtDYcZ4rLG40phmbZBxXILJKC2iMVHva9SHiien8f4EczUVzPA==~3424565~4272432; ak_bmsc=B6EE9000E28A3A353342C69AF71CFFAE~000000000000000000000000000000~YAAQu/4xFxII3fR6AQAAclxpBgzTi58QftjOMKJFaIfSPJ1L4pwLnSuWU1mGdXJfuoP/wHkxjidl+EyGrOMnIfiYHZ4UDEwjWH79Pxorw4WTUDIvAd0KaLcrXz6p5KHf79qaVQIda7vpXS2KY18QwxUJyajTKppodXivIHAZ2P4qSgdNaURuL1e7uu6UuzzgriOPbBsDCCO7Z7Vfz7gneddYnhlCf+R1ye3MltbgCrCfIkZjJhhrKww1H3cCQXoRdc1FWe7O1rzI2QogVzuWpM/WHAUjP8JFxU5bd5lnBqKTLK1yL+y9Xhj9pOOd8CIDEVMO2yqEKnBBuuxVK5tev0hXIe9T0yuLVxO4yCvMWgRmcEwcaPl/mjlN2CSaMCJCOTZ6g6brMRIvz0IumEr9Ug91k2VSG+lwTar20tkAawj2SnjsTcbwJU4gJ02AA36ZpJWanT0/6IpmdaIt1/G5PE+MuPi7x5BXueNNweDZxb+vosfKgrVYnK+LCa54; gtm-session-start=1627900169333; _gcl_au=1.1.1336395229.1627900175; _scid=4495c9ce-e118-4eb8-aaba-e4eb550ecad0; _ga=GA1.2.401804774.1627900179; _gid=GA1.2.1508636216.1627900179; _rdt_uuid=1627900181319.1bad5a64-83a5-4439-a088-ff0a01602a68; __adroll_fpc=477c09be938a8db791cb58383ec05402-1627900181621; _fbp=fb.1.1627900182259.284628160; _sctr=1|1627842600000; www-siteview=www; pizzabucket=101%7E91; TS0118ed69=01da65bfdd880711fbeeaf28e0d0712e1244578a9bcae735a12cf5be0f85b63506bfb92ea5f8697d991b6ce8c853954dcc64f8cf5af1fc0b117b2da796c7f543d84273db5547d993e4cfe126a0859bec3f085592464699f73a232032b73770adfc64bf013f0e523c04fa551201d7dc8ca5768a32834447906e254bb53d0549b58a59c32dd0; at_check=true; mboxEdgeCluster=34; optimizelyEndUserId=oeu1627900217248r0.976058334447053; optimizelySegments=%7B%22209642986%22%3A%22direct%22%2C%22209669694%22%3A%22gc%22%2C%22209692476%22%3A%22false%22%2C%22209740042%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; TS01bded03=01da65bfdd782fd54dd1ecc8ae12db9197970fe2b6cae735a12cf5be0f85b63506bfb92ea5f8697d991b6ce8c853954dcc64f8cf5af1fc0b117b2da796c7f543d84273db5547d993e4cfe126a0859bec3f08559246a05e09008f4b18ce458ef97cd8db5e15d209399ddb9a96ffb3d18037152a0b3d; bm_sv=9C00186167FC1A901023253C2F751BF4~NIb6TJj0cpQZm5mLtU6Bk37qTJDwJqZ6vwCNyAmYJMhqk1Q+hoyRrdll2ouskkJsUH4R1QY7CwEqBQ7rqPUJ7Zzroyycx2Drie4CJ43mG4tRXd93TzX+rBZaXOkTg5Fm5ABL6bozqN8cyuXblTShXKhtbm4yDcE4DUmjnkBvaWY=; mbox=session#9e9ff8f0cedb4568a9ddebe900496090#1627902074|PC#9e9ff8f0cedb4568a9ddebe900496090.34_0#1691145024; _pin_unauth=dWlkPVlUQmhNR0kwTkdFdE1UYzNPUzAwTmpZekxUZ3labUl0TldKa1pUZGxOV001TldWbQ; __ar_v4=H6RSMMPK2BCVPNRJTV5AVK%3A20210801%3A2%7CV5SJZXPENBCN7NX3FYVVIB%3A20210801%3A2%7COTUCE2Z3VBGWFHOFWGQHTL%3A20210801%3A2; optimizelyPendingLogEvents=%5B%5D; utag_main=v_id:017b06695ed3000e4750e7bdcdfb03073001906b00978$_sn:1$_se:14$_ss:0$_st:1627902082550$ses_id:1627900174036%3Bexp-session$_pn:2%3Bexp-session$centro_sync_session:1627900174036%3Bexp-session$ispot_uid:v2%3A8096b2011e1eff67df89dc7540f597ad02c7fad86e5fcd88e1f6e54fe688e825%7Ce2003fb11006dbb6ef8264e8ae31a71563629124344f10e51fa91ec83b364c52%3Bexp-session$dc_visit:1$dc_event:5%3Bexp-session$dc_region:us-east-1%3Bexp-session$dcsyncran:1%3Bexp-session; _abck=2DDF95B594F219A38F965361FCF7158A~-1~YAAQnP4xF4W+2vR6AQAA5xZrBgbXK6eIv79radEtdgYuLOoRltJorjZ3CeRbqSNNis30l9YYEPzpfSS9UXC2M2khsikxebWso+dz5V3Nipm4UiVwh6RH0dXGyGb8UHmGHdksZnbDYkpyG3qmkbHNqVlvGvyOIF7Rx6cZGBovHTB20s16MFbFnRMpELHQEeiECsW100Rez7FuOCFCPbkuV0AeEDWA3m+LUvLPlMndbBmgSeo4qW7Fiq/jiB2HnWDGF+BOJXeQQ9ZyVhDY/fg3Q5teWA1OSsBP/h/1N9Tj2g02FFtEZaMSfhLhnmL/cW/5p/4U3QmwbZOAWb/GGFXQHadbV2NTxZ5/fWTOzMcwZmtx0SHFmRbYAQFicG0KfpWkzfcwHDkKDfgNSPF24dzT0PnEED02+FCVqIWTRNYX9zjGCj2svoWZZnbFk1H/An6paXPGh/s=~-1~-1~-1"
                       }

        confirm_location_url_payload = {'occasion': "C", 'storenum': "028798", 'saKey': ""}

        print('cursor in confirm location')
        confirm_location_url = 'https://www.pizzahut.com/api.php/site/api_ajax/confirm_location'
        confirm_location_url_response = s.post(confirm_location_url, headers=confirm_location_download_headers,
                                               cookies=carry_out_download_cookies,
                                               data=confirm_location_url_payload)
        print(confirm_location_url_response.url, confirm_location_url_response.status_code)

        getstoretiles_download_headers = {
            'authority': 'www.pizzahut.com',
            'method': 'GET',
            'path': '/api.php/site/api_pages/api_menu/getstoretiles',
            'scheme': 'https',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'referer': 'https://www.pizzahut.com/index.php?menu=pizza',
            'sec-ch-ua': "\"Chromium\";v=\"92\", \"Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            'x-sec-clge-req-type': 'ajax'
        }

        carry_out_download_cookies = {
            'cookie': "QOSESSID=b4s6smh9gg3d2t1hr950e1m5co; PHPpoolSSL=!tlI5bmvoPTe9oI9kew+uhP1RVJNFfYH0jfPI0k82YC2JAXFvPdZFAeCFrBmZj6vkiChBrJn+hY44/zk=; akadcgtm=dc1; akadcgtm2=dc1; SEGNUM=62; User-Experience=PH-WEB1; AKA_A2=A; bm_sz=4D68AB8970547C66F745C4893615EFE7~YAAQu/4xF/sH3fR6AQAAj0hpBgwmL19Di2wZxr/qv8Pbl0rMTwMWQr8AN6f3UzspzQPFvG4JBFrZ3SAwnb61IB9+hr02AMRgAUVjCPr3q46QyEqfaFrB2BJDSb0OVgTH7U9aBaxuau6wDdqVj/DTJIPkNV1H8W/yR2r8yJRychbM5fu9zSgwrb9hzWp/VDu2tdvka5jonPivkFNzJa8kADULYjBut9oK/TusdNsUqKm0HbtEuQ/Wot6N8/gBrTTqEtDYcZ4rLG40phmbZBxXILJKC2iMVHva9SHiien8f4EczUVzPA==~3424565~4272432; ak_bmsc=B6EE9000E28A3A353342C69AF71CFFAE~000000000000000000000000000000~YAAQu/4xFxII3fR6AQAAclxpBgzTi58QftjOMKJFaIfSPJ1L4pwLnSuWU1mGdXJfuoP/wHkxjidl+EyGrOMnIfiYHZ4UDEwjWH79Pxorw4WTUDIvAd0KaLcrXz6p5KHf79qaVQIda7vpXS2KY18QwxUJyajTKppodXivIHAZ2P4qSgdNaURuL1e7uu6UuzzgriOPbBsDCCO7Z7Vfz7gneddYnhlCf+R1ye3MltbgCrCfIkZjJhhrKww1H3cCQXoRdc1FWe7O1rzI2QogVzuWpM/WHAUjP8JFxU5bd5lnBqKTLK1yL+y9Xhj9pOOd8CIDEVMO2yqEKnBBuuxVK5tev0hXIe9T0yuLVxO4yCvMWgRmcEwcaPl/mjlN2CSaMCJCOTZ6g6brMRIvz0IumEr9Ug91k2VSG+lwTar20tkAawj2SnjsTcbwJU4gJ02AA36ZpJWanT0/6IpmdaIt1/G5PE+MuPi7x5BXueNNweDZxb+vosfKgrVYnK+LCa54; gtm-session-start=1627900169333; _gcl_au=1.1.1336395229.1627900175; _scid=4495c9ce-e118-4eb8-aaba-e4eb550ecad0; _ga=GA1.2.401804774.1627900179; _gid=GA1.2.1508636216.1627900179; _rdt_uuid=1627900181319.1bad5a64-83a5-4439-a088-ff0a01602a68; __adroll_fpc=477c09be938a8db791cb58383ec05402-1627900181621; _fbp=fb.1.1627900182259.284628160; _sctr=1|1627842600000; www-siteview=www; pizzabucket=101%7E91; TS0118ed69=01da65bfdd880711fbeeaf28e0d0712e1244578a9bcae735a12cf5be0f85b63506bfb92ea5f8697d991b6ce8c853954dcc64f8cf5af1fc0b117b2da796c7f543d84273db5547d993e4cfe126a0859bec3f085592464699f73a232032b73770adfc64bf013f0e523c04fa551201d7dc8ca5768a32834447906e254bb53d0549b58a59c32dd0; at_check=true; mboxEdgeCluster=34; optimizelyEndUserId=oeu1627900217248r0.976058334447053; optimizelySegments=%7B%22209642986%22%3A%22direct%22%2C%22209669694%22%3A%22gc%22%2C%22209692476%22%3A%22false%22%2C%22209740042%22%3A%22none%22%7D; optimizelyBuckets=%7B%7D; mbox=session#9e9ff8f0cedb4568a9ddebe900496090#1627902074|PC#9e9ff8f0cedb4568a9ddebe900496090.34_0#1691145024; _pin_unauth=dWlkPVlUQmhNR0kwTkdFdE1UYzNPUzAwTmpZekxUZ3labUl0TldKa1pUZGxOV001TldWbQ; __ar_v4=H6RSMMPK2BCVPNRJTV5AVK%3A20210801%3A2%7CV5SJZXPENBCN7NX3FYVVIB%3A20210801%3A2%7COTUCE2Z3VBGWFHOFWGQHTL%3A20210801%3A2; _gat_UA-34361514-2=1; utag_main=v_id:017b06695ed3000e4750e7bdcdfb03073001906b00978$_sn:1$_se:20$_ss:0$_st:1627902097076$ses_id:1627900174036%3Bexp-session$_pn:2%3Bexp-session$centro_sync_session:1627900174036%3Bexp-session$ispot_uid:v2%3A8096b2011e1eff67df89dc7540f597ad02c7fad86e5fcd88e1f6e54fe688e825%7Ce2003fb11006dbb6ef8264e8ae31a71563629124344f10e51fa91ec83b364c52%3Bexp-session$dc_visit:1$dc_event:8%3Bexp-session$dc_region:us-east-1%3Bexp-session$dcsyncran:1%3Bexp-session; _abck=2DDF95B594F219A38F965361FCF7158A~-1~YAAQnP4xF4i+2vR6AQAAA0RrBgZK5MjmYOJ+CmuAVuoVLvhcLVKAftVa2rMb3J+Nkn1CnRqu7ujdqgT6BbZa/1rWT/J6p1IpJ43pTWx1x36gPXzXv2CTZckE2rb1qK8BY37jnr+eiHQbNzsPlGv1c0IgTk70Ev9w+7o/0S+LzCEaMNHbSrgX8mMsEskf3HFbiejM23TAvfpy1ok1zMwm+zlmWuHCHlzh3IhKEWFvWI1wFBFxrxlVziSM3JMvJR0STY71Xo1IlvWGHS5y0NuM5352j6CYarUxPiih7rrqQbEsd8Zez1S65StcWUs+86HnTzI0F/E/x42dYidVXLheEQbuoNj72uNFhZz5k23nd77tvJ/Y84G8VPZGjTDKLqCux+6PVziNFu6FogClaD6FtZbT/hN9we4BCkFVGN2anaDonzb+I+ppuRJ66r1cdqOPxpY4XFo=~-1~-1~-1; localization-token=eyJhbGciOiJQUzUxMiIsImtpZCI6ImU5ZTAxMWEyLWUzYWUtNDdjMC1hMDhlLTVmNjFmYWJmNjM0MyIsInR5cCI6IkpXVCJ9.eyJhZGRyMSI6IjQzMDMgUyBDbGFjayBTdCIsImF1ZCI6WyJQSERBUEkiLCJQSFBBWSJdLCJjaXR5IjoiQWJpbGVuZSIsImV4cCI6MTYzMDQ5MjI5OSwiaWF0IjoxNjI3OTAwMjk5LCJpc3MiOiJQSCBDb25uZWN0IiwibGF0IjozMi40MDA5NjcsImxvbmciOi05OS43NTk0OSwibmJmIjoxNjI3OTAwMjk5LCJvY2MiOiJDQVJSWU9VVCIsInNuIjoiMDI4Nzk4Iiwic3RhdGUiOiJUWCIsInN1YiI6IkNsaWVudCIsInR6IjoiQW1lcmljYS9DaGljYWdvIiwiemlwIjoiNzk2MDYifQ.ezjdiqc_fwK2Vp7Y_hM1ZF1EDWt_yO6j8mHYKaGTvA43Yn80rDmGO_7WohXAiRE7GXGWkMjlYCuIwX4HnusxsBANXg1PEgk6ZBDJVNnL_PwgdntaMmAAu_ZpgcU3Qih74zSfNmuvbGsC9KF2_318xXa6IFQpvWxyYM1TEGp80L4hwS7yTCbt-mMpp2KihyWaYfgiNmHszs1uRN-qJ5RgTx824QgTkfHb7PhL7swwTYqNXhEudtEgKJEtmN1ljCBupvhKB2J0vyaRZO4j8tYIMLsVls3HKjtsjAYEzc8SRxiJAiRd1hjMops8xilDeq5ynwCVrqX2t68S0mXsCS2tUQ; to_cart=a%3A4%3A%7Bs%3A5%3A%22total%22%3Bs%3A0%3A%22%22%3Bs%3A8%3A%22subtotal%22%3Bs%3A0%3A%22%22%3Bs%3A15%3A%22loyalty_removed%22%3Bi%3A0%3Bs%3A11%3A%22expiry_time%22%3Bi%3A1638268300%3B%7D; user_state=%7B%22menu%22%3A%5B%22pizza%22%2C%22wings%22%2C%22sides%22%2C%22pasta%22%2C%22desserts%22%2C%22drinks%22%5D%2C%22action%22%3A%22%22%2C%22deliveryAddress%22%3A%22%22%2C%22currentSavedLocationIndex%22%3Anull%2C%22storeLatitude%22%3A%2232.400966%22%2C%22storeLongitude%22%3A%22-99.759488%22%2C%22StoreNumber%22%3A%22028798%22%2C%22occasion%22%3A%22C%22%2C%22zipcode%22%3A%2279606%22%2C%22wingstreetleadmkt%22%3A0%2C%22user_state_abbrev%22%3A%22U%22%7D; TS01bded03=01da65bfdd406f312e66763247154aaee3ddf56ef6cae735a12cf5be0f85b63506bfb92ea5f8697d991b6ce8c853954dcc64f8cf5af1fc0b117b2da796c7f543d84273db5547d993e4cfe126a0859bec3f08559246a05e09008f4b18ce458ef97cd8db5e15f51bdec9e6232aa9c15f97acb89acd3779b69a912a08a94651edb9acb991d034; TS011d6839=01da65bfdd392766529a68dfd0255a923a2c9b1adfcae735a12cf5be0f85b63506bfb92ea5533f09bfc9954796668d0510b3dd38bbde3b55b9ba2e750ba63928c702c591152ad2b498d02f5f0bdea661997a6176f9edf0b43426ed79476a47f76438aaa994a6e86c9e65e2f621b1707379482e1f66; bm_sv=9C00186167FC1A901023253C2F751BF4~NIb6TJj0cpQZm5mLtU6Bk37qTJDwJqZ6vwCNyAmYJMhqk1Q+hoyRrdll2ouskkJsUH4R1QY7CwEqBQ7rqPUJ7Zzroyycx2Drie4CJ43mG4tBeUg9qwxSWW4a1qLMXO+QOsC0wSir8lnWzGVjIYjd9fUzXNRUHRRz+hN7lWNl5IY="
        }

        tiles = s.get('https://www.pizzahut.com/api.php/site/api_pages/api_menu/getstoretiles',
                      headers=getstoretiles_download_headers,
                      cookies=carry_out_download_cookies)
        print(tiles.url,tiles.status_code)
        print('Getting the data from pizzahut.com site')
        required_data = dict(tiles.json())

        popular_pizza_list = []
        for i in range(len(required_data['pages']['pizza']['sections'][0]['tiles'])):
            popular_pizza_list.append(required_data['pages']['pizza']['sections'][0]['tiles'][i])

    print('requests are completed')
    crust_dictionary = {
        'H': 'Hand Tossed pizza',
        'T': 'Thin \'N crispy',
        'P': 'Original pan pizza',
        'S': 'Original stuffed crust'
    }
    size_dictionary = {
        'L': 'Large',
        'M': 'Medium',
        'P': 'Personal Pan Pizza'
    }
    pizzahut_price_list = []

    if 'popular_pizza' in popular_pizza_list[0].keys():
        submenu = 'popular_pizza'
    else:
        submenu = ''

    for k in range(len(popular_pizza_list)):
        for i in range(len(popular_pizza_list[k]['crusts'])):
            crust = popular_pizza_list[k]['crusts'][i]['val']
            for j in range(len(popular_pizza_list[k]['sizes'])):
                size = popular_pizza_list[k]['sizes'][j]['val']
                final_value = ''
                final_value = get_final_value(crust, size, final_value)
                if final_value in popular_pizza_list[k]['tile_data']['prices'].keys():

                    final_price_dictionary = {
                        'menu' : popular_pizza_list[k]['analytics']['category'],
                        'submenu' : submenu,
                        'product' : popular_pizza_list[k]['analytics']['name'],
                        'size' : size_dictionary[size],
                        'crust' : crust_dictionary[crust],
                        'price' : float(popular_pizza_list[k]['tile_data']['prices'][final_value])
                    }
                pizzahut_price_list.append(final_price_dictionary)

    print('Execution Completed!')

    pizzahut_df = pd.DataFrame(pizzahut_price_list)
    pizzahut_df.drop_duplicates(inplace = True)
    pizzahut_df['product'] = pizzahut_df['product'].apply(remove_non_ascii)
    file_name = 'pizzahut_data.csv'
    pizzahut_df.to_csv(file_name, index=None)

    print(f'data saved as {file_name} in current working directory.')

except Exception as e:
    print(e)
