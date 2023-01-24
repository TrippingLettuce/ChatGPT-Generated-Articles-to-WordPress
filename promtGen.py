
def pop():
    try:
        with open('loc.txt', 'r') as fr:
            # reading line by line
            first_line = fr.readline()
            lines = fr.readlines()
            # opening in writing mode
            with open('loc.txt', 'w') as fw:
                for line in lines:
                    fw.write(line)
        return first_line
        
    except:
        print("error")

