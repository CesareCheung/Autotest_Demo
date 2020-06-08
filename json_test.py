import json

"""
实现：
1.json_txt(dic_json)：json格式，遍历key,value，存储到字典中
2.heck_json_value(dic_json,k,v)json格式，遍历后，替换key的value值
3.data_Json(Sendjson_txt),将json字符串转化为json格式
"""


# json序列化json格式
def data_Json(Sendjson_txt):
    data_json = json.loads(Sendjson_txt)
    print('data_json: ', data_json)
    return data_json


# 遍历json文件所有的key对应的value,存储到一个字典中
dic = {}


def json_txt(dic_json):
    if isinstance(dic_json, dict):  # 判断是否是字典类型isinstance 返回True,false
        for key in dic_json:
            if isinstance(dic_json[key], dict):  # 如果dic_json[key]依旧是字典类型
                print("****key--：%s ,value--: %s" % (key, dic_json[key]))
                # 递归调用
                json_txt(dic_json[key])
                dic[key] = dic_json[key]
            else:
                print("****key--：%s ,value--: %s" % (key, dic_json[key]))
                dic[key] = dic_json[key]


# 遍历json字典key值后，查到ke则修改值value
def check_json_value(dic_json, k, v):
    if isinstance(dic_json, dict):
        for key in dic_json:
            if key == k:
                dic_json[key] = v
            elif isinstance(dic_json[key], dict):
                check_json_value(dic_json[key], k, v)

# Ctrl+R:替换

if __name__ == "__main__":
    # json文件发送形式
    Sendjson_txt = """
    {
      "header":{
        "funcNo": "IF010002",
        "opStation": "11.11.1.1",
        "appId": "aaaaaa",
        "deviceId": "kk",
        "ver":"wx-1.0",
        "channel": "4"
      },
      "payload": {
        "mobile": "13817120001"
      }
    }
    """
    # 格式化
    data_json = data_Json(Sendjson_txt)
    print('data_json: ', data_json)
    print("*" * 10)
    #
    json_txt(data_json)
    print("dic ---: " + str(dic))

    #
    print("data_json 变更前   :")
    print(data_json)
    check_json_value(data_json, 'mobile', '13333333333')
    print("data_json 变更后   :")
    print(data_json)
