from copy import deepcopy
from  distanceCalculationBetweenDriversRiders.multiplicationOfGivenDistanceValue import valuesToBeMultiplied
from  distanceCalculationBetweenDriversRiders.calculationOfSquareRootFunction import toCalculateSquareRootOfGivenValue
from  distanceCalculationBetweenDriversRiders.distanceOfRidersDriversValue import subtractionOfTheGivenValues


class distanceCalculationRidersDrivers : 

    def dataToCalculateDistance(self,riderDistanceValue,driverDistanceValues) :

        newRiderDistacneValue = deepcopy(riderDistanceValue)
        newDriverDistanceValue = deepcopy(driverDistanceValues)
        for eachDistanceValue in driverDistanceValues:
            resultOfSetOfValues = subtractionOfTheGivenValues.functionToPerformSubtraction(self,newRiderDistacneValue,newDriverDistanceValue)
            outputValueReceived = valuesToBeMultiplied.multiplicationOfValues(resultOfSetOfValues[0],resultOfSetOfValues[1])
            finalcalculatedValue = toCalculateSquareRootOfGivenValue.squareRootCalculation(self,outputValueReceived)
        
        if finalcalculatedValue <= 5 :
            return finalcalculatedValue
            
            

DISTANCE_CALCULATION_FILE_INSTANCE = "__main__"      
if __name__ == DISTANCE_CALCULATION_FILE_INSTANCE:
    distanceCalculationRidersDrivers()