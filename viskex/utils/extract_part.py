# Copyright (C) 2023-2024 by the viskex authors
#
# This file is part of viskex.
#
# SPDX-License-Identifier: MIT
"""viskex utils module."""

import typing

import numpy as np
import numpy.typing

from viskex.utils.scalar_type import ScalarType


def extract_part(
    values: np.typing.NDArray[ScalarType], name: str, part: str
) -> typing.Tuple[np.typing.NDArray[np.float64], str]:
    """Extract real or complex part from an array, and update the name to reflect this."""
    if np.issubdtype(ScalarType, np.complexfloating):
        if part == "real":
            values = values.real
            name = "real(" + name + ")"
        elif part == "imag":
            values = values.imag
            name = "imag(" + name + ")"
    return values, name
