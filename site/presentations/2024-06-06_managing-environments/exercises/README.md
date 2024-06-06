# Using virtual environments
Virtual environments are very useful in order to avoid breaking dependencies across projects and improve reusability of your code. Multiple options are available in for each language and for each purpose. For this session, we will focus on the most commonly used solutions in Python and R: Venv, Renv, Conda, Docker and chroot.

## [Venv for Python](https://docs.python.org/3/library/venv.html) (beginner)
You can find more information on the use of Venv [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/). In this part we will try to install an open source chatbot that will run on you own machine. For that, we will use the software [GPT4All](https://github.com/nomic-ai/gpt4all) that is open source and optimized to run with or without a GPU on your computer. A desktop application is available for this software (that is really great) but we will use the [Python version](https://github.com/nomic-ai/gpt4all/tree/main/gpt4all-bindings/python) for this tutorial.

1. If not already installed, you can download and install Python from [here](https://www.python.org/downloads/)
2. Create a folder called GPT4All
3. Open a terminal in this folder and create a new environment  
* Linux/Mac `python -m venv .venv`
* Windows `py -m venv .venv`    
5. Activate your new environment
* Linux/Mac `source .venv/bin/activate`
* Windows `.venv\Scripts\activate`
6. Check that your terminal now shows `(.venv)`
7. Install GPT4All using `pip install gpt4all typer`
8. Download this [file](https://github.com/nomic-ai/gpt4all/blob/main/gpt4all-bindings/cli/app.py)
9. Run the chatbot
* Linux/Mac `python app.py repl`
* Windows `py app.py repl`

You just installed and ran your own chatbot in a virtual environment.

## [Renv for R](https://rstudio.github.io/renv/) (beginner)
You can find more information on the use of Renv [here](https://rstudio.github.io/renv/). In this part we will try to install the library [NetworkD3](https://christophergandrud.github.io/networkD3/) that is used to display graph networks. 

1. If not already installed, you can download and install R and RStudio from [here](https://posit.co/download/rstudio-desktop/).
2. Create a new project in a new folder called NetworkD3
3. Open the console of RStudio and install Renv `install.packages("renv")`
4. Activate your new environment `renv::init()`
5. Install NetworkD3 `install.packages("networkD3")`
6. Run the following code

```r
# Load package
library(networkD3)

# Create fake data
src <- c("A", "A", "A", "A",
        "B", "B", "C", "C", "D")
target <- c("B", "C", "D", "J",
            "E", "F", "G", "H", "I")
networkData <- data.frame(src, target)

# Plot
simpleNetwork(networkData)
```

Now you can see a folder called renv in you project that contains all the installed packages

## [Conda](https://www.anaconda.com/download) (beginner)
Aside from the language-specific environments, a very popular solution in data-science is [Conda](https://www.anaconda.com/download). In this part, we will use a [Jupyter Notebook](https://docs.anaconda.com/free/navigator/tutorials/r-lang/) for data processing in R.

## [Docker](https://docs.docker.com/get-started/) and [chroot](https://www.howtogeek.com/441534/how-to-use-the-chroot-command-on-linux/) (advanced)
For more complex dependencies across mutliple languages and compatibility accross OS, [Docker](https://docs.docker.com/get-started/) is the most used solution. Other solutions offer the same advantages like [Podman](https://podman.io/). For this part, we will follow the tutorial of [Docker](https://docs.docker.com/get-started/) and try to understand what is happening when using Docker. Additionnally, you can try to run the community edition of [Overleaf](https://github.com/overleaf/overleaf) on your machine.

As a light-weight alternative to containers when needing to run unknown code on a Linux machine, [chroot](https://www.howtogeek.com/441534/how-to-use-the-chroot-command-on-linux/) is a good choice. For example, chroot is used to securely run students code handed out for programming assignments in an automatic way on our instance of [DOMjudge](https://domjudge.uu.nl/). 
