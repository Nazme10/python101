def my_f(first,middle=' ',last):
    full= f'{first} {middle} {last}'
    return full
f_name = input("write first")
m_name = input("write mid")
l_name = input("write last")

full_name=my_f(first=f_name,middle=m_name,last=l_name)
print(full_name) 