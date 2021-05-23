import os, django
from selenium.common.exceptions import NoSuchElementException
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moviepalette.settings')
django.setup()
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request as req
import collections
from konlpy.tag import Okt
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pylab as plt
from matplotlib import font_manager, rc
from movies.models import Movie


# 모든 영화 리스트를 돌면서 title 뽑고 아래의 로직 돌기
# -> 크롤링 결과 txt 파일과 워드클라우드 png 파일이 생긴다
movie_red = Movie.objects.filter(custom_genre=1)
movie_orange = Movie.objects.filter(custom_genre=2)
movie_yellow = Movie.objects.filter(custom_genre=3)
movie_greenyellow = Movie.objects.filter(custom_genre=4)
movie_green = Movie.objects.filter(custom_genre=5)
movie_bluegreen = Movie.objects.filter(custom_genre=6)
movie_blue = Movie.objects.filter(custom_genre=7)
movie_darkblue = Movie.objects.filter(custom_genre=8)
movie_purple = Movie.objects.filter(custom_genre=9)
movie_redpurple = Movie.objects.filter(custom_genre=10)

movies_all = {'PuRd': movie_red, 'OrRd': movie_orange, 'YlOrBr': movie_yellow, 'YlGn': movie_greenyellow, 'Greens': movie_green, 'BuGn': movie_bluegreen, 'Blues': movie_blue, 'BuPu': movie_darkblue, 'Purples': movie_purple, 'RdPu': movie_redpurple}

for key, movies in movies_all.items():
    for movie in movies:
        title = movie.title
# title = '혹성탈출'

        # 자동화 크롬드라이버 실행하기
        url="https://movie.naver.com/"
        driver=webdriver.Chrome("./chromedriver.exe")

        # 크롬 윈도우 창 사이즈 조절하기
        driver.set_window_size(600,900)

        # 설정한 url로 접속하기
        driver.get(url)

        # title = '미나리'
        # 검색창에 영화 제목 검색하고 검색 버튼 클릭 -> 영화 상세 정보 클릭
        element=driver.find_element_by_id('ipt_tx_srch')
        element.send_keys(title)
        driver.implicitly_wait(2)
        try:
            driver.find_element_by_class_name('btn_srch').click()
        except NoSuchElementException:
            continue
            # pass
        try:
            driver.find_element_by_class_name('result_thumb').click()
        except NoSuchElementException:
            continue
            # pass

        # result = []
        # 현재 페이지에서 원하는 요소 값 가져오기: 영화 장르, 줄거리
        # res=req.urlopen(driver.current_url)
        # soup=BeautifulSoup(res,'html.parser')
        # genre = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span:nth-child(1) > a').text
        # detail = soup.find('p', {"class": "con_tx"}).text
        # print(genre)
        # print(detail)

        # 현재 페이지에서 원하는 요소 값 가져오기: 리뷰
        reviews = []
        driver.find_element_by_class_name('tab05').click()
        res=req.urlopen(driver.current_url)
        soup=BeautifulSoup(res,'html.parser')

        # 전문가 평점 / 리뷰
        for i in soup.find_all('div', {"class":"score_reple"}):
            reviews.append(i.find('p').text)   
        for i in soup.find_all('p', {"class":"tx_report"}):
            reviews.append(i.text)

        # 네티즌 평점
        # for i in range(10):
        #     print(soup.find('span', {"id": "_filtered_ment_"+ str(i)}))
        # result.append({'title': title, 'genre': genre, 'detail': detail, 'review': review})

        # txt 파일로 저장하기
        f = open('./files_crawling/' + title + '.txt', 'w', encoding='utf-8')
        for review in reviews:
            f.write(review)
        f.close()

        # 크롬 드라이버 끝내고 결과 확인하기 
        driver.quit()


        # 워드 클라우드 만들기 ============================================
        # 텍스트 명사 
        f = open('./files_crawling/' + title + '.txt', 'r', encoding='utf-8')
        data = f.read()

        if len(data) == 0: 
            continue
            # pass
        okt = Okt()
        noun_data = okt.nouns(data)
            
        # 불용어 제거
        stopword=[]
        word=[i for i in noun_data if i not in stopword]
        word=[i for i in word if len(i)>1]  

        data_cnt=collections.Counter(noun_data) 

        # font_name=font_manager.FontProperties(fname="C:/USERS/USER/APPDATA/LOCAL/MICROSOFT/WINDOWS/FONTS/A옛날사진관3.TTF"). get_name()
        font_name=font_manager.FontProperties(fname="C:/Font/a옛날사진관3.TTF"). get_name()
        rc('font', family=font_name)

        # wc=WordCloud(font_path="C:/USERS/USER/APPDATA/LOCAL/MICROSOFT/WINDOWS/FONTS/A옛날사진관3.TTF", width=900, height=500, colormap = 'RdPu', background_color='white', max_words=100, stopwords=STOPWORDS).generate_from_frequencies(data_cnt)
        wc=WordCloud(font_path="C:/Font/a옛날사진관3.TTF", width=600, height=900, colormap = 'Purples', background_color='white', max_words=100, stopwords=STOPWORDS).generate_from_frequencies(data_cnt)
        # wordcloud.recolor(color_func = "colorbrewer.diverging.Spectral_11")
        wc.to_file('static/'+ title +'.png')
        plt.figure(figsize=(10,10))
        plt.imshow(wc)
        plt.axis('off')
        plt.show(block=False)
        plt.pause(0.3)
        plt.close()
