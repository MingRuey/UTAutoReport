import svgwrite


if __name__ == "__main__":
    dwg = svgwrite.Drawing(
        filename="/home/mrchou/code/AxisDraw/sample/draw.svg",
        height="29.7cm", width="21cm"
    )
    dwg.add(
        dwg.text(
            "This is some text",
            insert=("1cm", "1cm")
        )
    )
    dwg.save()
