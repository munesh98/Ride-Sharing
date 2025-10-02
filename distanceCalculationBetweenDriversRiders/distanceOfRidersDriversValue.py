
class subtractionOfTheGivenValues :
    @staticmethod
    def functionToPerformSubtraction(self,driverDistanceValues,riderDistanceValue):
        resultOfFirstSetOfValues = driverDistanceValues[0] - riderDistanceValue[0]
        resultOfSecondSetOfValues = driverDistanceValues[1] - riderDistanceValue[1]
        
        return resultOfFirstSetOfValues,resultOfSecondSetOfValues

SUBTRACTION_FILE_INSTANCE = "__main__"      
if __name__ == SUBTRACTION_FILE_INSTANCE:
    fileDistance = subtractionOfTheGivenValues()