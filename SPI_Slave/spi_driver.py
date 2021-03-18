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
# File name     : spi_driver.py
# Author        : Jose R Garcia
# Created       : 2021/02/19 23:54:51
# Last modified : 2021/03/01 15:00:29
# Project Name  : UVM-Python Verification Library
# Module Name   : spi_driver
# Description   : SPI Driver.
#
# Additional Comments:
#   This driver drives the signals to respond to a transaction.
##################################################################################################
import cocotb
from cocotb.triggers import *
from cocotb.clock import Clock

from uvm import *
from uvm.base import *
from uvm.comps import UVMDriver
from uvm.macros import uvm_component_utils, uvm_info

from spi_transfer import *
from spi_if import *
from spi_monitor import *
from spi_csr import *

class spi_driver(UVMDriver):
    """         
       Class: SPI Driver
        
       Definition: Contains functions, tasks and methods to drive the read interface
                   signals in response to the DUT. This is the stimulus generator.
    """

    def __init__(self, name, parent=None):
        super().__init__(name,parent)
        """         
           Function: new
          
           Definition: Read slave agent constructor.

           Args:
             name: This agents name.
             parent: NONE
        """
        self.seq_item_port
        self.vif   = spi_if
        self.csr_s = spi_csr("csr_s")
        self.trig  = Event("trans_exec")  # event
        self.tag   = "spi_driver" + name
        self.data  = 0
        self.sclk_out = None


    def build_phase(self, phase):
        super().build_phase(phase)
        """         
           Function: build_phase
          
           Definition: Gets this agent's interface.

           Args:
             phase: build_phase
        """


    def connect_phase(self, phase):
        """         
           Function: connect_phase
          
           Definition: Connects the analysis port and sequence item export. 

           Args:
             phase: connect_phase
        """
        ##self.sclk_out_clk = Clock(self.sclk_out, self.csr_s.baud_rate_divisor, units="us") 
    
    async def run_phase(self, phase):
        """         
           Function: run_phase
          
           Definition: Task executed during run phase. Drives the signals in
                       response to a UUT requests. 

           Args:
             phase: run_phase
        """
            # Create a 1000Mhz clock
        ##cocotb.fork(self.sclk_out_clk.start())  # Start the clock
        cocotb.fork(self.get_and_drive(phase))
        cocotb.fork(self.reset_signals())


    async def get_and_drive(self, phase):
        tr = []
        while True:
            # Drives signals with sequences
            if (self.vif.i_reset == 0):
                self.vif.o_ss_en <= 0b0
                await self.seq_item_port.get_next_item(tr)
                phase.raise_objection(self, self.tag + "objection")
                tr = tr[0]
                await self.drive_transfer(tr)
                self.seq_item_port.item_done()
                phase.drop_objection(self, self.tag + "drop objection")
                self.trig.set()
                await FallingEdge(self.vif.o_sclk_out)
                tr = []


    async def reset_signals(self):
        while True:
            # Hold signals low while reset
            await RisingEdge(self.vif.i_reset)
            self.vif.o_so_en         <= 0
            self.vif.o_so            <= 0
            self.vif.o_ss_en         <= 0
            self.vif.o_ss_out        <= 0
            self.vif.o_sclk_en       <= 0
            self.vif.o_mo_en         <= 0
            self.vif.o_mo            <= 0
            await FallingEdge(self.vif.i_reset)


    async def drive_transfer(self, tr):
        #if (self.csr_s.mode_select == 1):
            # DUT MASTER mode, OVC SLAVE mode
                #@monitor.new_transfer_started;
                #for (int i = 0; i < self.csr_s.data_size; i++) begin
                ##@monitor.new_bit_started;
        #spi_if.o_so_en <= 0b1;

        #await RisingEdge(self.vif.o_sclk_out)
        self.vif.o_mo    <= tr.transfer_data
        self.vif.o_mo_en <= 0b1
        self.vif.o_ss_en <= 0b1
        await RisingEdge(self.vif.o_sclk_out)

        ##self.vif.o_sclk_out <= self.sclk_out;
        #self.vif.o_so_en <= 0b1;
        #uvm_info("SPI_DRIVER", $sformatf("Transfer sent :\n%s", trans.sprint()), UVM_MEDIUM)

uvm_component_utils(spi_driver)
