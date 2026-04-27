import pandas as pd


class SME:
    """
    Subject Matter Expert (SME) class for querying student success labels.

    This class simulates a domain expert who can answer limited questions about
    whether students are likely to succeed based on a student ID.

    Usage:
        sme = SME()
        likely_success = sme.ask("S00001")
    """

    def __init__(self):
        """
        Initialize the SME by loading the student data and hidden labels.
        """
        self.asked = 0
        self.base_url = "https://raw.githubusercontent.com/msaricaumbc/DS_data/master/ds602/final/"
        self.df = self._load_data()

    def _load_data(self):
        """
        Load the full dataset for querying.

        Returns:
        --------
        pandas.DataFrame
            Full dataset with features and target
        """
        try:
            students = pd.read_csv(self.base_url + "student_success_unlabeled.csv")
            labels = pd.read_csv(self.base_url + "student_success_labels.csv")
            return students.merge(labels, on="student_id")
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                "SME requires student_success_unlabeled.csv and "
                "student_success_labels.csv. Please run the generator first "
                "to create these files."
            ) from exc

    def ask(self, student_id):
        self.asked += 1
        if self.asked > 500:
            raise Exception("Sorry, you have asked enough (500 query limit)")

        return int(self.df[self.df["student_id"] == student_id]["likely_success"])


if __name__ == "__main__":
    sme = SME()
    sample_student = sme.df.iloc[0]
    likely_success = sme.ask(sample_student["student_id"])
    print(f"Likely success: {likely_success}")
