#git pull origin main
#py -m venv venv
#.\venv\Scripts\active
# git add -A
# git commit -m "6/9"
# git push origin main


#print()
print("変数", end='')#endを指定しないと\nになる

#空の辞書
dic = {}
#キーが辞書に存在しないなら追加存在するなら更新になる
dic["key"] = "value"
#まとめて追加
dic2 = {}
dic.update(dic2)
#キーの取り出し
key = dic.keys()
for key in dic:
    pass



#集合による重複排除
num_list =[1,1,1,2,2,3,4,4,4,4]
num_set = set(num_list) #集合を作成
num_list = list(set(num_list)) #集合の特性を利用して重複排除

#if文
if False:
    pass
elif 50 > 100:
    pass
else:
    true = True
list = {"b"}
if "a" in list:
    pass
    #listの中に"a"がある
elif "b" not in list:
    pass
    #listの中に"b"はない

#for文
for item in range(0,10):#range(ここから,ここ未満,歩幅 ふつうは０)
    pass#itemに0から9までの数字が入る
    break
    continue
#for-else
for i in range(10):
    if i=="a":
        break
else:
    pass#forを完走したら


#アンパック
tuple = ((1,"a"),(2,"b"))
for a,b in tuple:
    pass

#内包表記 []内に記述
number_list = [i for i in range(5)]#0から4のリスト
[print(i,j) for i in range(3) for j in range(3)]#複雑なものも書けはするが可読性はよくない

#関数
#hello() エラー
def hello(hikisu, hikisu2=1):
    print(hikisu, hikisu2)
hello("dd")
#引数
def kansu(hikisu, *hikisu2):
    #hikkisu2はタプルになる
    for i in hikisu2:
        pass
kansu(1,"a","b","c")

def kansu2(hikisu, **kwargs):
    #kwargsは辞書
    for a,b in kwargs.items():
        pass

#スコープ
def kansu3():
    kan3 = 3
    b= 99
    return g+1,b
b =29
g=1;
#print(kansu3(),b);#returnは(2,99)
#print(kan3)#aは存在しない

#クラス
class ClassName:
    data = "データ"
    #コンストラクタ. 特殊メソッド__init__を持たせる。
    def __init__(self, name="びび"):
        data = name

    def method(self, gg):#クラスメソッドは第一引数にインスタンス自身を渡す。別にselfじゃなくてもいい
        h = self.data

GG = ClassName() # インスタンス化
GG.method("gg")

import  datetime


