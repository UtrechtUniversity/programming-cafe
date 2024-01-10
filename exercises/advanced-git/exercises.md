# New to git?

If you're completely new to git, or need to refresh your memory, just start with [the basics](https://coderefinery.github.io/git-intro/basics/)!

# Beginners

If you're a beginner, we recommend that you do the following exercises/tutorials from the CodeRefinery course [Introduction to version control with Git](https://coderefinery.github.io/git-intro/):

1. [Branching](https://coderefinery.github.io/git-intro/branches/)
1. [Conflict resolution](https://coderefinery.github.io/git-intro/conflicts/)
1. [Pull Requests](https://coderefinery.github.io/git-intro/remotes/)
1. [The Staging Area](https://coderefinery.github.io/git-intro/staging-area/#staging-area-commands)

Clone [this repository](https://github.com/dometto/git-tutorial-testrepo) to do the exercises in.


If you have time left, proceed with the exercises from the Intermediate/Advanced section below, focusing on the following:

1. [Exercise2 Staging and Stashing](#Exercise2-Staging-and-Stashing)
1. [Exercise7 RebaseAndAmend](#Exercise7-RebaseAndAmend)
1. [Exercise4 Merging and ReReRe](#Exercise4-Merging-and-ReReRe)

# Intermediate/Advanced

If you are a more advanced `git` user and are already familiar with the concepts of branching and merging, we recommend that you pick exercises from the [[Advanced Git In Depth](https://github.com/nnja/advanced-git/tree/master/exercises) course by Nina Zakharenko that cover topics you don't know yet.

**Use the following repository to complete the exercises: https://github.com/nnja/advanced-git-exercises **

We recommend first picking the exercises listed below. For some of these topics, we've also added additional challenges!

## Exercise1 SimpleCommit

https://github.com/nnja/advanced-git/blob/master/exercises/Exercise1-SimpleCommit.md

Learn about git's internals by inspecting a commit under the hood.

### Additional exercises

1. Create a subdirectory `subdir` and create a file `hello2.txt` in it, with content such as `Hello to you too!`.
2. Commit `subdir/hello2.txt`

Now, using just the following three commands, can you output the contents of the file you just committed, `hello2.txt`?

* `git log`
* `git ls-tree`
* `git cat-file blob`

## Exercise2 Staging and Stashing

https://github.com/nnja/advanced-git/blob/master/exercises/Exercise2-StagingAndStashing.md

Learn to exercise precise control what is added to your commits, with `git add -p` and `git stash`.

### Additional exercise

Can you figure out how to use `git stash` to stash *everything that is not staged for commit*? (Hint: you'll need to pass two options to `git stash`). [Solution](git stash --keep-index --include-untracked https://calebhearth.com/stash-what-git-wouldnt-commit).

## Exercise7 RebaseAndAmend

https://github.com/nnja/advanced-git/blob/master/exercises/Exercise7-RebaseAndAmend.md

### Additional exercises

1. The exercise in the tutorial has you use `git commit --amend` to change a commit's message. Can you also use `amend` to change the *contents* of the files within the commit?
2. Most difficult: the exercise in the tutorial has you use `rebase -i` to squash some commits. This allows you to combine a number of commits that each contain *too little* to amount to an atomic commit into one. But suppose you have a commit in your history that contains *too much* to amount to an atomic commit -- i.e. a commit that changes two logically distinct bits of code. How can you use `rebase -i` to split this commit into two atomic commits? (Hint: you'll need more commands than just `rebase`). [Solution](https://github.com/kimgr/git-rewrite-guide#split-a-commit).
3. Similarly, can you use `rebase -i` to completely delete an unwanted commit, as well?
4. Oops! You just deleted a commit and it's all gone from your branch. This is one of the ways in which you could (accidentally) lose work while rebasing. But git wouldn't be git if you couldn't undo a rebase. Can you figure out how to restore your previous commit? [Hint](https://git-scm.com/docs/git-reflog) [Solution](https://jvns.ca/blog/2023/11/06/rebasing-what-can-go-wrong-/#undoing-a-rebase-is-hard)

## Exercise4 Merging and ReReRe

https://github.com/nnja/advanced-git/blob/master/exercises/Exercise4-MergingAndReReRe.md

Reuse Recorded Resolution is a feature that lets you automate merge conflict resolution (for similar/recurring merge conflicts). This can be especially handy when rebasing, as [rebasing can require you to solve the same merge conflict multiple times](https://mindup.medium.com/enable-git-rerere-for-easy-merging-303c6f2dacd3)!

## Exercise9 Advanced Tools

https://github.com/nnja/advanced-git/blob/master/exercises/Exercise9-AdvancedTools.md

Notes:

* `cherry-pick` can be very useful for creating atomic git histories. It essentially does the inverse of `rebase`: rather than replaying the changes on the current branch on top of (typically) `main` (rebase), it replays the changes from a commit on a *different* branch on top of the current branch. If your feature branch is a mess, but contains some commits that are nice atomic gems, you may be able to `cherry-pick` the latter on your `main` branch!
* `git bisect` is a great debugging tool, especially when used in its automatic mode in conjunction with unit tests. Give the example [here](https://mlo.io/blog/2020/08/05/debugging-with-git-bisect/) a go!