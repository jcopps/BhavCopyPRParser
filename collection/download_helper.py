from collection.constants import PR_URL

class PrProperties(object):
    def __init__(self, day, month, year) -> None:
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def pad_zero(element, final_len=2):
        if element < 10:
            element = str(element).rjust(final_len, '0')
        return element

    @staticmethod
    def format_year(year):
        year = str(year)
        if len(year) > 2:
            year = year[-2:]
        return year

    def get_file_name(self, directory=False) -> str:
        file_name = 'PR{0}{1}{2}'

        day = PrProperties.pad_zero(self.day)
        month = PrProperties.pad_zero(self.month)
        year = PrProperties.format_year(self.year)

        file_name = file_name.format(day, month, year)
        if directory:
            return file_name
        file_name = ''.join([file_name, '.zip'])
        return file_name

    def get_anddmmyy_file_name(self) -> str:
        file_name = self.get_file_name(directory=True)
        file_name = file_name.replace('PR', 'an')
        return ''.join([file_name, '.txt'])

    def get_bcddmmyy_file_name(self) -> str:
        file_name = self.get_file_name(directory=True)
        file_name = file_name.replace('PR', 'bc')
        return ''.join([file_name, '.csv'])

    def get_download_url(self) -> str:
        file_name = self.get_file_name()
        url = PR_URL.format(file_name)
        return url


