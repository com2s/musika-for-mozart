import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from parse_test import parse_args
from models import Models_functions
from utils import Utils_functions

if __name__ == "__main__":

    # parse args
    args = parse_args()

    # initialize networks
    M = Models_functions(args)
    models_ls_1, models_ls_2, models_ls_3 = M.get_networks()

    # test musika
    U = Utils_functions(args)
    U.render_gradio(models_ls_1, models_ls_2, models_ls_3, train=False)
