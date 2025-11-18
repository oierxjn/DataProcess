import data_process
import numpy as np
import os
import re

n = 5
T = 1.567

def process_data(m: int):
    with open(f"{m}.txt","r") as f:
        lines = f.readlines()

    data = []
    tmp = []
    cnt = 0
    for line in lines:
        linedata = str(line).strip().split()
        for item in linedata:
            tmp.append(float(item))
            cnt += 1
            if cnt == 3:
                data.append(tmp)
                tmp = []
                cnt = 0

    datap = data_process.GetData(data)

    datap.data_add_byfunc(lambda x: (np.log(x[1])-np.log(x[2]))/n/T)

    cnt = 0
    num_sum = 0
    for i in datap.data:
        num_sum += i[3]
        cnt += 1
    
    num_sum /= cnt
    print(f"{m}: {num_sum}")
    return num_sum

tot_sum = 0
tot_cnt = 0
pattern = re.compile(r'^(\d+)\.txt$')
for name in os.listdir():
    full_path = os.path.join(os.getcwd(), name)
    if os.path.isfile(full_path):
        m_group = pattern.fullmatch(name)
        if m_group is None:
            continue
        m = int(m_group.group(1))
        tot_sum += process_data(m)
        tot_cnt += 1

print(tot_sum/tot_cnt)
