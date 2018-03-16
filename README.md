# smsh
Stupid module to smoosh lists, as inspired by this tweet:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Proposal: A smoosh function where the number of o’s tells how deep to flatten.<br><br>smoosh([1,[2,[3,[4]]]]) =&gt; [1,2,[3,[4]]]<br>smooosh([1,[2,[3,[4]]]]) =&gt; [1,2,3,[4]]<br>smoooosh([1,[2,[3,[4]]]]) =&gt; [1,2,3,4]</p>&mdash; YAML Clark (@jasonrclark) <a href="https://twitter.com/jasonrclark/status/974449543688339456?ref_src=twsrc%5Etfw">March 16, 2018</a></blockquote>

```python
>>> from smsh import s
>>> s.mosh([1,[2,[3,[4]]]])
[1, [2, [3, [4]]]]
>>> s.moosh([1,[2,[3,[4]]]])
[1, 2, [3, [4]]]
>>> s.mooosh([1,[2,[3,[4]]]])
[1, 2, 3, [4]]
>>> s.moooosh([1,[2,[3,[4]]]])
[1, 2, 3, 4]
```
