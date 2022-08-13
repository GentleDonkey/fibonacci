## Guide
- install [websocket](https://websockets.readthedocs.io/en/stable/intro/index.html)
```
pip install websockets
```
- run the `server.py` 
- run the `client.py` 
- the websocket is listening on port 7890, if you would like to change it, pls set in `setting.py` file

## Somewhere could be improved
- add security
- add test
- overflow when input number bigger than 2^31
- consider if there are multi clients connected
  - an IP address standing for each of them is needed
- consider if there are huge volume request:
  - instead of generate a new sub-fibonacci every time, save the fibonacci array in cache when first time run
  - check if the next request is in the cache
    - if yes, return
    - if no, generate and append the elements 

## Reference of learning
### websocket
- https://websockets.readthedocs.io/en/stable/intro/index.html
- https://www.youtube.com/watch?v=tgtb9iucOts
### asynchronous
- https://docs.python.org/3/library/asyncio.html
- https://www.youtube.com/watch?v=t5Bo1Je9EmE
- https://zhuanlan.zhihu.com/p/27258289
### logging
- https://docs.python.org/3/library/logging.html
### troubleshooting
- keep the connection alive: https://websockets.readthedocs.io/en/stable/topics/timeouts.html
- fibonacci generator: https://stackoverflow.com/questions/15305362/python-fibonacci-sequence