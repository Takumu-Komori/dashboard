import pandas as pd
import random 
import sys

def make_demodata():
    print("行の長さ")
    line = input()
    line = int(line)
    print("列の長さ")
    row = input()
    row = int(row)

    data = []
    columns = [i for i in range(row)]
    #各行のデータ生成

    for i in range(line):
        rlist = [random.randint(1, 100) for _ in range(row)]
        data.append(rlist)


    df = pd.DataFrame(data, columns=columns)
    print("ファイル名")
    file_name = input()


    df.to_csv(f'{file_name}.csv')

make_demodata()

