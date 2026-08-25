---
doc_id: arxiv-2507.13873v1
doc_title: "Probing the singularity at the holographic screen via q-holography"
section_id: sec-011-sinh-dilaton-gravity-quantization
section_title: "Sinh dilaton gravity quantization"
section_number: null
pages: 31-44
source_pdf: 2507.13873v1.pdf
source_sha256: fa1d38d08dc4976a
doc_brief: "Probing the singularity at the holographic screen via q-holography — We study the emergence ofq-deformed spacetime in a lower-dimensional gravitational system whose asymptotic region geometrizes the"
---
In order to be self-contained, we follow here a more direct approach based on the canonical
phase space quantization of the theory, which will allow us to directly identify the boundary
dynamics and the associated symmetry algebra. A similar analysis was carried out for sine
dilaton gravity in [59, 60], so we will not repeat the full set of equations here, but rather
summarize the key steps leading to the derivation of the gravitational Hamiltonian forsinh
dilaton gravity.
The above formulation of the action (3.1) is convenient to directly take the JT limit as
b→ 0. Here it is convenient to rescaleπb2Φ→ Φ and take the latter to beΦ∼ 1, such that
the whole action is multiplied by1/b2, and theb parameter governs the semiclassical saddle
as ℏ∼b2:
S =− 1
πb2
1
2
Z
M
d2x√g (ΦR + sinh(2Φ))+
I
∂M
dτ
√
h

ΦK−
r
cosh(2Φ)− 1
2

. (B.18)
This leads to an effective rescaled dilaton potentialV (Φ)→ πb2V (Φ). The corresponding
rescaled energy and temperature can be deduced from the generic thermodynamic relations
E = cosh(2Φh)
4πb2 , β = 4π
sinh(2Φh). (B.19)
In performing canonical quantization of general dilaton gravities, an apparent difficulty
arises from the fact that there is no unique geodesic connecting two arbitrary boundary
points [102]. To address this, in our case it is more natural to consider geodesic distances
measured in a Weyl-rescaled geometryds2
eff = ds2e−2Φ. Writing the metric in conformal
gauge as ds2 = ds2
flate2ρ, this effective metric
ds2
eff = ds2e−2Φ = ds2
flate2ρ−2Φ = ds2
flate2bφ, (B.20)
30
corresponds to the one associated with the Liouville fieldφ in the original Liouville grav-
ity formulation. Indeed the Liouville equation admits AdS2 conformal factors as classical
solutions. This leads to an effective AdS2 black hole geometry in which the renormalized
geodesic lengthL between the two boundaries is well-defined:
L =
Z
geodesic
dseff =
Z
geodesic
dsflatebφ. (B.21)
A canonical transformation is then performed in phase space, replacing the original vari-
ables, namely the ADM energyEADM and its conjugate two-sided boundary time coordinate
T, with a new pair: the renormalized Einstein-Rosen bridge lengthL (B.21) and its conju-
gate momentumP. Specifically, one requires the canonical symplectic form in the original
coordinates to be of the formω = dT∧ dEADM. Upon rescaling the coordinates to obtain
a nice saddle, we have
ω = dT∧ dEADM = sinh(2Φh)
2πb2 dT∧ dΦh = 1
2πb2 dP∧ dL, (B.22)
such that after quantization,πb2 takes the role ofℏ. One can easily prove that the canonical
transformations which ensure (B.22) are
L = 2 log
cosh (T sinh(2Φh)/4)
sinh(2Φh)

