from src.valuesListAfterCalculationOfDistance import riderDriverMatchedListValues
from src.filteringInputFile import removingNewLineCharacter

class concatenationOfTheOriginalList(riderDriverMatchedListValues):

    MATCH_STATEMENT = "MATCH"
    DRIVER_STATEMENT = "DRIVERS_MATCHED"
    DRIVER_NOT_AVAILABLE = "NO_DRIVERS_AVAILABLE"
    __SORTED_DRIVER_VALUE = []
    
    def valuesRequiredForConcatenation(self):
        valuesConcationationObject = riderDriverMatchedListValues()
        valuesConcationationObject.valuesImported()
        valuesConcationationObject.valuesToBeSorted()
        self.__concatinationValue = valuesConcationationObject.stringDataValue()
        
    def rideInformationRequiredForCalculation(self):
        rideValueObject = removingNewLineCharacter()
        rideValueObject.newLineRemovalFunction()
        rideValueObject.distanceValueSeperation()
        self.__rideStartingInformation = rideValueObject.rideInformationRequired()
        
    
    def functionToCheckDriverAvailability(self,driverInformation):
        if driverInformation:
            driverValue = self.DRIVER_STATEMENT +" "+ ' '.join([eachDriverValue for eachDriverValue in driverInformation])    
        else :
            driverValue = self.DRIVER_NOT_AVAILABLE
        
        self.__SORTED_DRIVER_VALUE.append(driverValue.split()[1:])
        return driverValue
    
    def joinTheListValue(self):
        self.__stringConcatenationValue = []
        for eachInformation in self.__concatinationValue :
            driverConcatenation = self.functionToCheckDriverAvailability(eachInformation)
            self.__stringConcatenationValue.append(driverConcatenation)
            

    
    def joiningTheTwoListValue(self):    
        for eachData in self.__rideStartingInformation :
            if eachData.startswith(self.MATCH_STATEMENT) :
                indexValue = self.__rideStartingInformation.index(eachData)
                self.__rideStartingInformation[indexValue] = self.__stringConcatenationValue[0]
                self.__stringConcatenationValue.remove(self.__stringConcatenationValue[0])
                
        return self.__rideStartingInformation


    def driverRawList(self):
        return self.__SORTED_DRIVER_VALUE

MATCHED_LIST_INSTANCE = "__main__"      
if __name__ == MATCHED_LIST_INSTANCE:
    listConcationation = concatenationOfTheOriginalList()
    listConcationation.valuesRequiredForConcatenation()
    listConcationation.rideInformationRequiredForCalculation()
    listConcationation.joinTheListValue()
    listConcationation.joiningTheTwoListValue()
    



