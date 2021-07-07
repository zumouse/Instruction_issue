#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/7/5 20:41
# @Author  : super_kun
# @Email   : mouse_zy@qq.com
# @File    : bd09ll_to_bd09mc.py
# @Software: PyCharm
"""
该模块需求:
1.0 百度坐标系转换：
    BD09LL[度为单位，百度经纬度坐标] --> UTM[米为单位，百度墨卡托米制坐标]
    转换路径：BD0LL --> BCJ02 --> WGS84 --> UTM
2.0 BD09LL 绘制地图时用
    BD09MC 自动驾驶导航用
该模块功能
"""

# import
import requests
import json
import converter
from pyproj import Proj


# import argparse


# class


# decorator


# function
def get_bd09ll_to_bd09mc(lng, lat):
    """
    利用百度地图web服务提供的api,
    实现BD09LL[百度经纬度坐标] 转换为  BD09MC[百度墨卡托米制坐标]
    5：百度地图采用的经纬度坐标（bd09ll）
    http://api.map.baidu.com/geoconv/v1/?coords=114.21892734521,29.575429778924&from=5&to=6&ak=RHaqBj2RZwz4KNoeKG4FxjNYpy47vr72
    :param lng: 经度[百度经纬度坐标] -- string
    :param lat: 纬度[百度经纬度坐标] -- string
    :return: BD09MC[百度墨卡托米制坐标] -- list
    """
    url = "http://api.map.baidu.com/geoconv/v1/?coords=" + lng + "," + lat \
          + "&from=5&to=6&ak=RHaqBj2RZwz4KNoeKG4FxjNYpy47vr72"
    response = requests.get(url)
    data = json.loads(response.text)
    print(response.text)
    # data dict == {'status': 0, 'result': [{'x': 12714931.180000365, 'y': 3427808.711290251}]}
    # data["result"] list == [{'x': 12714931.180000365, 'y': 3427808.711290251}]
    return data["result"][0]


def wgs84_to_utm(lng, lat):
    """
    # 地理坐标系WKID：https://developers.arcgis.com/javascript/3/jshelp/gcs.htm
    # 投影坐标系WKID：https://developers.arcgis.com/javascript/3/jshelp/pcs.htm
    wgs84经纬度 中国[72°， 138°]
    UTM投影带   中国[43, 53]
    Transformer.from_crs is parameter:
    crs_from: Any -- 输入的坐标参考系统
    crs_to：       -- 输出的坐标投影带数
    :param lng: 经度 -- int
    :param lat: 纬度 -- int
    :return: UTM -- list
    """
    band_number = int(lng // 6) + 31
    p = Proj(proj='utm', zone=band_number, ellps='WGS84', preserve_units=False)
    return p(lng, lat)


def bd09_to_utm(lng, lat):
    """
    :param lng: 经度 -- int
    :param lat: 纬度 -- int
    :return: UTM -- list
    """
    lng, lat = float(lng), float(lat)
    lng, lat = converter.bd09_to_wgs84(lng, lat)
    print(lng, lat)
    return wgs84_to_utm(lng, lat)


# function-main
def main():
    print("main-function......")
    # lng = "114.21892734521"
    # lat = "29.575429778924"
    # bd09mc = get_bd09ll_to_bd09mc(lng, lat)
    # print("x=", bd09mc["x"])
    # print("y=", bd09mc["y"])
    print("BD09LL to UTM:")
    lng01 = 125.21892734521
    lat01 = 46.575429778924
    utm = bd09_to_utm(lng01, lat01)
    print(utm)


# module-test
if __name__ == '__main__':
    print("module-test......")
    main()
