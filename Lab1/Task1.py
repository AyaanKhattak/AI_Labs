def sundaes():
    flavors=["vanilla","chocolate","strawberry","pistacchio"]
    sauces = ["caramel", "butterscotch", "chocolate"]
    count=0
    for flavor in flavors:
        for sauce in sauces:
            print(flavor+" ice cream sundae with "+sauce+" sauce")
            count+=1
    return count

total_com=sundaes()
print("Total number of sundaes: ",total_com)