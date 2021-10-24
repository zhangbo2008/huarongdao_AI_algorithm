#2021-10-23,14点41 华容道
'''
demo棋盘


1 1 21 21
1 1 22 22
4 4 21 21
4 4 22 22
0 0 31 32



0是空白, 1是曹操, 21, 22 是竖, 3132 是横 4是小兵.






'''
import numpy as np



def cunzai(a,b):  # b是否在a里面
    #a是一堆array组成的list
# b是一个array
    for i in a:
        if (i==b).all():
            return True

    return False






#=====为了效率qipan是一个numpy数组.
def available_step(qipan): # 使用numpy 做棋盘重复检测时候速度快.
    #给定棋盘返回可以走的步奏.
# 再演技一下移动的编码. 不变量是0位置. 任何移动都是0周围的棋子才能动.
# 并且移动的结果一定是干掉一个0, 然后出来一个其他位置的0,而任何一个0,他周围最多有4个棋子
# 这4个棋子的移动是4个方向. 所以一个步至多有8种走法.
    #========找到空白位置的索引
    qipan=np.array(qipan)
    blank_index=[]
    step_over_qipan=[]
    for i in range(len(qipan)):
       for j in range(len(qipan[0])):
           if qipan[i][j]==0:
               blank_index.append([i,j])
    # print('空白索引是',blank_index)
    # print('原始棋盘是',qipan)



