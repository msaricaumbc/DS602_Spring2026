import pandas as pd

class SME:
    """
    Subject Matter Expert (SME) class for querying churn probabilities.
    
    This class simulates a domain expert who can answer questions about
    customer churn probabilities based on feature values.
    
    Usage:
        sme = SME()
        churn = sme.ask(12)
    """
    
    def __init__(self):
        """
        Initialize the SME by loading the full dataset.
        """
        self.asked = 0
        self.base_url = 'https://raw.githubusercontent.com/msaricaumbc/DS_data/master/ds602/final/';
        self.df = self._load_data()
    
    def _load_data(self):
        """
        Load the full dataset for querying.
        
        Returns:
        --------
        pandas.DataFrame
            Full dataset with features
        """
        try:
            X_train = pd.read_csv(self.base_url + 'streaming_churn_dataset.csv')
            y_train = pd.read_csv(self.base_url + 'streaming_churn_dataset_y.csv')
            X_train['will_churn'] = y_train['will_churn']
            return X_train
        except FileNotFoundError:
            raise FileNotFoundError(
                "SME requires streaming_churn_dataset_X.csv and streaming_churn_dataset_y.csv. "
                "Please run the generator first to create these files."
            )
    
    def ask(self, idx):
        self.asked += 1
        if self.asked > 500:
            raise Exception("Sorry, you have asked enough (500 query limit)")
    
        return int(self.df['will_churn'][idx])

if __name__ == "__main__":
    sme = SME()
    churn = sme.ask(12)
    print(f"Churn: {churn}")