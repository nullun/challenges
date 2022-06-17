from typing import Tuple
import algosdk.abi  as sdk_abi
from pyteal import *

router = Router(
    name="calculator",
    bare_calls=BareCallActions(
        no_op=OnCompleteAction.create_only(Approve()),
    ),
)


@router.method
def add(a: abi.Uint64, b: abi.Uint64, *, output: abi.Uint64):
    return output.set(a.get() + b.get())


@router.method
def sub(a: abi.Uint64, b: abi.Uint64, *, output: abi.Uint64):
    # implement a method to subtract b from a
    pass


@router.method
def mul(a: abi.Uint64, b: abi.Uint64, *, output: abi.Uint64):
    # implement a method to multiply a and b
    pass


@router.method
def div(a: abi.Uint64, b: abi.Uint64, *, output: abi.Uint64):
    # implement a method to divide b by a
    pass


def build_router()->Tuple[str, str, sdk_abi.Contract]:
    return router.compile_program(version=6)