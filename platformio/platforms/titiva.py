# Copyright (C) Ivan Kravets <me@ikravets.com>
# See LICENSE for details.

from os.path import join

from platformio.platforms._base import BasePlatform


class TitivaPlatform(BasePlatform):
    """
        An embedded platform for TI TIVA C ARM microcontrollers
        (with Energia Framework)
    """

    PACKAGES = {

        "toolchain-gccarmnoneeabi": {
            "path": join("tools", "toolchain"),
            "default": True
        },

        "tool-lm4flash": {
            "path": join("tools", "lm4flash"),
            "default": True,
        },

        "framework-energiativa": {
            "path": join("frameworks", "energia"),
            "default": True
        }
    }

    def get_name(self):
        return "titiva"
