# 数据处理
data_process.py 用于处理数据，提供了绘制功能  

物理实验数据处理.py 中调用了data_process.py 中的功能  

1.txt 是实验数据

## 关于实验

由于只需要提交阻尼振动的$\beta $值，所以所以只考虑阻尼振动的数据。

用到的参数  

$$
\begin{aligned}
振幅\quad &\theta _n\\
五次后的振幅\quad &\theta _{n+5}\\
振动周期 \quad &T\\
\end{aligned}
$$

用到的公式  

$$
\begin{aligned}
\beta &= \frac{ln\theta _{n}-ln\theta _{n+5}}{5T}
\end{aligned}
$$

由于实验一般会固定测五次后的振幅，所以程序中只需要输入振幅即可。当然你可以在程序中修改这个值（默认值为$n=5$）。

振动周期由于是用的同样的仪器，所以不用写了，默认为$T=1.567$。同样的，程序中也可以修改这个值。

$\beta$ 的大概的值为 $0.07$ 

## 数据格式
你可以在校园网的环境登上 http://202.120.171.159/，然后将实验数据的阻尼振动部分复制到 1.txt 中。

我从网站上复制的数据是一列排列的（见1.txt），所以我写的程序会自动处理这个情况。

当然，也可以是行排列的（见2.txt）

对于所有格式，程序自动识别。三个数为一组，分别是序号（无意义，可以乱填，但是必须要有）、振幅、五次后的振幅。

为什么要设计序号这个东西？因为复制下来比较方便。鼠标一拖就复制下来了，只是多带了个序号。

## 运行

### 安装依赖
需要你先安装Python，建议版本为3.10及以上。  
然后你需要安装一些Python库，你可以在项目根目录的命令行中输入以下命令安装：
```
pip install -r requirements.txt
```

如果报错无pip命令，试试：
```
python -m pip install -r requirements.txt
```

如果你觉得下载太慢，你可以运行一下语句将pip源永久换成清华源
```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

利用清华源更新pip：
```
python -m pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple --upgrade pip
```
### 运行程序
直接点开 物理实验数据处理.py 即可运行。  
或者在项目根目录的命令行中输入以下命令运行：
```
python 物理实验数据处理.py
```