# Caching with memcache

## Problem statement
Setup a 3 node key-value cache cluster on local using Redis/Memcached and write a simple CRUD application to perform Get and Put operations.


## Testing

`curl -X PUT "http://localhost:8000/cache/doctor" -H "Content-Type: application/json" -d '{"value": "Aditya"}'`

`curl -X GET "http://localhost:8000/cache/doctor"`

`curl -X DELETE "http://localhost:8000/cache/doctor"`

## Staring the server - 
python main.py

## Api documentation - 
http://127.0.0.1/docs
