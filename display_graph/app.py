import json
from typing import List

# import requests
# 0以上の整数値を5つ入力させ、それぞれの値に対して、次の形式でグラフを描くプログラムを作成せよ。
# 形式：左端に値を表示し、適切に空白を空けて":"を書く
# その後ろに値の数だけ*を描くが、5個おきに空白を１つ入れる。

class InvalidError(Exception):
    pass
def is_number(x: str):
    if x.startswith("-"):
        x = x[1:]
    if not x.isdigit():
        return False
    return True
def number(x):
    if not is_number(x):
        raise InvalidError("整数値を入力してください。")
    return int(x)

# 入力された文字列を分割し、listする 
def split_numbers(text: str):
    text_list = text.split(",")
    number_list = []
    for i in text_list:
        i = number(i)
        number_list.append(i)
    return number_list

def number_display_graph(numbers:List[int])->List[str]:
    if len(numbers) > 5:
        numbers = numbers[0:5]
    graph = []
    for n in numbers:
        ind_number = str(n)+ "  :"
        for i in range(n):
            if i % 5 == 0 and i != 0 :
                ind_number += " "
            ind_number += "*"
        graph.append(ind_number)
    return graph
    


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    print(event)
    try:
        n = event.get('queryStringParameters').get('numbers')
        n = split_numbers(n)
        n = number_display_graph(n)
        print(n)
    except Exception as e:
        return{
        "statusCode": 400,
        "headers":{
            "Content-type": "application/json;charset=UTF-8"
        },
        "body":json.dumps({
            "message":str(e)
        },ensure_ascii=False).encode("utf8"),
    }

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": n,
            # "location": ip.text.replace("\n", "")
        }),
    }
