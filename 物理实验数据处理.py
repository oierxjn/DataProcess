import data_process

position = None
unit_list = None
unit = []

with open("config.txt", "r") as f:
    lines = f.readlines()
    position = lines[0].strip().split()
    unit_list = lines[1].strip().split()
    for i in unit_list:
        if i == "mm":
            unit.append(0.1)
        else:
            unit.append(1)


origin_data = data_process.GetData()

origin_data.file_get("1.txt").lines_extract_data()

data = data_process.GetData(
    origin_data.extract_data_from_data(
        func=lambda x: [x[int(position[0])]*unit[int(position[0])], x[int(position[1])]*unit[int(position[1])], x[int(position[2])]*unit[int(position[2])]]
        )
    )

data.data_add_byfunc(lambda x: (x[1] - x[2])) #3
data.data_add_byfunc(lambda x: (x[3]*x[3])) #4

data_flags = {}

def add_data(i):
    global data_flags
    return data_flags[i[0]]



for i in data.data:
    if i[0] in data_flags:
        continue
    for j in data.data:
        if j[0] in data_flags:
            continue
        if j[0] == i[0]+5 or j[0] == i[0]-5:
            ans = abs(i[4] - j[4])
            if j[0]>i[0]:
                data_flags[j[0]] = ans
                data_flags[i[0]] = 0
            else :
                data_flags[i[0]] = ans
                data_flags[j[0]] = 0

data.data_add_byfunc(add_data) #5
data.data_add_byfunc(lambda x: x[5]/(20*(589.3*0.0000001))) #6

col = ['级次', '$x1$', '$x2$', '$D_1$', '$D_1^2$', '$D_m-D_n$', '$R_{m-n}$']

data.table_drawing(columns=col , precision=4, title="用牛顿环测透镜的曲率半径实验数据记录表")
