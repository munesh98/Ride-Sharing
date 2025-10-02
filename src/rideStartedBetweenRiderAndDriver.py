from copy import deepcopy
from src.concatenationOfTheValuesOfRiderDriver import concatenationOfTheOriginalList
from src.driversRidersDistanceInformation import matchingRidersWithDrivers
from rideStartingInformationToBeProcessed.rideStartedwithDriverRequestedByRider import rideStartedBetweenRiderDriver
from rideStartingInformationToBeProcessed.driversMatchedToRequestedRider import combiningTheRiderIDwithDrivers

class riderDriverRideStartedInformation(concatenationOfTheOriginalList):

    RIDE_START_STATEMENT = "START_RIDE"
    DRIVERS_MATCHED_STATEMENT = "DRIVERS_MATCHED"
    NO_DRIVERS_MATCHED_STATEMENT = "NO_DRIVERS_AVAILABLE"
    
    
    def valuesRequiredForConcatenation(self):
        RideInformationObject = concatenationOfTheOriginalList()
        RideInformationObject.valuesRequiredForConcatenation()
        RideInformationObject.rideInformationRequiredForCalculation()
        RideInformationObject.joinTheListValue()
        self.__rideStartInformation = RideInformationObject.joiningTheTwoListValue()
        self.__rawInformationOfDrivers = RideInformationObject.driverRawList()
   
    def startingOfRideFunction(self):
        driverMatchedObject = matchingRidersWithDrivers()
        driverMatchedObject.infoFromPreviousFunction()
        riderValueRequired = driverMatchedObject.groupingDistanceValue()
        rideObject = rideStartedBetweenRiderDriver()
        rideDataToBeTransferred = deepcopy(self.__rideStartInformation) 
        rawDriversList = deepcopy(self.__rawInformationOfDrivers)
        self.__uniqueIdentificationValue = rideObject.functionToProcessRideInformation(rideDataToBeTransferred,(riderValueRequired,rawDriversList))

    def functionToClubDriverWithRidersId(self,dataValue):
        if dataValue.startswith(self.NO_DRIVERS_MATCHED_STATEMENT):
            return []
        else:
            dataRequired = dataValue.split()[1:]
            return " ".join(dataRequired)
    
    def rideIDStartingFunction(self):
        rawMatchedDataObject = matchingRidersWithDrivers()
        rawMatchedDataObject.infoFromPreviousFunction()
        rawRiderDriverValue = rawMatchedDataObject.groupingDistanceValue()
        rawDriverListValue = []
        for eachData in self.__uniqueIdentificationValue :
            if eachData.startswith(self.NO_DRIVERS_MATCHED_STATEMENT) or eachData.startswith(self.DRIVERS_MATCHED_STATEMENT) :
                rawDriverListValue.append(self.functionToClubDriverWithRidersId(eachData))
        
        self.__rawFinalValueRequired = combiningTheRiderIDwithDrivers.ridersRequestedByDriver(self,rawRiderDriverValue,rawDriverListValue)
        return self.__uniqueIdentificationValue,self.__rawFinalValueRequired

RIDE_VALUE_INSTANCE = "__main__"      
if __name__ == RIDE_VALUE_INSTANCE:
    rideStartedObject = riderDriverRideStartedInformation()
    rideStartedObject.valuesRequiredForConcatenation()
    rideStartedObject.startingOfRideFunction()
    rideStartedObject.rideIDStartingFunction()
 
    



