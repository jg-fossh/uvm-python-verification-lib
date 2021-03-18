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
# File name     : spi_monitor.py
# Author        : Jose R Garcia
# Created       : 2020/11/05 20:08:35
# Last modified : 2021/02/25 17:39:10
# Project Name  : UVM Python Verification Library
# Module Name   : spi_monitor
# Description   : Wishbone Master Monitor.
#
# Additional Comments:
#
##################################################################################################
import cocotb
from cocotb.triggers import *

from uvm.base.uvm_callback import *
from uvm.comps.uvm_monitor import UVMMonitor
from uvm.tlm1 import *
from uvm.macros import *

from spi_transfer import *
from spi_if import *
from spi_csr import *

class spi_monitor(UVMMonitor):
    """         
       Class: Wishbone Master Monitor
        
       Definition: Contains functions, tasks and methods of this agent's monitor.
    """

    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        """         
           Function: new
          
           Definition: Class Constructor.

           Args:
             name: This agents name.
             parent: NONE
        """
        self.ap        = None
        self.vif       = spi_if  # connected at the agent
        self.errors    = 0
        self.num_items = 0
        self.csr_s     = spi_csr
        self.tag       = "spi_monitor" + name


    def build_phase(self, phase):
        super().build_phase(phase)
        """         
           Function: build_phase
          
           Definition: 

           Args:
             phase: build_phase
        """
        self.ap = UVMAnalysisPort("ap", self)

    
    async def run_phase(self, phase):
        """         
           Function: run_phase
          
           Definition: Task executed during run phase.

           Args:
             phase: run_phase
        """
        cocotb.fork(self.collect_transactions())


    async def collect_transactions(self):
        while True:
            tr = None  # Clean transaction for every loop.
            # Create sequence item for this transaction.
            await RisingEdge(self.vif.i_ss_in)
            
            tr = spi_transfer.type_id.create("tr", self)

            if (self.csr_s.tx_clk_phase == 0):
                i = 0
                while (i < self.csr_s.data_size):
                    i = i + 1
                    await FallingEdge(self.vif.i_sclk_in)
                    if (self.csr_s.mode_select == 1) :
                        tr.receive_data[i] = self.vif.i_si;
                    # uvm_info("SPI_MON", $sformatf("received data in mode_select 1 is %h", trans_collected.receive_data), UVM_HIGH)
                    # uvm_info(self.tag, tr.convert2string(), UVM_LOW)
                    else:
                        tr.receive_data[i] = self.vif.i_mi;
                    # uvm_info("SPI_MON", $sformatf("received data in mode_select 0 is %h", trans_collected.receive_data), UVM_HIGH)
                
            else:
                i = 0
                while (i < csr_s.data_size):
                    await RisingEdge(self.vif.i_sclk_in)
                    if (self.csr_s.mode_select == 1):
                        tr.receive_data[i] = spi_if.i_si
                    else:
                        tr.receive_data[i] = spi_if.i_mi
            
            self.num_items += 1       # Increment transactions count
            self.ap.write(tr) # Send transaction through analysis port
            # uvm_info(self.tag, tr.convert2string(), UVM_HIGH)


uvm_component_utils(spi_monitor)
