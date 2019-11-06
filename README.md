# A Web Crawler with asyncio coroutines

[Jesse-Jiryu-Davis-and-Guido-van-Rossum Example](http://www.aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html)

## 1. Threads and Asynchronous IO for concurrency

Traditionally we create a thread pool to do concurrent tasks, however when we need to do A LOT OF concurrent tasks, there is a limit beyond which most systems can still create sockets, but have run out of threads. Because it's quite expensive to use a thread. This is why Async IO was born.


## 2. Async Frameworks - Non blocking sockets + Event Loop

> "An async framework builds on the two features we have shown—**non-blocking sockets** and the **event loop**—to run concurrent operations on a single thread."

## 3. Concurrent Programming with Callbacks

We can program asynchronously, using event loops and non blocking sockets, using the `DefaultSelector` that utilizes `epoll, kqueue, or select`. 

However there are 2 problems with this kind of progamming

#### 1) Spaghetti Code
#### 2) Stack Ripping (Loss of Context - Error prone, debugging is hard)
> The stack trace shows only that the event loop was running a callback. We do not remember what led to the error. The chain is broken on both ends: we forgot where we were going and whence we came. This loss of context is called "stack ripping", and in many cases it confounds the investigator.
> So, even apart from the long debate about the relative efficiencies of multithreading and async, there is this other debate regarding which is more error-prone: threads are susceptible to data races if you make a mistake synchronizing them, but callbacks are stubborn to debug due to stack ripping.
