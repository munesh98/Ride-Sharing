import math

class toCalculateSquareRootOfGivenValue :

    @staticmethod
    def squareRootCalculation(self,inputValueProvided):
            valueForSquareRoot = math.sqrt(inputValueProvided)
            roundedToTwoDigits = round(valueForSquareRoot,2)
            return roundedToTwoDigits
            
            


SQUARE_ROOT_FILE_INSTANCE = "__main__"      
if __name__ == SQUARE_ROOT_FILE_INSTANCE:
    toCalculateSquareRootOfGivenValue()