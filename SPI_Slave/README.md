# Wishbone Pipeline Master Verification Agent Specifications

Document      | Metadata
:------------ | :------------------
_Version_       | v0.0.1
_Prepared by_   | Jose R Garcia
_Created_       | 2020/11/26 23:18:53
_Last modified_ | 2020/12/22 23:18:53
_Project_       | UVM-Python Verification Library

## Overview

Python code for a UVM SPI Slave Interface Verification Agent. This code depends on uvm-python and cocotb.

## Table Of Contents

<!-- TOC -->

- [Wishbone Pipeline Master Verification Agent Specifications](#wishbone-pipeline-master-verification-agent-specifications)
  - [Overview](#overview)
  - [Table Of Contents](#table-of-contents)
  - [2 Design](#2-design)
  - [3 Agent Configuration](#3-agent-configuration)
  - [4 Interfaces](#4-interfaces)
    - [4.1 Interface Definition](#41-interface-definition)
  - [5 Sequence Items](#5-sequence-items)
    - [5.1 spi_transfer](#51-spi_transfer)
  - [6 Sequences](#6-sequences)
    - [6.1 trans_seq](#61-trans_seq)
    - [6.2 spi_incr_payload](#62-spi_incr_payload)

<!-- /TOC -->

 ## 1 Syntax and Abbreviations

Term        | Definition
:---------- | :---------------------------------
0b0         | Binary number syntax
0x0000_0000 | Hexadecimal number syntax
bit         | Single binary digit (0 or 1)
BYTE        | 8-bits wide data unit
DWORD       | 32-bits wide data unit
LSB         | Least Significant bit
MSB         | Most Significant bit
SPI         | Serial Peripheral Interface
UVM         | Universal Verification Methodology


## 2 Design



|               ![Pipeline](Agent.png)
| :----------------------------------------------------:
| Figure 1 : Verification Environment Components and Connection Example

## 3 Agent Configuration

Signals   | Initial State | Direction | Definition
:-------- | :-----------: | :-------: | :-----------------------------------------------
`i_clk`   |      N/A      |    In     | Input clock. Data is sampled on the rising edge.
`i_reset` |      N/A      |    In     | Synchronous reset.

## 4 Interfaces


### 4.1 Interface Definition

Signals      | Initial State | Dimension | Direction | Definition
:----------- | :-----------: | :-------: | :-------: | :-----------------------
`i_si`       |      N/A      |   1-bit   |    In     |
`i_sclk_in`  |      N/A      |   1-bit   |    In     |
`i_ss_in`    |      N/A      |   1-bit   |    In     |
`i_in_clk`   |      N/A      |   1-bit   |    In     |
`o_so_en`    |       0       |   1-bit   |    Out    |
`o_so`       |       0       |   1-bit   |    Out    |
`i_mi`       |      N/A      |   1-bit   |    In     |
`i_ext_clk`  |       0       |   1-bit   |    In     |
`o_ss_en`    |      N/A      |   1-bit   |    Out    |
`o_ss_out`   |       0       |   1-bit   |    Out    |
`o_sclk_en`  |       0       |   1-bit   |    Out    |
`o_sclk_out` |       0       |   1-bit   |    Out    |
`o_mo_en`    |       0       |   1-bit   |    Out    |
`o_mo`       |       0       |   1-bit   |    Out    |


## 5 Sequence Items

### 5.1 spi_transfer

Fields          | Description
:-------------- | :------------------------------------------
`transfer_data` | Data to be serialized and sent to UUT.
`receive_data`  | Vector containing the received serial data.
`delay`         | Optional transaction delay.

## 6 Sequences

### 6.1 trans_seq

Fields  | Description
:------ | :---------------------------------------------------
`req`   | spi_transfer sequence item. Mainly used for directed testing. The sequence item is not randomized.
`delay` | Optional transaction delay.


### 6.2 spi_incr_payload

Fields           | Description
:--------------- | :---------------------------------------------------
`payload`        | Transmit data vector
`payload_width`  | payload's number of bits
