def get_cats_info(path):
    list_cats = []
    
    try:
        with open(path, encoding='utf-8') as file:
            cats = [el.strip() for el in file.readlines()]

            for cat in cats:
                id, name, age = cat.split(',')
                list_cats.append({"id": id, "name": name, "age": age})
                
        return list_cats

    except FileNotFoundError:
        print (f'File with {path} not found')
        return []
    
    except ValueError:
        print('Not accurate data')
        return []

cats_info = get_cats_info("./files/cats_file.txt")
print(cats_info)
