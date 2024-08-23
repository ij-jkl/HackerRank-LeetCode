if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_value = -101
    for i in arr:
        if(max_value < i):
            max_value = i
    
    runnerUp = -101
    
    for i in arr:
        if(i != max_value and runnerUp < i):
            runnerUp = i
        
    print(runnerUp)