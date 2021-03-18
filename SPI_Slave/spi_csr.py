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
# File name     : spi_csr.py
# Author        : Jose R Garcia
# Created       : 2020/11/22 10:24:13
# Last modified : 2021/02/25 16:37:10
# Project Name  : UVM Python Verification Library
# Module Name   : spi_csr, spi_base_sequence
# Description   : Wishbone Bus Sequence Item and Sequences.
#
# Additional Comments:
#   Create a a read or write transaction.
##################################################################################################
from uvm import *

class spi_csr_s:
    pass
    """         
       Class: spi_csr_s
        
       Definition: Empty class used to create a struct
    """


class spi_csr(UVMSequenceItem):
    """         
       Class: Wishbone Master Sequence Item
        
       Definition: Contains functions, tasks and methods of this
    """

    def __init__(self, name="spi_csr"):
        super().__init__(name)
        """         
           Function: new
          
           Definition: Class Constructor.

           Args:
             name: This agents name.
             parent: NONE
        """
        # self.csr_s = spi_csr_s()
        # default config
        self.ss_out             = 0x01
        self.transfer_data_size = 0b0001000
        self.baud_rate_divisor  = 0x0001
        self.tx_clk_phase       = 0b0
        self.rx_clk_phase       = 0b0
        self.mode_select        = 0b1

        self.tx_fifo_underflow = 0b1
        self.rx_fifo_full      = 0b1 
        self.rx_fifo_not_empty = 0b1
        self.tx_fifo_full      = 0b1
        self.tx_fifo_not_empty = 0b1
        self.mode_fault        = 0b1
        self.rx_fifo_overrun   = 0b1

        self.spi_enable = 0b1

        self.d_btwn_slave_sel    = 0x00
        self.d_btwn_word         = 0x00
        self.d_btwn_senable_word = 0x00
  
        if (self.transfer_data_size == 0b0000000):
            self.data_size = 128
        else:
            self.data_size = self.transfer_data_size



uvm_object_utils(spi_csr)