# Displaydir

I made this project because I needed a simple way to host a folder in a visually appealing way online, without setting up some kind of live service or complex hosting solution. I also, for somewhat obvious reasons, didn't want to rely on the direct but somewhat crude file browsing provided by each browser. By running `build.py`, you will generate a finished, user-navigable site tree with an index.html for each subfolder that allows them to view the files in the directory, view any readmes you have included in parsed markdown form, and return to the previous directory.

## Usage
1. Make sure your finished html directory (by default `public`) exists.
2. Put your content in `content`. Recursive directories are supported. If you want to show text alongside the folder, create a `readme.md`.
3. Run `build.py`.

## Credits
Default file icons from the excellent [VSCode Material Icon Theme](https://github.com/PKief/vscode-material-icon-theme).