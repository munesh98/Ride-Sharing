from rideStartingInformationToBeProcessed.verificationOfUniquenessOfRideID import rideIdentificationVerification
from rideStartingInformationToBeProcessed.driversMatchedToRequestedRider import combiningTheRiderIDwithDrivers
from rideStartingInformationToBeProcessed.additionOfRideStartedStatement import rideStartedStatementToStartRide
from rideStartingInformationToBeProcessed.toRestrictDriversFromAcceptingRideWhileRideStarted import toHideTheDriverWhoAcceptedTheRide

class rideStartedBetweenRiderDriver:

    
    def functionToProcessRideInformation(self,uniqueRiderIdentification,riderValue):
        self.uniqueRideId = []
        uniqueRideValueIdentification = rideIdentificationVerification()
        riderDriverInformation = combiningTheRiderIDwithDrivers.ridersRequestedByDriver(self,riderValue[0],riderValue[1])
        for eachValue in uniqueRiderIdentification :
            if eachValue.startswith("START_RIDE"):
                indexValue = uniqueRiderIdentification.index(eachValue)
                uniqueRideIdValues = uniqueRideValueIdentification.functionToVerifyUniqueness(eachValue.split()[1],self.uniqueRideId)
                uniqueRiderIdentification = uniqueRideValueIdentification.resultToBeReturned((indexValue,uniqueRiderIdentification),uniqueRideIdValues)
                uniqueRiderIdentification,driverSelectedByRider = combiningTheRiderIDwithDrivers.validationOfDriverSelectedByRider(self,(eachValue.split(),riderDriverInformation,indexValue),uniqueRiderIdentification)
                uniqueRiderIdentification = toHideTheDriverWhoAcceptedTheRide.functionToRestrictDriver((uniqueRiderIdentification[indexValue::],driverSelectedByRider,uniqueRiderIdentification))
                
        return uniqueRiderIdentification

RIDE_STARTED_INSTANCE = "__main__"      
if __name__ == RIDE_STARTED_INSTANCE:
    rideStartedObject = rideStartedBetweenRiderDriver()
    rideStartedObject.functionToProcessRideInformation()