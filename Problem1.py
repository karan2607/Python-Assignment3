user = input("Please provide a string : ")
split_value = []
tmp = ''
for c in user:
    if c == ' ':
        split_value.append(tmp)
        tmp = ''
    else:
        tmp += c
if tmp:
    split_value.append(tmp)
print(split_value)

for i in range(len(split_value)-1):
    for j in range(i+1,len(split_value)):
        if split_value[i]>split_value[j]:
            temp = split_value[i]
            split_value[i] = split_value[j]
            split_value[j] = temp
print("Output 2 : {}".format(split_value))
 
