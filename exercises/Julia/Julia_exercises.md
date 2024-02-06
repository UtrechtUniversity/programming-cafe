# Julia intro with exercises

## 0. Help?

To get help in Julia REPL, type `?` followed by a `command` or a `"string"`, which can be a regular expression. For example `?div` will give you direct help on the `div` operation, but `?"div"` will return a list of functions whose docstrings mention `"div"`. 

#### Try using help

Find out the difference in the `div` and `/` functions. Try them on some examples: when do they give the same results?

[This cheatsheet](https://cheatsheets.quantecon.org/julia-cheatsheet.html) provides examples of common operations in Julia.

## 1. Importing packages 

Like in Python or R, to use additional packages, first you need to **install** them and then **import** into your session. Unlike in Python, but similarly to R, you do it from within Julia.

Julia comes with some optional packages that you can import without having to install them additionally. One of them is `Pkg.jl`. To launch it:

```
using Pkg
```
Now you can install Julia's most advanced plotting package, `Makie`:

```
Pkg.add("Makie")
```
This will trigger installation of all other packages that `Makie` uses, it might be a longish list if you don't have any Julia packages on your computer yet. 

### Precompilation

After downloading `Makie`, you will notice the message "Precompiling project". If you're installing many packages, this can take a while. Every time you add or remove a new package from your project, or change the version of a package you're using, you will trigger precompilation. It will be a one-time operation that can take a few (tens of) seconds, but it will make the subsequent use faster.

### Environments

If you want to keep track of what packages you're using or share your project with others, you can create your own environment. Different environments can have different totally different packages and versions installed from another environment. 

To create an environment in a the current directory (where you started Julia):
```
Pkg.activate(".")
```

now add some packages to this environment, for example `Makie`:
```
Pkg.add("Makie")
```

If you exit Julia and come back to this environment later, you can re-activate it and it will already "know" which packages you're using:

```
using Pkg
Pkg.activate(".")
```

To create an environment in a given path:
```
Pkg.activate("path/to/environment")
```

## Linear algebra

For any operations on matrices (except for creating, reading, deleting), it is best to import `LinearAlgebra`:
```
using LinearAlgebra
```
To calculate the *inverse* of a matrix, you can use the `inv()` function.

To transpose a matrix, use the `transpose()` function or, shorter, a single quote at the end of its name, e.g. `X'` to get the inverse of `X`.

The identity matrix (a quare matrix with 1 on the diagonal and zeros elsewhere) is created by referring to `I` or `I(n)` for a n-sized matrix.

#### Matrix multiplication

```
X * B
```

carries out regular matrix multiplication, so the number of rows of the first must be the same as the number of columns of the second matrix.

```
X .* B
```

Multiplies elements of `X` and `B` one by one. The *dot operator* works for various mathematical operators by making them *element-wise* - something akin to vectorized operations in R using the `apply()` command family.

#### Matrix division

Let's create some matrices as an example:
```
A = [1 2; 2 -4]
B = [28, -2]
```

To find `X` such that `A * X = B`, divide `B` by `A`:
```
X = A\B
```

### Exercise

A linear regression model is used to find linear relationships between some input variables and an output variable. In other terms, we try to predict a continuous variable using some input variables. For example, if the output variable is y and input variables are x₁, x₂, and x₃ then we want to find the β variables for best fit of y = β₀ + β₁x₁ + β₂x₂ + β₃x₃ or in matrix form y = βX.

Assume we have 100 observations of inputs and output. There are three input variables. The matrix of xs is X (100x3):
```
X = rand(Float64, (100,3))
```
The vector of the outputs is y which has length 100:
```
y = rand(100)
```

A shortcut to calculate the optimum β is calculated by using the formula β = (X'X)⁻¹X'y.

Write this formula in Julia to find β. 

<details open>
  <summary>Solution</summary>
  Note that the multiplier of β₀ is actually 1.

y = β₀.1 + β₁x₁ + β₂x₂ + β₃x₃

So, we should add a column of ones to the matrix as the first column.

X = [ones(100) X]

Now we can write the formula.

β = inv(X'X)X'y
</details>

This exercise comes from the [Udemy course "Programming with Julia" by Dr. İlker Arslan](https://www.udemy.com/course/programming-with-julia/)

## Types and multiple dispatch

In Julia, you don't have to define the types of variables. This is similar like in R or Python, but in all languages you will soon notice that some functions don't work on all types, or work the wrong way. For example, `"a"` and `a` might look similar, but in all of these langugages it will be processed differently.

Check the type of `1.0`:
```
typeof(1.0)
```

Julia has a hierarchical system of types. So you can define functions for more specific types or more general. If you define a function for a general type, for example all numbers, it will work for all sub-types of the type `Number`. You don't need to be specific about the level of the type, because every Julia command (every function call) will be compiled **for that specific type that was used**. 

For example, the function `abs()` is defined for multiple types, and does different things depending on the type of the variable. You can see what types it is defined for:

```
methods(abs)
```

But a different code will be in fact executed depending on what parameter you call the function with. You can see it using the macro `@code_typed` which gives you what will *in fact* be done for the respective argument:

```
@code_typed abs(-100)
```
That will execute a different function than:
```
@code_typed abs(-100.0)
```
So multiple dispatch means that the best function can be chosen for a given situation, but the user only needs to remember one function and not worry about the types. 

Incidentally, a function may have different methods because of speed, e.g. when there are different methods of calculating values for different types of arguments. So you can check how long the execution took using the package `BenchmarkTools`.

```
@btime abs(-100)
@btime abs(-100.0)
```

#### The gamma function

In the presentation, you saw adding a simpler method to the existing function `gamma()` from the package `SpecialFunctions`. Now you can check if that indeed gained you anything at all, using the `BenchmarkTools` package:

```
import SpecialFunctions:gamma
using BenchmarkTools
```

First see what methods are already defined for `gamma()`:

```
methods(gamma)
```
The function already has a method for a *union* of types that includes integers: 

```
 [5] gamma(n::Union{Int16, Int32, Int64, Int8, UInt16, UInt32, UInt64, UInt8})
     @ ~/.julia/packages/SpecialFunctions/QH8rV/src/gamma.jl:569
```

but we can assume that it is probably something more complicated than a factorial (fortunately all Julia packages are written in Julia so you can check the code of the function if you're curious!). 

Now add another methods for integers:

```
gamma( x :: Int ) = x > 0 ? factorial(x-1) : Inf
```

and check if this method is faster for integers:

```
@btime gamma(15.0)
@btime gamma(15)
```

The second line will use the method you defined for integers. Is it faster on your computer?

This example comes from the blog [MatecDev by Martin D. Maas](https://www.matecdev.com/posts/julia-multiple-dispatch.html). You can find more examples of multiple dispatch there.

You can find another educational example of Julia's multiple dispatch in [chapter 2.3.3](https://juliadatascience.io/julia_accomplish) of the online book Data Science using Julia by Storopoli, Huijzer and Alonso (2021).

#### Julia type tree

You can plot part of Julia's type tree with the following:

```
using GraphRecipes, Plots
plot(AbstractFloat, method=:tree, fontsize=10, nodeshape=:rect)
```

And using just ASCII characters in the terminal:

```
using AbstractTrees
AbstractTrees.children(d::DataType) = subtypes(d)
print_tree(Integer)
```

This exercise is based on [the solution by Przemyslaw Szufel at StackOverflow](https://stackoverflow.com/a/71526202/17001395), distributed under [the CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).

## Further reading

### Resources for a quick start

* [MATLAB--Python--Julia cheatsheet](https://cheatsheets.quantecon.org/)

### Prose and code examples explaining how Julia compares to other languages

* [Julia vs Numba and Cython: Looking Beyond Microbenchmarks](https://www.matecdev.com/posts/julia-python-numba-cython.html)
* [How to solve the same numerical Problem in 7 different Programming Languages](https://medium.com/@andreaskuhn92/how-to-solve-the-same-numerical-problem-in-7-different-programming-languages-a64daac3ed64) - these examples may not necessarily be the fastest code possible in the respective languages
