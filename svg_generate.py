from pathlib import Path
from typing import List
import datetime
import subprocess

HEADER_LIMIT = 40
PER_LINE_LIMIT = 65
TOTAL_LINES_LIMIT = 11

COL = "\n"
HEAD = r"""<svg baseProfile="full" width="8.3in" height="11.7in">"""
HEAD += COL + r"""<rect width="100%" height="100%" fill="white"/>"""
END = r"""</svg>"""


def count_length(content: str):
    count = 0
    for char in content:
        if 0x4e00 <= ord(char) <= 0x9fa5:
            count += 2
        else:
            count += 1
    return count


def _process_string(content: str):
    content = content.replace(r"&", r"&amp;")
    content = content.replace(r">", r"&gt;")
    content = content.replace(r"<", r"&lt;")
    content = content.replace(r"\"", r"&quot;")
    content = content.replace(r"'", r"&apos;")
    return content


def create_header(date: datetime.date, header: str):
    header = _process_string(header)
    txt_year = f"""<text x="107" y="162" font-size="12" text-anchor="left" fill="black">{date.year}</text>"""
    txt_month = f"""<text x="162" y="162" font-size="12" text-anchor="left" fill="black">{date.month}</text>"""
    txt_day = f"""<text x="208" y="162" font-size="12" text-anchor="left" fill="black">{date.day}</text>"""
    txt_header = f"""<text x="265" y="162" font-size="12" text-anchor="left" fill="black">{header}</text>"""
    return txt_year + COL + txt_month + COL + txt_day + COL + txt_header


def _convert_to_svgline(line: str, idx: int):
    _SVGLINE = r"""<text x="120" y="{}" font-size="16" text-anchor="left" fill="black">{}</text>"""
    return _SVGLINE.format(270 + idx * 40, _process_string(line))


def read_content(file: str):
    file = Path(file)
    if not file.is_file:
        raise ValueError(f"File {file} not exist")

    with open(str(file), "r") as f:
        lines = f.readlines()
        if len(lines) < 3:
            raise ValueError(f"Lack content in {file}")

        if not lines[0].upper().startswith("DATE:"):
            raise ValueError("First line must start with 'HEADER: '")
        date = lines[0][5:].strip()
        date = datetime.datetime.strptime(date, r"%Y-%m-%d")

        if not lines[1].upper().startswith("HEADER:"):
            raise ValueError("First line must start with 'HEADER: '")
        header = lines[1][7:].strip()

        if not len(header):
            raise ValueError("Empty header")

        if len(lines[2:]) > TOTAL_LINES_LIMIT:
            raise ValueError("More than 9 lines in content")

    return date, header, [line.strip() for line in lines[2:]]


def create_svg(date: datetime.date,
               header: datetime.date,
               lines: List[str]):
    svg = HEAD + COL

    if count_length(header) > HEADER_LIMIT:
        raise ValueError(f"Length of header {header} exceed {HEADER_LIMIT}")
    svg += create_header(date, header) + COL

    for idx, line in enumerate(lines):
        if count_length(line) > PER_LINE_LIMIT:
            raise ValueError(f"Line {line} exceed {PER_LINE_LIMIT}")
        svg += _convert_to_svgline(line, idx) + COL

    svg += END
    return svg


if __name__ == "__main__":
    RAWPATH = Path(r"/home/mrchou/code/AxisDraw/files/inter")
    OUTPATH = Path(r"/home/mrchou/code/AxisDraw/files/out")

    FILEPATH = Path(r"/home/mrchou/code/AxisDraw/files/raw/201907")

    for ifile in FILEPATH.glob(r"*.txt"):
        print(f"Process file {ifile.name}")
        date, header, lines = read_content(str(ifile))
        svg = create_svg(date=date, header=header, lines=lines)

        fname = Path(f"{date.year}-{date.month:02d}-{date.day:02d}.svg")
        ofile = str(RAWPATH.joinpath(fname))
        with open(ofile, "w") as out:
            out.write(svg)

        cmd = ["inkscape"]
        arguments = [
            ofile, "--export-text-to-path", "--export-plain-svg",
            str(OUTPATH.joinpath(fname.stem + "_graph.svg"))
        ]
        subprocess.call(" ".join(cmd + arguments), shell=True)
