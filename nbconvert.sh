#!/bin/bash
rm -f Enterprise_ML_Part_II.slides.html && jupyter nbconvert --to slides Enterprise_ML_Part_II.ipynb \
--post serve \
--SlidesExporter.reveal_scroll=True \
--SlidesExporter.reveal_transition=none  \
--SlidesExporter.reveal_theme=sky
