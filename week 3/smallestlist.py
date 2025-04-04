def smallest_list(elements):
    return min(elements)


elements=[]
limit=int(input("enetr the length"))
for i in range(limit):
    temp=int(input("enetr the elements"))
    elements.append(temp)
smallest_element=smallest_list(elements)
print("smallest element is",smallest_element)
