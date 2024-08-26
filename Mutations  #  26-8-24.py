""" https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true """

def mutate_string(string, position, character):
    #We convert the string into a list so we can change it
    string = list(string)

    # This step can be more effective just doing  string_list[position] = character (No need of a For and If)
    for i in range(len(string)):
        if(i == position):
            string[i] = character

    #We use the join to convert it into a single String
    string = "".join(string)
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)    