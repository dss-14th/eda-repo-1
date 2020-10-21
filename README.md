패스트캠퍼스 EDA 프로젝트 : 코로나로 인한 지역 매출 하락 지원 및 복구 정책
==========================================================

# 팀 구성
> 1. 김연수
> 2. 황지수


# 문제 정의

> ## 1. 분석의 목적
 우리 팀의 목적은 ‘코로나로 인한 매출 하락 지역 및 산업에 관해 지원 및 복구 정책 제언을 하는 것입니다.
 그래서 코로나 전과 후의 매출을 비교해 어떠한 요소들이 영향을 미쳤는지 알아보고자 EDA 분석을 하였습니다.
> ## 2. 분석 의의	
 1) 코로나로 인한 경제 악화가 위험한 이유는 전세계적인 팬데믹 상황으로 인해 소비량뿐 아니라 공급량 역시 줄어들어 가격은 오르고 재화의 수는 감소하는, 자칫하면 장기 경기 불황으로 갈 수 있는 상황이 되기 때문입니다.
 따라서 정부는 소비와 공급을 모두 높이기 위한 정책을 운영해야 합니다.
 2) 아래 두 그래프는 2020년 1월부터 5월까지 두 명의 카드 사용량을 나타낸 그래프입니다.
 보시면 코로나의 여파가 시작된 3,4월에 가장 낮은 소비량을 기록하고 있음을 알 수 있습니다.
 (1월의 경우 카드 소지자가 외국에 있었어서, 한국에서 카드를 거의 사용사지 않았기 때문에 낮은 것입니다.)
 그리고 5월로 갈 수록 높은 카드 소비량을 보이고 있습니다.  
 코로나의 영향력이 약해진 까닭이라고 생각할수도있지만, 사실 이 두 명은 프로젝트 참여자 본인들로 한명은 5월 이태원 클럽 확진자가 퍼진 동네에 살고 있고,다른  한 명 역시 인천에 살며 인천학원강사의 7차 감염이 터진 시기었기에 활동량은 그리 변화하지 않았습니다. 소비량이 늘어난 가장 큰 이유는 바로 ‘재난 지원금’을 사용할 수 있었기 때문입니다. 
 
![1 j_money](https://user-images.githubusercontent.com/68367334/92301319-e0e17f80-ef9d-11ea-8047-ec246df96a5d.jpg)
![2 y_money](https://user-images.githubusercontent.com/68367334/92301320-e343d980-ef9d-11ea-81de-f2855dbd8e06.jpg)

> ## 3. 가설 수립
1) 시간별 매출양이 나온 데이터: 주말이 평일보다 매출이 높을 것이다. 그래서 하락도 주말에 관련된 업종(산업)의 하락률이 컸을것이다. (요식업)
2) 새벽 오전 오후 저녁으로 나눔. 일과가 끝난 후 활동 시간인 저녁때 매출이 높을 것으로 예상하여 저녁 결제 건수, 건당 결제 금액 둘다 저녁이 높을 거라 예상
3) 계절별로 보면 봄의 매출이 겨울보다 높을 것으로 예상 (활동성이 높은 계절이니) 그런데 코로나가 봄에 터졌으니 매출의 전반적인 타격은 클 것으로 예상
4) 활동성이 높은 계절에 타격이 컸을 거라 예상을 했기때문에 활동성과 관련이 있는 유동인구 변화에 대한 타격이 있을 거라 예상

> ## 4. 분석 지표: 5년전의 한국을 위협했던 메르스 바이러스 상황을 분석 지표로 삼아 기사 및 매거진 참고

* 관련 기사 1 : <https://www.sedaily.com/NewsVIew/1Z2WWFRPUW>
* 관련 기사 2 : <https://biz.chosun.com/site/data/html_dir/2020/03/22/2020032200608.html>
* 관련 기사 3 : <https://news.joins.com/article/23695525>

> ## 5. 분석 예상 시간
1) 주제 선정 및 도메인 지식 : 2020.07.20 - 2020.07.22
2) 데이터 수집 : 2020.07.23 - 2020.07.24
3) 데이터 전처리 : 2020.07.25 - 2020.07.26
4) 데이터 분석 및 시각화 : 2020.07.27 - 2020.07.29
5) 보고서 작성 및 발표 자료 준비 : 2020.07.29 - 2020.07.30
6) 발표 : 2020.07.31
  


# 데이터 수집

