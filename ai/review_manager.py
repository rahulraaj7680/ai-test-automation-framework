import csv


class ReviewManager:

    def __init__(self, review_file):
        self.review_file = review_file

    def get_approved_test_cases(self):
        approved_cases = []

        with open(
            self.review_file,
            "r",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:
                if row["status"].strip().upper() == "APPROVED":
                    approved_cases.append(row["test_case_id"])

        return approved_cases