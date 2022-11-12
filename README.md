<div align=center>
    <h1>BLUE SHELTER</h1>
</div>

>정신건강 의료서비스 수요자와 공급자의 상호소통 플랫폼
> 

<div align=left>
    <br>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
    <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
    <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
    <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
    <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
    <img src="https://img.shields.io/badge/Folium-77B829?style=for-the-badge&logo=Folium&logoColor=white">
    <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
</div>
<br>

Blue Shelter는 정신의료서비스의 수요자와 공급자 간의 상호소통을 목적으로 한 사용자 위치기반 서비스입니다. 정신의료서비스에 대한 접근성이 부족하다는 문제의식에서 얻어낸 아이디어를 바탕으로 개발했습니다. 이용자 주변의 정신건강의료시설과의 온라인 상담이 실제 오프라인 상담까지 이어지는, 선순환 구조의 형성을 목표로 합니다.

프로젝트 기간 : 2022.06.24 ~ 2022.07.08

# 프로젝트 배경

- 정신질환 환자의 정신건강 서비스 이용율이 다른 국가에 비해 매우 낮음(약 22%)
- 정신건강 문제 발생 후 최초 정신보건서비스 이용까지 걸리는 시간이 다른 국가에 비해 오래 걸림(약 84주)
- 이같은 현상은 우리나라 국민들의 낮은 정신건강 이해력으로 인한 치료격차의 발생이 주요 원인이라고 판단

# 서비스 구상 및 차별성

## 서비스 대상

- 정신의료서비스 수요자(일반이용자) + 정신의료서비스 공급자(기관이용자)

## 주요 기능

- 이용자 위치 기반 정신의료서비스시설 지도 기능(원하는 반경, 원하는 지역 설정 가능)
- 기관별 게시판 기능
- 익명 게시글 및 댓글 기능

## 기대효과

- 일반이용자 : 개인정보 노출 없이 의료서비스를 조회하고 기관과 상담함으로써, 정신의료서비스에 대한 접근성을 높이고 심리적 장벽을 낮출 수 있다.
- 기관이용자 : 별도의 관리없이 플랫폼을 통하여 기관을 홍보하고 이용자와 소통이 가능하다. 또한 잠재수요자를 중심으로 서비스 니즈 파악이 가능하다.

## 기존의 유사 서비스

- 마인드 카페 : 온라인 상담 중심의 서비스. 이용자 위치 기반의 오프라인 연계서비스가 미비
- GOODOC : 오프라인 병원의 검색 및 예약이 주 서비스. 온라인 상담 서비스가 미비

- **Blue shelter**는 두가지 어플의 특징을 융합하고 보완하여 **이용자 위치 기반의 온라인 상담 서비스를 제공 가능**

# 세부 구현 내용

## 데이터 수집 및 처리

- 공공의료시설, 사설의료시설, 상담소를 구분하여 데이터 수집
- 전체 병원 중 진료과목에 정신의료서비스가 포함된 병원 추출
- 공공/민간 병원과 정신진료 상담소 데이터 병합
- Google Map API로 X,Y 좌표값을 위경도값(WGS84)으로 변환
- MySQL SCHEMA 작성 및 적재

## 사용자 위치 기반 지도 구현

- 중심값(default는 이용자 현재 위치) 기준으로 일정 반경 내 좌표정보들을 필터링 후 folium map으로 시각화
    - 반경그리기 -> 반경 안에 있는 정신의료시설 필터링 -> 지도 그리기
    - 파라메터는 좌표에 대한 컬럼을 가진 데이터프레임
    - 반경 값은 지도를 시각화한 템플릿에서 선택가능(default 3km)
    - geolocation으로 사용자 위경도값을 추출하여, 작성된 함수의 중심값으로 사용
    - 중심값의 일정 반경 내에 있는 모든 정신의료기관들을 마커로 표시
        - 카테고리 구분(상담소/센터/시설/병원/보건소)
        - layer 기능 추가
    - pop-up창 구현
        - 병원 이름, 병원 주소
  
- 원하는 주소를 입력하여 중심값으로 설정가능
  - Kakao API 사용하여 입력한 주소를 좌표계로 변환 후 folium map으로 시각화


# 사용 데이터

| no | 내용 | 출처 | 형식/방식 |
| --- | --- | --- | --- |
| 1 | 건강보험심사평가원_병원정보서비스 | 공공데이터포털 | API/JSON |
| 2 | 보건복지부 국립정신건강센터_정신건강 관련기관 정보 | 공공데이터포털 | API/JSON |
| 3 | 상담사 개업현황 | 한국임상심리학회 | CRAWLING/JSON |
| 4 | 상담센터 조회 | 한국상담학회 | CRAWLING/JSON |

# ERD
![erd](/general-user-service-process/pjt1-erd.png)

| Table | 역할 |
| --- | --- |
| visualization_mentalservicelocation | 의료기관 정보관리 |
| visualization_myboard | 게시판 관리 |
| visualization_mymembers | 회원 관리 |
| visualization_comment | 댓글 관리 |
| mental_board | 게시판 관리- 의료기관정보관리 Join 용 |
| member_board | 회원관리-게시판 관리 Join용 |

# 서비스 화면
- 메인페이지
![main](/institutional-users-service-process/1.png)

- 지도 페이지
![map](/general-user-service-process/4.png)

- 게시판 페이지
![posting](/general-user-service-process/6.png)
