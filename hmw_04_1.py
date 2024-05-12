def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    salary = int(parts[1])
                    total += salary
                    count += 1
    except FileNotFoundError:
        print("File not found.")
        return None, None
    except Exception as e:
        print(f"Error: {e}")
        return None, None

    if count == 0:
        print("File is empty or does not contain valid data.")
        return None, None

    average = total / count
    return total, average