from src.driversRidersDistanceInformation import matchingRidersWithDrivers


class distanceBetweenRiderDriverValue(matchingRidersWithDrivers) :

    def informationRequired(self):
        matchData = matchingRidersWithDrivers()
        matchData.infoFromPreviousFunction()
        self.newDistanceList = matchData.groupingDistanceValue()
        
    def distanceValues(self) :
        self.driversData = []
        self.ridersInfo = []
        for eachValue in self.newDistanceList :
            key,value = eachValue
            temporaryList = [] 
            [temporaryList.append(eachData) for eachData in value if eachData.startswith("D")]
            [self.ridersInfo.append(eachData) for eachData in value if "R" in eachData and key in eachData]
            self.driversData.append(temporaryList)

class distanceBetweenRiderDriverModification(distanceBetweenRiderDriverValue) :

    
    def riderDistanceModification(self):
        self.__riderDistance = []
        for eachValue in self.ridersInfo :
            riderData = eachValue.split("_")
            riderId = riderData[0]
            riderDistanceInfo = [int(riderData[1]),int(riderData[2])]
            self.__riderDistance.append(riderDistanceInfo)
            
        
        
    def driverDistanceModification(self):
        self.__driverDistance = []
        for eachValue in self.driversData :  
            distanceValue = []
            for eachData in eachValue :
                driverData = eachData.split("_")
                driverId = driverData[0]
                driverDistanceInfo = [int(driverData[1]),int(driverData[2])]
                distanceValue.append((driverId,driverDistanceInfo))
            self.__driverDistance.append(distanceValue)

        return self.__riderDistance,self.__driverDistance
        
    
    
DRIVER_RIDER_MODIFICATION = "__main__"       
if __name__ == DRIVER_RIDER_MODIFICATION:
    fileDistanceObject = distanceBetweenRiderDriverModification()
    fileDistanceObject.informationRequired()
    fileDistanceObject.distanceValues()
    fileDistanceObject.riderDistanceModification()
    fileDistanceObject.driverDistanceModification()

