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
# File name     : wb_master_seq.py
# Author        : Jose R Garcia
# Created       : 2020/11/22 10:24:13
# Last modified : 2020/12/01 00:17:12
# Project Name  : UVM Python Verification Library
# Module Name   : wb_master_seq, wb_master_base_sequence
# Description   : Wishbone Bus Sequence Item and Sequences.
#
# Additional Comments:
#   Create a a read or write transaction.
##################################################################################################
from uvm import *

class wb_master_seq(UVMSequenceItem):
    """         
       Class: Wishbone Master Sequence Item
        
       Definition: Contains functions, tasks and methods of this
    """

    def __init__(self, name="wb_master_seq"):
        super().__init__(name)
        self.data_in           = 0 
        self.stall             = 0 
        self.response_data_tag = 0 
        self.acknowledge       = 1
        self.transmit_delay    = 0 
        

    def do_copy(self, rhs):
        self.addr           = rhs.addr
        self.data           = rhs.data
        self.type           = rhs.type
        self.byte_enable    = rhs.byte_enable
        self.transmit_delay = rhs.transmit_delay


    def do_clone(self):
        new_obj = wb_master_seq()
        new_obj.copy(self)
        return new_obj


    def convert2string(self):
        return sv.sformatf("\n ======================================= \n     ACK_i  : %s \n  TDG_i : 0h%0h \n     DATA_i : 0h%0h \n    Delay : %d  clocks \n ======================================= \n ",
                self.acknowledge, self.response_data_tag, self.data_in, self.transmit_delay)


uvm_object_utils(wb_master_seq)


class wb_master_base_sequence(UVMSequence):

    def __init__(self, name="wb_master_base_sequence"):
        super().__init__(name)
        self.set_automatic_phase_objection(1)
        self.req = wb_master_seq()
        self.rsp = wb_master_seq()

uvm_object_utils(wb_master_base_sequence)


class read_single_sequence(wb_master_base_sequence):
    """         
       Class: Wishbone Read Sequence
        
       Definition: Contains functions, tasks and methods
    """
    def __init__(self, name="read_single_sequence"):
        wb_master_base_sequence.__init__(self, name)


    async def body(self):
        # Build the sequence item


uvm_object_utils(read_sequence)


class write_single_sequence(wb_master_base_sequence):
    """         
       Class: Wishbone Write Sequence
        
       Definition: Contains functions, tasks and methods
    """
    def __init__(self, name="write_single_sequence"):
        wb_master_base_sequence.__init__(self, name)


    async def body(self):
        # Build the sequence item



uvm_object_utils(write_sequence)
