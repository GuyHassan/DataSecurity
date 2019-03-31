
class Depth():
    def __init__(self):
        self.RadiusList = []
    #a number of radiuses will be due to the depth
    #that will be choosen
    def RunNumberOfRadiuses(self , TimeToLive):
        if(TimeToLive == 0):
            return 0
        self.RunNumberOfRadiuses(self,TimeToLive -1)
        #####


        #####

