if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    count = 0
    sc = student_marks[query_name]
    aver= sum(sc)/3 
print(f"{aver:.2f}")