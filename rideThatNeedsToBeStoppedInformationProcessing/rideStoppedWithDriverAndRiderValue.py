from copy import deepcopy
from rideThatNeedsToBeStoppedInformationProcessing.dataRelatedToStopRideStatement import toCheckWhetherRideIDExist
from rideThatNeedsToBeStoppedInformationProcessing.toCheckWhetherRideIsOver import toCheckWhetherRideIsAlreadyCompleted


class rideOnceStartedNeedsToStop :
    
    def mainFunctionToProcessInformation(self,value):
        self.riderDriverInformationList = value[-1]
        rideAlreadyCompletedList = []
        i = 0
        for eachValue in self.riderDriverInformationList :
            if eachValue.startswith("STOP_RIDE"):
                self.riderDriverInformationList = toCheckWhetherRideIDExist.functionToStoreRideThatHaveStopped(self,(eachValue,value[0],value[-1],i))
                self.riderDriverInformationList = toCheckWhetherRideIsAlreadyCompleted.functionToValidateStopRide(self,(eachValue,value[-1],i),rideAlreadyCompletedList)
            i = i + 1    
        
        return self.riderDriverInformationList,rideAlreadyCompletedList



RIDE_STOP_INSTANCE = "__main__"      
if __name__ == RIDE_STOP_INSTANCE:
    rideOnceStartedNeedsToStop()

