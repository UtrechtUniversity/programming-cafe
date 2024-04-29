# Contributing

## Slides & Exercises

All slides and exercises are stored in the `presentations` directory, which can be found at the root of the Programming Cafe GitHub repository.

When preparing a presentation for the Programming Cafe, we request you organize your materials in the following manner:

### HTML

```
YYYY-MM-DD_short-title-of-your-presentation
    |_ exercises -> _additional sub-directories are possible if you want to provide materials to participants etc._
        |_ YYYY-MM-DD_exercises.md
    |_ slides -> _additional sub-directories are possible to organize images etc._
        |_ YYYY-MM-DD_short-title-of-your-presentation.html
        |_ YYYY-MM-DD_short-title-of-your-presentation.qmd -> _if using Quarto to build slides, hint: use the embed-resources: true function_
```

### PDF 

```
YYYY-MM-DD_short-title-of-your-presentation
    |_ exercises
        |_ YYYY-MM-DD_exercises.md
    |_ slides
        |_ YYYY-MM-DD_short-title-of-your-presentation.pdf
```

You're welcome to open a pull request to add your contribution to the `presentations` directory. Alternatively, you can provide the organizers with a zipped folder which they can eventually upload to GitHub.

When the website is ready to updated, the slide deck in HTML or PDF format will copied to `site/static/` where it will be embedded in the blog post related to the presentation. 

