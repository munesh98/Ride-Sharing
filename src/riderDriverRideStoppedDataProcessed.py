from copy import deepcopy
from src.rideStartedBetweenRiderAndDriver import riderDriverRideStartedInformation
from rideStartingInformationToBeProcessed.rideStartedwithDriverRequestedByRider import rideStartedBetweenRiderDriver
from rideStartingInformationToBeProcessed.driversMatchedToRequestedRider import combiningTheRiderIDwithDrivers
from src.filteringInputFile import removingNewLineCharacter
from rideThatNeedsToBeStoppedInformationProcessing.rideStoppedWithDriverAndRiderValue import rideOnceStartedNeedsToStop
from rideThatNeedsToBeStoppedInformationProcessing.distanceCalculationAndRideNotCompletedVerification import toCalculateDistanceAndVerifyRide


class riderDriverRideStoppingInformation(riderDriverRideStartedInformation):
    
    RIDE_STARTED_STATEMENT = "RIDE_STARTED"
    START_RIDE_STATEMENT = "START_RIDE"
    STOP_RIDE_STATEMENT = "STOP_RIDE"
    
    def functionToCreateTheUniqueRiderId(self):
        dataRequired = riderDriverRideStartedInformation()
        dataRequired.valuesRequiredForConcatenation()
        dataRequired.startingOfRideFunction()
        self.__uniqueRiderDriverList,self.__uniqueRiderDictionary = dataRequired.rideIDStartingFunction()


    def driverSelectedForSpecifiedRide(self):
        self.__driverValueWithRideId = {} #rideId with respective Driver
        self.__rideIdWithTheirLocation = {}
        self.__uniqueRideIdentificationValue =[]
        for eachValue in self.__uniqueRiderDriverList :
            if eachValue.startswith(self.START_RIDE_STATEMENT):
                dataValueRequired = eachValue.split()
                stringRideValue = self.__uniqueRiderDictionary[dataValueRequired[-1]].split()
                self.__driverValueWithRideId[dataValueRequired[1]] = [stringRideValue[int(dataValueRequired[2])-1],dataValueRequired[-1]]
                indexValueOfUniqueList = self.__uniqueRiderDriverList.index(eachValue)
                self.__uniqueRiderDriverList[indexValueOfUniqueList] = self.RIDE_STARTED_STATEMENT +" "+dataValueRequired[1]
                self.__uniqueRideIdentificationValue.append(dataValueRequired[1])
                self.__rideIdWithTheirLocation[dataValueRequired[1]]=indexValueOfUniqueList
        
        return self.__driverValueWithRideId
    
    def listToStoreRidesThatAreValid(self):
        rideStoppedValue = rideOnceStartedNeedsToStop()
        riderDistanceValueObject = removingNewLineCharacter()
        riderDistanceValueObject.newLineRemovalFunction()
        riderDistanceValueObject.distanceValueSeperation()
        self.__riderDistanceCordinates = riderDistanceValueObject.riderDistanceListValue()
        dataThatContainsDriverListValue = deepcopy(self.__uniqueRideIdentificationValue)
        uniqueRideIdValue = deepcopy(self.__driverValueWithRideId)
        riderDistanceValue = deepcopy(self.__riderDistanceCordinates)
        uniqueRiderDriverList = deepcopy(self.__uniqueRiderDriverList)
        self.__dataThatNeedsToBeSent,self.__rideAlreadyCompleted = rideStoppedValue.mainFunctionToProcessInformation((dataThatContainsDriverListValue,uniqueRideIdValue,riderDistanceValue,uniqueRiderDriverList))

        return self.__dataThatNeedsToBeSent
        
    def distanceBetweenSourceAndDestination(self):
        distanceCalculationDataList = deepcopy(self.__dataThatNeedsToBeSent)
        rideIdWithDriver = deepcopy(self.__driverValueWithRideId)
        driverPickUpCoordinates = deepcopy(self.__riderDistanceCordinates)
        rideStopVerificationData = deepcopy(self.__rideIdWithTheirLocation)
        self.__finalDriverRiderValueList,self.__dataThatNeedsToBeSent = toCalculateDistanceAndVerifyRide.functionToCalculateDistance(distanceCalculationDataList,(rideIdWithDriver,driverPickUpCoordinates,rideStopVerificationData))
        
        return self.__finalDriverRiderValueList,(self.__dataThatNeedsToBeSent,self.__rideIdWithTheirLocation)
   
RIDE_STOPPED_VALUE_INSTANCE = "__main__"      
if __name__ == RIDE_STOPPED_VALUE_INSTANCE:
    rideStoppedObject = riderDriverRideStoppingInformation()
    rideStoppedObject.functionToCreateTheUniqueRiderId()
    rideStoppedObject.driverSelectedForSpecifiedRide()
    rideStoppedObject.listToStoreRidesThatAreValid()
    rideStoppedObject.distanceBetweenSourceAndDestination()



