
class toHideTheDriverWhoAcceptedTheRide :

    def toRemoveTheDriveWhoseRideStarted(self,valueSet,driverValueList,driverSelected):
        indexValueOfValueSet = driverValueList.index(valueSet)
        dataRequired = valueSet.split()
        if driverSelected in dataRequired :
            dataRequired.remove(driverSelected)
            dataRequired = " ".join(dataRequired)
        driverValueList[indexValueOfValueSet] = dataRequired
        
        return driverValueList
    
    @classmethod
    def functionToRestrictDriver(self,value):
        driverListAfterRideStarted,driverSelectedByRider,riderDriverListValue = value
        for eachData in driverListAfterRideStarted :
            if eachData.startswith("DRIVERS_MATCHED"):
                riderDriverListValue = self.toRemoveTheDriveWhoseRideStarted(self,eachData,riderDriverListValue,driverSelectedByRider)
                pass
            else:
                continue
        
        return riderDriverListValue


RISTRICTING_DRIVER_INSTANCE = "__main__"      
if __name__ == RISTRICTING_DRIVER_INSTANCE:
    toHideTheDriverWhoAcceptedTheRide()
