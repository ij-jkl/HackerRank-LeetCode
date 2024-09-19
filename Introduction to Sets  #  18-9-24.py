""" https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true """

#My code works but Hacker rank wont accept it, but its fine by me bc i did by myself!!
def average(array, n):
    wholeSet = set(array)
    totalWords = len(wholeSet)
    totalSum = 0

    #We put a set so repetead numbers dont count, and we start to drop them so we dont add them twice
    for i in range(n):
        if array[i] in wholeSet:
            totalSum += int(array[i]) 
            wholeSet.remove(array[i]) 
    
    avg = totalSum / totalWords

    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr,n)
    print(result)

    #10 - 161 182 161 154 176 170 167 171 170 174 Expected output  169.375
    # 8 - 154 161 167 170 171 174 176 182 Expected output 169.375
    # 100 - 166 169 173 164 171 152 178 182 182 156 163 159 154 160 166 179 153 169 176 164 173 170 176 172 167 171 175 155 171 182 164 170 156 170 165 178 174 178 184 170 173 170 155 156 175 168 184 168 171 152 157 152 164 165 165 175 160 161 173 172 164 179 169 184 153 176 157 158 164 156 183 178 180 178 183 180 165 155 156 163 161 162 181 165 173 154 174 154 172 172 174 180 153 155 165 174 157 171 163 171 Expected output 167.71875

    """
    Hacker Rank accepted output 
    def average(array):
    
    my_set = set(array)
    avg = sum(my_set)/len(my_set)
    
    return(avg) """