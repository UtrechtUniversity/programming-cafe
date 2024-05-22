# Exercises Parallel Programming

## Python

There are many ways to speed up your code in Python, and also many ways to parallelize your code. The [Parallel Programming in Python course](https://carpentries-incubator.github.io/lesson-parallel-python) that is co-developed and taught by the eScience Center is a great way to learn more about this in more detail. Below is a notebook that will introduce you to the `multiprocessing` library in Python, and a link to some the course materials of the above course about `dask`.

### 1. `multiprocessing` library

Download the _notebook_ from the notebooks folder and follow the instructions in the notebook.

### 2. `dask` and profilers

Checkout this cool [tutorial](https://carpentries-incubator.github.io/lesson-parallel-python/02-benchmarking/index.html) on `dask` and measuring performance from the Parallel Programming in Python course (by the eScience Center).

### Optional:

Browse the [Parallel Programming in Python course](https://carpentries-incubator.github.io/lesson-parallel-python) to see what other topics might be interesting for you, and feel free to try out some of the code examples.


## R

There are different approaches to parallel programming in R. One package that can be used is the `doFuture` package in combination with the `foreach` package. 

```
install.packages("doFuture")
install.packages('foreach')
```

Follow [this tutorial](https://msu-icer.github.io/r-for-hpcc/parallelizing-r-code.html#writing-code-that-runs-on-multiple-cores) on how to use this package and stop at the section **Writing code that runs on multiple nodes**.

Try now to use the same method for doing some computations in parallel. For example:

```
estimate_pi <- function(N) {
    j <- 0
    for (i in 1:N) {
        x <- runif(1,-1,1)
        y <- runif(1,-1,1)
        if (x^2+y^2< 1)  {
            j=j+1
        }
    }
return(4*j/N)
}
```
Tip: There are two approaches: either parallelize the function, or run the function in parallel with batched inputs. Try both, think on forehand what would be the more useful approach and why and compare the results.




