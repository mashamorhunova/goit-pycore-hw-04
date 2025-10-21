def get_cats_info(path):
    try:
        cats_info = []
    
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                cat_id, name, age = line.split(",")
                cats_info.append({"id": cat_id, "name": name, "age": age})
        return cats_info
    except FileNotFoundError:
        print("The file you're trying to access doesn't exist.") 
    except ValueError:
        print("There was an error when reading the file.")