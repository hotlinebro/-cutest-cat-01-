"""Cutest cat entry: copy the cat picture to the output directory.

The output is a byte-exact copy of cat.jpg (a JPEG; the output file keeps
the name entry.png and the format is told apart by its first bytes, as the
competition rules allow). A plain copy is deterministic: two runs write
identical bytes.
"""

import hashlib
import os
import shutil

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cat.jpg")
DST = os.path.join(OUT_DIR, "entry.png")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    assert os.path.getsize(DST) == os.path.getsize(SRC)
    assert sha256(DST) == sha256(SRC)
    print("wrote", DST, os.path.getsize(DST), "bytes, sha256", sha256(DST))


if __name__ == "__main__":
    main()
