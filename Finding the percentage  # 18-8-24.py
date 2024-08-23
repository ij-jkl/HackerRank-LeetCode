if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # Quantity of Students // n variable
    
    marks = student_marks[query_name]
    
    average = sum(marks) / len(marks)
    
    rounderAverage = (average,2)

    print(f"{average:.2f}")
        
    