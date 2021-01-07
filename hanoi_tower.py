def move_hanoi(n, source, target, spare):
    # role of source, target and spare may change for different case

    # move the only disk from source to target
    if n == 1:
        print("move ", n, "from ", source, "to ", target)
        return
    # move the top n-1 disks from source to spare by target
    move_hanoi(n-1, source, spare, target)
    # move last disk from source to target
    print("move ", n, "from ", source, "to ", target)
    # move top n-1 disks from spare to target by source
    move_hanoi(n-1, spare, target, source)

    return

move_hanoi(4, 'A', 'C', 'B')