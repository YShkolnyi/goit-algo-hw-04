def get_cats_info(path):
    cats_info = []
    try:
        with open(path) as fh:
            lines = [el.strip() for el in fh.readlines()]
        
        for line in lines:
            line = line.split(',')
            info_dict = {"id": line[0], "name": line[1], "age": line[2]}
            cats_info.append(info_dict)
    
    except FileNotFoundError:
        print("You have some trouble with your file.\nPls fix it before. Thx U! ;)")

    finally:
        return cats_info    
        

cats_info = get_cats_info('cats_info_file.txt')
print(cats_info)