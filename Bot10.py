class Bot:
    def __init__(self, id, lowToType, highToType, lowToNum, highToNum):
        self.Id = id
        self.LowToNum = lowToNum
        self.HighToNum = highToNum
        self.Values = []
        self.LowToType = lowToType # 'bot' or 'output'
        self.HighToType = highToType
    def __str__(self):
        if self.Values == []:
            return ''
        s = '('
        s = s + str(self.Id) + '->'
        for v in self.Values:
            s += str(v) + ' '
        s = s.strip() + ')'
        return s
        
        