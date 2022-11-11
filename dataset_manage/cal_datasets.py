import os 
#数据地址
# biaozhutu_dir = input()

biaozhutu_dir = r'\\10.10.1.39\d\FT220005_丰越全车检测\丰越所有数据\标注图'
yuantu_dir = r'\\10.10.1.39\d\FT220005_丰越全车检测\丰越所有数据\原图'

#需计算的日期范围 
biaozhutu_data = range(220831,220901    +1)
# yuantu_data = range(20220909,20220915   +1)
yuantu_data =["20220916晚",
               "20220916白",
                "20220922", 
                "20220923",
                "20220926",
                "20220926晚",
                "20220927",
                "20220928"]

def biaozhutu():
    # print("标注图数量:")
    # print("     ","发图时间","图数量")
    for each_dir in os.listdir(biaozhutu_dir):
        for data in biaozhutu_data:
            if each_dir[5:] == str(data):
                new_dir = biaozhutu_dir + "/" + each_dir
                jpg_list = []
                for each_group in os.walk(new_dir):
                    for each_jpg in each_group[2]:
                        if each_jpg.endswith(".jpg"):
                            jpg_list.append(each_jpg)
                return each_dir[5:],len(jpg_list)

def yuantu():
    print("原图:")
    print("     ","原图时间","车数量","图数量")
    for each_dir in os.listdir(yuantu_dir):
        for data in yuantu_data:
            if each_dir == str(data):
                new_dir = yuantu_dir + "/" + each_dir
                jpg_list = []
                each_group_list = []
                for each_group in os.listdir(new_dir):
                    each_group_list.append(each_group)
                for each_group in os.walk(new_dir):
                    for each_jpg in each_group[2]:
                        if each_jpg.endswith(".jpg"):
                            jpg_list.append(each_jpg)
                print("     ",each_dir," ",len(each_group_list)," ",len(jpg_list))
