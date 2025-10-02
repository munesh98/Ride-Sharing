from src.filteringInputFile import removingNewLineCharacter


class matchingRidersWithDrivers(removingNewLineCharacter) :
    
    def infoFromPreviousFunction(self):
        objectValue = removingNewLineCharacter()
        objectValue.newLineRemovalFunction()
        self.__inputData = objectValue.distanceValueSeperation()
    
    
    def groupingDistanceValue(self):
        newDistanceList = []
        for eachValue in self.__inputData: 
            if eachValue.startswith("MATCH"):
                newDistanceList.append([eachValue.split()[1],self.__inputData[0:self.__inputData.index(eachValue)]])
                self.__inputData[self.__inputData.index(eachValue)] =""
        
        return newDistanceList    

DRIVER_RIDER_DISTANCE_INSTANCE = "__main__"
if __name__ == DRIVER_RIDER_DISTANCE_INSTANCE:
    fileObject = matchingRidersWithDrivers()
    fileObject.infoFromPreviousFunction()
    fileObject.groupingDistanceValue()