## 1. 본 데이터 설명
1) 출처: Daycon <https://dacon.io/competitions/official/140472/overview/>
2) 설명
- 핀테크 기업 ‘FUNDA(펀다)’ 에서 제공한 2016.06.01-2019.02.28까지의 상점별 카드 매출 내역
- 컬럼: store_id, card_id, card_company, transacted_date, transacted_time, installment_term(할부 개월 수), region, type_of_business, amount

## 2. 카드 & 물가 지수
1) 출처: Daycon <https://www.dacon.io/competitions/official/235618/overview/>
2) 설명
- KT 빅데이터 플랫폼에서 제공해준 업종 별 결제 금액인 2020년 카드 데이터와 품목 별 소비자 수인 물가지수 데이터를 사용했습니다.
- 컬럼: receipt_dttm[카드회사가 카드사용내역을 접수한일자], adstrd_code[가맹점 위치 기준 행정동 코드], adstrd_nm[가맹점 위치 기준 행정동명], mrhst_induty_cl_code[가맹점 업종코드], mrhst_induty_cl_nm[가맹   점 업종명], selng_cascnt[매출발생건수], salamt[매출발생금액]

## 3. 주민등록 인구수
1) 출처: 서울 열린데이터 광장 <https://data.seoul.go.kr/dataList/419/S/2/datasetView.do>
2) 설명
- 2020년 1/4분기 서울 주민등록인구수를 자치구별로 제공하는 데이터로 “거주자”, “거주불명자”, “재외국인”을 포함
- 컬럼: 세대, 인구 합계, 남자 인구 합계, 여자 인구 합계, 한국인 인구 합계, 한국 남자 인구, 한국 여자 인구, 등록 외국인 합계, 남자 등록 외국인, 여자 등록 외국인

## 4. 유동인구 데이터
1) 출처: 통계청 빅데이터통계과, SK텔레콤 IoT/Data 사업부 <https://giraf.sktelecom.com/cartoweb/kostat/index.html#>
2) 설명
- 전국 시군구별 주중/주말의 월별 일평균 유동 인구를 GIS기반으로 제공된 유입 인구 데이터 지도

## 5. 관광객 데이터
1) 출처: 서울 열린데이터 광장 <https://data.seoul.go.kr/dataList/10858/S/2/datasetView.do>
2) 설명
- 2019년 서울시 주요 관광지점 입장객 현황을 제공하는 데이터


## 6. 의류 및 숙박업, 의약품 도매업 분포 지도 데이터 시각화
1) 출처 : 서울시정책지도 <http://map.seoul.go.kr:9978/spm/gly/policy/view.do?POLICY_NO=109&THEMADO_NO=276>


# EDA 분석 설명 

> ## 1. 데이터 전처리 설명