#=================我们改成不从方向和空白索引入手了.而是整体看. 华容道每次棋盘一定只有2个空.
    #后续可以使用曹操,每次只有一种和0种的走法,这一点来加速.
    # 这里面还是去重逻辑,这样的话更一般性.


    for i in [(-1,0),(1,0),(0,-1),(0,1)]:
        for j in blank_index:
            #我们看看空白偏移之后的位置是什么
            before_move_index=[j[0]+i[0],j[1]+i[1]]
            after_move_index=j


            if before_move_index[0] >=0 and before_move_index[0]<qipan.shape[0] and before_move_index[1]>=0 and before_move_index[1]<qipan.shape[1]:
                qizi_property = qipan[before_move_index[0]][before_move_index[1]]
                #=======下面进行检测这个属性的棋子是否可以移动到j坐标上
            # 如果可以的话,那么我们就把移动之后的棋盘放入 step_over_qipan 里面
                another_blank_index=[tt for tt in blank_index if tt!=j][0] # 得到另外一个空的索引.

                # 下面进行移动合理性判断的逻辑
                if qizi_property==0:
                    continue # 空到空没意义.跳过
                if qizi_property == 4:#必然合理
                    new_qipan=qipan.copy()
                    new_qipan[before_move_index[0],before_move_index[1]]=0
                    new_qipan[after_move_index[0],after_move_index[1]]=4
                    if not cunzai(step_over_qipan,new_qipan):
                        step_over_qipan.append(new_qipan)

                if qizi_property==1:# 如果棋子移动之前是曹!!!!!!!!!!!!!
                    if (i==np.array([-1,0])).all():#如果操作是向下移动曹:
                        # 如果j的右边是空白, j的右再上也必须是1.
                        if  j[0]-1>=0 and      j[1]+1<qipan.shape[1] and qipan[j[0],j[1]+1]==0 and qipan[j[0]-1,j[1]+1]==1:
                            # 这时是合理的移动.
                             new_qipan=qipan.copy()
                             new_qipan[before_move_index[0]-1,before_move_index[1]]=0
                             new_qipan[before_move_index[0]-1,before_move_index[1]+1]=0
                             new_qipan[after_move_index[0],after_move_index[1]]=1
                             new_qipan[after_move_index[0],after_move_index[1]+1]=1
                             if not cunzai(step_over_qipan, new_qipan):
                                 step_over_qipan.append(new_qipan)
                             # print(1)
                        #如果j的左边是空白,
                        elif j[0] - 1 >=0 and j[1]-1 >=0 and qipan[j[0], j[1] - 1] == 0 and qipan[j[0] - 1, j[1] - 1] == 1:
                            new_qipan = qipan.copy()
                            new_qipan[before_move_index[0] - 1, before_move_index[1]] = 0
                            new_qipan[before_move_index[0] - 1, before_move_index[1] - 1] = 0
                            new_qipan[after_move_index[0], after_move_index[1]] = 1
                            new_qipan[after_move_index[0], after_move_index[1] - 1] = 1
                            if not cunzai(step_over_qipan, new_qipan):
                               step_over_qipan.append(new_qipan)
                    #==========同理写好其他4个方向
                    # 棋子向上移动,
                    if (i==np.array([1,0])).all():#

                        if  j[0]+1<qipan.shape[0] and     j[1]+1<qipan.shape[1] and   qipan[j[0],j[1]+1]==0 and qipan[j[0]+1,j[1]+1]==1:

                             new_qipan=qipan.copy()
                             new_qipan[before_move_index[0]+1,before_move_index[1]]=0
                             new_qipan[before_move_index[0]+1,before_move_index[1]+1]=0
                             new_qipan[after_move_index[0],after_move_index[1]]=1
                             new_qipan[after_move_index[0],after_move_index[1]+1]=1
                             if not cunzai(step_over_qipan, new_qipan):

                                            step_over_qipan.append(new_qipan)
                             # print(1)
                        elif j[0] + 1 < qipan.shape[0] and j[1]-1>=0 and  qipan[j[0], j[1] - 1] == 0 and qipan[j[0] + 1, j[1] - 1] == 1:
                            new_qipan = qipan.copy()
                            new_qipan[before_move_index[0] + 1, before_move_index[1]] = 0
                            new_qipan[before_move_index[0] + 1, before_move_index[1] - 1] = 0
                            new_qipan[after_move_index[0], after_move_index[1]] = 1
                            new_qipan[after_move_index[0], after_move_index[1] - 1] = 1
                            if not cunzai(step_over_qipan, new_qipan):
                              step_over_qipan.append(new_qipan)

                    # 棋子向左移动,
                    if (i == np.array([0, 1])).all():  #

                        if j[1] + 1 < qipan.shape[1] and  j[0]+1 < qipan.shape[0] and qipan[j[0]+1, j[1] ] == 0 and qipan[j[0] + 1, j[1] + 1] == 1:
                            new_qipan = qipan.copy()
                            new_qipan[before_move_index[0] , before_move_index[1]+1] = 0
                            new_qipan[before_move_index[0] +1, before_move_index[1] + 1] = 0
                            new_qipan[after_move_index[0], after_move_index[1]] = 1
                            new_qipan[after_move_index[0]+1, after_move_index[1] ] = 1
                            if not cunzai(step_over_qipan, new_qipan):
                              step_over_qipan.append(new_qipan)
                            # print(1)
                        elif j[1] + 1 < qipan.shape[1] and j[0]-1>=0 and qipan[j[0]-1, j[1]] == 0 and qipan[j[0] - 1, j[1] + 1] == 1:
                            new_qipan = qipan.copy()
                            new_qipan[before_move_index[0] , before_move_index[1]+1] = 0
                            new_qipan[before_move_index[0] -1, before_move_index[1] + 1] = 0
                            new_qipan[after_move_index[0], after_move_index[1]] = 1
                            new_qipan[after_move_index[0]-1, after_move_index[1] ] = 1
                            if not cunzai(step_over_qipan, new_qipan):
                               step_over_qipan.append(new_qipan)

                        # 棋子向右移动,
                    if (i == np.array([0, -1])).all():  #

                        if j[1] - 1>-1 and j[0]+1<qipan.shape[0] and    qipan[j[0]+1, j[1] ] == 0 and qipan[j[0] + 1, j[1] - 1] == 1:
                            new_qipan = qipan.copy()
                            new_qipan[before_move_index[0] , before_move_index[1]-1] = 0
                            new_qipan[before_move_index[0] +1, before_move_index[1] - 1] = 0
                            new_qipan[after_move_index[0], after_move_index[1]] = 1
                            new_qipan[after_move_index[0]+1, after_move_index[1] ] = 1
                            if not cunzai(step_over_qipan, new_qipan):
                              step_over_qipan.append(new_qipan)
                            # print(1) # elif逻辑是因为在走一步的前提下,不可能存在2种曹操的同方向走法.其实不同方向也只有一种或者没有.所以上面if失效时候下面检测即可,不存在2个都成立的情况.2个都成立的时候结果也等效.等价于跑上面就够了
                        elif j[1] - 1 >-1 and j[0]-1>=0 and qipan[j[0]-1, j[1]] == 0 and qipan[j[0] - 1, j[1] - 1] == 1:
                            new_qipan = qipan.copy()
                            new_qipan[before_move_index[0] , before_move_index[1]-1] = 0
                            new_qipan[before_move_index[0] -1, before_move_index[1] - 1] = 0
                            new_qipan[after_move_index[0], after_move_index[1]] = 1
                            new_qipan[after_move_index[0]-1, after_move_index[1] ] = 1
                            if not cunzai(step_over_qipan, new_qipan):
                             step_over_qipan.append(new_qipan)
