# Braulio Carillo National Park / La Selva Research Station 2024

This audio dataset contains 601 audio files (~600 hours) collected from five locations at Braulio Carillo National Park and La Selva Research Station, Costa Rica during July 2024. The audio was captured using Wildlife Acoustics Song Meter Micro devices. This dataset contains various species of birds, frogs, and other vocalizing taxa. In some areas of La Selva, audio was captured in publicly accessible areas and thus contains other ambient sounds such as people or vehicles.

The original dataset is currently hosted on Google Drive (<a href="https://drive.google.com/drive/folders/1Zfttms73TA-HYK5DFD8o0eZpfvRn_ATe?usp=drive_link">BioAMLA-Costa-Rica-2024</a>). The raw uncompressed audio is in wav format (44.1 KHz, 16-bit depth, mono). A compressed version is also available in mp3 format.

A resampled (44.1 KHz, 16-bit depth, mono) version of this dataset lives on Hugging Face [bioamla/costa-rica](https://huggingface.co/datasets/bioamla/costa-rica).

## Locations

Coordinates are rounded to 0.01° (about 1 km).

- La Selva Research Station 
  - Research Swamp (10.43°N, 84.01°W)
  - CCA Trail (10.43°N, 84.00°W)
  - CCC Trail (10.43°N, 84.01°W)
- Braulio Carillo National Park
  - El Ceibo Site 1 (10.33°N, 84.08°W)
  - El Ceibo Site 2 (10.32°N, 84.07°W)

## Known Issues

- Wildlife Acoustics embedded GPS metadata in the original wav files is not accurate. GPS coordinates in the accompanying recorder log is accurate. A script is being developed to fix this in the wav version of the dataset and will be shared here along with the updated data.
