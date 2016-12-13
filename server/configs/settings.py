import os
#image folder path
images_hdfs_path="hdfs://172.17.0.5:9000/images"
images_cache_folder="/home/sxiong/workspace/ImageServer/caches/images"
mapfile_cache_folder="/home/sxiong/workspace/ImageServer/caches/mapfiles"

#scp config
server_host="127.0.0.1"
ssh2_port=22
ssh2_username="sxiong"
ssh2_passwd="123456"

#redis config
redis_host="127.0.0.1"
redis_port=6379
redis_db=1

#Hbase config
hbase_host="172.17.0.5"
hbase_table_prefix="v1"
hbase_table_name="image"
hbase_pool_size=10
hbase_time_out=None

#api service config
api_host="0.0.0.0"
api_port=8001
#Byte
MAX_IMAGE_SIZE=200

#time interval
TIME_INTERVAL=3


