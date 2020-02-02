finalList = []
class flattenList:
    # def __init__(self):
    #     self.finalList = []
    def flattenList_helper(self, inputList):
        for val in inputList:
            if type(val) == list:
                self.flattenList_helper(val)
            else:
                finalList.append(val)
        return finalList

fList = flattenList()
result = fList.flattenList_helper([1,2,[3,4],[[5,6],[7,8]]])
print(result)