import datetime
from glob import glob
import itertools
import os
from pathlib import PurePath
from xml.etree import ElementTree
import collections
import pandas as pd


def getFilePaths(folder_path: str, extension: str):
    wildcard = os.path.join(folder_path, f"*.{extension}")
    filePaths = glob(wildcard)
    return filePaths


def getAnnotationList(xml_path):
    tree = ElementTree.parse(xml_path)
    root = tree.getroot()
    objects = root.findall("object")
    nameList = [o.find("name").text for o in objects]
    return nameList


def counter(xml_folder_path):
    print("計測中…\n")

    xml_list = getFilePaths(xml_folder_path, "xml")
    files = [PurePath(p).stem for p in xml_list]
    names = itertools.chain.from_iterable([getAnnotationList(p) for p in xml_list])

    num = len(files)
    nameDict = collections.Counter(names)
    data = (
        pd.Series(nameDict.values(), nameDict.keys())
        .sort_index(axis=0)
        .sort_values(ascending=False)
    )

    print(data)
    print("総ファイル数: ", num)

    generate = input("\nエクセルファイルを生成しますか？[y/N]").lower()
    if generate in ["y", "ye", "yes"]:
        xlsx = f"{datetime.date.today()} {num}Files.xlsx"
        data.to_excel(xlsx, header=False)
        print(f"\n{xlsx}として保存しました")

    input("\nEnterで終了")
