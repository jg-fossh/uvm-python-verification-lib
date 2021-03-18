#####################################################################################
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
#####################################################################################
# File name     : spi_agent.py
# Author        : Jose R Garcia
# Created       : 2021/02/20 00:08:57
# Last modified : 2021/02/25 17:49:03
# Project Name  : UVM-Python Verification Library
# Module Name   : spi_agent
# Description   : SPI Verification Component Agent.
#
# Additional Comments:
#   The agent's components instantiations and connections.
#####################################################################################
from uvm import *
from spi_if import *
from spi_driver import *
from spi_sequencer import *
from spi_monitor import *
from spi_csr import *

class spi_agent(UVMAgent):
    """
       Class: SPI Verification Agent

       Definition: Contains the instantiations and connections of this agents
                   components.
    """

    def __init__(self, name, parent=None):
        """
           Function: new

           Definition: Agent constructor.

           Args:
             name: This agents name.
             parent: NONE
        """
        super().__init__(name, parent)
        self.cfg = None  # config
        self.sqr = None  # sequencer
        self.drv = None  # driver
        self.mon = None  # monitor
        self.id  = None  # agent's id
        self.csr_s = spi_csr("csr_s")
        self.ap  = UVMAnalysisPort("ap", self) # analysis port for the monitor


    def build_phase(self, phase):
        super().build_phase(phase)
        """
           Function: build_phase

           Definition: Creates this agent's components.

           Args:
             phase: build_phase
        """

        self.mon = spi_monitor.type_id.create("mon", self)

        if (self.cfg.is_active):
            self.drv = spi_driver.type_id.create("drv", self)
            self.sqr = UVMSequencer.type_id.create("sqr", self)
            #self.drv.mon = self.mon


    def connect_phase(self, phase):
        """
           Function: connect_phase

           Definition: Connects the analysis port and sequence item export.

           Args:
             phase: connect_phase
        """
        self.mon.vif   = self.cfg.vif
        self.mon.csr_s = self.csr_s
        # sself.mon.ap.connect(self.ap)

        if (self.cfg.is_active):
            self.drv.vif = self.cfg.vif
            self.drv.csr_s = self.csr_s
            self.drv.seq_item_port.connect(self.sqr.seq_item_export) # Driver Connection


uvm_component_utils(spi_agent)
