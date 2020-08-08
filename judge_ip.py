import re


def judge_legal_ip(one_str):

    """
    正则匹配方法:match() 从字符串的起始位置开始匹配，若起始位置不匹配则会直接返回 None
    判断一个字符串是否是合法IP地址
    """

    compile_rule = '[1-2][0-5]{2}.[0-2][0-5]{2}.[0-2][0-5]{2}$'

    result = re.match(compile_rule, one_str)
    if result is None:
        print("False")
    else:
        print("True")


if __name__ == '__main__':
    test_ip = ["122.234.155b", "a122.000.000", "011.111.222", "022.256.000",
               "222.111.300", "222, 111,100", "122.000.000"]
    for i in test_ip:
        judge_legal_ip(i)
