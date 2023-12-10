from dagster import asset
import pandas as pd

@asset
def test_assets_1():
    # Dummy data - in a real scenario, this would be loaded from a database, API, etc.
    data = {
        "name": ["John", "Bobbie", "Courtney"],
        "age": [18, 25, 34]
    }
    df = pd.DataFrame(data)

    # Process data (simple example)
    df['age_category'] = df['age'].apply(lambda x: 'Above 30' if x > 30 else 'Below 30')

    # Save to CSV
    csv_file = '/tutorial/data/test_assets_1.csv'
    df.to_csv(csv_file, index=False)
    return csv_file
