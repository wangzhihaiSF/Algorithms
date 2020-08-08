# 判断两个字典，若key不同，打印key及value；若key相同，value不同打印key及value
# value 可能同样是字典,同样需要判断key及value（递归）


def judge_dict(dict1, dict2):

    # dict1 中不同的key
    for key in dict1.keys():
        if key not in dict2.keys():
            print(key, dict1[key])

    # dict2 中不同的key
    for key in dict2.keys():
        if key not in dict1.keys():
            print(key, dict2[key])
        else:
            if dict1[key] != dict2[key]:
                print(key, dict1[key], dict2[key])
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                    judge_dict(dict1[key], dict2[key])


if __name__ == '__main__':
    dict11 = {'name': 'ni', 'city': 'tt', 'id': 2256, "address": {"province": "河北", "city": "石家庄"}}
    dict22 = {'name': 'ni', 'city': 'tt', 'id': 225633, "sex": 1, "address": {"province": "河北", "city": "邯郸",
                                                                              "country": "西陆开"}}
    judge_dict(dict11, dict22)

