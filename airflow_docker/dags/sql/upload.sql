ALTER ROLE airflow; -- to allow superuser to store data
COPY objects("track_id", "type","traveled_d", "avg_speed", "lat", "lon", "speed", "lon_acc", "lat_acc", "time")
FROM '/20181024_d1_0830_0900.csv'
DELIMITER ','
CSV HEADER;


