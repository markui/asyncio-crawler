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

## 4. Coroutines

"A subroutine that can be paused and resumed"

When do threads switch? Whenever a thread begins sleeping or awaiting network I/O, there is a chance for another thread to take the GIL and execute Python code. This is cooperative multitasking. CPython also has preemptive multitasking: If a thread runs uninterrupted for 1000 bytecode instructions in Python 2, or runs 15 milliseconds in Python 3, then it gives up the GIL and another thread may run. Think of this like time slicing in the olden days when we had many threads but one CPU

#### With Coroutines,
> It is possible to write asynchronous code that combines the efficiency of callbacks with the classic good looks of multithreaded programming. This combination is achieved with a pattern called "coroutines".
> It is also scalable. Compared to the 50k of memory per thread and the operating system's hard limits on threads, a Python coroutine takes barely 3k of memory on Jesse's system. Python can easily start hundreds of thousands of coroutines
> Whereas threads are preemptively multitasked by the operating system, coroutines multitask cooperatively: they choose when to pause, and which coroutine to run next.
> Steps need no longer be scattered among callbacks; we gather them into the same generator function:

####  The coroutines in the standard "asyncio" library in Python 3.4 are built upon generators, a Future class, and the "yield from" statement. 

cf) A coroutine can delegate work to a sub-coroutine with `yield from` and receive the result of the work.

## 5. asyncio Coroutines

> We no longer need a fetcher class like we had in the callback-based program. That class was a workaround for a deficiency of callbacks: they need some place to store state while waiting for I/O, since their local variables are not preserved across calls. But the fetch coroutine can store its state in local variables like a regular function does, so there is no more need for a class
