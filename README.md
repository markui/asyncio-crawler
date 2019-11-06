# A Web Crawler with asyncio coroutines

[Jesse-Jiryu-Davis-and-Guido-van-Rossum Example](http://www.aosabook.org/en/500L/a-web-crawler-with-asyncio-coroutines.html)

## Threads and Asynchronous IO for concurrency


## "An async framework builds on the two features we have shown—non-blocking sockets and the event loop—to run concurrent operations on a single thread."

## The stack trace shows only that the event loop was running a callback. We do not remember what led to the error. The chain is broken on both ends: we forgot where we were going and whence we came. This loss of context is called "stack ripping", and in many cases it confounds the investigator.
