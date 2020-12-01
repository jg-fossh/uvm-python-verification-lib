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
# File name     : wb_master_agent.py
# Author        : Jose R Garcia
# Created       : 2020/11/09 21:43:54
# Last modified : 2020/12/01 00:11:28
# Project Name  : UVM-Python Verification Library
# Module Name   : wb_master_agent
# Description   : Wishbone Bus Master Verification Component Agent.
#
# Additional Comments:
#   The agent's components instantiations and connections.
##################################################################################################
from uvm import *
from wb_master_agent_if import *
from wb_master_agent import *
from wb_master_agent_sequencer import *
from wb_master_agent_monitor import *
from mem_model import *

class wb_master_agent(UVMAgent):
    """         
       Class: Wishbone Bus Verification Component Agent
        
       Definition: Contains the instantiations and connections of this agents components.
    """
    
    def __init__(self, name, parent=None):
        """         
           Function: new
          
           Definition: Read slave agent constructor.

           Args:
             name: This agents name.
             parent: NONE
        """
        super().__init__(name, parent)
        self.wb_master_cfg = None  # wb_master_agent_config
        self.wb_master_sqr = None  # wb_master_agent_sequencer
        self.wb_master_drv = None  # wb_master_agent (driver)
        self.wb_master_mon = None  # wb_master_agent_monitor
        self.wb_master_vif = None  # memory_intfc_vif No library import, it is in __init__.py
        self.wb_master_ap  = UVMAnalysisPort("ap", self) # analysis port for the monitor


    def build_phase(self, phase):
        super().build_phase(phase)
        """         
           Function: build_phase
          
           Definition: Create a new read slave agent with all its components.

           Args:
             phase: build_phase
        """
        arr = []
        if (not UVMConfigDb.get(self, "*", "wb_master_cfg", arr)):
            uvm_fatal("MEM_INFC_READ_SLAVE/AGENT/CONFIG", "No wb_master_agent_config")
        self.wb_master_cfg = arr[0]
        
        
        if (self.wb_master_cfg.has_driver)
            self.wb_master_drv = wb_master_agent.type_id.create("wb_master_drv", self)
            # self.sqr = wb_master_agent_sequencer.type_id.create("sqr", self)
            self.wb_master_sqr = UVMSequencer.type_id.create("wb_master_sqr", self)
       
        if (self.wb_master_cfg.has_monitor)
            self.wb_master_mon = wb_master_agent_monitor.type_id.create("wb_master_mon", self)


    def connect_phase(self, phase):
        """         
           Function: connect_phase
          
           Definition: Connects the analysis port and sequence item export. 

           Args:
             phase: connect_phase
        """
        if (self.wb_master_cfg.has_monitor)
            self.wb_master_mon.vif = self.wb_master_cfg.vif
            self.wb_master_mon.ap.connect(self.wb_master_ap)
       
        if (self.wb_master_cfg.has_driver)
            self.wb_master_drv.seq_item_port.connect(self.wb_master_sqr.seq_item_export) # Driver Connection
            self.wb_master_drv.vif = self.wb_master_cfg.vif


uvm_component_utils(wb_master_agent)
