---
title: "ECE120 Lecture 22 - Memory"
---
## Storing Lots of Bits
The computer we’re going to design has a lot of places to store bits. Each place stores 32 bits. We need names for the places. The best way is to assign them with a number.

But with so many bits, how to access one or multiple of them? We need to build a circuit that lets us read and write the bits stored in each place.

The circuit should have:
- Input ADDR: Tell the circuit the address we want
- Output DATA-OUT: The data stored in ADDR.
- Input DATA-IN: The data we wish to store in ADDR.
- Input WE: Tell the circuit whether we want to read or write (write enable).

## Memory
The circuit we proposed is called **memory**. The symbol diagram below well illustrates it.
![[lecture_notes/ECE120/images/Pasted image 20220414213722.png]]

CS means “chip select”. If CS = 1, the memory reads or write; if CS = 0, the memory does nothing.

### Certain Restrictions in ECE120
1. The memory we talk about in ECE120 is **Random Access Memory (RAM)**. Addresses can be read/written (accessed) in any order and the time required to read/write an address does not depend (much) on the address.
2. Besides, we consider only volatile forms of RAM, which lose their bits if electrical power is turned off.
3. There're mainly two types of RAM:
	- **Static RAM (SRAM)** uses a two-inverter loop to store a bit retains bit indefinitely while powered. (faster, less dense)
	- **Dynamic RAM (DRAM)** uses a capacitor to store a bit loses bit over time (_even with electricity!_), so must be refreshed (rewritten) periodically. (slower, more dense)
4. We only talk about SRAM here.

## SRAM Cell
This is a SRAM cell.
![[lecture_notes/ECE120/images/Pasted image 20220414214504.png]]

Two n-type MOSFETs connect the two inverters to the bit lines ($BIT$ and $BIT’$). When $SELECT = 1$, the bit is connected to the bit lines. When $SELECT = 0$, this cell is disconnected.

### Write a Bit
To write a bit in SRAM cell, simply set $SELECT = 1$, then set bit lines held at opposite values. This will force the inverters to store the bit.
![[lecture_notes/ECE120/images/Pasted image 20220414214705.png]]

This operation is a bit dangerous, because it wires together outputs! Changing one bit means short circuit, so the system must be designed carefully.

### Read a Bit
To read bits from the cell, $BIT$ and $BIT'$ should be left floating. Then $SELECT=1$ will write bits to two lines.
![[lecture_notes/ECE120/images/Pasted image 20220414215030.png]]

Normally, to speed up reads, bit lines are pre-charged to $V_{dd}/2$, and sense amplifiers (analog devices) amplify any changes in voltage between bit lines to 0/1.

### 6T Cell
The SRAM cell design is called 6T Cell because it has 6 transistors. The designed is commonly used due to its balance of speed and good reliability with small size.

## Memory Control Circuit
Below is a $16\times 1$ memory.
![[lecture_notes/ECE120/images/Pasted image 20220414215508.png]]

When $CS=1$, the decoder activates the specified cell and then the read/write logic is ready to read or write to the specified cell.

### Non-Clocked Memory
Remind that memory is not clocked by $CLK$ signal. So we need to ensure a read/write has finished before the next move.

There're two ways to accomplish this:
1. The memory designer specifies a minimum wait time (in the datasheet) for a read/write to complete.
2. Or the memory raises an output (called R in Patt and Patel) to indicate that it is Ready for another operation.

### Balance of Speed and Size
When the memory gets larger, the decoder will expand with size. This causes the circuit size very large.

We can use a technique called **Coincident Selection** to significantly reduce the number of gates required. The technique is simply putting a new decoder like the graph below.
![[lecture_notes/ECE120/images/Pasted image 20220414220058.png]]

### Expanding Memory
#### More Addresses
Given two $2^{k}×N$-bit memories, construct a $2^{k+1}×N$-bit memory.
![[lecture_notes/ECE120/images/Pasted image 20220414220617.png]]
#### Wider Addressability
Given two $2^{k}×N$-bit memories, construct a $2^{k}×(2N)$-bit memory.
![[lecture_notes/ECE120/images/Pasted image 20220414220633.png]]

## Tri-State Buffer
The small triangle is a **tri-state buffer**.
![[lecture_notes/ECE120/images/Pasted image 20220414221133.png]]

| EN  | IN  | OUT |
| --- | --- | --- |
| 0   | x   | Z\*  | 
| 1   | 0   | 0   |
| 1   | 1   | 1   |

\* Z means high impedance, input doesn't affect output.

Tri-state buffer is not a CMOS gate! Look at the design:
![[lecture_notes/ECE120/images/Pasted image 20220414221305.png]]

For our memory design, DATA-OUT is gated with tri-state buffers, so these lines float whenever CS = 0 or WE = 1.

In real memory chips, the same pins (wires) can be used for DATA-IN and DATA-OUT.