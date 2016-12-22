
# iteration
def replicate_iter(times,data):
  data_list = []
  if(isinstance(data,(int)) or isinstance(data,(str))):
    if(isinstance(times,(int))):
      if(times <= 0):
        return data_list
      else:
        for i in range(0,times):
          data_list.append(data)
        return data_list
    else:
      raise ValueError("Invalid argument")
  else:
      raise ValueError("Invalid argument")




#   recursion
def replicate_recur(times,data):
  x = []
  if(isinstance(data,(int)) or isinstance(data,(str))):
    if(isinstance(times,( int))):
      if times <= 0 :
        return x
      else:
        return [data] + replicate_recur(times-1, data)
    else:
      raise ValueError("Invalid argument")
  else:
    raise ValueError("Invalid argument")