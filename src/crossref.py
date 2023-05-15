
import requests

# Crossref API에서 발급받은 인증키를 입력하세요.
# API_KEY = 'YOUR_API_KEY'

# Crossref API의 base URL을 정의합니다.
BASE_URL = 'https://api.crossref.org'

# 레퍼런스와 인용 정보를 가져올 논문의 DOI를 입력하세요.
doi = '10.1109/5.771073'

# Crossref API에서 논문의 메타데이터와 레퍼런스 정보를 가져옵니다.
response = requests.get(f'{BASE_URL}/works/{doi}', params={'mailto': 'drawinghongcha@gmail.com', 'rows': 0, 'select': 'reference-count,citation-count'}, headers={'User-Agent': 'MyScript/1.0'})

# API 호출이 성공했는지 확인합니다.
if response.status_code == requests.codes.ok:
    data = response.json()

    # 논문의 레퍼런스와 인용 정보를 출력합니다.
    reference_count = data['message']['reference-count']
    citation_count = data['message']['is-referenced-by-count']
    print(f'Reference count: {reference_count}')
    print(f'Citation count: {citation_count}')
else:
    # API 호출이 실패한 경우 오류 메시지를 출력합니다.
    print(f'Error: {response.status_code}')