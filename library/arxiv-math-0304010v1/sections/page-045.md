---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-045
section_title: "Page 45"
section_number: null
pages: 45-45
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
be the generating series for the complete homogeneous symmetric functions. We
introduce elements f1 , f2 , . . . in Λ as follows:
f1 = h1 ;
fk = −
1
k −1 [tk]
n
H−(k−1)(t)
o
,
k = 2, 3, . . . .
More explicitly,
fk =
X
m1,m2,···≥0
1·m1+2·m2+···=k
(−1)
P mj−1 k↑(P mj−1) Y
j≥1
hmj
j
mj! ,
where
x↑m = Γ(x + m)
Γ(x)
= x(x + 1) . . .(x + m −1).
This deﬁnition is inspired by Voiculescu’s free probability theory [Vo], [VoDN].
Let µ be a compactly supported probability measure on R, i.e., an element of M,
in our notation. When the hk’s are specialized to the moments of µ,
hk
−→
Z
R
xkµ(dx),
k = 1, 2, . . .,
the elements fk turn into the free cumulants of the measure µ. The free cumulants
are counterparts of the semi–invariants in the sense of conventional probability
theory. The free cumulants are additive functionals with respect to additive free
convolution of measures (just as the semi–invariants are additive functionals with
respect to the conventional convolution product). See [Vo], [VoDN], [Sp].
Denote by efk ∈A the image of fk ∈Λ under the morphism (2.18). Note that
ef1 = 0. Let λ ∈Y be arbitrary and let µ ∈M0 be the transition measure of λ, see
(8.2)–(8.3). Then efk(λ) coincides with the kth free cumulant of µ.
Proposition 10.1. For any k = 1, 2, . . ., the element efk+1 coincides with the top
weight homogeneous component of p#
k .
Proof. By the very deﬁnition
efk+1 = −1
k [tk+1]


(1 +
X
j≥2
ehjtj)−k


= −1
k [tk+1]


exp(−k
X
j≥2
epj
j tj)


,
which is exactly formula (3.4). Then the claim follows from Proposition 3.5.
□
Biane [Bi1] found out that free cumulants emerge in the asymptotic theory of
characters of the symmetric groups. To state his result we need a notation.
Given A > 1, let Y(A) denote the set of the Young diagrams λ such that λ1 ≤
√nA, λ′
1 ≤√nA, where n = |λ|. Equivalently, ¯λ(x) = |x| whenever |x| ≥A. Recall
that ¯λ(x) = n−1/2(n1/2x) is the scaled version of λ( · ).
45
