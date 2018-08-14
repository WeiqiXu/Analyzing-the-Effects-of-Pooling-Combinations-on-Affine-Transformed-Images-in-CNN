## read log file of training and test process
## created by Caffe
class ReadLogFile(object):
    def __init__(self,_LogFilePath):
        """
        get log file path from LogFilePath
        """
        self.LogFilePath = _LogFilePath
        
    def read_trainLog(self,LogName):
        """
        get iterations and training loss from 
        training log file named LogName
        """
        LogPath = self.LogFilePath+LogName
        
        # load all training data
        with open(LogPath) as f:
            data = f.readlines()
            data = data[1:] # remove the first row (title) 
            data_len = len(data)
            
        Iters = []
        TrainLoss = []

        for row in range(data_len):
            data_row = data[row].split(' ') # splitted by ' '
            while '' in data_row: # remove 'None'
                data_row.remove('')
            Iters.append(int(data_row[0]))
            TrainLoss.append(float(data_row[2]))           
        return Iters, TrainLoss    
    
    def read_testLog(self,LogName):
        """
        get iterations, test accuracy and test loss 
        from test log file named LogName
        """
        LogPath = self.LogFilePath+LogName
        
        with open(LogPath) as f:
            data = f.readlines()
            data = data[1:]
            data_len = len(data)
            
        Iters = []
        TestAccuracy = []
        TestLoss = []
        
        for row in range(data_len):
            data_row = data[row].split(' ')
            while '' in data_row:
                data_row.remove('')
            Iters.append(int(data_row[0]))
            TestAccuracy.append(float(data_row[2]))
            TestLoss.append(float(data_row[3]))     
        return Iters, TestAccuracy, TestLoss
