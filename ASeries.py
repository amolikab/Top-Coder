#An arithmetic series consists of a sequence of terms such that each term minus its immediate predecessor gives the same result. For example, the sequence 3,7,11,15 is the terms of the arithmetic series 3+7+11+15; each term minus its predecessor equals 4. (Of course there is no requirement on the first term since it has no predecessor.)
#Given a collection of integers, we want to find the longest arithmetic series that can be formed by choosing a sub-collection (possibly the entire collection). Create a class ASeries that contains a method longest that is given a values and returns the length of the longest arithmetic series that can be formed from values.

#Definition
#Class: ASeries
#Method: longest
#Parameters: tuple (integer)
#Returns: integer
#Method signature: def longest(self, values):




class ASeries:
    
    def IsSeq(self,ar,i):
        n = len(ar)
        
        potential_list = []
        if(n==1):
            if(ar[0]>= i):
                potential_list = [i,ar[0]]
                return potential_list
            elif(ar[0]<i):
                potential_list = [ar[0],i]
                return potential_list
            else:
                return potential_list
        elif(n==2):
            if(ar[0] < i and i < ar[1]):
                
                if(i-ar[0] == ar[1] -i):
                    potential_list = [ar[0],i,ar[1]]
                    return potential_list
                else:
                    return potential_list
                    
            elif(i<=ar[0]):
                
                if(ar[0] - i == ar[1] - ar[0]):
                    potential_list = [i,ar[0],ar[1]]
                    return potential_list
                else:
                    return potential_list
            elif(ar[1]<i):
                
                if(ar[1] - ar[0] == i - ar[1]):
                    potential_list = [ar[0],ar[1],i]
                    return potential_list
                else:
                    return potential_list
            else:
                return potential_list
                
        elif(n>=3):
            
            if(ar[n-1]< i and (ar[n-1] - ar[n-2] == i - ar[n-1]) ):
                potential_list = ar
                potential_list.append(i)
                return potential_list
                
            elif(ar[0] > i and (ar[0] - i == ar[1] - ar[0]) ):
                potential_list = ar
                potential_list.insert(0,i)
                return potential_list
                
            else:
                return potential_list
                
    
    def longest(self,values):
        
        diction = dict()
        arr = []
        arr.append([values[0]])
        
        for i in range(1,len(values)):
            n = len(arr)
            for x in arr:
                list = self.IsSeq(x,values[i])
                
                z =len(list)
                if(z == 0):
                    pass
                else:
                    #valid list
                    length = len(list)
                    diff = list[1] - list[0]
                    if( diction.has_key(diff) ):
                        if(diction[diff] < length):
                            diction[diff] = length
                    else:
                        diction[diff] = length
                    arr.append(list)
                    
            arr.append([values[i]])
        max = 0
        
        for value in diction.values():
            
            if(value> max):
                max = value
        return max
        
        


arr = (-10,-20,-10,-10,-10)
arr1 = [-10,-10,-10,-10]
obj = ASeries()
ans = obj.longest(arr)
print(ans)





