---
title: "ECE120 Lecture 32 - LC-3 Programming example: letter frequency counter"
---
## Letter Frequency Counter
We wish to design a program that:
- given an ASCII string (a sequence of characters terminated by a `NUL`, ASCII `x00`)
- count the occurrences of each letter (regardless of case)
- and count the number of non-alphabetic characters.

## Planning
### Algorithm I: Look Through String Once for Each Letter
A possible approach is to look for occurrences of each letter one by one.
```
for each letter (and once for non-letters)
	count = 0 
	for each character in the string
	if character matches letter (either case)
		count = count + 1
	store count for the letter in histogram
```

### Algorithm II: Look through String Once

```
initialize 27-bin histogram to all 0s
for each character in the string
	increment the appropriate histogram bin
```

### Algorithm III: Build a Bigger Histogram
```
initialize 128-bin histogram to all 0s
for each character in the string
	increment bin for that character
for each letter
	add the two corresponding bins
sum all non-letter bins
```

### The Best Algorithm Depends
The best algorithm depends on the metrics you choose. But we'll go with algorithm II here because it's both time-efficient and space-efficient.

## Flowchart
