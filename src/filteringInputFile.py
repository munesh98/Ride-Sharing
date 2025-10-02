from src.readingInputFile import main

class removingNewLineCharacter() :
    
    def checkingTheAvailabilityOfTestData(self,testData):
        if testData != None :
            __dataToBeSent = testData
        else:
            __dataToBeSent = main()
        return __dataToBeSent
       
    def newLineRemovalFunction(self,testData=None):
        self.__inputData = removingNewLineCharacter.checkingTheAvailabilityOfTestData(self,testData)
        NEWLINE_CHARACTER = "\n"
        for eachData in self.__inputData :
            if eachData.endswith(NEWLINE_CHARACTER):
                lenghtOfData = len(eachData)
                dataIndex = self.__inputData.index(eachData)
                eachData = eachData[0:lenghtOfData-1]
                self.__inputData[dataIndex] = eachData
        return self.__inputData
        
        
    def distanceValueSeperation(self):
        self.__rideStartedInformation = []
        for eachValue in self.__inputData :
            if eachValue.startswith("ADD_DRIVER") or eachValue.startswith("ADD_RIDER"):
                firstValue = eachValue.split()[1] 
                secondValue = eachValue.split()[2::]
                self.__inputData[self.__inputData.index(eachValue)] = firstValue+"_"+"_".join(secondValue)
            
            else :
                self.__rideStartedInformation.append(eachValue)
        
        return self.__inputData
        
    def rideInformationRequired(self):
        return self.__rideStartedInformation
    
    def riderDistanceListValue(self):
        self.__riderDictonaryValue = {}
        for eachDataValue in self.__inputData :
            if eachDataValue.startswith("R"):
                dataRequired = eachDataValue.split('_')
                self.__riderDictonaryValue[dataRequired[0]]=dataRequired[1:]
        
        return self.__riderDictonaryValue


FILTERING_INPUT_INSTANCE =  "__main__"
if __name__ == FILTERING_INPUT_INSTANCE :
    fileObject = removingNewLineCharacter()
    fileObject.checkingTheAvailabilityOfTestData()
    fileObject.newLineRemovalFunction()
    fileObject.distanceValueSeperation()
    fileObject.rideInformationRequired()
    fileObject.riderDistanceListValue()