#===================================下面处理横和竖!!!!!!!!!!!!!!!!!!!!!
                if 31>qizi_property >20:  # 如果棋子移动之前是列.
                    #========现在发现光21,22还是不够, 区分哪个21和22匹配也很难. 所以用21,22   23,24   25,26  27,28 29,30来编码5个列.
                    if qizi_property%2==1:
                        qizishishang=True#说明定位是2*1棋子的上面
                    else:
                        qizishishang=False
                    if (i == np.array([0, -1])).all():#如果是棋子往右走
                        #==========这次我们优化一下,其实只关注棋子的上半部分就够了.棋子下半部分移动的情况一定被上半部分考虑过了.
                        if qizishishang==True:
                            if qipan[before_move_index[0]+1][before_move_index[1]]==qizi_property+1 and qipan[j[0]+1][j[1]]==0:
                                new_qipan = qipan.copy()
                                new_qipan[before_move_index[0]+1, before_move_index[1]]= 0
                                new_qipan[before_move_index[0], before_move_index[1]]= 0

                                new_qipan[after_move_index[0], after_move_index[1]] = qizi_property
                                new_qipan[after_move_index[0] +1, after_move_index[1]] = qizi_property+1
                                if not cunzai(step_over_qipan, new_qipan):
                                    step_over_qipan.append(new_qipan)
                    if (i == np.array([0, 1])).all():#如果是棋子往zuo走
                        #==========这次我们优化一下,其实只关注棋子的上半部分就够了.棋子下半部分移动的情况一定被上半部分考虑过了.
                        if qizishishang==True:
                            if qipan[before_move_index[0]+1][before_move_index[1]]==qizi_property+1  and qipan[j[0]+1][j[1]]==0:
                                new_qipan = qipan.copy()
                                new_qipan[before_move_index[0]+1, before_move_index[1]]= 0
                                new_qipan[before_move_index[0], before_move_index[1]]= 0

                                new_qipan[after_move_index[0], after_move_index[1]] = qizi_property
                                new_qipan[after_move_index[0] +1, after_move_index[1]] = qizi_property+1
                                if not cunzai(step_over_qipan, new_qipan):
                                    step_over_qipan.append(new_qipan)

                    if (i == np.array([1, 0])).all():#如果是棋子往上走
                        #==========这次我们优化一下,其实只关注棋子的上半部分就够了.棋子下半部分移动的情况一定被上半部分考虑过了.
                        if qizishishang==True:

                                new_qipan = qipan.copy()

                                new_qipan[before_move_index[0], before_move_index[1]]= qizi_property+1
                                new_qipan[before_move_index[0]+1, before_move_index[1]]= 0

                                new_qipan[after_move_index[0], after_move_index[1]] = qizi_property

                                if not cunzai(step_over_qipan, new_qipan):
                                    step_over_qipan.append(new_qipan)
                    if (i == np.array([-1, 0])).all():#如果是棋子往xia走
                        #==========这次我们优化一下,其实只关注棋子的上半部分就够了.棋子下半部分移动的情况一定被上半部分考虑过了.
                        if qizishishang==False:

                                new_qipan = qipan.copy()

                                new_qipan[before_move_index[0], before_move_index[1]]= qizi_property-1
                                new_qipan[before_move_index[0]-1, before_move_index[1]]= 0

                                new_qipan[after_move_index[0], after_move_index[1]] = qizi_property

                                if not cunzai(step_over_qipan, new_qipan):
                                    step_over_qipan.append(new_qipan)
                    #==========同理把横的也弄上.
                if 41 > qizi_property > 30:  # 如果棋子移动之前是hang.
                    # ========现在发现光21,22还是不够, 区分哪个21和22匹配也很难. 所以用21,22   23,24   25,26  27,28 29,30来编码5个列. # 用31, 32,       33, 34,        35, 36,      37 38      39 40来编码5个行.

                    if qizi_property%2==1:
                        qizishizuo=True#说明定位是2*1棋子的上面
                    else:
                        qizishizuo=False
                    if (i == np.array([1, 0])).all():#如果是棋子往上走
                        #==========这次我们优化一下,其实只关注棋子的zuo半部分就够了.
                        if qizishizuo==True:
                            if qipan[before_move_index[0]][before_move_index[1]+1]==qizi_property+1 and qipan[j[0]][j[1]+1]==0:
                                new_qipan = qipan.copy()
                                new_qipan[before_move_index[0], before_move_index[1]]= 0
                                new_qipan[before_move_index[0], before_move_index[1]+1]= 0

                                new_qipan[after_move_index[0], after_move_index[1]] = qizi_property
                                new_qipan[after_move_index[0], after_move_index[1]+1] = qizi_property+1
                                if not cunzai(step_over_qipan, new_qipan):
                                    step_over_qipan.append(new_qipan)
                    if (i == np.array([-1, 0])).all():#如果是棋子往下走
                        #==========这次我们优化一下,其实只关注棋子的zuo半部分就够了.
                        if qizishizuo==True:
                            if qipan[before_move_index[0]][before_move_index[1]+1]==qizi_property+1 and qipan[j[0]][j[1]+1]==0:
                                new_qipan = qipan.copy()
                                new_qipan[before_move_index[0], before_move_index[1]]= 0
                                new_qipan[before_move_index[0], before_move_index[1]+1]= 0

                                new_qipan[after_move_index[0], after_move_index[1]] = qizi_property
                                new_qipan[after_move_index[0], after_move_index[1]+1] = qizi_property+1
                                if not cunzai(step_over_qipan, new_qipan):
                                    step_over_qipan.append(new_qipan)
                    if (i == np.array([0, 1])).all():#如果是棋子往zuo走
                        #==========这次我们优化一下,其实只关注棋子的zuo半部分就够了.
                        if qizishizuo==True:
                            if qipan[before_move_index[0]][before_move_index[1]+1]==qizi_property+1:
                                new_qipan = qipan.copy()
                                new_qipan[before_move_index[0], before_move_index[1]]= qizi_property+1
                                new_qipan[before_move_index[0], before_move_index[1]+1]= 0

                                new_qipan[after_move_index[0], after_move_index[1]] = qizi_property

                                if not cunzai(step_over_qipan, new_qipan):
                                    step_over_qipan.append(new_qipan)

                    if (i == np.array([0, -1])).all():  # 如果是棋子往you走
                        # ==========这次我们优化一下,其实只关注棋子的zuo半部分就够了.
                        if qizishizuo == False:
                            if qipan[before_move_index[0]][before_move_index[1] - 1] == qizi_property- 1:
                                new_qipan = qipan.copy()


                                new_qipan[before_move_index[0], before_move_index[1]] = qizi_property-1
                                new_qipan[before_move_index[0], before_move_index[1] -1] = 0

                                new_qipan[after_move_index[0], after_move_index[1]] = qizi_property

                                if not cunzai(step_over_qipan, new_qipan):
                                    step_over_qipan.append(new_qipan)
                    pass

    return step_over_qipan










