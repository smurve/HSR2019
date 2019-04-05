# How to generate slides for printing as a PDF

(This is also how the PDF in this directory was created.)

1. [install nbconvert](https://nbconvert.readthedocs.io/en/latest/install.html)
2. From this repository's root directory (the directory above this one), run
   ```bash
   jupyter-nbconvert --to slides --post serve Enterprise_ML_Part_I.ipynb
   ```

   This will open `http://127.0.0.1:8000/Enterprise_ML_Part_I.slides.html#/` in your browser.
3. Direct your browser to <http://127.0.0.1:8000/Enterprise_ML_Part_I.slides.html?print-pdf>, e.g. by replacing the `#/` part in the URL with `?print-pdf` in the browser's address field. (Clicking that link will work, too.)
4. Print the page to a PDF file

(based on [this StackOverflow answer](https://stackoverflow.com/a/52930481/674064) by [Hendrik Wiese](https://stackoverflow.com/users/205147/hendrik-wiese))
