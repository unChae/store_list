# store_list
print store sale pruduct list by python crawling

---
2020-07-31

###Complete
- crawling
- test table에 python으로 insert

###Todolist
- write_item table 구성 파악
- 프렌차이즈는 이미지 링크가 없던데 어케 찾는지 파악
- rds 데이터베이스에 실제 처럼 한 이벤트 입력
- 크롤링 돌리면서 전체 데이터 insert
- crontab 사용해서 지정 시간에 크롤링 -> insert 구현

###Problem
- 작성자가 admin이 입력되지 않는다.

---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
2020-08-03

###Complete
- gs25, emart24 크롤링 완료

###Todolist
- gs25, emart24 크롤링한 데이터 정규화 시키기

###add file
+ selenium_test file
+ chromedriver.exe
+ debug.log
+ selenium_test.py
+ t1.py
+ t2.py

---
2020-08-04

###Complete
- cu 크롤링 완료
- 크롤링한 데이터 포매팅 완료
- sale 데이터 별개로 크롤링 완료

###Todolist
- 주석 처리
- 불필요한 코드 정리
- 비동기 처리로 크롤링 속도 올리기

###add file
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
2020-08-07

###Complete
- 실제 서버 데이터베이스에 데이터 업로딩 완료
- 파일명 변수명 조금 정리

###Todolist
- 속도 개선 여러개의 홈페이지를 한번에 크롤링 돌릴 수 있도록
- 세븐 일레븐 추가
- itemlist 1+1, 2+1, 3+1 순서대로 sort

###add file
+ insert_check.py
+ insert_data.py
+ sort_items.py
+ plus_seven.py
+ sale_seven.py

