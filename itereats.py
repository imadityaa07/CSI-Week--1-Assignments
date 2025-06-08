from itertools import combinations
N = int(input().strip())  
letters = input().strip().split()  
K = int(input().strip())
if K > N or K <= 0:
    print("Invalid selection size. K must be between 1 and N.")
else:
    indices = list(range(N)) 
    combinations_list = list(combinations(indices, K))
    count = 0
    for combo in combinations_list:
        if any(letters[i] == 'a' for i in combo): 
            count += 1
    probability = count / len(combinations_list)
    if probability == 0:
        print("No valid selections contain 'a'. Probability is 0.0000")
    else:
        print(f"{probability:.4f}")
