# Julia installation

Julia default [installation instructions](https://julialang.org/downloads/) include `juliaup`, a handy manager that allows you to switch Julia versions and set the default one for your system. It has the same purpose as `pyenv`.

For this exercise, you just need one version, let's make it the latest: Julia 1.10.0 But if you want to see if you have other Julia installs on your computer, or what else you can do, just type 

```
juliaup
```

This will return a list of commands with explanations.

Once you've installed Julia, you can use it without further ado. Just type `julia` in the terminal. You quit using `exit()`.

# VS Code Installation

[Visual Studio Code](https://code.visualstudio.com/) is popular and Julia community is very active in developing a Julia Extension for this IDE. Usually the website identifies your system and [offers the right download](https://code.visualstudio.com/Download). You can add the [Julia Extension](https://marketplace.visualstudio.com/items?itemName=julialang.language-julia) from within VS Code once it is running on your computer. It will use the Julia installation that is in your `PATH`, which is usually what has been set by `juliaup`.

If you are reluctant to install VS Code because of its tracking options, you can use [VS Codium](https://vscodium.com/). It is the same IDE, but without tracking (for what it's worth). I do not know how it affects work with Julia Extension, but [tracking in the extension is disabled, unless you opt in](https://github.com/julia-vscode/julia-vscode/wiki/Privacy-Policy).