qipan_demo=[

    [1 ,1 ,21, 21],
    [1 ,1 ,22 ,22],
    [0,0 ,21, 21],
    [4 ,4 ,22 ,22],
    [4 ,4 ,31, 32]
]


qipan_demo=[

    [0 ,0 ,31,32],
    [1 ,33 ,34 ,0],
    [25 ,1 ,0,1],
    [26 ,0 ,0 ,0],


]

qipan_demo=[

    [0 ,0 ,31,32],
    [1 ,33 ,34 ,0],
    [25 ,1 ,0,1],
    [26 ,0 ,0 ,0],


]


qipan_demo=[

    [21 ,1 ,1,23],
    [22 ,1 ,1 ,24],
    [25 ,31 ,32,27],
    [26 ,4 ,4 ,28],
    [4 ,0 ,0 ,4],


]









qipan_demo=np.array(qipan_demo)
# print(available_step(qipan_demo))


#============================游戏部分编辑完毕. 下面做算法部分, 核心是带记忆体的bfs

wintest=[

    [21 ,1 ,1,23],
    [22 ,1 ,1 ,24],
    [25 ,31 ,32,27],
    [26 ,1 ,1 ,28],
    [4 ,1 ,1 ,4],


]

hengdaolima=[

    [21 ,1 ,1,23],
    [22 ,1 ,1 ,24],
    [25 ,31 ,32,27],
    [26 ,4 ,4 ,28],
    [4 ,0 ,0 ,4],


]

