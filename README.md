# store_list
print store sale pruduct list by python crawling

---
### 2020-07-31

##### Complete
- crawling
- test table에 python으로 insert

##### Todolist
- write_item table 구성 파악
- 프렌차이즈는 이미지 링크가 없던데 어케 찾는지 파악
- rds 데이터베이스에 실제 처럼 한 이벤트 입력
- 크롤링 돌리면서 전체 데이터 insert
- crontab 사용해서 지정 시간에 크롤링 -> insert 구현

##### Problem
- 작성자가 admin이 입력되지 않는다.

---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
### 2020-08-03

##### Complete
- gs25, emart24 크롤링 완료

##### Todolist
- gs25, emart24 크롤링한 데이터 정규화 시키기

##### add file
+ selenium_test file
+ chromedriver.exe
+ debug.log
+ selenium_test.py
+ t1.py
+ t2.py

---
### 2020-08-04

##### Complete
- cu 크롤링 완료
- 크롤링한 데이터 포매팅 완료
- sale 데이터 별개로 크롤링 완료

##### Todolist
- 주석 처리
- 불필요한 코드 정리
- 비동기 처리로 크롤링 속도 올리기

##### Add file
+ deploy
    + index.py
    + chromedriver.exe
    + franchise
        + p_cu.py
        + p_emart.py
        + p_gs.py
        + s_emart.py
        + modules
            + fm.py

---
### 2020-08-07

##### Complete
- 실제 서버 데이터베이스에 데이터 업로딩 완료
- 파일명 변수명 조금 정리

##### Todolist
- 속도 개선 여러개의 홈페이지를 한번에 크롤링 돌릴 수 있도록
- 세븐 일레븐 추가
- itemlist 1+1, 2+1, 3+1 순서대로 sort

##### Add file
+ insert_check.py
+ insert_data.py
+ sort_items.py
+ plus_seven.py
+ sale_seven.py

---
### 2020-08-10

##### Complete
- 멀티프로세스를 활용해서 병렬 실행 구현 18분에서 9분으로 시간 감축
- remake 폴더에 class로 변형하여 코드 정리
- 리스트 sort 완료

##### Todolist
- gs25 속도가 너무 느려서 시간을 많이 잡아먹음 멀티스레드로 gs만 시간 줄여도 6분까지 시간 감축 가능
- 세븐 일레븐 추가

##### Add file
+ remake

---
### 2020-08-11

##### Complete
- 세븐 일레븐 추가
- 코드 새롭게 정리 완료 franchise_list.json에 필요사항만 입력하면 자동으로 크롤링 및 data insert

##### Todolist
- Insert_data.py 소스코드 정리
- 변수 정리
- gs25 속도 개선
- 펴늬 크롤링 시스템이랑 병합
- 세븐 일레븐 세일 데이터를 주석에 적혀있는 값을 가져와서 입력하려고 해봤지만 13개 상품 이후에는 주석이 없어서 가져오기 실패
    - 세일값은 페이지 하나 하나 들어가서 가져와야할 거 같음
    - 페이지 주소로 하나 하나 이동 가능하도록 처리해놨으니 긁어서 배열에 때려넣고 return만 시켜주면 ok

##### Add file
none

---
### 2020-08-11

##### Complete
- sort 순서 (1+1 ~ sale) 세팅
- 세븐일레븐 세일 데이터 받아와서 뿌려주기까지 완료
- .gitignore 보안 처리

##### Todolist
- 조금씩 코드 정리
- api로 지원가능하도록 제작
    1. 1일 자정이되면 자동으로 DB에 데이터 insert 구조
    1. 데이터 뿌려주는 서버단 api 제작
    1. 배포

- 앱에서 카테고리 분류를 해야할 경우 어떻게 할지 생각해보기

##### Add file
 - folder name change(remake -> dist)