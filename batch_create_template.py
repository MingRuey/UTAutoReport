import datetime
from pathlib import Path

OUTPATH = Path(r"/home/mrchou/code/AxisDraw/files/unfinished")
CONTENT = \
    """Date:{date}
HEADER:{header}
{content}
"""

dates = [
    "2019-06-04", "2019-06-06", "2019-06-11", "2019-06-13", "2019-06-18", "2019-06-20", "2019-06-25", "2019-06-27",
    "2019-07-02", "2019-07-04", "2019-07-09", "2019-07-11", "2019-07-16", "2019-07-18", "2019-07-23", "2019-07-25",
    "2019-08-06", "2019-08-08", "2019-08-13", "2019-08-15", "2019-08-20", "2019-08-22", "2019-08-27", "2019-08-29",
    "2019-09-03", "2019-09-05", "2019-09-10", "2019-09-12", "2019-09-17", "2019-09-19", "2019-09-24", "2019-09-26",
    "2019-10-03", "2019-10-08", "2019-10-10", "2019-10-15", "2019-10-17", "2019-10-22", "2019-10-24", "2019-10-29",
    "2019-11-05", "2019-11-07", "2019-11-12", "2019-11-14", "2019-11-19", "2019-11-21", "2019-11-26", "2019-11-28",
    "2019-12-03", "2019-12-05", "2019-12-10", "2019-12-12", "2019-12-17", "2019-12-19", "2019-12-24", "2019-12-26",
    "2020-01-02", "2020-01-07", "2020-01-09", "2020-01-14", "2020-01-21", "2020-01-30",
    "2020-02-04", "2020-02-06", "2020-02-11", "2020-02-13", "2020-02-18", "2020-02-20", "2020-02-25", "2020-02-27",
    "2020-03-03", "2020-03-05", "2020-03-10", "2020-03-12", "2020-03-17", "2020-03-19", "2020-03-24", "2020-03-26",
    "2020-04-07", "2020-04-09", "2020-04-14", "2020-04-16", "2020-04-21", "2020-04-23", "2020-04-28", "2020-04-30",
    "2020-05-05", "2020-05-07", "2020-05-12", "2020-05-14", "2020-05-19", "2020-05-21", "2020-05-26", "2020-05-28",
    "2020-06-02", "2020-06-04", "2020-06-09", "2020-06-11", "2020-06-16", "2020-06-18", "2020-06-23", "2020-06-30",
    "2020-07-07", "2020-07-09", "2020-07-14", "2020-07-16", "2020-07-21", "2020-07-23", "2020-07-28", "2020-07-30",
    "2020-08-04", "2020-08-06", "2020-08-11", "2020-08-13", "2020-08-18", "2020-08-20", "2020-08-25", "2020-08-27",
    "2020-09-03", "2020-09-08", "2020-09-10", "2020-09-15", "2020-09-17", "2020-09-22", "2020-09-24", "2020-09-29",
    "2020-10-06", "2020-10-08", "2020-10-13", "2020-10-15", "2020-10-20", "2020-10-22", "2020-10-27", "2020-10-29",
    "2020-11-03", "2020-11-05", "2020-11-10", "2020-11-12", "2020-11-17", "2020-11-19", "2020-11-24", "2020-11-26",
    "2020-12-03", "2020-12-08", "2020-12-10", "2020-12-15", "2020-12-17", "2020-12-22", "2020-12-24", "2020-12-29",
    "2021-01-05", "2021-01-07", "2021-01-12", "2021-01-14", "2021-01-19", "2021-01-21", "2021-01-26", "2021-01-28",
    "2021-02-02", "2021-02-04", "2021-02-09", "2021-02-18", "2021-02-23", "2021-02-25",
    "2021-03-04", "2021-03-09", "2021-03-11", "2021-03-16", "2021-03-18", "2021-03-23", "2021-03-25", "2021-03-30",
    "2021-04-06", "2021-04-08", "2021-04-13", "2021-04-15", "2021-04-20", "2021-04-22", "2021-04-27", "2021-04-29",
    "2021-05-04", "2021-05-06", "2021-05-11", "2021-05-13", "2021-05-18", "2021-05-20", "2021-05-25", "2021-05-27"
]

if __name__ == "__main__":
    for date in dates:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")

        PARENT = f"{date.year}{date.month:02d}"
        PARENT = OUTPATH.joinpath(PARENT)
        if not PARENT.is_dir():
            PARENT.mkdir()

        fname = f"{date.year}-{date.month:02d}-{date.day:02d}"
        outf = PARENT.joinpath(f"{fname}.txt")
        with open(str(outf), "w") as f:
            f.write(CONTENT.format(date=fname, header="header", content="content"))
