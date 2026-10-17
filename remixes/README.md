# Remixes

A remix is a dataset derived from one of the datasets here, usually ESC-50,
by dropping classes, adding classes, or swapping a class's examples. Each
remix is a small TOML recipe in this directory, rebuilt on demand with
`make remix NAME=<recipe>`, which writes `build/<recipe>/`. The built audio
is never committed; only the recipe is.

Recipes are read by `bioamla dataset remix`. Relative paths inside a recipe
are resolved against this directory, so `../datasets/esc-50` is the ESC-50 copy.

## Recipe format

```toml
[remix]
name = "esc-50-animals"            # output dataset name (reporting only)
source = "../datasets/esc-50"      # base dataset (has metadata.csv)
# label_column = "category"        # optional; auto-detects label, then category

# Pick one of keep / drop. `keep` removes every class not named;
# `drop` removes only the classes named.
keep = ["dog", "cat", "frog"]
# drop = ["airplane", "helicopter"]

# Add a class from a directory of clips with its own metadata.csv.
# [[add]]
# label = "spring_peeper"
# source = "../build/spring-peeper-clips"
# max_clips = 40

# Replace a class's examples with clips from another directory.
# [[replace]]
# label = "frog"
# source = "../build/frog-clips"
```

The output keeps the source's metadata columns, so the `attr_*` attribution
columns carry through and a `LICENSE` is generated for every remix.
