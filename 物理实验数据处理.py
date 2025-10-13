import data_process
import os

def print_list(t: list):
    for i in t:
        print(i, end=' ')
    print('')

swap_flag: bool = True
zip_flag: bool = True
title = "标定传感器灵敏度测量数据"

x_lable = 'I_m'
y_lable = 'U_s'

x_unit = 'mA'
y_unit = 'mV'

col = [f'${y_lable} ({y_unit})$', f'${x_lable} ({x_unit})$']

x: list = None
y: list = None


get_data = data_process.GetData()

x, y = get_data.file_get("1.txt").lines_extract_data().data_extract_xy(swap_flag=swap_flag)

get_data.table_drawing(zip_flag=zip_flag, columns=col, title=title)

run_Linear = data_process.UnivariateLinearRegression()
run_Linear.fit(x,y)

run_Linear.show_graph(
    x_label=x_lable,
    y_label=y_lable,
    x_unit=x_unit,
    y_unit=y_unit
)

print(run_Linear.slope)
print(run_Linear.score())

# ==========================================
# swap_flag: bool = True
zip_flag: bool = False
title = "螺线内磁感应强度B与位置刻度x的关系"

x = ['x','cm']
U1 = ['U_1','mV']
U2 = ['U_2','mV']
Us = ['U_s','mV']
B = ['B','mT']

ks = 31.9

col = [
    f'${x[0]} \; ({x[1]})$', 
    f'${U1[0]}\; ({U1[1]})$', 
    f'${U2[0]}\; ({U2[1]})$',
    f'${Us[0]}\; ({Us[1]})$',
    f'${B[0]} \; ({B[1]})$'
]
result = (
    get_data.file_get("2.txt")
            .lines_extract_data()
            .sort()
            .data_add_byfunc(lambda x: (x[1]-x[2])/2)
            .data_add_byfunc(lambda x: x[3]/ks)
)
get_data.table_drawing(zip_flag=zip_flag, columns=col, title=title, small_size=True)

# =================================================
x_lable = x[0]
y_lable = Us[0]

x_unit = x[1]
y_unit = Us[1]

title = ""

Bx_data = data_process.GetData()
Bx_data.data = Bx_data.extract_data_from_data(
    lambda x: [x[0], x[4]],
    get_data.data
)

xt, yt = get_data.data_extract_xy(0, 4)

graph = data_process.Visual(title="通电螺线管轴线上磁感应强度分布散点图")
graph.set_label(f"{x[0]}({x[1]})", f"{B[0]}({B[1]})")

graph.add_multi_dot(xt, yt)
graph.show()
graph.reset()

graph.set_title(title="通电螺线管轴线上磁感应强度分布曲线")

graph.set_label(f"{x[0]}({x[1]})", f"{B[0]}({B[1]})")
graph.add_multi_dot(xt, yt, color="red")
graph.add_line_between_dot(xt ,yt)
graph.show()