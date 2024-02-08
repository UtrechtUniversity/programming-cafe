# Julia intro with exercises

## Starting Julia

To start Julia, open a terminal window (git bash for windows) and enter `julia`.
This will open the so-called REPL, which stands for read-evaluate-print-loop. The interactive command-line REPL allows quick and easy execution of Julia statements.

Like the terminal, the Julia REPL has a prompt, where it awaits input:
`julia>`

If you work in VS code you can interact with the Julia REPL via the terminal window within VS code.

## 0. Getting help
To get help in Julia REPL, type `?` (the prompt will now change) followed by a `command` or a `"string"`, which can be a regular expression. For example `?div` will give you direct help on the `div` operation, but `?"div"` will return a list of functions whose docstrings mention `"div"`. 

The chapters in this document are zero-indexed, but Julia is 1-indexed, like R or FORTRAN, but unlike Python.

### Try using help

Find out the difference in the `div` and `/` functions. Try them on some examples: when do they give the same results?

[This cheatsheet](https://cheatsheets.quantecon.org/julia-cheatsheet.html) provides examples of common operations in Julia.

## 1. Importing packages 

Like in Python or R, to use additional packages, first you need to **install** them and then **import** into your session. Unlike in Python, but similarly to R, you do it from within Julia.

Julia comes with some optional packages that you can import without having to install them additionally. One of them is `Pkg.jl`. To launch it:

```julia
using Pkg
```
Now you can install Julia's most advanced plotting package, `CairoMakie`:

```julia
Pkg.add("CairoMakie")
```
This will trigger installation of all other packages that `CairoMakie` uses, it might be a longish list if you don't have any Julia packages on your computer yet. 

Once `CairoMakie` is installed, you can import it into your current session:
```julia
using CairoMakie
```

If you try importing a package that is not installed yet, Julia will ask you if you want to install it. The following exercises don't include explicit instructions for installing each package that is used; they only tell you what to import. If the package is missing, you can just confirm that you do intend to install it.

### Precompilation

After downloading `CairoMakie`, you will notice the message "Precompiling project". If you're installing many packages, this can take a while. Every time you add or remove a new package from your project, or change the version of a package you're using, you will trigger precompilation. It will be a one-time operation that can take a few (tens of) seconds, but it will make the subsequent use faster.

### Environments

If you want to keep track of what packages you're using or share your project with others, you can create your own environment. **This step is optional: if you just want to try some commands and don't plan to return to yur project later, you can skip this chapter.**

Different environments can have totally different packages and versions installed. 

To create an environment in a the current directory (where you started Julia):
```julia
Pkg.activate(".")
```

now add some packages to this environment, for example `Makie`:
```julia
Pkg.add("GLMakie")
```

If you exit Julia and come back to this environment later, you can re-activate it and it will already "know" which packages you're using:
```julia
using Pkg
Pkg.activate(".")
```

To create an environment in a given path:
```
Pkg.activate("path/to/environment")
```

## 2. Variables

Assigning variables works the same way as in R, Python or MATLAB:
```julia
name = "Julia" # string variable
```
Extract parts of a variable:
```julia
name[end]
name[begin]
name[2:4]
```

Get the length of a variable and the position of the first and last character:

```julia
length(name)
firstindex(name)
lastindex(name)
```

In variables (names and contents) you can use any character that is represented in Unicode:

```julia
θ = π * 3
```
To type a symbol in Julia that you don't have on your keyboard, you can use its Unicode id (that you are not likely to remember) or a word corresponding to it, for example `\pi` followed by the `TAB` key. A Unicode cheatsheet can be found [here](https://docs.julialang.org/en/v1/manual/unicode-input/).

You can paste the value of a variable into displayed text (e.g. returned by a function) by referring to the variable name preceded with `$`:

```julia
Δ = 2; Ω = 3
"The first variable equals $Δ, the second: $Ω"
```

### Structs

Structs are composite types, cosisting of several objects which can be of several types. 

```julia
struct Student
  major::String
  grade::Float64
  name::String
  enrolled::Bool
  group::Integer
end
```
This is a struct that we can use to create instances, i.e. record of individual students, and make operations on them.

```julia
Emilia = Student("Geoscience", 5.5, "Jarochowska", true, 1)
```

You can see student's properties by writing `Emilia.major`.

Regular structs cannot be changed once defined (without restarting Julia). But you can make a `mutable struct` that can be modified. 

#### Exercise 

Create a struct for a prism. The struct should include three fields: width, length, height.
Data types of the fields should be the same and they should be a subtype of Real type.
Create an instance of a Prism type. Set the values for width, length, and height any value you like.
Calculate the volume of the prism object using the field values. You can look up the syntax and try to write a [function](https://docs.julialang.org/en/v1/manual/functions/).

This exercise comes from the [Udemy course "Programming with Julia" by Dr. İlker Arslan](https://www.udemy.com/course/programming-with-julia/)
<details open>
  <summary>Solution</summary>
```julia

mutable struct Prism{T <: Real} 
  width::T 
  length::T 
  height::T
end

p = Prism(3.5, 7.2, 7.5)

volume = p.height * p.length * p.width
```
</details>

### Arrays

#### Creating arrays

To Julia, a 1-dimensional array is still an array (what is called a "vector" in R). A 2-dimensional array is a matrix. You can have n-dimensional arrays. You can create arrays in various ways:

A 3 x 4 array of zeros:
```julia
Z = zeros(3, 4)
```

Arrays can store variables of one type of various types. Make an array with strings, integers and complex numbers:

```julia
weird_array = [2, "example text",  1+2im]
```
You will get an object `3-element Vector{Any}` so a vector (1-dimensional array) with the type `Any`. `Any` is the most general of variable types in Julia, it encompasses number, strings and other things. So when Julia cannot narrow down the type of objects, it will assume they are of type `Any`.

You can also make an array of a more specified type, e.g. floating-point numbers:
```julia
floats = [1.1 1.2 1.3; 2.1 2.2 2.3]
```

Check the type of `floats`:
```julia
typeof(floats)
```

You can tell Julia upfront what data type you intend for an array, instead of letting it guess:

```julia
my_floats = Float64[3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0]
```

You can make an array by taking a slice from another array:
```julia
new = Z[1:2, 2:end] # this takes a range: from position 1 to 2 in rows and 2 to the end in columns
a = floats[end, end]
```

What is the type of `new` and of `a`?
You can't really tell if `Z[1:2, 2:end]` cuts out the right part of the matrix because all elements are zeros. So let's overwrite some elements in the array:
```
Z[2,3] = 1
Z[1:2, 2:end]
```

This time we see that we indeed sliced out the right part of the matrix `Z`. And even though you assign `1` (an integer) to the element in the 2nd row and 2nd column of `Z`, it has automatically been converted to a float, because that is the type of `Z`.

If you want to check if an element is included in an array, you can use a function (`issubset()`) but also the mathematical operator ∊ which is easier to read:

```julia
0 ∈ Z
```
You type it as `\in` and the `TAB` key. Julia has a lot of logical operators for all occasions.

#### Operations on arrays

Broadcasting is applying an operation element-wise:
```julia
Y = Z .+ 0.5
```
Adds 0.5 to each element of `Z`.

You can use the `.` operator with any function. For example the exponent:
```julia
ℯ .^ floats
```
calculates ℯ to the power defined by each element of `floats`.

You can create an array that is a result of a function. That is: using an array comprehension.
For example:
```julia
U = [x + 2y for x in 1:5, y in 0:1] 
```

#### Exercise
Hints: Use `?` and `command` to check how to use a function. [This cheatsheet](https://cheatsheets.quantecon.org/julia-cheatsheet.html) provides examples of common operations in Julia.


1. Create an array with 10 random numbers.
2. Use the `reshape()` function to make the array 2 x 5.
3. Apply the function `==` to the array to check element-wise if it is equal to `my_floats`
4. Create an array that contains the reciprocals (1/n) for each element of `floats`
5. Create a vector that contains the reciprocals (1/n) for n from 8 to 12

## 3. Linear algebra

For any operations on matrices (except for creating, reading, deleting), it is best to import `LinearAlgebra`:
```julia
using LinearAlgebra
```
To calculate the *inverse* of a matrix, you can use the `inv()` function.

To transpose a matrix, use the `transpose()` function or, shorter, a single quote at the end of its name, e.g. `X'` to get the transpose.

The identity matrix (a square matrix with 1 on the diagonal and zeros elsewhere) is created by referring to `I` or `I(n)` for a n-sized matrix.

### Matrix multiplication

```julia
X * B
```

carries out regular matrix multiplication, so the number of rows of the first must be the same as the number of columns of the second matrix.

```julia
X .* B
```

Multiplies elements of `X` and `B` one by one. The *dot operator* works for various mathematical operators by making them *element-wise* - something akin to vectorized operations in R using the `apply()` command family.

### Matrix division

Let's create some matrices as an example:
```julia
A = [1 2; 2 -4]
B = [28, -2]
```

To find `X` such that `A * X = B`, divide `B` by `A`:
```julia
X = A\B
```

### Exercise

A linear regression model is used to find linear relationships between some input variables and an output variable. In other terms, we try to predict a continuous variable using some input variables. For example, if the output variable is y and input variables are x₁, x₂, and x₃ then we want to find the β variables for best fit of y = β₀ + β₁x₁ + β₂x₂ + β₃x₃ or in matrix form y = βX.

Assume we have 100 observations of inputs and output. There are three input variables. The matrix of xs is X (100x3):
```julia
X = rand(Float64, (100,3))
```
The vector of the outputs is y which has length 100:
```julia
y = rand(100)
```

A shortcut to calculate the optimum β is calculated by using the formula β = (X'X)⁻¹X'y.

Write this formula in Julia to find β. 

<details open>
  <summary>Solution</summary>
  Note that the multiplier of β₀ is actually 1.

  y = β₀.1 + β₁x₁ + β₂x₂ + β₃x₃

  So, we should add a column of ones to the matrix as the first column.
  ```julia
  X = [ones(100) X]
  ```
  Now we can write the formula.
  ```julia
  β = inv(X'X)X'y
  ```
</details>

This exercise comes from the [Udemy course "Programming with Julia" by Dr. İlker Arslan](https://www.udemy.com/course/programming-with-julia/)

## 4. Types and dispatch

In Julia, you don't have to define the types of variables. This is similar like in R or Python, but in all languages you will soon notice that some functions don't work on all types, or work the wrong way. For example, `"a"` and `a` might look similar, but in all of these languages it will be processed differently.

Check the type of `1.0`:
```julia
typeof(1.0)
```

Earlier we created arrays with a specific type. You can create objects that have type `Any` but sometimes you want just a specific selection of types. Then you can list the types allowed for your objects using a `Union` type:
```julia
my_custom_type = Union{Integer, String}
x = "Geoscience"
y = "100"
z = 1.0
```

Now you can check if the variables `x`, `y` and `z` we just created fall into your custom type:
```julia
x::my_custom_type
```

Which one throws an error?

Julia has a hierarchical system of types. So you can define functions for more specific types or more general. If you define a function for a general type, for example all numbers, it will work for all sub-types of the type `Number`. You don't need to be specific about the level of the type, because every Julia command (every function call) will be compiled **for that specific type that was used**. 

For example, the function `abs()` is defined for multiple types, and does different things depending on the type of the variable. You can see what types it is defined for:

```julia
methods(abs)
```

But a different code will be in fact executed depending on what parameter you call the function with. You can see it using the macro `@code_typed` which gives you what will *in fact* be done for the respective argument:

```julia
@code_typed abs(-100)
```
That will execute a different function than:
```julia
@code_typed abs(-100.0)
```
So multiple dispatch means that the best function can be chosen for a given situation, but the user only needs to remember one function and not worry about the types. 

Incidentally, a function may have different methods because of speed, e.g. when there are different methods of calculating values for different types of arguments. So you can check how long the execution took using the package `BenchmarkTools`.

```julia
@btime abs(-100)
@btime abs(-100.0)
```

#### Single dispatch: The gamma function

In the presentation, you saw adding a simpler method to the existing function `gamma()` from the package `SpecialFunctions`. You can check if that indeed gained you anything at all, using the `BenchmarkTools` package:

```julia
import SpecialFunctions:gamma
using BenchmarkTools
```

First see what methods are already defined for `gamma()`:

```julia
methods(gamma)
```
The function already has a method for a *union* of types that includes integers: 

```
 [5] gamma(n::Union{Int16, Int32, Int64, Int8, UInt16, UInt32, UInt64, UInt8})
     @ ~/.julia/packages/SpecialFunctions/QH8rV/src/gamma.jl:569
```

but we can assume that it is probably something more complicated than a factorial (fortunately all Julia packages are written in Julia so you can check the code of the function if you're curious!). 

Now add another methods for integers:

```julia
gamma( x :: Int ) = x > 0 ? factorial(x-1) : Inf
```

and check if this method is faster for integers:

```julia
@btime gamma(15.0)
@btime gamma(15)
```

The second line will use the method you defined for integers. Is it faster on your computer?

This example comes from the blog [MatecDev by Martin D. Maas](https://www.matecdev.com/posts/julia-multiple-dispatch.html). You can find more examples of multiple dispatch there.

#### Multiple dispatch: trivial example

```julia
multi_dispatch( x :: Int, y :: Int ) = x^2 + y^2
multi_dispatch( x :: AbstractFloat, y :: String ) = print("$y = ", x)
multi_dispatch( x :: String) = print("Great string you have here, $x, but I prefer numbers")
```
##### Exercise

Currently, the second method only works for floating point numbers. If you pass an integer and a string as arguments, it will return an error. Change the method so that it handles 1) any number, 2) a pair of boolean (true or false) arguments. You can find names of Julia types in [the manual](https://docs.julialang.org/en/v1/manual/types/).

<details open>
  <summary>1. Any number</summary>
  
  ```julia
  multi_dispatch( x :: Number, y :: String ) = print("$y = ", x, " but we don't know if exactly")
  ```
  What will happen now if we call the function with the first argument `5` and `5.0`?
</details>

<details open>
  <summary>2. Boolean</summary>
  
  ```julia
  multi_dispatch( x :: Bool, y :: Bool ) = print("The first argument is $x, the second is $y")
  ```
  This is just an example but I hope you can come up with a better use of two booleans!
</details>

You can find a longer educational example of Julia's multiple dispatch in [chapter 2.3.3](https://juliadatascience.io/julia_accomplish) of the online book Data Science using Julia by Storopoli, Huijzer and Alonso (2021). If you look for real-life examples, check the `methods()` of common functions, such as `rand()`, `%` or `\` (yes, mathematical operators are also functions!).

#### Julia type tree

You can plot part of Julia's type tree with the following:

```julia
using GraphRecipes, Plots
plot(AbstractFloat, method=:tree, fontsize=10, nodeshape=:rect)
```

And using just ASCII characters in the terminal:

```julia
using AbstractTrees
AbstractTrees.children(d::DataType) = subtypes(d)
print_tree(Integer)
```

This exercise is based on [the solution by Przemyslaw Szufel at StackOverflow](https://stackoverflow.com/a/71526202/17001395), distributed under [the CC BY-SA 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).

## 5. Plotting

Julia has basic plotting capability using `Plots.jl`. That is comparable to `plot()` in base R. It's quick.
There are several other plotting ecosystems for Julia, akin to the `ggplot` family. There is a Julia version of Plotly. A Julia-specific and most intensively developed plotting tool is [Makie.jl](https://docs.makie.org/stable/), which contains in fact several packages, depending on whether you want to only plot in 2D, in 3D, for the web, or something even more specific.

### Simple example

```julia
using Plots

x = range(0, 10, length=100)
y1 = sin.(x) # note the dot operator discussed earlier!
y2 = cos.(x)
plot(x, y)
```
Exercise:
plot the parabola x³ for x values of [0, 1]. 

<details open>
  <summary>Solution</summary>
  
  ```julia
  x = range(0, 1, step = 0.1)
  y = x.^3
  plot(x, y)
  ```
</details>

`plot()` is a function name used by many packages. If you have Makie loaded, Julia may not know if you want to use `plot()` from `Plots` or from `Makie`. You can tell it by prepending the name of the package: `Plots.plot(x, y)`. That may be a good practice in general, it certainly is in R!

### Intermediate example

Plot a polynomial approximation of $sin(x)$ employing Unicode characters to label axes and legends. This example comes from [the Makie tutorial](https://github.com/MakieOrg/Makie.jl#a-more-complex-plot-with-unicode-characters-and-latex-strings).

Installing and opening `GLMakie` might take a minute or so, depending on your computer and other Julia packages you already have.

```julia
using GLMakie

x = -2pi:0.1:2pi
approx = fill(0.0, length(x))
cmap = [:gold, :deepskyblue3, :orangered, "#e82051"]
with_theme(palette = (; patchcolor = cgrad(cmap, alpha=0.45))) do
    fig, axis, lineplot = lines(x, sin.(x); label = L"sin(x)", linewidth = 3, color = :black,
        axis = (; title = "Polynomial approximation of sin(x)",
            xgridstyle = :dash, ygridstyle = :dash,
            xticksize = 10, yticksize = 10, xtickalign = 1, ytickalign = 1,
            xticks = (-π:π/2:π, ["π", "-π/2", "0", "π/2", "π"])
        ))
    translate!(lineplot, 0, 0, 2) # move line to foreground
    band!(x, sin.(x), approx .+= x; label = L"n = 0")
    band!(x, sin.(x), approx .+= -x .^ 3 / 6; label = L"n = 1")
    band!(x, sin.(x), approx .+= x .^ 5 / 120; label = L"n = 2")
    band!(x, sin.(x), approx .+= -x .^ 7 / 5040; label = L"n = 3")
    limits!(-3.8, 3.8, -1.5, 1.5)
    axislegend(; position = :ct, backgroundcolor = (:white, 0.75), framecolor = :orange)
    fig
end
```

### Advanced example with complex layout

Let's not copy the entire example here, please just take a look at the [Makie layout tutorial](https://docs.makie.org/stable/tutorials/layout-tutorial/).

## 6. Further reading

### Resources for a quick start

* [MATLAB--Python--Julia cheatsheet](https://cheatsheets.quantecon.org/)
* [Julia track on Exercism](https://exercism.org/tracks/julia)

### Prose and code examples explaining how Julia compares to other languages

* [Julia vs Numba and Cython: Looking Beyond Microbenchmarks](https://www.matecdev.com/posts/julia-python-numba-cython.html)
* [How to solve the same numerical Problem in 7 different Programming Languages](https://medium.com/@andreaskuhn92/how-to-solve-the-same-numerical-problem-in-7-different-programming-languages-a64daac3ed64) - these examples may not necessarily be the fastest code possible in the respective languages

### Trivia

* [Multiple dispatch explained with Pokemon](https://www.moll.dev/projects/effective-multi-dispatch/), a bit too complicated for this demo