import math
from copy import deepcopy
from src.modificationDriverRiderTwo import driverRiderDistanceModified
from distanceCalculationBetweenDriversRiders.distanceToBeCalculatedBetweenRiderDriver import distanceCalculationRidersDrivers


class driverRiderDistanceCalculation(driverRiderDistanceModified):

    
    def dataRequired(self):
        dataObject = driverRiderDistanceModified()
        dataObject.informationRetrieved()
        self.__distanceValue = dataObject.distanceRiderValueModification()
        return self.__distanceValue
        
    
    def functionToCheckTheMaximumDistanceValue(self,dataObtained) :
        newListAfterLimitingDistance = []
        for eachValue in dataObtained :
            key,value = eachValue 
            if value != None :
                newListAfterLimitingDistance.append(eachValue)
        
        return newListAfterLimitingDistance


    def distanceCalculationFunction(self):
        finalDistanceValue = []
        calculationObject = distanceCalculationRidersDrivers()
        newDistanceValue = deepcopy(self.__distanceValue)
        for eachInformation in newDistanceValue :
            self.riderDistanceValue,driverDistanceInformation = eachInformation
            distanceFinalList = []
            for eachDistanceInformation in driverDistanceInformation :
                driverIdentification,driverDistance = eachDistanceInformation
                outputDataRequired = calculationObject.dataToCalculateDistance(self.riderDistanceValue,driverDistance)
                distanceFinalList.append((driverIdentification,outputDataRequired))
            finalDistanceValue.append(self.functionToCheckTheMaximumDistanceValue(distanceFinalList))
            
        self.__distanceValue= deepcopy(finalDistanceValue)
        
        return self.__distanceValue
        
        
        

FILE_NAME_INSTANCE = "__main__"      
if __name__ == FILE_NAME_INSTANCE:
    fileDistance = driverRiderDistanceCalculation()
    fileDistance.dataRequired()
    fileDistance.distanceCalculationFunction()



