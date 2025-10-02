from rideThatNeedsToBeStoppedInformationProcessing.pointAtWhichRiderWantsToBeDropped import distanceTravelledBetweenRidesPickUpAndDrop


class toCalculateDistanceAndVerifyRide :
    
    RIDE_STOP_STATEMENT = "STOP_RIDE"
    
    @classmethod
    def functionToCalculateDistance(self,riderDriveList,distanceValue) :
        rideIdWithRequiredData = {}
         
        for eachDistanceValue in riderDriveList :
            indexValueOfDataRequired = riderDriveList.index(eachDistanceValue)
            if eachDistanceValue.startswith(self.RIDE_STOP_STATEMENT) :
                indexValueOfDistance = riderDriveList.index(eachDistanceValue)
                rideIdWithRequiredData = distanceTravelledBetweenRidesPickUpAndDrop.functionToCalculateRiderDistance(eachDistanceValue,distanceValue)
                riderDriveList[indexValueOfDataRequired] = "RIDE_STOPPED"+ " " + eachDistanceValue.split()[1] 
        
        return rideIdWithRequiredData,riderDriveList


VERIFY_RIDE_STOPPED_INSTANCE = "__main__"      
if __name__ == VERIFY_RIDE_STOPPED_INSTANCE:
    toCalculateDistanceAndVerifyRide()
