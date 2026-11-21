---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-018-321-refined-superconformal-index
section_title: "Refined superconformal index"
section_number: 3.2.1
pages: 32-34
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
toc_source: inferred
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
We now move to the case of M3 = L(p, 1) ∼= S3/Zp. The theory T[L(p, 1), U(N)] is an N = 2
Chern-Simons theory at level p, with a chiral multiplet Φ in the adjoint representation with
R-charge R(Φ) = 2 [54,66,67]. Its superconformal index is given by (see e.g. [68])
IU(N)(q, t) =
X
m1⩾···⩾mN∈Z
1
|Wm|
Z
|zi|=1
Y
j
dzj
2πizj
N
Y
i
(zi)pmi
N
Y
i̸=j
t−|mi−mj|/2q−R|mi−mj|/4 ×

1 −q|mi−mj|/2 zi
zj
 N
Y
i̸=j
 zj
zi t−1q|mi−mj|/2+1−R/2; q

∞

zi
zj tq|mi−mj|/2+R/2; q

∞
×
"
(t−1q1−R/2; q)∞
(tqR/2; q)∞
#N
.
(3.29)
Here R stands for the R-charge of the adjoint chiral multiplet Φ and the fugacity t is associated
to the U(1)β ﬂavor symmetry which acts on the adjoint chiral multiplet via Φ 7→eiθΦ. Using
some computer algebra (e.g. Mathematica) one can calculate explicitly I(q, t) as a series in q
up to a relatively high order. The coeﬃcients are polynomials in t, that is
I(q, t) ∈Z[t][[q]].
(3.30)
30In order for the background to be supersymmetric, one also needs to turn on a constant σ for the back-
ground gauge multiplet, which won’t aﬀect the analysis in this section.
– 31 –
For gauge group G = SU(2), the expression for the index simpliﬁes to
ISU(2)(q, t) = 1
2
X
m∈Z
Z
dz
2πiz z2pm t−2|m| q−2|m| (1 −z±2q|m|)
× (1/t; q)∞(z±2q|m|/t; q)∞
(qt; q)∞(z±2q|m|+1t; q)∞
(3.31)
where we use the standard notation
f(z±2) ≡f(z2)f(z−2).
(3.32)
The unreduced homological blocks can be calculated using the following formula [27]:
bZa(q, t) = ZT[M3](D2 ×q S1; a) =
1
|Wa|
1
(tq; q)N
∞
Z
|zi|=1
N
Y
i=1
dzi
2πizi
Y
i̸=j
(zi/zj; q)∞
(zi/zjtq; q)∞
ΘZN,p
a
(z; q),
(3.33)
where ΘZN;p
a
(z; q) is the theta function of the rank-N lattice ZN with quadratic form p · Id:
ΘZN;p
a
(z, q) =
X
n∈pZN+a
q
PN
i=1 n2
i /2p
N
Y
i=1
zni
i .
(3.34)
We would like to check that the following relation holds:
IU(N)(q, t) =
X
a∈ZN
p /SN
|Wa| bZa(q, t) bZa(1/q, 1/t).
(3.35)
Compared to the case p = 1 (M3 = S3) considered in section 3.1, there are now multiple
homological blocks. Another technical complication is that the formula (3.33) only deﬁnes
bZa(q, t) for |q| < 1, since the theta function is only given in terms of series convergent in
|q| < 1, with no canonical analytic continuation outside of the unit disk.
This problem will be resolved in section 3.2.4. For now, let us note that in the unreﬁned
case (t = 1) such problem does not appear because
bZa(q) =
bZa(q, t)
(tq; q)N
∞

t→1
=
1
|Wa|
Z
|zi|=1
N
Y
i=1
dzi
2πizi
Y
i̸=j
(1 −zi/zj) ΘZN,p
a
(z; q)
∈Z[q]
(3.36)
is just a polynomial and is obviously well-deﬁned for any |q| < ∞. Note, that the factorization
of the superconformal index in the unreﬁned case was essentially checked in [31]. There it
was shown that
IU(N)(q) =
X
a∈ZN
p /SN
|Wa|Za(q)Za(1/q)
(3.37)
– 32 –
where31
IU(N)(q) = IU(N)(q, t) · (tq; q)N
∞
(1/t; q)N
∞

t→1
(3.40)
and Za(q) = P
b Sab bZb(q) is as in (2.42), the contributions of ﬂat connection a to WRT
invariant/CS partition function on M3 = L(p, 1). Then
IU(N)(q) =
X
a∈ZN
p /SN
|Wa| bZa(q) bZa(1/q)
(3.41)
follows from (3.37) and S2 = Id (2.10) along with the symmetry
|Wa|Sab = |Wb|Sba.
(3.42)
