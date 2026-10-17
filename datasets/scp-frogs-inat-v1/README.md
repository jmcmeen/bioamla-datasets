# SCP Frogs iNaturalist v1

1,087 frog recordings from iNaturalist observations near Steele Creek Park,
Bristol, TN, covering 11 species. The files are unedited and of mixed length.

**The audio is not in this repo.** It lives on Hugging Face:

- https://huggingface.co/datasets/bioamla/scp-frogs-inat-v1

```python
from datasets import load_dataset
ds = load_dataset("bioamla/scp-frogs-inat-v1", split="train")
```

This directory keeps `metadata.csv` (one row per clip, same columns as the
HF dataset) and `LICENSE` (per-clip attribution).

## Licence

Each clip carries the licence its iNaturalist recordist chose, recorded in
the `attr_lic` column:

| Licence | Clips |
| --- | ---: |
| CC BY-NC | 957 |
| CC BY | 115 |
| CC0 | 15 |

Because most clips are CC BY-NC, the dataset as a whole is
**CC BY-NC 4.0** with per-clip attribution. Credit the recordist named in
`attr_id` and link `attr_url` when redistributing. A CC-BY/CC0-only subset
could be published under CC BY if a commercial-use version is needed.

## Species

| target (iNat taxon) | label |
| --- | --- |
| 64968 | anaxyrus_americanus |
| 64977 | anaxyrus_fowleri |
| 23930 | hyla_chrysoscelis |
| 65979 | lithobates_catesbeianus |
| 65982 | lithobates_clamitans |
| 66002 | lithobates_palustris |
| 60341 | lithobates_sphenocephalus |
| 66012 | lithobates_sylvaticus |
| 24256 | pseudacris_brachyphona |
| 24268 | pseudacris_crucifer |
| 24263 | pseudacris_feriarum |
