ori_list=[6,4,7,9,1,2,9,4,6]

def bubble_sor(ori_list):
    ori_len = len(ori_list)-1
    for a in range(ori_len):
        print('{}번째 loop1'.format(a))
        for b in range(ori_len-a):
            if ori_list[b] > ori_list[b+1]:
                print('   {}번쨰 loop2'.format(b))
                ori_list[b],ori_list[b+1] = ori_list[b+1],ori_list[b]
                print('   {}와 {} 변화'.format(ori_list[b+1],ori_list[b]))
                print(ori_list)
        print(ori_list)

bubble_sor(ori_list)
