from bhavpr.collection.logger_factory import get_logger


class BhavPR(object):
    def __init__(self):
        self.logger = get_logger()
        pass

    def collect(date_start, date_end):
        """Downloads and extracts PR zip files to a temporary directory.
        date_start: Format as 01-01-2020 DD-MM-YYYY
        date_end: Format as 05-01-2020 DD-MM-YYYY
        """
        logger.info("collect(): Received inputs {}, {}".format(date_start, date_end))
        download_data(from_str, to_str)
