---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-014-erdős-12-ii
section_title: "Erdős #12-(ii)"
section_number: null
pages: 31-34
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
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