,
P =− log [cosh(2Φh) + sinh(2Φh) tanh (T sinh(2Φh)/4)],
(B.23)
where L is indeed the length of a Cauchy slice in a two-sided AdS2 black hole at the same
inverse temperature as the original sinh dilaton gravity black hole.
We now invert the relations (B.23) and express the gravity Hamiltonian (3.3) in terms
of the new phase space variablesL and P, obtaining:
4πb2HADM = cosh(P ) +e−LeP
2 . (B.24)
A remarkable feature is that, by performing a Legendre transform of the Hamiltonian (B.24),
one obtains the action of the so-calledq-Liouville system. The latter is part of a more
general theory, consisting of three coordinatesxa = (L/2,β,γ ) and three corresponding
momenta pa = (P,pβ,pβ), known as theq-Schwarzian [36, 35]. This six-dimensional phase
space reduces to the two-dimensional phase space of the system (B.24) upon imposing two
constraints, which were interpreted as Brown–Henneaux boundary conditions at the two
asymptotic boundaries of the two-sided gravitational system [36, 35]. Theq-Schwarzian
system has classically 6 conserved charges which, upon quantization, satisfy two copies
of the SLq(2) algebra (A.20). In conclusion, by showing that the boundary dynamics of
31
Liouville gravity reduce to the constrained version (B.24) of theq-Schwarzian, which is
basically the simplest dynamical system encoding the desired symmetry algebra, we argue
that Liouville gravity may serve as a natural bulk gravitational dual capable of reproducing
the two-point function obtained in the main text.
All amplitudes in sinh dilaton gravity, and in particular the matter two-point function
we are interested in, can be obtained by quantizing the system (B.24). From the symplectic
form (B.22), the associated Poisson brackets{L,P} = 2πb2, become upon quantization
[L,P ] = 2πib2ℏ. Setting ℏ≡ 1 by absorbing it in the definitionπb2ℏ→πb2, we see thatb2
effectively governs the semiclassical regime. By realizing the canonical commutation relation
by settingP =−2πib2 d
dL, the Schrödinger equation associated with the Hamiltonian (B.24)
becomes
ψs(L/2 +iπb2) +

1 +eiπb2
e−L

ψs(L/2−iπb2) = 2 cosh(2πbs)ψs(L/2), (B.25)
where, for convenience, we have introduced a new energy variablesΦh =πbs. The additional
factor e2πib2
is an order ambiguity in the quantization procedure. This difference equation
appeared before within the context of the relativistic Toda chain [91]. The solution to this
difference equation (B.25) is known and becomes unique once we require it to also satisfy the
dual equation obtained by the transformationb→ 1/b.14 This requirement is not manifest
at the level of the classical action, which is not invariant under this duality, but it emerges
in the structure of the quantum amplitudes of Liouville gravity [25, 27].15 The boundary-to-
boundary propagator of a matter scalar field in the bulk of sinh dilaton gravity is dual to the
insertion of the operatore−∆L in theq-Liouville path integral [36]. Once the gravitational
eigenfunctions are known, the matrix element of this operator between two fixed energy
states s1 and s2 can be computed, yielding:
Z +∞
−∞
dϕ ψs1(ϕ)ψ∗
s2(ϕ)e−2∆ϕ = Sb(b∆±is1±is2)
Sb(2b∆) , (B.27)
where the shorthand notationa±b±c indicates the product over all combinations of signs.
Taking the limit∆→ 0 the expression above reduces to the orthogonality relation between
14For completeness, the solution is given by [91, 25, 27]
ψs(L/2) =e−isL/b
Z
C
dξSb(−iξ)Sb(−iξ− 2is)e−πi(ξ2+2sξ)e−iξL/b, (B.26)
whereC denotes an appropriate integration contour.
15Liouville gravity has a quantum group theoretic description in terms of the modular double
Uq(sl(2, R))⊗U˜q(sl(2, R)) Hopf algebra [27, 103], building on the same structure present in 2d Liouville
CFT [98, 99].
32
the eigenfunctions, from which one can extract the Liouville gravity density of states:
ρ(s) = sinh(2πbs) sinh
2πs
b

