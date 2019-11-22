import random

room_lenght = random.randint(1,20)
room_width = random.randint(1,20)
print("Room lenght:")
print(room_lenght)
print("Room width:")
print(room_width)

print("The area of the room is :")
area = (room_lenght)*(room_width)
print(area)

if area > 100:
    print("THE ROOM IS HUGE!")

elif area < 100:
    print("the room is small")

elif area == 100:
    print("its just right")
    


      
