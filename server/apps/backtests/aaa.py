import pandas_market_calendars as mcal
import pandas as pd
from datetime import time
import sys
sys.path.append("../")

nyse = mcal.get_calendar('NYSE')

# Show available calendars
print(mcal.get_calendar_names())
