---
layout: default
title: pytest-autofocus
---

# pytest-autofocus

<p class="tagline">Fast, focused feedback</p>

<div class="hero-code">
{% highlight python %}
@pytest.mark.focus
def test_the_thing_im_working_on():
    assert magic() == True
{% endhighlight %}
</div>

## Healthy code requires exercise

The earlier and more frequently your code runs, the better. You're using an automated test runner, right? `pytest-autofocus` is a pytest plugin intended to be used with an automated test runner like [pytest-watcher](https://github.com/olzhasar/pytest-watcher):

```bash
ptw . -- --auto-focus
```

## The problem

You're iterating on a feature. Your intuition says something is off in the `is_valid` function. You want to focus on just one test. Right now that means restarting the watcher with marker arguments or a path filter, leaving your editor - requiring a context switch.

## The solution

Once installed, just add `@pytest.mark.focus` to any test and click save. Move the decorator or add it to more tests. Remove them when you're done and the full suite runs again.

```python
@pytest.mark.focus
def test_is_valid():
    assert is_valid(data) == expected
```

Never leave your editor. Never restart the watcher. Ergonomic, focused, feedback when you need it.

## Install

<div class="install">pip install pytest-autofocus pytest-watcher</div>

<div class="video-placeholder">
  Video coming soon
</div>

