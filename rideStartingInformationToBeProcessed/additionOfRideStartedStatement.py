
class rideStartedStatementToStartRide :
    
    INVALID_RIDE_STATEMENT = "INVALID_RIDE"
    RIDE_STARTED_STATEMENT = "RIDE_STARTED"
    
    @classmethod
    def finilizingRideStartedStatement(self,riderDriverValueList,index):
        indexValueOfRideStatement = index[0]
        riderIdentificationValue = index[1]
        
        if riderDriverValueList[indexValueOfRideStatement] != self.INVALID_RIDE_STATEMENT :
            riderDriverValueList[indexValueOfRideStatement] = self.RIDE_STARTED_STATEMENT +" "+riderIdentificationValue
            return riderDriverValueList
        else :
            return riderDriverValueList




RIDE_STATEMENT_RIDE_ID_INSTANCE = "__main__"      
if __name__ == RIDE_STATEMENT_RIDE_ID_INSTANCE:
    rideStartedStatementToStartRide()
