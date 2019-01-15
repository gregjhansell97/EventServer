import argparse
import inspect
from flask import Flask
from flask import request

from EventServer import EventServer


app = Flask(__name__)
server = EventServer(bit_depth=32, min_x=0, min_y=0)

def handle_request(data=None):
    method = data["method"]
    args = []
    kwargs = {}
    if "args" in data:
        args = data["args"]
    if "kwargs" in data:
        kwargs = data["kwargs"]
    result = getattr(server, method)(*args, **kwargs)


#
# def generate_arguments():
#
#     functions = [
#         (n, f)
#         for n, f in inspect.getmembers(EventServer)
#         if inspect.isfunction(f) and "__" not in n]
#
#     for f in functions:
#         print(f)
#     # for name, function in inspect.getmembers(EventServer):
#     #     if hasattr(i, "__name__"):
#     #         print(i.__name__)
#
#     parser = argparse.ArgumentParser("testing the event commands without a server attatched")
#     parser.add_argument("strings", metavar="S", type=str, nargs="+")
#     for n, f in functions:
#         parser.add_argument("--" + n, dest="run", const=f)
#
#     parser.add_argument("--sum", dest="accumulate", action="store_const", const=sum, default=max, help="sum the integers")
#     return parser.parse_args()

if __name__ == "__main__":
    handle_request(
    {
        "method": "hello_world",
        "args": ["does this work? "],
        "kwargs": {
            "kwarg1": "I think this will!"
        }
    })
    # args = generate_arguments()
    # print(args.accumulate(args.integers))
