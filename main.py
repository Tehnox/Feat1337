from scr.logger import setup_logger
from scr.runner import run
import scr.generator as g


if __name__ == '__main__':
    # setup_logger()
    # run()
    g.generate_small_set()
    g.generate_full_set()
