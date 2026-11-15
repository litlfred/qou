---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-015-erdős-125
section_title: "Erdős #125"
section_number: null
pages: 34-35
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
Question. Let 𝐴= {Í 𝜖𝑘3𝑘: 𝜖𝑘∈{0, 1}} be the set of integers which have only the digits 0,1
when written base 3, and 𝐵= {Í 𝜖𝑘4𝑘: 𝜖𝑘∈{0, 1}} be the set of integers which have only
the digits 0, 1 when written base 4. Does 𝐴+ 𝐵have positive lower density?
Proof. We show that the answer is no: the lower density is zero. Let 𝐴and 𝐵be defined as
the sets of integers whose base 3 and base 4 representations, respectively, contain only the
digits 0 and 1. We will show that the lower density of 𝐴+ 𝐵is zero.
For any integer 𝑎∈𝐴, we can decompose it at the 𝑘-th digit into a top and bottom part,
writing 𝑎= 3𝑘𝑎𝑡𝑜𝑝+ 𝑎𝑏𝑜𝑡. Because 𝑎uses only the digits 0 and 1, both 𝑎𝑡𝑜𝑝and 𝑎𝑏𝑜𝑡must also
belong to 𝐴. Furthermore, the maximum possible value for 𝑎𝑏𝑜𝑡is the integer consisting of 𝑘
ones in base 3, which provides the strict upper bound 𝑎𝑏𝑜𝑡≤(3𝑘−1)/2. By applying the exact
same logic to any 𝑏∈𝐵at scale 𝑚, we can write 𝑏= 4𝑚𝑏𝑡𝑜𝑝+ 𝑏𝑏𝑜𝑡, yielding the analogous
bound 𝑏𝑏𝑜𝑡≤(4𝑚−1)/3.
To evaluate the density of 𝐴+ 𝐵up to a large scale, we define a threshold 𝑀· 𝑁0, where
𝑀= min(3𝑘, 4𝑚) for some integers 𝑘and 𝑚. Consider any element 𝑥∈𝐴+ 𝐵such that
𝑥< 𝑀· 𝑁0. By definition, 𝑥= 𝑎+ 𝑏for some 𝑎∈𝐴and 𝑏∈𝐵. Using the previously established
decompositions, we can express this sum as 𝑥= 3𝑘𝑎𝑡𝑜𝑝+ 𝑎𝑏𝑜𝑡+ 4𝑚𝑏𝑡𝑜𝑝+ 𝑏𝑏𝑜𝑡. Assume without
loss of generality that 3𝑘≤4𝑚, so 𝑀= 3𝑘. We can rewrite this expression to factor out 𝑀,
yielding 𝑥= 3𝑘(𝑎𝑡𝑜𝑝+ 𝑏𝑡𝑜𝑝) + 𝑐, where the remainder term is 𝑐= (4𝑚−3𝑘)𝑏𝑡𝑜𝑝+ 𝑎𝑏𝑜𝑡+ 𝑏𝑏𝑜𝑡.
Let 𝑦= 𝑎𝑡𝑜𝑝+ 𝑏𝑡𝑜𝑝. Since 𝑎𝑡𝑜𝑝∈𝐴and 𝑏𝑡𝑜𝑝∈𝐵, it naturally follows that 𝑦∈𝐴+ 𝐵.
Furthermore, because 𝑥< 3𝑘𝑁0, we must have 𝑦< 𝑁0, which in turn dictates that 𝑏𝑡𝑜𝑝≤𝑁0.
Applying our bounds for the bottom parts, we can bound the remainder 𝑐by a maximum
value 𝐶, defined as 𝐶= |4𝑚−3𝑘|𝑁0 + (3𝑘−1)/2 + (4𝑚−1)/3.
This shows that any valid sum 𝑥< 𝑀· 𝑁0 is uniquely determined by choosing a base value
𝑦∈(𝐴+ 𝐵) ∩[0, 𝑁0) and a remainder 𝑐∈[0, 𝐶]. Therefore, the total number of elements in
𝐴+ 𝐵strictly less than 𝑀· 𝑁0 is bounded by the product of the number of choices for 𝑦and
the number of choices for 𝑐. Dividing by the interval length 𝑀· 𝑁0 yields an upper bound on
the density at this new scale: the density up to 𝑀· 𝑁0 is less than or equal to the density up
to 𝑁0 multiplied by the factor (𝐶+ 1)/𝑀.
To force the density to drop, we require this multiplying factor to be strictly less than 1.
Because the ratio of logarithms ln(4)/ln(3) is irrational, Dirichlet’s Approximation Theorem
guarantees that we can find arbitrarily large integers 𝑘and 𝑚such that the ratio 4𝑚/3𝑘is
arbitrarily close to 1. By choosing 𝑘and 𝑚carefully, the absolute difference |4𝑚−3𝑘| becomes
extremely small relative to 𝑀. Consequently, for any given 𝑁0, we can select 𝑘and 𝑚large
enough such that (𝐶+ 1)/𝑀≤0.99.
We can now apply this bounding process iteratively. Starting from an arbitrary scale 𝑁0,
we can find a larger scale 𝑁1 = 𝑀1𝑁0 where the density of 𝐴+ 𝐵drops by a factor of at least
0.99. Taking 𝑁1 as our new baseline, we find a still larger scale 𝑁2 = 𝑀2𝑁1 where the density
drops by another factor of 0.99. After 𝑟iterations, the density of the set up to the scale 𝑁𝑟is
bounded by (0.99)𝑟. As 𝑟→∞, this bound approaches 0. This demonstrates the existence of
a sequence of arbitrarily large scales where the density tends to 0, proving that the lower
density of 𝐴+ 𝐵is 0.
□
34
Advancing Mathematics Research with AI-Driven Formal Proof Search
We originally communicated the result in https://www.erdosproblems.com/fo
rum/thread/125#post-5110. The Lean proof is at https://github.com/google-d
eepmind/alphaproof-nexus-results/blob/main/APNOutputs/ErdosProblem
s/erdos_125.variants.positive_lower_density.lean. In the discussion at the
ErdosProblems site, it was pointed out that this leaves two possibilities regarding the set
𝐴+ 𝐵:
1. 𝐴+ 𝐵has zero upper and lower density (and hence also zero density), or
2. 𝐴+ 𝐵has zero lower density, but positive upper density (and hence no density).
