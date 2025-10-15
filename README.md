# 数据处理
data_process.py 用于处理数据，提供了绘制功能  

物理实验数据处理.py 中调用了data_process.py 中的功能  

1.txt 和 2.txt 是实验数据

## 关于实验

用到的参数  

$$
\begin{aligned}
螺线管直径&\quad D = 0.035m\\
螺线管长度&\quad L = 0.260m\\
真空磁导率&\quad \mu _0 = 4\pi \times 10^{-7} T\cdot m\cdot A^{-1}\\
螺线管匝数&\quad N = 3000\\
霍尔电压&\quad U_s \\
正向电流的霍尔电压&\quad U_{s+} \\
反向电流的霍尔电压&\quad U_{s-} \\
励磁电流&\quad I_m \\
测量位置&\quad x \\
\end{aligned}
$$

用到的公式  

$$
\begin{aligned}
K_s &= \frac{\sqrt{D^2 + L^2}}{\mu _0N}\cdot k\\
k &= \frac{\Delta U_s}{\Delta I_m}
\end{aligned}
$$

显然这个 $k$ 需要利用实验数据进行线性回归获得。

如果上面的那些参数不变，那么 $K_s = 69.58922362 \cdot k$ 。

$k$ 的大概的值为 $0.45$ 。$K_s$ 的大概的值为 $31$ 。

## 数据格式
1.txt 中是测量位置固定（默认$16cm$）时测量 $U_s$ 和 $I_m$ 的数据，每一行是一个数据点，空格或Tab隔开。  
注意第一列是测量到的霍尔电压，单位是$mV$，第二列是测量到的励磁电流，单位是$mA$。  
你可以在Excel或WPS等表格软件中提前处理好数据格式，然后将处理好的数据框选后直接复制到 1.txt 中。

2.txt 中是测量位置变化时测量 $x$ 、 $U_{s+}$ 和 $U_{s-}$ 的数据，每一行是一个数据点，空格或Tab隔开。  
但是注意一行中第一个数是测量位置，单位是$cm$，第二个数是测量到的正向电流的霍尔电压，单位是$mV$，第三个数是测量到的反向电流的霍尔电压，单位是$mV$，而且数值基本上都是负的。  
你可以在Excel或WPS等表格软件中提前处理好数据格式，然后将处理好的数据框选后直接复制到 2.txt 中。

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
直接点开 data_process.py 即可运行。  
或者在项目根目录的命令行中输入以下命令运行：
```
python data_process.py
```