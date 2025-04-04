def largest_list(elements):
    return max(elements)


elements=[]
limit=int(input("enetr the length"))
for i in range(limit):
    temp=int(input("enetr the elements"))
    elements.append(temp)
largest_element=largest_list(elements)
print("largest element is",largest_element)