. (B.28)
These two ingredients form the fundamental building blocks of the Liouville gravity two-
point function (3.9) and the partition function (3.6).
C Useful manipulations involving Ramanujan’s formula
A crucial identity for this work is Ramanujan’s summation formula:
Z
R
dτe−2πβτeπ(Q−α)τe−iπ
2 α(Q−α)eiπαβSb(iτ +α)Sb(−iτ) = Sb(α)Sb(β)
Sb(α +β) . (C.1)
We now aim to rewrite it in a way that will be useful to us. The argument has poles of
Sb(−iτ) atτ =−inb−im/b and atτ =iα +inb +im/b forSb(iτ +α). The contour avoids
the pole atτ = 0 from above. Deforming the contour toτ→τ−iα/2, we can rewrite this
formula suggestively as
Z
R
dτe−2πβτeπ(Q−α)τSb(α/2±iτ)
Sb(α) = Sb(β)
Sb(α +β). (C.2)
Moreover, a useful rewriting of the exact Liouville gravity two-point function (3.9) can be
achieved by exploiting the following version of Ramanujan’s formula (C.2):
Z +∞
−∞
dpe2πipxSb(ip +Q/2−βM)
Sb(ip +Q/2 +βM) = Sb(βM±ix)
Sb(2βM) . (C.3)
By applying (C.3) twice, we can express the product of double sine functions appearing in
(3.9) in Fourier space and exchange the order of integrals, performing the integrals overs1
and s2 first. An equivalent manipulation was performed in the case of JT gravity in [104].
The integrals overs1 and s2 can be done using the following integral representation of the
modified Bessel function:
Kν(z) =
Z +∞
0
e−z cosh(t) cosh(νt)dt. (C.4)
After some manipulations, the Liouville gravity two-point function (3.9) can then be rewrit-
ten as
AβM (τ1,τ 2) = C∆
τ(β−τ)
Z +∞
−∞
dp
Z +∞
−∞
dqSb(ip/b +Q/2−βM)
Sb(ip/b +Q/2 +βM)
Sb(iq/b +Q/2−βM)
Sb(iq/b +Q/2 +βM)
q2− (p−i)2

K 1
b2 (1+i(p+q))(κτ)K 1
b2 (1+i(p−q))(κ(β−τ)),
(C.5)
33
where we setβM = ∆b and the constantC∆ = Sb(2∆b)
b4(πb2)2κ2.
A remarkable simplification of the above formula happens when∆∈ 1
2 N. For instance,
using the propertySb(x +b) = 2 sin(πbx)Sb(x) iteratively, the ratio ofSb functions reduces
to Sb(ip/b +Q/2−βM)
Sb(ip/b +Q/2 +βM) = 1
22∆ cosh(πp)Q∆− 1
2
j=1 cosh (πp±iπb2j)
(C.6)
when ∆ is an half integer, and to
Sb(ip/b +Q/2−βM)
Sb(ip/b +Q/2 +βM) = 1
22∆Q∆−1
k=0 cosh (πp±iπb2(k + 1/2))
(C.7)
when ∆ is an integer, wherej and k in (C.6) and (C.7) run over integer values.
Moreover, when ∆∈ 1
2 N, one of the two integrals in (C.5) can be computed in closed
form. Indeed, one can shift the contour forp from the real line to the line atp +i in the
complexp plane and notice the second line in (C.5) is antisymmetric in the exchangep↔q.
On the other hand, one has on the first line
Sb(ip/b +Q/2−βM)
Sb(ip/b +Q/2 +βM)→ Sb(ip/b +Q/2−βM)
Sb(ip/b +Q/2 +βM)× cos (πip/b2 +π/2b2 +πh)
cos (πip/b2 +π/2b2−πh), (C.8)
which indeed is invariant, up to a factor of(−1)∆, when ∆∈ 1
2 N. One can check this also
using the explicit forms in (C.6) and (C.7). This property implies the full integrand in (C.5)
is antisymmetric inp↔ q on the shifted contour and therefore the integral vanishes on
that contour. By applying Cauchy’s theorem, the integral overp can then be evaluated by
summing the residues of the poles located within the rectangular region bounded by the
lines Re(p) = 0 and Re(p) =i.
When ∆ = 1/2, we just get the residue atp =i/2, yielding:
Ab/2(τ1,τ 2) = 1
b4
Sb(b)
(8πb2)2κ2τ(β−τ)
Z +∞
−∞
dq 1 + 4q2
cosh (πq) K 1
b2 ( 1
2 +iq)(κτ)K 1
b2 ( 1
2−iq)(κ(β−τ)),
(C.9)
so the original integral has simplified enormously. A possible rewriting of this formula can
also be achieved using the formula:
Z +∞
−∞
eiρx Kν+ix(α)Kν−ix(β)dx =π
αeρ +β
α +βeρ
ν
K2ν
p
α2 +β2 + 2αβ cosh(ρ)

. (C.10)
In fact one can write
 
4q2 + 1

sech(πq) = 1
π
Z +∞
−∞
dx sech3
x
2

eiqx, (C.11)
34
exchange the integrals and use (C.10) to get
Ab/2(τ1,τ 2) = 1
b4
Sb(b)
(8πb2)2κ2τ(β−τ)
Z +∞
−∞
dx 1
cosh3  x
2b2

 τex +β−τ
τ + (β−τ)ex
 1
