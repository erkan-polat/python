def up_and_low(name):
    up=0
    low=0
    for i in range(0,len(name)):
        name_i=name[i]
        check=name_i.isupper()
        if  check:
            up=up+1
        else:
            low=low+1
    print( "No. of Upper case characters:"+str(up))
    print( "No. of Lower case characters:"+str(low))