from numpy import array
hengdaolima=np.array(hengdaolima)
a=hengdaolima.__repr__()
# print(a,11111111)
# a=eval(a)
# print(a,2222222222222)
if 1:#=========这个是numpy str互化的方法.
    from numpy import array
    a = array([[0,3,5],[2,3,4]])
    a_str = a.__repr__() # 'array([[0, 3, 5],\n       [2, 3, 4]])'
    a2 = eval(a_str)
    # print(a2,88888888888888)



tmp=hengdaolima.tostring()
tmp=np.fromstring(tmp,dtype=int)
# print(tmp,44444444444)
# print((hengdaolima.tostring()),33333333333)
#=========算法每次输入一个qipan,然后返回他所有走一步之后的变化.
def whether_win(arr): #这个函数判断曹操是否win
    arr=np.array(arr)
    if (arr[3:,1:3]==np.array([[1,1],[1,1]])).all():
        return True
    return False
# print(whether_win(hengdaolima))
# print(whether_win(wintest))


#===========初始qipan放进去.然后出来几个走法之后的棋盘.拿一个数组记录下曾经走过的棋盘.走过的棋盘就不再进入循环中.
#不停的走,一定有一次走法是whether_win=True的.




debug=0

def play(first):
    first_qipan=first

    memory_qipan={first_qipan.__repr__():None}
    import pandas as pd
    import numpy as np
    #设定一个整体循环的次数
    step=100
    bfs_shuzu=[first_qipan]
    if debug:
        print('开始的棋盘是')
        #漂亮打印
        [print(pd.DataFrame(arr, index=None,columns=None)) for arr in bfs_shuzu]
    for _ in range(1,step+1):
        print("正在进行第几次bfs",_)
        next_shuzu=[]#用来保存本次bfs的结果
        for j in bfs_shuzu:
            tmp=available_step(j)
            #======我们为了最后得到路径, 每一个qipan他的父qipan我们也记录下来.这样逆序就可以找到了.
            #首先tmp进行去重.加入记忆体.
            for  kk in tmp:
                #==========进行win判断

                kk_encoded=kk.__repr__()
                j_encoded=j.__repr__()
                if   kk_encoded not in memory_qipan:
                    memory_qipan[kk_encoded]=j
                    next_shuzu.append(kk) #是新的qipan可以继续计算.
                if whether_win(kk):
                    print("暴力方法成功找到了答案,使用了多少步",_)
                    print("结果长相",pd.DataFrame(kk, index=None, columns=None))
                    return kk,memory_qipan
        bfs_shuzu=next_shuzu
        if debug:
            print('当前步奏',_,'结果是')
            #漂亮打印用df
            for arr in bfs_shuzu:
                print(pd.DataFrame(arr, index=None, columns=None))
                print("================棋盘切割线=================")



first=np.array([

    [21 ,23 ,0,25],
    [22 ,24 ,0 ,26],
    [27 ,29 ,1,1],
    [28 ,30 ,1 ,1],
    [4 ,4 ,4 ,4],


])






#=================
print('下面反解每一步的走法:')
kk,memory=play(first)
print(1111111)


tmp=kk
tmp_encoded=tmp.__repr__()
path=[tmp]
while not (tmp==first).all():


      last=memory[tmp.__repr__()]
      path.append(last)
      tmp=last

print(1)


import pandas as pd
path=path[::-1]
print('路径是')
            #漂亮打印用df
for arr in path:
    print(pd.DataFrame(arr, index=None, columns=None))
    print("================棋盘切割线=================")























