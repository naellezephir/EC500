import threading

'''
This class is responsible for updating its internal model and 
alerting the user if a worrisome prediction occurs
'''


class PredictionEngine(threading.Thread):
    def __init__(self):
        super().__init__()
        self._update_interval = 0

    def run(self):
        '''
        Entry point for the thread library.
        In here we should update the model and send notifications (if any)
        :return: None
        '''
        raise NotImplementedError

    def update_model(self):
        raise NotImplementedError

    def get_latest_reading_from_db(self):
        '''
        Reads the latest entry in the Vitals database
        :return: a three tuple (BloodOxygenData, PulseData, BloodPressureData)
        :raises: Database Exception
        '''
        raise NotImplementedError

    def notify_on_prediction(self):
        '''
        Sends a message to the notification engine detailing significant predictions
        :return: None
        :raises: RuntimeException
        '''
        raise NotImplementedError