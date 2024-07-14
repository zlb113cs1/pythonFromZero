import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Define a Data Model
class DataModel(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Float)

# Data Acquisition
def acquire_data():
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'value': np.random.rand(5) * 100
    }
    df = pd.DataFrame(data)
    return df

# Data Processing
def process_data(df):
    df['value'] = df['value'] * 1.1  # Arbitrary processing step
    df['value'] = df['value'].round(2)
    return df

# Data Storage
def store_data(df, engine):
    df.to_sql('data', con=engine, if_exists='replace', index=False)

# Data Visualization
def visualize_data(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['name'], df['value'], color='skyblue')
    plt.xlabel('Name')
    plt.ylabel('Value')
    plt.title('Data Visualization')
    plt.show()

# Main function to manage the data pipeline
def main():
    # Create a SQLite database
    engine = create_engine('sqlite:///data.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Step 1: Acquire Data
    data = acquire_data()
    print("Acquired Data:")
    print(data)

    # Step 2: Process Data
    processed_data = process_data(data)
    print("\nProcessed Data:")
    print(processed_data)

    # Step 3: Store Data
    store_data(processed_data, engine)
    print("\nData stored in database.")

    # Step 4: Visualize Data
    visualize_data(processed_data)

    # Optional: Query the database to check stored data
    queried_data = session.query(DataModel).all()
    print("\nQueried Data from Database:")
    for row in queried_data:
        print(row.id, row.name, row.value)

if __name__ == "__main__":
    main()
