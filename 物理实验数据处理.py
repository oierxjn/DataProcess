import data_process


data1 = data_process.GetData()

data1.file_get("1.txt").lines_extract_data()

data1.data_add_byfunc(lambda x: (x[1] + x[2])/2)
data1.data_add_byfunc(lambda x: (x[3] + x[4])/2)
data1.data_add_byfunc(lambda x: (x[5] + x[6])/2)

data1.print_data(position=[7, 8, 9])

data2 = data_process.GetData()
data2.file_get("2.txt").lines_extract_data()

data2.data_add_byfunc(lambda x: (x[1] + x[2])/2)
data2.data_add_byfunc(lambda x: (x[3] + x[4])/2)
data2.data_add_byfunc(lambda x: (x[5] + x[6])/2)

data2.print_data(position=[7])


data3 = data_process.GetData()

data3.file_get("3.txt").lines_extract_data()

data3.data_add_byfunc(lambda x: (x[1] + x[2])/2)
data3.data_add_byfunc(lambda x: (x[3] + x[4])/2)
data3.data_add_byfunc(lambda x: (x[5] - x[6]))

data3.print_data(position=[7])