def find_consecutives(tup):#taking tuple as parameter, defining function.
    elements = iter(tup)#"iter ()" function returns an iterator in tuple(with this iterator ,can access the elements in the tuple sequentially.)and assigned elements.
    x,y=None,next(elements,None)#declaring x and y  with None in elements.
    consecutives=[y]#consecutive ones are put in "consecutives".
    while y is not None:
        x,y=y,next(elements,None)
        if y is not None and x + 1==y:#It is checked whether the numbers are consecutive or not.
            consecutives.append(y)#If the numbers are consecutive, they are added to "consecutives".
        else:
            if len(consecutives) > 1:
                yield list(consecutives)
            consecutives=[y]

print(list(find_consecutives((2,8,4,6,1,2,8,4,7,9,5,6,7))))