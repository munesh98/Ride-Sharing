
class combiningTheRiderIDwithDrivers :
    
    @staticmethod
    def ridersRequestedByDriver(self,riderValue,uniqueIdentificationOfRiders) :
        self.driverMatchedlists = {}
        startIndex = 0
        for eachValue in riderValue :
            self.driverMatchedlists[eachValue[0]] = uniqueIdentificationOfRiders[startIndex]
            startIndex = startIndex + 1

        return self.driverMatchedlists
    
    @staticmethod
    def validationOfDriverSelectedByRider(self,rideStartedInformation,validationOfDriver):
        driverSelected,riderIdentificationDictionary,indexValue = rideStartedInformation
        indexValueOfDriver = int(driverSelected[2])-1
        if int(driverSelected[2]) > len(riderIdentificationDictionary[driverSelected[-1]]) or riderIdentificationDictionary[driverSelected[-1]] == [] :
            validationOfDriver[indexValue] = "INVALID_RIDE"
            return validationOfDriver,"None"
        else :
            dataToBeReturned = riderIdentificationDictionary[driverSelected[-1]][indexValueOfDriver]
            return validationOfDriver,dataToBeReturned





RIDE_COMBINING_INSTANCE = "__main__"      
if __name__ == RIDE_COMBINING_INSTANCE:
    rideCombiningObject = combiningTheRiderIDwithDrivers()
