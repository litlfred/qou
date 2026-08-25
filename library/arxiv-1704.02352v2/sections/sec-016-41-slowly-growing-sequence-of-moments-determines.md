---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-016-41-slowly-growing-sequence-of-moments-determines
section_title: "Slowly growing sequence of moments determines the measure"
section_number: 4.1
pages: 29-30
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
---
Lemma 4.1. Assume that µ is a probability measure which is supported
on the interval [x0, ∞) (respectively, on the interval (−∞, x0]) for some
x0 ∈ R and such that
(4.1) |ml| ≤ C l l2l
holds true for some constant C and all integers l ≥ 1, where
ml = ml(µ) =
∫
R
xl dµ
is the l-th moment of µ.
Then the measure µ is uniquely determined by its moments.
Similarly, if the measure µ is supported on the real line R and such that
(4.2) |ml| ≤ C l ll
holds true for some constant C and all integers l ≥ 1, then the measure µ
is uniquely determined by its moments.
Proof. In the case when µ is supported on the interval [0, ∞) this is exactly
Stieltjes moment problem, while in the case when µ is supported on the real
line R this is exactly the Hamburger moment problem. It is easy to ch eck
that the assumptions (4.1), and (4.2) imply that the Carlema n’s conditions
in both Stieltjes and Hamburger, respectively, problems ar e satisiﬁed and it
follows that the measure µ is uniquely determined by its moments.
30 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
Now, assume that µ is a probability measure which is supported on the
interval [x0, ∞). We deﬁne a probability measure µx0 supported on the
interval [0, ∞), as a translation of µ that is, for any measurable set A ⊂ R
we have
µx0(A) := µ(A + x0).
Let us compute the moments of µx0:
ml(µx0) =
∫
R
xl dµx0 =
∫
R
(x − x0)l dµ =
∑
k
(l
k
)
(−x0)l−k
∫
R
xk dµ.
This leads to the following inequalities:
⏐
⏐ml(µx0)
⏐
⏐ ≤
∑
k
(l
k
)
|x0|l−k |mk| ≤
∑
k
(l
k
)
|x0|l−k C k k2k ≤ (C + |x0|)l l2l.
By Carleman’s criterion it means that the measure µx0 is uniquely de-
termined by its moments, which is equivalent by the construc tion that the
measure µ is uniquely determined by its moments, too.
The case, when µ is supported on the interval (−∞, x0] is analogous, and
we leave it as a simple exercise. □
