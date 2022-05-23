---
title: "ECE120 Lecture 35 - LC-3 Control Signals and FETCH"
---
## LC-3 Control Signals
### Control Unit FSM
Remind that the control unit of LC-3 is a **FSM**.([[lecture_notes/ECE120/ECE120 Lecture 26#Control Unit|Lecture 26]])

The inputs: signals from the datapath
The outputs: control signals for the datapath

### Control Signals in LC-3 Datapath
#### Group 1: Register Loads
Each signal is set iff the RTL for the current FSM state changes that register’s value. In other words, the load signal is 1 if the register appears on the left side of an RTL expression, and is 0 otherwise.

List of register loads:
- `LD.MAR`
- `LD.MDR`
- `LD.IR`
- `LD.BEN`
- `LD.REG`
- `LD.CC`
- `LD.PC`

#### Group 2: Bus Gating
These are tri-state buffers used to write values onto the bus. At most one bus gating signal can be a 1. All others must be 0 to avoid short circuits through the bus.

List of bus gating:
- `GatePC`
- `GateMDR`
- `GateALU`
- `GateMARMUX`

#### Group 3: Mux Selection
These 6 MUXes serves different purposes:
1. `PCMUX` controls the value loaded into the PC, (thus only useful when `LD.PC`=1.)
	- 00 `PC+1`
	- 01 bus
	- 10 address generation adder (for `BR` and `JMP`)
2. `DRMUX` controls the destination register, (thus only useful when `LD.REG`=1.)
	- 00 `IR[11:9]`
	- 01 `R7`
	- 10 `R6`
3. `SR1MUX` controls source register 1 from the register file.
	- 00 `IR[11:9]`
	- 01 `IR[8:6]`
	- 10 `R6`
4. `ADDR1MUX` 
	- 0 `PC`
	- 1 `SR1`
5. `ADDR2MUX`
	- 00 `0`
	- 01 `SEXT(IR[5:0])`
	- 10 `SEXT(IR[8:0])`
	- 11 `SEXT(IR[10:0])`
6. `MARMUX`
	- 0 `ZEXT(IR[7:0])`
	- 1 address generation adder

#### Group 4: ALU Function Selection
The `ALUK` control signal supports four functions, including passing the `A` input to the output:
- 00 `ADD`
- 01 `AND`
- 10 `NOT A`
- 11 PASS `A`

#### Group 5: Memory Operations
`MIO.EN` tells the memory to operate (1 to do a read or a write).
When `MIO.EN` = 1:
- `R.W` = 1 for a write
- `R.W` = 0 for a read

### All the Signals Together
How many control signals do we have?

| Group                  | #   |
| ---------------------- | --- |
| register loads         | 7   |
| bus gating             | 4   |
| mux selection          | 10  |
| ALU function selection | 2   |
| memory operation       | 2   |
| **TOTAL**              | 25  |

## LC-3 Control Signals in FETCH and DECODE
### RTL for FETCH and DECODE
Fetch 1:$MAR\leftarrow PC,PC\leftarrow PC+1$
Fetch 2:$MDR\leftarrow M[MAR]$
Fetch 3:$IR\leftarrow MDR$
Decode: $BEN\leftarrow IR[11]\&N +IR[10]\&Z+IR[9]\&P$

### Control Signals

|        | `LD.MAR` | `LD.MDR` | `LD.IR` | `LD.BEN` | `LD.REG` | `LD.CC` | `LD.PC` |
| ------ | -------- | -------- | ------- | -------- | -------- | ------- | ------- |
| fetch1 | 1        | 0        | 0       | 0        | 0        | 0       | 1       |
| fetch2 | 0        | 1        | 0       | 0        | 0        | 0       | 0       |
| fetch3 | 0        | 0        | 1       | 0        | 0        | 0       | 0       |
| decode | 0        | 0        | 0       | 1        | 0        | 0       | 0        |

|        | `GatePC` | `GateMDR` | `GateALU` | `GateMARMUX` |
| ------ | -------- | --------- | --------- | ------------ |
| fetch1 | 1        | 0         | 0         | 0            |
| fetch2 | 0        | 0         | 0         | 0            |
| fetch3 | 0        | 1         | 0         | 0            |
| decode | 0        | 0         | 0         | 0            | 

|        | `PCMUX` | `DRMUX` | `SR1MUX` | `ADDR1MUX` | `ADDR2MUX` | `MARMUX` |
| ------ | ------- | ------- | -------- | ---------- | ---------- | -------- |
| fetch1 | 00      | xx      | xx       | x          | xx         | x        |
| fetch2 | xx      | xx      | xx       | x          | xx         | x        |
| fetch3 | xx      | xx      | xx       | x          | xx         | x        |
| decode | xx      | xx      | xx       | x          | xx         | x         |

|        | `ALUK` | `MIO.EN` | `R.W` |
| ------ | ------ | -------- | ----- |
| fetch1 | xx     | 0        | x     |
| fetch2 | xx     | 1        | 0     |
| fetch3 | xx     | 0        | x     |
| decode | xx     | 0        | x      |

