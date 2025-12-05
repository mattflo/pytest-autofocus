---
layout: default
title: pytest-autofocus
---

# pytest-autofocus

<p class="tagline">Fast, focused feedback</p>


Healthy code requires exercise. The earlier and more frequently your code runs, the better. You use an automated test runner, right? `pytest-autofocus` is a pytest plugin intended to be used with an automated test runner like [pytest-watcher](https://github.com/olzhasar/pytest-watcher):

## The problem

You're iterating on a feature but it's not quite working yet. Your intuition says something is off in the `is_valid` function. You want to focus on just those test(s). Right now that means restarting the watcher with a path filter or marker arguments and adding a decorator. 

## The solution

In a perfect world, all you have to do is add `@pytest.mark.focus` to any test and save. Move the decorator or add it to more tests. Remove when done and the full test suite runs again.

```python
@pytest.mark.focus
def test_is_valid():
    assert is_valid(data) == expected
```

Never leave your editor. Never restart the watcher. Ergonomic, focused, granular feedback right when you need it.

## But AI

If all your code is written by background agents and humans never look at code directly, this tool isn't for you. Also of note, this tool is intended to be used directly humans not by AI agents.

## Install

<div class="install">pip install pytest-autofocus pytest-watcher</div>

## Usage

In the terminal, run:

```bash
ptw . -- --auto-focus
```
Just add `@pytest.mark.focus` to the desired test(s).

<div class="hero-code">
{% highlight python %}
@pytest.mark.focus
def test_the_thing_im_working_on():
    assert magic() == True
{% endhighlight %}
</div>
