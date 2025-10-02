from copy import deepcopy
from src.riderDriverRideStoppedDataProcessed import riderDriverRideStoppingInformation
from toCalculateBillsForEachRide.billCalculationForEachRide import toCalculateTheRideCompletedBill

class riderDriverDataEnteringFinalStage(riderDriverRideStoppingInformation):
    
    def valuesRequiredToTheProcess(self):
        rideStoppedDataObject = riderDriverRideStoppingInformation()
        rideStoppedDataObject.functionToCreateTheUniqueRiderId()
        rideStoppedDataObject.driverSelectedForSpecifiedRide()
        rideStoppedDataObject.listToStoreRidesThatAreValid()
        self.__riderDriverRideIdListData,self.__rideIdWithTheirLocation = rideStoppedDataObject.distanceBetweenSourceAndDestination()
        
        
    def toCalculateTheBillForTheRide(self) :
        riderDriverInformationProvided = deepcopy(self.__rideIdWithTheirLocation[0])
        riderDriverAvailableData = deepcopy(self.__rideIdWithTheirLocation[1])
        rideIdWithDriverList = deepcopy(self.__riderDriverRideIdListData)
        self.__finalDriverRiderListValue = toCalculateTheRideCompletedBill.functionToCalculateBill(riderDriverInformationProvided,(riderDriverAvailableData,rideIdWithDriverList))
        return self.__finalDriverRiderListValue
   
BILL_CALCULATION_SUCCESS_INSTANCE = "__main__"      
if __name__ == BILL_CALCULATION_SUCCESS_INSTANCE:
    rideFinalObject = riderDriverDataEnteringFinalStage()
    rideFinalObject.valuesRequiredToTheProcess()
    rideFinalObject.toCalculateTheBillForTheRide()



