d1 = int(input("Enter first point: "))
d2 = int(input("Enter second point: "))

dist = d2 - d1
if dist < 0:
    dist = - dist

print("The distance btw the two pts is: ", dist)
