import shutil
from pathlib import Path
from pyaxidraw import axidraw

FILE = Path(r"/home/mrchou/code/AxisDraw/files/out/2021-5-2_graph.svg")
DONE_DIR = Path(r"/home/mrchou/code/AxisDraw/files/done")

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
    # ad.disconnect()
    # ad.plot_setup(str(FILE))
    # ad.plot_run()

    shutil.move(str(FILE), str(DONE_DIR.joinpath(FILE.stem + "_done.svg")))
