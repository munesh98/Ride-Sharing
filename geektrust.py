from src.billCalculationForEachRideSuccess import riderDriverDataEnteringFinalStage

class displayOfTheResultOfRiderDriverValue(riderDriverDataEnteringFinalStage):
    
    def dataRequiredToDisplayOutput(self):
        outputValueObject = riderDriverDataEnteringFinalStage()
        outputValueObject.valuesRequiredToTheProcess()
        self.__finalOutputListValue = outputValueObject.toCalculateTheBillForTheRide()
    
    def functionTODisplayOutput(self):
        for eachOutputValue in self.__finalOutputListValue :
            print(eachOutputValue)

   
RIDE_FINAL_INSTANCE = "__main__"      
if __name__ == RIDE_FINAL_INSTANCE:
    rideFinalOutputObject = displayOfTheResultOfRiderDriverValue()
    rideFinalOutputObject.dataRequiredToDisplayOutput()
    rideFinalOutputObject.functionTODisplayOutput()



