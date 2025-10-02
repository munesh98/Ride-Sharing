
class rideIdentificationVerification :

    INVALID_RIDE_STATEMENT = "INVALID_RIDE"
    
    def functionToVerifyUniqueness(self,rideID,riderIdentificationList):
        if rideID not in riderIdentificationList :
            riderIdentificationList.append(rideID)
            return riderIdentificationList
        else:
            return self.INVALID_RIDE_STATEMENT
        
  
    def resultToBeReturned(self,rideInformationList,resultValue):
        indexValue = rideInformationList[0]
        riderListValue = rideInformationList[1]
        if resultValue == self.INVALID_RIDE_STATEMENT :
            riderListValue[indexValue] = resultValue
            return riderListValue
        else :
            return riderListValue



RIDE_VERIFICATION_INSTANCE = "__main__"      
if __name__ == RIDE_VERIFICATION_INSTANCE:
    rideVerificationObject = rideIdentificationVerification()
    rideVerificationObject.functionToVerifyUniqueness()