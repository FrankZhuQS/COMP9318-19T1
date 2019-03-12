## import modules here 
import pandas as pd
import numpy as np

x = [3, 1, 18, 11, 13, 17]
num_bins = 4

################# Question 1 #################


#SSE is the sum of the squared differences between each
# observation and its group's mean.
# It can be used as a measure of variation within a cluster.
# If all cases within a cluster are identical the SSE would then be equal to 0.

def SSE(x):
    mean = np.average(x)
    sse = 0.0
    for i in x:
        rd = i - mean
        sse += rd**2
    return sse



def v_opt_dp(x, num_bins):# do not change the heading of the function
    cost_matrix = [[-1 for _ in range(len(x))] for _ in range(num_bins)]
    index_matrix = [[-1 for _ in range(len(x))] for _ in range(num_bins)]
    path_matrix  = [[-1 for _ in range(len(x))] for _ in range(num_bins)]

    for i in range(1,num_bins+1):
        set_path = []
        for j in range(len(x)):
            if num_bins - i <= j and len(x) - j >= i:
                suffix = x[j:]
                print('i**********',i)
                print('suffix',suffix)
                if i == 1:
                    cost = SSE(suffix)
                    cost_matrix[i-1][j] = cost
                    index_matrix[i-1][j] = suffix

                else:
                    if len(suffix) == i:
                        lis_path = []
                        for ele in suffix:
                            set_path.append([ele])
                        print('ele',lis_path)
                        index_matrix[i-1][j] = suffix
                        path_matrix[i-1][j] = set_path
                        cost_matrix[i-1][j] = 0
                        print('inde',index_matrix)
                #print(cost_matrix)
                    else:
                        lis_cost = []
                        for mid in range(1, len(suffix) -i + 2):
                            one_path = []
                            print('mid: ',mid)
                            pre_suffix = suffix[:mid]
                            one_path.append(pre_suffix)
                            print(pre_suffix)
                            suf_suffix = suffix[mid:]
                            one_path.append(suf_suffix)
                            pre_cost = SSE(pre_suffix)
                            num = index_matrix[i-2].index(suf_suffix)
                            print('num',num)
                            print(index_matrix[i-2].index(suf_suffix))
                            cost = pre_cost + cost_matrix[i-2][num]
                            print('cost',cost)
                            lis_cost.append(cost)
                            print('lis_cost',lis_cost)
                            print('one_path',one_path)
                            set_path.append(one_path)
                        cost_matrix[i-1][j] = min(lis_cost)
                        index_matrix[i-1][j] = suffix
                        path_matrix[i-1][j] = set_path
                        print('index_matrix',index_matrix)

                        print('path_matrix',path_matrix)

                        print('lis_cost',cost_matrix)
    print('cost_matirx', cost_matrix)








a = [1]


#print(SSE(a))



    

v_opt_dp(x,num_bins)