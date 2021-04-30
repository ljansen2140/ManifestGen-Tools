# ManifestGen-Tools
Used for generating manifests for the VAE_V2

This code is provided as is and with minimal documentation. This serves purely as a reference for how to generate manifests that are compatible with VAE_V2.

## genman.py

This file takes the manifest from IARPA's FMoW dataset and selects image locations to be added to a general manifest. Only a relative filepath is selected here, so an absolute one must be supplied later. This can be used as a standalone manifest generator if this relative filepath is converted to an abolsute one.

## copy_local.py

This file copies FMoW images and normalizes them, while also generating a manifest to their new location. The generated manifest is compatible with VAE_V2. Note that normalization is required for VAE_V2 to work.


## Usage

Genman is used first to select images from the IARPA dataset. Copy_local should then be used to move the images as needed. Variables will need to be altered depending on the desired output directories.

It is recommended to edit the variables: `directory, train_loc, val_loc, man_loc` in `copy_local.py` in order to specify your own directory structure.
