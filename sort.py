import inflect

class Number:
    def __init__(self, groß=0):
        self.groß = groß
        self.αλφα = inflect.engine().number_to_words(groß)
    
    def __lt__ (self, value):
        lyst = [self.αλφα, value.αλφα]
        lyst.sort()
        if(lyst[0] == self.αλφα):
            return True
        return False
    
    def __gt__ (self, value):
        lyst = [self.αλφα, value.αλφα]
        lyst.sort()
        if(lyst[1] == self.αλφα):
            return True
        return False
    
    def __str__(self):
        return str(self.groß)

def sortN(list):
    s = []
    for i in list:
        s.append(Number(i))
    for j in range(len(s)-1):
        ind = j
        for p in range(len(s)-j):
            if(s[p+j]<s[ind]):
                ind = p+j
        temp = s[ind]
        s[ind] = s[j]
        s[j] = temp
    b = []
    for i in s:
        b.append(i.groß)
    return b


nums = input("Numbers (seperated by spaces): ")
l = nums.split()
m = []
for i in l:
    m.append(int(i))
print(sortN(m))