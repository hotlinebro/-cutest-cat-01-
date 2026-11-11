# Cutest cat — make.fun entry

A photorealistic fluffy cream-and-ginger kitten with huge bright blue eyes,
head tilted, one paw on a small pink ball of yarn. The entry program copies
the image to `/output/entry.png`.

## Files

- `main.py` — the entry program (Python 3.13, standard library only).
  Copies `cat.jpg` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`).
- `cat.jpg` — the cat picture (JPEG, 1024x1024, 245,464 bytes).
  The output keeps the name `entry.png`; the format is told apart by its
  first bytes, as the competition rules allow.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two runs write byte-identical output (a plain file copy).
