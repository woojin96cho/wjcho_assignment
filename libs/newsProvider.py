#-*-coding: utf-8-*-
#-*-coding: euc-kr-*-

import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

'''
Reference  :
https://requests.readthedocs.io/en/master/
https://m.boannews.com/html/news.html



'''

# Disable flag warning (Ref : https://stackoverrun.com/ko/q/11748404)
requests.packages.urllib3.disable_warnings()


def get_boanNews():
    with requests.Session() as s:
        before_auth_header = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9'
        }

        cookie = ''
        # Get Cookie Value
        tmp = s.get('https://m.boannews.com/html/news.html?mtype=1&tab_type=1', headers=before_auth_header, verify=False)
        #print(tmp.headers)
        #print(tmp.content)
        cookie = tmp.headers['Set-Cookie']
        #print(cookie)


        cookie_include_header = {
            'Connection': 'keep-alive',
            'Content-Length': '18',
            'Accept': 'text/html, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://m.boannews.com',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://m.boannews.com/html/news.html?mtype=1&tab_type=1',
            'Cookie': cookie
        }

        '''
        <li><a href="detail.html?tab_type=1&idx=91992"><dl><dt>마크애니, 제주도에 인공지능 기반 선별관제 시스템 구축</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/mark_20201023_thumb.jpg" alt=""></dd></dl></a><ul><li><a href="detail.html?tab_type=1&idx=90648">마크애니, 세종시에 안전한 비대면 협업을 위한 VPN 화면보안 솔루션 구축</a></li><li><a href="detail.html?tab_type=1&idx=91772">고양시 시민안전센터, 시민안전 위해 CCTV 영상정보관리 고도화 선택</a></li></ul></li><li><a href="detail.html?tab_type=1&idx=91991"><dl><dt>미래기술연구회 ‘패러 코로나 시대에 정보보호의 역할’ 세미나 개최</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/seminar_102301_main.jpg" alt=""></dd></dl></a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91974"><dl><dt>경남도, ‘지역안전지수 향상 전담팀’ 출범해 안전역량 결집한다</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/10-163(295).jpg" alt=""></dd></dl></a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91990"><dl><dt>산림청, 모바일과 ICT 활용한 산림 현장 업무 혁신</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/10-179(295).jpg" alt=""></dd></dl></a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91989" class="refer">정부, 내년도 재난안전 분야 472개 사업에 19조8000억 투자한다</a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91988"><dl><dt>통계청, 뉴스 빅데이터 기반 통계 자동 검색 대국민 서비스 실시</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/10-177(295).jpg" alt=""></dd></dl></a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91986"><dl><dt>SKT, 부산대병원·스타트업과 손잡고 5G·VR로 치매 예방 나선다</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/10-175(295).jpg" alt=""></dd></dl></a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91985"><dl><dt>LG CNS, 비대면으로 청소년 AI 교육 강화</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/10-174(295).jpg" alt=""></dd></dl></a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91984" class="refer">IFEZ·인천테크노파크, 혁신 기술 보유 스타트업에 실증 기회 제공한다</a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91983" class="refer">삼성SDS, 국내외 AI 경진대회 1위 석권</a><ul></ul></li>
        '''
        # bs4_test_body = '<li><a href="detail.html?tab_type=1&idx=91992"><dl><dt>마크애니, 제주도에 인공지능 기반 선별관제 시스템 구축</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/mark_20201023_thumb.jpg" alt=""></dd></dl></a><ul><li><a href="detail.html?tab_type=1&idx=90648">마크애니, 세종시에 안전한 비대면 협업을 위한 VPN 화면보안 솔루션 구축</a></li><li><a href="detail.html?tab_type=1&idx=91772">고양시 시민안전센터, 시민안전 위해 CCTV 영상정보관리 고도화 선택</a></li></ul></li><li><a href="detail.html?tab_type=1&idx=91991"><dl><dt>미래기술연구회 ‘패러 코로나 시대에 정보보호의 역할’ 세미나 개최</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/seminar_102301_main.jpg" alt=""></dd></dl></a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91974"><dl><dt>경남도, ‘지역안전지수 향상 전담팀’ 출범해 안전역량 결집한다</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/10-163(295).jpg" alt=""></dd></dl></a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91990"><dl><dt>산림청, 모바일과 ICT 활용한 산림 현장 업무 혁신</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/10-179(295).jpg" alt=""></dd></dl></a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91989" class="refer">정부, 내년도 재난안전 분야 472개 사업에 19조8000억 투자한다</a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91988"><dl><dt>통계청, 뉴스 빅데이터 기반 통계 자동 검색 대국민 서비스 실시</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/10-177(295).jpg" alt=""></dd></dl></a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91986"><dl><dt>SKT, 부산대병원·스타트업과 손잡고 5G·VR로 치매 예방 나선다</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/10-175(295).jpg" alt=""></dd></dl></a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91985"><dl><dt>LG CNS, 비대면으로 청소년 AI 교육 강화</dt><dd class="news-img2"><img src="https://www.boannews.com/media/upFiles2/2020/10/10-174(295).jpg" alt=""></dd></dl></a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91984" class="refer">IFEZ·인천테크노파크, 혁신 기술 보유 스타트업에 실증 기회 제공한다</a><ul></ul></li><li><a href="detail.html?tab_type=1&idx=91983" class="refer">삼성SDS, 국내외 AI 경진대회 1위 석권</a><ul></ul></li>'
        # soap = BeautifulSoup(bs4_test_body, 'html.parser')
        # names = soap.findAll('dt')
        # addr = soap.findAll('li')
        # print(names, addr)

        news = []
        for i in range(1, 11):
            all_news_body  = 'tab_type=1&page1='+str(i)
            news_need_parse = s.post('https://m.boannews.com/html/ajaxAllNews.html', headers = cookie_include_header, data = all_news_body)
            #print(news_need_parse.text)
            soap = BeautifulSoup(news_need_parse.text, 'html.parser')
            names = soap.findAll('dt')
            addr = soap.findAll('li')
            for j in range(0, len(names)):
                tmp_name = str(names[j])
                tmp_addr = str(addr[j])
                news_name = tmp_name.replace('<dt>', '').replace('</dt>', '')
                news_addr = "https://m.boannews.com/html/" + tmp_addr.replace('<li>', '').replace('</li>', '').split('href="')[1].split('">')[0].replace('amp;','')
                #print(news_name,news_addr)
                news.append([news_name,news_addr, "보안뉴스"])
        #print(news)


    return news

