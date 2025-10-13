import numpy as np
import matplotlib.pyplot as plt
class Visual:
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
    
    def add_dot(self, x: int, y: int):
        x = np.array([x])
        y = np.array([y])
        return self.add_multi_dot(x, y)

    def add_multi_dot(self, x, y, color='blue'):
        self._ax.plot(x, y, marker='o', linestyle='', color=color, markersize=8)
        return self

    def add_line_between_dot(self, x, y, label=None):
        
        self._ax.plot(x, y, label=label)
        
        self._fig.canvas.draw_idle()  # 更新画布

    def show(self, 
            show_legend: bool=True,
            show_grid: bool=True
        ):
        """显示窗口（阻塞）"""
        if show_legend is True:
            self._ax.legend()
        if show_grid is True:
            self._ax.grid(True)
        plt.show()

    def clear(self):
        """清空绘图"""
        self._ax.clear()

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

window = Visual()
window.add_line_between_dot(x, y, "1")
# window.add_line_between_dot(y, x, "2")
window.add_multi_dot(x, y)
window.show()