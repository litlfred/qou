---
doc_id: arxiv-hep-th-9310070v1
doc_title: "Quantum dilogarithm"
section_id: page-002
section_title: "Page 2"
section_number: null
pages: 2-2
source_pdf: 9310070v1.pdf
source_sha256: b979ebf2f47a4653
toc_source: undetermined
doc_brief: "Quantum dilogarithm — A quantum generalization of Rogers’ ﬁve term, or “pentagon” dilogarithm identity is suggested. It is shown that the classical limit gives usual Rogers’ identity."
---
1. Introduction
Recently, the dilogarithm function appeared in the study of the two dimensional quantum
conformal ﬁeld theory (CFT)[1] and solvable lattice models both in two [2] and three
dimensions [3]. Particularly, the eﬀective central charges of some rational CFT can be
expressed as ﬁnite sums of Rogers’ dilogarithm function with the arguments being solutions
for certain algebraic relations (e. g. thermodynamical Bethe anzats relations).
People use the dilogarithm function in two forms, L2(x) and L(x), introduced by
Euler and Rogers, respectively. Euler’s dilogarithm for any complex x can be deﬁned by
the following integral:
L2(x) = −
Z x
0
log(1 −z)
z
dz,
(1.1)
while Rogers’ diﬀers by the addition of an elementary function
L(x) = L2(x) + log(1 −x) log(x)/2.
(1.2)
Among the various properties of these functions the most profound one is (probably) the
ﬁve term or “pentagon” identity for L(x), proved by Rogers [4]:
L(x) + L(y) −L(xy) = L(x −xy
1 −xy ) + L(y −xy
1 −xy ),
(1.3a)
which in terms of Euler’s dilogarithm looks like
L2(x) + L2(y) −L2(xy) = L2(x −xy
1 −xy ) + L2(y −xy
1 −xy ) + log( 1 −x
1 −xy ) log( 1 −y
1 −xy ).
(1.3b)
On the other hand, in the context of integrable lattice quantum ﬁeld theory models
and quantum groups the problem of constructing of the Virasoro algebra on the lattice has
been suggested and partially solved [5], [6]. The following transcendental function plays
the signiﬁcant role in the latter:
Ψ(x) =
∞
Y
n=1
(1 −xθn),
|θ| < 1,
(1.4)
where x is any complex variable and θ, a ﬁxed complex parameter, lies within a unit
disk⋆. Considering θ as a quantization parameter, the function Ψ(x) can be interpreted as
a “quantum” Euler’s dilogarithm in the following sense. Let θ = exp(ǫ) for Re(ǫ) < 0 and
perform the limit ǫ →0. Then, it is easy to see that
Ψ(x) =
1
√1 −x exp(L2(x)/ǫ)(1 + O(ǫ)).
(1.5)
⋆In [6] this function has been deﬁned using a slightly diﬀerent argument and denoted
as S(x), with θ being q2 of [6]. In fact, the precise relation between the two deﬁnitions is
Ψ(x) = S(−θ1/2x).
1
