import pandas as pd
import matplotlib.pyplot as plt
taxi_jan = pd.read_parquet('C:/Users/prageesh.s/Documents/Python/DS/DS-Taxi-Analysis/data/yellow_tripdata_2025-01.parquet')
#print(taxi_jan.shape)
taxi_feb = pd.read_parquet('C:/Users/prageesh.s/Documents/Python/DS/DS-Taxi-Analysis/data/yellow_tripdata_2025-02.parquet')
#print(taxi_feb.shape)
taxi_df = pd.concat([taxi_jan, taxi_feb], ignore_index=True)
taxi_df_new = taxi_df[['tpep_pickup_datetime', 'tpep_dropoff_datetime',
       'passenger_count', 'trip_distance', 'PULocationID', 'DOLocationID', 'payment_type', 'fare_amount',
       'total_amount']]
taxi_df_new['total_amount'].value_counts().plot(kind='bar', figsize=(10, 5),bin =1000)
plt.title('Total Amount Distribution')
plt.show()