import shutil
from pathlib import Path
from pyaxidraw import axidraw

IN_DIR = Path(r"/home/mrchou/code/AxisDraw/files/out/")
DONE_DIR = Path(r"/home/mrchou/code/AxisDraw/files/done")
files = list(IN_DIR.glob("*.svg"))
files.sort()
FILE = files[0]

if __name__ == "__main__":
    if not FILE.is_file:
        raise ValueError(f"{FILE} not exist")

    if not DONE_DIR.is_dir:
        raise ValueError(f"{DONE_DIR} is not a directory")

    ad = axidraw.AxiDraw()
    ad.interactive()
    ad.connect()
    ad.moveto(0, 0)
    ad.options.pen_rate_raise = 100
    ad.disconnect()
    ad.plot_setup(str(FILE))
    ad.plot_run()

    shutil.move(str(FILE), str(DONE_DIR.joinpath(FILE.stem + "_done.svg")))
