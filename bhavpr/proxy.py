from bhavpr.collection.logger_factory import get_logger
from bhavpr.collection.fetch_pr import download_data
from bhavpr.parser.pr_record import load_meta, company_name_search


class BhavPR(object):
    def __init__(self):
        self.logger = get_logger()
        self.meta = load_meta(local=True)
        self.focus = None
        pass

    def collect(self, date_start, date_end) -> bool:
        """Downloads and extracts PR zip files to a temporary directory.
        date_start: Format as 01-01-2020 DD-MM-YYYY
        date_end: Format as 05-01-2020 DD-MM-YYYY
        """
        self.logger.info(
            "collect(): Received inputs {}, {}".format(date_start, date_end)
        )
        download_data(date_start, date_end)
        return True

    def get_symbol(self, search_string, on_symbol=False) -> set:
        return company_name_search(self.meta, search_string, on_symbol)

    def set_company(self, company_name) -> bool:
        record = self.get_symbol(company_name, on_symbol=True)
        if len(record) != 1:
            return False
        self.focus = record[0]
        return True
