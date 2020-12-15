import re


def find_special_character(info):
    result = re.findall(".*?(\W)", info)
    return result


if __name__ == "__main__":
    str_info = "sdfjl;*&_+sdfa毫升！@"
    result = find_special_character(str_info)
    print(result)
