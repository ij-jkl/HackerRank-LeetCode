""" https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true """

if __name__ == '__main__':
    
    # Create Nested List
    nestedList = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        # Append name and score
        nestedList.append([name, score])
    
    # Sort the list by score
    nestedList.sort(key=lambda x: x[1])
    
    # Extract scores and find unique values
    # I[1] references to the score
    scores = [i[1] for i in nestedList]
    
    #The set makes it unique, no duplicate
    unique_scores = list(set(scores))
    
    # Sort unique scores in ascending order
    unique_scores.sort()
    
    # Ensure there are at least two unique scores for the second lowest
    if len(unique_scores) >= 2:
        # Find the second lowest score
        second_lowest = unique_scores[1]
    else:
        second_lowest = None  # Handle the case where there are fewer than two unique scores
    
    # Find names with the second lowest score
    second_lowest_names = [name for name, score in nestedList if score == second_lowest]
    
    # Print names in alphabetical order
    for name in sorted(second_lowest_names):
        print(name)
