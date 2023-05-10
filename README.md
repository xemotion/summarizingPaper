# Streamlit을 이용하여 웹 페이지 배포하기 


### 개발 환경 구축 
conda + visual studio + github 
#### conda 설치 시 주의점 
conda + visual studio로 설치해서 진행 
conda 설치 시에 conda init을 해야 시작됨. 
conda 설치 후에 visual studio 에서 작업하려면 ctrl+shift+p 를 누르면 visual studio의 인터프리터 설정을 할 수 있는 칸이 나옴
해당 내용을 conda python위치로 설정한다. (기존에 파이썬 path가 있는 경우 설치가 안될 수도 있으니, python path를 삭제하고 아나콘다 실행하니 되네요... ㅜㅜ) 



#### 가상 환경에서 작업하자 


* streamlit이라는 가상 환경 user 생성 
```
conda create -n streamlit 
```

#### streamlit 으로 들어감 
``` 
conda activate streamlit 
```




```
pip isntall streamtlit 
streamlit hello 
```

서버 띄우기 
```
streamlit run app.py 
``` 
 

