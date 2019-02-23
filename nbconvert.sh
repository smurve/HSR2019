#!/bin/bash
rm Enterprise_ML_Part_I.slides.html && jupyter nbconvert --to slides Enterprise_ML_Part_I.ipynb \
--post serve \
--SlidesExporter.reveal_scroll=True \
--SlidesExporter.reveal_transition=none  \
--SlidesExporter.reveal_theme=sky