def get_yonhapNews():
    with requests.Session() as s:
        before_auth_header = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9'
        }


        tmp = s.get('https://m.yna.co.kr/industry/technology-science', headers=before_auth_header, verify=False)
        json_data = json.loads(tmp.text.split('var json = JSON.stringify(')[1].split(');\r\n')[0])
       # json_data = json.loads(str(json_data['TOTAL']['DATA']))
        data = pd.json_normalize(json_data['DATA'])

        news = []
        for i in range(len(data)):
            news.append([data['TITLE'][i], "https://m.yna.co.kr/" + data['URL'][i], "연합뉴스"])

        return news


def get_itworld():
    with requests.Session() as s:
        before_auth_header = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Dest': 'document',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'ko-KR,ko;q=0.9'
        }

        cookie = ''
        # Get Cookie Value
        tmp = s.get('http://www.itworld.co.kr/news?page=1', headers=before_auth_header, verify=False)
        #print(tmp.headers)
        #print(tmp.content)
        cookie = tmp.headers['Set-Cookie']
        #print(cookie)


        cookie_include_header = {
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'ko-KR,ko;q=0.9',
            'Cookie': cookie
        }

        '''
              <h4 class="news_list_full_size news_list_title default_font font_bold font_limit title_h3" title="아이폰 12 프로 심층 리뷰 : 미래를 위한 아이폰">
            <a href="/news/170164">아이폰 12 프로 심층 리뷰 : 미래를 위한 아이폰</a>
            </h4>
        '''
        # bs4_test_body = '<h4 class="news_list_full_size news_list_title default_font font_bold font_limit title_h3" title="아이폰 12 프로 심층 리뷰 : 미래를 위한 아이폰"><a href="/news/170164">아이폰 12 프로 심층 리뷰 : 미래를 위한 아이폰</a></h4>'
        # soap = BeautifulSoup(bs4_test_body, 'html.parser')
        # names = soap.findAll('h4')
        # # addr = soap.findAll('li')
        # print(names)

        news = []
        for i in range(1, 11):
            all_news_body  = 'tab_type=1&page1='+str(i)
            news_need_parse = s.post('http://www.itworld.co.kr/news?page='+str(i), headers = cookie_include_header, data = all_news_body)
            # print(news_need_parse.text)
            soap = BeautifulSoup(news_need_parse.text, 'html.parser')
            names = soap.findAll('h4')
            for j in range(0, len(names)):
                tmp_name = str(names[j])
                tmp_addr = str(names[j]).split('<a href=')[1].split('">')[0]
                news_name = tmp_name.replace('<h4 class="news_list_full_size news_list_title default_font font_bold font_limit title_h3" title="', '').split('">')[0].replace('&amp;', '&')
                news_addr = "http://www.itworld.co.kr" + tmp_addr.replace('"','')
                #print(news_name,news_addr)
                news.append([news_name,news_addr,"ITWorld"])
        #print(news)


    return news
