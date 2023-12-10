import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """

    # Write your logic here
    car_matrix=data.pivot(index='id_1',columns='id_2',values='car')
    car_matrix
    
the below are the result performed

id_2	801	802	803	804	805	806	807	808	809	821	822	823	824	825	826	827	829	830	831
id_1																			
801	NaN	2.80	6.00	7.70	11.70	13.40	16.90	19.60	21.00	23.52	24.67	26.53	27.92	29.08	30.87	32.53	36.32	38.27	39.24
802	2.80	NaN	3.40	5.20	9.20	10.90	14.30	17.10	18.50	20.92	22.07	23.93	25.32	26.48	28.27	29.93	33.72	35.67	36.64
803	6.00	3.40	NaN	2.00	6.00	7.70	11.10	13.90	15.30	17.72	18.87	20.73	22.12	23.28	25.07	26.73	30.52	32.47	33.44
804	7.70	5.20	2.00	NaN	4.40	6.10	9.50	12.30	13.70	16.12	17.27	19.13	20.52	21.68	23.47	25.13	28.92	30.87	31.84
805	11.70	9.20	6.00	4.40	NaN	2.00	5.40	8.20	9.60	12.02	13.17	15.03	16.42	17.58	19.37	21.03	24.82	26.77	27.74
806	13.40	10.90	7.70	6.10	2.00	NaN	3.80	6.60	8.00	10.42	11.57	13.43	14.82	15.98	17.77	19.43	23.22	25.17	26.14
807	16.90	14.30	11.10	9.50	5.40	3.80	NaN	2.90	4.30	6.82	7.97	9.83	11.22	12.38	14.17	15.83	19.62	21.57	22.54
808	19.60	17.10	13.90	12.30	8.20	6.60	2.90	NaN	1.70	4.12	5.27	7.13	8.52	9.68	11.47	13.13	16.92	18.87	19.84
809	21.00	18.50	15.30	13.70	9.60	8.00	4.30	1.70	NaN	2.92	4.07	5.93	7.32	8.48	10.27	11.93	15.72	17.67	18.64
821	23.52	20.92	17.72	16.12	12.02	10.42	6.82	4.12	2.92	NaN	1.80	3.67	5.06	6.22	8.01	9.43	13.26	15.17	16.15
822	24.67	22.07	18.87	17.27	13.17	11.57	7.97	5.27	4.07	1.80	NaN	2.21	3.60	4.76	6.55	8.00	11.81	13.74	14.68
823	26.53	23.93	20.73	19.13	15.03	13.43	9.83	7.13	5.93	3.67	2.21	NaN	1.79	2.94	4.74	6.15	10.00	11.89	12.87
824	27.92	25.32	22.12	20.52	16.42	7.80	11.22	8.52	7.32	5.06	3.60	1.79	NaN	1.71	3.50	4.92	8.77	10.66	11.64
825	29.08	26.48	23.28	21.68	17.58	15.98	12.38	9.68	8.48	6.22	4.76	2.94	1.71	NaN	2.20	3.65	7.46	9.35	10.33
826	30.87	28.27	25.07	23.47	19.37	17.77	14.17	11.47	10.27	8.01	6.55	4.74	3.50	2.20	NaN	2.05	5.81	7.71	8.69
827	32.53	29.93	26.73	25.13	21.03	19.43	15.83	13.13	11.93	9.43	8.00	6.15	4.92	3.65	2.05	NaN	4.14	6.06	7.04
829	36.32	33.72	30.52	28.92	24.82	23.22	19.62	16.92	15.72	13.26	11.81	10.00	21.40	7.46	5.81	4.14	NaN	2.38	3.36
830	38.27	35.67	32.47	30.87	26.77	25.17	21.57	18.87	17.67	15.17	13.74	11.89	10.66	NaN	7.71	6.06	2.38	NaN	1.39
831	39.24	36.64	33.44	31.84	27
    return df




def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    car_counts=data['car'].value_counts().to_dict()
    car_counts

    return dict()


def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    bus_column=data['bus']
    bus_column
    
    0      10.1
1      32.4
2      64.7
3      28.8
4      14.2
       ... 
336     6.9
337    12.0
338    50.1
339    15.3
340    72.6
Name: bus, Length: 341, dtype: float64
    
    bus_mean=bus_column.mean()
    bus_mean
    
    31.932844574780056
    
    bus_indexes=bus_column[bus_column>2*bus_mean].index.tolist()
    bus_indexes
    
    [2, 7, 12, 17, 25, 30, 54, 64, 70, 97, 144, 145, 149, 154, 160, 201,  206,  210,  215,  234,  235,  245,  250,  309,  314,  319,  322,  323,  334,  340]
    
    return list()


def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here
    truck_column=data['truck']
truck_column
     0       15.2
1       48.5
2       97.0
3       43.2
4       21.2
       ...  
336     10.3
337     17.9
338     75.2
339     23.0
340    108.8
Name: truck, Length: 341, dtype: float64
   
    truck_avg=data.groupby('route')['truck'].mean()
truck_avg   
   route
1     49.164103
2     41.403125
3     50.075000
4     51.096774
5     43.327778
6     47.952500
7     52.525862
8     46.128571
9     54.531429
10    41.400000
Name: truck, dtype: float64
     
    truck_routes=truck_avg[truck_avg>7].index.tolist()
truck_routes
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return list()


def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    matrix = pd.DataFrame(df)
def custom_multiply(x):
    return x * 2  
  custom_multiply = matrix.applymap(custom_multiply)

# Print the custom_multiplymatrix
print(custom_multiply)
 
def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here
    
import pandas as pd

def time_check(df: pd.DataFrame) -> pd.Series:
    time_check_result = df.groupby(['id', 'id_2'])['timestamp'].apply(lambda x: (x.max() - x.min()) == pd.Timedelta(days=7))

    return time_check_result

    return pd.Series()

the below are the result parformed

     id_1  id_2  route   moto    car     rv   bus  truck
0     829   827      1   2.05   4.14   4.14  10.1   15.2
1     829   821      4   6.63  13.26  13.26  32.4   48.5
2     829   804      7  14.41  28.92  28.92  64.7   97.0
3     829   822      6   5.90  11.81  11.81  28.8   43.2
4     829   826      9   2.87   5.81   5.81  14.2   21.2
..    ...   ...    ...    ...    ...    ...   ...    ...
336   803   802      3   1.70   3.40   3.40   6.9   10.3
337   803   805      4   3.00   6.00   6.00  12.0   17.9
338   803   825      3  11.59  23.28  23.28  50.1   75.2
339   803   806      9   3.80   7.70   7.70  15.3   23.0
340   803   830      1  16.18  32.47  32.47  72.6  108.8

[341 rows x 8 columns]






