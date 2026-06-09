class parentheses:
    def removeStartandEndParentheses(self, s):
        string=""
        counter=0

        for i in s:
            if(i == '('):
                if counter>0:
                    string+=i

                counter +=1
            elif (i==')'):
                counter -=1
                if counter>0:
                    string+=i
        return string
s = "(()())(())"  
sol = parentheses() 

# Get result
print(sol.removeOuterParentheses(s)) 