# models/industry_forecasting.py

import pandas as pd
import numpy as np
from prophet import Prophet

def forecast_industry(industry_name, periods=30):
    """
    Forecasts industry performance using synthetic historical data.
    
    Parameters:
    - industry_name: str, the name of the industry (for logging/demonstration)
    - periods: int, number of future days to forecast
    
    Returns:
    - List of forecast records with date (ds), forecast value (yhat), and confidence intervals.
    """
    # For demonstration purposes, we generate synthetic daily data for the past 2 years.
    dates = pd.date_range(start="2023-01-01", periods=730, freq='D')
    
    # Create a synthetic trend with some noise (this would normally be your historical metric)
    base_value = 100  # starting value
    trend = np.linspace(0, 50, len(dates))  # gradual increase over time
    noise = np.random.normal(0, 5, len(dates))  # random fluctuations
    data = base_value + trend + noise
    
    # Create a DataFrame in Prophet's expected format
    df = pd.DataFrame({'ds': dates, 'y': data})
    
    # Initialize and fit the Prophet model
    m = Prophet()
    m.fit(df)
    
    # Create a dataframe for future dates
    future = m.make_future_dataframe(periods=periods, freq='D')
    forecast = m.predict(future)
    
    # Extract only the forecast for the future periods
    forecast_data = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(periods)
    return forecast_data.to_dict(orient='records')

if __name__ == "__main__":
    # Test the forecasting function for a sample industry
    forecast = forecast_industry("Tech", periods=10)
    print("Industry Forecast:", forecast)
