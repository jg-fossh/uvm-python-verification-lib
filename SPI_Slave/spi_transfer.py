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
# File name     : spi_transfer.py
# Author        : Jose R Garcia
# Created       : 2020/11/22 10:24:13
# Last modified : 2021/02/20 11:51:35
# Project Name  : UVM Python Verification Library
# Module Name   : spi_transfer
# Description   : Wishbone Bus Sequence Item and Sequences.
#
# Additional Comments:
#   Creates a a read or write transaction.
##################################################################################################
from uvm import *

class spi_transfer(UVMSequenceItem):
    """
       Class: SPI Sequence Item

       Definition: Contains functions, tasks and methods of this
    """

    def __init__(self, name="spi_transfer"):
        super().__init__(name)
        """
           Function: new

           Definition: Class Constructor.

           Args:
             name: This agents name.
             parent: NONE
        """
        self.transfer_data = 0
        self.receive_data  = 0
        self.delay         = 0


uvm_object_utils(spi_transfer)
