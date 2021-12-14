import pandas as ps

def test():
    print("----------------------------数据信息csv数据格式----------------------------------")
    #数据源 csv
    red = ps.read_csv('cav/nba.csv')
    print(red.info())
    print(red.head(9))
    print(red.tail())

    print("----------------------------数据信息json数据格式----------------------------------")

    redjson = ps.read_json('json/user.json')
    print(redjson.to_string())


    print("----------------------------数据清洗----------------------------------")

    nallstirng =  ["n/a", "na", "--"]
