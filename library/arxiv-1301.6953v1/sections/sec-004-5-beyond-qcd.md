---
doc_id: arxiv-1301.6953v1
doc_title: "LU TP 13-03 Januray 2013"
section_id: sec-004-5-beyond-qcd
section_title: "Beyond QCD"
section_number: 5
pages: 8-10
source_pdf: 1301.6953v1.pdf
source_sha256: 8c9231d0832df3b6
doc_brief: "LU TP 13-03 Januray 2013 — 12 sections: Chiral Perturbation Theory; Introduction; Determining low-energy-constants i"
---
The methods of effective ﬁeld theory and in particular ChPT can also be used for extensions. A
simple extension is to take QCD withN light ﬂavours but one can also envisage usingN fermions in
different representations of the gauge group. The represen tations can be complex, real or pseudo-
real so we have in general three generic cases to study for the spontaneous breaking of the global
8
Chiral Perturbation Theory and Mesons Johan Bijnens
 0.7
 0.8
 0.9
 1
 1.1
 1.2
 0  0.2  0.4  0.6  0.8  1  1.2  1.4
f+(q2)
q2 [GeV2]
f+ D→π
f+ D→ K
 0.7
 0.8
 0.9
 1
 1.1
 1.2
 0  0.2  0.4  0.6  0.8  1  1.2  1.4
f+(q2)
q2 [GeV2]
f+ D→π FD→ K/FD→π
f+ D→ K
Figure 4: The left plot shows the form-factor f+ in D → πeν and D → Keν decays from CLEO [46]. In the
right hand side theD → Keν has been corrected with the chiral logarithms viaf+D→π = f+D→KFD→π/FD→K
[42].
symmetries [47, 48]
SU(N) × SU(N) → SU(N), SU(2N) → SO(2N), SU(2N) → Sp(2N) . (5.1)
The cases correspond to a complex, real and pseudo-real repr esentation for the N fermions. The
global symmetry group in the latter two cases isSU(2N) since both fermion and antifermion are in
the same representation of the gauge group. Many one-loop re sults existed especially for the ﬁrst
case, the equal mass case has been pushed to two-loop order in [49 – 51]. The main observation
[49] is that the whole machinery developed for ChPT can be brought over with a few simple mod-
iﬁcations to the three cases given above. This allowed us to p erform the calculations for the mass
and decay constants [49], meson-meson scattering [50] and t he electroweak precision parameters
[51]. The main idea was that lattice calculation can use our formulas to extrapolate to the massless
case, see e.g. [52].
The main trick involved is that in all cases mesons can be desc ribed by a unitary matrix U =
exp(i
φaX a/(
√
2F)) with the X a a different set of generators for the three cases. All ﬂavour sums
in the equal mass case can be done using the relations
⟨X aAX aB⟩ = ⟨A⟩⟨B⟩ − 1
NF
⟨AB⟩, ⟨X aA⟩⟨X aB⟩ = ⟨AB⟩ − 1
NF
⟨A⟩⟨B⟩.
⟨X aAX aB⟩ = ⟨A⟩⟨B⟩
2 + 1
2 ⟨AJSBT JS⟩ −⟨AB⟩
2NF
, ⟨X aA⟩⟨X aB⟩ = 1
2 ⟨AB⟩+ 1
2 ⟨AJSBT JS⟩ −⟨A⟩⟨B⟩
2NF
.
⟨X aAX aB⟩ = ⟨A⟩⟨B⟩
2 + 1
2 ⟨AJABT JA⟩ −⟨AB⟩
2NF
, ⟨X aA⟩⟨X aB⟩ = 1
2 ⟨AB⟩ −1
2 ⟨AJABT JA⟩ −⟨A⟩⟨B⟩
2NF
.
(5.2)
The lines are for the complex, real and pseudo-real case and JS =
(
0 I
I 0
)
, JA =
(
0 −I
I 0
)
.
9
Chiral Perturbation Theory and Mesons Johan Bijnens
QCD Adjoint 2-colour
aV n − 1
n n + 1
2 − 1
2n n − 1
2 − 1
2n
bV 16nLr
6 + 8Lr
8 + 4Hr
2
32nLr
6 + 8Lr
8 + 4Hr
2
32nLr
6 + 8Lr
8 + 4Hr
2
cV 3
2
(
−1 + 1
n2
) 3
8
(
−1 + 1
n2 − 2
n + 2n
) 3
8
(
−1 + 1
n2 + 2
n − 2n
)
dV −24
(
n2 − 1
)(
LA + LB
n
)
−12
(
2n2 + n − 1
)(
2LA + LB
n
)
−12
(
2n2 − n − 1
)(
2LA + LB
n
)
eV 1 − 1
n2
1
4
(
1 − 1
n2 + 2
n − 2n
) 1
4
(
1 − 1
n2 − 2
n + 2n
)
fV 48
(
Kr
25 + nKr
26 + n2Kr
27
)
rr
VA rr
V T
gV 8
(
n2 − 1
)(
LA + 1
nLB
)
4
(
2n2 + n − 1
)(
2LA + 1
nLB
)
4
(
2n2 − n − 1
)(
2LA + 1
nLB
)
Table 3: The coefﬁcients appearing the corrections to the vacuum-ex pectation-value for the three generic
cases with n ﬂavours. Table from [49]. We have deﬁned the abbreviationsLA = Lr
4 − 2Lr
6 and LB = Lr
5 − 2Lr
8.
As an example I quote the results for the vacuum expectation value ⟨¯qq⟩ for all three cases.
⟨
qq⟩ = ⟨qq⟩LO + ⟨qq⟩NLO + ⟨qq⟩NNLO .
⟨qq⟩LO ≡ ∑
i=1,NF
⟨qRiqLi + qLiqRi⟩LO = −NFB0F2
⟨qq⟩NLO = ⟨qq⟩LO
(
aV
A(M2)
F 2 + bV
M2
F2
)
,
⟨qq⟩NNLO = ⟨qq⟩LO
(
cV
A(M2)2
F4 + M2A(M2)
F4
(
dV + eV
16π2
)
+ M4
F4
(
fV + gV
16π2
) )
. (5.3)
I used here M2 = 2B0 ˆm and A(M2) = − M2
16π2 log M2
μ2 . The coefﬁcients appearing are given in Tab. 3.
Note the similarity between the different results and the existence of a number of large n relations
between the various cases [49].
