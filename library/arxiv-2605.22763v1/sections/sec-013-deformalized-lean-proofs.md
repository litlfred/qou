---
doc_id: arxiv-2605.22763v1
doc_title: "2026-5-22 Advancing Mathematics Research with AI-Driven Formal Proof Search George Tsoukalas1† , Anton Kovsharov1† , Sergey Shirobokov1† , Anja Surina1, Moritz Firsching1, Gergely"
section_id: sec-013-deformalized-lean-proofs
section_title: "Deformalized Lean Proofs"
section_number: null
pages: 30-59
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
doc_brief: "2026-5-22 Advancing Mathematics Research with AI-Driven Formal Proof Search George Tsoukalas1† , Anton Kovsharov1† , Sergey Shirobokov1† , Anja Surina1, Moritz Firsching1, Gergely — 14 sections: Intro"
---
Next, we give deformalized versions of the Lean proofs discovered by our full-featured Agent
(D).
Erdős #12-(i)
First, we give the proof of the first question under Erdős problem #12, as classified on the
ErdosProblems site (https://www.erdosproblems.com).
Theorem (i).There is an infinite set𝐴⊆ℕ satisfying that there are no distinct𝑎,𝑏,𝑐∈𝐴
with𝑎 < 𝑏,𝑐satisfying𝑎|𝑏+𝑐and
lim inf
𝑁→∞
|𝐴∩{1,...,𝑁}|
𝑁 1/2 >0.
Proof.We will construct a sequence of "blocks" that individually cannot contain such𝑎,𝑏,𝑐 ,
and with a careful choice of parameters, their union forms the desired set. By precisely
controlling the growth and modular residues of these blocks, we ensure the set remains
denseenoughtosatisfythe lim inf conditionwhileavoidingallforbiddendivisibilityrelations.
Let 𝑓 : ℕ→ℕ be defined by 𝑓( 0)= 0and 𝑓(𝑛)= 3𝑓(⌊𝑛/ 2⌋)+(𝑛mod 2). The func-
tion 𝑓 takes a number represented in base 2 and outputs the number given by the same
representation but read in base 3. In particular, the base 3 representation of𝑓(𝑛) will contain
only0s and1s. For this reason,𝑓(𝑎)+𝑓(𝑏)= 2𝑓(𝑐) implies𝑎=𝑏=𝑐 , ensuring the sequence
(𝑓(𝑛)) 𝑛∈ℕ contains no 3-APs.
Next, let𝐹𝑖 be the𝑖-th odd prime, and write𝑀𝑖 = ˛
𝑗<𝑖 𝐹𝑗 and 𝑉𝑖 =𝐹 𝑖𝑀𝑖. By Bertrand’s
postulate, we have𝐹𝑖≤ 2𝑖+2. By the Chinese Remainder Theorem, for each𝑖, let𝐶𝑖 <𝑉 𝑖 be
the unique integer such that𝐶𝑖≡0(mod𝐹 𝑖)and𝐶 𝑖≡1(mod𝑀 𝑖).
Now we define the parameters for the blocks(𝐵𝑖). Let
•𝑌 𝑖 = 3(𝑖+20) 3
be the exponential bounding scale to control the distance between blocks.
•𝑃 𝑖 =10𝑉𝑖𝑌𝑖+𝐶 𝑖 be the starting coordinate of block𝑖.
•𝑋 𝑖 =⌊√
𝑃𝑖+1⌋ be the element capacity of block𝑖. Note that the capacity of𝐵𝑖 is directly
tied to the starting point of the next block𝐵𝑖+1.
30
Advancing Mathematics Research with AI-Driven Formal Proof Search
Formally, define𝐵𝑖 ={𝑃 𝑖+𝑉𝑖𝑓(𝑦)|𝑦 < 𝑋 𝑖}. The purpose of𝑌𝑖 is to keep the blocks relatively
narrow while ensuring they are well-spaced. Note that if𝑦 < 2𝑘, then 𝑓(𝑦)< 3𝑘. Letting
𝑘=(𝑖+ 20)3, we want to guarantee that for any𝑦 < 𝑋𝑖, we have𝑓(𝑦)<𝑌 𝑖 = 3𝑘. To do this, it
suffices to show𝑋𝑖≤√
𝑃𝑖+1 <2 𝑘, which is equivalent to𝑃𝑖+1≤4 𝑘.
Observe that 𝑃𝑖+1 ≤ 11𝑉𝑖+1𝑌𝑖+1 ≤ 11· 2(𝑖+4) 2
· 3(𝑖+21) 3
, following from the bound on𝐹𝑖.
This is asymptotically strictly smaller than4𝑘 = 4(𝑖+20) 3
. By adding the shift of20, the
inequality11·2 (𝑖+4) 2
·3(𝑖+21) 3
≤4(𝑖+20) 3
holds universally for all𝑖≥1.
Set 𝐴= —
𝑖∈ℕ 𝐵𝑖. Clearly,𝐴 is an infinite set. Suppose, for the sake of contradiction, that there
exist distinct𝑎,𝑏,𝑐∈𝐴with𝑎 < 𝑏,𝑐such that𝑎|(𝑏+𝑐). Let𝑎∈𝐵 𝑖. We analyze two cases:
• (Case 1: Cross-block) Suppose at least one of𝑏,𝑐 is not in𝐵𝑖. Without loss of generality,
assume𝑏∈𝐵 𝑗 for some𝑗 > 𝑖(since𝑏 > 𝑎). Since𝑎∈𝐵 𝑖, we have𝑎≡ 0(mod𝐹 𝑖), and
thus𝑏+𝑐≡ 0(mod𝐹 𝑖) by the divisibility condition. However, by our CRT construction,
𝑏≡ 1(mod𝐹 𝑖). The element𝑐 must belong to some block𝐵𝑚 with 𝑚≥𝑖 , so𝑐≡ 0
(mod𝐹 𝑖) (if 𝑚=𝑖 ) or𝑐≡ 1(mod𝐹 𝑖) (if 𝑚 > 𝑖). Therefore, 𝑏+𝑐≡ 1(mod𝐹 𝑖) or
𝑏+𝑐≡2(mod𝐹 𝑖). Since𝐹 𝑖≥3, this directly contradicts𝑏+𝑐≡0(mod𝐹 𝑖).
• (Case 2: Same block) Suppose𝑏,𝑐∈𝐵 𝑖. They must be tightly clustered around𝑃𝑖.
Because 𝑦 < 𝑋𝑖, we have𝑓(𝑦)<𝑌 𝑖. The maximum "noise" added to any block element is
𝑉𝑖𝑌𝑖. Since𝑃𝑖 > 10𝑉𝑖𝑌𝑖, any𝑥∈𝐵 𝑖 must satisfy𝑥∈[𝑃 𝑖, 1.1𝑃𝑖]. The divisibility condition
𝑎| (𝑏+𝑐) implies 𝑚𝑎=𝑏+𝑐 for some integer𝑚. Because 𝑏+𝑐∈ [ 2𝑃𝑖, 2.2𝑃𝑖] and
𝑎∈[𝑃 𝑖,1.1𝑃 𝑖], it must be that𝑚=2, implying2𝑎=𝑏+𝑐.
Writing the elements as𝑎=𝑃 𝑖+𝑉𝑖𝑓(𝑎′),𝑏=𝑃 𝑖+𝑉𝑖𝑓(𝑏′), and𝑐=𝑃 𝑖+𝑉𝑖𝑓(𝑐′), substitution and
cancellation yield2𝑓(𝑎′)=𝑓(𝑏 ′)+𝑓(𝑐 ′). This is impossible for distinct𝑎′,𝑏′,𝑐′ because the
image of𝑓avoids 3-APs, contradicting the assumption that𝑎,𝑏,𝑐are distinct.
Finally, we show that𝐶(𝑁)=|𝐴∩{ 1,...,𝑁}|≥𝑐
√
𝑁 for some constant𝑐 > 0. We split
into two cases:
1.𝑁 falls in the gap between𝐵𝑖 and 𝐵𝑖+1; precisely,𝑃𝑖+𝑉 𝑖𝑌𝑖≤𝑁 < 𝑃 𝑖+1. Here, 𝐶(𝑁)
counts at least all elements in𝐵𝑖, meaning𝐶(𝑁)≥𝑋 𝑖 =⌊√
𝑃𝑖+1⌋. Since𝑁≤𝑃 𝑖+1, we
have
√
𝑁≤ √
𝑃𝑖+1. Thus, 𝐶(𝑁)√
𝑁 ≥ ⌊√𝑃𝑖+1⌋√𝑃𝑖+1
≈1.
2.𝑁 is inside the block𝐵𝑖; precisely,𝑃𝑖≤𝑁 < 𝑃𝑖+𝑉𝑖𝑌𝑖. A pessimistic lower bound counts
only the elements up to the previous block, giving𝐶(𝑁)≥𝑋 𝑖−1 =⌊√
𝑃𝑖⌋. Observe that
𝑉𝑖𝑌𝑖≤0.1𝑃 𝑖, so𝑁≤1.1𝑃 𝑖 <2𝑃 𝑖. Consequently,√
𝑃𝑖 >
√︁
𝑁/2, which implies𝐶(𝑁)√
𝑁 ≥ 1√
2.
In both cases,lim inf𝑁→∞
𝐶(𝑁)
𝑁1/2≥ 1√
2 >0.□
Erdős #12-(ii)
Next, we give a proof for the second question of the three listed in Erdős #12.
Theorem (ii).There exists an infinite set𝐴⊂ℤ + with no distinct𝑎,𝑏,𝑐∈𝐴 with 𝑏,𝑐 > 𝑎,
31
Advancing Mathematics Research with AI-Driven Formal Proof Search
and𝑎|𝑏+𝑐, yet for any𝜀 >0and all sufficiently large𝑁:
|𝐴∩{1,...,𝑁}|≥𝑁 1−𝜀.
Consequently, there is no absolute constant𝑐 > 0such that every such set 𝐴 satisfies
|𝐴∩{1,...,𝑁}|< 𝑁 1−𝑐 for infinitely many𝑁.
Proof.The proof is similar to the previous one for Erdős #12(i), differing mainly in the use
of a Behrend-style construction to produce a dense 3-AP-free set.
Let 𝑐∈ (0, 1), and let(𝑃𝑘) be a sequence of pairwise coprime integers with𝑃𝑘 ≥ 3
and 𝑃𝑘≤ 4𝑘+2 (for example, we can choose𝑃𝑘 to be the𝑘-th odd prime). Next, define the
running product𝐿𝑘 = ˛𝑘
𝑖=0𝑃𝑖. As before, we have𝐿𝑘≤ 4(𝑘+2) 2
. By the Chinese Remainder The-
orem, thereareintegers 𝑅𝑘 < 𝐿𝑘 satisfying 𝑅𝑘≡ 0(mod𝑃 𝑘) and𝑅𝑘≡ 1(mod𝑃 𝑖) forall 𝑖 < 𝑘.
Choose an integer𝑚≥ 2satisfying 𝑚 >( 2𝑚+ 1)1−𝑐/2 and define the dimension𝑉𝑘 =(𝑘+ 10)4.
We use a construction of Behrend to generate dense sets free of 3-term arithmetic progres-
sions. Consider the grid of vectors{1,...,𝑚} 𝑉𝑘−1. Let𝑣=(𝑣 0,...,𝑣 𝑉𝑘−2) be such a vector. The
squared norm∥𝑣∥ 2
2 takes integer values in the range[𝑉𝑘− 1,(𝑉 𝑘− 1)𝑚2]. By the pigeonhole
principle, there exists an integer radius𝐾 such that the number of vectors on this sphere
satisfies|{𝑣∈{1,...,𝑚} 𝑉𝑘−1|∥𝑣∥ 2
2 =𝐾}|≥𝑚 𝑉𝑘−1/(𝑉𝑘𝑚2+1).
Define𝑆𝑘 as the set of integers formed by evaluating these vectors in base2𝑚+ 1, strictly
offset by adding a massive leading digit𝑚(2𝑚+1)𝑉𝑘−1:
𝑆𝑘 =
(
𝑚(2𝑚+1) 𝑉𝑘−1+
𝑉𝑘−2∑︁
𝑖=0
𝑣𝑖(2𝑚+1) 𝑖

 𝑣∈{1,...,𝑚} 𝑉𝑘−1,
𝑉𝑘−2∑︁
𝑖=0
𝑣2
𝑖 =𝐾
)
Because the digits are bounded by𝑚, adding two elements in base2𝑚+ 1involves no
carrying. The restriction to the sphere of radius
√
𝐾 ensures𝑆𝑘 contains no 3-APs. Further-
more, because the vectors use digits strictly between1and𝑚, every element𝑥∈𝑆 𝑘 satisfies
𝑚(2𝑚+1) 𝑉𝑘−1≤𝑥 <(𝑚+1)(2𝑚+1) 𝑉𝑘−1, ensuring the set is tightly clustered.
We define the blocks𝐴𝑘 ={𝐿 𝑘𝑥+𝑅 𝑘|𝑥∈𝑆 𝑘}, and set𝐴= —
𝑘∈ℕ 𝐴𝑘. Clearly, 𝐴 is an in-
finite set. We verify𝐴 contains no distinct𝑎,𝑏,𝑐 such that𝑎|(𝑏+𝑐) with𝑏,𝑐 > 𝑎. If𝑎,𝑏,𝑐 are
in different blocks, a similar modular arithmetic argument as before using the CRT conditions
yields a contradiction. If they are in the same block, the tightness of𝑆𝑘 guarantees𝑏+𝑐 < 3𝑎,
forcing the divisibility multiplier to be exactly 2 (i.e.,2𝑎=𝑏+𝑐 ), which contradicts the fact
that𝑆𝑘 is 3-AP-free. To ensure the blocks𝐴𝑘 do not overlap, we bound their elements. The
maximum element in𝐴𝑘 is bounded above by:
max(𝐴𝑘)≤𝐿 𝑘(𝑚+1)(2𝑚+1) 𝑉𝑘−1
The minimum element in the next block𝐴𝑘+1 is bounded below by:
min(𝐴𝑘+1)≥𝐿 𝑘+1𝑚(2𝑚+1) 𝑉𝑘+1−1
Because the dimension𝑉𝑘+1 =(𝑘+ 11)4 is significantly larger than𝑉𝑘 =(𝑘+ 10)4, the base
exponent strictly dominates, separating the blocks.
32
Advancing Mathematics Research with AI-Driven Formal Proof Search
We now show that|𝐴∩{ 1,...,𝑁}| ≥𝑁 1−𝑐 for sufficiently large𝑁. The density drops
the most in the empty gaps between blocks, with the absolute minimum occurring immedi-
ately before block𝐴𝑘+1 begins. At this point,𝑁=min(𝐴 𝑘+1)− 1, and our total element count
is strictly greater than|𝐴𝑘|. Thus, it suffices to prove:
|𝐴𝑘|≥(max(𝐴 𝑘+1)) 1−𝑐
Substituting our parameter bounds into this inequality yields, and since𝑚 was chosen to
satisfy𝑚 >(2𝑚+1) 1−𝑐/2, it remains to prove

(2𝑚+1) 1−𝑐/2
𝑉𝑘−1
𝑉𝑘𝑚2+1 ≥

𝐿𝑘+1(𝑚+1)(2𝑚+1) 𝑉𝑘+1−1
 1−𝑐
Ignoring the polynomial denominator and constant multipliers, we compare the asymptotic
growth of the exponents on the base2𝑚+1:
•On the left hand side, the exponent is(1−𝑐/2)(𝑉𝑘−1)=(1−𝑐/2)𝑘 4+𝑂(𝑘 3).
• On the right hand side, the exponent is(1−𝑐)(𝑉 𝑘+1− 1)=( 1−𝑐)(𝑘+ 11)4 =( 1−𝑐)𝑘 4+
𝑂(𝑘 3).
The contribution of the running product𝐿𝑘+1≤ 4(𝑘+3) 2
and the constant(𝑚+ 1) to the right
hand side is only𝑂(𝑘 2), which is safely absorbed into the𝑂(𝑘 3) error term. Because𝑐 >0,
the 𝑘4 coefficient on the left hand side(1−𝑐/ 2) is strictly greater than the𝑘4 coefficient on
the right hand side(1−𝑐) . Thus, for sufficiently large𝑘, the left hand side asymptotically
dominates, and the inequality holds.□
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
question, asking whether such a set𝐴 could satisfy˝
𝑎∈𝐴 1/𝑎=∞ , is still open and seems
difficult.
We provide the Lean proof discovered for (i) athttps://github.com/google-dee
pmind/alphaproof-nexus-results/blob/main/APNOutputs/ErdosProblems/er
dos_12.parts.i.lean and for (ii) athttps://github.com/google-deepmind/alph
aproof-nexus-results/blob/main/APNOutputs/ErdosProblems/erdos_12.par
ts.ii.lean. Our original communication of the result can be found at the problem thread
of the ErdosProblems site:https://www.erdosproblems.com/forum/thread/12.
33
Advancing Mathematics Research with AI-Driven Formal Proof Search
Erdős #125
Question.Let 𝐴={ ˝𝜖𝑘3𝑘 :𝜖𝑘∈{ 0, 1}} be the set of integers which have only the digits 0,1
when written base 3, and𝐵={ ˝𝜖𝑘4𝑘 : 𝜖𝑘∈{ 0, 1}} be the set of integers which have only
the digits0,1when written base4. Does𝐴+𝐵have positive lower density?
Proof.We show that the answer is no: the lower density is zero. Let𝐴 and 𝐵 be defined as
the sets of integers whose base 3 and base 4 representations, respectively, contain only the
digits 0 and 1. We will show that the lower density of𝐴+𝐵is zero.
For any integer𝑎∈𝐴 , we can decompose it at the𝑘-th digit into a top and bottom part,
writing 𝑎= 3𝑘𝑎𝑡𝑜𝑝+𝑎 𝑏𝑜𝑡. Because𝑎 uses only the digits 0 and 1, both𝑎𝑡𝑜𝑝 and 𝑎𝑏𝑜𝑡 must also
belong to𝐴. Furthermore, the maximum possible value for𝑎𝑏𝑜𝑡 is the integer consisting of𝑘
ones in base 3, which provides the strict upper bound𝑎𝑏𝑜𝑡≤( 3𝑘− 1)/2. By applying the exact
same logic to any𝑏∈𝐵 at scale𝑚, we can write𝑏= 4𝑚𝑏𝑡𝑜𝑝+𝑏 𝑏𝑜𝑡, yielding the analogous
bound𝑏 𝑏𝑜𝑡≤(4 𝑚−1)/3.
To evaluate the density of𝐴+𝐵 up to a large scale, we define a threshold𝑀·𝑁 0, where
𝑀=min( 3𝑘, 4𝑚) for some integers𝑘 and 𝑚. Consider any element𝑥∈𝐴+𝐵 such that
𝑥 < 𝑀·𝑁0. By definition,𝑥=𝑎+𝑏 for some𝑎∈𝐴 and𝑏∈𝐵 . Using the previously established
decompositions, we can express this sum as𝑥= 3𝑘𝑎𝑡𝑜𝑝+𝑎 𝑏𝑜𝑡+ 4𝑚𝑏𝑡𝑜𝑝+𝑏 𝑏𝑜𝑡. Assume without
loss of generality that3𝑘≤ 4𝑚, so𝑀= 3𝑘. We can rewrite this expression to factor out𝑀,
yielding𝑥=3 𝑘(𝑎𝑡𝑜𝑝+𝑏 𝑡𝑜𝑝)+𝑐, where the remainder term is𝑐=(4 𝑚−3 𝑘)𝑏𝑡𝑜𝑝+𝑎 𝑏𝑜𝑡+𝑏 𝑏𝑜𝑡.
Let 𝑦=𝑎 𝑡𝑜𝑝+𝑏 𝑡𝑜𝑝. Since 𝑎𝑡𝑜𝑝 ∈𝐴 and 𝑏𝑡𝑜𝑝 ∈𝐵 , it naturally follows that𝑦∈𝐴+𝐵 .
Furthermore, because𝑥 <3𝑘𝑁0, we must have𝑦 < 𝑁0, which in turn dictates that𝑏𝑡𝑜𝑝≤𝑁 0.
Applying our bounds for the bottom parts, we can bound the remainder𝑐 by a maximum
value𝐶, defined as𝐶=|4 𝑚−3 𝑘|𝑁 0+(3 𝑘−1)/2+(4 𝑚−1)/3.
This shows that any valid sum𝑥 < 𝑀·𝑁0 is uniquely determined by choosing a base value
𝑦∈(𝐴+𝐵)∩[ 0,𝑁 0) and a remainder𝑐∈[ 0,𝐶] . Therefore, the total number of elements in
𝐴+𝐵 strictly less than𝑀·𝑁 0 is bounded by the product of the number of choices for𝑦 and
the number of choices for𝑐. Dividing by the interval length𝑀·𝑁 0 yields an upper bound on
the density at this new scale: the density up to𝑀·𝑁 0 is less than or equal to the density up
to𝑁 0 multiplied by the factor(𝐶+1)/𝑀.
To force the density to drop, we require this multiplying factor to be strictly less than 1.
Because the ratio of logarithmsln(4)/ln( 3) is irrational, Dirichlet’s Approximation Theorem
guarantees that we can find arbitrarily large integers𝑘 and𝑚 such that the ratio4𝑚/3𝑘 is
arbitrarily close to 1. By choosing𝑘 and𝑚 carefully, the absolute difference|4𝑚− 3𝑘| becomes
extremely small relative to𝑀. Consequently, for any given𝑁0, we can select𝑘 and𝑚 large
enough such that(𝐶+1)/𝑀≤0.99.
We can now apply this bounding process iteratively. Starting from an arbitrary scale𝑁0,
we can find a larger scale𝑁1 =𝑀 1𝑁0 where the density of𝐴+𝐵 drops by a factor of at least
0.99. Taking𝑁1 as our new baseline, we find a still larger scale𝑁2 =𝑀 2𝑁1 where the density
drops by another factor of0.99. After𝑟 iterations, the density of the set up to the scale𝑁𝑟 is
bounded by(0.99)𝑟. As𝑟→∞ , this bound approaches 0. This demonstrates the existence of
a sequence of arbitrarily large scales where the density tends to 0, proving that the lower
density of𝐴+𝐵is 0.□
34
Advancing Mathematics Research with AI-Driven Formal Proof Search
We originally communicated the result inhttps://www.erdosproblems.com/fo
rum/thread/125#post-5110 . The Lean proof is athttps://github.com/google-d
eepmind/alphaproof-nexus-results/blob/main/APNOutputs/ErdosProblem
s/erdos_125.variants.positive_lower_density.lean . In the discussion at the
ErdosProblems site, it was pointed out that this leaves two possibilities regarding the set
𝐴+𝐵:
1.𝐴+𝐵has zero upper and lower density (and hence also zero density), or
2.𝐴+𝐵has zero lower density, but positive upper density (and hence no density).
Erdős #138, Differences Variant
Question.Let the van der Waerden number𝑊(𝑘) be such that whenever𝑁≥𝑊(𝑘) and
{1,...,𝑁} is 2-coloured there must exist a monochromatic𝑘-term arithmetic progression. Is
it true that𝑊(𝑘+1)−𝑊(𝑘)→∞?
Proof.We will show that𝑊(𝑘+ 1)≥𝑊(𝑘)+𝑘 , which establishes that𝑊(𝑘+ 1)−𝑊(𝑘)→∞ .
Given a 2-coloring of the first𝑊(𝑘)− 1integers without a monochromatic𝑘-AP, we can
extend it by𝑘 further elements without creating a monochromatic(𝑘+ 1)-AP by proceeding
greedily. Adding new elements one by one, suppose we have validly colored up to𝑀 (where
𝑀 <𝑊(𝑘)− 1+𝑘); we simply color𝑀+ 1red if doing so doesn’t create a red(𝑘+ 1)-AP, and
blue otherwise.
The only way this algorithm could result in an invalid coloring is if both choices are
blocked, meaning there is already a red𝑘-AP with some step size𝑑𝑅 and a blue𝑘-AP with
some step size𝑑𝐵 such that the(𝑘+ 1)-th element for both progressions lands exactly on𝑀+ 1.
But this is impossible. Because our original interval up to𝑊(𝑘)− 1has no monochromatic
𝑘-APs, these progressions must contain at least one newly added element, which bounds their
step sizes to𝑑𝑅,𝑑 𝐵≤𝑘− 1. Hence, if we step backward𝑑𝐵 times along the red progression
and𝑑𝑅 times along the blue progression, both calculations land exactly on the positive integer
𝑀+ 1−𝑑 𝑅𝑑𝐵, meaning this single point would have to be simultaneously colored red and
blue, which is a contradiction.□
We originally communicated the result inhttps://www.erdosproblems.com/foru
m/thread/138#post-5314, and share the Lean proof athttps://github.com/googl
e-deepmind/alphaproof-nexus-results/blob/main/APNOutputs/ErdosProbl
ems/erdos_138.variants.difference.lean. In the discussion at the ErdosProblems
site, Thomas Bloom pointed out that the obvious generalization of this argument gives
𝑊(𝑘+ 1,𝑙+ 1)≥𝑊(𝑘,𝑙)+min(𝑘,𝑙) , and asked what this kind of argument can prove for the
𝑟-color variant𝑊𝑟(𝑘).
Erdős #741-(i)
Question.Let 𝐴⊆ℕ be such that𝐴+𝐴 has positive upper density. Can one always decompose
𝐴=𝐴 1⊔𝐴 2 such that𝐴 1+𝐴 1 and𝐴 2+𝐴 2 both have positive upper density?
Proof.We show that the answer is yes. We use an alternating block partition. Given a rapidly
35
Advancing Mathematics Research with AI-Driven Formal Proof Search
growing sequence𝑀 0 < 𝑀1 < 𝑀2 <···, we define
𝐴1 =𝐴∩
Ø
𝑘
(𝑀 2𝑘,𝑀 2𝑘+1], 𝐴 2 =𝐴\𝐴 1.
In odd-indexed intervals(𝑀 2𝑘,𝑀 2𝑘+1], all elements of𝐴 belong to𝐴1; in even-indexed inter-
vals(𝑀 2𝑘+1,𝑀 2𝑘+2], they all belong to𝐴2. The sequence𝑀 is chosen to grow fast enough
that each block dwarfs all previous ones. We split into two cases.
Case 1: 𝐴 has positive upper density.There exist a constant 𝑐 > 0and a strictly in-
creasing sequence of scales along which|𝐴∩[ 1,𝑁]| ≥𝑐·𝑁 . Using a dependent-choice
argument, we extract a rapidly growing sequence𝑀𝑘 such that for each𝑘:
•|𝐴∩[1,𝑀 𝑘+1]|≥𝑐·𝑀 𝑘+1 (density is retained at the next scale),
•|𝐴∩[1,𝑀 𝑘]|≤ 𝑐
4·𝑀 𝑘+1 (the “past” is negligible relative to the “future”).
Because each new block contains all the “fresh” elements of𝐴, looking at scale𝑀2𝑘+1 shows
that 𝐴1 has positive upper density, and looking at scale𝑀2𝑘+2 shows the same for𝐴2. A
short argument then lifts this: if a set has positive upper density, so does its sumset with itself.
Case 2: 𝐴 has zero upper density but𝐴+𝐴 has positive upper density.This is the
harder case, since𝐴 is too sparse to guarantee positive density for the parts directly. Instead,
we argue about the sumsets themselves. Since𝐴+𝐴 has positive upper density, there exist
𝑐 > 0and a sequence of scales along which|(𝐴+𝐴)∩[ 1,𝑁]|≥𝑐·𝑁 . Since 𝐴 has zero
upper density,|𝐴∩[ 1,𝑁]|=𝑜(𝑁) , so for any fixed𝐾 there are arbitrarily large𝑁 where
(𝐾+ 1)·|𝐴∩[ 1,𝑁]|≤ 𝑐
4·𝑁 . By dependent choice, we extract a rapidly growing𝑀𝑘 such that
for each𝑘:
•|(𝐴+𝐴)∩[1,𝑀 𝑘+1]|≥𝑐·𝑀 𝑘+1,
•(𝑀 𝑘+1)·|𝐴∩[1,𝑀 𝑘+1]|≤ 𝑐
4·𝑀 𝑘+1.
The key ingredient is a combinatorial sumset bound: if𝐴=𝐴 1∪𝐴 2 and every element of𝐴2
in[1,𝑁]is at most𝐾, then
|(𝐴+𝐴)∩[1,𝑁]|≤|(𝐴 1+𝐴 1)∩[1,𝑁]|+(𝐾+1)·|𝐴∩[1,𝑁]|.
The idea is that any sum involving an element of𝐴2 has one summand bounded by𝐾, giving
at most(𝐾+1)·|𝐴∩[1,𝑁]|such sums. Applying this bound at alternating scales:
• At scale𝑁=𝑀 2𝑘+1: all elements of𝐴2 in[1,𝑁] lie below𝑀2𝑘, so the bound with
𝐾=𝑀 2𝑘 gives|(𝐴 1+𝐴 1)∩[1,𝑁]|≥ 3𝑐
4·𝑁.
• At scale𝑁=𝑀 2𝑘+2: symmetrically, all elements of𝐴1 in[1,𝑁] lie below𝑀2𝑘+1, giving
|(𝐴 2+𝐴 2)∩[1,𝑁]|≥ 3𝑐
4·𝑁.
Since these bounds hold for infinitely many𝑁, both sumsets have positive upper density.□
The agent also initially disproved a strict “natural density” formulation of this problem
(where the density must exist as a limit), which served as a diagnostic for the correct
36
Advancing Mathematics Research with AI-Driven Formal Proof Search
interpretation of Erdős’ original phrasing. Following Thomas Bloom’s observation that Erdős
likely meant “positive upper density,” the formulation was amended and the agent resolved
the corrected version as described above. The Lean proof for the upper density variant is
available athttps://github.com/google-deepmind/alphaproof-nexus-results
/blob/main/APNOutputs/ErdosProblems/erdos_741.parts.i.lean.
Erdős #741-(ii)
Question.Is there a basis𝐴 of order2such that if 𝐴=𝐴 1⊔𝐴 2 then 𝐴1+𝐴 1 and 𝐴2+𝐴 2
cannot both have bounded gaps?
Proof.We show that the answer is yes by constructing a pathological basis𝐴 with “forbidden
zones” that force any partition to create arbitrarily large gaps in at least one component
sumset.
Step 1: The construction.Choose a sequence of rapidly growing scales𝑃𝑘 = 100𝑘. For each
𝑘≥ 1, define a forbidden zone𝑍𝑘, which is a broad interval of integers running roughly
from 11
2 𝑃𝑘 to11 𝑃𝑘+𝑘 . In the middle of this zone, we leave a single “oasis” — an isolated
element 𝑥𝑘 = 10𝑃𝑘. The set𝐴 consists of all natural numbers that avoid every forbidden
zone, together with the oases𝑥𝑘. In visual terms,𝐴 is made of clumps of consecutive integers
separated by large empty gaps, each containing a single survivor𝑥𝑘.
Step 2: 𝐴∪{ 0} is a basis of order 2.We must show every natural number𝑛 can be
written as𝑎+𝑏with𝑎,𝑏∈𝐴∪{0}:
•If𝑛∉𝑍 𝑘 for any𝑘, then𝑛∈𝐴and we use𝑛+0=𝑛.
• If 𝑛∈𝑍 𝑘 and 𝑛 lies in the lower half of𝑍𝑘, we use⌊𝑛/2⌋+⌈𝑛/ 2⌉. Because𝑛 is small
enough, neither half lands in𝑍𝑘, and both are large enough to avoid the previous zone
𝑍𝑘−1.
• If𝑛∈𝑍 𝑘 and 𝑛 lies in the upper half, we use the oasis:𝑛=𝑥 𝑘+(𝑛−𝑥 𝑘). The difference
𝑛−𝑥 𝑘 is small enough that it falls safely before the forbidden zone𝑍𝑘.
Step 3: No syndetic partition exists.Suppose 𝐴=𝐴 1⊔𝐴 2. Consider a target sum
𝑚∈[ 11𝑃𝑘, 11𝑃𝑘+𝑘] . To write𝑚=𝑢+𝑣 with𝑢,𝑣∈𝐴 , the algebra forces the larger operand
𝑣 to land inside the forbidden range[ 11
2 𝑃𝑘, 11𝑃𝑘+𝑘] . But the only element of𝐴 in this range
is𝑥 𝑘. Therefore, representing any sum in[11𝑃𝑘,11𝑃 𝑘+𝑘]requires𝑥 𝑘.
By the pigeonhole principle,𝑥𝑘 belongs to exactly one partition component, say𝐴1. Then
𝐴1+𝐴 1 can cover the interval[11𝑃𝑘, 11𝑃𝑘+𝑘] using 𝑥𝑘, but𝐴2+𝐴 2 is completely locked out
— it cannot represent any element in that interval. This leaves a gap of length𝑘 in 𝐴2+𝐴 2.
Since𝑘 can be made arbitrarily large, the gaps in one component’s sumset are unbounded,
proving it is impossible to partition𝐴so that both sumsets have bounded gaps.□
The Lean proof for part (ii) is available athttps://github.com/google-deepmind/
alphaproof-nexus-results/blob/main/APNOutputs/ErdosProblems/erdos_12
.parts.ii.lean. Our original communication of both results can be found in the problem
thread on the ErdosProblems site (https://www.erdosproblems.com/forum/thread
/741).
37
Advancing Mathematics Research with AI-Driven Formal Proof Search
Erdős #26, More General Variant
Theorem.Let M(𝑆) denote the set of multiples of a subset𝑆⊆ℕ , and let𝑑(𝑋) denote
the upper asymptotic density of a set𝑋. There exists a sequence𝐴 : ℕ→ℕ satisfying˝
𝑖∈ℕ 1/𝐴(𝑖)=∞, such that for𝜖=1/4and for all𝑘≥1, we have 𝑑(M(𝐴+𝑘))<1−𝜖.
Proof.We construct the sequence iteratively in finite blocks and show that for any arbitrary
shift𝑘, we can bound the upper density of the shifted sequence by analyzing three distinct
cases, the third case relying on the construction being similar to the simple counterexample
of Ruzsa which resolved the original question Erdős #26.
Let(𝑞𝑗)∞
𝑗=1 be a strictly increasing sequence of primes satisfying𝑞1 ≥ 29(chosen large
enough to cause small enough density in the infinite tail of the sequence). We define a
strictly increasing sequence of indices (or “jumps”)(𝐽𝑚)∞
𝑚=0 recursively, starting with𝐽0 = 0.
Suppose 𝐽𝑚 has been defined, and the sequence𝐴(𝑖) has been constructed for all𝑖 < 𝐽𝑚. We
define the parameters for the𝑚-th block as follows.
First, define the step size𝑃𝑚 = ˛ 10𝐽𝑚
𝑗=1 𝑞𝑗. Next, by the Chinese Remainder Theorem, we can
choose a base size𝑅𝑚 satisfying the following system of congruences
𝑅𝑚≡−𝑗(mod𝑞 𝑗)for1≤𝑗≤10𝐽 𝑚
as well as the strict monotonicity condition𝑅𝑚 > 𝐴(𝐽𝑚− 1) (where we set𝐴(− 1)= 0), by
adding enough multiples of𝑃𝑚.
With 𝑅𝑚 and 𝑃𝑚 fixed, the series ˝∞
𝑥=1
1
𝑅𝑚+𝑥𝑃𝑚
diverges. Thus, we can compute a block
length𝐿 𝑚≥1such that the partial sum satisfies:
0.1≤
𝐿𝑚∑︁
𝑥=1
1
𝑅𝑚+𝑥𝑃 𝑚
≤0.2
We then set𝐽𝑚+1 =𝐽 𝑚+𝐿 𝑚. Now that the bounds of the block are properly defined, for
indices𝑖∈[𝐽 𝑚,𝐽 𝑚+1), we set:
𝐴(𝑖)=𝑅 𝑚+(𝑖−𝐽 𝑚+1)𝑃 𝑚
Since each block contributes at least0.1to the total harmonic sum, the overall sum˝ 1/𝐴(𝑖)
diverges. Pick an arbitrary shift𝑘≥ 1; we must now show that𝑑(M(𝐴+𝑘)) stays bounded
below3/4. Let𝑚 0 be the unique integer satisfying:
10𝐽𝑚0≤𝑘 <10𝐽 𝑚0+1
We partition the shifted sequence𝐴+𝑘 into three regimes and bound the upper density of
the multiples generated by each:
• (Case 1:𝑖 < 𝐽𝑚0) The upper density of the multiples generated by this finite set is
bounded by the sum of their reciprocals. Because𝐴(𝑖)> 0, we have𝐴(𝑖)+𝑘 > 𝑘 ,
yielding:
𝑑(M({𝐴(𝑖)+𝑘|𝑖 < 𝐽 𝑚0}))≤
𝐽𝑚0−1∑︁
𝑖=0
1
𝐴(𝑖)+𝑘 <
𝐽𝑚0−1∑︁
𝑖=0
1
𝑘 = 𝐽𝑚0
𝑘 ≤0.1
38
Advancing Mathematics Research with AI-Driven Formal Proof Search
• (Case 2:𝐽𝑚0≤𝑖 < 𝐽𝑚0+1) Shifting by a positive𝑘 strictly decreases the reciprocals, so
the upper density of the multiples from this critical block satisfies:
𝑑(M({𝐴(𝑖)+𝑘|𝐽 𝑚0≤𝑖 < 𝐽𝑚0+1}))≤
𝐽𝑚0+1−1∑︁
𝑖=𝐽𝑚0
1
𝐴(𝑖)+𝑘 <
𝐽𝑚0+1−1∑︁
𝑖=𝐽𝑚0
1
𝐴(𝑖) ≤0.2
• (Case 3:𝑖≥𝐽 𝑚0+1) Consider any element𝐴(𝑖) where𝑖 belongs to some block𝑚≥𝑚 0+1,
meaning10𝐽 𝑚≥10𝐽 𝑚0+1 > 𝑘. Recall the construction of the𝑚-th block:
𝐴(𝑖)+𝑘=(𝑅 𝑚+𝑘)+(𝑖−𝐽 𝑚+1)𝑃 𝑚
Because10 𝐽𝑚 ≥𝑘 , we have𝑞𝑘 |𝑃 𝑚. By construction, we also have𝑞𝑘 | (𝑅𝑚+𝑘) .
Consequently,𝑞𝑘|(𝐴(𝑖)+𝑘) for every element in this infinite tail. The set of multiples
generated by Case 3 is therefore entirely contained within the multiples of the prime
𝑞𝑘. Expressing this with the upper density notation:
𝑑(M({𝐴(𝑖)+𝑘|𝑖≥𝐽 𝑚0+1}))≤ 𝑑(M({𝑞 𝑘}))= 1
𝑞𝑘
≤ 1
29
By the union bound, the total upper density of the multiples of𝐴+𝑘is bounded above by:
0.1+0.2+ 1
29≈0.334< 3
4 =1−𝜖.
□
This problem is a more general variant to the original question stating that “For all𝐴⊆ℕ ,
does there exist𝑘≥ 1such that almost all integers have a divisor of the form𝑎+𝑘 for
some 𝑎∈𝐴 ?”. A simple counterexample to this question can be produced using the Chinese
Remainder Theorem. In the more general variant we resolve, note the Chinese Remainder
Theorem is still used to construct a counterexample, but with additional constraints to
make the upper density of𝐴+𝑘 small, for all𝑘. We originally communicated the result in
https://www.erdosproblems.com/forum/thread/26 , and share the Lean proof at
https://github.com/google-deepmind/alphaproof-nexus-results/blob/main
/APNOutputs/ErdosProblems/erdos_26.variants.tenenbaum.lean.
Erdős #846
Theorem. Let𝐴⊂ℝ 2 be an infinite set for which there exists some𝜖 >0such that in any
subset of𝐴of size𝑛there are always at least𝜖𝑛with no three on a line.
Is it true that𝐴is the union of a finite number of sets where no three are on a line?
Proof.We will show that there exists an infinite set𝐴⊂ℝ 2 for which any𝑛-element subset
contains at least𝑛/2points with no three on a line, but𝐴 is not the union of a finite number
of sets where no three are on a line.
Let 𝐾∞ be the countably infinite complete graph with vertex set𝑉={𝑥 1,𝑥 2,...} . We
choose the sequence of real numbers(𝑥𝑖)∞
𝑖=1 such that it grows sufficiently fast to avoid
39
Advancing Mathematics Research with AI-Driven Formal Proof Search
any accidental roots of polynomials that will arise in our collinearity condition, by setting
𝑥𝑛 =100 4𝑛
.
We construct our point set𝐴⊂ℝ 2 by mapping each edge𝑒={𝑥 𝑖,𝑥 𝑗} of 𝐾∞ to a point𝑃𝑒
as follows:
𝑃𝑒 =(𝑥 𝑖+𝑥 𝑗,𝑥 2
𝑖+𝑥 𝑖𝑥𝑗+𝑥 2
𝑗)(1)
Let𝐴={𝑃 𝑒|𝑒∈𝐸(𝐾 ∞)}.
Lemma.Three points in 𝐴 are collinear if and only if their corresponding edges form a
triangle in𝐾∞.
Proof of Lemma.First, assume three edges form a triangle in𝐾∞ with vertices𝑎,𝑏,𝑐∈𝑉 .
The corresponding points in𝐴are:
𝑃𝑎𝑏 =(𝑎+𝑏,𝑎 2+𝑎𝑏+𝑏 2)
𝑃𝑏𝑐 =(𝑏+𝑐,𝑏 2+𝑏𝑐+𝑐 2)
𝑃𝑐𝑎 =(𝑐+𝑎,𝑐 2+𝑐𝑎+𝑎 2)
The slope𝑚of the line connecting𝑃𝑎𝑏 and𝑃 𝑏𝑐 is given by:
𝑚= (𝑏2+𝑏𝑐+𝑐 2)−(𝑎 2+𝑎𝑏+𝑏 2)
(𝑏+𝑐)−(𝑎+𝑏) = 𝑐2−𝑎 2+𝑏𝑐−𝑎𝑏
𝑐−𝑎
Factoring the numerator yields:
𝑚= (𝑐−𝑎)(𝑐+𝑎)+𝑏(𝑐−𝑎)
𝑐−𝑎 =𝑎+𝑏+𝑐
By symmetry, the slope of the line connecting𝑃𝑏𝑐 and 𝑃𝑐𝑎 is also𝑎+𝑏+𝑐 . Because the slopes
are equal, the three points are collinear.
Conversely, suppose three distinct edges do not form a triangle. We must show their
corresponding points are not collinear. The condition that these points are collinear is
equivalent to the determinant of their3× 3augmented coordinate matrix evaluating to zero.
Because the sequence(𝑥𝑖)∞
𝑖=1 grows quickly enough, any polynomial evaluated on its terms
is strictly dominated by the highest power of its largest variable. By sorting the endpoints
of the three edges, we can group the expanded determinant into three topological cases
based on whether the largest vertex is present in one, two, or all three of the edges. In
every case, because the edges are distinct and do not form a triangle, the coefficient of the
dominant highest-degree term is bounded strictly away from zero. Furthermore, the massive
gap between consecutive terms in the sequence ensures that the lower-degree terms are
strictly bounded and cannot sum to cancel the leading term out. Therefore, the determinant
never evaluates to zero, and no accidental collinearities occur.□
Lemma.Any𝑛-element subset of𝐴contains at least𝑛/2points with no three on a line.
Proof of Lemma.Let𝑆⊂𝐴 be an arbitrary subset of size𝑛. The elements of𝑆 correspond
to a subgraph𝐺𝑆⊂𝐾 ∞ containing exactly𝑛 edges. Every graph with𝑛 edges contains a
bipartite subgraph𝐵𝑆 with at least𝑛/2edges. Because 𝐵𝑆 is bipartite, it contains no odd
cycles and is therefore triangle-free. By the previous lemma, the corresponding points in𝐴
40
Advancing Mathematics Research with AI-Driven Formal Proof Search
contain no collinear triplets. This provides a subset of at least⌈𝑛/2⌉ points with no three on
a line, satisfying the condition with𝜖=1/2.□
To complete the proof of the theorem, assume for contradiction that𝐴 can be covered by
a finite number of sets where no three are on a line; that is,𝐴=—𝑟
𝑘=1𝐴𝑘.
This partition naturally induces an𝑟-coloring on the edges of𝐾∞. By the infinite Ramsey
Theorem, any finite coloring of the edges of the infinite complete graph must contain a
monochromatic triangle. Consequently, there exists some color class𝑘 containing three edges
that form a triangle. By the lemma, these three edges map to three collinear points in𝐴𝑘.
This contradicts the assumption that𝐴𝑘 contains no three collinear points.
Therefore,𝐴cannot be covered by finitely many sets with no three on a line.□
We originally communicated the result inhttps://www.erdosproblems.com/fo
rum/thread/846#post-4447 to the ErdosProblems site, and share the Lean proof at
https://github.com/google-deepmind/alphaproof-nexus-results/blob/ma
in/APNOutputs/ErdosProblems/erdos_846.lean . This result was independently
discovered by an internal model at OpenAI [49]. In the discussion at the ErdosProblems site,
it was pointed out that this result also follows from a projection argument of Reiher, Rödl
and Sales [50].
Erdős #152
Theorem.For a Sidon set𝐴⊂ℕ of size𝑛, let𝐼(𝐴+𝐴) count the isolated elements of the
sumset — those𝑠∈𝐴+𝐴 with 𝑠± 1 ∉𝐴+𝐴 . Define𝑓(𝑛) as the minimum of𝐼(𝐴+𝐴) over all
Sidon sets of size𝑛. Then𝑓(𝑛)≥(𝑛 2−100𝑛−16)/16, so in particular𝑓(𝑛)→∞.
Proof.The proof establishes, for every Sidon set𝐴of size𝑛:
16·𝐼(𝐴+𝐴)+100𝑛+16≥𝑛 2.(★)
Let 𝐷={𝑎−𝑏 : 𝑎,𝑏∈𝐴} denote the difference set and𝑆=𝐴+𝐴 the sumset. For
any set 𝑋⊆ℤ , let 𝑁𝑘(𝑋) :=|𝑥∈𝑋:𝑥+𝑘∈𝑋| be the number of pairs at distance𝑘,
𝑉2(𝑋) :=|𝑥∈𝑋:𝑥±1∈𝑋| be the number of interior points, and𝐼(𝑋) be the isolated points .
Let𝑋⊂ℤ. We will employ the following three facts:
1.𝐼(𝑋)+2𝑁 1(𝑋)=|𝑋|+𝑉 2(𝑋), by partitioning elements by neighbor count.
2. 4𝑁1(𝑋)+𝑁 3(𝑋)≤ 3|𝑋|+ 2𝑁2(𝑋), which follows from writing𝑁𝑘(𝑥)= ˝
𝑥∈ℤ 1𝑋(𝑥) 1𝑋(𝑥+
𝑘) and a pointwise check of the indicator function1𝑋 across all4-point windows
(𝑥,𝑥+ 1,𝑥+ 2,𝑥+ 3); that is, summing the local inequality1𝑋(𝑥)+ 1𝑋(𝑥+ 1)+ 1𝑋(𝑥+
2)+ 1𝑋(𝑥) 1𝑋(𝑥+ 2)+ 1𝑋(𝑥+ 1)1𝑋(𝑥+ 3)≥ 1𝑋(𝑥) 1𝑋(𝑥+ 1)+ 21𝑋(𝑥+ 1)1𝑋(𝑥+ 2)+
1𝑋(𝑥+2)1 𝑋(𝑥+3)+1 𝑋(𝑥)1𝑋(𝑥+3)and then summing over all𝑥∈ℤ.
3. 2𝑁2(𝑋)≤𝑁 3(𝑋)+ 2𝑉2(𝑋)+ 2𝐼(𝑋) . Consider each pair(𝑥,𝑥+ 2)∈𝑋 2 and we proceed
by cases on𝑥+ 1. Let𝐺={𝑥∈𝑋|𝑥+ 1 ∉𝑋∧𝑥+ 2∈𝑋} . If𝑥+ 1∈𝑋 , then the pair is
counted exactly by𝑉2, so𝑁 2(𝑋)=𝑉 2(𝑋)+|𝐺|. If𝑥+1∉𝑋, then
•If𝑥−1∈𝑋, then(𝑥−1,𝑥+2)is a pair counted in𝑁 3(𝑋).
•If𝑥+3∈𝑋, then(𝑥,𝑥+3)is a pair counted in𝑁 3(𝑋).
41
Advancing Mathematics Research with AI-Driven Formal Proof Search
• If 𝑥− 1 ∉𝑋 , then𝑥 is an isolated point in𝐼(𝑋) , and if𝑥+ 3 ∉𝑋 , then𝑥+ 2is an
isolated point in𝐼(𝑋).
Since each𝑁3 pair can be counted by two different gaps, while isolated points are
distinct in this construction, we have2|𝐺|≤𝑁3(𝑋)+2𝐼(𝑋).
Next, for each𝑘≥ 1, count quadruples(𝑎,𝑏,𝑐,𝑑)∈𝐴 4 with 𝑎+𝑏+𝑘=𝑐+𝑑 . Rewriting as
𝑎−𝑐=𝑑−𝑏−𝑘 and partitioning by𝛿=𝑎−𝑐 yields the following two quadruple transfer
bounds:
1. The cases𝛿= 0and 𝛿=−𝑘 each contribute≤|𝐴| (one coordinate determines the rest).
For any𝛿∉{ 0,−𝑘} , the Sidon property ensures that there is at most one pair(𝑎,𝑐)
with 𝑎−𝑐=𝛿 and at most one pair(𝑑,𝑏) with 𝑑−𝑏=𝛿+𝑘 . Consequently, each gap of
size𝑘in𝐷identifies exactly one quadruple. Thus|quad 𝑘|≤𝑁 𝑘(𝐷)+2𝑛.
2. Each "good" element𝑠∈𝑆 with 𝑠+𝑘∈𝑆 (excluding≤ 2𝑛 doubles of the form2𝑎)
produces≥4quadruples, giving4𝑁 𝑘(𝑆)≤|quad 𝑘|+8𝑛.
Combining these bounds shows that𝑁𝑘(𝐷) and 𝑁𝑘(𝑆) are related up to𝑂(𝑛) error. Apply-
ing fact (2) to𝐷=𝐴−𝐴gives
4𝑁1(𝐷)+𝑁 3(𝐷)≤3|𝐷|+2𝑁 2(𝐷)
and then substitute the above two quadruple transfer bounds for𝑘= 1, 2, 3and collecting
all𝑂(𝑛)terms gives
16𝑁1(𝑆)+4𝑁 3(𝑆)≤3|𝐷|+8𝑁 2(𝑆)+100𝑛
Then, using fact (3) on𝑆we obtain
16𝑁1(𝑆)+4𝑁 3(𝑆)≤3|𝐷|+(4𝑁 3(𝑆)+8𝑉 2(𝑆)+8𝐼(𝑆))+100𝑛
and notice that the4𝑁3(𝑆)terms cancel. Then applying fact (1) we obtain
(8|𝑆|+8𝑉 2(𝑆)−8𝐼(𝑆))≤3|𝐷|+8𝑉 2(𝑆)+8𝐼(𝑆)+100𝑛
and see that the8𝑉2(𝑆)terms now cancel, leaving
16𝐼(𝑆)+100𝑛≥8|𝑆|−3|𝐷|.
ThestandardSidonestimates |𝑆|≥𝑛 2/2and|𝐷|≤𝑛 2 thengive16 𝐼(𝑆)+ 100𝑛≥ 4𝑛2−3𝑛2 =𝑛 2,
accounting for a boundary correction of+16at zero yields(★).□
We include the Lean proof athttps://github.com/google-deepmind/alphapro
of-nexus-results/blob/main/APNOutputs/ErdosProblems/erdos_152.lean.
OEIS Conjectures
Theorem.(A conjecture of OEIS A051293, 2002) Let𝑎𝑛 denote the number of nonempty
subsets of{1,2,3,...,𝑛}whose elements have an integer average. Then
𝑎𝑛 = 2𝑛+1
𝑛

1+ 1
𝑛+ 3
𝑛2+ 13
𝑛3+ 75
𝑛4+ 541
𝑛5 +𝑜
 1
𝑛5

42
Advancing Mathematics Research with AI-Driven Formal Proof Search
Proof.Asubset 𝑆⊆{ 1, 2,...,𝑛} hasanintegeraverageifandonlyifthesumofitselementsis
divisible by its cardinality|𝑆|. Let𝑁(𝑛,𝑘) denote the number of subsets of size𝑘 whose sum is
divisible by𝑘. We can express the total number of such subsets as𝑎𝑛 = ˝𝑛
𝑘=1𝑁(𝑛,𝑘) To isolate
the condition that𝑘 divides the sum of the elements in𝑆, we utilize the orthogonality of roots
of unity. Let𝜔𝑘,𝑗 =exp

2𝜋𝑖𝑗
𝑘

. By the standard orthogonality relation, the sum1
𝑘
˝𝑘−1
𝑗=0 𝜔𝑁
𝑘,𝑗
equals1if 𝑘 divides 𝑁, and0otherwise. Thus, the indicator function for divisibility by𝑘 is
1
𝑘
˝𝑘−1
𝑗=0 𝜔
˝
𝑠∈𝑆 𝑠
𝑘,𝑗 . Summing this over all 𝑛
𝑘
 subsets of size𝑘yields
𝑁(𝑛,𝑘)= 1
𝑘
𝑘−1∑︁
𝑗=0
∑︁
|𝑆|=𝑘
𝜔
˝
𝑠∈𝑆 𝑠
𝑘,𝑗
We isolate the principal term corresponding to𝑗= 0, which evaluates trivially to1
𝑘
 𝑛
𝑘
. Let
the remainder term be𝑅𝑛,𝑘, defined as
𝑅𝑛,𝑘 = 1
𝑘
𝑘−1∑︁
𝑗=1
∑︁
|𝑆|=𝑘
𝜔
˝
𝑠∈𝑆 𝑠
𝑘,𝑗
Thus,𝑁(𝑛,𝑘)= 1
𝑘
 𝑛
𝑘
+𝑅 𝑛,𝑘. Summing over all possible subset sizes𝑘, we obtain
𝑎𝑛 =
𝑛∑︁
𝑘=1
1
𝑘
𝑛
𝑘

+
𝑛∑︁
𝑘=1
𝑅𝑛,𝑘
Using the well-known identity˝𝑛
𝑘=1
1
𝑘
 𝑛
𝑘
 = ˝𝑛
𝑗=1
2𝑗−1
𝑗 , we separate this into two sums:𝑆𝑛 =
˝𝑛
𝑗=1
2𝑗
𝑗 and the harmonic number𝐻𝑛 = ˝𝑛
𝑗=1
1
𝑗. This yields our fundamental decomposition
𝑎𝑛 =𝑆 𝑛−𝐻 𝑛+
𝑛∑︁
𝑘=1
𝑅𝑛,𝑘
Next, we establish that the sum of the remainders˝𝑛
𝑘=1𝑅𝑛,𝑘 is asymptotically negligible.
Considertheinnersum ˝
|𝑆|=𝑘 𝜔
˝
𝑠∈𝑆 𝑠
𝑘,𝑗 . Thissumisexactlythecoefficientof 𝑧𝑘 inthepolynomial
𝑃𝑛,𝑘,𝑗(𝑧)= ˛𝑛
𝑚=1(1+𝑧𝜔 𝑚
𝑘,𝑗). By standard coefficient bounds, the magnitude of the𝑘-th
coefficient of a polynomial is bounded by its maximum modulus on the unit circle|𝑧|=1:

∑︁
|𝑆|=𝑘
𝜔
˝
𝑠∈𝑆 𝑠
𝑘,𝑗

≤max
|𝑧|=1
𝑛Ö
𝑚=1
|1+𝑧𝜔 𝑚
𝑘,𝑗|
For a fixed𝑘 and 𝑗∈ {1,...,𝑘− 1}, the sequence of roots𝜔𝑚
𝑘,𝑗 is periodic with period
𝐿= 𝑘
gcd(𝑗,𝑘) ≥ 2. The product over a full period𝐿 can be evaluated algebraically: the roots of
𝑋𝐿− 1dictate that ˛ 𝐴+𝐿−1
𝑚=𝐴 (1+𝑧𝜔 𝑚
𝑘,𝑗)= 1−(−𝑧) 𝐿. For any𝑧 on the unit circle, the magnitude
|1−(−𝑧) 𝐿| is strictly bounded by2. When taking the product over all𝑛 terms, we group
them into⌊𝑛/𝐿⌋ full periods, leaving𝑛mod𝐿 residual terms. For|𝑧|= 1, each full period
contributes at most a factor of2, and by the triangle inequality|1+𝑧𝜔 𝑚
𝑘,𝑗|≤ 2, each residual
term also contributes at most a factor of2. Therefore, the total product is bounded by
43
Advancing Mathematics Research with AI-Driven Formal Proof Search
2⌊𝑛/𝐿⌋+(𝑛mod𝐿) . Because𝐿≥ 2, we have⌊𝑛/𝐿⌋+(𝑛mod𝐿)≤ 𝑛
2+ 1. Thus, for any𝑧 on the
unit circle, we have
|𝑃𝑛,𝑘,𝑗(𝑧)|≤2
𝑛
2+1 =2·2 𝑛/2
Consequently, the magnitude of the coefficient is bounded by2· 2𝑛/2. Applying this to our
remainder definition yields|𝑅𝑛,𝑘|≤ 𝑘−1
𝑘 2· 2𝑛/2≤ 2· 2𝑛/2. Summing over𝑘∈{ 1,...,𝑛} gives
the strict bound 

𝑛∑︁
𝑘=1
𝑅𝑛,𝑘

≤2𝑛2 𝑛/2
We must now evaluate the asymptotics of𝑆𝑛 = ˝𝑛
𝑗=1
2𝑗
𝑗 . We propose the asymptotic approxi-
mation𝑓 𝑛, defined as
𝑓𝑛 = 2𝑛+1
𝑛

1+ 1
𝑛+ 3
𝑛2+ 13
𝑛3+ 75
𝑛4+ 541
𝑛5

= 2𝑛+1𝑃(𝑛)
𝑛6
where 𝑃(𝑛)=𝑛 5+𝑛 4+ 3𝑛3+ 13𝑛2+ 75𝑛+ 541. To demonstrate that𝑓𝑛 is a highly accurate
approximation of𝑆𝑛, we analyze the discrepancy in their consecutive differences. Let𝐸𝑗 be
the discrete derivative error given by
𝐸𝑗 =𝑓 𝑗−𝑓 𝑗−1− 2𝑗
𝑗
By telescoping summation,𝑆𝑛−𝑓 𝑛 =𝑆 1−𝑓 1− ˝𝑛
𝑗=2𝐸𝑗. To bound𝐸𝑗, we expand𝑓𝑗−𝑓 𝑗−1
algebraically to obtain
𝑓𝑗−𝑓 𝑗−1− 2𝑗
𝑗 =
2𝑗 
2𝑃(𝑗)(𝑗−1) 6−𝑃(𝑗−1)𝑗 6−𝑗 5(𝑗−1) 6
𝑗6(𝑗−1) 6
Let 𝐴(𝑥)= 2𝑃(𝑥)(𝑥− 1)6−𝑃(𝑥− 1)𝑥 6−𝑥 5(𝑥− 1)6. Expanding𝐴(𝑥) leaves a polynomial of
strictly degree5:
𝐴(𝑥)=−4683𝑥 5+13586𝑥 4−19540𝑥 3+15356𝑥 2−6342𝑥+1082
In particular, it is easy to show that|𝐴(𝑗)|≤ 100000𝑗5 for 𝑗≥ 2. Substituting this back into
the error term yields
|𝐸𝑗|≤ 100000·2 𝑗
𝑗7
Summing these errors up to𝑛, the sum is dominated by its largest terms, giving˝𝑛
𝑗=2|𝐸𝑗|=
O

2𝑛
𝑛7

. Recall our decomposition𝑎𝑛 =𝑓 𝑛+(𝑆 𝑛−𝑓 𝑛)−𝐻 𝑛+ ˝𝑛
𝑘=1𝑅𝑛,𝑘. To prove the theorem,
it suffices to show that the combined error terms are𝑜

2𝑛+1
𝑛6

:
1.𝑆 𝑛−𝑓 𝑛 =O

2𝑛
𝑛7

=𝑜

2𝑛+1
𝑛6

.
2.𝐻 𝑛∼ln𝑛=𝑜

2𝑛+1
𝑛6

.
3. ˝𝑅𝑛,𝑘≤2𝑛2 𝑛/2 =𝑜

2𝑛+1
𝑛6

.
44
Advancing Mathematics Research with AI-Driven Formal Proof Search
Since all residual terms are bounded by𝑜

2𝑛+1
𝑛6

, we conclude that
𝑎𝑛 =𝑓 𝑛+𝑜
 2𝑛+1
𝑛6

= 2𝑛+1
𝑛

1+ 1
𝑛+ 3
𝑛2+ 13
𝑛3+ 75
𝑛4+ 541
𝑛5 +𝑜
 1
𝑛5

This establishes the conjectured asymptotic expansion.□
Theorem.(A conjecture of OEIS A228143, 2018) Let𝑠𝑚 = ˝𝑚
𝑘=0
 𝑚
𝑘
 2 𝑚+𝑘
𝑘
 2
be the sequence
A005259. Let𝑎𝑛 denote the determinant of the(𝑛+ 1)×(𝑛+ 1) Hankel-type matrix whose
(𝑖, 𝑗)-entry is𝑠𝑖+𝑗 for all𝑖, 𝑗= 0,...,𝑛 . Let 𝐴(𝑥)= ˝∞
𝑛=0𝑎𝑛𝑥𝑛 = 1+ 48𝑥+ 161856𝑥2+...
denote the ordinary generating function of𝑎𝑛. Then𝐴(𝑥/3) 1/8 has integer coefficients.
Proof.We proceed in three main stages: analyzing the matrix entries modulo3, analyzing
them modulo4, and using the resulting divisibility properties of the determinant𝑎𝑛 to
construct the required eighth root as a formal power series over the integers.
First, we determine the residues of𝑠𝑚 modulo3. By writing 𝑘 in base3, Kummer’s
Theorem dictates that the highest power of3dividing 2𝑘
𝑘
 equals the number of carries when
evaluating 𝑘+𝑘 in base3. If 𝑘 contains the digit2, a carry occurs, so 2𝑘
𝑘
≡ 0(mod 3).
Alternatively, if𝑘 consists only of the digits0and1, there are no carries. Applying Lucas’s
Theorem digit-by-digit to 2𝑘
𝑘
 yields a product of terms 0
0
 = 1and  2
1
 = 2≡− 1(mod 3).
Thus,  2𝑘
𝑘
≡(− 1)𝑐 (mod 3), where𝑐 is the number of1s in the base-3 representation of𝑘.
Since𝑐shares the same parity as𝑘, we obtain 2𝑘
𝑘
≡(−1) 𝑘 (mod 3).
We can rewrite the squared product of binomial coefficients as:
𝑚
𝑘
𝑚+𝑘
𝑘
 2
=
𝑚+𝑘
2𝑘
 22𝑘
𝑘
 2
When  2𝑘
𝑘
 . 0(mod 3), the base-3 digits of2𝑘 are strictly0s and2s. Applying Lucas’s
Theorem to 𝑚+𝑘
2𝑘
, each digit of the evaluation takes the form 𝑑𝑖
0
 = 1or  𝑑𝑖
2
∈{ 0, 1}. Thus,
 𝑚+𝑘
2𝑘
≡ 0 or 1(mod 3). Since values in{0, 1} are invariant under squaring, 𝑚+𝑘
2𝑘
 2
≡  𝑚+𝑘
2𝑘

(mod 3). Furthermore, since  2𝑘
𝑘
 ∈ {0,(− 1)𝑘} (mod3), squaring it absorbs the parity:
 2𝑘
𝑘
 2
≡(−1) 𝑘 2𝑘
𝑘
 (mod 3). Combining these pieces, we find that for all𝑚and𝑘:
𝑚
𝑘
𝑚+𝑘
𝑘
 2
≡(−1) 𝑘
𝑚+𝑘
2𝑘
 2𝑘
𝑘

≡(−1) 𝑘
𝑚
𝑘
𝑚+𝑘
𝑘

(mod 3)
Summing this equivalence over𝑘= 0,...,𝑚 yields 𝑠𝑚≡ ˝𝑚
𝑘=0(−1)𝑘 𝑚
𝑘
 𝑚+𝑘
𝑘
 (mod 3). By
a standard alternating binomial sum identity,˝𝑚
𝑘=0(−1)𝑘 𝑚
𝑘
 𝑚+𝑘
𝑘
 =(− 1)𝑚. Consequently,
𝑠𝑚≡(−1) 𝑚 (mod 3).
Using this congruence, we apply row operations to the matrix𝑀(𝑛) to establish that3𝑛|𝑎 𝑛.
Let 𝑃𝑛 be the lower-triangular matrix with ones on the main diagonal,𝑃𝑖,0 =−(− 1)𝑖 for𝑖≥ 1,
and zeros elsewhere. The matrix product𝑃𝑛𝑀(𝑛) replaces each row𝑖≥ 1with the 𝑖-th row
45
Advancing Mathematics Research with AI-Driven Formal Proof Search
minus(−1) 𝑖 times the0-th row. Visually, the modified matrix takes the form:
𝑃𝑛𝑀(𝑛) =

𝑠0 𝑠1 𝑠2 ···𝑠 𝑛
𝑠1+𝑠 0 𝑠2+𝑠 1 𝑠3+𝑠 2 ···𝑠 𝑛+1+𝑠 𝑛
𝑠2−𝑠 0 𝑠3−𝑠 1 𝑠4−𝑠 2 ···𝑠 𝑛+2−𝑠 𝑛
... ... ... ... ...
𝑠𝑛−(−1) 𝑛𝑠0 𝑠𝑛+1−(−1) 𝑛𝑠1 𝑠𝑛+2−(−1) 𝑛𝑠2 ···𝑠 2𝑛−(−1) 𝑛𝑠𝑛

The new(𝑖, 𝑗)-entry for𝑖≥ 1is 𝑠𝑖+𝑗−(− 1)𝑖𝑠𝑗. By our previous congruence,𝑠𝑖+𝑗−(− 1)𝑖𝑠𝑗≡
(−1)𝑖+𝑗−(− 1)𝑖(−1)𝑗≡ 0(mod 3). Thus, every entry in rows1through𝑛 of the new matrix
is divisible by3. Factoring a3out of each of these 𝑛 rows gives a factor of3𝑛. Because
det(𝑃𝑛)=1, we conclude that3 𝑛|det(𝑀 (𝑛))=𝑎 𝑛.
Second, we analyze𝑠𝑚 modulo4. For any 𝑘≥ 1, the product 𝑚
𝑘
 𝑚+𝑘
𝑘
 is always even,
which implies its square is divisible by4. Thus,
 𝑚
𝑘
 𝑚+𝑘
𝑘
 2
≡ 0(mod 4) for all𝑘≥ 1. The
𝑘=0term evaluates to1, yielding𝑠 𝑚≡1(mod 4)for all𝑚.
We apply a similar matrix transformation to establish divisibility by4𝑛. Let 𝑃′
𝑛 be the
lower-triangular matrix with ones on the diagonal,𝑃′
𝑖,0 =−1for𝑖≥1, and zeros elsewhere.
The product𝑃′
𝑛𝑀(𝑛) subtracts the0-th row from every subsequent row𝑖≥1:
𝑃′
𝑛𝑀(𝑛) =

𝑠0 𝑠1 ···𝑠 𝑛
𝑠1−𝑠 0 𝑠2−𝑠 1 ···𝑠 𝑛+1−𝑠 𝑛
𝑠2−𝑠 0 𝑠3−𝑠 1 ···𝑠 𝑛+2−𝑠 𝑛
... ... ... ...

For𝑖≥ 1, the(𝑖, 𝑗)-entry becomes𝑠𝑖+𝑗−𝑠 𝑗. Since𝑠𝑚≡ 1(mod 4) for all𝑚, this difference
evaluates to1− 1≡ 0(mod 4). Factoring4out of the 𝑛 modified rows shows that4𝑛|
det(𝑀(𝑛))=𝑎 𝑛.
Now we combine these divisibility properties. We explicitly compute𝑎1 =48. For𝑛≥1,
we know4𝑛|𝑎 𝑛, and since4𝑛≥ 16for 𝑛≥ 2, it follows that16|𝑎 𝑛 for all𝑛≥ 1(as16 | 48
for𝑛= 1). Because16and3 𝑛 are coprime, their respective divisibilities imply16· 3𝑛|𝑎 𝑛 for
all𝑛≥1.
We consider the scaled generating function𝐴(𝑥/ 3)= ˝∞
𝑛=0
𝑎𝑛
3𝑛𝑥𝑛. Let𝑏𝑛 =𝑎 𝑛/3𝑛 denote
the coefficients of this series. Since𝑎0 = 1, we have𝑏0 = 1. For𝑛≥ 1, our divisibility result
yields16 |𝑏 𝑛. Therefore, we can write𝐴(𝑥/ 3)= 1+ 16𝑌(𝑥) , where𝑌(𝑥)= ˝∞
𝑛=1𝑦𝑛𝑥𝑛 is a
formal power series with integer coefficients and zero constant term (𝑌(0)=0).
Finally, we construct the eighth root𝐶(𝑥)=𝐴(𝑥/ 3)1/8∈ℤ⟦𝑥⟧ . We seek a series of the
form 𝐶(𝑥)= 1+ 2𝑋(𝑥) where 𝑋(𝑥)∈ℤ⟦𝑥⟧ has no constant term. Expanding the eighth
power yields
(1+2𝑋(𝑥)) 8 =1+16𝑋(𝑥)+112𝑋(𝑥) 2+448𝑋(𝑥) 3+1120𝑋(𝑥) 4
+1792𝑋(𝑥) 5+1792𝑋(𝑥) 6+1024𝑋(𝑥) 7+256𝑋(𝑥) 8
Factoring out16from the higher degree terms, we define the polynomial
𝑃(𝑋)=7𝑋 2+28𝑋 3+70𝑋 4+112𝑋 5+112𝑋 6+64𝑋 7+16𝑋 8
46
Advancing Mathematics Research with AI-Driven Formal Proof Search
Thus,(1+ 2𝑋(𝑥)) 8 = 1+ 16(𝑋(𝑥)+𝑃(𝑋(𝑥))) . To satisfy𝐶(𝑥) 8 =𝐴(𝑥/ 3), we must solve the
equation1+16(𝑋(𝑥)+𝑃(𝑋(𝑥)))=1+16𝑌(𝑥), which simplifies to𝑋(𝑥)+𝑃(𝑋(𝑥))=𝑌(𝑥).
We determine the coefficients𝑥𝑛 of𝑋(𝑥)= ˝∞
𝑛=1𝑥𝑛𝑥𝑛 inductively. We set𝑥0 = 0. For the
inductive step, the coefficient of𝑥𝑛+1 in the equation is
𝑥𝑛+1+[𝑥 𝑛+1]𝑃(𝑋(𝑥))=𝑦 𝑛+1
Because every term in𝑃(𝑋) has degree at least2, and𝑋(𝑥) has no constant term, the𝑥𝑛+1
coefficient of𝑃(𝑋(𝑥)) depends only on the terms𝑥1,...,𝑥 𝑛. Therefore, we can uniquely solve
for the integers𝑥𝑛+1 as
𝑥𝑛+1 =𝑦 𝑛+1−[𝑥 𝑛+1]𝑃
 𝑛∑︁
𝑘=1
𝑥𝑘𝑥𝑘
!
This well-defined recurrence provides an integer sequence(𝑥𝑛)𝑛≥1 giving a formal power
series 𝑋(𝑥) ∈ℤ⟦𝑥⟧ that satisfies𝑋(𝑥)+𝑃(𝑋(𝑥))=𝑌(𝑥) . Substituting this back into our
expansion yields(1+ 2𝑋(𝑥)) 8 = 1+ 16𝑌(𝑥)=𝐴(𝑥/ 3). Setting𝐶(𝑥)= 1+ 2𝑋(𝑥) , we have
established the existence of the desired integer power series𝐶(𝑥)=𝐴(𝑥/3)1/8.□
These OEIS problems were added as conjectures in 2022 (https://oeis.org/A0512
93) and 2018 (https://oeis.org/A228143). Though neither problem has likely received
much attention, the ability to provide a guarantee on the correctness of the statement that
an expert conjectured serves value. For example, it appears that a good part of the work is
done in identifying the asymptotic formula to be conjectured in OEIS A051293. In this case,
ensuring the formula holds with a rigorous proof is a matter of validating intuition without
carrying out potentially tedious proof steps, which our agent can handle. The Lean proofs
for the two problems can be found athttps://github.com/google-deepmind/alphap
roof-nexus-results/blob/main/APNOutputs/OEIS.
A variant of the Graph Reconstruction Conjecture
The Kelly-Ulam graph reconstruction program aims to recover a graph from its deck of
one-vertex-deleted subgraphs [62, 36]. A standard bipartite version was formulated by
Bondy and Hemminger as the problem of showing that bipartite graphs are reconstructible
[10]. The following theorem proves a structured incidence-deletion analogue under strong
type-distinguishability assumptions.
TerminologyLet Ω=𝐿⊔𝑅 be a finite vertex set with a partition into the disjoint parts
𝐿,𝑅⊆Ω . A graph𝐾 is bipartite with respect to(𝐿,𝑅) if every edge of𝐾 has one endpoint in
𝐿 and one endpoint in𝑅. We say𝐾 is2-connected if 𝐾 is connected and, for every vertex𝑣,
the induced graph onΩ\{𝑣} is connected. For a graph𝐾 and a vertex𝑣, write𝐾\ inc𝑣 for
the graph obtained from𝐾 by deleting all edges incident to𝑣, while leaving the vertex set
unchanged. Thus
𝐸(𝐾\ inc𝑣)={𝑥𝑦∈𝐸(𝐾):𝑥≠𝑣, 𝑦≠𝑣}.
Abipartiteisomorphism 𝐾 𝐵 𝐾′ isagraphisomorphismwhoseunderlyingbijectionpreserves
both parts𝐿and𝑅. The bipartite deck is the multiset
D𝐵(𝐾):={{[𝐾\ inc𝑣]𝐵 :𝑣∈Ω}},
47
Advancing Mathematics Research with AI-Driven Formal Proof Search
where[·]𝐵 denotes bipartite-isomorphism class. Let𝑁𝐾(𝑥) be the neighbor set of𝑥 in 𝐾. The
degree profile and type of𝑥are
𝑃𝐾(𝑥):={{deg 𝐾(𝑦):𝑦∈𝑁 𝐾(𝑥)}}, 𝜏 𝐾(𝑥):=(deg 𝐾(𝑥),𝑃 𝐾(𝑥)).
The type profile of𝑢is the multiset of the types of its neighbors:
𝑇𝐾(𝑢):={{𝜏 𝐾(𝑥):𝑥∈𝑁 𝐾(𝑢)}}.
Finally, for a type𝑡=(𝑑,𝑀)∈ℕ×Multiset(ℕ)and𝑎∈ℕ, define
𝐹𝑎(𝑡):=(max(𝑑−1,0),𝑀\{𝑎}),
where 𝑀\{𝑎} means deletion of one occurrence of𝑎 from the multiset𝑀. In the applications
below,𝐹𝑎 is applied to neighbor-types, whose first coordinate is positive, somax(𝑑− 1, 0)=
𝑑−1there. We write# 𝑡𝑀for the multiplicity of𝑡in a multiset𝑀.
Theorem(Weak bipartite graph reconstruction) Let𝐺 and 𝐻 be finite simple graphs on
the same finite vertex setΩ, both bipartite with respect to the same partsΩ=𝐿⊔𝑅 and
|Ω|≥ 3. Assume that𝐺 is 2-connected and all vertex types of𝐺 are pairwise distinct, that is,
𝜏𝐺(𝑥)≠𝜏 𝐺(𝑦)if𝑥≠𝑦. IfD 𝐵(𝐺)=D 𝐵(𝐻), then𝐺and𝐻are bipartite-isomorphic.
Proof.Write 𝑛= |Ω| and𝑒(𝐾)= |𝐸(𝐾)|. Since bipartite isomorphisms preserve edge counts,
the deck determines the multiset
{{𝑒(𝐾\ inc𝑣):𝑣∈Ω}}.
For every vertex𝑣,
𝑒(𝐾\ inc𝑣)+deg 𝐾(𝑣)=𝑒(𝐾),(1)
because𝐾\ inc𝑣removes exactly the edges incident to𝑣. Also,
∑︁
𝑣∈Ω
𝑒(𝐾\ inc𝑣)=(𝑛−2)𝑒(𝐾),(2)
because each edge of𝐾 remains in precisely the cards indexed by the𝑛− 2vertices not
incident to that edge. Since𝑛≥ 3, equation (2) shows that the deck determines𝑒(𝐾) .
Applying this to the equal decks of𝐺and𝐻gives
𝑒(𝐺)=𝑒(𝐻),(3)
and then equation (1) shows that the degree multisets of𝐺and𝐻are equal.
Equality of the two decks also gives a bijection𝑓 : Ω→Ω such that, for every𝑣∈Ω ,
there is a bipartite isomorphism
𝜙𝑣 :𝐺\ inc𝑣 𝐵 𝐻\ inc 𝑓(𝑣).(4)
For this matched pair of cards, edge counts are equal. Combining this with (1) and (3) yields
deg𝐺(𝑣)=deg 𝐻(𝑓(𝑣))(5)
for every𝑣.
48
Advancing Mathematics Research with AI-Driven Formal Proof Search
Next,𝐺 has minimum degree at least2. Indeed, if a vertex had degree0, then𝐺 would
not be connected; if a vertex𝑥 had the unique neighbor𝑦, then the induced graph onΩ\{𝑦}
would contain the isolated vertex𝑥, contradicting2-connectivity. Since the degree multisets
of𝐺and𝐻are equal,𝐻also has minimum degree at least2.
Therefore, in any graph𝐾 with minimum degree at least2, the card𝐾\ inc𝑣 has a unique
isolated vertex, namely𝑣. Indeed, the vertex𝑣 is isolated because all its incident edges have
been removed. On the other hand, if𝑥≠𝑣 , then𝑥 has at least two neighbors in𝐾, at most
one of which is𝑣; hence𝑥has a neighbor𝑦≠𝑣, and the edge𝑥𝑦remains in𝐾\ inc𝑣.
Applying this uniqueness to (4), the isomorphism𝜙𝑣 sends the unique isolated vertex of
𝐺\ inc𝑣to the unique isolated vertex of𝐻\inc 𝑓(𝑣). Hence
𝜙𝑣(𝑣)=𝑓(𝑣).(6)
Since𝜙 𝑣 preserves𝐿and𝑅, (6) implies that𝑓preserves the two parts:
𝑣∈𝐿⇐⇒𝑓(𝑣)∈𝐿, 𝑣∈𝑅⇐⇒𝑓(𝑣)∈𝑅.(7)
We now prove that𝑓 preserves vertex types. It remains, in view of (5), to compare degree
profiles. For a graph𝐾and vertex𝑣, put
𝐴𝐾(𝑘):=#{𝑥∈Ω: deg 𝐾(𝑥)=𝑘},
𝐵𝐾,𝑣(𝑘):=#{𝑥∈Ω: deg 𝐾\inc𝑣(𝑥)=𝑘},
and
𝐶𝐾,𝑣(𝑘):=#{𝑥∈𝑁 𝐾(𝑣): deg 𝐾(𝑥)=𝑘}.
Counting vertices of degree𝑘 before and after deleting the incidence set of𝑣 gives, for every
𝑘≥0,
𝐶𝐾,𝑣(𝑘+1)+𝐴 𝐾(𝑘)+1 𝑘=0 =𝐶 𝐾,𝑣(𝑘)+𝐵 𝐾,𝑣(𝑘)+1 deg𝐾(𝑣)=𝑘.(8)
Indeed, in𝐾\ inc𝑣, every non-neighbor of𝑣 keeps its degree, while every neighbor of𝑣 has
its degree lowered by1. Hence the vertices of degree𝑘 in 𝐾\ inc 𝑣 are precisely the old
non-neighbors of degree𝑘, the old neighbors of degree𝑘+ 1, and additionally𝑣 itself if𝑘= 0.
Therefore
𝐵𝐾,𝑣(𝑘)=𝐴 𝐾(𝑘)−𝐶 𝐾,𝑣(𝑘)−1 deg𝐾(𝑣)=𝑘+𝐶 𝐾,𝑣(𝑘+1)+1 𝑘=0.
Since the global degree multisets are equal,𝐴𝐺(𝑘)=𝐴 𝐻(𝑘). Since 𝜙𝑣 is an isomorphism
between the matched cards,𝐵𝐺,𝑣(𝑘)=𝐵 𝐻,𝑓(𝑣)(𝑘). By (5), the final indicator in (8) is also
the same for𝐺 and 𝐻. Finally,𝐶𝐾,𝑣(0)= 0, because a neighbor always has positive degree.
Induction on𝑘in (8) gives
𝐶𝐺,𝑣(𝑘)=𝐶 𝐻,𝑓(𝑣)(𝑘) (𝑘≥0).
Thus
𝑃𝐺(𝑣)=𝑃 𝐻(𝑓(𝑣)),
and together with (5) this proves
𝜏𝐺(𝑣)=𝜏 𝐻(𝑓(𝑣))(9)
49
Advancing Mathematics Research with AI-Driven Formal Proof Search
for every𝑣∈Ω. We next prove equality of type profiles:
𝑇𝐺(𝑢)=𝑇 𝐻(𝑓(𝑢))(10)
for every𝑢. Fix𝑢. If𝑢∈𝐿 , take𝑆=𝑅 , otherwise take𝑆=𝐿 (thus𝑆 is the opposite side from
𝑢). By (7) and (9), the multisets of global types on𝑆agree:
{{𝜏𝐺(𝑥):𝑥∈𝑆}}={{𝜏 𝐻(𝑥):𝑥∈𝑆}}.(11)
The card isomorphism𝜙𝑢 also preserves𝑆, and therefore the multisets of local types on𝑆
agree:
{{𝜏𝐺\inc𝑢(𝑥):𝑥∈𝑆}}={{𝜏 𝐻\inc𝑓(𝑢)(𝑥):𝑥∈𝑆}}.(12)
For𝑥∈𝑆, bipartiteness gives the local-type formula
𝜏𝐺\inc𝑢(𝑥)=
(
𝐹deg𝐺(𝑢)(𝜏𝐺(𝑥)),if𝑥∈𝑁 𝐺(𝑢),
𝜏𝐺(𝑥),if𝑥∉𝑁 𝐺(𝑢).
(13)
Indeed, if𝑥 is adjacent to𝑢, then deleting the incidence set of𝑢removes the edge𝑢𝑥, lowering
deg𝐺(𝑥) by one and deleting one occurrence ofdeg𝐺(𝑢) from the degree profile of𝑥. If𝑥 is
not adjacent to𝑢, then any neighbor of𝑥 lies on the same side of the bipartition as𝑢, and
therefore cannot be adjacent to𝑢; hence the type of𝑥 is unchanged. The same formula holds
for𝐻and𝑓(𝑢).
Taking the number of occurrences of an arbitrary type𝑡in (13) gives
#𝑡{{𝜏𝐺\inc𝑢(𝑥):𝑥∈𝑆}}+# 𝑡𝑇𝐺(𝑢)=# 𝑡{{𝜏𝐺(𝑥):𝑥∈𝑆}}+# 𝑡{{𝐹deg𝐺(𝑢)(𝑠):𝑠∈𝑇 𝐺(𝑢)}}.(14)
There is an identical identity for𝐻. The first terms on the two sides of (14) agree by (12),
and the global-type terms agree by (11). Alsodeg𝐺(𝑢)=deg 𝐻(𝑓(𝑢)) by (5). Hence equality
of the type-profile counts can be proved by descending induction on the first coordinate of𝑡.
The base case is that no type in a type profile can have first coordinate at least𝑛, since every
vertex degree is< 𝑛. For the induction step, the only types𝑠 with 𝐹deg𝐺(𝑢)(𝑠)=𝑡 have first
coordinate𝑡1+ 1; moreover every𝑠 occurring in a type profile has positive first coordinate.
Thus the rightmost term in (14) is already equal for𝐺 and 𝐻 by the induction hypothesis,
and subtracting the two versions of (14) yields equality of the number of occurrences of𝑡 in
𝑇𝐺(𝑢)and in𝑇 𝐻(𝑓(𝑢)). This proves (10).
The distinctness of types transfers from𝐺 to 𝐻: if𝜏𝐻(𝑥)=𝜏 𝐻(𝑦), then by applying (9) to
𝑓−1(𝑥)and𝑓 −1(𝑦)we obtain equality of the corresponding𝐺-types, so𝑥=𝑦.
Since types are pairwise distinct, adjacency is determined by type profiles: for every
graph𝐾among𝐺,𝐻and every pair of vertices𝑎,𝑏,
𝐾has edge𝑎𝑏⇐⇒𝜏 𝐾(𝑏)∈𝑇 𝐾(𝑎).(15)
The forward implication is the definition of𝑇𝐾(𝑎). Conversely, if𝜏𝐾(𝑏) occurs in𝑇𝐾(𝑎), then
some neighbor𝑐of𝑎has𝜏 𝐾(𝑐)=𝜏 𝐾(𝑏), and distinctness of types gives𝑐=𝑏.
Finally, for any𝑢,𝑣∈Ω, equations (9), (10), and (15) give
𝐺has edge𝑢𝑣⇐⇒𝜏 𝐺(𝑣)∈𝑇 𝐺(𝑢)⇐⇒𝜏 𝐻(𝑓(𝑣))∈𝑇 𝐻(𝑓(𝑢))⇐⇒𝐻has edge𝑓(𝑢)𝑓(𝑣).
50
Advancing Mathematics Research with AI-Driven Formal Proof Search
Thus 𝑓 is a graph isomorphism𝐺𝐻 . By (7), it preserves the two bipartition parts, so it is a
bipartite isomorphism.□
The Lean proof discovered for this problem is athttps://github.com/google-dee
pmind/alphaproof-nexus-results/blob/main/APNOutputs/AICollaborator/G
raphs/bipartite_graph_reconstruction_conjecture_2.lean.
Log-Concavity of Hilbert Sequences
Pure𝑂-sequences, introduced in the context of Stanley’s work on Hilbert functions of mono-
mial level algebras in the late 1970s, have been studied intensively over the last fifteen years
[57]. They exhibit surprisingly strong positivity phenomena, especially in small codimension
and type. Although pure𝑂-sequences are not log-concave in general, the case of codimension
3 and type 2 remained open for over a decade [9, 68]. The following theorem establishes
log-concavity in precisely this remaining case.
Theorem.Every pure𝑂-sequence of codimension3and type2is log-concave.
Terminology.A monomial𝑥𝑚(0)
0 𝑥𝑚(1)
1 𝑥𝑚(2)
2 in three variables is identified with its exponent
vector𝑚=(𝑚( 0),𝑚( 1),𝑚( 2))∈ℕ 3. We write𝑚′≤𝑚 for coordinate-wise inequality and
|𝑚|=𝑚( 0)+𝑚( 1)+𝑚( 2) for total degree. A finite order idealΓ⊂ℕ 3 is a finite set closed
downward under this order: if𝑛∈Γand𝑚≤𝑛, then𝑚∈Γ.
A monomial𝑚∈Γ is maximal if every𝑛∈Γ with 𝑚≤𝑛 also satisfies𝑛≤𝑚 . The ideal is
pure if all maximal monomials have the same total degree; this common degree is the socle
degree. The type is the number of maximal monomials. The pure𝑂-sequence ofΓis
ℎΓ(𝑑)=#{𝑚∈Γ:|𝑚|=𝑑}.
For a monomial𝑔, we simply writeℎ𝑔(𝑑)= #{𝑢≤𝑔 :|𝑢|=𝑑} . The𝑂-sequence is log-concave
if
ℎΓ(𝑖−1)ℎ Γ(𝑖+1)≤ℎ Γ(𝑖) 2 (0< 𝑖 < 𝑒),
where𝑒is the socle degree ofΓ. We write1𝑃 for the indicator of the condition𝑃.
Proof.Let Γ be a pure order ideal in three variables and suppose that its two maximal
monomials are𝑚1 ≠𝑚 2. Since Γ is pure,|𝑚1|=|𝑚 2|=𝑒 . Every element of a finite order
ideal lies below a maximal element, so
Γ={𝑢:𝑢≤𝑚 1}∪{𝑢:𝑢≤𝑚 2},
After possibly interchanging𝑚1 and𝑚 2, there is a coordinate𝑥∈{0,1,2}such that
𝑚2(𝑥)> 𝑚 1(𝑥), 𝑚 2(𝑦)≤𝑚 1(𝑦) (𝑦≠𝑥).(1)
Indeed, the three integers𝑚1(𝑖)−𝑚 2(𝑖) sum to zero and are not all zero, hence one sign
occurs in a minority position; if necessary we swap the two monomials so that the minority
sign is negative.
Let𝑐=𝑚 1(𝑥)+1, and define
𝑀red(𝑦)=
(
𝑚2(𝑥)−𝑚 1(𝑥)−1, 𝑦=𝑥,
𝑚2(𝑦), 𝑦≠𝑥.
51
Advancing Mathematics Research with AI-Driven Formal Proof Search
Then|𝑀 red|=𝑒−𝑐. For𝑢≤𝑚 2, condition (1) implies
𝑢̸≤𝑚 1 ⇐⇒𝑢(𝑥)≥𝑐.
If 𝑑≥𝑐 , the map𝑢↦→𝑢−𝑐𝑒 𝑥 bijects{𝑢≤𝑚 2 :|𝑢|=𝑑, 𝑢(𝑥)≥𝑐} with{𝑣≤𝑀 red :|𝑣|=𝑑−𝑐} .
If𝑑 < 𝑐, the first set is empty. Hence the𝑂sequence ofΓcan be written as
𝐻(𝑑):=ℎ Γ(𝑑)=ℎ 𝑚1(𝑑)+1 𝑑≥𝑐ℎ𝑀red(𝑑−𝑐).(2)
We need to prove that𝐻(𝑑−1)𝐻(𝑑+1)≤𝐻(𝑑) 2 holds for0< 𝑑 < 𝑒.
For an integer-valued sequence𝐹 : ℕ→ℤ , define the first and scond difference sequences
as
Δ𝐹(0)=𝐹(0),Δ𝐹(𝑑)=𝐹(𝑑)−𝐹(𝑑−1) (𝑑 >0),
Δ2𝐹(0)=Δ𝐹(0),Δ 2𝐹(𝑑)=Δ𝐹(𝑑)−Δ𝐹(𝑑−1) (𝑑 >0).
Wefirstproveanelementarydivisor-countformulaforasinglemonomial. Let 𝑚=(𝛼,𝛽,𝛾)
be a monomial. For𝑝,𝑞∈ℕ, set
𝐿𝑝,𝑞(𝑘)=#{𝑟∈ℕ:𝑟 < 𝑝, 𝑟≤𝑘, 𝑘−𝑟 < 𝑞}.
Thus 𝐿𝑝,𝑞(𝑘) counts the number of pairs(𝑟,𝑠) with0 ≤𝑟 < 𝑝,0 ≤𝑠 < 𝑞, and𝑟+𝑠=𝑘 . A direct
box count gives
ℎ𝑚(𝑡)=
𝑡∑︁
𝑘=0
1𝑡−𝑘<𝛾+1 𝐿𝛼+1,𝛽+1(𝑘).
With the conventionΔ𝐹(0)=𝐹(0), the first-difference identities are
Δ𝐿𝑝,𝑞(𝑡)=1 𝑡<𝑝+1 𝑡<𝑞−1 𝑡<𝑝+𝑞 (𝑡≥0),
and hence
Δℎ𝑚(𝑡)=𝐿 𝛼+1,𝛽+1(𝑡)−1 𝑡≥𝛾+1 𝐿𝛼+1,𝛽+1(𝑡−𝛾−1) (𝑡≥0).
Taking one more difference gives, for every𝑡 >0,
Δ2ℎ𝑚(𝑡)=1 𝑡≤𝛼+1 𝑡≤𝛽+1 𝑡≤𝛾−1 𝑡≤𝛼+𝛽+1−1 𝑡≤𝛽+𝛾+1
−1 𝑡≤𝛾+𝛼+1+1 𝑡≤𝛼+𝛽+𝛾+2.(3)
Inparticular, Δ2ℎ𝑚(𝑡)≤ 1. Thesameboundholdsfortheshiftedsequence 𝑡↦−→ 1𝑡≥𝑐ℎ𝑀red(𝑡−𝑐),
because below the shift its second difference is zero, and from the shift onward it is the
second difference of the principal sequence of𝑀red. ThereforeΔ 2𝐻(𝑡)≤2.
Formula (3) also implies the following useful dichotomy. If𝑡 >0and Δ2ℎ𝑚(𝑡)= 1, then
either
𝑡≤𝑚(0), 𝑡≤𝑚(1), 𝑡≤𝑚(2),(L)
or
𝑡≥𝑚(0)+𝑚(1)+2, 𝑡≥𝑚(1)+𝑚(2)+2, 𝑡≥𝑚(0)+𝑚(2)+2, 𝑡≤|𝑚|+2.(U)
We refer to these as the lower and upper alternatives. For𝑡= 0, the lower alternative is
automatic.
We shall also use the following elementary consequences of the same box count.
52
Advancing Mathematics Research with AI-Driven Formal Proof Search
1. If𝑡≤𝑚(𝑖)for all𝑖, then
2ℎ𝑚(𝑡)=(𝑡+1)(𝑡+2),Δℎ 𝑚(𝑡)=𝑡+1.(5)
2. If𝑡≥𝑚(𝑖)+𝑚(𝑗)for every pair{𝑖, 𝑗}, and𝑡≤|𝑚|+2, then,
2ℎ𝑚(𝑡)=(|𝑚|+1−𝑡)(|𝑚|+2−𝑡).(6)
3. If𝑡≥𝑚(𝑖)+𝑚(𝑗)+1for every pair{𝑖, 𝑗}, and𝑡≤|𝑚|+2, then
Δℎ𝑚(𝑡)=−(|𝑚|+2−𝑡).(7)
4. For all𝑡,
2ℎ𝑚(𝑡)≤(|𝑚|−𝑡+1)(|𝑚|−𝑡+2).(8)
5. If2𝑡≥|𝑚|+1, then
Δℎ𝑚(𝑡)≤0.(9)
Now fix0 < 𝑑 < 𝑒=|𝑚 1|=|𝑚 2|. Using 𝐻(𝑑)=𝐻(𝑑− 1)+Δ𝐻(𝑑) and Δ𝐻(𝑑+ 1)=
Δ𝐻(𝑑)+Δ 2𝐻(𝑑+1)gives
𝐻(𝑑) 2−𝐻(𝑑−1)𝐻(𝑑+1)=(Δ𝐻(𝑑)) 2−𝐻(𝑑−1)Δ 2𝐻(𝑑+1).(10)
Since 𝐻(𝑑− 1)≥ 0and Δ2𝐻(𝑑+ 1)≤ 2, it is enough to prove the following two statements:
Δ2𝐻(𝑑+1)=1=⇒𝐻(𝑑−1)≤(Δ𝐻(𝑑)) 2,(11)
and
Δ2𝐻(𝑑+1)=2=⇒2𝐻(𝑑−1)≤(Δ𝐻(𝑑)) 2.(12)
Indeed, if Δ2𝐻(𝑑+ 1)≤ 0, equation (10) is immediate; if it is1or2, then (11) or (12)
applies.
Write 𝑓(𝑡)=ℎ 𝑚1(𝑡) and 𝑔(𝑡)= 1𝑡≥𝑐ℎ𝑀red(𝑡−𝑐) , so that𝐻=𝑓+𝑔 . Since Δ2𝑓≤ 1and
Δ2𝑔≤1, ifΔ 2𝐻(𝑑+1)=1, then either
Δ2𝑓(𝑑+1)=1,Δ 2𝑔(𝑑+1)=0,(A)
or
Δ2𝑓(𝑑+1)=0,Δ 2𝑔(𝑑+1)=1.(B)
IfΔ 2𝐻(𝑑+1)=2, then
Δ2𝑓(𝑑+1)=Δ 2𝑔(𝑑+1)=1.(C)
Case A1: (A)+(L) for𝑓.Suppose equation (A) holds and the lower alternative (L) holds
for 𝑓 with 𝑡=𝑑+ 1. Then in particular𝑑+ 1≤𝑚 1(𝑥)< 𝑐 , thus𝑔(𝑑− 1)=𝑔(𝑑)= 0, hence
Δ𝑔(𝑑)=0and therefore
𝐻(𝑑−1)=𝑓(𝑑−1),Δ𝐻(𝑑)=Δ𝑓(𝑑).
By (5),2𝑓(𝑑−1)=𝑑(𝑑+1)andΔ𝑓(𝑑)=𝑑+1. Therefore
𝐻(𝑑−1)=𝑓(𝑑−1)≤(𝑑+1) 2 =(Δ𝑓(𝑑)) 2 =(Δ𝐻(𝑑)) 2.
53
Advancing Mathematics Research with AI-Driven Formal Proof Search
This proves (11) in this case.
Case A2: (A)+(U) for𝑓. Assume equation (A) holds and the upper alternative (U) holds for
𝑓 with𝑡=𝑑+ 1. Let us introduce the shorthand notation𝜌=𝑒−𝑑 . Then (U) gives𝜌≥− 1.
Applying (6) and (7) gives
2𝑓(𝑑−1)=(𝜌+2)(𝜌+3),Δ𝑓(𝑑)=−(𝜌+2).(13)
The shifted summand satisfies
Δ𝑔(𝑑)≤0,2𝑔(𝑑−1)≤(𝜌+2)(𝜌+3),2𝑔(𝑑)≤(𝜌+1)(𝜌+2).(14)
Indeed, the two inequalities for𝑔(𝑑− 1) and 𝑔(𝑑) follow from the universal upper bound (8),
applied to the shifted sequence. For the sign ofΔ𝑔(𝑑) , if𝑑 < 𝑐, then Δ𝑔(𝑑)= 0. If𝑑≥𝑐 , then
the upper alternative for𝑓implies
𝑑≥𝑚 1(𝑥)+𝑚 1(𝑦)+1, 𝑑≥𝑚 1(𝑥)+𝑚 1(𝑧)+1,
where{𝑥,𝑦,𝑧}={0,1,2}. Adding these inequalities gives
2𝑑≥2𝑚 1(𝑥)+𝑚 1(𝑦)+𝑚 1(𝑧)+2=𝑒+𝑚 1(𝑥)+2.
Since 𝑐=𝑚 1(𝑥)+ 1and |𝑀 red|=𝑒−𝑐 , this is equivalent to2(𝑑−𝑐)≥|𝑀 red|+ 1. Thus the
midpoint monotonicity (9) applies to the shifted𝑀red-sequence and givesΔ𝑔(𝑑)≤0.
To prove (11), by (13) it remains to show
𝑓(𝑑−1)+𝑔(𝑑−1)≤  −(𝜌+2)+Δ𝑔(𝑑)  2.
By (13) and (14), this follows from
(𝜌+2)(𝜌+3)+2𝑔(𝑑−1)≤2  −(𝜌+2)+Δ𝑔(𝑑)  2.(15)
Since𝑔(𝑑)=𝑔(𝑑−1)+Δ𝑔(𝑑), the third inequality in (14) gives
2𝑔(𝑑−1)≤(𝜌+1)(𝜌+2)−2Δ𝑔(𝑑).
Therefore the difference between the right-hand side and the left-hand side of (15) is at least
2 −(𝜌+2)+Δ𝑔(𝑑)  2−(𝜌+2)(𝜌+3)−  (𝜌+1)(𝜌+2)−2Δ𝑔(𝑑) 
=2Δ𝑔(𝑑)  
Δ𝑔(𝑑)−2(𝜌+2)+1 
.
This is nonnegative becauseΔ𝑔(𝑑)≤0,𝜌≥−1, and hence
Δ𝑔(𝑑)−2(𝜌+2)+1≤0.
Thus (11) holds in this case, and we completed the (A) case.
For the two cases when (B) holds, that isΔ2𝑔(𝑑+ 1)= 1, we use the following shift
reduction. If
Δ2𝐻(𝑑+1)=1and𝐻(𝑑+1)≤(Δ𝐻(𝑑+1)) 2,
54
Advancing Mathematics Research with AI-Driven Formal Proof Search
then
𝐻(𝑑−1)≤(Δ𝐻(𝑑)) 2.(16)
Indeed,Δ𝐻(𝑑)=Δ𝐻(𝑑+1)−1and𝐻(𝑑−1)=𝐻(𝑑+1)−Δ𝐻(𝑑+1)−Δ𝐻(𝑑). Therefore
𝐻(𝑑−1)=𝐻(𝑑+1)−2Δ𝐻(𝑑+1)+1≤(Δ𝐻(𝑑+1)) 2−2Δ𝐻(𝑑+1)+1=(Δ𝐻(𝑑)) 2.
Case B1: (B)+(L) for𝑔.Assume equation (B) holds and the lower alternative (L) holds for
𝑔 with𝑡=𝑑+ 1. Let𝐷=𝑑+ 1. Since Δ2𝑔(𝐷)= 1, necessarily𝐷≥𝑐 , and Δ2ℎ𝑀red(𝐷−𝑐)= 1.
In the lower subcase𝐷−𝑐≤𝑀 red(𝑖) for every𝑖. Then𝐷−𝑐+ 1≥ 1, and the lower formula
(5) gives
2𝑔(𝐷)=(𝐷−𝑐+1)(𝐷−𝑐+2),Δ𝑔(𝐷)=𝐷−𝑐+1.(17)
We next prove two bounds for𝑓at𝐷:
𝑓(𝐷)≤(𝐷+1)Δ𝑓(𝐷),Δ𝑓(𝐷)=𝑐.(18)
First, sinceΔ2𝑓(𝐷)= 0, the explicit formula (3), together with the lower inequalities for𝑀red,
implies
𝐷≤𝑚 1(0)+𝑚 1(1)+1, 𝐷≤𝑚 1(1)+𝑚 1(2)+1, 𝐷≤𝑚 1(0)+𝑚 1(2)+1.(19)
Indeed, the two pair inequalities involving𝑥 follow directly from𝐷−𝑐≤𝑀 red(𝑦)≤𝑚 1(𝑦) for
𝑦≠𝑥 . The remaining pair inequality follows from (3): if it failed, then the corresponding
two single indicators would be zero; since𝐷≥𝑐=𝑚 1(𝑥)+ 1, the𝑥-single indicator is also
zero, and the right-hand side of (3) would be negative, contradictingΔ2𝑓(𝐷)=0.
Thus, in (3) for𝑓 at 𝐷, all three pair indicators and the triple indicator are equal to1.
Since Δ2𝑓(𝐷)= 0, exactly two of the three single indicators are equal to1. Moreover the
𝑥-single indicator is zero, because𝐷≥𝑚 1(𝑥)+ 1. Hence the two remaining single indicators
are equal to1.
It follows that for every1≤𝑘≤𝐷 , the same two single indicators are still equal to1,
while the three pair indicators and the triple indicator are also equal to1. Therefore
Δ2𝑓(𝑘)≥2−3+1=0(1≤𝑘≤𝐷).
Thus the first differencesΔ𝑓(𝑘)are nondecreasing on{0,1,...,𝐷}. Since
𝑓(𝐷)=
𝐷∑︁
𝑗=0
Δ𝑓(𝑗),
we get
𝑓(𝐷)≤(𝐷+1)Δ𝑓(𝐷).
This proves the first inequality in (18).
For the second inequality in (18), relabel the two coordinates different from𝑥 as 𝑦,𝑧 ,
and write
𝐴=𝑚 1(𝑦)+1, 𝐵=𝑚 1(𝑧)+1,
55
Advancing Mathematics Research with AI-Driven Formal Proof Search
and recall𝑐=𝑚 1(𝑥)+ 1. Using the box-count formula with𝑥 as the third coordinate, the
first-difference formula gives
Δ𝑓(𝐷)=𝐿 𝐴,𝐵(𝐷)−𝐿 𝐴,𝐵(𝐷−𝑐),
because𝐷≥𝑐. From the preceding paragraph,𝐷 < 𝐴and𝐷 < 𝐵, hence
𝐿𝐴,𝐵(𝐷)=𝐷+1, 𝐿 𝐴,𝐵(𝐷−𝑐)=𝐷−𝑐+1.
Therefore
Δ𝑓(𝐷)=(𝐷+1)−(𝐷−𝑐+1)=𝑐,
proving (18). Using (17) and (18), we have
2𝐻(𝐷)=2𝑓(𝐷)+2𝑔(𝐷)≤2Δ𝑓(𝐷)(𝐷+1)+(𝐷−𝑐+1)(𝐷−𝑐+2).
Also, by (17),
Δ𝐻(𝐷)=Δ𝑓(𝐷)+Δ𝑔(𝐷)=Δ𝑓(𝐷)+(𝐷−𝑐+1).
Thus it is enough to show
2Δ𝑓(𝐷)(𝐷+1)+(𝐷−𝑐+1)(𝐷−𝑐+2)≤2  
Δ𝑓(𝐷)+𝐷−𝑐+1  2.
Since 𝐷+ 1 =(𝐷−𝑐+ 1)+𝑐 , the difference between the right-hand side and the left-hand
side is
2Δ𝑓(𝐷)  
Δ𝑓(𝐷)−𝑐
+2Δ𝑓(𝐷)(𝐷−𝑐+1)+(𝐷−𝑐+1)(𝐷−𝑐).
This is nonnegative becauseΔ𝑓(𝐷)≥𝑐 and 𝐷−𝑐+ 1≥ 1. Therefore𝐻(𝐷)≤(Δ𝐻(𝐷)) 2. By
the shift reduction (16), this proves (11).
Case B2: (B)+(U) for𝑔.Again let 𝐷=𝑑+ 1and put 𝜌=𝑒−𝐷 . The upper alternative for
ℎ𝑀red at𝐷−𝑐gives𝜌≥−2. Since|𝑀 red|=𝑒−𝑐, formulas (6) and (7) give
2𝑔(𝐷)=(𝜌+1)(𝜌+2),Δ𝑔(𝐷)=−(𝜌+2).(20)
For the first summand, the universal upper bound (8) gives
2𝑓(𝐷)≤(𝑒−𝐷+1)(𝑒−𝐷+2)=(𝜌+1)(𝜌+2).(21)
It remains to justify the sign ofΔ𝑓(𝐷). Since𝑔is in the upper alternative at𝐷, we have
𝐷−𝑐≥𝑀 red(0)+𝑀 red(1)+2, 𝐷−𝑐≥𝑀 red(1)+𝑀 red(2)+2, 𝐷−𝑐≥𝑀 red(0)+𝑀 red(2)+2.
Adding these three inequalities gives
3(𝐷−𝑐)≥2|𝑀 red|+6=2(𝑒−𝑐)+6.
Hence
2(𝐷−𝑐)≥ 2
3
 2|𝑀 red|+6  =|𝑀 red|+1+ |𝑀 red|+9
3 >|𝑀 red|+1,
because|𝑀 red|≥0. Therefore
2𝐷=2(𝐷−𝑐)+2𝑐≥(𝑒−𝑐+1)+2𝑐=𝑒+𝑐+1≥𝑒+1.
56
Advancing Mathematics Research with AI-Driven Formal Proof Search
By midpoint monotonicity (9), applied to𝑓=ℎ 𝑚1, we getΔ𝑓(𝐷)≤ 0. Using (20), (21), we
get
2𝐻(𝐷)≤2(𝜌+1)(𝜌+2),Δ𝐻(𝐷)=Δ𝑓(𝐷)−(𝜌+2).
Since𝜌≥−2andΔ𝑓(𝐷)≤0, we have
(𝜌+1)(𝜌+2)≤  −Δ𝑓(𝐷)+𝜌+2  2.
giving the desired𝐻(𝐷)≤(Δ𝐻(𝐷)) 2. By the shift reduction (16), this proves (11).
Case C: (C) holds.So hereΔ2𝐻(𝑑+ 1)= 2and hence Δ2𝑓(𝑑+ 1)=Δ 2𝑔(𝑑+ 1)= 1. Since
Δ2𝑔(𝑑+ 1)= 1, necessarily𝑑+ 1≥𝑐 . Therefore the lower alternative (L) for𝑓 is impossible,
because it would imply𝑑+ 1≤𝑚 1(𝑥)< 𝑐 . Hence 𝑓 is in its upper alternative, that is, (U)
holds for𝑓. The lower alternative (L) for𝑔 is also impossible. Indeed, if𝑑+ 1−𝑐≤𝑀 red(𝑖)
for every𝑖, then, choosing any𝑦≠𝑥, we get
𝑑+1≤𝑚 1(𝑥)+1+𝑀 red(𝑦)=𝑚 1(𝑥)+1+𝑚 2(𝑦)≤𝑚 1(𝑥)+1+𝑚 1(𝑦).
But the upper alternative for𝑓 gives𝑑+ 1≥𝑚 1(𝑥)+𝑚 1(𝑦)+ 2, a contradiction. Thus𝑔 is
also in its upper alternative, and (U) holds for𝑔. Put𝜌=𝑒−𝑑 again. Since|𝑀 red|=𝑒−𝑐 , we
also have|𝑀 red|−(𝑑−𝑐)=𝑒−𝑑=𝜌 . The upper formulas (6) and (7), applied to𝑓 and to
the shifted summand𝑔, give
2𝑓(𝑑−1)=(𝜌+2)(𝜌+3),Δ𝑓(𝑑)=−(𝜌+2),
and
2𝑔(𝑑−1)=(𝜌+2)(𝜌+3),Δ𝑔(𝑑)=−(𝜌+2).
Therefore
2𝐻(𝑑−1)=2(𝜌+2)(𝜌+3),Δ𝐻(𝑑)=−2(𝜌+2).
Since the upper alternative for𝑓gives𝜌≥−1, we have
(Δ𝐻(𝑑)) 2−2𝐻(𝑑−1)=4(𝜌+2) 2−2(𝜌+2)(𝜌+3)=2(𝜌+2)(𝜌+1)≥0.
which proves (12). This completes the proof of (11) and (12), and hence by (10)𝐻(𝑑−
1)𝐻(𝑑+ 1)≤𝐻(𝑑) 2. Since0 < 𝑑 < 𝑒was arbitrary and𝐻 is the pure𝑂-sequence ofΓ by (2),
the theorem follows.□
The Lean proof for the problem can be found athttps://github.com/google-dee
pmind/alphaproof-nexus-results/tree/main/APNOutputs/AICollaborator/A
lgebraicGeometry.
A Convergence Proof of Modified Anchored Gradient Descent-Ascent
A natural-language version of the convergence proof we discovered can be found in Surina et
al. [58]. The Lean proof is athttps://github.com/google-deepmind/alphaproof-n
exus-results/blob/main/APNOutputs/Optimization/LastIterateConvergence.
lean.
57
Advancing Mathematics Research with AI-Driven Formal Proof Search
Written on the Wall, Conjecture 2
For a graph𝐺, let𝑉(𝐺) be the set of vertices and𝐸(𝐺) the set of edges. For𝑣∈𝑉(𝐺) , write
𝑑(𝑣) for the degree of𝑣, and let𝑁(𝑣) be the set of vertices adjacent to𝑣 in𝐺. Let𝛼(𝑣) be
the local independence number of𝑣: the size of the largest independent set in𝐺[𝑁(𝑣)] . Let
ℓ(𝐺) := 1
𝑛
˝
𝑣𝛼(𝑣) be the average of the local independence numbers, and let𝐿𝑆(𝐺) be the
maximum number of leaves in a spanning tree of𝐺, or0if𝐺is not connected.
Theorem.If𝐺is a simple connected graph on𝑛vertices, then
𝐿𝑆(𝐺)≥2(ℓ(𝐺)−1).
Proof.Let 𝑉 :=𝑉(𝐺) . For every vertex𝑣∈𝑉 , fix a maximum independent set𝐴(𝑣) in𝐺[𝑁(𝑣)] .
Then𝛼(𝑣)=|𝐴(𝑣)|.
Now take two copies of𝑉, and add edges𝑢𝑣 from𝑢∈𝑉 on the left to𝑣∈𝐴(𝑢) on the
right. This forms a bipartite graph, where vertices on the left side have degree𝛼(𝑣). The key
idea is to look at the degrees of the vertices on the right side, and formulate the entire proof
in terms of them. Formally, put𝑐(𝑣) :=|𝑢∈𝑉(𝐺):𝑣∈𝐴(𝑢)| as the degree of a vertex𝑣 on
the right side.
Note that𝑐(𝑣)≤𝑑(𝑣) , for all𝑣∈𝑉 . Because˝
𝑣𝛼(𝑣)= ˝
𝑣𝑐(𝑣), it is enough to show that˝
𝑣𝑐(𝑣)≤𝑛(𝐿 𝑆(𝐺)/ 2+ 1). To simplify the notation, we set𝜇 :=𝐿 𝑆(𝐺)/ 2+ 1, and so the goal
is to show˝
𝑣𝑐(𝑣)≤𝑛𝜇.
Lemma 1.For every edge𝑢𝑣∈𝐸(𝐺)we have𝑐(𝑢)+𝑐(𝑣)≤|𝑁(𝑢)∪𝑁(𝑣)|.
Proof of Lemma 1.For every vertex𝑤∈𝑁(𝑢)∪𝑁(𝑣) , at most one of𝑢 and 𝑣 can be part
of 𝐴(𝑤), otherwise the edge𝑢𝑣 would contradict the fact that𝐴(𝑤) is independent. On the
other hand, if𝑤∈𝑉 is such that𝑢 or 𝑣 is in𝐴(𝑤), then𝑤 must be part of𝑁(𝑢)∪𝑁(𝑣) . Then
𝑐(𝑢)+𝑐(𝑣)is at most the size of𝑁(𝑢)∪𝑁(𝑣).□
Lemma 2.For every edge𝑢𝑣∈𝐸(𝐺)we have|𝑁(𝑢)∪𝑁(𝑣)|≤𝐿 𝑆(𝐺)+2.
Proof of Lemma 2.We construct a spanning tree in𝐺 with at least|𝑁(𝑢)∪𝑁(𝑣)|− 2leaves.
Start with the edge𝑢𝑣 and add all the vertices in𝑁(𝑢)∪𝑁(𝑣)\{𝑢,𝑣} as pendant vertices
of degree1. There are|𝑁(𝑢)∪𝑁(𝑣)|− 2leaves in this tree𝑇′. Because𝐺 is connected, we can
expand𝑇′ to a spanning tree𝑇 of𝐺 by adding edges until no more can be added. Then from
every leaf in𝑇′ there is a path to a leaf in𝑇 that doesn’t cross𝑢𝑣. All these leaves must be
distinct, since they are contained in distinct subtrees of𝑇. Then𝑇 has at least|𝑁(𝑢)∪𝑁(𝑣)|− 2
leaves.□
Lemmas 1 and 2 show that for every edge𝑢𝑣∈𝐸(𝐺),
𝑐(𝑢)+𝑐(𝑣)≤𝐿 𝑆(𝐺)+2=2𝜇.
Next, we observe that˝
𝑣𝑐(𝑣)≤𝑛𝜇 trivially holds if every𝑐(𝑣)≤𝜇 . So assume this is
not the case. Then we can split the vertices into "heavy" vertices with𝑐(𝑣)> 𝜇 , and "light"
vertices with𝑐(𝑣)≤𝜇. Let𝑆be the set of heavy vertices.
𝑆 must be an independent set, since the above equation shows that for any edge𝑢𝑣,
at most one of𝑢 or 𝑣 can be heavy. Less obvious is that light vertices cannot have many
neighbors in𝑆.
Lemma 3.If𝑣is a light vertex, then|𝑁(𝑣)∩𝑆|< 𝜇.
58
Advancing Mathematics Research with AI-Driven Formal Proof Search
Proof of Lemma 3.Let𝑢∈𝑁(𝑣)∩𝑆 . Since𝑆 is independent, all neighbours of𝑢 are outside
𝑁(𝑣)∩𝑆. So|𝑁(𝑢)∪𝑁(𝑣)|≥|𝑁(𝑣)∩𝑆|+|𝑁(𝑢)|. Using Lemma 2 we get
|𝑁(𝑣)∩𝑆|≤|𝑁(𝑢)∪𝑁(𝑣)|−|𝑁(𝑢)|≤𝐿 𝑆(𝐺)+2−𝑑(𝑢).
As𝑑(𝑢)≥𝑐(𝑢)> 𝜇, we obtain|𝑁(𝑣)∩𝑆|< 𝐿 𝑆(𝐺)+2−𝜇=𝜇.□
Then the theorem follows from the following more general statement:
Claim.Let𝑐:𝑉→ℝand𝜇≥0satisfy:
1.𝑐(𝑣)≤𝑑(𝑣)for all𝑣,
2.𝑐(𝑢)+𝑐(𝑣)≤2𝜇for every edge𝑢𝑣,
3.𝑆:={𝑢:𝑐(𝑢)> 𝜇}is an independent set,
4.|𝑁(𝑣)∩𝑆|< 𝜇for every𝑣∉𝑆.
Then ˝
𝑣𝑐(𝑣)≤𝑛𝜇.
Proof of Claim.We assume𝑆 is non-empty, otherwise the claim is trivially true. The proof
uses a discharging argument: it sends theexcess𝑐(𝑢)−𝜇 from a heavy vertex𝑢∈𝑆 to its
neighbors. The redistribution keeps the total sum˝
𝑣𝑐(𝑣) constant. However, the amount
sent to a light vertex𝑣 is less than theslack𝜇−𝑐(𝑣) , so the overall sum can’t exceed𝑛𝜇.
Precisely, define a weight function that transfers excess from heavy to light vertices:
𝑊(𝑢,𝑣):=
(𝜇−𝑐(𝑣)
𝑑(𝑢) if𝑢∈𝑆and𝑢𝑣is an edge,
0otherwise.
Because𝑆 is independent, the weight flows only from heavy to light vertices. We now show
two statements.
Eachheavyvertexsendsoutenoughweight. If 𝑢∈𝑆 and𝑢𝑣 isanedge, then 𝑐(𝑢)+𝑐(𝑣)≤ 2𝜇
by condition 2. So𝜇−𝑐(𝑣)≥𝑐(𝑢)−𝜇. Then
∑︁
𝑣∈𝑁(𝑢)
𝑊(𝑢,𝑣)≥𝑑(𝑢) 𝑐(𝑢)−𝜇
𝑑(𝑢) =𝑐(𝑢)−𝜇.
Each light vertex absorbs at most its slack. Let𝑣∉𝑆 . Then𝑣 receives weight from vertices
in𝐹:=𝑁(𝑣)∩𝑆.
Let 𝑢∈𝐹 . From conditions (1) and (4), we have|𝐹|< 𝜇 < 𝑐(𝑢)≤𝑑(𝑢) . Then the total weight
received is ∑︁
𝑢∈𝐹
𝑊(𝑢,𝑣)=
∑︁
𝑢∈𝐹
𝜇−𝑐(𝑣)
𝑑(𝑢) <
∑︁
𝑢∈𝐹
𝜇−𝑐(𝑣)
|𝐹| =𝜇−𝑐(𝑣).
These two statements together show that
∑︁
𝑢∈𝑆
𝑐(𝑢)−𝜇≤
∑︁
𝑢∈𝑆
∑︁
𝑣∉𝑆
𝑊(𝑢,𝑣)=
∑︁
𝑣∉𝑆
∑︁
𝑢∈𝑆
𝑊(𝑢,𝑣)≤
∑︁
𝑣∉𝑆
𝜇−𝑐(𝑣).
Re-arranging the terms gives˝
𝑣𝑐(𝑣)< 𝑛𝜇as desired.□
The discovered lean proof for this is available athttps://github.com/google-dee
pmind/alphaproof-nexus-results/blob/main/APNOutputs/OEIS/GraphConjec
ture2.lean.
59
