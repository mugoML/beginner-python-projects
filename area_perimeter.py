import math
#Perimeter and area of a square
print("calculating perimeter and area of a square")
square_side = float(input("Enter measurements: "))
print()
perimeter = square_side * 4
area = pow(square_side, 2)
print(f"""The perimeter is {perimeter} cm
      The area of the square is {area} cm^2
""")


# perimeter and area of rectangle
print("Calculating perimeter and area of a rectangle.")
length = float(input("Length: "))
width = float(input("Width: "))
print()
perimeter = (length + width) * 2
area = length * width
print(f"The perimeter of the rectangle is {perimeter} cm")
print(f"The area of the rectangle is {area} cm^2")

# circumference and area of a circle
print("Calculating area and perimeter of a circle.")
diameter = float(input("Diameter: "))
radius = diameter / 2
circumference = math.pi * diameter
area = math.pi * pow(radius, 2)
print()
print(f"The perimeter of the circle is {round(circumference, 2)} cm.")
print(f"The area of the circle is {round(area, 2)} cm^2.")

# finally done
print("Here are the simple methods of using Input")