import sys
import os
import random
from collections import Counter

class MetaPathGenerator:
    def __init__(self):
        self.id_user = dict()
        self.id_loc = dict()
        self.id_cate = dict()
        self.id_time = dict()
        self.cate_userlist = dict()
        self.user_catelist = dict()
        self.time_userlist = dict()
        self.user_timelist = dict()
        self.time_catelist = dict()
        self.cate_timelist = dict()
        self.loc_userlist = dict()
        self.user_loclist = dict()
        self.loc_catelist = dict()
        self.cate_loclist = dict()
    # def readtestdata(self, dirpath):
    #     self.id_poi.clear()
    #     self.id_user.clear()
    #     self.poi_userlist.clear()
    #     self.user_poilist.clear()
    #
    #     with open(dirpath + "\\id_user.txt",'r', encoding='ISO-8859-1') as adictfile:
    #         for line in adictfile:
    #             toks = line.strip().split("\t")
    #             if len(toks) == 2:
    #                 self.id_user[toks[0]] = toks[1].replace(" ", "")
    #
    #     with open(dirpath + "\\id_poi.txt",'r', encoding='ISO-8859-1') as cdictfile:
    #         for line in cdictfile:
    #             toks = line.strip().split("\t")
    #             if len(toks) == 2:
    #                 self.id_poi[toks[0]] = toks[0]
    #
    #     with open(dirpath + "\\user_poi.txt",'r', encoding='ISO-8859-1') as pafile:
    #         for line in pafile:
    #             toks = line.strip().split("\t")
    #             if len(toks) == 2:
    #                 u, p = toks[0], toks[1]
    #                 #u:'37',p:'4e3e097552b1a04aff2139ff'
    #                 if u not in self.user_poilist:
    #                     self.user_poilist[u] = []
    #                 self.user_poilist[u].append(p)
    #                 if p not in self.poi_userlist:
    #                     self.poi_userlist[p] = []
    #                 self.poi_userlist[p].append(u)

    #构造
    def read_ucudata(self, dirpath):
        self.id_cate.clear()
        self.id_user.clear()
        self.cate_userlist.clear()
        self.user_catelist.clear()

        with open(dirpath + "\\id_user.txt",'r', encoding='ISO-8859-1') as adictfile:
            for line in adictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_user[toks[1].replace(" ", "")] = toks[1].replace(" ", "")

        with open(dirpath + "\\id_category.txt",'r', encoding='ISO-8859-1') as cdictfile:
            for line in cdictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_cate[toks[0].replace(" ", "").replace("\n", "")] = toks[1].replace(" ", "")

        with open(dirpath + "\\user_category.txt",'r', encoding='UTF-8') as pafile:
            for line in pafile:
                toks = line.split("\t")
                if len(toks) == 2 and len(toks[1]) != 0:
                    u, c = toks[0].replace(" ", ""), toks[1].replace(" ", "").replace("{", "").replace("}", "").replace("\"", "").replace("\n", "")
                    #u:'37',p:'4e3e097552b1a04aff2139ff'
                    cate = c.split(',')

                    if u not in self.user_catelist:
                        self.user_catelist[u] = []
                    for i in range(0,len(cate)):
                        self.user_catelist[u].append(cate[i])

                    for i in range(0,len(cate)):
                        if cate[i] not in self.cate_userlist:
                            self.cate_userlist[cate[i]] = []
                        self.cate_userlist[cate[i]].append(u)

    def generate_random_ucu(self, outfilename, numwalks, walklength):
        outfile = open(outfilename, 'w', encoding="ISO-8859-1")
        for user in self.user_catelist:
            user0 = user
            for j in range(0, numwalks):
                outline = self.id_user[user0]
                for i in range(0, walklength):
                    cates = self.user_catelist[user]
                    numa = len(cates)
                    cateid = random.randrange(numa)
                    cate = cates[cateid]
                    outline += " " + self.id_cate[cate]

                    users = self.cate_userlist[cate]
                    numa = len(users)
                    userid = random.randrange(numa)
                    user = users[userid]
                    outline += " " + self.id_user[user]
                outfile.write(outline + "\n")
        outfile.close()

    # def read_utlpdata(self, dirpath):
    #     self.id_poi.clear()
    #     self.id_user.clear()
    #     self.id_tl.clear()
    #     self.user_tllist.clear()
    #     self.tl_userlist.clear()
    #     self.tl_poilist.clear()
    #     self.poi_tllist.clear()
    #
    #     with open(dirpath + "\\id_user.txt",'r', encoding='ISO-8859-1') as adictfile:
    #         for line in adictfile:
    #             toks = line.strip().split("\t")
    #             if len(toks) == 2:
    #                 self.id_user[toks[0]] = toks[1].replace(" ", "")
    #
    #     with open(dirpath + "\\id_poi.txt",'r', encoding='ISO-8859-1') as cdictfile:
    #         for line in cdictfile:
    #             toks = line.strip().split("\t")
    #             if len(toks) == 3:
    #                 self.id_poi[toks[0]] = toks[0]
    #
    #     with open(dirpath + "\\id_tl.txt",'r', encoding='ISO-8859-1') as cdictfile:
    #         for line in cdictfile:
    #             toks = line.strip().split("\t")
    #             if len(toks) == 2:
    #                 self.id_tl[toks[0]] = toks[1]  #tl的id，tl内容
    #     with open(dirpath + "\\user_tl_poi.txt",'r', encoding='ISO-8859-1') as pafile:
    #         for line in pafile:
    #             toks = line.strip().split("\t")
    #             if len(toks) == 3:
    #                 u, tl, p = toks[0], toks[1], toks[2]  #tokes[2]是类别名称，toks[3]是类别id
    #                 #u:'37',p:'4e3e097552b1a04aff2139ff'
    #                 if u not in self.user_tllist:
    #                     self.user_tllist[u] = []
    #                 self.user_tllist[u].append(tl)
    #                 if tl not in self.tl_userlist:
    #                     self.tl_userlist[tl] = []
    #                 self.tl_userlist[tl].append(u)
    #                 # poi_user:{'21525':['33467','33467','33468'}]}
    #                 # user_poi:{'33467':['21525'],'33468':['21525']}
    #                 if p not in self.poi_tllist:
    #                     self.poi_tllist[p] = []
    #                 self.poi_tllist[p].append(tl)
    #                 if tl not in self.tl_poilist:
    #                     self.tl_poilist[tl] = []
    #                 self.tl_poilist[tl].append(p)
    # def generate_random_utlptlu(self, outfilename, numwalks, walklength):
    #     outfile = open(outfilename, 'w', encoding="ISO-8859-1")
    #     for user in self.user_tllist:
    #         user0 = user
    #         #随机初始tl0
    #         tls = self.user_tllist[user]
    #         tlid0 = random.randrange(len(tls))
    #         tl0 = tls[tlid0]
    #         h0 = self.id_tl[tl0][0:2]
    #         l0 = self.id_tl[tl0][2:]
    #
    #         for j in range(0, numwalks):
    #             outline = self.id_user[user0]  #路径U
    #             for i in range(0, walklength):
    #                 tls = self.user_tllist[user]
    #                 numtl = len(tls)
    #                 while(1):
    #                     tlid = random.randrange(numtl)
    #                     tl = tls[tlid]
    #                     h = self.id_tl[tl][0:2]
    #                     l = self.id_tl[tl][2:]
    #                     if abs(int(h)-int(h0)) < 4 and str(l).__eq__(l0):  #时间邻域，上下3个小时
    #                         outline += " " + tl  #路径U TL
    #                         h0 = h
    #                         l0 = l
    #                         break
    #
    #                 pois = self.tl_poilist[tl]  #时空对应的地点
    #                 nump = len(pois)
    #                 poiid = random.randrange(nump)
    #                 poi = pois[poiid]
    #                 outline += " " + self.id_poi[poi]    #路径U TL P
    #
    #                 tls = self.poi_tllist[poi]
    #                 numtl = len(tls)
    #                 while (1):
    #                     tlid = random.randrange(numtl)
    #                     tl = tls[tlid]
    #                     h = self.id_tl[tl][0:2]
    #                     l = self.id_tl[tl][2:]
    #                     if abs(int(h) - int(h0)) < 4 and str(l).__eq__(l0):  #时间邻域，上下3个小时
    #                         outline += " " + tl  # 路径U TL P TL
    #                         h0 = h
    #                         l0 = l
    #                         break
    #                 # tlid = random.randrange(numtl)
    #                 # tl = tls[tlid]
    #                 # outline += " " + self.id_tl[tl]
    #
    #                 users = self.tl_userlist[tl] # 地点对应的用户
    #                 numu = len(users)
    #                 userid = random.randrange(numu)
    #                 user = users[userid]
    #                 outline += " " + self.id_user[user]  #路径U TL P TL U
    #             outfile.write(outline + "\n")
    #     outfile.close()

dirpath = ".\\data\\ucu\\input"
upuoutfilename = ".\\data\\ucu\\vector\\random_walks.txt"

utlptlu_dirpath = ".\\data\\utlptlu\\input"
utlptlu_outfilename = ".\\data\\utlptlu\\vector\\random_walks.txt"

if __name__ == "__main__":
    numwalks = 20  #同一个起点开始的路径的数量
    walklength = 10  #路径长度
    mpg = MetaPathGenerator()

    mpg.read_ucudata(dirpath)
    mpg.generate_random_ucu(upuoutfilename, numwalks, walklength)

    # mpg.read_utlpdata(utlptlu_dirpath)
    # mpg.generate_random_utlptlu(utlptlu_outfilename, numwalks, walklength)

