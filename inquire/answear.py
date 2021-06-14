import random


def number_of_certain_probability(sequence, probability):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(sequence, probability):
        # 只有当累加的概率比刚才随机生成的随机数大时候，才跳出，并输出此时对应的值
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item

def d_answear():
    # 值
    value_list_2 = [1, 2, 3, 4, 5, 6, 7, 8]
    # 概率(4~6三选，7~8双选)
    answear_num = [3, 3, 3, 2, 2]
    null_answear = [0.15, 0.2, 0.1]

    probability_1 = [0.714 / 3, 0.381 / 3, 0.429 / 3, 0.452 / 3, 0.381 / 3, 0.214 / 3, 0.214 / 3, 0.214 / 3]
    probability_2 = [0.714 / 3, 0.643 / 3, 0.619 / 3, 0.238 / 3, 0.476 / 3, 0.357 / 3, 0.024 / 3, -1]
    probability_3 = [0.333 / 3, 0.833 / 3, 0.857 / 3, 0.357 / 3, 0.071 / 3, 0.286 / 3, 0.048 / 3, 0.048 / 3]
    probability_4 = [0.333 / 2, 0.81 / 2, 0.214 / 2, 0.31 / 2, 0.119 / 2, 0.095 / 2, -1, -1]
    probability_5 = [0.633 / 2, 0.442 / 2, 0.26 / 2, 0.49 / 2, 0.071 / 2, 0.033 / 2, -1, -1]

    probability = [
        probability_1,
        probability_2,
        probability_3,
        probability_4,
        probability_5
    ]
    d_answear_list = []
    for i in range(5):
        answear = []
        for j in range(answear_num[i]):
            result = number_of_certain_probability(value_list_2, probability[i])
            while (result in answear):  # 使多选的结果不会重复
                result = number_of_certain_probability(value_list_2, probability[i])
            answear.append(result)
        d_answear_list.append(answear)

    # 三选项的概率只选两项，使第三项为0
    x = random.uniform(0, 1)
    if (x < null_answear[0]):
        d_answear_list[0][2] = 0
    x = random.uniform(0, 1)
    if (x < null_answear[1]):
        d_answear_list[1][2] = 0
    x = random.uniform(0, 1)
    if (x < null_answear[2]):
        d_answear_list[2][2] = 0
    print(d_answear_list)

d_answear()

