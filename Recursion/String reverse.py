
def str_revese(str):
    
    if len(str)<=1:
        return str

    return str_revese(str[1:])+str[0]

str="shahin"
val=str_revese(str)
print(str)
print(val)