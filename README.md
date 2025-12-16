# BioAMLA Datasets

## Annotated Datasets

- [audio/scp-frogs-small](audio/scp-frogs/): A very small audio set built for environmental sound analyis at Steele Creek Park in Bristol TN. Currently consisting of 11 species of frogs. Initially built to test workflows for the bioamla package

- [audio/scp-frogs-inat-v1](audio/scp-frogs-inat-v1/): A larger frog dataset pulled from iNaturalist for Steele Creek Park. This dataset has not been edited and contains mixed length files.

## Externally Hosted Raw Data

- [Steele Creek Park Wetlands, Bristol, TN 2023](external/steele-creek-park-2023-raw/README.md) : 
This raw audio dataset contains 2822 wav/mp3 files collected from five locations in Steele Creek Park from Feb. through Sept. 2023.
- [Braulio Carillo National Park/ La Selva Research Station, Costa Rica 2024](external/costa-rica-2024-raw/README) :
This raw audio dataset contains 601 wav/mp3 files (600 hours) collected from five locations at Braulio Carillo National Park, Costa Rica from July 9th - 24th, 2024.

## Licenses

All metadata files in this repository contain licensing and attribution for audio files and were generated using the bioamla package

``` bash
bioamla dataset license ./audio/esc-50/ --metadata-filename metadata.csv -t ./templates/esc50_license_template -o LICENSE
```
