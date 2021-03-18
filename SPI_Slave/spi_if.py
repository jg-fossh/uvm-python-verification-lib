##################################################################################################
# BSD 3-Clause License
#
# Copyright (c) 2020, Jose R. Garcia
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##################################################################################################
# File name     : spi_if.py
# Author        : Jose R Garcia
# Created       : 2020/11/22 10:20:00
# Last modified : 2021/02/25 17:37:14
# Project Name  : UVM-Python Verification Library
# Module Name   : spi_if
# Description   : SPI virtual interface
#
# Additional Comments:
#
##################################################################################################
import cocotb
from cocotb.triggers import *
from uvm.base.sv import sv_if

class spi_if(sv_if):
    """
       Class: SPI Interface

       Definition: Contains functions, tasks and methods of this agent's virtual interface.
    """


    def __init__(self, dut, bus_map=None):
        """
           Function: new

           Definition: Read slave interface constructor.

           Args:
             dut: The dut it connects to. Passed in by cocotb top.
             bus_map: Naming of the bus signals.
        """
        if bus_map is None:
            #  If NONE then create this as default.
            bus_map = {"i_clk": "i_clk",
                       "i_reset": "i_reset",
                       "i_si": "i_si",
                       "i_sclk_in": "i_sclk_in",
                       "i_ss_in": "i_ss_in",
                       "i_in_clk": "i_in_clk",
                       "o_so_en": "o_so_en",
                       "o_so": "o_so",
                       "i_mi": "i_mi",
                       "i_ext_clk": "i_ext_clk",
                       "o_ss_en": "o_ss_en",
                       "o_ss_out": "o_ss_out",
                       "o_sclk_en": "o_sclk_en",
                       "o_sclk_out": "o_sclk_out",
                       "o_mo_en": "o_mo_en",
                       "o_mo": "o_mo"}
        super().__init__(dut, "",bus_map)


    async def start(self):
        await Timer(0, "NS")
