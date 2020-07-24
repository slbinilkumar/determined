"""
This example raises an error from user code.
"""
from determined.pytorch import PyTorchTrial, PyTorchTrialContext


class ErrorTrial(PyTorchTrial):
    def __init__(self, context: PyTorchTrialContext) -> None:
        raise NotImplementedError
