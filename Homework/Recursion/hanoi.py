def hanoi(source, target, spare, n):
    if n == 1:
        print("Move a disk from", source, "to", target)
    else:    
        hanoi (source, spare, target, n-1)
        print("Move a disk from", source, "to", target)
        hanoi(spare,target, source, n-1)