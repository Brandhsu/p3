# Python Parallel Programming

Standard libraries and concepts for exploiting concurrency and parallelism in Python.

---

**Sequential**

<img src="https://files.realpython.com/media/IOBound.4810a888b457.png" width=50%>

**MultiThreading**

<img src="https://files.realpython.com/media/Threading.3eef48da829e.png" width=50%>

**Asynchronous**

<img src="https://files.realpython.com/media/Asyncio.31182d3731cf.png" width=50%>

**MultiProcessing**

<img src="https://files.realpython.com/media/MProc.7cf3be371bbc.png" width=50%>

Credits: [RealPython: Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/)

## Setup

Requires Python 3.7+

```shell
$ pip install -r requirements.txt
```

To run a benchmark:

```shell
$ time python benchmark.py
```

## Results

The benchmark configurations are stored in `src/config.py`.

```shell
   _async.py  _asyncmp.py  _process.py  _thread.py  _unsync.py
0   3.333787     4.344021    19.011878    3.568494    3.358578
1   3.314583     5.886029    19.020730    3.334171    3.234820
2   3.219676     4.231164    19.032776    3.606869    3.332381
3   3.428546     7.124887    19.071330    3.401811    3.234913
4   3.238335     4.185607    18.942086    3.394499    3.259408
5   3.227443     4.261500    19.061262    3.692943    3.230274
6   3.234738     4.954754    18.994630    3.631398    3.241176
7   3.252762     4.144249    19.070190    3.522916    3.227482
8   3.235387     4.156997    19.137934    3.332789    3.298010
9   3.231671     4.302706    19.017840    3.344478    3.238097

       _async.py  _asyncmp.py  _process.py  _thread.py  _unsync.py
count  10.000000    10.000000    10.000000   10.000000   10.000000
mean    3.271693     4.759191    19.036065    3.483037    3.265514
std     0.067263     0.993399     0.052844    0.136898    0.047301
min     3.219676     4.144249    18.942086    3.332789    3.227482
25%     3.232438     4.196996    19.013368    3.356983    3.234843
50%     3.236861     4.282103    19.026753    3.462363    3.239637
75%     3.299128     4.802071    19.067958    3.597275    3.288360
max     3.428546     7.124887    19.137934    3.692943    3.358578

```

> NOTE: For reasons beyond my understanding, `src/_asyncmp.py` which uses [aiomultiprocess](https://github.com/omnilib/aiomultiprocess) is not reliable.

## Recommendations

- For I/O bound tasks you want concurrency, use async or threads (async better for very large amount of tasks)
- For CPU bound tasks you want parallelism, use multiprocessing

## References

- [RealPython: Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/)
- [RealPython: Python asyncio Course Intro and Overview](https://realpython.com/lessons/python-asyncio-course-intro-and-overview/)
- [GitHub: async-await-jetbrains-webcast](https://github.com/mikeckennedy/async-await-jetbrains-webcast)
- [YouTube: Demystifying Python's Async and Await Keywords](https://www.youtube.com/watch?v=F19R_M4Nay4)
- [YouTube: Python Asynchronous Programming - AsyncIO & Async/Await](https://www.youtube.com/watch?v=t5Bo1Je9EmE)
- [Medium: Python Asyncio with Multiprocessing](https://medium.com/@nbasker/python-asyncio-with-multiprocessing-2595f8ee3f8)
