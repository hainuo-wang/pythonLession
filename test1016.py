# 2、编写函数，接收两个等长度的列表a和b，以第一个列表a中元素升序对应的索引为依据，对第2个列表b中元素进行排序，并输出排序结果。
# 例如：若输入a=[1,3,5,9,12],b=[8,6,9,0,1],则排序后输出[8,6,9,0,1]，
# 若输入a=[6,13,5,9,12],b=[7,9,8,1,2],则排序后输出[8,7,1,2,9]。
def dict_sort(lst1, lst2):
    lst1_new = []
    lst2_new = []
    dictionary = dict(zip(lst1, lst2))
    for key in sorted(dictionary.keys()):
        lst1_new.append(key)
        lst2_new.append(dictionary[key])
    print(lst1_new, lst2_new)


a = list(eval(input()))
b = list(eval(input()))
dict_sort(a, b)
