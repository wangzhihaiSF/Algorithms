# dict_num = {'a': 3, 'b': 2, 'c': 1}
# result_dict = sorted(dict_num.items(), key=lambda item: item[1])
# print(dict(result_dict))


def sort_input():
    input_dict = {}
    input_str = input("请输入一长串字符，我们将统计相同的字符数量：")
    for i in input_str:
        if i not in input_dict:
            input_dict[i] = 1
        else:
            input_dict[i] += 1
    return_list = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    print(return_list)
    return dict(return_list)


if __name__ == '__main__':
    result = sort_input()
    print(result)
