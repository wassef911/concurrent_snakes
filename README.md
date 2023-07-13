###### quick side project to learn more about coroutines...
![background](https://github.com/wassef911/concurrent_snakes/blob/master/images/background.png?raw=true)

running dockerised kafka with two producers and two consumers, to visualize performance diffrences between working with subroutines and coroutines (async/wait) syntax...

# PRODUCERS:

after running both producers querying **jsonplaceholder.typicode.com** endpoints, results are being published ≈120%
![Screenshot](https://github.com/wassef911/concurrent_snakes/blob/master/images/producer_benchmark.png?raw=true)

# CONSUMERS:
![Screenshot](https://github.com/wassef911/concurrent_snakes/blob/master/images/consumer_benchmark.png?raw=true)
although messages to the async topic are being published at much faster rate, the "async syntax" consumer kept a similar performance...
