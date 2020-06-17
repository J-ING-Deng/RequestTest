import requests

# get请求 轮播图
# url = "http://106.53.232.198:2333/get_title_img?num=3" #接口信息
# res = requests.get(url)     #发送请求并且获得返回值
# print(res.text)             #打印返回值信息

# #登录 post请求
u = "http://106.53.232.198:2333/login" #接口信息
d = {"username":"jing5","password":"djy98623"}
res = requests.post(url=u,json=d)   #使用post方法向u接口请求，并且使用json格式的数据传参数
print(res.text)             #打印返回值信息

#token要从登录之后来取
# r = res.json()
# print(r.get("data").get("token"))
token = res.json()["data"]["token"] #res.json（）把返回值变成pthon的字典
print(token)

#评论文章
u1 = "http://106.53.232.198:2333/comment/new"
d1 = {"ctype": 1, "comment": "当时是士大夫十分", "fid": "3738"}
h1 = {"token":token}

res = requests.post(url=u1,json=d1,headers=h1) #headers 请求头
print(res.text)             #打印返回值信息