2b2
×
×K 1
b2

κ
p
τ 2 + (β−τ)2 + 2τ(β−τ) cosh(x)

.
(C.12)
Similar expressions can be obtained for∆ = 1, 3/2, 2,··· , where one just needs to pick more
residues for evaluating the integral overp, since according to (C.6) and (C.7) there are more
poles located in the rectangular region bounded by the linesRe(p) = 0 and Re(p) =i.
References
[1] J. M. Maldacena, “The LargeN limit of superconformal field theories and
supergravity,” Adv. Theor. Math. Phys. 2 (1998) 231–252, arXiv:hep-th/9711200.
[2] A. Giveon and D. Kutasov, “Little string theory in a double scaling limit,”JHEP 10
(1999) 034, arXiv:hep-th/9909110.
[3] I. R. Klebanov and M. J. Strassler, “Supergravity and a confining gauge theory:
Duality cascades and chi SB resolution of naked singularities,”JHEP 08 (2000) 052,
arXiv:hep-th/0007191.
[4] I. Kanitscheider, K. Skenderis, and M. Taylor, “Precision holography for
non-conformal branes,” JHEP 09 (2008) 094, arXiv:0807.3324 [hep-th] .
[5] M. Taylor, “Lifshitz holography,”Class. Quant. Grav. 33 no. 3, (2016) 033001,
arXiv:1512.03554 [hep-th] .
[6] R. Jackiw, “Lower Dimensional Gravity,”Nucl. Phys. B 252 (1985) 343–356.
[7] C. Teitelboim, “Gravitation and Hamiltonian Structure in Two Space-Time
Dimensions,” Phys. Lett. B 126 (1983) 41–45.
[8] A. Almheiri and J. Polchinski, “Models of AdS2 backreaction and holography,”
JHEP 11 (2015) 014, arXiv:1402.6334 [hep-th] .
[9] K. Jensen, “Chaos in AdS2 Holography,” Phys. Rev. Lett. 117 no. 11, (2016) 111601,
arXiv:1605.06098 [hep-th] .
35
[10] J. Maldacena, D. Stanford, and Z. Yang, “Conformal symmetry and its breaking in
two dimensional Nearly Anti-de-Sitter space,”PTEP 2016 no. 12, (2016) 12C104,
arXiv:1606.01857 [hep-th] .
[11] J. Engelsöy, T. G. Mertens, and H. Verlinde, “An investigation of AdS2 backreaction
and holography,” JHEP 07 (2016) 139, arXiv:1606.03438 [hep-th] .
[12] J. S. Cotler, G. Gur-Ari, M. Hanada, J. Polchinski, P. Saad, S. H. Shenker,
D. Stanford, A. Streicher, and M. Tezuka, “Black Holes and Random Matrices,”
JHEP 05 (2017) 118, arXiv:1611.04650 [hep-th] . [Erratum: JHEP 09, 002
(2018)].
[13] D. Stanford and E. Witten, “Fermionic Localization of the Schwarzian Theory,”
JHEP 10 (2017) 008, arXiv:1703.04612 [hep-th] .
[14] A. Kitaev and S. J. Suh, “Statistical mechanics of a two-dimensional black hole,”
JHEP 05 (2019) 198, arXiv:1808.07032 [hep-th] .
[15] T. G. Mertens, G. J. Turiaci, and H. L. Verlinde, “Solving the Schwarzian via the
Conformal Bootstrap,” JHEP 08 (2017) 136, arXiv:1705.08408 [hep-th] .
[16] T. G. Mertens, “The Schwarzian theory — origins,”JHEP 05 (2018) 036,
arXiv:1801.09605 [hep-th] .
[17] H. T. Lam, T. G. Mertens, G. J. Turiaci, and H. Verlinde, “Shockwave S-matrix
from Schwarzian Quantum Mechanics,”JHEP 11 (2018) 182, arXiv:1804.09834
[hep-th].
[18] D. Harlow and D. Jafferis, “The Factorization Problem in Jackiw-Teitelboim
Gravity,” JHEP 02 (2020) 177, arXiv:1804.01081 [hep-th] .
[19] A. Kitaev, “Talks given at the Fundamental Physics Prize Symposium and KITP
seminars,”.
[20] S. Sachdev and J. Ye, “Gapless spin fluid ground state in a random, quantum
Heisenberg magnet,” Phys. Rev. Lett. 70 (1993) 3339, arXiv:cond-mat/9212030.
[21] P. Saad, S. H. Shenker, and D. Stanford, “JT gravity as a matrix integral,”
arXiv:1903.11115 [hep-th] .
[22] P. Nayak, A. Shukla, R. M. Soni, S. P. Trivedi, and V. Vishal, “On the Dynamics of
Near-Extremal Black Holes,”JHEP 09 (2018) 048, arXiv:1802.09547 [hep-th] .
36
[23] L. V. Iliesiu and G. J. Turiaci, “The statistical mechanics of near-extremal black
holes,” JHEP 05 (2021) 145, arXiv:2003.02860 [hep-th] .
[24] H. Kyono, S. Okumura, and K. Yoshida, “Comments on 2D dilaton gravity system
with a hyperbolic dilaton potential,”Nucl. Phys. B 923 (2017) 126–143,
arXiv:1704.07410 [hep-th] .
[25] T. G. Mertens and G. J. Turiaci, “Liouville quantum gravity – holography, JT and
matrices,” JHEP 01 (2021) 073, arXiv:2006.07072 [hep-th] .
[26] T. G. Mertens, “Degenerate operators in JT and Liouville (super)gravity,”JHEP 04
(2021) 245, arXiv:2007.00998 [hep-th] .
[27] Y. Fan and T. G. Mertens, “From quantum groups to Liouville and dilaton quantum
gravity,” JHEP 05 (2022) 092, arXiv:2109.07770 [hep-th] .
[28] K. Suzuki and T. Takayanagi, “JT gravity limit of Liouville CFT and matrix model,”
JHEP 11 (2021) 137, arXiv:2108.12096 [hep-th] .
[29] S. Collier, L. Eberhardt, B. Mühlmann, and V. A. Rodriguez, “The Virasoro
minimal string,” SciPost Phys. 16 no. 2, (2024) 057,arXiv:2309.10846 [hep-th] .
[30] M. Berkooz, P. Narayan, and J. Simon, “Chord diagrams, exact correlators in spin
glasses and black hole bulk reconstruction,”JHEP 08 (2018) 192,
arXiv:1806.04380 [hep-th] .
[31] M. Berkooz, M. Isachenkov, V. Narovlansky, and G. Torrents, “Towards a full
solution of the large N double-scaled SYK model,”JHEP 03 (2019) 079,
arXiv:1811.02584 [hep-th] .
[32] H. W. Lin, “The bulk Hilbert space of double scaled SYK,”JHEP 11 (2022) 060,
arXiv:2208.07032 [hep-th] .
[33] L. Susskind, “De Sitter Space, Double-Scaled SYK, and the Separation of Scales in
the Semiclassical Limit,”arXiv:2209.09999 [hep-th] .
[34] B. Bhattacharjee, P. Nandy, and T. Pathak, “Krylov complexity in large q and
double-scaled SYK model,” JHEP 08 (2023) 099, arXiv:2210.02474 [hep-th] .
[35] A. Blommaert, T. G. Mertens, and S. Yao, “Dynamical actions and q-representation
theory for double-scaled SYK,”arXiv:2306.00941 [hep-th] .
37
[36] A. Blommaert, T. G. Mertens, and S. Yao, “The q-Schwarzian and Liouville
gravity,” JHEP 11 (2024) 054, arXiv:2312.00871 [hep-th] .
[37] L. Susskind, “De Sitter Space has no Chords. Almost Everything is Confined.,”
JHAP 3 no. 1, (2023) 1–30,arXiv:2303.00792 [hep-th] .
[38] B. Mukhametzhanov, “Large p SYK from chord diagrams,”JHEP 09 (2023) 154,
arXiv:2303.03474 [hep-th] .
[39] M. Berkooz, Y. Jia, and N. Silberstein, “Parisi’s Hypercube, Fock-Space Frustration,
and Near-AdS2/Near-CFT1 Holography,”Phys. Rev. Lett. 132 no. 8, (2024) 081601,
arXiv:2303.18182 [hep-th] .
[40] K. Okuyama and K. Suzuki, “Correlators of double scaled SYK at one-loop,”JHEP
05 (2023) 117, arXiv:2303.07552 [hep-th] .
[41] H. Lin and L. Susskind, “Infinite Temperature’s Not So Hot,”arXiv:2206.01083
[hep-th].
[42] M. Berkooz, M. Isachenkov, M. Isachenkov, P. Narayan, and V. Narovlansky,
“Quantum groups, non-commutative AdS2, and chords in the double-scaled SYK
model,” JHEP 08 (2023) 076, arXiv:2212.13668 [hep-th] .
[43] A. Goel, V. Narovlansky, and H. Verlinde, “Semiclassical geometry in double-scaled
SYK,” arXiv:2301.05732 [hep-th] .
[44] V. Narovlansky and H. Verlinde, “Double-scaled SYK and de Sitter Holography,”
arXiv:2310.16994 [hep-th] .
[45] H. Verlinde and M. Zhang, “SYK Correlators from 2D Liouville-de Sitter Gravity,”
arXiv:2402.02584 [hep-th] .
[46] M. Berkooz, N. Brukner, Y. Jia, and O. Mamroud, “From Chaos to Integrability in
Double Scaled Sachdev-Ye-Kitaev Model via a Chord Path Integral,”Phys. Rev.
Lett. 133 no. 22, (2024) 221602,arXiv:2403.01950 [hep-th] .
[47] H. W. Lin and D. Stanford, “A symmetry algebra in double-scaled SYK,”SciPost
Phys. 15 no. 6, (2023) 234,arXiv:2307.15725 [hep-th] .
[48] H. Verlinde, “Double-scaled SYK, Chords and de Sitter Gravity,”
arXiv:2402.00635 [hep-th] .
38
[49] A. Almheiri and F. K. Popov, “Holography on the quantum disk,”JHEP 06 (2024)
070, arXiv:2401.05575 [hep-th] .
[50] A. Almheiri, A. Goel, and X.-Y. Hu, “Quantum gravity of the Heisenberg algebra,”
arXiv:2403.18333 [hep-th] .
[51] L. Bossi, L. Griguolo, J. Papalini, L. Russo, and D. Seminara, “Sine-dilaton gravity
vs double-scaled SYK: exploring one-loop quantum corrections,”arXiv:2411.15957
[hep-th].
[52] J. Xu, “Von Neumann Algebras in Double-Scaled SYK,”arXiv:2403.09021
[hep-th].
[53] J. Xu, “On Chord Dynamics and Complexity Growth in Double-Scaled SYK,”
arXiv:2411.04251 [hep-th] .
[54] M. P. Heller, J. Papalini, and T. Schuhmann, “Krylov spread complexity as
holographic complexity beyond JT gravity,”arXiv:2412.17785 [hep-th] .
[55] S. E. Aguilar-Gutierrez, “Towards complexity in de Sitter space from the
doubled-scaled Sachdev-Ye-Kitaev model,”JHEP 10 (2024) 107, arXiv:2403.13186
[hep-th].
[56] D. Tietto and H. Verlinde, “A microscopic model of de Sitter spacetime with an
observer,” arXiv:2502.03869 [hep-th] .
[57] S. E. Aguilar-Gutierrez, “Symmetry Sectors in Chord Space and Relational
Holography in the DSSYK,”arXiv:2506.21447 [hep-th] .
[58] M. Berkooz, T. Kukolj, and J. Seitz, “Comments on Class S(YK),”
arXiv:2507.12524 [hep-th] .
[59] A. Blommaert, T. G. Mertens, and J. Papalini, “The dilaton gravity hologram of
double-scaled SYK,” JHEP 06 (2025) 050, arXiv:2404.03535 [hep-th] .
[60] A. Blommaert, A. Levine, T. G. Mertens, J. Papalini, and K. Parmentier, “An
entropic puzzle in periodic dilaton gravity and DSSYK,”JHEP 07 (2025) 093,
arXiv:2411.16922 [hep-th] .
[61] A. Blommaert, A. Levine, T. G. Mertens, J. Papalini, and K. Parmentier,
“Wormholes, branes and finite matrices in sine dilaton gravity,”arXiv:2501.17091
[hep-th].
39
[62] S. Collier, L. Eberhardt, B. Mühlmann, and V. A. Rodriguez, “Complex Liouville
String,” Phys. Rev. Lett. 134 no. 25, (2025) 251602,arXiv:2409.17246 [hep-th] .
[63] S. Collier, L. Eberhardt, and B. Mühlmann, “A microscopic realization of dS3,”
SciPost Phys. 18 no. 4, (2025) 131,arXiv:2501.01486 [hep-th] .
[64] E. Witten, “Gravity and the crossed product,”JHEP 10 (2022) 008,
arXiv:2112.12828 [hep-th] .
[65] V. Chandrasekaran, R. Longo, G. Penington, and E. Witten, “An algebra of
observables for de Sitter space,”JHEP 02 (2023) 082, arXiv:2206.10780 [hep-th] .
[66] K. Jensen, J. Sorce, and A. J. Speranza, “Generalized entropy for general subregions
in quantum gravity,”JHEP 12 (2023) 020, arXiv:2306.01837 [hep-th] .
[67] L. Susskind, “Black Holes Hint towards De Sitter Matrix Theory,”Universe 9 no. 8,
(2023) 368, arXiv:2109.01322 [hep-th] .
[68] E. Shaghoulian, “The central dogma and cosmological horizons,”JHEP 01 (2022)
132, arXiv:2110.13210 [hep-th] .
[69] E. Shaghoulian and L. Susskind, “Entanglement in De Sitter space,”JHEP 08
(2022) 198, arXiv:2201.03603 [hep-th] .
[70] V. Franken, H. Partouche, F. Rondeau, and N. Toumbas, “Bridging the static
patches: de Sitter holography and entanglement,”JHEP 08 (2023) 074,
arXiv:2305.12861 [hep-th] .
[71] G. Penington, “Entanglement Wedge Reconstruction and the Information Paradox,”
JHEP 09 (2020) 002, arXiv:1905.08255 [hep-th] .
[72] A. Almheiri, N. Engelhardt, D. Marolf, and H. Maxfield, “The entropy of bulk
quantum fields and the entanglement wedge of an evaporating black hole,”JHEP 12
(2019) 063, arXiv:1905.08762 [hep-th] .
[73] T. Hartman and J. Maldacena, “Time Evolution of Entanglement Entropy from
Black Hole Interiors,”JHEP 05 (2013) 014, arXiv:1303.1080 [hep-th] .
[74] A. R. Brown, D. A. Roberts, L. Susskind, B. Swingle, and Y. Zhao, “Holographic
Complexity Equals Bulk Action?,”Phys. Rev. Lett. 116 no. 19, (2016) 191301,
arXiv:1509.07876 [hep-th] .
40
[75] D. Bernard and A. LeClair, “q Deformation of SU(1,1) Conformal Ward Identities
and q Strings,” Phys. Lett. B 227 (1989) 417–423.
[76] T. Matsuzaki and T. Suzuki, “A Representation of Uq(su(1, 1)) on the space of
quasiprimary fields and correlation functions,”Phys. Lett. B 296 (1992) 33–39.
[77] L. D. Faddeev, “Modular double of quantum group,” inConference Moshe Flato,
pp. 149–156. 2000. arXiv:math/9912078.
[78] C. Keeler and G. S. Ng, “Partition Functions in Even Dimensional AdS via
Quasinormal Mode Methods,” JHEP 06 (2014) 099, arXiv:1401.7016 [hep-th] .
[79] A. M. Polyakov, “Quantum Geometry of Bosonic Strings,”Phys. Lett. B 103 (1981)
207–210.
[80] J. Distler and H. Kawai, “Conformal Field Theory and 2D Quantum Gravity,”Nucl.
Phys. B 321 (1989) 509–527.
[81] F. David, “Conformal Field Theories Coupled to 2D Gravity in the Conformal
Gauge,” Mod. Phys. Lett. A 3 (1988) 1651.
[82] V. G. Knizhnik, A. M. Polyakov, and A. B. Zamolodchikov, “Fractal Structure of 2D
Quantum Gravity,” Mod. Phys. Lett. A 3 (1988) 819.
[83] L. Susskind and E. Witten, “The Holographic bound in anti-de Sitter space,”
arXiv:hep-th/9805114.
[84] J. Teschner and G. Vartanov, “6j symbols for the modular double, quantum
hyperbolic geometry, and supersymmetric gauge theories,”Lett. Math. Phys. 104
(2014) 527–551, arXiv:1202.4698 [hep-th] .
[85] L. Hadasz, M. Pawelkiewicz, and V. Schomerus, “Self-dual Continuous Series of
Representations forUq(sl(2)) andUq(osp(1|2)),” JHEP 10 (2014) 091,
arXiv:1305.4596 [hep-th] .
[86] J. Shiraishi, H. Kubo, H. Awata, and S. Odake, “A Quantum deformation of the
Virasoro algebra and the Macdonald symmetric functions,”Lett. Math. Phys. 38
(1996) 33–51, arXiv:q-alg/9507034.
[87] H. Awata, H. Kubo, S. Odake, and J. Shiraishi, “Quantum W(N) algebras and
Macdonald polynomials,” Commun. Math. Phys. 179 (1996) 401–416,
arXiv:q-alg/9508011.
41
[88] F. Nieri, S. Pasquetti, and F. Passerini, “3d and 5d Gauge Theory Partition
Functions asq-deformed CFT Correlators,”Lett. Math. Phys. 105 no. 1, (2015)
109–148, arXiv:1303.2626 [hep-th] .
[89] F. Nieri, S. Pasquetti, F. Passerini, and A. Torrielli, “5D partition functions,
q-Virasoro systems and integrable spin-chains,”JHEP 12 (2014) 040,
arXiv:1312.1294 [hep-th] .
[90] A. Nedelin, F. Nieri, and M. Zabzine, “q-Virasoro modular double and 3d partition
functions,” Commun. Math. Phys. 353 no. 3, (2017) 1059–1102,arXiv:1605.07029
[hep-th].
[91] S. Kharchev, D. Lebedev, and M. Semenov-Tian-Shansky, “Unitary representations
of Uq(sl(2, R)), the modular double, and the multiparticle q deformed Toda chains,”
Commun. Math. Phys. 225 (2002) 573–609, arXiv:hep-th/0102180.
[92] A. G. Bytsko and J. Teschner, “R operator, coproduct and Haar measure for the
modular double of U(q)(sl(2,R)),”Commun. Math. Phys. 240 (2003) 171–196,
arXiv:math/0208191.
[93] A. G. Bytsko and J. Teschner, “Quantization of models with non-compact quantum
group symmetry: Modular XXZ magnet and lattice sinh-Gordon model,”J. Phys. A
39 (2006) 12927–12981, arXiv:hep-th/0602093.
[94] V. Fateev, A. B. Zamolodchikov, and A. B. Zamolodchikov, “Boundary Liouville
field theory. 1. Boundary state and boundary two point function,”
arXiv:hep-th/0001012.
[95] J. Teschner, “Remarks on Liouville theory with boundary,”PoS tmr2000 (2000)
041, arXiv:hep-th/0009138.
[96] I. C.-H. Ip, “Representation of the quantum plane, its quantum double and harmonic
analysis onGL+
q (2,R ),” Selecta Mathematica New Series Vol 19 (4) (2013)
987–1082, arXiv:1108.5365 [math.QA] .
[97] A. Belaey, T. G. Mertens, and T. Tappeiner, “Quantum group origins of edge states
in double-scaled SYK,”arXiv:2503.20691 [hep-th] .
[98] B. Ponsot and J. Teschner, “Liouville bootstrap via harmonic analysis on a
noncompact quantum group,”arXiv:hep-th/9911110.
42
[99] B. Ponsot and J. Teschner, “Clebsch-Gordan and Racah-Wigner coefficients for a
continuous series of representations of U(q)(sl(2,R)),”Commun. Math. Phys. 224
(2001) 613–655, arXiv:math/0007097.
[100] T. G. Mertens and G. J. Turiaci, “Solvable models of quantum black holes: a review
on Jackiw–Teitelboim gravity,”Living Rev. Rel. 26 no. 1, (2023) 4,
arXiv:2210.10846 [hep-th] .
[101] E. Witten, “Deformations of JT Gravity and Phase Transitions,”arXiv:2006.03494
[hep-th].
[102] J. Kruthoff and A. Levine, “Semi-classical dilaton gravity and the very blunt defect
expansion,” arXiv:2402.10162 [hep-th] .
[103] T. G. Mertens, “Quantum exponentials for the modular double and applications in
gravity models,” JHEP 09 (2023) 106, arXiv:2212.07696 [hep-th] .
[104] L. Griguolo, J. Papalini, and D. Seminara, “On the perturbative expansion of exact
bi-local correlators in JT gravity,”JHEP 05 (2021) 140, arXiv:2101.06252
[hep-th].
43
