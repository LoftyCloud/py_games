import time

from selenium import webdriver
import random


# 按给定的概率返回一个列表中的值
def number_of_certain_probability(sequence, probability):
    x = random.uniform(0, 1)
    cumulative_probability = 0.0
    for item, item_probability in zip(sequence, probability):
        # 只有当累加的概率比刚才随机生成的随机数大时候，才跳出，并输出此时对应的值
        cumulative_probability += item_probability
        if x < cumulative_probability:
            break
    return item


# 生成单选题的答案
def s_answear():
    # 值
    value_list_1 = [1, 2, 3, 4, 5]
    # 概率(1、2、3、9、10单选题)
    probability_1 = [0.204, 0.314, 0.428, 0.054]
    probability_2 = [0.171, 0.599, 0.091, 0.139]
    probability_3 = [0.048, 0.075, 0.526, 0.351]
    probability_4 = [0.024, 0.191, 0.466, 0.319]
    probability_5 = [0.115, 0.351, 0.061, 0.435, 0.038]

    probability = [
        probability_1,
        probability_2,
        probability_3,
        probability_4,
        probability_5
    ]
    s_answear_list = []

    for i in range(5):
        result = number_of_certain_probability(value_list_1[:len(probability[i])], probability[i])
        s_answear_list.append(result)

    return s_answear_list


# 生成多选题的答案
def d_answear():
    # 值
    value_list_2 = [1, 2, 3, 4, 5, 6, 7, 8]
    # 多选题各选项单次被选择的概率(4~6三选，7~8双选)
    answear_num = [3, 3, 3, 2, 2]
    null_answear = [0.15, 0.2, 0.1]

    probability_1 = [0.714 / 3, 0.381 / 3, 0.429 / 3, 0.452 / 3, 0.381 / 3, 0.214 / 3, 0.214 / 3, 0.214 / 3]
    probability_2 = [0.714 / 3, 0.643 / 3, 0.569 / 3, 0.188 / 3, 0.476 / 3, 0.357 / 3, 0.124 / 3]
    probability_3 = [0.333 / 3, 0.833 / 3, 0.857 / 3, 0.357 / 3, 0.071 / 3, 0.286 / 3, 0.048 / 3, 0.048 / 3]
    probability_4 = [0.333 / 2, 0.81 / 2, 0.214 / 2, 0.31 / 2, 0.119 / 2, 0.095 / 2]
    probability_5 = [0.633 / 2, 0.442 / 2, 0.26 / 2, 0.49 / 2, 0.071 / 2, 0.033 / 2]

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
            result = number_of_certain_probability(value_list_2[:len(probability[i])], probability[i])
            while (result in answear):  # 使多选的结果不会重复
                result = number_of_certain_probability(value_list_2[:len(probability[i])], probability[i])
            answear.append(result)
        d_answear_list.append(answear)

    # 三选项的概率只选两项，使第三项为0
    x = random.uniform(0, 1)
    if x < null_answear[0]:
        d_answear_list[0][2] = 0
    x = random.uniform(0, 1)
    if x < null_answear[1]:
        d_answear_list[1][2] = 0
    x = random.uniform(0, 1)
    if x < null_answear[2]:
        d_answear_list[2][2] = 0

    return d_answear_list


def time_write(num):
    for i in range(num):
        s_answear_list = s_answear()
        d_answear_list = d_answear()
        print(s_answear_list)
        print(d_answear_list)

        driver = webdriver.Chrome()
        driver.get('https://wj.qq.com/s2/8386364/cee9/')
        time.sleep(1)
        # 第一题
        driver.find_element_by_xpath(
            '//*[@id="question_q-1-B1GQ"]/div[2]/div[' + str(s_answear_list[0]) + ']/label/p').click()

        # 第二题
        driver.find_element_by_xpath(
            '//*[@id="question_q-2-fphY"]/div[2]/div[' + str(s_answear_list[1]) + ']/label/p').click()

        # 第三题
        driver.find_element_by_xpath(
            '//*[@id="question_q-3-I8ZM"]/div[2]/div[' + str(s_answear_list[2]) + ']/label/p').click()

        # 第四题
        driver.find_element_by_xpath(
            '//*[@id="question_q-4-B7dm"]/div[2]/div[' + str(d_answear_list[0][0]) + ']/label/p').click()
        driver.find_element_by_xpath(
            '//*[@id="question_q-4-B7dm"]/div[2]/div[' + str(d_answear_list[0][1]) + ']/label/p').click()
        if d_answear_list[0][2] != 0:
            driver.find_element_by_xpath(
                '//*[@id="question_q-4-B7dm"]/div[2]/div[' + str(d_answear_list[0][2]) + ']/label/p').click()

        js = "var q=document.documentElement.scrollTop=800"  # 下拉像素(800是基于最顶端测算的距离)
        driver.execute_script(js)  # 执行下拉像素操作

        # 第五题
        driver.find_element_by_xpath(
            '//*[@id="question_q-5-HC0e"]/div[2]/div[' + str(d_answear_list[1][0]) + ']/label/p').click()
        driver.find_element_by_xpath(
            '//*[@id="question_q-5-HC0e"]/div[2]/div[' + str(d_answear_list[1][1]) + ']/label/p').click()
        if d_answear_list[1][2] != 0:
            driver.find_element_by_xpath(
                '//*[@id="question_q-5-HC0e"]/div[2]/div[' + str(d_answear_list[1][2]) + ']/label/p').click()

        # 第六题
        driver.find_element_by_xpath(
            '//*[@id="question_q-6-JR3p"]/div[2]/div[' + str(d_answear_list[2][0]) + ']/label/p').click()
        driver.find_element_by_xpath(
            '//*[@id="question_q-6-JR3p"]/div[2]/div[' + str(d_answear_list[2][1]) + ']/label/p').click()
        if d_answear_list[2][2] != 0:
            driver.find_element_by_xpath(
                '//*[@id="question_q-6-JR3p"]/div[2]/div[' + str(d_answear_list[2][2]) + ']/label/p').click()

        # 第七题
        driver.find_element_by_xpath(
            '//*[@id="question_q-7-G2IG"]/div[2]/div[' + str(d_answear_list[3][0]) + ']/label/p').click()
        driver.find_element_by_xpath(
            '//*[@id="question_q-7-G2IG"]/div[2]/div[' + str(d_answear_list[3][1]) + ']/label/p').click()

        # 第八题
        driver.find_element_by_xpath(
            '//*[@id="question_q-8-bIMJ"]/div[2]/div[' + str(d_answear_list[4][0]) + ']/label/p').click()
        driver.find_element_by_xpath(
            '//*[@id="question_q-8-bIMJ"]/div[2]/div[' + str(d_answear_list[4][1]) + ']/label/p').click()

        js = "var q=document.documentElement.scrollTop=1600"
        driver.execute_script(js)

        # 第九题
        driver.find_element_by_xpath(
            '//*[@id="question_q-9-4W4s"]/div[2]/div[' + str(s_answear_list[3]) + ']/label/p').click()

        # 第十题
        driver.find_element_by_xpath(
            '//*[@id="question_q-11-MM9o"]/div[2]/div[' + str(s_answear_list[4]) + ']/label/p').click()

        js = "var q=document.documentElement.scrollTop=3600"
        driver.execute_script(js)

        # 提交按钮
        driver.find_element_by_xpath(
            '//*[@id="root-container"]/div/div[1]/div[2]/div[2]/div[5]/div/button/span').click()
        print('第' + str(i) + '次填写成功')
        driver.quit()
        # time.sleep(5)


time_write(1)
