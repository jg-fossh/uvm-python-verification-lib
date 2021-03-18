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
# File name     : spi_seq_lib.py
# Author        : Jose R Garcia
# Created       : 2020/11/22 10:24:13
# Last modified : 2021/03/01 19:06:13
# Project Name  : UVM Python Verification Library
# Module Name   : spi_seq_lib, trans_seq, spi_incr_payload
# Description   : Wishbone Bus Sequence Item and Sequences.
#
# Additional Comments:
#   Create a a read or write transaction.
##################################################################################################
from uvm import *
from spi_transfer import *

class trans_seq(UVMSequence):
    """         
       Class: 
        
       Definition: Contains functions, tasks and methods of this
    """

    def __init__(self, name="trans_seq"):
        super().__init__(name)
        self.set_automatic_phase_objection(1)
        self.req = spi_transfer()
        self.delay = 0

    async def body(self):
        # Build the sequence item
        self.req.delay = self.delay
        await uvm_do_with(self, self.req) # start_item 
        
uvm_object_utils(trans_seq)


class spi_incr_payload(trans_seq):
    """         
       Class: 
        
       Definition: Contains functions, tasks and methods of this
    """

    def __init__(self, name="spi_incr_payload"):
        super().__init__(name)
        self.payload = 0
        self.payload_width = 0
        self.payload_array = []

    async def body(self):
        # Build the sequence item
        self.payload_array = [int(x) for x in '{:0{size}b}'.format(self.payload,size=self.payload_width+1)]
        i = 0
        while (i < self.payload_width):
            i = i + 1 
            self.req.transfer_data = self.payload_array[i]
            await uvm_do_with(self, self.req) # start_item 

uvm_object_utils(spi_incr_payload)
