if __name__ == '__main__':
    n = int(input().strip())  
    integer_tuple = tuple(map(int, input().split()))  
    print(hash(integer_tuple))  
