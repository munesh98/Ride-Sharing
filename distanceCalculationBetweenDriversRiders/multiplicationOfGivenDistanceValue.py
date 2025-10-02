class valuesToBeMultiplied :

    POWER_REQUIRED_FOR_CALCULATION = 2
    
    @classmethod
    def multiplicationOfValues(self,firstSetOfValue,secondSetOfValues):
        return firstSetOfValue**self.POWER_REQUIRED_FOR_CALCULATION + secondSetOfValues**self.POWER_REQUIRED_FOR_CALCULATION
        
        
        

MULTIPLICATION_FILE_INSTANCE = "__main__"      
if __name__ == MULTIPLICATION_FILE_INSTANCE:
    valuesToBeMultiplied()