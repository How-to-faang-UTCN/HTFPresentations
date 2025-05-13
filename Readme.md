Make sure to:

- Use python 3.11, the others run into stupid bugs
- We use [manim community](https://docs.manim.community/en/stable/installation/uv.html) for this project. Make sure to install `cairo pkg-config cmake` for it to work. After these 3, you can use `pip install manim` and it works, you can ignore their uv instructions
- Afterwards, install [manim slides](https://manim-slides.eertmans.be/latest/installation.html) which turns normal manim presentation into slides format

Using manim community seem to break manim slides opengl renderer, that is not an issue unless you want live scene interactivity which is overkill mostly.
