def max_rectangle(list_of_pairs:list=[(1, 2), (3, 4), (5, 6), (-1, 6), (-3, -8)]):
    max=0
    max_two_points=[]
    max_two_points.append(list_of_pairs[0])
    max_two_points.append(list_of_pairs[1])
    for i in range(len(list_of_pairs)):
        for k in range(1,len(list_of_pairs)):
            if area_of_two_points(list_of_pairs[i],list_of_pairs[k])>max:
                max=area_of_two_points(list_of_pairs[i],list_of_pairs[k])
                max_two_points=[list_of_pairs[i],list_of_pairs[k]]
    return max_two_points

def area_of_two_points(point1:tuple,point2:tuple):
    area=(point1[1]-point2[1])*(point1[0]-point2[0])
    if area<0:
        return area*(-1)
    else:
        return area
List_of_pairs=input()
List_of_pairs=eval(List_of_pairs)
print(max_rectangle(List_of_pairs))