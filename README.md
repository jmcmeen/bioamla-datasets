# BioAMLA Datasets

Environmental audio datasets for bioacoustics research and machine learning,
supporting the [bioamla](https://github.com/jmcmeen/bioamla) package. This
repo is the working copy for building, remixing, and publishing datasets with
the `bioamla dataset` commands; most audio lives elsewhere (Hugging Face,
Google Drive) and the directories here hold metadata and pointers.

## Layout

```text
bioamla-datasets/
├── datasets/
│   ├── esc-50/                      # 2,000 clips, 50 classes; audio in git LFS
│   ├── scp-frogs-inat-v1/           # metadata only; audio on Hugging Face
│   ├── steele-creek-park-2023-raw/  # README only; audio on Google Drive
│   └── costa-rica-2024-raw/         # README only; audio on Google Drive / HF
├── remixes/                         # recipes for datasets derived from esc-50
├── templates/                       # headers for generated LICENSE files
└── Makefile                         # thin wrappers over `bioamla dataset ...`
```

| Dataset | Audio | Size | Licence |
| --- | --- | --- | --- |
| [ESC-50](datasets/esc-50/) | here (LFS) | 2,000 five-second clips, 50 classes | CC BY-NC 3.0, per-clip attribution in `metadata.csv` |
| [SCP Frogs iNat v1](datasets/scp-frogs-inat-v1/) | [Hugging Face](https://huggingface.co/datasets/bioamla/scp-frogs-inat-v1) | 1,087 clips, 11 frog species | Mixed CC-BY-NC / CC-BY / CC0, per clip |
| [Steele Creek Park 2023](datasets/steele-creek-park-2023-raw/) | Google Drive | 2,282 files, ~2,809 h | CC BY-NC 4.0 |
| [Braulio Carrillo / La Selva 2024](datasets/costa-rica-2024-raw/) | Google Drive, [Hugging Face](https://huggingface.co/datasets/bioamla/costa-rica) | 601 files, ~600 h | CC BY-NC 4.0 |

Every dataset directory has a `README.md`. Those with clips also have a
`metadata.csv` (one row per clip, with `attr_id`, `attr_lic`, `attr_url`,
`attr_note` attribution columns) and a generated `LICENSE`.

## Cloning

Audio is stored with [Git LFS](https://git-lfs.com/). Install it before
cloning or the wav files come down as small pointer files:

```sh
brew install git-lfs && git lfs install
git clone https://github.com/jmcmeen/bioamla-datasets.git   # ~850 MB of LFS objects
```

To clone the metadata without the audio: `GIT_LFS_SKIP_SMUDGE=1 git clone ...`,
then `git lfs pull -I "datasets/esc-50/dog/*"` for just the parts you need.

## Working with the datasets

Install bioamla, then use the Makefile (run `make` to list targets):

```sh
pip install "bioamla[cli]"
make stats DS=esc-50          # summary of a dataset's metadata.csv
make license DS=esc-50        # regenerate datasets/esc-50/LICENSE from metadata
make manifest DS=esc-50       # write datasets/esc-50/dataset.json
make push DS=esc-50           # push a dataset directory to huggingface.co/bioamla
make remix NAME=esc-50-animals  # build build/esc-50-animals from remixes/esc-50-animals.toml
```

Set `BIOAMLA='uv run --project /path/to/bioamla bioamla'` to use a
development checkout of bioamla instead of the installed package.

### Remixes

`remixes/` holds small recipe files describing datasets derived from ESC-50:
classes dropped or added, examples replaced. See
[remixes/README.md](remixes/README.md). A remix is rebuilt from its recipe
into the ignored `build/` directory, so derived audio never enters git.


## Acknowledgements

ESC-50 is used under CC BY-NC 3.0. If you use it, please cite:

> K. J. Piczak. **ESC: Dataset for Environmental Sound Classification**.
> *Proceedings of the 23rd ACM International Conference on Multimedia*,
> Brisbane, Australia, 2015. DOI: [10.1145/2733373.2806390](http://dx.doi.org/10.1145/2733373.2806390)

The copy here was built from the Hugging Face mirror
[ashraq/esc50](https://huggingface.co/datasets/ashraq/esc50), published by
[ashraq](https://huggingface.co/ashraq). Its clips derive from recordings shared on
[Freesound.org](https://freesound.org/); full attribution is in
[datasets/esc-50/LICENSE](datasets/esc-50/LICENSE).
The iNaturalist clips are credited per recordist in that dataset's
`metadata.csv` and `LICENSE`.

## Related

- [bioamla](https://github.com/jmcmeen/bioamla), the Python package these datasets feed
- [bioamla-hub](https://github.com/jmcmeen/bioamla-hub), resources on bioacoustics and machine learning
- [frogs-of-steele-creek](https://github.com/jmcmeen/frogs-of-steele-creek), frog identification at Steele Creek Park
