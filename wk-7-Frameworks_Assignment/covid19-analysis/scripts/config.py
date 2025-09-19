import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project configuration
class Config:
    # Project info
    PROJECT_NAME = os.getenv('PROJECT_NAME', 'COVID-19 Research Analysis')
    PROJECT_VERSION = os.getenv('PROJECT_VERSION', '1.0.0')
    
    # Data paths
    DATA_PATH = os.getenv('DATA_PATH', './data')
    RAW_DATA_FILE = os.getenv('RAW_DATA_FILE', 'metadata.csv')
    CLEANED_DATA_FILE = os.getenv('CLEANED_DATA_FILE', 'cleaned_metadata.csv')
    
    # Analysis settings
    SAMPLE_SIZE = int(os.getenv('SAMPLE_SIZE', '1000'))
    YEAR_RANGE_START = int(os.getenv('YEAR_RANGE_START', '2019'))
    YEAR_RANGE_END = int(os.getenv('YEAR_RANGE_END', '2023'))
    
    # Visualization settings
    PLOT_STYLE = os.getenv('PLOT_STYLE', 'default')
    COLOR_PALETTE = os.getenv('COLOR_PALETTE', 'husl')
    FIGURE_WIDTH = int(os.getenv('FIGURE_WIDTH', '10'))
    FIGURE_HEIGHT = int(os.getenv('FIGURE_HEIGHT', '6'))
    
    # Streamlit settings
    APP_TITLE = os.getenv('APP_TITLE', 'COVID-19 Research Explorer')
    APP_LAYOUT = os.getenv('APP_LAYOUT', 'wide')
    APP_THEME = os.getenv('APP_THEME', 'light')
    
    # Helper methods
    def get_data_path(self, filename=None):
        """Get full path to data file"""
        if filename:
            return os.path.join(self.DATA_PATH, filename)
        return self.DATA_PATH

# Create a config instance
config = Config()
