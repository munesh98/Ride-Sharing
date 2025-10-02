
class toCheckWhetherRideIDExist :
    
    @staticmethod
    def functionToStoreRideThatHaveStopped(self,dataReceived):   
        driverRiderListValue = dataReceived [2]
        stringDataValue = dataReceived[0].split()[1]
        indexValue = dataReceived[3]
        if stringDataValue in dataReceived[1] :
            return driverRiderListValue
        else:
            driverRiderListValue[indexValue] = "INVALID_RIDE"
            return driverRiderListValue



RIDE_STOP_COLLECTION_INSTANCE = "__main__"      
if __name__ == RIDE_STOP_COLLECTION_INSTANCE:
    toCheckWhetherRideIDExist()