![전국 데이터 중 서울만 추출](https://user-images.githubusercontent.com/68367334/92301314-cc04ec00-ef9d-11ea-97ce-af99ef5d8aa3.jpg)
 
우선 저희는 전국의 소비 데이터 중, 서울 지역만을 추출하여 사용하였습니다. 워낙 방대한 양의 데이터라 모든 지역을 살펴보는 것은 무리가 있다고 생각하였고, 한 지역만 봐야 할 경우 서울이 가장 경제상황에 민감하게 반응하는 지역이기 때문에 필요성이 높다고 판단하였기 때문입니다.

![3 도봉구 결측치](https://user-images.githubusercontent.com/68367334/92301332-f48ce600-ef9d-11ea-88e3-da58a4f6afe6.png)

이 과정에서 발견한 결측치는, 총 25개의 서울특별시 행정구역 중 ‘도봉구’가 존재하지 않는다는 것이었습니다. 하지만, 해당 결측치는 다른 값으로 대체하는 것은 불가능하기 때문에 이후 도봉구는 제외하고 비교를 하는 것으로 결론 지었습니다. 
 
![환불 값 처리 (표 및 전처리)](https://user-images.githubusercontent.com/68367334/92301429-e12e4a80-ef9e-11ea-9443-9bb7fcb8e2b5.jpg)
![환불 값 처리 함수](https://user-images.githubusercontent.com/68367334/92301433-f1dec080-ef9e-11ea-8364-6e05d77b247c.jpg)

전처리에서 가장 중점을 두었던 부분은 환불 값을 처리해주는 파트였습니다. 해당 자료에는 어떤 부분을 환불한 것인지 정보가 나와있지 않은 (-) 금액을 포함하고 있었기 때문입니다. 따라서 저희는 같은 상점에서 같은 카드로 더 많거나 같은 금액을 결제한 것 중에 가장 최근의 결제에서 그 값은 빼 주는 방식으로 처리하였습니다. 

> ## 2. 데이터 분석 및 결과 그래프 삽입

### 요일에 따른 분석
 
![시간별로 데이터 나누는 코드 및 표](https://user-images.githubusercontent.com/68367334/92301449-09b64480-ef9f-11ea-8fd9-70754a523980.jpg)

저희는 이후 날짜와 시간을 모두 자유롭게 사용하기 위해서 ‘date’ 컬럼을 년월일과 시간으로 분리하였습니다. 
 
![요일별 데이터로 만드는 코드](https://user-images.githubusercontent.com/68367334/92301469-1b97e780-ef9f-11ea-8278-9603550f8ae9.jpg)

![요일별 데이터로 만든 표](https://user-images.githubusercontent.com/68367334/92301476-29e60380-ef9f-11ea-88db-040874e3ed6e.jpg)

또한, 날짜에서 하나 더 나아가 요일별 매출 차이를 파악하기 위해서 ‘week’ 컬럼 역시 추가해주었습니다. 

> [요일별 매출량]
<img width="337" alt="4 1번데이터 요일별 매출양" src="https://user-images.githubusercontent.com/68261338/92301413-be039b00-ef9e-11ea-9521-91bd9224bab9.png">

그 결과, 저희가 가설1에서 생각했던 것과 달리 평일에 요식업 거래량이 주말보다 많다는 것을 알 수 있었습니다. 또한, 하루 총 매출 역시 평일이 주말보다 월등히 높은 양상을 보여주고 있었습니다.

---------------------------------------------

### 시간대에 따른 분석

 
![오전 오후 저녁 새벽 시간별로 나눈 데이터 코드](https://user-images.githubusercontent.com/68367334/92301512-6c0f4500-ef9f-11ea-9299-d09e7a47ad1b.png)

<img width="736" alt="시간별 1" src="https://user-images.githubusercontent.com/68367334/92301539-a8db3c00-ef9f-11ea-9002-1dc032c2035a.png">
<img width="736" alt="시간별 2" src="https://user-images.githubusercontent.com/68367334/92301547-ad9ff000-ef9f-11ea-9094-7ca9e64d39a6.png">
<img width="735" alt="시간별 3" src="https://user-images.githubusercontent.com/68367334/92301551-b1cc0d80-ef9f-11ea-80e7-16e37c03d7ff.png">

다음으로, 저희는 하루의 시간대별 매출 차이 역시 파악하고자 하였습니다. 하루를 6시간 씩 4개의 구간으로 정의한 후 (오전 : 06 - 12시, 오후 : 12 - 18시, 저녁 : 18 - 24시, 새벽 : 00시 - 6시) 나누어 주었습니다.

이를 통해, 저희가 가설 2에서 생각했던 것처럼 저녁의 결제 건수가 높은 편임을 확인할 수 있었으나, 실제로 오후가 더 높다는 것 역시 새롭게 알게된 사실이었습니다.

한가지 특이했던 점은, 오전 시간대의 건당 결제 금액이 가장 높았다는 것입니다. 가설 2의 가정과는 달리 저녁은 그리 높지 않은 건당 결제 금액을 보여주었습니다.

이에 대한 이유를 알아보기 위해 저희는 산업 구조를 살펴보았고, 그 결과 오전 시간대에 다른 소매업 매출 비중이 작은 것에 비해 의약품 도매업과 같은 건당 매출 금액이 높은 산업이 활발하게 거래된다는 사실을 깨달았습니다. 
이는 앞서 살펴보았던, 평일이 주말보다 훨씬 높은 매출을 보여주고 있는 현상과도 일맥상통하는 바라고 생각했습니다. 즉, 도매업이 지역 매출에 상당한 영향을 끼친다는 것입니다.

> [산업별 / 시간대별 건당 평균 매출 금액]
![의약품](https://user-images.githubusercontent.com/68367334/92301555-b85a8500-ef9f-11ea-99ef-ce8aa8a54d7e.jpg)

------------------------------------------------------------------------------

### 계절에 따른 분석

> [2019년 지역 별 겨울 봄 매출 비교]
![8 2019 지역별 겨울 봄 합친 사진](https://user-images.githubusercontent.com/68261338/92301443-03c06380-ef9f-11ea-8045-5aa23cbc8be4.jpg)

가설 3에서 설정한 것과 같이, 활동량이 많은 봄에 코로나가 터졌기 때문에 매출의 감소폭 역시 클 것이라고 예상하였고 이를 검증 해보기 위해 데이터들을 봄과 겨울의 평균 매출로 전처리 하였습니다. 
실제로 3개의 구를 제외한 모든 구에서 평소 겨울보다 봄 매출이 높은 것으로 나타났으며, 이는 저희의 가설과 맞는 부분이었습니다. 

이렇게 지역별 매출 구조를 살펴본 후, 저희는 실제 코로나가 터진 이후의 매출 구조 역시 알아보고 싶었습니다. 따라서 코로나 전후의 매출 비교가 가능한 추가 데이터를 가져오게 되었고, 해당 데이터에는 2020년 1월부터 6월까지의 지역별 카드 매출이 나와있습니다. 

![카드 매출 데이터 겨울 봄 비교 밑에 있는 코드 뭔지 모름](https://user-images.githubusercontent.com/68367334/92301584-ed66d780-ef9f-11ea-9cde-96f9e6051bce.png)

여기에서의 문제점은, 지역구별로 절대적인 매출량의 차이가 커 단적으로 비교하기가 힘들다는 것이었습니다. 따라서 저희는 겨울 대비 봄의 매출을 퍼센테이지로 나타내어 비교를 가능케 하였습니다.  즉, 해당 구의 겨울 매출을 100으로 잡았을 때의 봄 매출의 상대 비율을 구하였습니다.

### 2020년 카드 매출 데이터 추가 

> [2020년 지역 별 겨울 봄 매출 비교]
![9 2020년 지역별 겨울 봄 매출 비교](https://user-images.githubusercontent.com/68261338/92301445-04f19080-ef9f-11ea-97e0-7c95d0d7c1ee.jpg)

최종적으로 19년도 봄의 매출과 20년도의 봄 매출을 비교하고자 하였으나, 가장 큰 문제는 데이터 별로 매출액 단위가 다르게 설정되어 있어 단적인 비교가 힘들다는 점이었습니다. 따라서 저희는 19년도 대비 20년도의 매출 증감량이 지수로 나와있는 데이터를 추가적으로 사용하게 되었습니다. 

저희는 19년도와 20년도의 겨울 대비 봄 매출의 퍼센테이지에 각각 해당 시기의 매출 지수를 곱해주면서, 비교를 가능한 형태로 변형시켰습니다. 

![물가지수 데이터 1901,1902_2001,2002_19 20 비교 코드 및 표](https://user-images.githubusercontent.com/68367334/92301593-ff487a80-ef9f-11ea-929a-eaa0256cf30c.jpg)

하지만, 여기서의 실수는 저희가 사용한 지수 데이터는 19년도 대비 20년도의 물가 지수를 나타내고 있었던 반면 매출 데이터는 18,19년도의 평균과 20년도의 평균 매출량이었다는 것입니다. 18년도의 매출이 평균에 들어가 있다는 것을 고려하지 못하고 단순히 지수를 사용한 것은 이후 프로젝트가 끝난 후 저희가 꼽았던 가장 큰 문제점 중 하나가 되었습니다. 

> [2019년 봄 대비 2020년 봄 매출 변화량 비교]
![10 2019봄_2020봄 매출변화량 비교](https://user-images.githubusercontent.com/68261338/92301884-564f4f00-efa2-11ea-8759-7dbc4db0b802.jpg)

결과적으로 모든 구에서 작년 봄 대비 올해 봄에 많은 매출 하락을 기록한 것을 발견할 수 있었습니다. 

----------------------------------

### 유동인구 및 주민등록상 인구에 따른 분석

위의 결론을 보아 실제로 사람들의 소비 활동이 활발해지는 봄에 매출이 평균적으로 겨울보다 높다는 것을 확인하였으며, 추가적으로 코로나로 인해 봄 매출이 많은 타격을 입었다는 사실을 발견하였습니다. 
여기에서 하나 더 나아가 사람들의 활동성이 높은 계절의 매출이 높다는 것은 사람들의 유동성과도 연관이 있을 수 있겠다는 생각을 하였습니다. 따라서 저희는 유동인구 데이터를 추가적으로 사용하게 되었습니다.
 
 > [2020년 유동인구]
![11 2020 01-2020 04 주중 주말 유동인구 전체_SK](https://user-images.githubusercontent.com/68261338/92301450-0a4edb00-ef9f-11ea-9aba-08059d06018b.png)

하지만, 단순히 유동인구가 높은 지역이 매출이 높다는 사실을 파악하는 것은 코로나 상황에 있어서 큰 도움이 되지 않는다고 생각했습니다. 따라서 유동인구의 증감량과 매출의 변화 추이를 비교해 보았습니다. 이 부분에서 나온 궁금증은 유동인구 자체의 감소량은 강남, 서초, 동대문구가 모두 높았으나 그 중에서도 동대문구의 매출이 많이 하락했다는 점이었습니다.

> [의약품 도매업 분포도]
![13 의약품 도매업 분포도_18](https://user-images.githubusercontent.com/68261338/92301455-0c189e80-ef9f-11ea-9437-211582b13669.jpg)

이는 저희가 앞서 알아보았던 도매업 비중이 큰 동대문구의 매출이 많이 하락했다는 것을 의미하기도 합니다. 따라서 이에 대한 이유를 찾던 중, 다음과 같은 논문 결론을 발견하였고 이에 저희는 유동인구와 더불어 상주인구 (즉, 주민등록상 인구) 역시 살펴 보아야 한다고 생각했습니다. 

<img width="840" alt="그림1" src="https://user-images.githubusercontent.com/62180861/92465426-88aeb580-f209-11ea-994f-9b62c0bba782.png">

_출처 : 정재훈, 남진. (2019) "위치기반 빅데이터를 활용한 서울시 활동 인구 유형 및 유형별 지역 특성 분석"_


![유동인구 주민등록상 인구 비교 코드 및 표 이걸로_상주대비유동변화량 까지 나타낸 코드 및 표](https://user-images.githubusercontent.com/68367334/92301613-125b4a80-efa0-11ea-84bf-d0dcf14cd576.png)

> [지역구별 1년 평균 주민등록 등록인구수 대비 유동인구]
![14 지역구별 1년평균 주민등록 등록인구수 대비 유동인구](https://user-images.githubusercontent.com/68261338/92301456-0d49cb80-ef9f-11ea-8194-7540f63e72f3.jpg)
 

여기에서 알아낸 사실은 상주 대비 유동인구가 높을수록 오히려 매출의 영향 타격이 작다는 사실을 발견하였습니다. 하지만, 한가지 튀는 점은 상주 대비 유동인구가 매우 높은 2 지역, 중구와 종로구의 매출 하락은 굉장히 컸다는 점이었습니다. 

중구와 종로구의 경우 상주 대비 유동인구가 매우 높은 지역이지만, 이는 단순히 유동인구 수가 타 지역 대비 높기 때문이 아니였습니다.
구도심 지역인 이 지역들은 기본적으로 주민등록상의 인구가 매우 적기 때문에 유동인구의 영향을 많이 받는 것이었습니다.
따라서 저희는 어떤 요인이 이 지역의 유동인구 변화에 많은 영향을 끼쳤을까 분석을 해 보았습니다.
단순히 사회적 거리두기로 인해 유동인구가 줄었다는 현상은 다른 지역도 마찬가지 였기 때문에, 유동인구에 미친 다른 요인이 있을 것으로 생각하였기 때문입니다.

결과적으로, 중구와 종로구의 유동인구 및 매출은 관광 및 쇼핑의 영향을 많이 받는다는 사실을 알게 되었습니다. 

![15 서울시 외국인 관광객 통계](https://user-images.githubusercontent.com/68261338/92301457-0e7af880-ef9f-11ea-8644-8f3f757b667e.jpg)

실제로 종로구와 중구는 외국인 관광객 수 1,2위를 차지하고 있는 지역으로 코로나로 인해 외국인 관광 인구가 기하급수적으로 줄면서 이런 형상이 발생하게 된 것입니다. 이 현상은 실제 숙박업의 분포를 보아도 같은 결과를 나타내고 있다는 사실 역시 파악할 수 있었습니다.

추가적으로, 종로와 중구의 매출에 큰 영향을 끼치는 도매업이 의류 산업이라는 사실도 주목해 볼 만 합니다. 의류 산업 자체가 쇠퇴하면서 매출 하락에 큰 영향을 끼쳤으며, 의류 산업의 주 고객층이었던 중국인 관광객 수가 99프로 이상 감소했다는 사실 또한 같은 결과를 말해주고 있습니다.
_(출처 : <https://www.donga.com/news/Culture/article/all/20200522/101175841/1> )_

> [숙박업 분포도]
![16 숙박업 분포도_18](https://user-images.githubusercontent.com/68261338/92301459-0fac2580-ef9f-11ea-9d4b-c87642eb5b69.jpg)

> [의복 및 악세서리 도매업 분포도]
![17 의복 악세서리 도매업](https://user-images.githubusercontent.com/68261338/92301461-10dd5280-ef9f-11ea-8690-3e5b9c192c4d.jpg)

> [셔프 및 그 외 의류 도매업 분포도]
![18 셔츠 및 그 외 도매업](https://user-images.githubusercontent.com/68261338/92301462-1175e900-ef9f-11ea-88c9-d39cfe56bed1.jpg)

--------------------------------------------------------------------------------------------------------


최종적으로, 저희는 19 봄 매출 대비 20 봄 매출의 증감량을 유동인구 및 주민등록상 인구와 관련이 있다는 사실을 보다 쉽게 보여주기 위한 시각화를 진행하였습니다. 각 지역별 간의 관계를 한눈에 보여주기 위해 scatter plot을 사용하였습니다.
결과적으로, 단순히 유동인구나 주민등록상의 인구와 매출의 증감은 높은 선형성을 보이지 않았으나, 주민등록상 인구 대비 유동인구를 변수로 설정한 경우 매출의 증감과의 어느정도 선형성을 보이며, 중구와 종로구가 outlier로 존재한다는 것까지 시각화할 수 있었습니다.

> [유동 인구와 매출 증감량 관계]
![19 유동인구 매출](https://user-images.githubusercontent.com/68261338/92301465-18046080-ef9f-11ea-9b89-aa41dda04679.jpg)

> [주민등록상 인구와 매출 증감량 관계]
![20 상주인구 매출](https://user-images.githubusercontent.com/68261338/92301467-189cf700-ef9f-11ea-9723-dab4756ddde7.jpg)

> [주민등록 인구 수 대비 유동인구와 매출 증감량 관계]
![21 주민등록 등록 인구수 대비 유동인구와 매출 변화량 스캐터](https://user-images.githubusercontent.com/68261338/92301468-19ce2400-ef9f-11ea-981f-21bbf3d0826a.jpg)


# 가설 검증 

> ## 1. 가설 검증
1) 시간별 매출양이 나온 데이터: 주말이 평일보다 매출이 높을 것이다. 그래서 하락도 주말에 관련된 업종(산업)의 하락률이 컸을 것이다. (요식업)
> > 건당 매출이 높은 의약품 도매업 거래가 평일에 이루어졌기 때문에 하루 매출 량과 거래 건수가 평일이 주말보다 높았다. 이를 통해 안 사실은 카드 매출에서도 B2C 보다 B2B가 미치는 영향이 높다는 것을 깨달았습니다. 

2) 새벽 오전 오후 저녁으로 나눔. 일과가 끝난 후 활동 시간인 저녁때 매출이 높을 것으로 예상하여 저녁 결제 건수, 건당 결제 금액 둘다 저녁이 높을 거라 예상하였습니다. 
> > 오후 저녁 오전 새벽 순으로 거래 총 금액이 높았으며 오후 저녁 새벽 오전 순으로 결제 건수가 높았습니다. 
하지만 건당 결제 금액은 오전 오후 저녁 새벽 순으로 높았습니다. 이를 통해 오후와 저녁에 활동이 많았다는 점과 반대로 오전에 건당 결제 금액이 높다는 것을 알았습니다. 이는 위를 통해 알게된 의약품 도매업 거래의 영향이 크다는 이유 입니다.

3) 계절별로 보면 봄의 매출이 겨울보다 높을 것으로 예상 (활동성이 높은 계절이니) 그런데 코로나가 봄에 터졌으니 매출의 전반적인 타격은 클 것으로 예상하였습니다. 
> > 금천구, 은평구, 종로구 제외한 다른 지역들은 위의 가설과 같이 겨울보다 봄의 매출의 하락율이 컸습니다. 이는 코로나 영향이 크다는 점을 확실히 알 수 있는 부분이었습니다.

4) 활동성이 높은 계절에 타격이 컸을 거라 예상을 했기때문에 활동성과 관련이 있는 유동인구 변화에 대한 타격이 있을 거라 예상
> > 강서구와 같이 겨울 대비 봄 매출 변화량은 컸지만 유동인구 변화량과 관련이 크지 않은 지역도 있었습니다. 이에 유동인구 변화량에 따라 매출 변화량을 확인했을 때 선형관계가 뚜렷이 나오지 않았습니다. 위의 이유에 따라 강서구 같은 지역의 매출변화량의 이유를 알기 위해 주민등록 인구 대비 유동인구 변화량을 확인했고 주민등록 인구 대비 유동인구가 적은 지역의 매출 변화량이 크다는 것을 확인했습니다. 
   그 결과 유동인구만이 영향을 미치는 것이 아닌 상주인구 대비 유동인구가 매출에 영향을 미친다는 사실을 알게 됐습니다.
   

> ## 2. 데이터로 알게 된 추가적인 사실
1) 코로나 사태로 인해 관광산업에 대한 매출의 하락율이 크다는 사실을 알게 됐습니다.
2) 주민등록 인구 대비 유동인구 변화량에 제일 큰 영향을 받은 지역은 종로와 중구였다. 이에 종로와 중구의 특성을 분석해본 결과 이 두 지역은 외국인 관광객이 많이 다니는 관광 지점이 모여있었습니다.
3) 실제로 관광과 관련된 숙박업 및 외국인 관광객이 많이 이용하는 의류 산업들이 종로, 중구를 중심으로 분포되 있었다는 사실과 그에 따른 매출 감소도 크다는 것을 통계자료 및 분포 지도 데이터로 알 수 있었습니다.

# 결론

* 첫째, 거래 단위가 큰 도매업이 하락한 지역이 높은 매출 하락을 기록하였습니다.
* 둘째, 외국인 관광객들이의 국내 유입이 불가능해지면서 관광 산업이 큰 타격을 받았고, 이에 숙박과 (관광객 비중이 큰 지역의) 의류 산업 역시 많은 매출 감소를 기록하였습니다.
* 셋째, 주민등록인구 대비 유동인구가 적은 지역이 (즉, 주거 기반 자치구가) 높은 매출 하락을 보였다는 것입니다.
* 넷째, 매년 겨울 대비 봄 매출이 높았으나 코로나로 인해 2020년은 봄 매출의 하락이 높다는 것입니다.

> 따라서 저희는 다음과 같은 제언을 하고자 합니다.

* 하나, 이미 매출에 큰 영향을 준 요소들을 파악한 바, 해당 요소들인 관광산업에 강한 영향력을 발휘하는 지역에 정책적으로 지원 필요합니다.
* 하나, 주거 기반 지역에 특화된 자치구별 지원이 필요합니다.
* _위와 같은 경제 활성화 정책은 2020 코로나 상황이 발생하지 않았을 경우를 가정한 해당 요소들의 데이터를 예상해, 코로나가 발생하지 않았을 때의 매출량을 예측하고 이와 실제 2020 코로나가 터진 경우의 매출량을 비교해 지원 금액 규모를 결정해 실행해야 합니다._

# 한계점 
1) 너무 많은 요소가 영향을 미치기 때문에 결과가 유기적이었습니다. 즉, 완벽한 선형성을 보이는 요소를 찾는 것이 불가능하였습니다. 그러다보니, 예외 상황을 설명하는 변수를 찾기 위해서 계속 다양한 데이터들을 파고들었고, 이로 인해 설명되지 않는 상황들이 생겨나게 되었다는 것이 가장 큰 한계점이었습니다.
2) 데이터를 수집하는 과정에서 각 데이터 구조가 달라 (예. 돈의 단위, 지역 구분 단위 등) 처리하는 과정이 오래 걸렸다는 점입니다.
3) 한정적인 데이터로 분석을 하여 결측치를 해결할 수 있는 방법이 없었다는 것이 아쉬움으로 남았습니다. (도봉구가 데이터가 존재하지 않아서 비교가 불가능하였습니다.)
4) 직접 구할 수 있는 데이터는 한정적이면서 뻔했기 때문에 참신한 결론을 도출해내기 어려웠습니다. 매출이라는 데이터는 다루는 범위가 넓다보니 영향을 미치는 색다른 변수를 결정하기가 힘들었다고 생각합니다.
