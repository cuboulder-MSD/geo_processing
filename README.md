# geo_processing

This repository contains code for working with MODS records for the Colorado Geolibrary. A workflow for new datasets is provided below.

## addARK.py

Legacy code that added ARKs to mods files. Kept here to be tweaked for other needs.

## addRights.py

Similar to addARK.py, it was necessary to make a global edit to the rights statement. This code could be adjusted for other global edits.

## cleanGeo.py

Script that also could be tweaked to change fields. Current iteration added a publisher and changed the form.

## geo2mods.py

This is the main script to convert the original geospatial metadata to MODS.

## geo2mods_blm.py

An iteration of `geo2mods.py` specific to metadata from BLM. Retained as an example of how to adjust the original script to unique needs of a particular data source.


# Geospatial to MODS workflow

1. Navigate to the geospatial dataset
2. Run `python geo2mods.py [metadata file]`
3. In a perfect world that script will run perfectly. This is not that world. Open the script and change it to around/adjust for the elements you need to find. 
Do this until you get an output that works.
4. Make a copy of the MODS(m1) file and store it outside the dataset.
5. Zip the dataset *with* the other MODS(m2) file.
6. Load the dataset in Geoloader. 
7. Crosswalk the metadata from the MODS file.
8. Insert the minted ARK into m1 `<mods:identifier type='ark'>new ark</mods:identifier>`.
9. Finish the Geoloader process.
10. Add m1 to https://github.com/cuboulder-MSD/geolibrary
