import sys
import os
import random
from collections import Counter

class MetaPathGenerator:
    def __init__(self):
        self.id_user = dict()
        self.id_poi = dict()
        self.id_cate = dict()
        self.id_tl = dict()
        self.poi_userlist = dict()
        self.user_poilist = dict()
        self.poi_catelist = dict()
        self.cate_poilist = dict()
        self.user_tllist = dict()
        self.tl_userlist = dict()
        self.poi_tllist = dict()
        self.tl_poilist = dict()

        self.poi_poilist = dict()

        # self.id_author = dict()
        # self.id_conf = dict()
        # self.author_coauthorlist = dict()
        # self.conf_authorlist = dict()
        # self.author_conflist = dict()
        # self.paper_author = dict()
        # self.author_paper = dict()
        # self.conf_paper = dict()
        # self.paper_conf = dict()
    def readtestdata(self, dirpath):
        self.id_poi.clear()
        self.id_user.clear()
        self.poi_userlist.clear()
        self.user_poilist.clear()

        with open(dirpath + "\\id_user.txt",'r', encoding='ISO-8859-1') as adictfile:
            for line in adictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_user[toks[0]] = toks[1].replace(" ", "")
        #Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
        #id_author={dict}{'89376': 'aRuiJiang', '36606': 'aDanConescu'.....}
        #print "#authors", len(self.id_author)

        with open(dirpath + "\\id_poi.txt",'r', encoding='ISO-8859-1') as cdictfile:
            for line in cdictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_poi[toks[0]] = toks[0]

        with open(dirpath + "\\user_poi.txt",'r', encoding='ISO-8859-1') as pafile:
            for line in pafile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    u, p = toks[0], toks[1]
                    #u:'37',p:'4e3e097552b1a04aff2139ff'
                    if u not in self.user_poilist:
                        self.user_poilist[u] = []
                    self.user_poilist[u].append(p)
                    if p not in self.poi_userlist:
                        self.poi_userlist[p] = []
                    self.poi_userlist[p].append(u)
                #poi_user:{'21525':['33467','33467','33468'}]}
                #user_poi:{'33467':['21525'],'33468':['21525']}

    #构造
    def read_upudata(self, dirpath):
        self.id_poi.clear()
        self.id_user.clear()
        self.poi_userlist.clear()
        self.user_poilist.clear()

        with open(dirpath + "\\id_user.txt",'r', encoding='ISO-8859-1') as adictfile:
            for line in adictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_user[toks[0]] = toks[1].replace(" ", "")
        #Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
        #id_author={dict}{'89376': 'aRuiJiang', '36606': 'aDanConescu'.....}
        #print "#authors", len(self.id_author)

        with open(dirpath + "\\id_poi.txt",'r', encoding='ISO-8859-1') as cdictfile:
            for line in cdictfile:
                toks = line.strip().split("\t")
                if len(toks) == 3:
                    self.id_poi[toks[0]] = toks[0]

        with open(dirpath + "\\user_poi.txt",'r', encoding='ISO-8859-1') as pafile:
            for line in pafile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    u, p = toks[0], toks[1]
                    #u:'37',p:'4e3e097552b1a04aff2139ff'
                    if u not in self.user_poilist:
                        self.user_poilist[u] = []
                    self.user_poilist[u].append(p)
                    if p not in self.poi_userlist:
                        self.poi_userlist[p] = []
                    self.poi_userlist[p].append(u)
                #poi_user:{'21525':['33467','33467','33468'}]}
                #user_poi:{'33467':['21525'],'33468':['21525']}
    def generate_random_upu(self, outfilename, numwalks, walklength):
        outfile = open(outfilename, 'w', encoding="ISO-8859-1")
        for user in self.user_poilist:
            user0 = user
            for j in range(0, numwalks):  # wnum walks以每个起点行走的路径的数量。以poi0为起点，随机numwalks个路径。
                outline = self.id_user[user0]  # outline='vADB'即122会议的名称
                for i in range(0, walklength):  # 行走的长度走一次是一个VAV，走walklength次，长度为2*walklength+1
                    pois = self.user_poilist[user]
                    numa = len(pois)  # numa代表用户u对应的地点个数
                    poiid = random.randrange(numa)
                    poi = pois[poiid]
                    outline += " " + self.id_poi[poi]  # 路径UP

                    users = self.poi_userlist[poi]
                    numa = len(users)  # numa代表该会议122的作者人数38
                    userid = random.randrange(numa)  # 将作者顺序打乱authorid=随机数28每次都不一样，但是为38中的一个数字
                    # authorid = 28
                    # randrange() 方法返回指定递增基数集合中的一个随机数，基数缺省值为1。
                    user = users[userid]  # 随机authorid的作者编号='33491' #将打乱的作者重新放入author
                    outline += " " + self.id_user[user]  # 将会议名称和作者名称以空格连接{'vADB' 'aJ.Maguire'}
                outfile.write(outline + "\n")  # 产生多个PUPUP的序列。
        outfile.close()

    def read_utlpdata(self, dirpath):
        self.id_poi.clear()
        self.id_user.clear()
        self.id_tl.clear()
        self.user_tllist.clear()
        self.tl_userlist.clear()
        self.tl_poilist.clear()
        self.poi_tllist.clear()

        with open(dirpath + "\\id_user.txt",'r', encoding='ISO-8859-1') as adictfile:
            for line in adictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_user[toks[0]] = toks[1].replace(" ", "")

        with open(dirpath + "\\id_poi.txt",'r', encoding='ISO-8859-1') as cdictfile:
            for line in cdictfile:
                toks = line.strip().split("\t")
                if len(toks) == 3:
                    self.id_poi[toks[0]] = toks[0]

        with open(dirpath + "\\id_tl.txt",'r', encoding='ISO-8859-1') as cdictfile:
            for line in cdictfile:
                toks = line.strip().split("\t")
                if len(toks) == 2:
                    self.id_tl[toks[0]] = toks[1]  #tl的id，tl内容
        with open(dirpath + "\\user_tl_poi.txt",'r', encoding='ISO-8859-1') as pafile:
            for line in pafile:
                toks = line.strip().split("\t")
                if len(toks) == 3:
                    u, tl, p = toks[0], toks[1], toks[2]  #tokes[2]是类别名称，toks[3]是类别id
                    #u:'37',p:'4e3e097552b1a04aff2139ff'
                    if u not in self.user_tllist:
                        self.user_tllist[u] = []
                    self.user_tllist[u].append(tl)
                    if tl not in self.tl_userlist:
                        self.tl_userlist[tl] = []
                    self.tl_userlist[tl].append(u)
                    # poi_user:{'21525':['33467','33467','33468'}]}
                    # user_poi:{'33467':['21525'],'33468':['21525']}
                    if p not in self.poi_tllist:
                        self.poi_tllist[p] = []
                    self.poi_tllist[p].append(tl)
                    if tl not in self.tl_poilist:
                        self.tl_poilist[tl] = []
                    self.tl_poilist[tl].append(p)
    def generate_random_utlptlu(self, outfilename, numwalks, walklength):
        outfile = open(outfilename, 'w', encoding="ISO-8859-1")
        for user in self.user_tllist:
            user0 = user
            #随机初始tl0
            tls = self.user_tllist[user]
            tlid0 = random.randrange(len(tls))
            tl0 = tls[tlid0]
            h0 = self.id_tl[tl0][0:2]
            l0 = self.id_tl[tl0][2:]

            for j in range(0, numwalks):
                outline = self.id_user[user0]  #路径U
                for i in range(0, walklength):
                    tls = self.user_tllist[user]
                    numtl = len(tls)
                    while(1):
                        tlid = random.randrange(numtl)
                        tl = tls[tlid]
                        h = self.id_tl[tl][0:2]
                        l = self.id_tl[tl][2:]
                        if abs(int(h)-int(h0)) < 4 and str(l).__eq__(l0):  #时间邻域，上下3个小时
                            outline += " " + tl  #路径U TL
                            h0 = h
                            l0 = l
                            break

                    pois = self.tl_poilist[tl]  #时空对应的地点
                    nump = len(pois)
                    poiid = random.randrange(nump)
                    poi = pois[poiid]
                    outline += " " + self.id_poi[poi]    #路径U TL P

                    tls = self.poi_tllist[poi]
                    numtl = len(tls)
                    while (1):
                        tlid = random.randrange(numtl)
                        tl = tls[tlid]
                        h = self.id_tl[tl][0:2]
                        l = self.id_tl[tl][2:]
                        if abs(int(h) - int(h0)) < 4 and str(l).__eq__(l0):  #时间邻域，上下3个小时
                            outline += " " + tl  # 路径U TL P TL
                            h0 = h
                            l0 = l
                            break
                    # tlid = random.randrange(numtl)
                    # tl = tls[tlid]
                    # outline += " " + self.id_tl[tl]

                    users = self.tl_userlist[tl] # 地点对应的用户
                    numu = len(users)
                    userid = random.randrange(numu)
                    user = users[userid]
                    outline += " " + self.id_user[user]  #路径U TL P TL U
                outfile.write(outline + "\n")
        outfile.close()

dirpath = ".\\data\\upu\\input"
upuoutfilename = ".\\data\\upu\\vector\\random_walks.txt"

# dirpath = ".\\data\\test\\input"
# upuoutfilename = ".\\data\\test\\vector\\random_walks.txt"

utlptlu_dirpath = ".\\data\\utlptlu\\input"
utlptlu_outfilename = ".\\data\\utlptlu\\vector\\random_walks.txt"

if __name__ == "__main__":
    numwalks = 20  #同一个起点开始的路径的数量
    walklength = 10  #路径长度
    mpg = MetaPathGenerator()
    print('ss')

    # mpg.read_upudata(dirpath)
    # mpg.generate_random_upu(upuoutfilename, numwalks, walklength)

    # mpg.read_utlpdata(utlptlu_dirpath)
    # mpg.generate_random_utlptlu(utlptlu_outfilename, numwalks, walklength)

