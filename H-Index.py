b=[0 for _ in range(1000000)]
n = int(input())
a = list(map(int, input().split()))
# calculating H-Index
def H_index(citations, n):
      
    # sorting in ascending order
    citations.sort()
      
    # iterating over the list
    for i, cited in enumerate(citations):
          
        # finding current result
        result = len(citations) - i
          
        # if result is less than or equal
        # to cited then return result
        if result <= cited:
            return result
           
    return 0
  
  
# calling the function
print(H_index(a, n))