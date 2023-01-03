# global
import jax

backend_version = {"version": jax.__version__}

# local sub-modules
# flake8: noqa
from .activations import *
from .compilation import *
from .converters import *
from .creation import *
from .data_type import *
from .device import *
from .elementwise import *
from .general import *
from .gradients import *
from .layers import *
from .linear_algebra import *
from .manipulation import *
from .random import *
from .searching import *
from .set import *
from .sorting import *
from .sparse_array import *
from .statistical import *
from .utility import *

del (
    activations,
    compilation,
    converters,
    creation,
    data_type,
    device,
    elementwise,
    general,
    gradients,
    layers,
    linear_algebra,
    manipulation,
    random,
    searching,
    set,
    sorting,
    sparse_array,
    statistical,
    utility,
)