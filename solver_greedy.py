#!/usr/bin/env python3

import sys
import math

from common import print_tour, read_input


def distance(city1, city2): #距離を求めている
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities) #リストの長さを求める

    dist = [[0] * N for i in range(N)]
    for i in range(N): #リストの長さ分だけfor文が回る
        for j in range(i, N): #iが今いる場所、jが次の地点の場所
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j]) #距離を求めている
            print("distance : ",i,j,dist[i][j]) # distance 0は同じ地点を指している

    current_city = 0 #初期値、０からスタート
    unvisited_cities = set(range(1, N)) #訪れていない場所をobject型？でセットしている
    tour = [current_city] #初期値をtourでセットしている

    while unvisited_cities: #訪れてない場所全部を見ている
        next_city = min(unvisited_cities,
                        key=lambda city: dist[current_city][city]) #最小値のものをnext_cityに入れる
        unvisited_cities.remove(next_city) #訪れていない場所から次のものを除外
        tour.append(next_city) #返す用のリストtourにappend
        current_city = next_city #今いる場所をcurrent_cityとして返している
    return tour


if __name__ == '__main__':
    assert len(sys.argv) > 1 #assertは想定と違ったら止まる（エラー処理）
    tour = solve(read_input(sys.argv[1])) #引数の１つ目を呼び出す、read_inputでファイルの読み込みを行っている
    print_tour(tour) #tour (list型) を呼び出す
