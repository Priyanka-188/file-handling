content = True    # set it true so that intitially the loop goes in file.
i=1     # this act as a counter

with open("log.txt") as f :
    while content:          
        content = f.readline()   # using this loop read only one line at a time

        if 'python' in content.lower():  # checkinh if 'python' is present uin the read line .
            # If 'python' is present .. print the line as well as the line number.
            print(content,f"Yes python is present on {i} th line of file\n" )   
        i+=1   # increment the line number after every iteration

