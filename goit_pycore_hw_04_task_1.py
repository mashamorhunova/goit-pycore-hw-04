
def total_salary(path):
    try:
        salaries = [] 

        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip() 
                name, salary = line.split(",")
                print(name, salary) 
                salaries.append(float(salary))

        total = sum(salaries)
        average = total / len(salaries)
        return total, average 

    except FileNotFoundError:
        print("The file you're trying to access doesn't exist.") 
    except ValueError:
        print("There was an error when reading the file.")

#Example usage
total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")