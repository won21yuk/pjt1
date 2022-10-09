import requests, xmltodict, json

# open API JSON 가공

key = 'MGlX8jT2jARU535Ywm%2FoJG192i6N5Bj%2Fxpb8RpxuKOU2o8LihjzxJPC0O0xg6RVZtBL%2FNvfSaBzhHUJK22CHXQ%3D%3D'

url = 'http://apis.data.go.kr/B551182/hospInfoService1/getHospBasisList1?numOfRows=3561&dgsbjtCd=03&ServiceKey={}'.format(key)

response = requests.get(url)
#print(response.content)

content = response.content

dict = xmltodict.parse(content)
dict_json = json.dumps(dict['response']['body']['items'], ensure_ascii=False, indent=4, sort_keys=True)

with open('hospital_mental2.json', 'w', encoding='utf-8') as f:
    f.write(dict_json)