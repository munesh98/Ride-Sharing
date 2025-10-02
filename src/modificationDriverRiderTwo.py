from src.distanceRiderDriverModification import distanceBetweenRiderDriverModification

class driverRiderDistanceModified(distanceBetweenRiderDriverModification):
    
    def informationRetrieved(self) :
        fileData = distanceBetweenRiderDriverModification()
        fileData.informationRequired()
        fileData.distanceValues()
        fileData.riderDistanceModification()
        self.__riderDistance,self.__driverDistance = fileData.driverDistanceModification()
        return self.__riderDistance,self.__driverDistance
        
    def distanceRiderValueModification(self):
        __finalListValue = []
        i = 0
        for eachRider in self.__driverDistance :      
            for eachDriver in self.__riderDistance :
                __finalListValue.append([self.__riderDistance[i],self.__driverDistance[i]])
                break
            i = i + 1

        return __finalListValue
      

MODIFICATION_DRIVER_INSTANCE = "__main__"       
if __name__ == MODIFICATION_DRIVER_INSTANCE:
    fileDistanceData = driverRiderDistanceModified()
    fileDistanceData.informationRetrieved()
    fileDistanceData.distanceRiderValueModification()

