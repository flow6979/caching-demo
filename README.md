# Caching with memcache

## Problem statement
Setup a 3 node key-value cache cluster on local using Redis/Memcached and write a simple CRUD application to perform Get and Put operations.


## Testing

`curl -X PUT "http://localhost:8000/put/{key}" -H "Content-Type: application/json" -d '{"value": "{value}"}'`

`curl -X GET "http://localhost:8000/get/{key}"`

Example - 

`curl -X PUT "http://localhost:8000/put/greeting" -H "Content-Type: application/json" -d '{"value": "hello_world"}'`


`curl -X GET "http://localhost:8000/get/greeting"`

## Staring the server - 
python main.py

## Api documentation - 
http://0.0.0.0:8000/docs