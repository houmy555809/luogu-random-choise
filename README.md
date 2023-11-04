# luogu-random-choise
Randomly choose a problem in <https://luogu.com.cn>

### About
With this program, you can randomly choose an existing problem in luogu. You can also customize your preferences.

### How to use
Download the source code and run `main.py`. Enter your customizations in Python grammar. If no customization needed, simply enter `True`. Here are some variables you can use:

- difficulty: One-digit difficulty from 0(grey) to 7(black).
- accepted: An integer that indicates how many people accepted this problem.
- submit: An integer that shows how many submissions does the problem has.
- acrate: An integer from 0 to 100 that shows the AC rate of the problem in percentage. Specially, if there are no submissions, it is `None`.
- translation: A boolean indicating does the problem needs translations.
- tag: An array that contains all tags of the problem in integer.

For example, if you want to search for green problems that requires segment tree, search for:

```
difficulty==4 and 42 in tag
```

If the data is outdated, run `download.py`. It may need 6 or 7 hours to fetch the whole problemset. This program helps you to update the data by updating the database. You can modify them by hand if you want. The database contains:

- `accepted.txt` for variable `accepted`
- `acrate.txt` for variable `acrate`
- `difficulty.txt` for variable `difficulty`
- `submit.txt` for variable `submit`
- `tag.txt` for array `tag`
- `translation.txt` for variable `translation`

They are all in value-key format. For example, the first line of `submit.txt` is:

```
990434 P1000
```

This indicates that `P1000` has 990434 submissions.
