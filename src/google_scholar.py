import requests

# SeraAPI 키를 설정합니다.
API_KEY = "YOUR_API_KEY"

# 검색할 논문의 DOI를 설정합니다.
DOI = "10.1038/nature14236"

# SeraAPI에 요청합니다.
response = requests.get("https://api.seraapi.com/v1/citations/by-doi?doi={}".format(DOI), headers={"Authorization": "Bearer {}".format(API_KEY)})

# 응답을 확인합니다.
if response.status_code == 200:
    # 응답을 디코딩합니다.
    response_json = response.json()

    # 인용 수를 가져옵니다.
    citations = response_json["citations"]

    print("논문의 인용 수는 {}입니다.".format(citations))

else:
    print("에러: {}".format(response.status_code))
