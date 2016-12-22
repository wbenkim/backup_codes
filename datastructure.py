def manipulate_data(data_type, data):
    if data_type == "list":
        data.reverse()
        return data
    if data_type == "set":
        countries = ['ANDELA','TIA','AFRICA']
        return data.union(set(countries))

    if data_type == "dict":
        return data.keys()

print(manipulate_data("list",[1,4,2,7,6,5]))
print(manipulate_data("set",{'a','b','c'}))
print(manipulate_data("dict",{'a':'1','b':'2','c':'3'}))
