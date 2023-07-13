###### quick side project to learn more about coroutines...

running dockerised kafka with two producers and two consumers, to visualize performance diffrences between working with subroutines and coroutines (async/wait) syntax...

# PRODUCERS:

after running both producers querying **jsonplaceholder.typicode.com** endpoints, results are being published ≈120%

# CONSUMERS:

although messages to the async topic are being published at much faster rate, the "async syntax" consumer kept a similar performance...
