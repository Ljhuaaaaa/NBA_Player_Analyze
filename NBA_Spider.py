#!/usr/bin/env python
# coding: utf-8
# author: LJH


from selenium import webdriver
from lxml import etree
import time
import pandas as pd
import os



class NbaSpider():
    """NBA中文网球员信息爬虫"""

    def __init__(self,url):
        self.url = url
        self.nba_list = list()
        self.all_nba = list()
        self.player_information = list()
        self.columns = ['name','team','location','height','weight','year','country','url','changshu'\
                        ,'xianfa','fenzhong','mingzhonglv','sanfen','faqiu','jingong','fanshou','defen'\
                            ,'lanban','zhugong','qiangduan','gaimao','shiwu','fangui']
        self.columns_num = 23
        self.filepath = r'C:\Users\Administrator\Desktop\nba_player.csv'

    def login_nba(self):
        """登陆NBA中文网"""
        global browser
        browser = webdriver.Chrome()
        browser.get(self.url)
    
    def get_one_page(self):
        """爬取当前页的数据"""
        one_list = list()
        one_response = browser.page_source
        one_html = etree.HTML(one_response)
        one_items = one_html.xpath('//div[@class="nba-stat-table__overflow"]/table/tbody/tr')
        for one_item in one_items:
            name = one_item.xpath('./td[2]/text()')
            team = one_item.xpath('./td[3]/a/text()')
            location = one_item.xpath('./td[4]/text()')
            height = one_item.xpath('./td[5]/text()')
            weight = one_item.xpath('./td[6]/text()')
            year = one_item.xpath('./td[7]/text()')
            country = one_item.xpath('./td[8]/text()')
            url = one_item.xpath('./td/a[2]/@href')
            info_url = ['https://china.nba.com/' + u for u in url]
            #添加到列表中
            one_list.append([name,team,location,height,weight,year,country,info_url])
            
        return one_list
    
    def get_all_page(self,pages):
        """遍历所有页面"""
        for page in range(pages):
            button =browser.find_element_by_xpath('//*[@id="main-container"]/div/div[2]/div[2]/section/div/div\
                                                  /div/div/div[3]/div[2]/div[2]/div[{}]'.format(page+1))
            button.click()
            time.sleep(5)
            one_list = self.get_one_page()
            if one_list:
                self.nba_list.append(one_list)
            else:
                pass
        browser.close()
    
    def get_info(self):
        """获取球员详情页数据"""
        
        #转化为二维列表
        for i in range(len(self.nba_list)):
            for j in range(len(self.nba_list[i])):
                self.all_nba.append(self.nba_list[i][j])
        
        browser1 = webdriver.Chrome()
        
        #提取球员详情页url
        for k in range(len(self.all_nba)):
            player_url = self.all_nba[k][-1][0]
            browser1.get(player_url)
            time.sleep(18)
            try:
                player_button = browser1.find_element_by_xpath('//*[@id="main-container"]/div/div[2]/div[2]\
                                                               /section/div/div[1]/div/div[1]/div[1]/a[2]/div')
                player_button.click()
                time.sleep(18)
                player_response = browser1.page_source
                player_html = etree.HTML(player_response)
                #场数
                changshu = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                             /div/div[1]/table/tfoot/tr/td[3]/text()')
                #先发
                xianfa = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                           /div/div[1]/table/tfoot/tr/td[4]/text()')
                #分钟
                fenzhong = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                             /div/div[1]/table/tfoot/tr/td[5]/text()')
                #%
                mingzhonglv = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                                /div/div[1]/table/tfoot/tr/td[6]/text()')
                #三分%
                sanfen = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                           /div/div[1]/table/tfoot/tr/td[7]/text()')
                #罚球%
                faqiu = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                          /div/div[1]/table/tfoot/tr/td[8]/text()')
                #进攻
                jingong = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                            /div/div[1]/table/tfoot/tr/td[9]/text()')
                #防守
                fanshou = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                            /div/div[1]/table/tfoot/tr/td[10]/text()')
                #场均得分
                defen = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                          /div/div[1]/table/tfoot/tr/td[11]/text()')
                #场均篮板
                lanban = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                           /div/div[1]/table/tfoot/tr/td[12]/text()')
                #场均助攻
                zhugong = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                            /div/div[1]/table/tfoot/tr/td[13]/text()')
                #场均抢断
                qiangduan = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                              /div/div[1]/table/tfoot/tr/td[14]/text()')
                #场均盖帽
                gaimao = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                           /div/div[1]/table/tfoot/tr/td[15]/text()')
                #失误
                shiwu = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                          /div/div[1]/table/tfoot/tr/td[16]/text()')
                #犯规
                fangui = player_html.xpath('//*[@id="single_player_stats"]/div[1]/div[1]/div[3]/nba-stat-table\
                                           /div/div[1]/table/tfoot/tr/td[17]/text()')
            except:
                pass
            else:
                #添加到列表中
                self.all_nba[k].append(changshu)
                self.all_nba[k].append(xianfa)
                self.all_nba[k].append(fenzhong)
                self.all_nba[k].append(mingzhonglv)
                self.all_nba[k].append(sanfen)
                self.all_nba[k].append(faqiu)
                self.all_nba[k].append(jingong)
                self.all_nba[k].append(fanshou)
                self.all_nba[k].append(defen)
                self.all_nba[k].append(lanban)
                self.all_nba[k].append(zhugong)
                self.all_nba[k].append(qiangduan)
                self.all_nba[k].append(gaimao)
                self.all_nba[k].append(shiwu)
                self.all_nba[k].append(fangui)
            print(player_url,changshu,xianfa,fenzhong,mingzhonglv,sanfen,faqiu\
                  ,jingong,fanshou,defen,lanban,zhugong,qiangduan,gaimao,shiwu,fangui)
    
    def deal_save_data(self):
        """处理和储存数据"""
        #把[]删掉
        for player_if in self.all_nba:
            player = list()
            for num in range(len(player_if)):
                if player_if[num]:
                    player.append(player_if[num][0])
                else:
                    pass
            
            #规整数据
            if len(player) != self.columns_num:
                for i in range(len(player),self.columns_num):
                    player.append('0')
                    
            self.player_information.append(player)
        #DataFrame
        nba_player = pd.DataFrame(self.player_information,columns=self.columns)
        #保存数据
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
        pd.DataFrame.to_csv(nba_player,self.filepath,',',index=False)

if __name__ == '__main__':
    nbaspider = NbaSpider("https://china.nba.com/playerindex/")
    nbaspider.login_nba()
    time.sleep(6)
    nbaspider.get_all_page(26)
    nbaspider.get_info()
    nbaspider.deal_save_data()

