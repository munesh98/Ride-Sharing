from toCalculateBillsForEachRide.validationOfBillStatement import toCheckInvalidBillStatement


class toCalculateTheRideCompletedBill :
    FIRST_INDEX = 1

    @classmethod
    def functionToCalculateBill(self,driverRiderListValue,data):
        riderIdWithRequiredData = data[self.FIRST_INDEX]
        for eachValue in driverRiderListValue :
            driverRiderListValue = toCheckInvalidBillStatement.toLocateAndFindTheInvalidBill(eachValue,driverRiderListValue,riderIdWithRequiredData)

        return driverRiderListValue

BILL_FINAL_INSTANCE = "__main__"      
if __name__ == BILL_FINAL_INSTANCE:
    toCalculateTheRideCompletedBill()

