def manipulate_data(data_type, data):
    if data_type == "list":
        data.reverse()
        return data

    if data_type == "set":
        li = ["ANDELA","TIA","AFRICA"]
        return data.union(set(li))

    if data_type == "dict":
        return data.keys()

print (manipulate_data("list",[2,3,4,5]))
print (manipulate_data("set",{2,3,4,5}))
print (manipulate_data("dict",{"a":1,"b":2,"c":3}))
