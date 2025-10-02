
class toCheckInvalidBillStatement :
    
    BILL_STATEMENT = "BILL"
    CHARGE_FOR_EACH_DISTANCE_TRAVELLED = 6.50
    CHARGE_FOR_EVERY_MINUTE_RIDE = 2
    SERVICE_TAX_FOR_EACH_RIDE = 20
    CENT_PERCENT = 100
    BASE_FARE_FOR_EACH_RIDE = 50
    NEGATIVE_INDEX = -1
    EMPTY_STRING_VALUE = " "
    FIRST_INDEX = 1
    INVALID_STATEMENT = "INVALID_RIDE"

    
    def functionToPerformCalculation(self,riderIdWithRequiredData,dataRequired):
        distanceTravelled = riderIdWithRequiredData[dataRequired][self.CHARGE_FOR_EVERY_MINUTE_RIDE]
        timeTravelledInMinutes  = riderIdWithRequiredData[dataRequired][self.NEGATIVE_INDEX]
        amount = self.BASE_FARE_FOR_EACH_RIDE + (distanceTravelled * self.CHARGE_FOR_EACH_DISTANCE_TRAVELLED) + int(timeTravelledInMinutes) * self.CHARGE_FOR_EVERY_MINUTE_RIDE
        finalAmountValue = round(amount+round(amount * self.SERVICE_TAX_FOR_EACH_RIDE/self.CENT_PERCENT,self.CHARGE_FOR_EVERY_MINUTE_RIDE),self.CHARGE_FOR_EVERY_MINUTE_RIDE)
        return '%.2f'%finalAmountValue
    
    
    @classmethod
    def toLocateAndFindTheInvalidBill(self,eachDataProvided,listValueOfRider,rideIdWithLocationCordinates):
        indexValueOfBill = listValueOfRider.index(eachDataProvided)
        try :
            if eachDataProvided.startswith(self.BILL_STATEMENT):
                dataRequired = eachDataProvided.split()[self.FIRST_INDEX]
                finalAmount = self.functionToPerformCalculation(self,rideIdWithLocationCordinates,dataRequired)
                listValueOfRider[indexValueOfBill] = self.BILL_STATEMENT+self.EMPTY_STRING_VALUE+dataRequired+self.EMPTY_STRING_VALUE+rideIdWithLocationCordinates[dataRequired][0]+self.EMPTY_STRING_VALUE+str(finalAmount)
        except KeyError :
            listValueOfRider[indexValueOfBill] = self.INVALID_STATEMENT
        return listValueOfRider

BILL_VALIDATION_INSTANCE = "__main__"      
if __name__ == BILL_VALIDATION_INSTANCE:
    toCheckInvalidBillStatement()
