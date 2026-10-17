---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-013-deformalized-lean-proofs
section_title: "Deformalized Lean Proofs"
section_number: null
pages: 30-59
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 15 sections: Front matter; Introduction; AlphaProof Nexus"
---
Next, we give deformalized versions of the Lean proofs discovered by our full-featured Agent
(D).
Erdős #12-(i)
First, we give the proof of the first question under Erdős problem #12, as classified on the
ErdosProblems site (https://www.erdosproblems.com).
Theorem (i). There is an infinite set 𝐴⊆ℕsatisfying that there are no distinct 𝑎, 𝑏, 𝑐∈𝐴
with 𝑎< 𝑏, 𝑐satisfying 𝑎|𝑏+ 𝑐and
lim inf
𝑁→∞
|𝐴∩{1, . . . , 𝑁}|
𝑁1/2
> 0.
Proof. We will construct a sequence of "blocks" that individually cannot contain such 𝑎, 𝑏, 𝑐,
and with a careful choice of parameters, their union forms the desired set. By precisely
controlling the growth and modular residues of these blocks, we ensure the set remains
dense enough to satisfy the lim inf condition while avoiding all forbidden divisibility relations.
Let 𝑓: ℕ→ℕbe defined by 𝑓(0) = 0 and 𝑓(𝑛) = 3 𝑓(⌊𝑛/2⌋) + (𝑛mod 2). The func-
tion 𝑓takes a number represented in base 2 and outputs the number given by the same
representation but read in base 3. In particular, the base 3 representation of 𝑓(𝑛) will contain
only 0s and 1s. For this reason, 𝑓(𝑎) + 𝑓(𝑏) = 2 𝑓(𝑐) implies 𝑎= 𝑏= 𝑐, ensuring the sequence
( 𝑓(𝑛))𝑛∈ℕcontains no 3-APs.
Next, let 𝐹𝑖be the 𝑖-th odd prime, and write 𝑀𝑖= Î
𝑗<𝑖𝐹𝑗and 𝑉𝑖= 𝐹𝑖𝑀𝑖. By Bertrand’s
postulate, we have 𝐹𝑖≤2𝑖+2. By the Chinese Remainder Theorem, for each 𝑖, let 𝐶𝑖< 𝑉𝑖be
the unique integer such that 𝐶𝑖≡0 (mod 𝐹𝑖) and 𝐶𝑖≡1 (mod 𝑀𝑖).
Now we define the parameters for the blocks (𝐵𝑖). Let
• 𝑌𝑖= 3(𝑖+20)3 be the exponential bounding scale to control the distance between blocks.
• 𝑃𝑖= 10𝑉𝑖𝑌𝑖+ 𝐶𝑖be the starting coordinate of block 𝑖.
• 𝑋𝑖= ⌊√
𝑃𝑖+1⌋be the element capacity of block 𝑖. Note that the capacity of 𝐵𝑖is directly
tied to the starting point of the next block 𝐵𝑖+1.
30
Advancing Mathematics Research with AI-Driven Formal Proof Search
Formally, define 𝐵𝑖= {𝑃𝑖+ 𝑉𝑖𝑓(𝑦) | 𝑦< 𝑋𝑖}. The purpose of 𝑌𝑖is to keep the blocks relatively
narrow while ensuring they are well-spaced. Note that if 𝑦< 2𝑘, then 𝑓(𝑦) < 3𝑘. Letting
𝑘= (𝑖+ 20)3, we want to guarantee that for any 𝑦< 𝑋𝑖, we have 𝑓(𝑦) < 𝑌𝑖= 3𝑘. To do this, it
suffices to show 𝑋𝑖≤√
𝑃𝑖+1 < 2𝑘, which is equivalent to 𝑃𝑖+1 ≤4𝑘.
Observe that 𝑃𝑖+1 ≤11𝑉𝑖+1𝑌𝑖+1 ≤11 · 2(𝑖+4)2 · 3(𝑖+21)3, following from the bound on 𝐹𝑖.
This is asymptotically strictly smaller than 4𝑘= 4(𝑖+20)3. By adding the shift of 20, the
inequality 11 · 2(𝑖+4)2 · 3(𝑖+21)3 ≤4(𝑖+20)3 holds universally for all 𝑖≥1.
Set 𝐴= Ð
𝑖∈ℕ𝐵𝑖. Clearly, 𝐴is an infinite set. Suppose, for the sake of contradiction, that there
exist distinct 𝑎, 𝑏, 𝑐∈𝐴with 𝑎< 𝑏, 𝑐such that 𝑎| (𝑏+ 𝑐). Let 𝑎∈𝐵𝑖. We analyze two cases:
• (Case 1: Cross-block) Suppose at least one of 𝑏, 𝑐is not in 𝐵𝑖. Without loss of generality,
assume 𝑏∈𝐵𝑗for some 𝑗> 𝑖(since 𝑏> 𝑎). Since 𝑎∈𝐵𝑖, we have 𝑎≡0 (mod 𝐹𝑖), and
thus 𝑏+ 𝑐≡0 (mod 𝐹𝑖) by the divisibility condition. However, by our CRT construction,
𝑏≡1 (mod 𝐹𝑖). The element 𝑐must belong to some block 𝐵𝑚with 𝑚≥𝑖, so 𝑐≡0
(mod 𝐹𝑖) (if 𝑚= 𝑖) or 𝑐≡1 (mod 𝐹𝑖) (if 𝑚> 𝑖). Therefore, 𝑏+ 𝑐≡1 (mod 𝐹𝑖) or
𝑏+ 𝑐≡2 (mod 𝐹𝑖). Since 𝐹𝑖≥3, this directly contradicts 𝑏+ 𝑐≡0 (mod 𝐹𝑖).
• (Case 2: Same block) Suppose 𝑏, 𝑐∈𝐵𝑖. They must be tightly clustered around 𝑃𝑖.
Because 𝑦< 𝑋𝑖, we have 𝑓(𝑦) < 𝑌𝑖. The maximum "noise" added to any block element is
𝑉𝑖𝑌𝑖. Since 𝑃𝑖> 10𝑉𝑖𝑌𝑖, any 𝑥∈𝐵𝑖must satisfy 𝑥∈[𝑃𝑖, 1.1𝑃𝑖]. The divisibility condition
𝑎| (𝑏+ 𝑐) implies 𝑚𝑎= 𝑏+ 𝑐for some integer 𝑚. Because 𝑏+ 𝑐∈[2𝑃𝑖, 2.2𝑃𝑖] and
𝑎∈[𝑃𝑖, 1.1𝑃𝑖], it must be that 𝑚= 2, implying 2𝑎= 𝑏+ 𝑐.
Writing the elements as 𝑎= 𝑃𝑖+ 𝑉𝑖𝑓(𝑎′), 𝑏= 𝑃𝑖+ 𝑉𝑖𝑓(𝑏′), and 𝑐= 𝑃𝑖+ 𝑉𝑖𝑓(𝑐′), substitution and
cancellation yield 2 𝑓(𝑎′) = 𝑓(𝑏′) + 𝑓(𝑐′). This is impossible for distinct 𝑎′, 𝑏′, 𝑐′ because the
image of 𝑓avoids 3-APs, contradicting the assumption that 𝑎, 𝑏, 𝑐are distinct.
Finally, we show that 𝐶(𝑁) = |𝐴∩{1, . . . , 𝑁}| ≥𝑐
√
𝑁for some constant 𝑐> 0. We split
into two cases:
1. 𝑁falls in the gap between 𝐵𝑖and 𝐵𝑖+1; precisely, 𝑃𝑖+ 𝑉𝑖𝑌𝑖≤𝑁< 𝑃𝑖+1. Here, 𝐶(𝑁)
counts at least all elements in 𝐵𝑖, meaning 𝐶(𝑁) ≥𝑋𝑖= ⌊√
𝑃𝑖+1⌋. Since 𝑁≤𝑃𝑖+1, we
have
√
𝑁≤√
𝑃𝑖+1. Thus, 𝐶(𝑁)
√
𝑁≥⌊√𝑃𝑖+1⌋
√𝑃𝑖+1 ≈1.
2. 𝑁is inside the block 𝐵𝑖; precisely, 𝑃𝑖≤𝑁< 𝑃𝑖+ 𝑉𝑖𝑌𝑖. A pessimistic lower bound counts
only the elements up to the previous block, giving 𝐶(𝑁) ≥𝑋𝑖−1 = ⌊√
𝑃𝑖⌋. Observe that
𝑉𝑖𝑌𝑖≤0.1𝑃𝑖, so 𝑁≤1.1𝑃𝑖< 2𝑃𝑖. Consequently, √
𝑃𝑖>
√︁
𝑁/2, which implies 𝐶(𝑁)
√
𝑁≥
1
√
2.
In both cases, lim inf𝑁→∞
𝐶(𝑁)
𝑁1/2 ≥
1
√
2 > 0.
□
Erdős #12-(ii)
Next, we give a proof for the second question of the three listed in Erdős #12.
Theorem (ii). There exists an infinite set 𝐴⊂ℤ+ with no distinct 𝑎, 𝑏, 𝑐∈𝐴with 𝑏, 𝑐> 𝑎,
31
Advancing Mathematics Research with AI-Driven Formal Proof Search
and 𝑎|𝑏+ 𝑐, yet for any 𝜀> 0 and all sufficiently large 𝑁:
|𝐴∩{1, . . . , 𝑁}| ≥𝑁1−𝜀.
Consequently, there is no absolute constant 𝑐> 0 such that every such set 𝐴satisfies
|𝐴∩{1, . . . , 𝑁}| < 𝑁1−𝑐for infinitely many 𝑁.
Proof. The proof is similar to the previous one for Erdős #12(i), differing mainly in the use
of a Behrend-style construction to produce a dense 3-AP-free set.
Let 𝑐∈(0, 1), and let (𝑃𝑘) be a sequence of pairwise coprime integers with 𝑃𝑘≥3
and 𝑃𝑘≤4𝑘+2 (for example, we can choose 𝑃𝑘to be the 𝑘-th odd prime). Next, define the
running product 𝐿𝑘= Î𝑘
𝑖=0 𝑃𝑖. As before, we have 𝐿𝑘≤4(𝑘+2)2. By the Chinese Remainder The-
orem, there are integers 𝑅𝑘< 𝐿𝑘satisfying 𝑅𝑘≡0 (mod 𝑃𝑘) and 𝑅𝑘≡1 (mod 𝑃𝑖) for all 𝑖< 𝑘.
Choose an integer 𝑚≥2 satisfying 𝑚> (2𝑚+1)1−𝑐/2 and define the dimension 𝑉𝑘= (𝑘+10)4.
We use a construction of Behrend to generate dense sets free of 3-term arithmetic progres-
sions. Consider the grid of vectors {1, . . . , 𝑚}𝑉𝑘−1. Let 𝑣= (𝑣0, . . . , 𝑣𝑉𝑘−2) be such a vector. The
squared norm ∥𝑣∥2
2 takes integer values in the range [𝑉𝑘−1, (𝑉𝑘−1)𝑚2]. By the pigeonhole
principle, there exists an integer radius 𝐾such that the number of vectors on this sphere
satisfies |{𝑣∈{1, . . . , 𝑚}𝑉𝑘−1 | ∥𝑣∥2
2 = 𝐾}| ≥𝑚𝑉𝑘−1/(𝑉𝑘𝑚2 + 1).
Define 𝑆𝑘as the set of integers formed by evaluating these vectors in base 2𝑚+ 1, strictly
offset by adding a massive leading digit 𝑚(2𝑚+ 1)𝑉𝑘−1:
𝑆𝑘=
(
𝑚(2𝑚+ 1)𝑉𝑘−1 +
𝑉𝑘−2
∑︁
𝑖=0
𝑣𝑖(2𝑚+ 1)𝑖

 𝑣∈{1, . . . , 𝑚}𝑉𝑘−1,
𝑉𝑘−2
∑︁
𝑖=0
𝑣2
𝑖= 𝐾
)
Because the digits are bounded by 𝑚, adding two elements in base 2𝑚+ 1 involves no
carrying. The restriction to the sphere of radius
√
𝐾ensures 𝑆𝑘contains no 3-APs. Further-
more, because the vectors use digits strictly between 1 and 𝑚, every element 𝑥∈𝑆𝑘satisfies
𝑚(2𝑚+ 1)𝑉𝑘−1 ≤𝑥< (𝑚+ 1)(2𝑚+ 1)𝑉𝑘−1, ensuring the set is tightly clustered.
We define the blocks 𝐴𝑘= {𝐿𝑘𝑥+ 𝑅𝑘| 𝑥∈𝑆𝑘}, and set 𝐴= Ð
𝑘∈ℕ𝐴𝑘. Clearly, 𝐴is an in-
finite set. We verify 𝐴contains no distinct 𝑎, 𝑏, 𝑐such that 𝑎| (𝑏+ 𝑐) with 𝑏, 𝑐> 𝑎. If 𝑎, 𝑏, 𝑐are
in different blocks, a similar modular arithmetic argument as before using the CRT conditions
yields a contradiction. If they are in the same block, the tightness of 𝑆𝑘guarantees 𝑏+ 𝑐< 3𝑎,
forcing the divisibility multiplier to be exactly 2 (i.e., 2𝑎= 𝑏+ 𝑐), which contradicts the fact
that 𝑆𝑘is 3-AP-free. To ensure the blocks 𝐴𝑘do not overlap, we bound their elements. The
maximum element in 𝐴𝑘is bounded above by:
max(𝐴𝑘) ≤𝐿𝑘(𝑚+ 1)(2𝑚+ 1)𝑉𝑘−1
The minimum element in the next block 𝐴𝑘+1 is bounded below by:
min(𝐴𝑘+1) ≥𝐿𝑘+1𝑚(2𝑚+ 1)𝑉𝑘+1−1
Because the dimension 𝑉𝑘+1 = (𝑘+ 11)4 is significantly larger than 𝑉𝑘= (𝑘+ 10)4, the base
exponent strictly dominates, separating the blocks.
32
Advancing Mathematics Research with AI-Driven Formal Proof Search
We now show that |𝐴∩{1, . . . , 𝑁}| ≥𝑁1−𝑐for sufficiently large 𝑁. The density drops
the most in the empty gaps between blocks, with the absolute minimum occurring immedi-
ately before block 𝐴𝑘+1 begins. At this point, 𝑁= min(𝐴𝑘+1) −1, and our total element count
is strictly greater than |𝐴𝑘|. Thus, it suffices to prove:
|𝐴𝑘| ≥(max(𝐴𝑘+1))1−𝑐
Substituting our parameter bounds into this inequality yields, and since 𝑚was chosen to
satisfy 𝑚> (2𝑚+ 1)1−𝑐/2, it remains to prove

(2𝑚+ 1)1−𝑐/2𝑉𝑘−1
𝑉𝑘𝑚2 + 1
≥

𝐿𝑘+1(𝑚+ 1)(2𝑚+ 1)𝑉𝑘+1−11−𝑐
Ignoring the polynomial denominator and constant multipliers, we compare the asymptotic
growth of the exponents on the base 2𝑚+ 1:
• On the left hand side, the exponent is (1 −𝑐/2)(𝑉𝑘−1) = (1 −𝑐/2)𝑘4 + 𝑂(𝑘3).
• On the right hand side, the exponent is (1 −𝑐)(𝑉𝑘+1 −1) = (1 −𝑐)(𝑘+ 11)4 = (1 −𝑐)𝑘4 +
𝑂(𝑘3).
The contribution of the running product 𝐿𝑘+1 ≤4(𝑘+3)2 and the constant (𝑚+ 1) to the right
hand side is only 𝑂(𝑘2), which is safely absorbed into the 𝑂(𝑘3) error term. Because 𝑐> 0,
the 𝑘4 coefficient on the left hand side (1 −𝑐/2) is strictly greater than the 𝑘4 coefficient on
the right hand side (1 −𝑐). Thus, for sufficiently large 𝑘, the left hand side asymptotically
dominates, and the inequality holds.
□
These questions were posed in 1970 [18], and saw attention from multiple human math-
ematicians, achieving partial results towards the questions [54, 7, 17]. We thank Thomas
Bloom for summarizing the history regarding these questions on the ErdosProblems site
(https://www.erdosproblems.com).
Note that the answer to the (ii) implies the answer to (i). Nevertheless, we included both
proofs as the agent found them independently, as each question was separately formalized as
a theorem in Formal Conjectures. Originally, the agent located multiple proofs for the second
question, though we chose the first proof to informalize for presentation. It also happened
to differ the most in the construction, which otherwise is quite similar to the proof for (i).
After sharing the solutions publicly, it was noted that a minor adjustment could be performed
on the construction from the original paper to answer the questions. The third and final
question, asking whether such a set 𝐴could satisfy Í
𝑎∈𝐴1/𝑎= ∞, is still open and seems
difficult.
We provide the Lean proof discovered for (i) at https://github.com/google-dee
pmind/alphaproof-nexus-results/blob/main/APNOutputs/ErdosProblems/er
dos_12.parts.i.lean and for (ii) at https://github.com/google-deepmind/alph
aproof-nexus-results/blob/main/APNOutputs/ErdosProblems/erdos_12.par
ts.ii.lean. Our original communication of the result can be found at the problem thread
of the ErdosProblems site: https://www.erdosproblems.com/forum/thread/12.
33
Advancing Mathematics Research with AI-Driven Formal Proof Search
Erdős #125
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
Erdős #138, Differences Variant
Question. Let the van der Waerden number 𝑊(𝑘) be such that whenever 𝑁≥𝑊(𝑘) and
{1, . . . , 𝑁} is 2-coloured there must exist a monochromatic 𝑘-term arithmetic progression. Is
it true that 𝑊(𝑘+ 1) −𝑊(𝑘) →∞?
Proof. We will show that 𝑊(𝑘+ 1) ≥𝑊(𝑘) + 𝑘, which establishes that 𝑊(𝑘+ 1) −𝑊(𝑘) →∞.
Given a 2-coloring of the first 𝑊(𝑘) −1 integers without a monochromatic 𝑘-AP, we can
extend it by 𝑘further elements without creating a monochromatic (𝑘+ 1)-AP by proceeding
greedily. Adding new elements one by one, suppose we have validly colored up to 𝑀(where
𝑀< 𝑊(𝑘) −1 + 𝑘); we simply color 𝑀+ 1 red if doing so doesn’t create a red (𝑘+ 1)-AP, and
blue otherwise.
The only way this algorithm could result in an invalid coloring is if both choices are
blocked, meaning there is already a red 𝑘-AP with some step size 𝑑𝑅and a blue 𝑘-AP with
some step size 𝑑𝐵such that the (𝑘+1)-th element for both progressions lands exactly on 𝑀+1.
But this is impossible. Because our original interval up to 𝑊(𝑘) −1 has no monochromatic
𝑘-APs, these progressions must contain at least one newly added element, which bounds their
step sizes to 𝑑𝑅, 𝑑𝐵≤𝑘−1. Hence, if we step backward 𝑑𝐵times along the red progression
and 𝑑𝑅times along the blue progression, both calculations land exactly on the positive integer
𝑀+ 1 −𝑑𝑅𝑑𝐵, meaning this single point would have to be simultaneously colored red and
blue, which is a contradiction.
□
We originally communicated the result in https://www.erdosproblems.com/foru
m/thread/138#post-5314, and share the Lean proof at https://github.com/googl
e-deepmind/alphaproof-nexus-results/blob/main/APNOutputs/ErdosProbl
ems/erdos_138.variants.difference.lean. In the discussion at the ErdosProblems
site, Thomas Bloom pointed out that the obvious generalization of this argument gives
𝑊(𝑘+ 1, 𝑙+ 1) ≥𝑊(𝑘, 𝑙) + min(𝑘, 𝑙), and asked what this kind of argument can prove for the
𝑟-color variant 𝑊𝑟(𝑘).
Erdős #741-(i)
Question. Let 𝐴⊆ℕbe such that 𝐴+ 𝐴has positive upper density. Can one always decompose
𝐴= 𝐴1 ⊔𝐴2 such that 𝐴1 + 𝐴1 and 𝐴2 + 𝐴2 both have positive upper density?
Proof. We show that the answer is yes. We use an alternating block partition. Given a rapidly
35
Advancing Mathematics Research with AI-Driven Formal Proof Search
growing sequence 𝑀0 < 𝑀1 < 𝑀2 < · · · , we define
𝐴1 = 𝐴∩
Ø
𝑘
(𝑀2𝑘, 𝑀2𝑘+1],
𝐴2 = 𝐴\ 𝐴1.
In odd-indexed intervals (𝑀2𝑘, 𝑀2𝑘+1], all elements of 𝐴belong to 𝐴1; in even-indexed inter-
vals (𝑀2𝑘+1, 𝑀2𝑘+2], they all belong to 𝐴2. The sequence 𝑀is chosen to grow fast enough
that each block dwarfs all previous ones. We split into two cases.
Case 1: 𝐴has positive upper density. There exist a constant 𝑐> 0 and a strictly in-
creasing sequence of scales along which |𝐴∩[1, 𝑁]| ≥𝑐· 𝑁. Using a dependent-choice
argument, we extract a rapidly growing sequence 𝑀𝑘such that for each 𝑘:
• |𝐴∩[1, 𝑀𝑘+1]| ≥𝑐· 𝑀𝑘+1 (density is retained at the next scale),
• |𝐴∩[1, 𝑀𝑘]| ≤𝑐
4 · 𝑀𝑘+1 (the “past” is negligible relative to the “future”).
Because each new block contains all the “fresh” elements of 𝐴, looking at scale 𝑀2𝑘+1 shows
that 𝐴1 has positive upper density, and looking at scale 𝑀2𝑘+2 shows the same for 𝐴2. A
short argument then lifts this: if a set has positive upper density, so does its sumset with itself.
Case 2: 𝐴has zero upper density but 𝐴+ 𝐴has positive upper density. This is the
harder case, since 𝐴is too sparse to guarantee positive density for the parts directly. Instead,
we argue about the sumsets themselves. Since 𝐴+ 𝐴has positive upper density, there exist
𝑐> 0 and a sequence of scales along which |(𝐴+ 𝐴) ∩[1, 𝑁]| ≥𝑐· 𝑁. Since 𝐴has zero
upper density, |𝐴∩[1, 𝑁]| = 𝑜(𝑁), so for any fixed 𝐾there are arbitrarily large 𝑁where
(𝐾+ 1) · |𝐴∩[1, 𝑁]| ≤𝑐
4 · 𝑁. By dependent choice, we extract a rapidly growing 𝑀𝑘such that
for each 𝑘:
• |(𝐴+ 𝐴) ∩[1, 𝑀𝑘+1]| ≥𝑐· 𝑀𝑘+1,
• (𝑀𝑘+ 1) · |𝐴∩[1, 𝑀𝑘+1]| ≤𝑐
4 · 𝑀𝑘+1.
The key ingredient is a combinatorial sumset bound: if 𝐴= 𝐴1 ∪𝐴2 and every element of 𝐴2
in [1, 𝑁] is at most 𝐾, then
|(𝐴+ 𝐴) ∩[1, 𝑁]| ≤|(𝐴1 + 𝐴1) ∩[1, 𝑁]| + (𝐾+ 1) · |𝐴∩[1, 𝑁]|.
The idea is that any sum involving an element of 𝐴2 has one summand bounded by 𝐾, giving
at most (𝐾+ 1) · |𝐴∩[1, 𝑁]| such sums. Applying this bound at alternating scales:
• At scale 𝑁= 𝑀2𝑘+1: all elements of 𝐴2 in [1, 𝑁] lie below 𝑀2𝑘, so the bound with
𝐾= 𝑀2𝑘gives |(𝐴1 + 𝐴1) ∩[1, 𝑁]| ≥3𝑐
4 · 𝑁.
• At scale 𝑁= 𝑀2𝑘+2: symmetrically, all elements of 𝐴1 in [1, 𝑁] lie below 𝑀2𝑘+1, giving
|(𝐴2 + 𝐴2) ∩[1, 𝑁]| ≥3𝑐
4 · 𝑁.
Since these bounds hold for infinitely many 𝑁, both sumsets have positive upper density. □
The agent also initially disproved a strict “natural density” formulation of this problem
(where the density must exist as a limit), which served as a diagnostic for the correct
36
Advancing Mathematics Research with AI-Driven Formal Proof Search
interpretation of Erdős’ original phrasing. Following Thomas Bloom’s observation that Erdős
likely meant “positive upper density,” the formulation was amended and the agent resolved
the corrected version as described above. The Lean proof for the upper density variant is
available at https://github.com/google-deepmind/alphaproof-nexus-results
/blob/main/APNOutputs/ErdosProblems/erdos_741.parts.i.lean.
Erdős #741-(ii)
Question. Is there a basis 𝐴of order 2 such that if 𝐴= 𝐴1 ⊔𝐴2 then 𝐴1 + 𝐴1 and 𝐴2 + 𝐴2
cannot both have bounded gaps?
Proof. We show that the answer is yes by constructing a pathological basis 𝐴with “forbidden
zones” that force any partition to create arbitrarily large gaps in at least one component
sumset.
Step 1: The construction. Choose a sequence of rapidly growing scales 𝑃𝑘= 100𝑘. For each
𝑘≥1, define a forbidden zone 𝑍𝑘, which is a broad interval of integers running roughly
from 11
2 𝑃𝑘to 11𝑃𝑘+ 𝑘. In the middle of this zone, we leave a single “oasis” — an isolated
element 𝑥𝑘= 10𝑃𝑘. The set 𝐴consists of all natural numbers that avoid every forbidden
zone, together with the oases 𝑥𝑘. In visual terms, 𝐴is made of clumps of consecutive integers
separated by large empty gaps, each containing a single survivor 𝑥𝑘.
Step 2: 𝐴∪{0} is a basis of order 2. We must show every natural number 𝑛can be
written as 𝑎+ 𝑏with 𝑎, 𝑏∈𝐴∪{0}:
• If 𝑛∉𝑍𝑘for any 𝑘, then 𝑛∈𝐴and we use 𝑛+ 0 = 𝑛.
• If 𝑛∈𝑍𝑘and 𝑛lies in the lower half of 𝑍𝑘, we use ⌊𝑛/2⌋+ ⌈𝑛/2⌉. Because 𝑛is small
enough, neither half lands in 𝑍𝑘, and both are large enough to avoid the previous zone
𝑍𝑘−1.
• If 𝑛∈𝑍𝑘and 𝑛lies in the upper half, we use the oasis: 𝑛= 𝑥𝑘+ (𝑛−𝑥𝑘). The difference
𝑛−𝑥𝑘is small enough that it falls safely before the forbidden zone 𝑍𝑘.
Step 3: No syndetic partition exists. Suppose 𝐴= 𝐴1 ⊔𝐴2. Consider a target sum
𝑚∈[11𝑃𝑘, 11𝑃𝑘+ 𝑘]. To write 𝑚= 𝑢+ 𝑣with 𝑢, 𝑣∈𝐴, the algebra forces the larger operand
𝑣to land inside the forbidden range [ 11
2 𝑃𝑘, 11𝑃𝑘+ 𝑘]. But the only element of 𝐴in this range
is 𝑥𝑘. Therefore, representing any sum in [11𝑃𝑘, 11𝑃𝑘+ 𝑘] requires 𝑥𝑘.
By the pigeonhole principle, 𝑥𝑘belongs to exactly one partition component, say 𝐴1. Then
𝐴1 + 𝐴1 can cover the interval [11𝑃𝑘, 11𝑃𝑘+ 𝑘] using 𝑥𝑘, but 𝐴2 + 𝐴2 is completely locked out
— it cannot represent any element in that interval. This leaves a gap of length 𝑘in 𝐴2 + 𝐴2.
Since 𝑘can be made arbitrarily large, the gaps in one component’s sumset are unbounded,
proving it is impossible to partition 𝐴so that both sumsets have bounded gaps.
□
The Lean proof for part (ii) is available at https://github.com/google-deepmind/
alphaproof-nexus-results/blob/main/APNOutputs/ErdosProblems/erdos_12
.parts.ii.lean. Our original communication of both results can be found in the problem
thread on the ErdosProblems site (https://www.erdosproblems.com/forum/thread
/741).
37
Advancing Mathematics Research with AI-Driven Formal Proof Search
Erdős #26, More General Variant
Theorem. Let M(𝑆) denote the set of multiples of a subset 𝑆⊆ℕ, and let 𝑑(𝑋) denote
the upper asymptotic density of a set 𝑋. There exists a sequence 𝐴: ℕ→ℕsatisfying
Í
𝑖∈ℕ1/𝐴(𝑖) = ∞, such that for 𝜖= 1/4 and for all 𝑘≥1, we have 𝑑(M(𝐴+ 𝑘)) < 1 −𝜖.
Proof. We construct the sequence iteratively in finite blocks and show that for any arbitrary
shift 𝑘, we can bound the upper density of the shifted sequence by analyzing three distinct
cases, the third case relying on the construction being similar to the simple counterexample
of Ruzsa which resolved the original question Erdős #26.
Let (𝑞𝑗)∞
𝑗=1 be a strictly increasing sequence of primes satisfying 𝑞1 ≥29 (chosen large
enough to cause small enough density in the infinite tail of the sequence). We define a
strictly increasing sequence of indices (or “jumps”) (𝐽𝑚)∞
𝑚=0 recursively, starting with 𝐽0 = 0.
Suppose 𝐽𝑚has been defined, and the sequence 𝐴(𝑖) has been constructed for all 𝑖< 𝐽𝑚. We
define the parameters for the 𝑚-th block as follows.
First, define the step size 𝑃𝑚= Î10𝐽𝑚
𝑗=1 𝑞𝑗. Next, by the Chinese Remainder Theorem, we can
choose a base size 𝑅𝑚satisfying the following system of congruences
𝑅𝑚≡−𝑗
(mod 𝑞𝑗)
for 1 ≤𝑗≤10𝐽𝑚
as well as the strict monotonicity condition 𝑅𝑚> 𝐴(𝐽𝑚−1) (where we set 𝐴(−1) = 0), by
adding enough multiples of 𝑃𝑚.
With 𝑅𝑚and 𝑃𝑚fixed, the series Í∞
𝑥=1
1
𝑅𝑚+𝑥𝑃𝑚diverges. Thus, we can compute a block
length 𝐿𝑚≥1 such that the partial sum satisfies:
0.1 ≤
𝐿𝑚
∑︁
𝑥=1
1
𝑅𝑚+ 𝑥𝑃𝑚
≤0.2
We then set 𝐽𝑚+1 = 𝐽𝑚+ 𝐿𝑚. Now that the bounds of the block are properly defined, for
indices 𝑖∈[𝐽𝑚, 𝐽𝑚+1), we set:
𝐴(𝑖) = 𝑅𝑚+ (𝑖−𝐽𝑚+ 1)𝑃𝑚
Since each block contributes at least 0.1 to the total harmonic sum, the overall sum Í 1/𝐴(𝑖)
diverges. Pick an arbitrary shift 𝑘≥1; we must now show that 𝑑(M(𝐴+ 𝑘)) stays bounded
below 3/4. Let 𝑚0 be the unique integer satisfying:
10𝐽𝑚0 ≤𝑘< 10𝐽𝑚0+1
We partition the shifted sequence 𝐴+ 𝑘into three regimes and bound the upper density of
the multiples generated by each:
• (Case 1: 𝑖< 𝐽𝑚0) The upper density of the multiples generated by this finite set is
bounded by the sum of their reciprocals. Because 𝐴(𝑖) > 0, we have 𝐴(𝑖) + 𝑘> 𝑘,
yielding:
𝑑(M({𝐴(𝑖) + 𝑘| 𝑖< 𝐽𝑚0})) ≤
𝐽𝑚0−1
∑︁
𝑖=0
1
𝐴(𝑖) + 𝑘<
𝐽𝑚0−1
∑︁
𝑖=0
1
𝑘= 𝐽𝑚0
𝑘
≤0.1
38
Advancing Mathematics Research with AI-Driven Formal Proof Search
• (Case 2: 𝐽𝑚0 ≤𝑖< 𝐽𝑚0+1) Shifting by a positive 𝑘strictly decreases the reciprocals, so
the upper density of the multiples from this critical block satisfies:
𝑑(M({𝐴(𝑖) + 𝑘| 𝐽𝑚0 ≤𝑖< 𝐽𝑚0+1})) ≤
𝐽𝑚0+1−1
∑︁
𝑖=𝐽𝑚0
1
𝐴(𝑖) + 𝑘<
𝐽𝑚0+1−1
∑︁
𝑖=𝐽𝑚0
1
𝐴(𝑖) ≤0.2
• (Case 3: 𝑖≥𝐽𝑚0+1) Consider any element 𝐴(𝑖) where 𝑖belongs to some block 𝑚≥𝑚0+1,
meaning 10𝐽𝑚≥10𝐽𝑚0+1 > 𝑘. Recall the construction of the 𝑚-th block:
𝐴(𝑖) + 𝑘= (𝑅𝑚+ 𝑘) + (𝑖−𝐽𝑚+ 1)𝑃𝑚
Because 10𝐽𝑚≥𝑘, we have 𝑞𝑘| 𝑃𝑚. By construction, we also have 𝑞𝑘| (𝑅𝑚+ 𝑘).
Consequently, 𝑞𝑘| (𝐴(𝑖) + 𝑘) for every element in this infinite tail. The set of multiples
generated by Case 3 is therefore entirely contained within the multiples of the prime
𝑞𝑘. Expressing this with the upper density notation:
𝑑(M({𝐴(𝑖) + 𝑘| 𝑖≥𝐽𝑚0+1})) ≤𝑑(M({𝑞𝑘})) = 1
𝑞𝑘
≤1
29
By the union bound, the total upper density of the multiples of 𝐴+ 𝑘is bounded above by:
0.1 + 0.2 + 1
29 ≈0.334 < 3
4 = 1 −𝜖.
□
This problem is a more general variant to the original question stating that “For all 𝐴⊆ℕ,
does there exist 𝑘≥1 such that almost all integers have a divisor of the form 𝑎+ 𝑘for
some 𝑎∈𝐴?”. A simple counterexample to this question can be produced using the Chinese
Remainder Theorem. In the more general variant we resolve, note the Chinese Remainder
Theorem is still used to construct a counterexample, but with additional constraints to
make the upper density of 𝐴+ 𝑘small, for all 𝑘. We originally communicated the result in
https://www.erdosproblems.com/forum/thread/26, and share the Lean proof at
https://github.com/google-deepmind/alphaproof-nexus-results/blob/main
/APNOutputs/ErdosProblems/erdos_26.variants.tenenbaum.lean.
Erdős #846
Theorem. Let 𝐴⊂ℝ2 be an infinite set for which there exists some 𝜖> 0 such that in any
subset of 𝐴of size 𝑛there are always at least 𝜖𝑛with no three on a line.
Is it true that 𝐴is the union of a finite number of sets where no three are on a line?
Proof. We will show that there exists an infinite set 𝐴⊂ℝ2 for which any 𝑛-element subset
contains at least 𝑛/2 points with no three on a line, but 𝐴is not the union of a finite number
of sets where no three are on a line.
Let 𝐾∞be the countably infinite complete graph with vertex set 𝑉= {𝑥1, 𝑥2, . . . }. We
choose the sequence of real numbers (𝑥𝑖)∞
𝑖=1 such that it grows sufficiently fast to avoid
39
Advancing Mathematics Research with AI-Driven Formal Proof Search
any accidental roots of polynomials that will arise in our collinearity condition, by setting
𝑥𝑛= 1004𝑛.
We construct our point set 𝐴⊂ℝ2 by mapping each edge 𝑒= {𝑥𝑖, 𝑥𝑗} of 𝐾∞to a point 𝑃𝑒
as follows:
𝑃𝑒= (𝑥𝑖+ 𝑥𝑗, 𝑥2
𝑖+ 𝑥𝑖𝑥𝑗+ 𝑥2
𝑗)
(1)
Let 𝐴= {𝑃𝑒| 𝑒∈𝐸(𝐾∞)}.
Lemma. Three points in 𝐴are collinear if and only if their corresponding edges form a
triangle in 𝐾∞.
Proof of Lemma. First, assume three edges form a triangle in 𝐾∞with vertices 𝑎, 𝑏, 𝑐∈𝑉.
The corresponding points in 𝐴are:
𝑃𝑎𝑏= (𝑎+ 𝑏, 𝑎2 + 𝑎𝑏+ 𝑏2)
𝑃𝑏𝑐= (𝑏+ 𝑐, 𝑏2 + 𝑏𝑐+ 𝑐2)
𝑃𝑐𝑎= (𝑐+ 𝑎, 𝑐2 + 𝑐𝑎+ 𝑎2)
The slope 𝑚of the line connecting 𝑃𝑎𝑏and 𝑃𝑏𝑐is given by:
𝑚= (𝑏2 + 𝑏𝑐+ 𝑐2) −(𝑎2 + 𝑎𝑏+ 𝑏2)
(𝑏+ 𝑐) −(𝑎+ 𝑏)
= 𝑐2 −𝑎2 + 𝑏𝑐−𝑎𝑏
𝑐−𝑎
Factoring the numerator yields:
𝑚= (𝑐−𝑎)(𝑐+ 𝑎) + 𝑏(𝑐−𝑎)
𝑐−𝑎
= 𝑎+ 𝑏+ 𝑐
By symmetry, the slope of the line connecting 𝑃𝑏𝑐and 𝑃𝑐𝑎is also 𝑎+ 𝑏+ 𝑐. Because the slopes
are equal, the three points are collinear.
Conversely, suppose three distinct edges do not form a triangle. We must show their
corresponding points are not collinear. The condition that these points are collinear is
equivalent to the determinant of their 3 × 3 augmented coordinate matrix evaluating to zero.
Because the sequence (𝑥𝑖)∞
𝑖=1 grows quickly enough, any polynomial evaluated on its terms
is strictly dominated by the highest power of its largest variable. By sorting the endpoints
of the three edges, we can group the expanded determinant into three topological cases
based on whether the largest vertex is present in one, two, or all three of the edges. In
every case, because the edges are distinct and do not form a triangle, the coefficient of the
dominant highest-degree term is bounded strictly away from zero. Furthermore, the massive
gap between consecutive terms in the sequence ensures that the lower-degree terms are
strictly bounded and cannot sum to cancel the leading term out. Therefore, the determinant
never evaluates to zero, and no accidental collinearities occur. □
Lemma. Any 𝑛-element subset of 𝐴contains at least 𝑛/2 points with no three on a line.
Proof of Lemma. Let 𝑆⊂𝐴be an arbitrary subset of size 𝑛. The elements of 𝑆correspond
to a subgraph 𝐺𝑆⊂𝐾∞containing exactly 𝑛edges. Every graph with 𝑛edges contains a
bipartite subgraph 𝐵𝑆with at least 𝑛/2 edges. Because 𝐵𝑆is bipartite, it contains no odd
cycles and is therefore triangle-free. By the previous lemma, the corresponding points in 𝐴
40
Advancing Mathematics Research with AI-Driven Formal Proof Search
contain no collinear triplets. This provides a subset of at least ⌈𝑛/2⌉points with no three on
a line, satisfying the condition with 𝜖= 1/2. □
To complete the proof of the theorem, assume for contradiction that 𝐴can be covered by
a finite number of sets where no three are on a line; that is, 𝐴= Ð𝑟
𝑘=1 𝐴𝑘.
This partition naturally induces an 𝑟-coloring on the edges of 𝐾∞. By the infinite Ramsey
Theorem, any finite coloring of the edges of the infinite complete graph must contain a
monochromatic triangle. Consequently, there exists some color class 𝑘containing three edges
that form a triangle. By the lemma, these three edges map to three collinear points in 𝐴𝑘.
This contradicts the assumption that 𝐴𝑘contains no three collinear points.
Therefore, 𝐴cannot be covered by finitely many sets with no three on a line.
□
We originally communicated the result in https://www.erdosproblems.com/fo
rum/thread/846#post-4447 to the ErdosProblems site, and share the Lean proof at
https://github.com/google-deepmind/alphaproof-nexus-results/blob/ma
in/APNOutputs/ErdosProblems/erdos_846.lean. This result was independently
discovered by an internal model at OpenAI [49]. In the discussion at the ErdosProblems site,
it was pointed out that this result also follows from a projection argument of Reiher, Rödl
and Sales [50].
Erdős #152
Theorem. For a Sidon set 𝐴⊂ℕof size 𝑛, let 𝐼(𝐴+ 𝐴) count the isolated elements of the
sumset — those 𝑠∈𝐴+ 𝐴with 𝑠± 1 ∉𝐴+ 𝐴. Define 𝑓(𝑛) as the minimum of 𝐼(𝐴+ 𝐴) over all
Sidon sets of size 𝑛. Then 𝑓(𝑛) ≥(𝑛2 −100𝑛−16)/16, so in particular 𝑓(𝑛) →∞.
Proof. The proof establishes, for every Sidon set 𝐴of size 𝑛:
16 · 𝐼(𝐴+ 𝐴) + 100𝑛+ 16 ≥𝑛2.
(★)
Let 𝐷= {𝑎−𝑏: 𝑎, 𝑏∈𝐴} denote the difference set and 𝑆= 𝐴+ 𝐴the sumset. For
any set 𝑋⊆ℤ, let 𝑁𝑘(𝑋) := |𝑥∈𝑋: 𝑥+ 𝑘∈𝑋| be the number of pairs at distance 𝑘,
𝑉2(𝑋) := |𝑥∈𝑋: 𝑥± 1 ∈𝑋| be the number of interior points, and 𝐼(𝑋) be the isolated points .
Let 𝑋⊂ℤ. We will employ the following three facts:
1. 𝐼(𝑋) + 2𝑁1(𝑋) = |𝑋| + 𝑉2(𝑋), by partitioning elements by neighbor count.
2. 4𝑁1(𝑋) + 𝑁3(𝑋) ≤3|𝑋| +2𝑁2(𝑋), which follows from writing 𝑁𝑘(𝑥) = Í
𝑥∈ℤ1𝑋(𝑥)1𝑋(𝑥+
𝑘) and a pointwise check of the indicator function 1𝑋across all 4-point windows
(𝑥, 𝑥+ 1, 𝑥+ 2, 𝑥+ 3); that is, summing the local inequality 1𝑋(𝑥) + 1𝑋(𝑥+ 1) + 1𝑋(𝑥+
2) + 1𝑋(𝑥)1𝑋(𝑥+ 2) + 1𝑋(𝑥+ 1)1𝑋(𝑥+ 3) ≥1𝑋(𝑥)1𝑋(𝑥+ 1) + 21𝑋(𝑥+ 1)1𝑋(𝑥+ 2) +
1𝑋(𝑥+ 2)1𝑋(𝑥+ 3) + 1𝑋(𝑥)1𝑋(𝑥+ 3) and then summing over all 𝑥∈ℤ.
3. 2𝑁2(𝑋) ≤𝑁3(𝑋) + 2𝑉2(𝑋) + 2𝐼(𝑋). Consider each pair (𝑥, 𝑥+ 2) ∈𝑋2 and we proceed
by cases on 𝑥+ 1. Let 𝐺= {𝑥∈𝑋| 𝑥+ 1 ∉𝑋∧𝑥+ 2 ∈𝑋}. If 𝑥+ 1 ∈𝑋, then the pair is
counted exactly by 𝑉2, so 𝑁2(𝑋) = 𝑉2(𝑋) + |𝐺|. If 𝑥+ 1 ∉𝑋, then
• If 𝑥−1 ∈𝑋, then (𝑥−1, 𝑥+ 2) is a pair counted in 𝑁3(𝑋).
• If 𝑥+ 3 ∈𝑋, then (𝑥, 𝑥+ 3) is a pair counted in 𝑁3(𝑋).
41
Advancing Mathematics Research with AI-Driven Formal Proof Search
• If 𝑥−1 ∉𝑋, then 𝑥is an isolated point in 𝐼(𝑋), and if 𝑥+ 3 ∉𝑋, then 𝑥+ 2 is an
isolated point in 𝐼(𝑋).
Since each 𝑁3 pair can be counted by two different gaps, while isolated points are
distinct in this construction, we have 2|𝐺| ≤𝑁3(𝑋) + 2𝐼(𝑋).
Next, for each 𝑘≥1, count quadruples (𝑎, 𝑏, 𝑐, 𝑑) ∈𝐴4 with 𝑎+ 𝑏+ 𝑘= 𝑐+ 𝑑. Rewriting as
𝑎−𝑐= 𝑑−𝑏−𝑘and partitioning by 𝛿= 𝑎−𝑐yields the following two quadruple transfer
bounds:
1. The cases 𝛿= 0 and 𝛿= −𝑘each contribute ≤|𝐴| (one coordinate determines the rest).
For any 𝛿∉{0, −𝑘}, the Sidon property ensures that there is at most one pair (𝑎, 𝑐)
with 𝑎−𝑐= 𝛿and at most one pair (𝑑, 𝑏) with 𝑑−𝑏= 𝛿+ 𝑘. Consequently, each gap of
size 𝑘in 𝐷identifies exactly one quadruple. Thus |quad𝑘| ≤𝑁𝑘(𝐷) + 2𝑛.
2. Each "good" element 𝑠∈𝑆with 𝑠+ 𝑘∈𝑆(excluding ≤2𝑛doubles of the form 2𝑎)
produces ≥4 quadruples, giving 4𝑁𝑘(𝑆) ≤|quad𝑘| + 8𝑛.
Combining these bounds shows that 𝑁𝑘(𝐷) and 𝑁𝑘(𝑆) are related up to 𝑂(𝑛) error. Apply-
ing fact (2) to 𝐷= 𝐴−𝐴gives
4𝑁1(𝐷) + 𝑁3(𝐷) ≤3|𝐷| + 2𝑁2(𝐷)
and then substitute the above two quadruple transfer bounds for 𝑘= 1, 2, 3 and collecting
all 𝑂(𝑛) terms gives
16𝑁1(𝑆) + 4𝑁3(𝑆) ≤3|𝐷| + 8𝑁2(𝑆) + 100𝑛
Then, using fact (3) on 𝑆we obtain
16𝑁1(𝑆) + 4𝑁3(𝑆) ≤3|𝐷| + (4𝑁3(𝑆) + 8𝑉2(𝑆) + 8𝐼(𝑆)) + 100𝑛
and notice that the 4𝑁3(𝑆) terms cancel. Then applying fact (1) we obtain
(8|𝑆| + 8𝑉2(𝑆) −8𝐼(𝑆)) ≤3|𝐷| + 8𝑉2(𝑆) + 8𝐼(𝑆) + 100𝑛
and see that the 8𝑉2(𝑆) terms now cancel, leaving
16𝐼(𝑆) + 100𝑛≥8|𝑆| −3|𝐷|.
The standard Sidon estimates |𝑆| ≥𝑛2/2 and |𝐷| ≤𝑛2 then give 16𝐼(𝑆)+100𝑛≥4𝑛2−3𝑛2 = 𝑛2,
accounting for a boundary correction of +16 at zero yields (★).
□
We include the Lean proof at https://github.com/google-deepmind/alphapro
of-nexus-results/blob/main/APNOutputs/ErdosProblems/erdos_152.lean.
OEIS Conjectures
Theorem. (A conjecture of OEIS A051293, 2002) Let 𝑎𝑛denote the number of nonempty
subsets of {1, 2, 3, . . . , 𝑛} whose elements have an integer average. Then
𝑎𝑛= 2𝑛+1
𝑛

1 + 1
𝑛+ 3
𝑛2 + 13
𝑛3 + 75
𝑛4 + 541
𝑛5 + 𝑜
 1
𝑛5

42
Advancing Mathematics Research with AI-Driven Formal Proof Search
Proof. A subset 𝑆⊆{1, 2, . . . , 𝑛} has an integer average if and only if the sum of its elements is
divisible by its cardinality |𝑆|. Let 𝑁(𝑛, 𝑘) denote the number of subsets of size 𝑘whose sum is
divisible by 𝑘. We can express the total number of such subsets as 𝑎𝑛= Í𝑛
𝑘=1 𝑁(𝑛, 𝑘) To isolate
the condition that 𝑘divides the sum of the elements in 𝑆, we utilize the orthogonality of roots
of unity. Let 𝜔𝑘,𝑗= exp

2𝜋𝑖𝑗
𝑘

. By the standard orthogonality relation, the sum 1
𝑘
Í𝑘−1
𝑗=0 𝜔𝑁
𝑘,𝑗
equals 1 if 𝑘divides 𝑁, and 0 otherwise. Thus, the indicator function for divisibility by 𝑘is
1
𝑘
Í𝑘−1
𝑗=0 𝜔
Í
𝑠∈𝑆𝑠
𝑘,𝑗
. Summing this over all  𝑛
𝑘
 subsets of size 𝑘yields
𝑁(𝑛, 𝑘) = 1
𝑘
𝑘−1
∑︁
𝑗=0
∑︁
|𝑆|=𝑘
𝜔
Í
𝑠∈𝑆𝑠
𝑘,𝑗
We isolate the principal term corresponding to 𝑗= 0, which evaluates trivially to 1
𝑘
 𝑛
𝑘
. Let
the remainder term be 𝑅𝑛,𝑘, defined as
𝑅𝑛,𝑘= 1
𝑘
𝑘−1
∑︁
𝑗=1
∑︁
|𝑆|=𝑘
𝜔
Í
𝑠∈𝑆𝑠
𝑘,𝑗
Thus, 𝑁(𝑛, 𝑘) = 1
𝑘
 𝑛
𝑘
 + 𝑅𝑛,𝑘. Summing over all possible subset sizes 𝑘, we obtain
𝑎𝑛=
𝑛
∑︁
𝑘=1
1
𝑘
𝑛
𝑘

+
𝑛
∑︁
𝑘=1
𝑅𝑛,𝑘
Using the well-known identity Í𝑛
𝑘=1
1
𝑘
 𝑛
𝑘
 = Í𝑛
𝑗=1
2𝑗−1
𝑗, we separate this into two sums: 𝑆𝑛=
Í𝑛
𝑗=1
2𝑗
𝑗and the harmonic number 𝐻𝑛= Í𝑛
𝑗=1
1
𝑗. This yields our fundamental decomposition
𝑎𝑛= 𝑆𝑛−𝐻𝑛+
𝑛
∑︁
𝑘=1
𝑅𝑛,𝑘
Next, we establish that the sum of the remainders Í𝑛
𝑘=1 𝑅𝑛,𝑘is asymptotically negligible.
Consider the inner sum Í
|𝑆|=𝑘𝜔
Í
𝑠∈𝑆𝑠
𝑘,𝑗
. This sum is exactly the coefficient of 𝑧𝑘in the polynomial
𝑃𝑛,𝑘,𝑗(𝑧) = Î𝑛
𝑚=1(1 + 𝑧𝜔𝑚
𝑘,𝑗). By standard coefficient bounds, the magnitude of the 𝑘-th
coefficient of a polynomial is bounded by its maximum modulus on the unit circle |𝑧| = 1:

∑︁
|𝑆|=𝑘
𝜔
Í
𝑠∈𝑆𝑠
𝑘,𝑗

≤max
|𝑧|=1
𝑛
Ö
𝑚=1
|1 + 𝑧𝜔𝑚
𝑘,𝑗|
For a fixed 𝑘and 𝑗∈{1, . . . , 𝑘−1}, the sequence of roots 𝜔𝑚
𝑘,𝑗is periodic with period
𝐿=
𝑘
gcd( 𝑗,𝑘) ≥2. The product over a full period 𝐿can be evaluated algebraically: the roots of
𝑋𝐿−1 dictate that Î𝐴+𝐿−1
𝑚=𝐴
(1 + 𝑧𝜔𝑚
𝑘,𝑗) = 1 −(−𝑧)𝐿. For any 𝑧on the unit circle, the magnitude
|1 −(−𝑧)𝐿| is strictly bounded by 2. When taking the product over all 𝑛terms, we group
them into ⌊𝑛/𝐿⌋full periods, leaving 𝑛mod 𝐿residual terms. For |𝑧| = 1, each full period
contributes at most a factor of 2, and by the triangle inequality |1 + 𝑧𝜔𝑚
𝑘,𝑗| ≤2, each residual
term also contributes at most a factor of 2. Therefore, the total product is bounded by
43
Advancing Mathematics Research with AI-Driven Formal Proof Search
2⌊𝑛/𝐿⌋+(𝑛mod 𝐿). Because 𝐿≥2, we have ⌊𝑛/𝐿⌋+ (𝑛mod 𝐿) ≤𝑛
2 + 1. Thus, for any 𝑧on the
unit circle, we have
|𝑃𝑛,𝑘,𝑗(𝑧)| ≤2
𝑛
2+1 = 2 · 2𝑛/2
Consequently, the magnitude of the coefficient is bounded by 2 · 2𝑛/2. Applying this to our
remainder definition yields |𝑅𝑛,𝑘| ≤𝑘−1
𝑘2 · 2𝑛/2 ≤2 · 2𝑛/2. Summing over 𝑘∈{1, . . . , 𝑛} gives
the strict bound

𝑛
∑︁
𝑘=1
𝑅𝑛,𝑘

 ≤2𝑛2𝑛/2
We must now evaluate the asymptotics of 𝑆𝑛= Í𝑛
𝑗=1
2𝑗
𝑗. We propose the asymptotic approxi-
mation 𝑓𝑛, defined as
𝑓𝑛= 2𝑛+1
𝑛

1 + 1
𝑛+ 3
𝑛2 + 13
𝑛3 + 75
𝑛4 + 541
𝑛5

= 2𝑛+1𝑃(𝑛)
𝑛6
where 𝑃(𝑛) = 𝑛5 + 𝑛4 + 3𝑛3 + 13𝑛2 + 75𝑛+ 541. To demonstrate that 𝑓𝑛is a highly accurate
approximation of 𝑆𝑛, we analyze the discrepancy in their consecutive differences. Let 𝐸𝑗be
the discrete derivative error given by
𝐸𝑗= 𝑓𝑗−𝑓𝑗−1 −2𝑗
𝑗
By telescoping summation, 𝑆𝑛−𝑓𝑛= 𝑆1 −𝑓1 −Í𝑛
𝑗=2 𝐸𝑗. To bound 𝐸𝑗, we expand 𝑓𝑗−𝑓𝑗−1
algebraically to obtain
𝑓𝑗−𝑓𝑗−1 −2𝑗
𝑗=
2𝑗
2𝑃( 𝑗)( 𝑗−1)6 −𝑃( 𝑗−1) 𝑗6 −𝑗5( 𝑗−1)6
𝑗6( 𝑗−1)6
Let 𝐴(𝑥) = 2𝑃(𝑥)(𝑥−1)6 −𝑃(𝑥−1)𝑥6 −𝑥5(𝑥−1)6. Expanding 𝐴(𝑥) leaves a polynomial of
strictly degree 5:
𝐴(𝑥) = −4683𝑥5 + 13586𝑥4 −19540𝑥3 + 15356𝑥2 −6342𝑥+ 1082
In particular, it is easy to show that |𝐴( 𝑗)| ≤100000𝑗5 for 𝑗≥2. Substituting this back into
the error term yields
|𝐸𝑗| ≤100000 · 2𝑗
𝑗7
Summing these errors up to 𝑛, the sum is dominated by its largest terms, giving Í𝑛
𝑗=2 |𝐸𝑗| =
O

2𝑛
𝑛7

. Recall our decomposition 𝑎𝑛= 𝑓𝑛+ (𝑆𝑛−𝑓𝑛) −𝐻𝑛+ Í𝑛
𝑘=1 𝑅𝑛,𝑘. To prove the theorem,
it suffices to show that the combined error terms are 𝑜

2𝑛+1
𝑛6

:
1. 𝑆𝑛−𝑓𝑛= O

2𝑛
𝑛7

= 𝑜

2𝑛+1
𝑛6

.
2. 𝐻𝑛∼ln 𝑛= 𝑜

2𝑛+1
𝑛6

.
3. Í 𝑅𝑛,𝑘≤2𝑛2𝑛/2 = 𝑜

2𝑛+1
𝑛6

.
44
Advancing Mathematics Research with AI-Driven Formal Proof Search
Since all residual terms are bounded by 𝑜

2𝑛+1
𝑛6

, we conclude that
𝑎𝑛= 𝑓𝑛+ 𝑜
2𝑛+1
𝑛6

= 2𝑛+1
𝑛

1 + 1
𝑛+ 3
𝑛2 + 13
𝑛3 + 75
𝑛4 + 541
𝑛5 + 𝑜
 1
𝑛5

This establishes the conjectured asymptotic expansion.
□
Theorem. (A conjecture of OEIS A228143, 2018) Let 𝑠𝑚= Í𝑚
𝑘=0
 𝑚
𝑘
2 𝑚+𝑘
𝑘
2 be the sequence
A005259. Let 𝑎𝑛denote the determinant of the (𝑛+ 1) × (𝑛+ 1) Hankel-type matrix whose
(𝑖, 𝑗)-entry is 𝑠𝑖+𝑗for all 𝑖, 𝑗= 0, . . . , 𝑛. Let 𝐴(𝑥) = Í∞
𝑛=0 𝑎𝑛𝑥𝑛= 1 + 48𝑥+ 161856𝑥2 + . . .
denote the ordinary generating function of 𝑎𝑛. Then 𝐴(𝑥/3)1/8 has integer coefficients.
Proof. We proceed in three main stages: analyzing the matrix entries modulo 3, analyzing
them modulo 4, and using the resulting divisibility properties of the determinant 𝑎𝑛to
construct the required eighth root as a formal power series over the integers.
First, we determine the residues of 𝑠𝑚modulo 3. By writing 𝑘in base 3, Kummer’s
Theorem dictates that the highest power of 3 dividing  2𝑘
𝑘
 equals the number of carries when
evaluating 𝑘+ 𝑘in base 3. If 𝑘contains the digit 2, a carry occurs, so  2𝑘
𝑘
 ≡0 (mod 3).
Alternatively, if 𝑘consists only of the digits 0 and 1, there are no carries. Applying Lucas’s
Theorem digit-by-digit to  2𝑘
𝑘
 yields a product of terms  0
0
 = 1 and  2
1
 = 2 ≡−1 (mod 3).
Thus,  2𝑘
𝑘
 ≡(−1)𝑐(mod 3), where 𝑐is the number of 1s in the base-3 representation of 𝑘.
Since 𝑐shares the same parity as 𝑘, we obtain  2𝑘
𝑘
 ≡(−1)𝑘(mod 3).
We can rewrite the squared product of binomial coefficients as:
𝑚
𝑘
 𝑚+ 𝑘
𝑘
2
=
𝑚+ 𝑘
2𝑘
22𝑘
𝑘
2
When  2𝑘
𝑘
 . 0 (mod 3), the base-3 digits of 2𝑘are strictly 0s and 2s. Applying Lucas’s
Theorem to  𝑚+𝑘
2𝑘
, each digit of the evaluation takes the form  𝑑𝑖
0
 = 1 or  𝑑𝑖
2
 ∈{0, 1}. Thus,
 𝑚+𝑘
2𝑘
 ≡0 or 1 (mod 3). Since values in {0, 1} are invariant under squaring,  𝑚+𝑘
2𝑘
2 ≡ 𝑚+𝑘
2𝑘

(mod 3). Furthermore, since  2𝑘
𝑘
 ∈{0, (−1)𝑘} (mod 3), squaring it absorbs the parity:
 2𝑘
𝑘
2 ≡(−1)𝑘 2𝑘
𝑘
 (mod 3). Combining these pieces, we find that for all 𝑚and 𝑘:
𝑚
𝑘
 𝑚+ 𝑘
𝑘
2
≡(−1)𝑘
𝑚+ 𝑘
2𝑘
 2𝑘
𝑘

≡(−1)𝑘
𝑚
𝑘
 𝑚+ 𝑘
𝑘

(mod 3)
Summing this equivalence over 𝑘= 0, . . . , 𝑚yields 𝑠𝑚≡Í𝑚
𝑘=0(−1)𝑘 𝑚
𝑘
  𝑚+𝑘
𝑘
 (mod 3). By
a standard alternating binomial sum identity, Í𝑚
𝑘=0(−1)𝑘 𝑚
𝑘
  𝑚+𝑘
𝑘
 = (−1)𝑚. Consequently,
𝑠𝑚≡(−1)𝑚(mod 3).
Using this congruence, we apply row operations to the matrix 𝑀(𝑛) to establish that 3𝑛| 𝑎𝑛.
Let 𝑃𝑛be the lower-triangular matrix with ones on the main diagonal, 𝑃𝑖,0 = −(−1)𝑖for 𝑖≥1,
and zeros elsewhere. The matrix product 𝑃𝑛𝑀(𝑛) replaces each row 𝑖≥1 with the 𝑖-th row
45
Advancing Mathematics Research with AI-Driven Formal Proof Search
minus (−1)𝑖times the 0-th row. Visually, the modified matrix takes the form:
𝑃𝑛𝑀(𝑛) =

𝑠0
𝑠1
𝑠2
· · ·
𝑠𝑛
𝑠1 + 𝑠0
𝑠2 + 𝑠1
𝑠3 + 𝑠2
· · ·
𝑠𝑛+1 + 𝑠𝑛
𝑠2 −𝑠0
𝑠3 −𝑠1
𝑠4 −𝑠2
· · ·
𝑠𝑛+2 −𝑠𝑛
...
...
...
. . .
...
𝑠𝑛−(−1)𝑛𝑠0
𝑠𝑛+1 −(−1)𝑛𝑠1
𝑠𝑛+2 −(−1)𝑛𝑠2
· · ·
𝑠2𝑛−(−1)𝑛𝑠𝑛

The new (𝑖, 𝑗)-entry for 𝑖≥1 is 𝑠𝑖+𝑗−(−1)𝑖𝑠𝑗. By our previous congruence, 𝑠𝑖+𝑗−(−1)𝑖𝑠𝑗≡
(−1)𝑖+𝑗−(−1)𝑖(−1) 𝑗≡0 (mod 3). Thus, every entry in rows 1 through 𝑛of the new matrix
is divisible by 3. Factoring a 3 out of each of these 𝑛rows gives a factor of 3𝑛. Because
det(𝑃𝑛) = 1, we conclude that 3𝑛| det(𝑀(𝑛)) = 𝑎𝑛.
Second, we analyze 𝑠𝑚modulo 4. For any 𝑘≥1, the product  𝑚
𝑘
  𝑚+𝑘
𝑘
 is always even,
which implies its square is divisible by 4. Thus,
 𝑚
𝑘
  𝑚+𝑘
𝑘
2
≡0 (mod 4) for all 𝑘≥1. The
𝑘= 0 term evaluates to 1, yielding 𝑠𝑚≡1 (mod 4) for all 𝑚.
We apply a similar matrix transformation to establish divisibility by 4𝑛. Let 𝑃′
𝑛be the
lower-triangular matrix with ones on the diagonal, 𝑃′
𝑖,0 = −1 for 𝑖≥1, and zeros elsewhere.
The product 𝑃′
𝑛𝑀(𝑛) subtracts the 0-th row from every subsequent row 𝑖≥1:
𝑃′
𝑛𝑀(𝑛) =

𝑠0
𝑠1
· · ·
𝑠𝑛
𝑠1 −𝑠0
𝑠2 −𝑠1
· · ·
𝑠𝑛+1 −𝑠𝑛
𝑠2 −𝑠0
𝑠3 −𝑠1
· · ·
𝑠𝑛+2 −𝑠𝑛
...
...
. . .
...

For 𝑖≥1, the (𝑖, 𝑗)-entry becomes 𝑠𝑖+𝑗−𝑠𝑗. Since 𝑠𝑚≡1 (mod 4) for all 𝑚, this difference
evaluates to 1 −1 ≡0 (mod 4). Factoring 4 out of the 𝑛modified rows shows that 4𝑛|
det(𝑀(𝑛)) = 𝑎𝑛.
Now we combine these divisibility properties. We explicitly compute 𝑎1 = 48. For 𝑛≥1,
we know 4𝑛| 𝑎𝑛, and since 4𝑛≥16 for 𝑛≥2, it follows that 16 | 𝑎𝑛for all 𝑛≥1 (as 16 | 48
for 𝑛= 1). Because 16 and 3𝑛are coprime, their respective divisibilities imply 16 · 3𝑛| 𝑎𝑛for
all 𝑛≥1.
We consider the scaled generating function 𝐴(𝑥/3) = Í∞
𝑛=0
𝑎𝑛
3𝑛𝑥𝑛. Let 𝑏𝑛= 𝑎𝑛/3𝑛denote
the coefficients of this series. Since 𝑎0 = 1, we have 𝑏0 = 1. For 𝑛≥1, our divisibility result
yields 16 | 𝑏𝑛. Therefore, we can write 𝐴(𝑥/3) = 1 + 16𝑌(𝑥), where 𝑌(𝑥) = Í∞
𝑛=1 𝑦𝑛𝑥𝑛is a
formal power series with integer coefficients and zero constant term (𝑌(0) = 0).
Finally, we construct the eighth root 𝐶(𝑥) = 𝐴(𝑥/3)1/8 ∈ℤ⟦𝑥⟧. We seek a series of the
form 𝐶(𝑥) = 1 + 2𝑋(𝑥) where 𝑋(𝑥) ∈ℤ⟦𝑥⟧has no constant term. Expanding the eighth
power yields
(1 + 2𝑋(𝑥))8 = 1 + 16𝑋(𝑥) + 112𝑋(𝑥)2 + 448𝑋(𝑥)3 + 1120𝑋(𝑥)4
+ 1792𝑋(𝑥)5 + 1792𝑋(𝑥)6 + 1024𝑋(𝑥)7 + 256𝑋(𝑥)8
Factoring out 16 from the higher degree terms, we define the polynomial
𝑃(𝑋) = 7𝑋2 + 28𝑋3 + 70𝑋4 + 112𝑋5 + 112𝑋6 + 64𝑋7 + 16𝑋8
46
Advancing Mathematics Research with AI-Driven Formal Proof Search
Thus, (1 + 2𝑋(𝑥))8 = 1 + 16(𝑋(𝑥) + 𝑃(𝑋(𝑥))). To satisfy 𝐶(𝑥)8 = 𝐴(𝑥/3), we must solve the
equation 1 + 16(𝑋(𝑥) + 𝑃(𝑋(𝑥))) = 1 + 16𝑌(𝑥), which simplifies to 𝑋(𝑥) + 𝑃(𝑋(𝑥)) = 𝑌(𝑥).
We determine the coefficients 𝑥𝑛of 𝑋(𝑥) = Í∞
𝑛=1 𝑥𝑛𝑥𝑛inductively. We set 𝑥0 = 0. For the
inductive step, the coefficient of 𝑥𝑛+1 in the equation is
𝑥𝑛+1 + [𝑥𝑛+1]𝑃(𝑋(𝑥)) = 𝑦𝑛+1
Because every term in 𝑃(𝑋) has degree at least 2, and 𝑋(𝑥) has no constant term, the 𝑥𝑛+1
coefficient of 𝑃(𝑋(𝑥)) depends only on the terms 𝑥1, . . . , 𝑥𝑛. Therefore, we can uniquely solve
for the integers 𝑥𝑛+1 as
𝑥𝑛+1 = 𝑦𝑛+1 −[𝑥𝑛+1]𝑃
 𝑛
∑︁
𝑘=1
𝑥𝑘𝑥𝑘
!
This well-defined recurrence provides an integer sequence (𝑥𝑛)𝑛≥1 giving a formal power
series 𝑋(𝑥) ∈ℤ⟦𝑥⟧that satisfies 𝑋(𝑥) + 𝑃(𝑋(𝑥)) = 𝑌(𝑥). Substituting this back into our
expansion yields (1 + 2𝑋(𝑥))8 = 1 + 16𝑌(𝑥) = 𝐴(𝑥/3). Setting 𝐶(𝑥) = 1 + 2𝑋(𝑥), we have
established the existence of the desired integer power series 𝐶(𝑥) = 𝐴(𝑥/3)1/8.
□
These OEIS problems were added as conjectures in 2022 (https://oeis.org/A0512
93) and 2018 (https://oeis.org/A228143). Though neither problem has likely received
much attention, the ability to provide a guarantee on the correctness of the statement that
an expert conjectured serves value. For example, it appears that a good part of the work is
done in identifying the asymptotic formula to be conjectured in OEIS A051293. In this case,
ensuring the formula holds with a rigorous proof is a matter of validating intuition without
carrying out potentially tedious proof steps, which our agent can handle. The Lean proofs
for the two problems can be found at https://github.com/google-deepmind/alphap
roof-nexus-results/blob/main/APNOutputs/OEIS.
A variant of the Graph Reconstruction Conjecture
The Kelly-Ulam graph reconstruction program aims to recover a graph from its deck of
one-vertex-deleted subgraphs [62, 36]. A standard bipartite version was formulated by
Bondy and Hemminger as the problem of showing that bipartite graphs are reconstructible
[10]. The following theorem proves a structured incidence-deletion analogue under strong
type-distinguishability assumptions.
Terminology Let Ω = 𝐿⊔𝑅be a finite vertex set with a partition into the disjoint parts
𝐿, 𝑅⊆Ω. A graph 𝐾is bipartite with respect to (𝐿, 𝑅) if every edge of 𝐾has one endpoint in
𝐿and one endpoint in 𝑅. We say 𝐾is 2-connected if 𝐾is connected and, for every vertex 𝑣,
the induced graph on Ω \ {𝑣} is connected. For a graph 𝐾and a vertex 𝑣, write 𝐾\inc 𝑣for
the graph obtained from 𝐾by deleting all edges incident to 𝑣, while leaving the vertex set
unchanged. Thus
𝐸(𝐾\inc 𝑣) = {𝑥𝑦∈𝐸(𝐾) : 𝑥≠𝑣, 𝑦≠𝑣}.
A bipartite isomorphism 𝐾𝐵𝐾′ is a graph isomorphism whose underlying bijection preserves
both parts 𝐿and 𝑅. The bipartite deck is the multiset
D𝐵(𝐾) := {{[𝐾\inc 𝑣]𝐵: 𝑣∈Ω}},
47
Advancing Mathematics Research with AI-Driven Formal Proof Search
where [·]𝐵denotes bipartite-isomorphism class. Let 𝑁𝐾(𝑥) be the neighbor set of 𝑥in 𝐾. The
degree profile and type of 𝑥are
𝑃𝐾(𝑥) := {{deg𝐾(𝑦) : 𝑦∈𝑁𝐾(𝑥)}},
𝜏𝐾(𝑥) := (deg𝐾(𝑥), 𝑃𝐾(𝑥)).
The type profile of 𝑢is the multiset of the types of its neighbors:
𝑇𝐾(𝑢) := {{𝜏𝐾(𝑥) : 𝑥∈𝑁𝐾(𝑢)}}.
Finally, for a type 𝑡= (𝑑, 𝑀) ∈ℕ× Multiset(ℕ) and 𝑎∈ℕ, define
𝐹𝑎(𝑡) := (max(𝑑−1, 0), 𝑀\ {𝑎}),
where 𝑀\ {𝑎} means deletion of one occurrence of 𝑎from the multiset 𝑀. In the applications
below, 𝐹𝑎is applied to neighbor-types, whose first coordinate is positive, so max(𝑑−1, 0) =
𝑑−1 there. We write #𝑡𝑀for the multiplicity of 𝑡in a multiset 𝑀.
Theorem (Weak bipartite graph reconstruction) Let 𝐺and 𝐻be finite simple graphs on
the same finite vertex set Ω, both bipartite with respect to the same parts Ω = 𝐿⊔𝑅and
|Ω| ≥3. Assume that 𝐺is 2-connected and all vertex types of 𝐺are pairwise distinct, that is,
𝜏𝐺(𝑥) ≠𝜏𝐺(𝑦) if 𝑥≠𝑦. If D𝐵(𝐺) = D𝐵(𝐻), then 𝐺and 𝐻are bipartite-isomorphic.
Proof. Write 𝑛= |Ω| and 𝑒(𝐾) = |𝐸(𝐾)|. Since bipartite isomorphisms preserve edge counts,
the deck determines the multiset
{{𝑒(𝐾\inc 𝑣) : 𝑣∈Ω}}.
For every vertex 𝑣,
𝑒(𝐾\inc 𝑣) + deg𝐾(𝑣) = 𝑒(𝐾),
(1)
because 𝐾\inc 𝑣removes exactly the edges incident to 𝑣. Also,
∑︁
𝑣∈Ω
𝑒(𝐾\inc 𝑣) = (𝑛−2)𝑒(𝐾),
(2)
because each edge of 𝐾remains in precisely the cards indexed by the 𝑛−2 vertices not
incident to that edge. Since 𝑛≥3, equation (2) shows that the deck determines 𝑒(𝐾).
Applying this to the equal decks of 𝐺and 𝐻gives
𝑒(𝐺) = 𝑒(𝐻),
(3)
and then equation (1) shows that the degree multisets of 𝐺and 𝐻are equal.
Equality of the two decks also gives a bijection 𝑓: Ω →Ω such that, for every 𝑣∈Ω,
there is a bipartite isomorphism
𝜙𝑣: 𝐺\inc 𝑣𝐵𝐻\inc 𝑓(𝑣).
(4)
For this matched pair of cards, edge counts are equal. Combining this with (1) and (3) yields
deg𝐺(𝑣) = deg𝐻( 𝑓(𝑣))
(5)
for every 𝑣.
48
Advancing Mathematics Research with AI-Driven Formal Proof Search
Next, 𝐺has minimum degree at least 2. Indeed, if a vertex had degree 0, then 𝐺would
not be connected; if a vertex 𝑥had the unique neighbor 𝑦, then the induced graph on Ω \ {𝑦}
would contain the isolated vertex 𝑥, contradicting 2-connectivity. Since the degree multisets
of 𝐺and 𝐻are equal, 𝐻also has minimum degree at least 2.
Therefore, in any graph 𝐾with minimum degree at least 2, the card 𝐾\inc 𝑣has a unique
isolated vertex, namely 𝑣. Indeed, the vertex 𝑣is isolated because all its incident edges have
been removed. On the other hand, if 𝑥≠𝑣, then 𝑥has at least two neighbors in 𝐾, at most
one of which is 𝑣; hence 𝑥has a neighbor 𝑦≠𝑣, and the edge 𝑥𝑦remains in 𝐾\inc 𝑣.
Applying this uniqueness to (4), the isomorphism 𝜙𝑣sends the unique isolated vertex of
𝐺\inc 𝑣to the unique isolated vertex of 𝐻\inc 𝑓(𝑣). Hence
𝜙𝑣(𝑣) = 𝑓(𝑣).
(6)
Since 𝜙𝑣preserves 𝐿and 𝑅, (6) implies that 𝑓preserves the two parts:
𝑣∈𝐿⇐⇒𝑓(𝑣) ∈𝐿,
𝑣∈𝑅⇐⇒𝑓(𝑣) ∈𝑅.
(7)
We now prove that 𝑓preserves vertex types. It remains, in view of (5), to compare degree
profiles. For a graph 𝐾and vertex 𝑣, put
𝐴𝐾(𝑘) := #{𝑥∈Ω : deg𝐾(𝑥) = 𝑘},
𝐵𝐾,𝑣(𝑘) := #{𝑥∈Ω : deg𝐾\inc𝑣(𝑥) = 𝑘},
and
𝐶𝐾,𝑣(𝑘) := #{𝑥∈𝑁𝐾(𝑣) : deg𝐾(𝑥) = 𝑘}.
Counting vertices of degree 𝑘before and after deleting the incidence set of 𝑣gives, for every
𝑘≥0,
𝐶𝐾,𝑣(𝑘+ 1) + 𝐴𝐾(𝑘) + 1𝑘=0 = 𝐶𝐾,𝑣(𝑘) + 𝐵𝐾,𝑣(𝑘) + 1deg𝐾(𝑣)=𝑘.
(8)
Indeed, in 𝐾\inc 𝑣, every non-neighbor of 𝑣keeps its degree, while every neighbor of 𝑣has
its degree lowered by 1. Hence the vertices of degree 𝑘in 𝐾\inc 𝑣are precisely the old
non-neighbors of degree 𝑘, the old neighbors of degree 𝑘+ 1, and additionally 𝑣itself if 𝑘= 0.
Therefore
𝐵𝐾,𝑣(𝑘) = 𝐴𝐾(𝑘) −𝐶𝐾,𝑣(𝑘) −1deg𝐾(𝑣)=𝑘+ 𝐶𝐾,𝑣(𝑘+ 1) + 1𝑘=0.
Since the global degree multisets are equal, 𝐴𝐺(𝑘) = 𝐴𝐻(𝑘). Since 𝜙𝑣is an isomorphism
between the matched cards, 𝐵𝐺,𝑣(𝑘) = 𝐵𝐻, 𝑓(𝑣)(𝑘). By (5), the final indicator in (8) is also
the same for 𝐺and 𝐻. Finally, 𝐶𝐾,𝑣(0) = 0, because a neighbor always has positive degree.
Induction on 𝑘in (8) gives
𝐶𝐺,𝑣(𝑘) = 𝐶𝐻, 𝑓(𝑣)(𝑘)
(𝑘≥0).
Thus
𝑃𝐺(𝑣) = 𝑃𝐻( 𝑓(𝑣)),
and together with (5) this proves
𝜏𝐺(𝑣) = 𝜏𝐻( 𝑓(𝑣))
(9)
49
Advancing Mathematics Research with AI-Driven Formal Proof Search
for every 𝑣∈Ω. We next prove equality of type profiles:
𝑇𝐺(𝑢) = 𝑇𝐻( 𝑓(𝑢))
(10)
for every 𝑢. Fix 𝑢. If 𝑢∈𝐿, take 𝑆= 𝑅, otherwise take 𝑆= 𝐿(thus 𝑆is the opposite side from
𝑢). By (7) and (9), the multisets of global types on 𝑆agree:
{{𝜏𝐺(𝑥) : 𝑥∈𝑆}} = {{𝜏𝐻(𝑥) : 𝑥∈𝑆}}.
(11)
The card isomorphism 𝜙𝑢also preserves 𝑆, and therefore the multisets of local types on 𝑆
agree:
{{𝜏𝐺\inc𝑢(𝑥) : 𝑥∈𝑆}} = {{𝜏𝐻\inc 𝑓(𝑢)(𝑥) : 𝑥∈𝑆}}.
(12)
For 𝑥∈𝑆, bipartiteness gives the local-type formula
𝜏𝐺\inc𝑢(𝑥) =
(
𝐹deg𝐺(𝑢)(𝜏𝐺(𝑥)),
if 𝑥∈𝑁𝐺(𝑢),
𝜏𝐺(𝑥),
if 𝑥∉𝑁𝐺(𝑢).
(13)
Indeed, if 𝑥is adjacent to 𝑢, then deleting the incidence set of 𝑢removes the edge 𝑢𝑥, lowering
deg𝐺(𝑥) by one and deleting one occurrence of deg𝐺(𝑢) from the degree profile of 𝑥. If 𝑥is
not adjacent to 𝑢, then any neighbor of 𝑥lies on the same side of the bipartition as 𝑢, and
therefore cannot be adjacent to 𝑢; hence the type of 𝑥is unchanged. The same formula holds
for 𝐻and 𝑓(𝑢).
Taking the number of occurrences of an arbitrary type 𝑡in (13) gives
#𝑡{{𝜏𝐺\inc𝑢(𝑥) : 𝑥∈𝑆}} + #𝑡𝑇𝐺(𝑢) = #𝑡{{𝜏𝐺(𝑥) : 𝑥∈𝑆}} + #𝑡{{𝐹deg𝐺(𝑢)(𝑠) : 𝑠∈𝑇𝐺(𝑢)}}.
(14)
There is an identical identity for 𝐻. The first terms on the two sides of (14) agree by (12),
and the global-type terms agree by (11). Also deg𝐺(𝑢) = deg𝐻( 𝑓(𝑢)) by (5). Hence equality
of the type-profile counts can be proved by descending induction on the first coordinate of 𝑡.
The base case is that no type in a type profile can have first coordinate at least 𝑛, since every
vertex degree is < 𝑛. For the induction step, the only types 𝑠with 𝐹deg𝐺(𝑢)(𝑠) = 𝑡have first
coordinate 𝑡1 + 1; moreover every 𝑠occurring in a type profile has positive first coordinate.
Thus the rightmost term in (14) is already equal for 𝐺and 𝐻by the induction hypothesis,
and subtracting the two versions of (14) yields equality of the number of occurrences of 𝑡in
𝑇𝐺(𝑢) and in 𝑇𝐻( 𝑓(𝑢)). This proves (10).
The distinctness of types transfers from 𝐺to 𝐻: if 𝜏𝐻(𝑥) = 𝜏𝐻(𝑦), then by applying (9) to
𝑓−1(𝑥) and 𝑓−1(𝑦) we obtain equality of the corresponding 𝐺-types, so 𝑥= 𝑦.
Since types are pairwise distinct, adjacency is determined by type profiles: for every
graph 𝐾among 𝐺, 𝐻and every pair of vertices 𝑎, 𝑏,
𝐾has edge 𝑎𝑏
⇐⇒
𝜏𝐾(𝑏) ∈𝑇𝐾(𝑎).
(15)
The forward implication is the definition of 𝑇𝐾(𝑎). Conversely, if 𝜏𝐾(𝑏) occurs in 𝑇𝐾(𝑎), then
some neighbor 𝑐of 𝑎has 𝜏𝐾(𝑐) = 𝜏𝐾(𝑏), and distinctness of types gives 𝑐= 𝑏.
Finally, for any 𝑢, 𝑣∈Ω, equations (9), (10), and (15) give
𝐺has edge 𝑢𝑣⇐⇒𝜏𝐺(𝑣) ∈𝑇𝐺(𝑢) ⇐⇒𝜏𝐻( 𝑓(𝑣)) ∈𝑇𝐻( 𝑓(𝑢)) ⇐⇒𝐻has edge 𝑓(𝑢) 𝑓(𝑣).
50
Advancing Mathematics Research with AI-Driven Formal Proof Search
Thus 𝑓is a graph isomorphism 𝐺 𝐻. By (7), it preserves the two bipartition parts, so it is a
bipartite isomorphism.
□
The Lean proof discovered for this problem is at https://github.com/google-dee
pmind/alphaproof-nexus-results/blob/main/APNOutputs/AICollaborator/G
raphs/bipartite_graph_reconstruction_conjecture_2.lean.
Log-Concavity of Hilbert Sequences
Pure 𝑂-sequences, introduced in the context of Stanley’s work on Hilbert functions of mono-
mial level algebras in the late 1970s, have been studied intensively over the last fifteen years
[57]. They exhibit surprisingly strong positivity phenomena, especially in small codimension
and type. Although pure 𝑂-sequences are not log-concave in general, the case of codimension
3 and type 2 remained open for over a decade [9, 68]. The following theorem establishes
log-concavity in precisely this remaining case.
Theorem. Every pure 𝑂-sequence of codimension 3 and type 2 is log-concave.
Terminology. A monomial 𝑥𝑚(0)
0
𝑥𝑚(1)
1
𝑥𝑚(2)
2
in three variables is identified with its exponent
vector 𝑚= (𝑚(0), 𝑚(1), 𝑚(2)) ∈ℕ3. We write 𝑚′ ≤𝑚for coordinate-wise inequality and
|𝑚| = 𝑚(0) + 𝑚(1) + 𝑚(2) for total degree. A finite order ideal Γ ⊂ℕ3 is a finite set closed
downward under this order: if 𝑛∈Γ and 𝑚≤𝑛, then 𝑚∈Γ.
A monomial 𝑚∈Γ is maximal if every 𝑛∈Γ with 𝑚≤𝑛also satisfies 𝑛≤𝑚. The ideal is
pure if all maximal monomials have the same total degree; this common degree is the socle
degree. The type is the number of maximal monomials. The pure 𝑂-sequence of Γ is
ℎΓ(𝑑) = #{𝑚∈Γ : |𝑚| = 𝑑}.
For a monomial 𝑔, we simply write ℎ𝑔(𝑑) = #{𝑢≤𝑔: |𝑢| = 𝑑}. The 𝑂-sequence is log-concave
if
ℎΓ(𝑖−1)ℎΓ(𝑖+ 1) ≤ℎΓ(𝑖)2
(0 < 𝑖< 𝑒),
where 𝑒is the socle degree of Γ. We write 1𝑃for the indicator of the condition 𝑃.
Proof. Let Γ be a pure order ideal in three variables and suppose that its two maximal
monomials are 𝑚1 ≠𝑚2. Since Γ is pure, |𝑚1| = |𝑚2| = 𝑒. Every element of a finite order
ideal lies below a maximal element, so
Γ = {𝑢: 𝑢≤𝑚1} ∪{𝑢: 𝑢≤𝑚2},
After possibly interchanging 𝑚1 and 𝑚2, there is a coordinate 𝑥∈{0, 1, 2} such that
𝑚2(𝑥) > 𝑚1(𝑥),
𝑚2(𝑦) ≤𝑚1(𝑦)
(𝑦≠𝑥).
(1)
Indeed, the three integers 𝑚1(𝑖) −𝑚2(𝑖) sum to zero and are not all zero, hence one sign
occurs in a minority position; if necessary we swap the two monomials so that the minority
sign is negative.
Let 𝑐= 𝑚1(𝑥) + 1, and define
𝑀red(𝑦) =
(
𝑚2(𝑥) −𝑚1(𝑥) −1,
𝑦= 𝑥,
𝑚2(𝑦),
𝑦≠𝑥.
51
Advancing Mathematics Research with AI-Driven Formal Proof Search
Then |𝑀red| = 𝑒−𝑐. For 𝑢≤𝑚2, condition (1) implies
𝑢̸ ≤𝑚1
⇐⇒
𝑢(𝑥) ≥𝑐.
If 𝑑≥𝑐, the map 𝑢↦→𝑢−𝑐𝑒𝑥bijects {𝑢≤𝑚2 : |𝑢| = 𝑑, 𝑢(𝑥) ≥𝑐} with {𝑣≤𝑀red : |𝑣| = 𝑑−𝑐}.
If 𝑑< 𝑐, the first set is empty. Hence the 𝑂sequence of Γ can be written as
𝐻(𝑑) := ℎΓ(𝑑) = ℎ𝑚1(𝑑) + 1𝑑≥𝑐ℎ𝑀red(𝑑−𝑐).
(2)
We need to prove that 𝐻(𝑑−1)𝐻(𝑑+ 1) ≤𝐻(𝑑)2 holds for 0 < 𝑑< 𝑒.
For an integer-valued sequence 𝐹: ℕ→ℤ, define the first and scond difference sequences
as
Δ𝐹(0) = 𝐹(0),
Δ𝐹(𝑑) = 𝐹(𝑑) −𝐹(𝑑−1)
(𝑑> 0),
Δ2𝐹(0) = Δ𝐹(0),
Δ2𝐹(𝑑) = Δ𝐹(𝑑) −Δ𝐹(𝑑−1)
(𝑑> 0).
We first prove an elementary divisor-count formula for a single monomial. Let 𝑚= (𝛼, 𝛽, 𝛾)
be a monomial. For 𝑝, 𝑞∈ℕ, set
𝐿𝑝,𝑞(𝑘) = #{𝑟∈ℕ: 𝑟< 𝑝, 𝑟≤𝑘, 𝑘−𝑟< 𝑞}.
Thus 𝐿𝑝,𝑞(𝑘) counts the number of pairs (𝑟, 𝑠) with 0 ≤𝑟< 𝑝, 0 ≤𝑠< 𝑞, and 𝑟+ 𝑠= 𝑘. A direct
box count gives
ℎ𝑚(𝑡) =
𝑡∑︁
𝑘=0
1𝑡−𝑘<𝛾+1 𝐿𝛼+1,𝛽+1(𝑘).
With the convention Δ𝐹(0) = 𝐹(0), the first-difference identities are
Δ𝐿𝑝,𝑞(𝑡) = 1𝑡<𝑝+ 1𝑡<𝑞−1𝑡<𝑝+𝑞
(𝑡≥0),
and hence
Δℎ𝑚(𝑡) = 𝐿𝛼+1,𝛽+1(𝑡) −1𝑡≥𝛾+1 𝐿𝛼+1,𝛽+1(𝑡−𝛾−1)
(𝑡≥0).
Taking one more difference gives, for every 𝑡> 0,
Δ2ℎ𝑚(𝑡) = 1𝑡≤𝛼+ 1𝑡≤𝛽+ 1𝑡≤𝛾−1𝑡≤𝛼+𝛽+1 −1𝑡≤𝛽+𝛾+1
−1𝑡≤𝛾+𝛼+1 + 1𝑡≤𝛼+𝛽+𝛾+2.
(3)
In particular, Δ2ℎ𝑚(𝑡) ≤1. The same bound holds for the shifted sequence 𝑡↦−→1𝑡≥𝑐ℎ𝑀red(𝑡−𝑐),
because below the shift its second difference is zero, and from the shift onward it is the
second difference of the principal sequence of 𝑀red. Therefore Δ2𝐻(𝑡) ≤2.
Formula (3) also implies the following useful dichotomy. If 𝑡> 0 and Δ2ℎ𝑚(𝑡) = 1, then
either
𝑡≤𝑚(0),
𝑡≤𝑚(1),
𝑡≤𝑚(2),
(L)
or
𝑡≥𝑚(0) + 𝑚(1) + 2,
𝑡≥𝑚(1) + 𝑚(2) + 2,
𝑡≥𝑚(0) + 𝑚(2) + 2,
𝑡≤|𝑚| + 2. (U)
We refer to these as the lower and upper alternatives. For 𝑡= 0, the lower alternative is
automatic.
We shall also use the following elementary consequences of the same box count.
52
Advancing Mathematics Research with AI-Driven Formal Proof Search
1. If 𝑡≤𝑚(𝑖) for all 𝑖, then
2ℎ𝑚(𝑡) = (𝑡+ 1)(𝑡+ 2),
Δℎ𝑚(𝑡) = 𝑡+ 1.
(5)
2. If 𝑡≥𝑚(𝑖) + 𝑚( 𝑗) for every pair {𝑖, 𝑗}, and 𝑡≤|𝑚| + 2, then,
2ℎ𝑚(𝑡) = (|𝑚| + 1 −𝑡)(|𝑚| + 2 −𝑡).
(6)
3. If 𝑡≥𝑚(𝑖) + 𝑚( 𝑗) + 1 for every pair {𝑖, 𝑗}, and 𝑡≤|𝑚| + 2, then
Δℎ𝑚(𝑡) = −(|𝑚| + 2 −𝑡).
(7)
4. For all 𝑡,
2ℎ𝑚(𝑡) ≤(|𝑚| −𝑡+ 1)(|𝑚| −𝑡+ 2).
(8)
5. If 2𝑡≥|𝑚| + 1, then
Δℎ𝑚(𝑡) ≤0.
(9)
Now fix 0 < 𝑑< 𝑒= |𝑚1| = |𝑚2|. Using 𝐻(𝑑) = 𝐻(𝑑−1) + Δ𝐻(𝑑) and Δ𝐻(𝑑+ 1) =
Δ𝐻(𝑑) + Δ2𝐻(𝑑+ 1) gives
𝐻(𝑑)2 −𝐻(𝑑−1)𝐻(𝑑+ 1) = (Δ𝐻(𝑑))2 −𝐻(𝑑−1)Δ2𝐻(𝑑+ 1).
(10)
Since 𝐻(𝑑−1) ≥0 and Δ2𝐻(𝑑+ 1) ≤2, it is enough to prove the following two statements:
Δ2𝐻(𝑑+ 1) = 1
=⇒
𝐻(𝑑−1) ≤(Δ𝐻(𝑑))2,
(11)
and
Δ2𝐻(𝑑+ 1) = 2
=⇒
2𝐻(𝑑−1) ≤(Δ𝐻(𝑑))2.
(12)
Indeed, if Δ2𝐻(𝑑+ 1) ≤0, equation (10) is immediate; if it is 1 or 2, then (11) or (12)
applies.
Write 𝑓(𝑡) = ℎ𝑚1(𝑡) and 𝑔(𝑡) = 1𝑡≥𝑐ℎ𝑀red(𝑡−𝑐), so that 𝐻= 𝑓+ 𝑔. Since Δ2 𝑓≤1 and
Δ2𝑔≤1, if Δ2𝐻(𝑑+ 1) = 1, then either
Δ2 𝑓(𝑑+ 1) = 1,
Δ2𝑔(𝑑+ 1) = 0,
(A)
or
Δ2 𝑓(𝑑+ 1) = 0,
Δ2𝑔(𝑑+ 1) = 1.
(B)
If Δ2𝐻(𝑑+ 1) = 2, then
Δ2 𝑓(𝑑+ 1) = Δ2𝑔(𝑑+ 1) = 1.
(C)
Case A1: (A)+(L) for 𝑓. Suppose equation (A) holds and the lower alternative (L) holds
for 𝑓with 𝑡= 𝑑+ 1. Then in particular 𝑑+ 1 ≤𝑚1(𝑥) < 𝑐, thus 𝑔(𝑑−1) = 𝑔(𝑑) = 0, hence
Δ𝑔(𝑑) = 0 and therefore
𝐻(𝑑−1) = 𝑓(𝑑−1),
Δ𝐻(𝑑) = Δ 𝑓(𝑑).
By (5), 2 𝑓(𝑑−1) = 𝑑(𝑑+ 1) and Δ 𝑓(𝑑) = 𝑑+ 1. Therefore
𝐻(𝑑−1) = 𝑓(𝑑−1) ≤(𝑑+ 1)2 = (Δ 𝑓(𝑑))2 = (Δ𝐻(𝑑))2.
53
Advancing Mathematics Research with AI-Driven Formal Proof Search
This proves (11) in this case.
Case A2: (A)+(U) for 𝑓. Assume equation (A) holds and the upper alternative (U) holds for
𝑓with 𝑡= 𝑑+ 1. Let us introduce the shorthand notation 𝜌= 𝑒−𝑑. Then (U) gives 𝜌≥−1.
Applying (6) and (7) gives
2 𝑓(𝑑−1) = (𝜌+ 2)(𝜌+ 3),
Δ 𝑓(𝑑) = −(𝜌+ 2).
(13)
The shifted summand satisfies
Δ𝑔(𝑑) ≤0,
2𝑔(𝑑−1) ≤(𝜌+ 2)(𝜌+ 3),
2𝑔(𝑑) ≤(𝜌+ 1)(𝜌+ 2).
(14)
Indeed, the two inequalities for 𝑔(𝑑−1) and 𝑔(𝑑) follow from the universal upper bound (8),
applied to the shifted sequence. For the sign of Δ𝑔(𝑑), if 𝑑< 𝑐, then Δ𝑔(𝑑) = 0. If 𝑑≥𝑐, then
the upper alternative for 𝑓implies
𝑑≥𝑚1(𝑥) + 𝑚1(𝑦) + 1,
𝑑≥𝑚1(𝑥) + 𝑚1(𝑧) + 1,
where {𝑥, 𝑦, 𝑧} = {0, 1, 2}. Adding these inequalities gives
2𝑑≥2𝑚1(𝑥) + 𝑚1(𝑦) + 𝑚1(𝑧) + 2 = 𝑒+ 𝑚1(𝑥) + 2.
Since 𝑐= 𝑚1(𝑥) + 1 and |𝑀red| = 𝑒−𝑐, this is equivalent to 2(𝑑−𝑐) ≥|𝑀red| + 1. Thus the
midpoint monotonicity (9) applies to the shifted 𝑀red-sequence and gives Δ𝑔(𝑑) ≤0.
To prove (11), by (13) it remains to show
𝑓(𝑑−1) + 𝑔(𝑑−1) ≤ −(𝜌+ 2) + Δ𝑔(𝑑)2.
By (13) and (14), this follows from
(𝜌+ 2)(𝜌+ 3) + 2𝑔(𝑑−1) ≤2 −(𝜌+ 2) + Δ𝑔(𝑑)2.
(15)
Since 𝑔(𝑑) = 𝑔(𝑑−1) + Δ𝑔(𝑑), the third inequality in (14) gives
2𝑔(𝑑−1) ≤(𝜌+ 1)(𝜌+ 2) −2Δ𝑔(𝑑).
Therefore the difference between the right-hand side and the left-hand side of (15) is at least
2 −(𝜌+ 2) + Δ𝑔(𝑑)2 −(𝜌+ 2)(𝜌+ 3) − (𝜌+ 1)(𝜌+ 2) −2Δ𝑔(𝑑)
= 2Δ𝑔(𝑑) Δ𝑔(𝑑) −2(𝜌+ 2) + 1
.
This is nonnegative because Δ𝑔(𝑑) ≤0, 𝜌≥−1, and hence
Δ𝑔(𝑑) −2(𝜌+ 2) + 1 ≤0.
Thus (11) holds in this case, and we completed the (A) case.
For the two cases when (B) holds, that is Δ2𝑔(𝑑+ 1) = 1, we use the following shift
reduction. If
Δ2𝐻(𝑑+ 1) = 1
and
𝐻(𝑑+ 1) ≤(Δ𝐻(𝑑+ 1))2,
54
Advancing Mathematics Research with AI-Driven Formal Proof Search
then
𝐻(𝑑−1) ≤(Δ𝐻(𝑑))2.
(16)
Indeed, Δ𝐻(𝑑) = Δ𝐻(𝑑+ 1) −1 and 𝐻(𝑑−1) = 𝐻(𝑑+ 1) −Δ𝐻(𝑑+ 1) −Δ𝐻(𝑑). Therefore
𝐻(𝑑−1) = 𝐻(𝑑+ 1) −2Δ𝐻(𝑑+ 1) + 1 ≤(Δ𝐻(𝑑+ 1))2 −2Δ𝐻(𝑑+ 1) + 1 = (Δ𝐻(𝑑))2.
Case B1: (B)+(L) for 𝑔. Assume equation (B) holds and the lower alternative (L) holds for
𝑔with 𝑡= 𝑑+ 1. Let 𝐷= 𝑑+ 1. Since Δ2𝑔(𝐷) = 1, necessarily 𝐷≥𝑐, and Δ2ℎ𝑀red(𝐷−𝑐) = 1.
In the lower subcase 𝐷−𝑐≤𝑀red(𝑖) for every 𝑖. Then 𝐷−𝑐+ 1 ≥1, and the lower formula
(5) gives
2𝑔(𝐷) = (𝐷−𝑐+ 1)(𝐷−𝑐+ 2),
Δ𝑔(𝐷) = 𝐷−𝑐+ 1.
(17)
We next prove two bounds for 𝑓at 𝐷:
𝑓(𝐷) ≤(𝐷+ 1)Δ 𝑓(𝐷),
Δ 𝑓(𝐷) = 𝑐.
(18)
First, since Δ2 𝑓(𝐷) = 0, the explicit formula (3), together with the lower inequalities for 𝑀red,
implies
𝐷≤𝑚1(0) + 𝑚1(1) + 1,
𝐷≤𝑚1(1) + 𝑚1(2) + 1,
𝐷≤𝑚1(0) + 𝑚1(2) + 1.
(19)
Indeed, the two pair inequalities involving 𝑥follow directly from 𝐷−𝑐≤𝑀red(𝑦) ≤𝑚1(𝑦) for
𝑦≠𝑥. The remaining pair inequality follows from (3): if it failed, then the corresponding
two single indicators would be zero; since 𝐷≥𝑐= 𝑚1(𝑥) + 1, the 𝑥-single indicator is also
zero, and the right-hand side of (3) would be negative, contradicting Δ2 𝑓(𝐷) = 0.
Thus, in (3) for 𝑓at 𝐷, all three pair indicators and the triple indicator are equal to 1.
Since Δ2 𝑓(𝐷) = 0, exactly two of the three single indicators are equal to 1. Moreover the
𝑥-single indicator is zero, because 𝐷≥𝑚1(𝑥) + 1. Hence the two remaining single indicators
are equal to 1.
It follows that for every 1 ≤𝑘≤𝐷, the same two single indicators are still equal to 1,
while the three pair indicators and the triple indicator are also equal to 1. Therefore
Δ2 𝑓(𝑘) ≥2 −3 + 1 = 0
(1 ≤𝑘≤𝐷).
Thus the first differences Δ 𝑓(𝑘) are nondecreasing on {0, 1, . . . , 𝐷}. Since
𝑓(𝐷) =
𝐷
∑︁
𝑗=0
Δ 𝑓( 𝑗),
we get
𝑓(𝐷) ≤(𝐷+ 1)Δ 𝑓(𝐷).
This proves the first inequality in (18).
For the second inequality in (18), relabel the two coordinates different from 𝑥as 𝑦, 𝑧,
and write
𝐴= 𝑚1(𝑦) + 1,
𝐵= 𝑚1(𝑧) + 1,
55
Advancing Mathematics Research with AI-Driven Formal Proof Search
and recall 𝑐= 𝑚1(𝑥) + 1. Using the box-count formula with 𝑥as the third coordinate, the
first-difference formula gives
Δ 𝑓(𝐷) = 𝐿𝐴,𝐵(𝐷) −𝐿𝐴,𝐵(𝐷−𝑐),
because 𝐷≥𝑐. From the preceding paragraph, 𝐷< 𝐴and 𝐷< 𝐵, hence
𝐿𝐴,𝐵(𝐷) = 𝐷+ 1,
𝐿𝐴,𝐵(𝐷−𝑐) = 𝐷−𝑐+ 1.
Therefore
Δ 𝑓(𝐷) = (𝐷+ 1) −(𝐷−𝑐+ 1) = 𝑐,
proving (18). Using (17) and (18), we have
2𝐻(𝐷) = 2 𝑓(𝐷) + 2𝑔(𝐷) ≤2Δ 𝑓(𝐷)(𝐷+ 1) + (𝐷−𝑐+ 1)(𝐷−𝑐+ 2).
Also, by (17),
Δ𝐻(𝐷) = Δ 𝑓(𝐷) + Δ𝑔(𝐷) = Δ 𝑓(𝐷) + (𝐷−𝑐+ 1).
Thus it is enough to show
2Δ 𝑓(𝐷)(𝐷+ 1) + (𝐷−𝑐+ 1)(𝐷−𝑐+ 2) ≤2 Δ 𝑓(𝐷) + 𝐷−𝑐+ 12.
Since 𝐷+ 1 = (𝐷−𝑐+ 1) + 𝑐, the difference between the right-hand side and the left-hand
side is
2Δ 𝑓(𝐷) Δ 𝑓(𝐷) −𝑐 + 2Δ 𝑓(𝐷)(𝐷−𝑐+ 1) + (𝐷−𝑐+ 1)(𝐷−𝑐).
This is nonnegative because Δ 𝑓(𝐷) ≥𝑐and 𝐷−𝑐+ 1 ≥1. Therefore 𝐻(𝐷) ≤(Δ𝐻(𝐷))2. By
the shift reduction (16), this proves (11).
Case B2: (B)+(U) for 𝑔. Again let 𝐷= 𝑑+ 1 and put 𝜌= 𝑒−𝐷. The upper alternative for
ℎ𝑀red at 𝐷−𝑐gives 𝜌≥−2. Since |𝑀red| = 𝑒−𝑐, formulas (6) and (7) give
2𝑔(𝐷) = (𝜌+ 1)(𝜌+ 2),
Δ𝑔(𝐷) = −(𝜌+ 2).
(20)
For the first summand, the universal upper bound (8) gives
2 𝑓(𝐷) ≤(𝑒−𝐷+ 1)(𝑒−𝐷+ 2) = (𝜌+ 1)(𝜌+ 2).
(21)
It remains to justify the sign of Δ 𝑓(𝐷). Since 𝑔is in the upper alternative at 𝐷, we have
𝐷−𝑐≥𝑀red(0) + 𝑀red(1) + 2, 𝐷−𝑐≥𝑀red(1) + 𝑀red(2) + 2, 𝐷−𝑐≥𝑀red(0) + 𝑀red(2) + 2.
Adding these three inequalities gives
3(𝐷−𝑐) ≥2|𝑀red| + 6 = 2(𝑒−𝑐) + 6.
Hence
2(𝐷−𝑐) ≥2
3
 2|𝑀red| + 6 = |𝑀red| + 1 + |𝑀red| + 9
3
> |𝑀red| + 1,
because |𝑀red| ≥0. Therefore
2𝐷= 2(𝐷−𝑐) + 2𝑐≥(𝑒−𝑐+ 1) + 2𝑐= 𝑒+ 𝑐+ 1 ≥𝑒+ 1.
56
Advancing Mathematics Research with AI-Driven Formal Proof Search
By midpoint monotonicity (9), applied to 𝑓= ℎ𝑚1, we get Δ 𝑓(𝐷) ≤0. Using (20), (21), we
get
2𝐻(𝐷) ≤2(𝜌+ 1)(𝜌+ 2),
Δ𝐻(𝐷) = Δ 𝑓(𝐷) −(𝜌+ 2).
Since 𝜌≥−2 and Δ 𝑓(𝐷) ≤0, we have
(𝜌+ 1)(𝜌+ 2) ≤ −Δ 𝑓(𝐷) + 𝜌+ 22.
giving the desired 𝐻(𝐷) ≤(Δ𝐻(𝐷))2. By the shift reduction (16), this proves (11).
Case C: (C) holds. So here Δ2𝐻(𝑑+ 1) = 2 and hence Δ2 𝑓(𝑑+ 1) = Δ2𝑔(𝑑+ 1) = 1. Since
Δ2𝑔(𝑑+ 1) = 1, necessarily 𝑑+ 1 ≥𝑐. Therefore the lower alternative (L) for 𝑓is impossible,
because it would imply 𝑑+ 1 ≤𝑚1(𝑥) < 𝑐. Hence 𝑓is in its upper alternative, that is, (U)
holds for 𝑓. The lower alternative (L) for 𝑔is also impossible. Indeed, if 𝑑+ 1 −𝑐≤𝑀red(𝑖)
for every 𝑖, then, choosing any 𝑦≠𝑥, we get
𝑑+ 1 ≤𝑚1(𝑥) + 1 + 𝑀red(𝑦) = 𝑚1(𝑥) + 1 + 𝑚2(𝑦) ≤𝑚1(𝑥) + 1 + 𝑚1(𝑦).
But the upper alternative for 𝑓gives 𝑑+ 1 ≥𝑚1(𝑥) + 𝑚1(𝑦) + 2, a contradiction. Thus 𝑔is
also in its upper alternative, and (U) holds for 𝑔. Put 𝜌= 𝑒−𝑑again. Since |𝑀red| = 𝑒−𝑐, we
also have |𝑀red| −(𝑑−𝑐) = 𝑒−𝑑= 𝜌. The upper formulas (6) and (7), applied to 𝑓and to
the shifted summand 𝑔, give
2 𝑓(𝑑−1) = (𝜌+ 2)(𝜌+ 3),
Δ 𝑓(𝑑) = −(𝜌+ 2),
and
2𝑔(𝑑−1) = (𝜌+ 2)(𝜌+ 3),
Δ𝑔(𝑑) = −(𝜌+ 2).
Therefore
2𝐻(𝑑−1) = 2(𝜌+ 2)(𝜌+ 3),
Δ𝐻(𝑑) = −2(𝜌+ 2).
Since the upper alternative for 𝑓gives 𝜌≥−1, we have
(Δ𝐻(𝑑))2 −2𝐻(𝑑−1) = 4(𝜌+ 2)2 −2(𝜌+ 2)(𝜌+ 3) = 2(𝜌+ 2)(𝜌+ 1) ≥0.
which proves (12). This completes the proof of (11) and (12), and hence by (10) 𝐻(𝑑−
1)𝐻(𝑑+ 1) ≤𝐻(𝑑)2. Since 0 < 𝑑< 𝑒was arbitrary and 𝐻is the pure 𝑂-sequence of Γ by (2),
the theorem follows.
□
The Lean proof for the problem can be found at https://github.com/google-dee
pmind/alphaproof-nexus-results/tree/main/APNOutputs/AICollaborator/A
lgebraicGeometry.
A Convergence Proof of Modified Anchored Gradient Descent-Ascent
A natural-language version of the convergence proof we discovered can be found in Surina et
al. [58]. The Lean proof is at https://github.com/google-deepmind/alphaproof-n
exus-results/blob/main/APNOutputs/Optimization/LastIterateConvergence.
lean.
57
Advancing Mathematics Research with AI-Driven Formal Proof Search
Written on the Wall, Conjecture 2
For a graph 𝐺, let 𝑉(𝐺) be the set of vertices and 𝐸(𝐺) the set of edges. For 𝑣∈𝑉(𝐺), write
𝑑(𝑣) for the degree of 𝑣, and let 𝑁(𝑣) be the set of vertices adjacent to 𝑣in 𝐺. Let 𝛼(𝑣) be
the local independence number of 𝑣: the size of the largest independent set in 𝐺[𝑁(𝑣)]. Let
ℓ(𝐺) := 1
𝑛
Í
𝑣𝛼(𝑣) be the average of the local independence numbers, and let 𝐿𝑆(𝐺) be the
maximum number of leaves in a spanning tree of 𝐺, or 0 if 𝐺is not connected.
Theorem. If 𝐺is a simple connected graph on 𝑛vertices, then
𝐿𝑆(𝐺) ≥2(ℓ(𝐺) −1).
Proof. Let 𝑉:= 𝑉(𝐺). For every vertex 𝑣∈𝑉, fix a maximum independent set 𝐴(𝑣) in 𝐺[𝑁(𝑣)].
Then 𝛼(𝑣) = |𝐴(𝑣)|.
Now take two copies of 𝑉, and add edges 𝑢𝑣from 𝑢∈𝑉on the left to 𝑣∈𝐴(𝑢) on the
right. This forms a bipartite graph, where vertices on the left side have degree 𝛼(𝑣). The key
idea is to look at the degrees of the vertices on the right side, and formulate the entire proof
in terms of them. Formally, put 𝑐(𝑣) := |𝑢∈𝑉(𝐺) : 𝑣∈𝐴(𝑢)| as the degree of a vertex 𝑣on
the right side.
Note that 𝑐(𝑣) ≤𝑑(𝑣), for all 𝑣∈𝑉. Because Í
𝑣𝛼(𝑣) = Í
𝑣𝑐(𝑣), it is enough to show that
Í
𝑣𝑐(𝑣) ≤𝑛(𝐿𝑆(𝐺)/2 + 1). To simplify the notation, we set 𝜇:= 𝐿𝑆(𝐺)/2 + 1, and so the goal
is to show Í
𝑣𝑐(𝑣) ≤𝑛𝜇.
Lemma 1. For every edge 𝑢𝑣∈𝐸(𝐺) we have 𝑐(𝑢) + 𝑐(𝑣) ≤|𝑁(𝑢) ∪𝑁(𝑣)|.
Proof of Lemma 1. For every vertex 𝑤∈𝑁(𝑢) ∪𝑁(𝑣), at most one of 𝑢and 𝑣can be part
of 𝐴(𝑤), otherwise the edge 𝑢𝑣would contradict the fact that 𝐴(𝑤) is independent. On the
other hand, if 𝑤∈𝑉is such that 𝑢or 𝑣is in 𝐴(𝑤), then 𝑤must be part of 𝑁(𝑢) ∪𝑁(𝑣). Then
𝑐(𝑢) + 𝑐(𝑣) is at most the size of 𝑁(𝑢) ∪𝑁(𝑣). □
Lemma 2. For every edge 𝑢𝑣∈𝐸(𝐺) we have |𝑁(𝑢) ∪𝑁(𝑣)| ≤𝐿𝑆(𝐺) + 2.
Proof of Lemma 2. We construct a spanning tree in 𝐺with at least |𝑁(𝑢) ∪𝑁(𝑣)| −2 leaves.
Start with the edge 𝑢𝑣and add all the vertices in 𝑁(𝑢) ∪𝑁(𝑣) \ {𝑢, 𝑣} as pendant vertices
of degree 1. There are |𝑁(𝑢) ∪𝑁(𝑣)| −2 leaves in this tree 𝑇′. Because 𝐺is connected, we can
expand 𝑇′ to a spanning tree 𝑇of 𝐺by adding edges until no more can be added. Then from
every leaf in 𝑇′ there is a path to a leaf in 𝑇that doesn’t cross 𝑢𝑣. All these leaves must be
distinct, since they are contained in distinct subtrees of 𝑇. Then 𝑇has at least |𝑁(𝑢)∪𝑁(𝑣)|−2
leaves. □
Lemmas 1 and 2 show that for every edge 𝑢𝑣∈𝐸(𝐺),
𝑐(𝑢) + 𝑐(𝑣) ≤𝐿𝑆(𝐺) + 2 = 2𝜇.
Next, we observe that Í
𝑣𝑐(𝑣) ≤𝑛𝜇trivially holds if every 𝑐(𝑣) ≤𝜇. So assume this is
not the case. Then we can split the vertices into "heavy" vertices with 𝑐(𝑣) > 𝜇, and "light"
vertices with 𝑐(𝑣) ≤𝜇. Let 𝑆be the set of heavy vertices.
𝑆must be an independent set, since the above equation shows that for any edge 𝑢𝑣,
at most one of 𝑢or 𝑣can be heavy. Less obvious is that light vertices cannot have many
neighbors in 𝑆.
Lemma 3. If 𝑣is a light vertex, then |𝑁(𝑣) ∩𝑆| < 𝜇.
58
Advancing Mathematics Research with AI-Driven Formal Proof Search
Proof of Lemma 3. Let 𝑢∈𝑁(𝑣) ∩𝑆. Since 𝑆is independent, all neighbours of 𝑢are outside
𝑁(𝑣) ∩𝑆. So |𝑁(𝑢) ∪𝑁(𝑣)| ≥|𝑁(𝑣) ∩𝑆| + |𝑁(𝑢)|. Using Lemma 2 we get
|𝑁(𝑣) ∩𝑆| ≤|𝑁(𝑢) ∪𝑁(𝑣)| −|𝑁(𝑢)| ≤𝐿𝑆(𝐺) + 2 −𝑑(𝑢).
As 𝑑(𝑢) ≥𝑐(𝑢) > 𝜇, we obtain |𝑁(𝑣) ∩𝑆| < 𝐿𝑆(𝐺) + 2 −𝜇= 𝜇. □
Then the theorem follows from the following more general statement:
Claim. Let 𝑐: 𝑉→ℝand 𝜇≥0 satisfy:
1. 𝑐(𝑣) ≤𝑑(𝑣) for all 𝑣,
2. 𝑐(𝑢) + 𝑐(𝑣) ≤2𝜇for every edge 𝑢𝑣,
3. 𝑆:= {𝑢: 𝑐(𝑢) > 𝜇} is an independent set,
4. |𝑁(𝑣) ∩𝑆| < 𝜇for every 𝑣∉𝑆.
Then Í
𝑣𝑐(𝑣) ≤𝑛𝜇.
Proof of Claim. We assume 𝑆is non-empty, otherwise the claim is trivially true. The proof
uses a discharging argument: it sends the excess 𝑐(𝑢) −𝜇from a heavy vertex 𝑢∈𝑆to its
neighbors. The redistribution keeps the total sum Í
𝑣𝑐(𝑣) constant. However, the amount
sent to a light vertex 𝑣is less than the slack 𝜇−𝑐(𝑣), so the overall sum can’t exceed 𝑛𝜇.
Precisely, define a weight function that transfers excess from heavy to light vertices:
𝑊(𝑢, 𝑣) :=
( 𝜇−𝑐(𝑣)
𝑑(𝑢)
if 𝑢∈𝑆and 𝑢𝑣is an edge,
0
otherwise.
Because 𝑆is independent, the weight flows only from heavy to light vertices. We now show
two statements.
Each heavy vertex sends out enough weight. If 𝑢∈𝑆and 𝑢𝑣is an edge, then 𝑐(𝑢)+𝑐(𝑣) ≤2𝜇
by condition 2. So 𝜇−𝑐(𝑣) ≥𝑐(𝑢) −𝜇. Then
∑︁
𝑣∈𝑁(𝑢)
𝑊(𝑢, 𝑣) ≥𝑑(𝑢) 𝑐(𝑢) −𝜇
𝑑(𝑢)
= 𝑐(𝑢) −𝜇.
Each light vertex absorbs at most its slack. Let 𝑣∉𝑆. Then 𝑣receives weight from vertices
in 𝐹:= 𝑁(𝑣) ∩𝑆.
Let 𝑢∈𝐹. From conditions (1) and (4), we have |𝐹| < 𝜇< 𝑐(𝑢) ≤𝑑(𝑢). Then the total weight
received is
∑︁
𝑢∈𝐹
𝑊(𝑢, 𝑣) =
∑︁
𝑢∈𝐹
𝜇−𝑐(𝑣)
𝑑(𝑢)
<
∑︁
𝑢∈𝐹
𝜇−𝑐(𝑣)
|𝐹|
= 𝜇−𝑐(𝑣).
These two statements together show that
∑︁
𝑢∈𝑆
𝑐(𝑢) −𝜇≤
∑︁
𝑢∈𝑆
∑︁
𝑣∉𝑆
𝑊(𝑢, 𝑣) =
∑︁
𝑣∉𝑆
∑︁
𝑢∈𝑆
𝑊(𝑢, 𝑣) ≤
∑︁
𝑣∉𝑆
𝜇−𝑐(𝑣).
Re-arranging the terms gives Í
𝑣𝑐(𝑣) < 𝑛𝜇as desired.
□
The discovered lean proof for this is available at https://github.com/google-dee
pmind/alphaproof-nexus-results/blob/main/APNOutputs/OEIS/GraphConjec
ture2.lean.
59
