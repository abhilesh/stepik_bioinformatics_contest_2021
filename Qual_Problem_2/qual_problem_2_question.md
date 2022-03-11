## Qualification Problem 2: Metabolite Annotation
​Mass spectrometry is a technique that can be used to detect the presence of metabolites (biochemical compounds) in a sample. In this technique, a neutral metabolite is ionized by gaining or losing a charged fragment (adduct), and then the mass-to-charge ratio is measured for this ionized metabolite. Your task is to annotate mass-spectrometry results: find for a measured mass-to-charge ratio from which metabolite it could come from.

Formally, there is a database of _M_ neutral metabolites with masses _m<sub>i</sub>_ > 0 and a database of _K_ potential adducts with masses _a<sub>i</sub>_ (_a<sub>i</sub>_ can be both positive and negative). Then there are _N_ measured signals _s<sub>i</sub>_ > 0. Each signal _s<sub>i</sub>_ corresponds to some metabolite _m<sub>j</sub>_ _(1 ≤ j ≤ M)_ with an adduct _a<sub>k</sub>_ _(1 ≤ k ≤ K)_ and some noise Δ (can be both positive and negative), that is  _s<sub>i</sub>_ = _m</sub>j</sub>_ + _a<sub>k</sub>_ + Δ, with _m<sub>j</sub>_ + _a<sub>k</sub>_ > 0. 

Your task is to find for each of _N_ signals _s<sub>i</sub>_ the pair of metabolite _m<sub>j</sub>_ and adduct _a<sub>k</sub>_ with the closest sum _m<sub>j</sub>_ + _a<sub>k</sub>_. 

### Input format
The first line of the input contains one integer _T_, _(1 ≤ T ≤ 3)_ - the number of test cases.

Each test case is specified by four lines. The first line of each test case contains three integer numbers _M_, _K_, _N_. The second line contains _M_ numbers _m<sub>i</sub>_ − masses of metabolites _(0 < m<sub>i</sub> ≤ 1000)_. The third line contains _K_ numbers _a<sub>i</sub>_ − masses of adducts _(−1000 ≤ a<sub>i</sub> ≤ 1000)_. The fourth line contains _N_ numbers _s<sub>i</sub>_ − masses of signals _(0 < s<sub>i</sub> ≤ 1000)_. **All the masses are indicated with exactly six decimal places.**

### Output format
For each signal _s<sub>i</sub>_ of each test case, print numbers _j_ and _k_ such that _s<sub>i</sub>_ = _m<sub>j</sub>_ + _a<sub>k</sub>_ + Δ, _m<sub>j</sub>_ + _a<sub>k</sub>_ > 0 and an absolute value of Δ is smallest possible. If there are multiple numbers _j_ and _k_ with same absolute value of Δ for some signal, you can print any of them.

### Sample input

```
3
2 2 5
1.000002 0.000002
0.500000 -0.500000
0.500001 0.500002 0.500003 1.000000 0.000001
2 2 5
1.000002 0.000001
0.500000 -0.500000
0.500001 0.500002 0.500003 1.000000 0.000001
5 4 7
0.000001 0.000002 0.000003 0.000004 0.000005
0.000002 0.000010 0.000001 -0.000001
0.000001 0.000002 0.000100 0.000005 0.000020 0.000010 0.000003
```

### Sample output

``` 
1 2
1 2
1 2
1 2
1 2
2 1
1 2
1 2
1 2
2 1
2 4
1 3
5 2
3 1
5 2
1 2
1 1
```