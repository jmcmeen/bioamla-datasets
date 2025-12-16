# ESC-50: Dataset for Environmental Sound Classification (Modified)

This is a reorganized copy of the **ESC-50 dataset** created by Karol J. Piczak.

**Original dataset:** https://github.com/karolpiczak/ESC-50

## Dataset Overview

The ESC-50 dataset is a labeled collection of 2000 environmental audio recordings suitable for benchmarking methods of environmental sound classification. The dataset consists of 5-second-long recordings organized into 50 semantic classes (40 examples per class) arranged into 5 major categories:

| Animals | Natural soundscapes & water sounds | Human, non-speech sounds | Interior/domestic sounds | Exterior/urban noises |
| :--- | :--- | :--- | :--- | :--- |
| Dog | Rain | Crying baby | Door knock | Helicopter |
| Rooster | Sea waves | Sneezing | Mouse click | Chainsaw |
| Pig | Crackling fire | Clapping | Keyboard typing | Siren |
| Cow | Crickets | Breathing | Door, wood creaks | Car horn |
| Frog | Chirping birds | Coughing | Can opening | Engine |
| Cat | Water drops | Footsteps | Washing machine | Train |
| Hen | Wind | Laughing | Vacuum cleaner | Church bells |
| Insects (flying) | Pouring water | Brushing teeth | Clock alarm | Airplane |
| Sheep | Toilet flush | Snoring | Clock tick | Fireworks |
| Crow | Thunderstorm | Drinking, sipping | Glass breaking | Hand saw |

Clips were manually extracted from public field recordings on [Freesound.org](http://freesound.org/). The dataset is prearranged into 5 folds for cross-validation.

## Changes from Original

This version has been modified from the original ESC-50 dataset with the following structural changes:

1. **Files organized by category**: Audio files are now organized into subdirectories by category name (e.g., `dog/`, `cat/`, `chainsaw/`) instead of a flat directory structure.

2. **Extended metadata**: The `metadata.csv` file includes four additional attribution columns:
   - `attr_id` - Author/contributor name from Freesound
   - `attr_lic` - License type (CC0, CC-BY, CC-BY-NC, CC-Sampling+, etc.)
   - `attr_url` - Source URL on Freesound
   - `attr_note` - Note about the original source file

3. **Updated file paths**: The `filename` column in `metadata.csv` now contains relative paths including the category folder (e.g., `dog/1-100032-A-0.wav`).

## File Structure

```
esc-50/
├── metadata.csv          # Metadata with attribution fields
├── LICENSE               # Per-clip licensing/attribution details
├── README.md             # This file
├── README_old.md         # Original README
├── dog/                  # Audio files organized by category
│   ├── 1-100032-A-0.wav
│   └── ...
├── cat/
├── chainsaw/
└── ... (50 category folders)
```

## Metadata Format

| filename | fold | target | category | esc10 | src_file | take | attr_id | attr_lic | attr_url | attr_note |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

## License

The dataset is available under the terms of the [Creative Commons Attribution Non-Commercial license](http://creativecommons.org/licenses/by-nc/3.0/).

A smaller subset (clips tagged as *ESC-10* in metadata) is distributed under CC BY (Attribution).

Per-clip attributions are available in the [LICENSE](LICENSE) file.

## Citation

If you use this dataset, please cite the original work:

> K. J. Piczak. **ESC: Dataset for Environmental Sound Classification**. *Proceedings of the 23rd Annual ACM Conference on Multimedia*, Brisbane, Australia, 2015.
>
> DOI: http://dx.doi.org/10.1145/2733373.2806390

```bibtex
@inproceedings{piczak2015dataset,
  title = {{ESC}: {Dataset} for {Environmental Sound Classification}},
  author = {Piczak, Karol J.},
  booktitle = {Proceedings of the 23rd {Annual ACM Conference} on {Multimedia}},
  date = {2015-10-13},
  url = {http://dl.acm.org/citation.cfm?doid=2733373.2806390},
  doi = {10.1145/2733373.2806390},
  location = {{Brisbane, Australia}},
  isbn = {978-1-4503-3459-4},
  publisher = {{ACM Press}},
  pages = {1015--1018}
}
```
