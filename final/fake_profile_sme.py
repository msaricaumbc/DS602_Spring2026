from pathlib import Path

import pandas as pd


class SME:
    """
    Subject Matter Expert (SME) class for querying fake profile probabilities.

    This class simulates a domain expert who can answer limited questions about
    whether social media profiles are likely fake based on feature values.

    Usage:
        sme = SME()
        fake_prob = sme.ask({
            "account_age_days": 45,
            "following_count": 1800,
            "username_digit_count": 5,
            "repeated_captions": 12,
        })
    """

    def __init__(self):
        """
        Initialize the SME by loading the profile data and hidden labels.
        """
        self.asked = 0
        self.base_url = 'https://raw.githubusercontent.com/msaricaumbc/DS_data/master/ds602/final/'
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
            profiles = pd.read_csv(self.base_url + "fake_profiles_unlabeled.csv")
            labels = pd.read_csv(self.base_url + "fake_profiles_labels.csv")
            return profiles.merge(labels, on="profile_id")
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                "SME requires data_/fake_profiles_unlabeled.csv and "
                "data_/fake_profiles_labels.csv. Please run the generator first "
                "to create these files."
            ) from exc

    def ask(self, profile_id):
        self.asked += 1
        if self.asked > 500:
            raise Exception("Sorry, you have asked enough (500 query limit)")

        return int(self.df[self.df["profile_id"] == profile_id]["fake_profile"])

if __name__ == "__main__":
    sme = SME()
    sample_profile = sme.df.iloc[0]
    fake_prob = sme.ask(sample_profile["profile_id"])
    print(f"Fake profile: {fake_prob}")
