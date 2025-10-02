from src.distanceBetweenRiderDriverCalculatedSuccessfully import driverRiderDistanceCalculation

class riderDriverMatchedListValues(driverRiderDistanceCalculation):

    
    def valuesImported(self):
        valuesObject = driverRiderDistanceCalculation()
        valuesObject.dataRequired()
        self.__ListValue = valuesObject.distanceCalculationFunction()
        return self.__ListValue
    
    def sortFunction(self,distanceList) : 
        distanceList.sort(key= lambda x: x[1])
        return distanceList
        
    
    def valuesToBeSorted(self):
        for eachValues in self.__ListValue:
            valueRequired = self.sortFunction(eachValues)
            
        return self.__ListValue
        
    
    def stringDataValue(self):
        self.__DriverMatchedList = []
        for eachData in self.__ListValue :
            stringDataRequired = []
            for eachDistanceValue in eachData :
                stringDataRequired.append(eachDistanceValue[0])
            self.__DriverMatchedList.append(stringDataRequired)    
    
        return self.__DriverMatchedList
    

MATCHED_LIST_INSTANCE = "__main__"      
if __name__ == MATCHED_LIST_INSTANCE:
    listDistance= riderDriverMatchedListValues()
    listDistance.valuesImported()
    listDistance.valuesToBeSorted()
    listDistance.stringDataValue()
    



