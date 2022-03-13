## Qualification Problem 1: Epigenomic Marks 2
While having a constant nucleotide sequence, DNA molecules in a cell can be chemically modified in several different ways. For example, the DNA bases can be methylated, or histone proteins, around which DNA is wrapped, can be supplied with chemical tags such as acetylation. It is thought that such modifications (or epigenomic marks) define cell specialization or a cell state when a specific combination of marks regulates how genes are expressed.

In this problem, you are given genomic tracks describing the presence or absence of several epigenomic marks. Your task is to split the genomic positions into the smallest number of states so that each state corresponds to a particular combination of marks.

### Input format
The first line of the input contains _t_ — the number of tests.

Each test consists of multiple lines. The first line contains two integers _n_ and _l_ — the number of sequences and their length. The remaining _n_ lines in the test include sequences of 0 and 1, describing the epigenomic marks. All sequences have the same length _l_. 

### Output format
Your output file should contain _2t_ lines with two lines per test. The first line of the answer on a test should contain the minimal number of used states _s_ to distinguish all combinations of marks. The second line should contain _l_ numbers separated by spaces — the states per each position, encoded as numbers from 1 to _s_.

### Sample input
```
2
4 10
0010001000
1001000001
0101010001
0010001100
2 14
00011100010100
00111000010001
```

### Sample output
```
6
1 2 3 4 5 2 3 6 5 4
4
1 1 2 3 3 4 1 1 1 3 1 4 1 2
```

### Notes
Let us consider the first sample test case. We have the following states (as read by positions): 0100, 0010, 1001, 0110, 0000, 0010, 1001, 0001, 0000, 0110. There are only 6 different states. Thus, we should map them to numbers from 1 to 6 as shown in the sample output.