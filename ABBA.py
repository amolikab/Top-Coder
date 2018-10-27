#One day, Jamie noticed that many English words only use the letters A and B. Examples of such words include "AB" (short for abdominal), "BAA" (the noise a sheep makes), "AA" (a type of lava), and "ABBA" (a Swedish pop sensation).
#Inspired by this observation, Jamie created a simple game. You are given two s: initial and target. The goal of the game is to find a sequence of valid moves that will change initial into target. There are two types of valid moves:

#Add the letter A to the end of the string.
#Reverse the string and then add the letter B to the end of the string.
#Return "Possible" (quotes for clarity) if there is a sequence of valid moves that will change initial into target. Otherwise, return "Impossible".





class ABBA:
    
    def move1(self,x):
        str = x[:]
        str.append('A')
        return str
    
    def move2(self,x):
        str = x[:]
        str = str[::-1]
        str.append('B')
        return str
    
    def canObtain(self,initial1,final1):
        
        initial = list(initial1)
        final = list(final1)
        arr = []
        arr.append(initial)
        n = len(final) - len(initial)
        
        for i in range(0,n):
            while(len(arr) != 0):
                x = arr[0]
                a = self.move1(x)
                aa = a[::-1]
                a1 = ''.join(a)
                aa1 = ''.join(aa)
                if(a1 == final1):
                    return 'Possible'
                elif((final1.find(a1)>=0) or (final1.find(aa1)>=0)):
                    arr.append(a)
                    
                b = self.move2(x)
                bb = b[::-1]
                b1 = ''.join(b)
                bb1 = ''.join(bb)
                if(b1 == final1):
                    return 'Possible'
                elif((final1.find(b1)>=0) or (final1.find(bb1)>=0)):
                    arr.append(b)
                del arr[0]
            
        return 'Impossible'
            
            
      
    
initial = 'BBBBABABBBBBBA'
final = 'BBBBABABBABBBBBBABABBBBBBBBABAABBBAA'
obj = ABBA()
ans = obj.canObtain(initial,final)
print(ans)







