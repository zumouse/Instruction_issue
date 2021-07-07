#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 23:57
# @Author  : super_kun
# @Email   : mouse_zy@qq.com
# @File    : cli_issue.py
# @Software: PyCharm
"""
该模块需求
该模块功能
"""
import argparse
import json


# import


# class


# decorator


# function
def sys_parameter():
    """
    1.0 终点坐标:
    {"action":"move", "data":{"lng":"123.456789", "lat":"123.465789"}}
    2.0 取消订单:
    {"action":"cancelorder"}
    3.0 叫车:
    touser -- 车找人
    toplace -- 车等人
    {"action":"request", "type":"touser", "data":{"lng":"123.456789", "lat":"123.465789"}}
    :return:
    """
    pass


# function-main
def main():
    print("main-function......")


# module-test
if __name__ == '__main__':
    print("module-test......")
    parser = argparse.ArgumentParser(description='Process some integers.')

    args = parser.parse_args()
    print(args.accumulate(args.integers))
    # para01 = json.loads(sys.argv[1])
    # print(type(para01))
