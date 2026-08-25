---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-017-311-categorifying-the-index
section_title: "Categorifying the index"
section_number: 3.1.1
pages: 29-30
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
As T [S3,U (N)] is dual to a system of free chirals, its space of BPS states on S2 — which
gives the homological invariant associated with M3 =S3 — factorizes as product
H(S3) = H2⊗H 4⊗... ⊗H 2N, (3.11)
whereH2i is the BPS Hilbert space of a single 3d N = 2 chiral multiplet with R-charge 2 i
and U(1)β ﬂavor chargei. Thus, we now turn to the problem of categorifying the index of a
free chiral multiplet.
Recall that for a 3d N = 2 chiral multiplet Φ of R-charge r and ﬂavor charge f, the
superconformal index — equal to the equivariant Euler characteristic of the BPS Hilbert
spaceHr,f — is given by
Ir(q,t ) =χq,t(Hr,f) =
∑
i,j,𝓁∈Z
qit𝓁(−1)j dimHi,j;𝓁
r,f =
∞∏
j=0
1−t−fq1−r/2+j
1−tfqr/2+j . (3.12)
Each term in this product corresponds to a generator of the BPS Hilbert space Hr,f. One
can identify the denominator of ( 3.12) as the contribution of the bosonic modes ∂jφ, and the
numerator as the contribution of the fermionic modes ∂jψ+. Then Hr,f is freely generated
by these generators as a supercommutative algebra,
Hr,f = C[xi,ξi] ∼= Ω•(Sym∞(C)) (3.13)
with an inﬁnite set of even generatorsx0, x1, x2, ... and odd generatorsξ0, ξ1, ξ2, ... coming
from
xi ←→ ∂jφ, (3.14)
ξi ←→ ∂jψ+.
In fact, this result has already appeared in math and physics literature (see e.g. [27, 58] and
references therein), and it is isomorphic to the colored HOMFLY-PT homology of the unknot.
The charges of the generators are summarized below
R F j3 R
2 +j3
φ r 1 0 r
2
ψ+ 1−r −1 1
2 1− r
2
∂+ 0 0 1 1
∂jφ r 1 j r
2 +j
∂jψ+ 1−r −1 1
2 +j 1− r
2 +j
.
HereR andF are generators of the R-symmetry U(1)R and the ﬂavor symmetry U(1)β, and
j3 generates a U(1) subgroup of the SU (2) isometry of the S2. Using this data, one can also
obtain the Poincar´ e polynomial ofHi,j;𝓁
r,f
Pr(q,z,t ) =
∑
i,j,𝓁∈Z
qizjt𝓁 dimHi,j;𝓁
r,f =
∞∏
j=0
1 +z1−rt−fq1−r/2+j
1−zrtfqr/2+j . (3.15)
– 28 –
One interesting observation of [27] is that, for some simple 3-manifolds M3, it is often
the case that one can trade the 𝓁-grading for the homological j-grading, making the Poincar´ e
polynomial eﬀectively computable. This phenomenon can be seen at the level of Hr,f for a
single chiral. Indeed, the ( i,j,𝓁 )-degrees of the generators are not independent, and under
the substitution of variables zr→tf and z→− 1, the Poincar´ e polynomial for the ﬁrst two
gradings becomes ( 3.12),
Pr(q,z, 1) =
∞∏
j=0
1 +z1−rq1−r/2+j
1−zrqr/2+j ↝ Pr(q,−1,t ) =Ir(q,t ) =
∞∏
j=0
1−t−fq1−r/2+j
1−tfqr/2+j .
The homology ( 3.13) obtained from the index has the same form as the homology on
D2×q S1 found in [27]. This could be justiﬁed by the following argument. The geometry
S1×S2 is conformally ﬂat, and the SUSY variation is obtain from that on ﬂat space. The
latter, in turn, is equivalent to partially A-twisted 3d N = 2 theory, which is precisely the
setting of [27].
