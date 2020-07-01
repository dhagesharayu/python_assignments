# DataFrame Basics

### Creating a dataframe

* Using csv file: weather_data.csv

![image](https://user-images.githubusercontent.com/63589909/86243927-cd442200-bbc4-11ea-8881-8b40d23fd965.png)

![image](https://user-images.githubusercontent.com/63589909/86244081-0aa8af80-bbc5-11ea-8b61-74f720ae1edf.png)

* Using a python dictionary

![image](https://user-images.githubusercontent.com/63589909/86244479-a4705c80-bbc5-11ea-95c1-d41cb8e7c4bd.png)

![image](https://user-images.githubusercontent.com/63589909/86244686-f5805080-bbc5-11ea-835a-ed33572b3dfd.png)

![image](https://user-images.githubusercontent.com/63589909/86245336-f2399480-bbc6-11ea-89c9-b43324c0076b.png)

```
df.head()  # starting 10 records      df.tail()  # end
df.head(2) # starting 2 records
df[:]  # indexing negative also works
df.loc[]  i.e on giving index gives value
```

* Every column of dataframe in pandas is a pandas Series.

![image](https://user-images.githubusercontent.com/63589909/86245508-3331a900-bbc7-11ea-9184-6ab7507f49a5.png)

* Print only a few columns

![image](https://user-images.githubusercontent.com/63589909/86245753-915e8c00-bbc7-11ea-8237-270566528da0.png)

* Max Temperature

![image](https://user-images.githubusercontent.com/63589909/86245950-e39fad00-bbc7-11ea-8e8d-4d4ded8ee069.png)

* std(), min() and other aggregation functions can also be used, as you can see below it gets executed only on numeric valued columns.

![image](https://user-images.githubusercontent.com/63589909/86246118-1a75c300-bbc8-11ea-9368-d4d2a8527e7f.png)

### Filtering: 

* All the rows where the temperature is greater than 32

![image](https://user-images.githubusercontent.com/63589909/86246390-8b1cdf80-bbc8-11ea-9fae-9cb519444f70.png)

* All the rows where the temperature is max

![image](https://user-images.githubusercontent.com/63589909/86246557-d0411180-bbc8-11ea-90c4-a1e5734c9d5e.png)

* Print only day and temp wher temp is max

![image](https://user-images.githubusercontent.com/63589909/86246755-21510580-bbc9-11ea-9602-dd67ed2dbf67.png)

### Change Dataframe index

![image](https://user-images.githubusercontent.com/63589909/86247075-96bcd600-bbc9-11ea-9b23-ea583a9d6aa7.png)

![image](https://user-images.githubusercontent.com/63589909/86247922-cae4c680-bbca-11ea-83f7-2172da5b354b.png)

* Now this day index can be used for filtering

![image](https://user-images.githubusercontent.com/63589909/86248729-e43a4280-bbcb-11ea-8bf9-f21f812899ae.png)

* Now to get back the index

![image](https://user-images.githubusercontent.com/63589909/86248988-47c47000-bbcc-11ea-9ff3-f7a25f7f2953.png)

* Suppose index is repeated

![image](https://user-images.githubusercontent.com/63589909/86249215-9a059100-bbcc-11ea-82f6-773c7c7251b1.png)

![image](https://user-images.githubusercontent.com/63589909/86249437-eea90c00-bbcc-11ea-99b4-5981aa4ea605.png)

