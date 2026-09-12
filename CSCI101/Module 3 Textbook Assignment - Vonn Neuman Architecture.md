# Module 3 Textbook Assignment - Von Neumann Architecture

### What does W represent when talking about memory?

'W' is the *width* of a memory cell. It is the number of bits stored in each addressable location, and is typically described as **B** * **W** (number of cells x how many bits each cell holds).

---

### At minimum how many bits are needed in the MAR for each of the following memory sizes?

- 256 MB: *28*
- 45 KB: *16*
- 98 MB: *27*
- 128 KB: *17*
- 2 GB: *31*
- 6 GB: *33*
- 16 GB: *34*
- 1 TB: *40*

---

### How many memory cells are contained in 16 GB of memory?

16GB = 2<sup>4</sup> x 2<sup>30</sup> = 2<sup>34</sup> = 17,179,869,184 cells

---

### What is a ROM? How is it different from RAM?

*ROM*: 'Read-Only Memory' is non-volatile, and its contents are written only once or very rarely, and is used for firmware such as the boot/startup code.
*RAM*: 'Random Access Memory' is volatile, losing data when it loses power, supports read and write operations, and is used for active programs and data.

---

### In 2D memory that has 8GB (8 * 230 bytes):

#### What are the dimensions? *2<sup>17</sup> x 2<sup>16</sup>*
#### How large would the MAR be? *33 bits*
#### How many bits are sent to each of the row and column decoders? *17 bits to the row decoded, 16 bits to the column decoder*
#### How many output lines would each of the decoders have? *row decoder output = 2<sup>17</sup> lines, column decoder output = 2<sup>16</sup> lines*

---

### Assume a 64-bit MAR that is organized with 32 bits for the row selector and 32 bits for the column selector.

#### What is the maximum size of the memory unit on this machine? Put your answer in terms of XB where X represents one of the byte units like G is Giga. *2<sup>64</sup> bytes = 16 Exabytes*
#### What is the byte unit for 2<sup>60</sup>? *Exabyte*
#### What are the dimensions of the memory (in bytes) assuming a square 2D organization? *2<sup>32</sup> x 2<sup>32</sup> = 4,294,967,296 × 4,294,967,296*

