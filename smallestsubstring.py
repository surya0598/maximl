from collections import defaultdict 
  
MAX_CHARS = 256
  

  
def findSubString(str): 
    n = len(str) 
      
    
    dist_count = len(set([x for x in str])) 
  
   
  
    count, start, start_index, min_len = 0, 0, -1, 9999999999
    curr_count = defaultdict(lambda: 0) 
    for j in range(n): 
        curr_count[str[j]] += 1
        
  
        if curr_count[str[j]] == 1: 
            count += 1
  
        
        if count == dist_count: 
            while curr_count[str[start]] > 1: 
                if curr_count[str[start]] > 1: 
                    curr_count[str[start]] -= 1
                start += 1
  
           
            len_window = j - start + 1
            if min_len > len_window: 
                min_len = len_window 
                start_index = start 
  
   
    return len(str[start_index: start_index + min_len])
      

if __name__=='__main__': 
    print(format(findSubString(str(input())))) 
  
