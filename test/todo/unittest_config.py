from pydantic import (
    BaseModel
)

from typing import Literal

class Config(BaseModel):
    print_out:Literal[True, False] = False

default_config = Config(
    ## write your default config here.
)

## write more pre-defined configurations here
