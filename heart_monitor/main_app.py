import sensors
import display
import prediction_engine
import notification_manager
import notifications_sender
import realtime_data_processor
from multiprocessing import Queue
from common_types import Contact


def main(cmd_args):
    data_queue = Queue()
    text_display = display.TextTerminalDisplay()
    notifications = notification_manager.FlexibleNotificationManager(
        Contact("Nurse Nancy", "NancySMS", "NancyTEL", "NancyEMAIL"),
        notifications_sender.MockSMSSender(),
        notifications_sender.MockTelegramSender(),
        notifications_sender.MockEmailSender()
        )
    oxygen_sensor = sensors.BloodOxygenSensorReader(2, data_queue, text_display)
    processing = realtime_data_processor.RealTimeDataProcessor(data_queue, notifications)
    oxygen_sensor.start()
    processing.start()
    oxygen_sensor.join()
    return 0


if __name__ == '__main__':
    main(None)