import json
import urllib.request


# 使用url获取数据
def get_url_data(url):
    r = urllib.request.urlopen(url)
    data = r.read().decode('utf-8')
    data = json.loads(data)
    return data


# 根据uid获取sid
def get_data_list(uid):
    url = f'https://api.bilibili.com/x/polymer/space/seasons_series_list?mid={uid}&page_num=1&page_size=20'
    datas = get_url_data(url)
    seasons_list = datas["data"]["items_lists"]["seasons_list"]
    series_list = datas["data"]["items_lists"]["series_list"]
    total_list = seasons_list + series_list
    res_list = []
    if not total_list:
        return res_list
    for seasons in seasons_list:
        seasons_meta = seasons["meta"]
        seasons_name = seasons_meta["name"]
        sid = seasons_meta["season_id"]
        total_seasons = seasons_meta["total"]
        seasons_url = f'https://api.bilibili.com/x/polymer/space/seasons_archives_list?mid=508370718&season_id={sid}&sort_reverse=false&page_num=1&page_size={total_seasons}'
        seasons_archives = get_url_data(seasons_url)["data"]["archives"]
        seasons_data = {
            "name": seasons_name,
            "archives": seasons_archives
        }
        res_list.append(seasons_data)
    for series in series_list:
        series_meta = series["meta"]
        series_name = series_meta["name"]
        sid = series_meta["series_id"]
        total_series = series_meta["total"]
        series_url = f'https://api.bilibili.com/x/series/archives?mid={uid}&series_id={sid}&only_normal=true&sort=desc&pn=1&ps={total_series}'
        series_archives = get_url_data(series_url)["data"]["archives"]
        series_data = {
            "name": series_name,
            "archives": series_archives
        }
        res_list.append(series_data)
    return res_list

