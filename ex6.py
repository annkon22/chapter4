#Implement a solution to the Tower of Hanoi
#using the three stacks to keep track of the disks

def move_tower(height, from_pole, to_pole, with_pole):
    if height >=1:
        move_tower(height - 1, from_pole, with_pole, to_pole, ) #move a tower of height - 1 to an intermediate pole, using the final pole
        move_disk(from_pole, to_pole)                           #move the remaining disk to the final pole
        move_tower(height - 1, with_pole, to_pole, from_pole)   #move the tower of height - 1 from the intermediate pole to the final pole using the original pole

def move_disk(fp, tp):
    print("moving disk from ", fp, "to", tp)

move_tower(3, "A", "B", "C")
