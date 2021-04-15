import sys  # nopep8
sys.path.append(".")  # nopep8
from sovt import SOVT


if __name__ == "__main__":
    # This is the path to the folder you wish to have the plots saved to
    path = r"J:\cutools\sovt"

    print("Working...")
    sovt = SOVT(path, clean=False, make_plots=True)
    sovt.run()
    print("Completed!")
