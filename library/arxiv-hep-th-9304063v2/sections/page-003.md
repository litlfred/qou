---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: undetermined
doc_brief: "arXiv:hep-th/9304063v2 29 Jan 1999 — 18 sections: Page 1; Page 2; Page 3"
---
B. The System of Partial Diﬀerential Equations
We set
J :=
m
[
j=1
(a2j−1, a2j)
(aj ≥0)
(1.4)
and write D(J; λ) for the Fredholm determinant of K (the operator with kernel K(x, y)) acting on J. If we think of
this as a function of a = (a1, . . . , a2m) then
d log D(J; λ) = −
2m
X
j=1
(−1)j R(aj, aj) daj
(1.5)
where R(x, y) is the kernel of K(I −K)−1. We introduce the notations
φ(x) :=
√
λ Jα(√x),
ψ(x) := x φ′(x)
(1.6)
and the quantities
qj : = (I −K)−1φ (aj),
pj := (I −K)−1ψ (aj),
(j = 1, . . . , 2m)
(1.7)
u : = (φ, (I −K)−1φ),
v := (φ, (I −K)−1ψ),
(1.8)
where the inner products refer to the domain J. The diﬀerential equations are
∂qj
∂ak
= (−1)k qjpk −pjqk
aj −ak
qk
(j̸ = k)
(1.9)
∂pj
∂ak
= (−1)k qjpk −pjqk
aj −ak
pk
(j̸ = k)
(1.10)
aj
∂qj
∂aj
= pj + 1
4 qj u −
X
k̸=j
(−1)k ak
qjpk −pjqk
aj −ak
qk
(1.11)
aj
∂pj
∂aj
= 1
4(α2 −aj + 2v) qj −1
4pj u −
X
k̸=j
(−1)k ak
qjpk −pjqk
aj −ak
pk
(1.12)
∂u
∂aj
= (−1)j q2
j
(1.13)
∂v
∂aj
= (−1)j pj qj.
(1.14)
Moreover the quantities R(aj, aj) appearing in (1.5) are given by
aj R(aj, aj) =
X
k̸=j
(−1)k ak
(qjpk −pjqk)2
aj −ak
+ p2
j −1
4 (α2 −aj + 2v)q2
j + 1
2 pj qj u.
(1.15)
These equations are quite similar to eqs. (1.4)–(1.9) of [28], as is their derivation.
C. The ordinary diﬀerential equation
For the special case J = (0, s) the above equations can be used to show that q(s; λ), the quantity q of the last
section corresponding to the endpoint s, satisﬁes
s(q2 −1)(s q′)′ = q(sq′)2 + 1
4(s −α2)q + 1
4sq3(q2 −2)
(′= d
ds).
(1.16)
with boundary condition
3
