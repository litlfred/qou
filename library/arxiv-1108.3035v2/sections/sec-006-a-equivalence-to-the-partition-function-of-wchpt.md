---
doc_id: arxiv-1108.3035v2
doc_title: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition"
section_id: sec-006-a-equivalence-to-the-partition-function-of-wchpt
section_title: "A Equivalence to the partition function of WchPT"
section_number: null
pages: 19-20
source_pdf: 1108.3035v2.pdf
source_sha256: 935bf1bd3e13821b
toc_source: outline
doc_brief: "Random Matrix Theory for the Hermitian Wilson Dirac Operator and the chGUE – GUE Transition — We introduce a random two-matrix model interpolating between a chiral Hermitian (2n + ν) × (2n+ν) matrix"
---
Equivalence to the partition function of WchPT
In this appendix we show the equivalence of our matrix model in the microscopic limit to WchPT in
the epsilon regime, as it was displayed in eq. (2.7). For non-degenerate parameters we have
Z(Nf )
ν
∼
Z
dAdBdWdΩ
Nf
Y
f=1
det
 (zf + mf)11n + A
W + Ω
W † + Ω†
(zf −mf)11n+ν + B

e
−
1
2(1−a2)Tr(W W †)
×e−
1
4a2 Tr(A2+B2+2ΩΩ†) .
(A.1)
Deﬁning z±
f ≡zf±mf we now express the determinants as integrals over Nf sets of complex Grassmann
variables ηf
i , i = 1, . . . , n and ψf
b , b = 1, . . . , n + ν,
Nf
Y
f=1
det[. . .]
=
Z
d2ηd2ψeη∗f
i
(z+
f δij+Aij)ηf
j +ψ∗f
b
(W †
bj+Ω†
bj)ηf
i +η∗f
i
(Wib+Ωib)ψf
b +ψ∗f
c
(z−
f δcb+Bcb)ψf
b , (A.2)
using summation conventions in all indices.
A completion of the squares and integration of the
Gaussian matrices yields
Z(Nf )
ν
∼
Z
d2ηd2ψ ez+
f η∗f
i
ηf
i +z−
f ψ∗f
b
ψf
b −a2
(η∗f
i
ηf
i )2+(ψ∗f
b
ψf
b )2
−2ψ∗f
b
ψf
b η∗g
i
ηg
i
=
Z
dQ1dQ2dT det[Z+ −i
√
2(aQ1 + T †)]n det[Z−−i
√
2(aQ2 + T)]n+νe−Tr(TT †+Q2
1+Q2
2) .
(A.3)
Here we have introduced two Hermitian matrices Q1,2 and one complex non-Hermitian matrix T
of size Nf × Nf to do the Hubbard-Stratonovich transformation.
Integrating out all Grassmann
variables yields an exact expression containing the diagonal matrices Z± with elements z±
f (up to
some constant prefactors that we dropped). If we parametrise T = UR with U unitary and R positive
deﬁnite Hermitian the saddle point is taken at R ∼11Nf
√n when we employ the scaling of masses and
a indicated in eq. (2.9). We obtain
lim
n→∞Z(Nf )
ν
∼
Z
dQ1dQ2
Z
dU det[U]νe
i
2Tr( ˆZ+U+ ˆZ−U†)+
√
2ˆa2Tr(Q1U+Q2U†)−1
2Tr(Q2
1+Q2
2)
∼
Z
dU det[U]ν exp
h1
2Tr( ˆ
M(U + U †)) + 1
2Tr( ˆZ(U −U †)) −ˆa2Tr(U 2 + U † 2)
i
,(A.4)
after integrating out the matrices Q1,2 and performing a further rotation U →iU, U † →−iU †. Eq.
(A.4) is the partition function of WchPT in the epsilon regime for non-degenerate masses, hence we
have completed our claimed proof.
