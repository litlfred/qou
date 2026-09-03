---
doc_id: hal-01215114
doc_title: "FPSAC 2011, Reykjavík, Iceland DMTCS proc. AO, 2011, 317–328 Dual combinatorics of zonal polynomials"
section_id: sec-016-in-terms-of-free-cumulants
section_title: "In terms of free cumulants"
section_number: null
pages: 10-11
source_pdf: hal-01215114.pdf
source_sha256: c70f8b04a5542a1f
doc_brief: "FPSAC 2011, Reykjavík, Iceland DMTCS proc. AO, 2011, 317–328 Dual combinatorics of zonal polynomials — In this paper we establish a new combinatorial formula for zonal polynomials in terms of"
---
The following observation is due to Lassalle [Las09]. Let k≥ 1 be a ﬁxed integer and let α be ﬁxed.
Since Σ(α)
k is an α-shifted symmetric function and the anisotropic free cumulants (R(α)
l )l≥2 form an
algebraic basis of the ring ofα-shifted symmetric functions (see [Las09] for their deﬁnition), there exists
a polynomialK(α)
k such that, for any Young diagramλ,
Σ(α)
k (λ) =K(α)
k
(
R(α)
2 (λ),R (α)
3 (λ),...
)
.
This polynomial is called Jack Kerov polynomial.
Thus Jack Kerov polynomials express Jack characters on cycles in terms of free cumulants. For more
complicated conjugacy classes it turns out to be more convenient to express not directly the characters
Σ(α)
(k1,...,k𝓁) but rather cumulant
(−1)𝓁−1κid(Σ(α)
k1
,..., Σ(α)
k𝓁
). (9)
This gives rise to generalized Jack Kerov polynomials K(α)
(k1,...,k𝓁). In the classical context α = 1 these
quantities have been introduced by one of us and Rattan [R ´S08]; in the Jack case they have been studied
by Lassalle [Las09]. We skip the deﬁnitions and refer to the above papers for details since generalized
Kerov polynomials are not of central interest for this paper.
Using the technology developed in [DF´S10], one can deduce from Theorem 9 a combinatorial interpre-
tation for the coefﬁcients of generalized zonal Kerov polynomials (i.e. generalized Jack Kerov polynomi-
als in the caseα = 2):
Dual combinatorics of zonal polynomials 327
Theorem 11 Letν be a partition of an integerk andS1,S2 be two ﬁxed pair-partitions of [2k] such that
µ
(
L(S1,S 2)
)
=ν. Consider also a sequence s2,s 3,... of non-negative integers with only ﬁnitely many
non-zero elements. The rescaled coefﬁcient
(−2)𝓁(ν)(−1)|ν|+2s2+3s3+···
[(
R(2)
2
)s2(
R(2)
3
)s3
···
]
K(2)
ν
of the (generalized) zonal Kerov polynomial is equal to the number of couples (S0,q ) with the following
properties:
(a) the graph of vertex set [2n] obtained by drawing an edge between i andj if they are in the same
part ofS0,S1 orS2 is connected;
(b) the number of loops in GS0,S1 is equal tos2 +s3 +··· ;
(c) the number of loops in GS0,S2 is equal tos2 + 2s3 + 3s4 +··· ;
(d) q is a function fromL(S0,S 1) to the set{2, 3,... }; we require that each numberi∈{ 2, 3,... } is
used exactlysi times;
(e) for every subset A⊂L (S0,S 1) of loops which is nontrivial (i.e.,A⁄=∅ andA⁄=L(S0,S 1)), there
are more than∑
v∈A
(
q(v)− 1
)
loops inL(S0,S 2) which have a non-empty intersection with at
least one loop fromA.
