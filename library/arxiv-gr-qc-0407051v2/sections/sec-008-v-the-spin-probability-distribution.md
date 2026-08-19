---
doc_id: arxiv-gr-qc-0407051v2
doc_title: "Black hole entropy from Quantum Geometry"
section_id: sec-008-v-the-spin-probability-distribution
section_title: "THE SPIN PROBABILITY DISTRIBUTION"
section_number: V
pages: 12-14
source_pdf: 0407051v2.pdf
source_sha256: 2de07e909b17c5a5
doc_brief: "Black hole entropy from Quantum Geometry — Quantum Geometry (the modern Loop Quantum Gravity using gra phs and spin-networks instead of the loops) provides microscopic d egrees of freedom that"
---
Given any value a of the classical horizon area, and the N(a) quantum states of the
horizon labeled by all the ﬁnite sequences ( m1, ..., mn) of the non-zero half-integers such
that (36) one can ﬁx any arbitrary
0 ⁄= m ∈ 1
2Z (59)
and consider the subset of states corresponding to the seque nces such that
m1 = m. (60)
Denote the number of the elements of this subset by N(a)(m). The ratio
P(a)(m) := N(a)(m)
N(a) (61)
can be considered as the probability that the ﬁrst puncture i s labeled by m1 = m. The
question is, what P(a)(m) is when a is large compared to the minimal area am created at the
puncture4,
am = 8 πγℓ 2
Pl
√
|m|(|m| + 1). (62)
4This issue has been raised recently by John Baez.
12
(Notice, that the answer could make no probabilistic sense, if the lim a→∞ P(a)(m) were 0 for
all the values of m, for example.) The number N(a)(m) deﬁned above can be also thought
of as a number of all the ﬁnite sequences ( m2, ..., mn) such that
n∑
i=2
mi = −m,
n∑
i=2
√
|mi|(|mi| + 1) ≤ a − am
8πγℓ 2
Pl
. (63)
By the same randon walk argument as the one used above in the tr eatment of the number
N ′−
k (as before, see [11] for a proof) we have
N(a)(m) = e− m2
a−am N(a − am) + ... (64)
where the other terms can be neglected when we go to the limit a → ∞. Since the number
N(a) is given by exponentiating (56), we can see that in the limit a → ∞
P(a)(m) → e−2πγM
√
|m|(|m|+1) =: P (m). (65)
Now, the equality (57) means that the limits P (m) of the probabilities still sum to 1,
∑
0⁄=m∈ 1
2 Z
P (m) = 1 . (66)
That (limit) probability distribution P (m) can also be written in terms of the entropy
S(am) corresponding to the area am, namely
P (m) = e−S(am), (67)
regardless of whether we ﬁx the value of γ by the agreement with the Bekenstein-Hawking
entropy or not.
Acknowledgments We beneﬁted a lot from the discussions with Abhay Ashtekar, J ohn
Baez, Alejandro Corichi, Kirill Krasnov and Marek Napi´ ork owski. Krzysztof Meissner, the
referee of the diploma thesis of one us (MD), helped us to unde rstand the relevance and
irrelevance of the constraint on the quantum excitations of the C-S ﬁeld. JL was partially
supported by Polish Committee for Scientiﬁc Research (KBN) under grant number 2P03B
12724.
13
