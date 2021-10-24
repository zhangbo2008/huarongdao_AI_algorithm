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


#=====为了效率qipan是一个numpy数组.
def available_step(qipan):
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






    for i in [(-1,0),(1,0),(0,-1),(0,1)]:
        for j in blank_index:
            #我们看看空白偏移之后的位置是什么
            before_move_index=[j[0]+i[0],j[1]+i[1]]
            if before_move_index[0] >=0 and before_move_index[1]<=qipan.shape[0]
            qizi_property=qipan[before_move_index[0]][before_move_index[1]]
            print(1)
            #=======下面进行检测这个属性的棋子是否可以移动到j坐标上.
        # 如果可以的话,那么我们就把移动之后的棋盘放入 step_over_qipan 里面
            another_blank_index=[tt for tt in blank_index if tt!=j][0] # 得到另外一个空的索引.
            print(1)






qipan_demo=[

    [1 ,1 ,21, 21],
    [1 ,1 ,22 ,22],
    [4, 4 ,21, 21],
    [4 ,4 ,22 ,22],
    [0 ,0 ,31, 32]
]
available_step(qipan_demo)

















