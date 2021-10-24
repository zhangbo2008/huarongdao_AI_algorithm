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

#=====为了效率qipan是一个numpy数组.
def available_step(qipan): # 使用numpy 做棋盘重复检测时候速度快.
    #给定棋盘返回可以走的步奏.
# 再演技一下移动的编码. 不变量是0位置. 任何移动都是0周围的棋子才能动.
# 并且移动的结果一定是干掉一个0, 然后出来一个其他位置的0,而任何一个0,他周围最多有4个棋子
# 这4个棋子的移动是4个方向. 所以一个步至多有8种走法.
    #========找到空白位置的索引
    blank_index=[]
    step_over_qipan=[]
    for i in range(len(qipan)):
       for j in range(len(qipan[0])):
           if qipan[i][j]==0:
               blank_index.append([i,j])
    print('空白索引是',blank_index)
    print('原始棋盘是',qipan)






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
                    new_qipan[before_move_index]=0
                    new_qipan[after_move_index]=4
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
                             step_over_qipan.append(new_qipan)
                             print(1)
                        #如果j的左边是空白,
                        elif j[0] - 1 >=0 and j[1]-1 >=0 and qipan[j[0], j[1] - 1] == 0 and qipan[j[0] - 1, j[1] - 1] == 1:
                            new_qipan = qipan.copy()
                            new_qipan[before_move_index[0] - 1, before_move_index[1]] = 0
                            new_qipan[before_move_index[0] - 1, before_move_index[1] - 1] = 0
                            new_qipan[after_move_index[0], after_move_index[1]] = 1
                            new_qipan[after_move_index[0], after_move_index[1] - 1] = 1
                            step_over_qipan.append(new_qipan)
                    #==========同理写好其他4个方向
                    # 棋子向上移动,
                    if (i==np.array([1,0])).all():#

                        if  j[0]+1<qipan.shape[0] and     j[1]+1<qipan.shape[1] and   qipan[j[0],j[1]+1]==0 and qipan[j[0]+1,j[1]+1]==1:

                             new_qipan=qipan.copy()
                             new_qipan[before_move_index[0]-1,before_move_index[1]]=0
                             new_qipan[before_move_index[0]-1,before_move_index[1]+1]=0
                             new_qipan[after_move_index[0],after_move_index[1]]=1
                             new_qipan[after_move_index[0],after_move_index[1]+1]=1
                             step_over_qipan.append(new_qipan)
                             print(1)
                        elif j[0] + 1 < qipan.shape[0] and j[1]-1>=0 and  qipan[j[0], j[1] - 1] == 0 and qipan[j[0] + 1, j[1] - 1] == 1:
                            new_qipan = qipan.copy()
                            new_qipan[before_move_index[0] - 1, before_move_index[1]] = 0
                            new_qipan[before_move_index[0] - 1, before_move_index[1] - 1] = 0
                            new_qipan[after_move_index[0], after_move_index[1]] = 1
                            new_qipan[after_move_index[0], after_move_index[1] - 1] = 1
                            step_over_qipan.append(new_qipan)

                    # 棋子向左移动,
                    if (i == np.array([0, -1])).all():  #

                        if j[1] + 1 < qipan.shape[1] and  j[0]+1 < qipan.shape[0] and qipan[j[0]+1, j[1] ] == 0 and qipan[j[0] + 1, j[1] + 1] == 1:
                            new_qipan = qipan.copy()
                            new_qipan[before_move_index[0] , before_move_index[1]+1] = 0
                            new_qipan[before_move_index[0] +1, before_move_index[1] + 1] = 0
                            new_qipan[after_move_index[0], after_move_index[1]] = 1
                            new_qipan[after_move_index[0]+1, after_move_index[1] ] = 1
                            step_over_qipan.append(new_qipan)
                            print(1)
                        elif j[1] + 1 < qipan.shape[1] and j[0]-1>=0 and qipan[j[0]-1, j[1]] == 0 and qipan[j[0] - 1, j[1] + 1] == 1:
                            new_qipan = qipan.copy()
                            new_qipan[before_move_index[0] , before_move_index[1]+1] = 0
                            new_qipan[before_move_index[0] -1, before_move_index[1] + 1] = 0
                            new_qipan[after_move_index[0], after_move_index[1]] = 1
                            new_qipan[after_move_index[0]-1, after_move_index[1] ] = 1
                            step_over_qipan.append(new_qipan)

                        # 棋子向右移动,
                    if (i == np.array([0, -1])).all():  #

                        if j[1] - 1>-1 and j[0]+1<qipan.shape[0] and    qipan[j[0]+1, j[1] ] == 0 and qipan[j[0] + 1, j[1] - 1] == 1:
                            new_qipan = qipan.copy()
                            new_qipan[before_move_index[0] , before_move_index[1]-1] = 0
                            new_qipan[before_move_index[0] +1, before_move_index[1] - 1] = 0
                            new_qipan[after_move_index[0], after_move_index[1]] = 1
                            new_qipan[after_move_index[0]+1, after_move_index[1] ] = 1
                            step_over_qipan.append(new_qipan)
                            print(1) # elif逻辑是因为在走一步的前提下,不可能存在2种曹操的同方向走法.其实不同方向也只有一种或者没有.所以上面if失效时候下面检测即可,不存在2个都成立的情况.2个都成立的时候结果也等效.等价于跑上面就够了
                        elif j[1] - 1 >-1 and j[0]-1>=0 and qipan[j[0]-1, j[1]] == 0 and qipan[j[0] - 1, j[1] - 1] == 1:
                            new_qipan = qipan.copy()
                            new_qipan[before_move_index[0] , before_move_index[1]-1] = 0
                            new_qipan[before_move_index[0] -1, before_move_index[1] - 1] = 0
                            new_qipan[after_move_index[0], after_move_index[1]] = 1
                            new_qipan[after_move_index[0]-1, after_move_index[1] ] = 1
                            step_over_qipan.append(new_qipan)

                if qizi_property == 21:  # 如果棋子移动之前是21
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

    [1 ,1 ,0,0],
    [1 ,1 ,0 ,0],


]


qipan_demo=np.array(qipan_demo)
print(available_step(qipan_demo))

















