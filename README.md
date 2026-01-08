# BioAMLA Datasets

A curated collection of environmental audio datasets for bioacoustics research and machine learning. This repository supports the [BioAMLA](https://github.com/jmcmeen/bioamla) project with labeled datasets for training environmental sound classification and species identification models.

## Repository Structure

```text
bioamla-datasets/
├── audio/                           # Annotated/curated audio datasets
│   ├── esc-50/                      # 2,000 environmental sounds, 50 categories
│   ├── scp-frogs-small/             # 110 frog recordings, 11 species
│   └── scp-frogs-inat-v1/           # 1,087 frog recordings from iNaturalist / raw/labeled             
│   ├── steele-creek-park-2023-raw/  # Raw/externally hosted dataset
│   └── costa-rica-2024-raw/  # Raw/externally hosted dataset
└── templates/                # License attribution templates
```

## Annotated Datasets

| Dataset | Size | Description | License |
|---------|------|-------------|---------|
| [ESC-50](audio/esc-50/) | 2,000 clips | Environmental Sound Classification - 50 categories across animals, nature, human sounds, domestic, and urban noises. 5-second clips at 44.1 kHz. | CC-BY-NC 3.0 |
| [SCP Frogs Small](audio/scp-frogs-small/) | 110 clips | 11 frog species from Steele Creek Park, Bristol, TN. Built for testing BioAMLA workflows. | CC-BY-4.0 |
| [SCP Frogs iNat v1](audio/scp-frogs-inat-v1/) | 1,087 clips | Frog recordings from iNaturalist for Steele Creek Park. Mixed-length, unedited files. | CC-BY-4.0 |
| [Steele Creek Park 2023](audio/steele-creek-park-2023-raw/README.md) | 2,822 files (~2,809 hours) | Field recordings from 5 locations in Bristol, TN.Feb-Sept 2023. | CC-BY-NC 4.0 |
| [Braulio Carillo / La Selva 2024](audio/costa-rica-2024-raw/README.md) | 601 files (~600 hours) | Field recordings from 5 locations in Costa Rica. July 2024. | CC-BY-NC 4.0 |

## Getting Started

Install the bioamla package to work with these datasets:

```bash
pip install bioamla
```

## Licenses

All metadata files contain licensing and attribution information which can be used to generate a LICENSE file using the bioamla package. Please refer to each dataset's license before use.

```bash
bioamla dataset license ./audio/esc-50/ --metadata-filename metadata.csv -t ./templates/esc50_license_template -o LICENSE
```

## Acknowledgements

The ESC-50 dataset is used under the Creative Commons Attribution-NonCommercial 3.0 license. If you use this dataset, please cite:

> K. J. Piczak. **ESC: Dataset for Environmental Sound Classification**. *Proceedings of the 23rd ACM International Conference on Multimedia*, Brisbane, Australia, 2015.
>
> DOI: [10.1145/2733373.2806390](http://dx.doi.org/10.1145/2733373.2806390)

The audio clips in ESC-50 are derived from recordings shared on [Freesound.org](https://freesound.org/). Full attribution details are available in [audio/esc-50/LICENSE](audio/esc-50/LICENSE).

## Related Projects

- [bioamla-hub](https://github.com/jmcmeen/bioamla-hub) - Resources for learning more about bioacoustics and machine learning.
- [bioamla](https://github.com/jmcmeen/bioamla) - Python package for bioacoustics machine learning
- [frogs-of-steele-creek](https://github.com/jmcmeen/frogs-of-steele-creek) - Frog species identification project for Steele Creek Park
- [riffy](https://github.com/jmcmeen/riffy) - Audio file utilities
