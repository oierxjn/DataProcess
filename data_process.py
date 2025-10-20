# data_process.py

import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as slm
import enum
import msvcrt

def override(func):
    return func

class UnivariateLinearRegression(slm.LinearRegression):
    def __init__(self):
        super().__init__()
        self.slope = None
        self.intercept = None
        self.x = None
        self.y = None
        
    @override
    def fit(self, x: list, y: list):
        x = np.array(x).reshape(-1, 1)
        y = np.array(y)
        
        super().fit(x, y)
        
        self.slope = self.coef_[0]
        self.intercept = self.intercept_
        self.x = x
        self.y = y
        
        return self
    
    @override
    def score(self):
        x = self.x
        y = self.y
        return super().score(x,y)
    
    def show_graph(self, title="实验数据", x_label="自变量", y_label="因变量", x_unit='', y_unit='', title_description="线性拟合"):
        x = self.x
        y = self.y
        slope = self.slope
        intercept = self.intercept
        
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False


        plt.scatter(x, y, color="blue", label=title)
        plt.plot(x, self.predict(x), color="red", linewidth=2, label="拟合直线")
        plt.xlabel(f"${x_label} \; {x_unit}$")
        plt.ylabel(f"${y_label} \; {y_unit}$")
        plt.title(f"${y_label}-{x_label}$ {title_description}")

        # mid_x = (x.min() + x.max()) / 2
        # mid_y = slope * mid_x + intercept
        # plt.text(mid_x, mid_y, f"k = {slope:.2f}", fontsize=12, color="blue")

        plt.legend()
        plt.grid(True)
        plt.show()
        
        return self

class GetData:
    def __init__(self ,data: list=None):
        self.lines: list = None
        self.data: list = data
        return
    
    def file_get(self, file_name="1.txt"):
        lines: list = None
        with open(file_name,'r') as f:
            lines = f.readlines()
        self.lines = lines
        return self
    
    class DataLayout(enum.Enum):
        VERTICAL = 1
        HORIZONTAL = 2

    def data_extract_xy(self, 
            x=0,
            y=1,
            data:list=None,
            swap_flag: bool = False,
            layout=DataLayout.VERTICAL 
        ):
        """
        从数据中提取二元数据，提取两列。

        参数：
            x：自变量列索引，默认第0列。
            y：因变量列索引，默认第1列。
            data：要提取数据的列表，默认使用self.data。
            swap_flag：是否交换x和y，默认False。
            layout：数据布局，默认垂直布局。（暂时无作用）
        返回：一个元组(ax, ay)
            ax：提取的自变量列表。
            ay：提取的因变量列表。
        """
        if data == None:
            data = self.data

        ax = []
        ay = []
        for i in data:
            ax.append(i[x])
            ay.append(i[y])
        
        if swap_flag:
            ax, ay = ay, ax
        return ax, ay
    
    def lines_extract_data(self, lines=None):
        if(lines == None):
            lines = self.lines
        
        data = []
        
        for line in lines:
            line = line.strip()

            if not line:
                continue

            temp = list(map(float, line.split()))
            data.append(temp)

        self.data = data
        return self
    
    def table_drawing(self,
            zip_flag: bool=False, 
            columns: list=None,
            title="表格",
            data: list=None,
            small_size: bool=False
        ):
        """
        绘制表格。

        参数：
            zip_flag：是否转置数据，默认False。
            columns：表头列表，默认None。
            title：表格标题，默认"表格"。
            data：要绘制的数据，默认使用self.data。
            small_size：是否使用小字体，默认False。
        返回：无
        """
        if data == None:
            data = self.data
        table_data = [[round(x, 2) for x in row] for row in data]
        
        if columns != None:
            if len(columns)==len(data[0]):
                table_data.insert(0,columns)
            else:
                print("table_drawing表格绘制：表头元素数量和数据分类数不相等")
        
        if zip_flag:
            table_data = list(zip(*table_data))

        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.axis('off')

        table = ax.table(
            cellText=table_data,
            cellLoc='center',
            loc='center',
            bbox=[0, 0, 1, 0.92]
        )
        ax.text(
            x=0.5, 
            y=0.95, 
            s=title, 
            fontsize=16,
            fontweight="bold",
            ha="center"
        )

        table.auto_set_font_size(False)
        if small_size:
            table.set_fontsize(10)
        else:
            table.set_fontsize(14)
        table.scale(1.2, 1.2)

        plt.show()
    
    def sort(self, data: list=None):
        if data == None:
            data = self.data
        data.sort()
        return self
    
    def data_add_byfunc(self, func, data: list=None):
        """
        将数据列表的每一行传入给定函数，并将给定函数的返回值添加为新列。

        参数：
            func：传入的函数。将传入数据的一行为参数，需要有返回值
            data：要处理的数据列表，默认使用self.data。
        返回：
            self：返回当前实例，用于链式调用。
        """
        if data == None:
            data = self.data
        for i in data:
            i.append(func(i))
        return self
    
    def extract_data_from_data(self, 
            func,
            data:list=None
        ):
        """
        将数据列表的每一行传入给定函数，并将给定函数的返回值作为列，返回新数据列表。

        参数：
            func：传入的函数。将传入数据的一行为参数，需要有返回值。
            data：要处理的数据列表，默认使用self.data。
        返回：
            out_data：处理后的新数据列表。
        """
        if data == None:
            if self.data == None:
                print("extract_data_from_data提取数据时出错：输入数据为空，实例数据为空")
                return
            data = self.data
        out_data = []
        for i in data:
            out_data.append(func(i))
        return out_data
    
    def print_data(self, 
            position: list=None,
            data: list=None,
        ):
        if data == None:
            data = self.data
        if position == None:
            position = range(len(data[0]))
        for i in data:
            for j in position:
                print(i[j], end=" ")
            print("")
        return self
    
    def insert_single(self, position: int=0, value: float=0, data: list=None):
        """
        在数据列表的每一行的指定位置插入给定值。

        参数：
            position：插入位置，默认0。
            value：插入值，默认0。
            data：要处理的数据列表，默认使用self.data。
        返回：
            self：返回当前实例，用于链式调用。
        """
        if data == None:
            data = self.data
        for i in data:
            i.insert(position, value)
        return self
class Visual:
    """
    单例plt
    """
    _instance = None
    _fig = None
    _ax = None

    def __new__(cls, title="窗口", *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._fig, cls._ax = plt.subplots()
            cls._ax.set_title(title)
            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.rcParams['axes.unicode_minus'] = False

        return cls._instance
    
    def add_dot(self, x: int, y: int, color="blue"):
        x = np.array([x])
        y = np.array([y])
        return self.add_multi_dot(x, y ,color=color)

    def add_multi_dot(self, x, y, color="blue"):
        return self._ax.scatter(x, y, color=color)

    def add_line_between_dot(self, x, y, label=None):
        
        self._ax.plot(x, y, label=label)
        self._fig.canvas.draw_idle()

    def set_title(self, title):
        self._ax.set_title(title)

    def set_label(self, x_label="x", y_label="y"):
        self._ax.set_xlabel(x_label)
        self._ax.set_ylabel(y_label)

    def show(self, 
            show_legend: bool=True,
            show_grid: bool=True
        ):
        if show_legend is True:
            self._ax.legend()
        if show_grid is True:
            self._ax.grid(True)
        plt.show()

    def clear(self):
        """清空绘图"""
        self._ax.clear()

    @classmethod
    def reset(cls, title="窗口"):
        """
        重开窗口，重置单例
        """

        cls._instance = None
        cls._fig = None
        cls._ax = None

        return cls.__new__(cls, title=title)