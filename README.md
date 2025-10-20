# 这个项目是什么
用来快捷地帮助同济的学子处理物理实验中的数据。

项目中对特定的实验提供了数据处理、图标绘制。

# 如何使用

## 获取代码
左上角切换到对应的实验分支，再点右边的code按钮，即可下载对应的zip包。

或者点这里在github上下载：  
[用霍尔效应法测量磁感应强度](https://github.com/oierxjn/DataProcess/archive/refs/heads/%E7%94%A8%E9%9C%8D%E5%B0%94%E6%95%88%E5%BA%94%E6%B3%95%E6%B5%8B%E9%87%8F%E7%A3%81%E6%84%9F%E5%BA%94%E5%BC%BA%E5%BA%A6.zip)  
[透镜焦距的测量](https://github.com/oierxjn/DataProcess/archive/refs/heads/%E9%80%8F%E9%95%9C%E7%84%A6%E8%B7%9D%E7%9A%84%E6%B5%8B%E9%87%8F.zip)  

## 安装依赖
项目需要python 3.10及以上的版本，更低版本不保证正常运行，并且在未来不进行维护。

项目需要pip

解压下载的zip包，在项目根目录下安装依赖：

```
pip install -r requirements.txt
```

如果下载过慢，上网搜索如何使用pip镜像源下载。推荐清华源。

## 填入数据

项目根目录下有一个README.md 文件，里面有关于对应实验数据格式的说明。

根据README说明，将实验数据相应文件中。

## 运行项目

在项目根目录下运行：

```
python 物理实验数据处理.py
```

# 反馈

你可以直接在我的github仓库中提交[issue](https://github.com/oierxjn/DataProcess/issues)。

或者是通过邮箱联系我：2553759@tongji.edu.cn