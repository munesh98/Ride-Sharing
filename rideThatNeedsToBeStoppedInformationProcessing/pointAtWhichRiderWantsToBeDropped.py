
from  distanceCalculationBetweenDriversRiders.multiplicationOfGivenDistanceValue import valuesToBeMultiplied
from  distanceCalculationBetweenDriversRiders.calculationOfSquareRootFunction import toCalculateSquareRootOfGivenValue
from  distanceCalculationBetweenDriversRiders.distanceOfRidersDriversValue import subtractionOfTheGivenValues



class distanceTravelledBetweenRidesPickUpAndDrop :
    
    def functionToCalculateDistanceBetweenTwoPoints(self,sourceValue,destinationValue):
        finalSubtractionValue = subtractionOfTheGivenValues.functionToPerformSubtraction(self,sourceValue,destinationValue)
        finalValueReceived = valuesToBeMultiplied.multiplicationOfValues(finalSubtractionValue[0],finalSubtractionValue[1])
        finalTravelledDistance = toCalculateSquareRootOfGivenValue.squareRootCalculation(self,finalValueReceived)
        return finalTravelledDistance
    
    @classmethod
    def functionToCalculateRiderDistance(self,statementInformation,distanceValue):
        rideIdWithDriverId,riderPickUpCoordinates,*notRequired = distanceValue
        rideStoppedData = statementInformation.split()
        destinationDistanceValue = [int(rideStoppedData[2]),int(rideStoppedData[3])]
        pickUpCoordinate = [int(riderPickUpCoordinates[rideIdWithDriverId[rideStoppedData[1]][1]][0]),int(riderPickUpCoordinates[rideIdWithDriverId[rideStoppedData[1]][1]][1])]
        distanceTravelled = self.functionToCalculateDistanceBetweenTwoPoints(self,pickUpCoordinate,destinationDistanceValue)
        rideIdWithDriverId[rideStoppedData[1]].append(distanceTravelled)
        rideIdWithDriverId[rideStoppedData[1]].append(rideStoppedData[-1])
        
        return rideIdWithDriverId



