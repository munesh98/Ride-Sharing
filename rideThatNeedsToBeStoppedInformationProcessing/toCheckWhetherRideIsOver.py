from copy import deepcopy

class toCheckWhetherRideIsAlreadyCompleted :
    
    def functionToValidateStopRide(self,dataNeeded,rideCompletedListValue):
        uniqueRiderDriverList = dataNeeded[1]
        indexValueOfStatement = dataNeeded[2]
        dataRequired = dataNeeded[0].split()[1]
        if dataRequired not in rideCompletedListValue :
            rideCompletedListValue.append(dataRequired)
            return uniqueRiderDriverList
        else:
            uniqueRiderDriverList[indexValueOfStatement] = "INVALID_RIDE"
            return uniqueRiderDriverList
            


STOP_RIDE_INSTANCE = "__main__"      
if __name__ == STOP_RIDE_INSTANCE:
    toCheckWhetherRideIsAlreadyCompleted()