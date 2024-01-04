# Kaggle LLM - AI 생성 text 감지를 위한 분류모델 경진대회
     


- url 주소 :
https://www.kaggle.com/competitions/llm-detect-ai-generated-text/overview

- 순위 : (✔내용 추가 예정)



## 학습방법 및 실험내용



### 학습 키워드와 핵심역할 :

     텍스트 정제, 토큰화       : 이호열, 김소연
     단어 빈도 분석            : 황석준
     감정 분석                 : 이재영, 임예리
     난독화                    : 정현기


- 개요 (분류모델선정 이유 및 진행방향 요약)
    - LR, XGB
    - RF, CatBoost


- 데이터 EDA

    - train_essay : (✔내용 추가 예정)
      - target의 불균형 유무
      - 이상치 유무
      - Null 값의 유무
      - 학습데이터의 크기 (외부데이터 확보 필요유무)
      - 로그스케일링 등 인코딩 방법 선정 (캐글 트래킹)
      - 새로운 특성의 생성 유무

    - train_prompt : 해당 text의 주제.
           - 0 : Car-free cities
           - 1 : Does the electoral college work?

    - 전처리 진행
      
        - 텍스트 정제, 토큰화
          - (✔내용 추가 예정)
          https://www.notion.so/94c69beb36b94564971c032503e66dc1

        - 단어 빈도 분석
          - (✔내용 추가 예정)
          
        - 감정 분석
          - (✔내용 추가 예정)
          
        - 난독화
          - (✔내용 추가 예정)
          - 'https://link.springer.com/article/10.1007/s40979-023-00146-z' 관련 논문 참고했습니다
          
        - Augmentation (보류)
          - 직접조사
       


- 모델학습
     - (✔내용 추가 예정)
     - (하이퍼파라미터, 학습률, 배치크기, 에포크 수)



- 추론 및 대처, discussion
  - accuracy 향상을 위한 노력

## 개발환경

## 라이브러리 버전

## pip

## 실행방법

## sample parameter 설정

## Test 및 Inference



