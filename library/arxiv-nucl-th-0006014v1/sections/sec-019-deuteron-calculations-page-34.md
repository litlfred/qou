---
doc_id: arxiv-nucl-th-0006014v1
doc_title: "The high-precision, charge-dependent Bonn nucleon-nucleon potential (CD-Bonn)"
section_id: sec-019-deuteron-calculations-page-34
section_title: "Deuteron calculations (page 34)"
section_number: null
pages: 34-34
source_pdf: 0006014v1.pdf
source_sha256: 208c7a6aaf628b30
toc_source: inferred
doc_brief: "The high-precision, charge-dependent Bonn nucleon-nucleon potential (CD-Bonn) — 56 sections: Front matter; Introduction; The model"
---
and the nucleon mass diﬀerence δM ≡Mn −Mp = 1.29332 MeV, and used Md = 2M −Bd.
From this we get
γ2 = MBd

1 −Bd
4M
 
1 −δM2
M2
d
!
,
(D9)
and, in terms of twice the reduced nucleon mass, c
M, which is deﬁned by
c
M ≡2MpMn
Mp + Mn
= M
 
1 −δM2
4M
2
!
= 938.91852 MeV ,
(D10)
we ﬁnally obtain
γ2 = c
MBd

1 −Bd
4M
 1 −δM2
M2
d
1 −δM2
4M
2
≈c
MBd

1 −Bd
4M

.
(D11)
The approximation involved in Eq. (D11) is good to one part in 109. Therefore, this equation
reproduces the exact value for γ to all digits given in Eq. (D6). One can now identify the
term c
MBd as the non-relativistic approximation to γ2 and the factor (1 −Bd/4M) as the
essential relativistic correction.
Partial wave decomposition of Eq. (D3) yields for the coupled 3S1 and 3D1 states,
ψ0(k) = −
c
M
γ2 + k2
Z ∞
0
dk′k′2 [V00(k, k′)ψ0(k′) + V02(k, k′)ψ2(k′)] ,
ψ2(k) = −
c
M
γ2 + k2
Z ∞
0
dk′k′2 [V20(k, k′)ψ0(k′) + V22(k, k′)ψ2(k′)] ,
(D12)
from which ψ0 and ψ2 are obtained. Considering a ﬁnite set of discrete arguments for the
functions on the l.h.s. and using the same set of momenta to discretize the integrals on the
r.h.s. produces a matrix equation that is solved easily by the matrix-inversion method [101].
The momentum-space wave funtions can be Fourier transformed into the conﬁguration-
space wave functions u and w by
uL(r)
r
=
s
2
π
Z ∞
0
dkk2jL(kr)ψL(k) ,
(D13)
with u0(r) ≡u(r), u2(r) ≡w(r), and jL the spherical Bessel functions. The normalization
is
Z ∞
0
dr
h
u2(r) + w2(r)
i
= 1.
(D14)
The asymptotic behavior of the wave functions for large values of r are
u(r) ∼ASe−γr,
w(r) ∼ADe−γr
"
1 +
3
(γr) +
3
(γr)2
#
,
(D15)
