from pyaxidraw import axidraw


if __name__ == "__main__":
    ad = axidraw.AxiDraw()
    ad.interactive()
    ad.connect()
    ad.diconnect()
