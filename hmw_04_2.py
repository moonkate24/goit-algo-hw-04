def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_info = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": int(parts[2])
                    }
                    cats_info.append(cat_info)
                    
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
    return cats_info