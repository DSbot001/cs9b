# Lecture 1: Review
# August 3rd 

x = 5          # int
y = 3.14       # float
name = "Bob"   # str
flag = True    # bool

arr = [10, 20, 30, 40]
arr[0]          # 10,索引从0开始
arr[-1]         # 40,负索引=从尾部数
arr.append(50)  # [10, 20, 30, 40, 50] 尾部加一个
arr.insert(1, 99)  # 在索引1插入99 -> [10, 99, 20, 30, 40, 50]
arr.pop()       # 删除并返回最后一个元素

arr.pop(0)      # 删除并返回索引0的元素
len(arr)        # 数组长度

# mixed = [1, "two", 3.0, True]  # 完全合法

# for i in range(5):        # i = 0,1,2,3,4
#     print(i)

# for item in arr:           # 直接遍历元素本身,不需要索引
#     print(item)

# for i, item in enumerate(arr):  # 同时要索引和值
#     print(i, item)

# i = 0
# while i < len(arr):
#     print(arr[i])
#     i += 1


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


target_Index = linear_search(arr,5)
print(target_Index)