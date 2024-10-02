def total_salary(path):
    total = 0
    average = 0

    try:
        with open(path) as fh:
            lines = [el.strip() for el in fh.readlines()]
        
        for line in lines:
            line = line.split(',')
            total += int(line[1])

        average=int(total/len(lines))
    
    except FileNotFoundError:
        print("You have some trouble with your file.\nPls fix it before. Thx U! ;)")

    finally:
        return total, average
        

total, average = total_salary('salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

