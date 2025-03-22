a=[1,3,5]
b=[2,4,6]
c=a+b
d=c.copy()
d.sort()
d.reverse()
c[3]=42
d.append(10)
c.extend([7,8,9])

print("Frist three elements of c:",c[:3])
print("Last three elements of d:",d[-1])
print("Lenght of d: ",len(d))

print("\nFinal state:")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)