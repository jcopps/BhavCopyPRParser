import os

from bhavpr.parser.anddmmyy import AnDDMMYY
from bhavpr.collection.download_helper import PrProperties
from bhavpr.parser.company import Company
from bhavpr.collection.constants import (
    PR_DATA_DIR,
    DEFAULT_COMPANY_NAME,
    ANNOUNCEMENT_PREFIX,
    TEXT_EXT,
    CSV_EXT,
)


class PRRecord(object):
    def __init__(self, pr_props):
        dir_path = os.path.join(PR_DATA_DIR, pr_props.get_file_name(directory=True))
        self.announcements = AnDDMMYY(
            DEFAULT_COMPANY_NAME,
            os.path.join(
                dir_path, pr_props.get_specific_file_name(ANNOUNCEMENT_PREFIX, TEXT_EXT)
            ),
        )


def load_meta(local=True) -> list:
    companies_set = set()
    print("Load_mta: ", PR_DATA_DIR)
    for file_name in os.listdir(PR_DATA_DIR):
        abs_path = os.path.join(PR_DATA_DIR, file_name)
        if not os.path.isdir(abs_path):
            continue
        print("Filename: ", file_name)
        pr_props = PrProperties.create_instance_from_directory(file_name)
        pr_rec = PRRecord(pr_props)
        company_keys = pr_rec.announcements.data.keys()
        companies_set = companies_set.union(company_keys)
        print("Length: ", len(companies_set))
        # print([(x.company_name, x.symbol) if x else "None" for x in companies_set][:10])
    return companies_set


def company_name_search(meta, pattern, on_symbol=False):
    return Company.company_name_search(meta, pattern, on_symbol)
