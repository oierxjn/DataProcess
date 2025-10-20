import data_process

config = []

# 预先插入空行
config.append([])

with open("config.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        try:
            line = list(map(int, line.split()))
        except ValueError:
            continue
        config.append(line)

data1 = data_process.GetData()

data1.file_get("1.txt").lines_extract_data()

# 若第一列有额外数据，尝试忽略
if len(data1.data[0]) == 6:
    data1.insert_single()

data1.data_add_byfunc(lambda x: (x[config[1][0]*2-1] + x[config[1][0]*2])/2)  #7
data1.data_add_byfunc(lambda x: (x[config[1][1]*2-1] + x[config[1][1]*2])/2)  #8
data1.data_add_byfunc(lambda x: (x[config[1][2]*2-1] + x[config[1][2]*2])/2)  #9
data1.data_add_byfunc(lambda x: abs(x[7] - x[8]))  #10
data1.data_add_byfunc(lambda x: abs(x[8] - x[9]))  #11
data1.data_add_byfunc(lambda x: (x[10]*x[11])/(x[10]+x[11]))  #12

print("第一组焦距")
data1.print_data(position=[12])

average_data1 = 0
for i in range(len(data1.data)):
    average_data1 += data1.data[i][12]
average_data1 /= len(data1.data)

print(f"第一组平均焦距为：{average_data1:.4f}")

table_col1 = ["次数", "$u$", "$v$", "$f$"]
table_data1 = data_process.GetData(data1.extract_data_from_data(lambda x: [x[10], x[11], x[12]]))
table_data1.insert_byfunc(lambda _, i: i+1)
table_data1.table_drawing(
    columns=table_col1,
    title="物距-像距法测凸透镜焦距"
)

data2 = data_process.GetData()
data2.file_get("2.txt").lines_extract_data()

if len(data2.data[0]) == 6:
    data2.insert_single()

data2.data_add_byfunc(lambda x: (x[config[2][0]*2-1] + x[config[2][0]*2])/2)  #7
data2.data_add_byfunc(lambda x: (x[config[2][1]*2-1] + x[config[2][1]*2])/2)  #8
data2.data_add_byfunc(lambda x: (x[config[2][2]*2-1] + x[config[2][2]*2])/2)  #9
data2.data_add_byfunc(lambda x: abs(x[7] - x[8]))  #10
data2.data_add_byfunc(lambda x: abs(x[8] - x[9]))  #11
data2.data_add_byfunc(lambda x: (x[10]*x[11])/(x[10]+x[11]))  #12

print("第二组焦距")
data2.print_data(position=[12])

average_data2 = 0
for i in range(len(data2.data)):
    average_data2 += data2.data[i][12]
average_data2 /= len(data2.data)

print(f"第二组平均焦距为：{average_data2:.4f}")

table_col2 = ["次数", "$u$", "$v$", "$f$"]
table_data2 = data_process.GetData(data2.extract_data_from_data(lambda x: [x[10], x[11], x[12]]))
table_data2.insert_byfunc(lambda _, i: i+1)
table_data2.table_drawing(
    columns=table_col2,
    title="共轭法测凸透镜焦距"
)

data2_has_matched = []
match_data2 = []

def element_match(i: int, j: int, deviation: float=0.01):
    if abs(i - j)*2/(i + j) <= deviation:
        return True
    return False
    

for i in range(len(data2.data)):
    if i in data2_has_matched:
        continue
    for j in range(i+1, len(data2.data)):
        if j in data2_has_matched:
            continue
        if element_match(data2.data[i][7], data2.data[j][7]):
            if element_match(data2.data[i][9], data2.data[j][9]):
                data2_has_matched.append(i)
                data2_has_matched.append(j)
                match_data2.append([data2.data[i][7], data2.data[i][8], data2.data[j][8], data2.data[i][9]])
                break

# print(data2_has_matched)

data2 = data_process.GetData(match_data2)
table_col2 = ["次数", "物屏", "第一次成像透镜", "第二次成像透镜", "白屏"]
data2.insert_byfunc(lambda _, i: i+1)
data2.table_drawing(
    columns=table_col2,
    title="共轭法测凸透镜焦距"
)

data3 = data_process.GetData()

data3.file_get("3.txt").lines_extract_data()

if len(data3.data[0]) == 4:
    data3.insert_single()

data3.data_add_byfunc(lambda x: (x[config[3][0]*2-1] + x[config[3][0]*2])/2)  #5
data3.data_add_byfunc(lambda x: (x[config[3][1]*2-1] + x[config[3][1]*2])/2)  #6
data3.data_add_byfunc(lambda x: abs(x[5] - x[6]))  #7

print("第三组焦距")
data3.print_data(position=[7])

average_data3 = 0
for i in range(len(data3.data)):
    average_data3 += data3.data[i][7]
average_data3 /= len(data3.data)

print(f"第三组平均焦距为：{average_data3:.4f}")

table_col3 = ["次数", "物屏", "凸透镜"]
table_data3 = data_process.GetData(data3.extract_data_from_data(lambda x: [x[5], x[6]]))
table_data3.insert_byfunc(lambda _, i: i+1)
table_data3.table_drawing(
    zip_flag=True,
    columns=table_col3,
    title="自准直法测凹透镜焦距"
)