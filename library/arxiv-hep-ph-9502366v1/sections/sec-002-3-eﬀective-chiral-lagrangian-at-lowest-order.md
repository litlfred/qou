---
doc_id: arxiv-hep-ph-9502366v1
doc_title: "Chiral Perturbation Theory"
section_id: sec-002-3-eﬀective-chiral-lagrangian-at-lowest-order
section_title: "Eﬀective chiral Lagrangian at lowest order"
section_number: 3
pages: 5-11
source_pdf: 9502366v1.pdf
source_sha256: 56df064956ca03f8
toc_source: inferred
doc_brief: "Chiral Perturbation Theory — An introduction to the basic ideas and methods of Chiral Perturbation Theory is presented."
---
The Goldstone nature of the pseudoscalar mesons implies strong constraints on
their interactions, which can be most easily analyzed on the basis of an eﬀective
Lagrangian. Since there is a mass gap separating the pseudoscalar octet from the rest
of the hadronic spectrum, we can build an eﬀective ﬁeld theory containing only the
Goldstone modes. Our basic assumption is the pattern of SCSB:
G ≡SU(3)L ⊗SU(3)R
SCSB
−→H ≡SU(3)V .
(3.1)
Let us denote φa (a = 1, . . ., 8) the coordinates describing the Goldstone ﬁelds in
the coset space G/H, and choose a coset representative ¯ξ(φ) ≡(ξL(φ), ξR(φ)) ∈G. The
change of the Goldstone coordinates under a chiral transformation g ≡(gL, gR) ∈G
is given by
ξL(φ)
G
−→gL ξL(φ) h†(φ, g) ,
ξR(φ)
G
−→gR ξR(φ) h†(φ, g) ,
(3.2)
where h(φ, g) ∈H is a compensating transformation which is needed to return to the
given choice of coset representative ¯ξ; in general, h depends both on φ and g. Since the
same transformation h(φ, g) occurs in the left and right sectors (the two chiral sectors
can be related by a parity transformation, which obviously leaves H invariant), we
can get rid of it by combining the two chiral relations in (3.2) into the simpler form
U(φ)
G
−→gR U(φ) g†
L ,
U(φ) ≡ξR(φ) ξ†
L(φ) .
(3.3)
Moreover, without lost of generality, we can take a canonical choice of coset
representative such that ξR(φ) = ξ†
L(φ) ≡u(φ). The 3 × 3 unitary matrix
U(φ) = u(φ)2 = exp
n
i
√
2Φ/f
o
(3.4)
gives a very convenient parametrization of the Goldstone ﬁelds
Φ(x) ≡⃗λ
√
2⃗φ =


1
√
2π0 +
1
√
6η8
π+
K+
π−
−1
√
2π0 +
1
√
6η8
K0
K−
¯K0
−2
√
6η8

.
(3.5)
Notice that U(φ) transforms linearly under the chiral group, but the induced
transformation on the Goldstone ﬁelds⃗φ is highly non-linear.
To get a low-energy eﬀective Lagrangian realization of QCD, for the light-quark
sector (u, d, s), we should write the most general Lagrangian involving the matrix
U(φ), which is consistent with chiral symmetry. The Lagrangian can be organized in
terms of increasing powers of momentum or, equivalently, in terms of an increasing
number of derivatives (parity conservation requires an even number of derivatives):
Leﬀ(U) =
X
n
L2n .
(3.6)
In the low-energy domain we are interested in, the terms with a minimum number of
derivatives will dominate.
Due to the unitarity of the U matrix, UU † = I, at least two derivatives are required
to generate a non-trivial interaction. To lowest order, the eﬀective chiral Lagrangian
is uniquely given by the term
L2 = f 2
4 ⟨∂µU †∂µU⟩,
(3.7)
where ⟨A⟩denotes the trace of the matrix A.
Expanding U(φ) in a power series in Φ, one obtains the Goldstone kinetic terms
plus a tower of interactions involving an increasing number of pseudoscalars.
The
requirement that the kinetic terms are properly normalized ﬁxes the global coeﬃcient
f 2/4 in equation (3.7). All interactions among the Goldstones can then be predicted
in terms of the single coupling f:
L2 = 1
2 ⟨∂µΦ∂µΦ⟩+
1
12f 2 ⟨(Φ
↔
∂µ Φ) (Φ
↔
∂µ Φ)⟩+ O(Φ6/f 4) .
(3.8)
To compute the ππ scattering amplitude, for instance, is now a trivial perturbative
exercise. One gets the well-known (Weinberg 1966) result [t ≡(p′
+ −p+)2]
T(π+π0 →π+π0) = t
f 2 .
(3.9)
Similar results can be obtained for ππ →4π, 6π, 8π, . . . The non-linearity of the
eﬀective Lagrangian relates amplitudes with diﬀerent numbers of Goldstone bosons,
allowing for absolute predictions in terms of f.
The eﬀective ﬁeld theory technique becomes much more powerful if one introduces
couplings to external classical ﬁelds. Let us consider an extended QCD Lagrangian,
with quark couplings to external Hermitian matrix-valued ﬁelds vµ, aµ, s, p:
LQCD = L0
QCD + ¯qγµ(vµ + γ5aµ)q −¯q(s −iγ5p)q .
(3.10)
The external ﬁelds will allow us to compute the eﬀective realization of general Green
functions of quark currents in a very straightforward way. Moreover, they can be
used to incorporate the electromagnetic and semileptonic weak interactions, and the
explicit breaking of chiral symmetry through the quark masses:
rµ ≡vµ + aµ = eQAµ + . . .
ℓµ ≡vµ −aµ = eQAµ +
e
√
2 sin θW
(W †
µT+ + h.c.) + . . .
(3.11)
s = M + . . .
Here, Q and M denote the quark-charge and quark-mass matrices, respectively,
Q = 1
3 diag(2, −1, −1) ,
M = diag(mu, md, ms) ,
(3.12)
and T+ is a 3×3 matrix containing the relevant Cabibbo–Kobayashi–Maskawa factors
T+ =


0
Vud
Vus
0
0
0
0
0
0

.
(3.13)
The Lagrangian (3.10) is invariant under the following set of local SU(3)L⊗SU(3)R
transformations:
qL −→gL qL ,
qR −→gR qR ,
s + ip −→gR (s + ip) g†
L ,
ℓµ −→gL ℓµ g†
L + igL∂µg†
L ,
rµ −→gR rµ g†
R + igR∂µg†
R .
(3.14)
We can use this symmetry to build a generalized eﬀective Lagrangian for the Goldstone
bosons, in the presence of external sources. Note that to respect the local invariance,
the gauge ﬁelds vµ, aµ can only appear through the covariant derivatives
DµU = ∂µU −irµU + iUℓµ ,
DµU † = ∂µU † + iU †rµ −iℓµU † , (3.15)
and through the ﬁeld strength tensors
F µν
L = ∂µℓν −∂νℓµ −i[ℓµ, ℓν] ,
F µν
R = ∂µrν −∂νrµ −i[rµ, rν] . (3.16)
At lowest order in momenta, the more general eﬀective Lagrangian consistent with
Lorentz invariance and (local) chiral symmetry is of the form (Gasser and Leutwyler
1985)
L2 = f 2
4 ⟨DµU †DµU + U †χ + χ†U⟩,
(3.17)
where
χ = 2B0 (s + ip),
(3.18)
and B0 is a constant, which, like f, is not ﬁxed by symmetry requirements alone.
Once special directions in ﬂavour space, like the ones in equation (3.11), are
selected for the external ﬁelds, chiral symmetry is of course explicitly broken. The
important point is that (3.17) then breaks the symmetry in exactly the same way as
the fundamental short-distance Lagrangian (3.10) does.
The power of the external ﬁeld technique becomes obvious when computing the
chiral Noether currents. The Green functions are obtained as functional derivatives
of the generating functional Z[v, a, s, p], deﬁned via the path-integral formula
exp {iZ} =
Z
Dq D¯q DGµ exp

i
Z
d4x LQCD

=
Z
DU exp

i
Z
d4x Leﬀ

.
(3.19)
At lowest order in momenta, the generating functional reduces to the classical action
S2 =
R
d4x L2; therefore, the currents can be trivially computed by taking the
appropriate derivatives with respect to the external ﬁelds:
Jµ
L
.= δS2
δℓµ
= i
2f 2DµU †U =
f
√
2DµΦ −i
2

Φ
↔
Dµ Φ

+ O(Φ3/f),
Jµ
R
.= δS2
δrµ
= i
2f 2DµUU † = −f
√
2
DµΦ −i
2

Φ
↔
Dµ Φ

+ O(Φ3/f).
(3.20)
The physical meaning of the chiral coupling f is now obvious; at O(p2), f equals
the pion decay constant, f = fπ = 92.4 MeV, deﬁned as
⟨0|(Jµ
A)12|π+⟩≡i
√
2fπpµ.
(3.21)
Similarly, by taking derivatives with respect to the external scalar and pseudoscalar
sources,
¯qj
Lqi
R
.= −
δS2
δ(s −ip)ji = −f 2
2 B0 U(φ)ij,
¯qj
Rqi
L
.= −
δS2
δ(s + ip)ji = −f 2
2 B0 U(φ)†ij,
(3.22)
we learn that the constant B0 is related to the quark condensate:
⟨0|¯qjqi|0⟩= −f 2B0δij.
(3.23)
The Goldstone bosons, parametrized by the matrix U(φ), correspond to the zero-
energy excitations over this vacuum condensate.
Taking s = M and p = 0, the χ term in equation (3.17) gives rise to a quadratic
pseudoscalar-mass term plus additional interactions proportional to the quark masses.
Expanding in powers of Φ (and dropping an irrelevant constant), one has:
f 2
4 2B0 ⟨M(U + U †)⟩= B0

−⟨MΦ2⟩+
1
6f 2⟨MΦ4⟩+ O(Φ6/f 4)

.(3.24)
The explicit evaluation of the trace in the quadratic mass term provides the relation
between the physical meson masses and the quark masses:
M 2
π± = 2 ˆmB0 ,
M 2
π0 = 2 ˆmB0 −ε + O(ε2) ,
M 2
K± = (mu + ms)B0 ,
M 2
K0 = (md + ms)B0 ,
(3.25)
M 2
η8 = 2
3( ˆm + 2ms)B0 + ε + O(ε2) ,
where‡
ˆm = 1
2(mu + md) ,
ε = B0
4
(mu −md)2
(ms −ˆm) .
(3.26)
Chiral symmetry relates the magnitude of the meson and quark masses to the size
of the quark condensate. Using the result (3.23), one gets from the ﬁrst equation in
(3.25) the well-known relation (Gell-Mann, Oakes and Renner 1968)
f 2
πM 2
π = −ˆm ⟨0|¯uu + ¯dd|0⟩.
(3.27)
Taking out the common B0 factor, equations (3.25) imply the old Current Algebra
mass ratios (Gell-Mann, Oakes and Renner 1968, Weinberg 1977),
M 2
π±
2 ˆm =
M 2
K+
(mu + ms) =
MK0
(md + ms) ≈
3M 2
η8
(2 ˆm + 4ms) ,
(3.28)
‡
The O(ε) corrections to M 2
π0 and M 2
η8 originate from a small mixing term between the π0 and η8
ﬁelds:
−B0⟨MΦ2⟩−→−(B0/
√
3) (mu −md) π0η8 .
The diagonalization of the quadratic π0, η8
mass matrix, gives the mass eigenstates, π0 = cos δ φ3 + sin δ φ8 and η8 = −sin δ φ3 + cos δ φ8, where
tan (2δ) =
√
3(md −mu)/ (2(ms −ˆm)) .
and (up to O(mu−md) corrections) the Gell-Mann (1962)–Okubo (1962) mass relation,
3M 2
η8 = 4M 2
K −M 2
π .
(3.29)
Note that the chiral Lagrangian automatically implies the successful quadratic Gell-
Mann–Okubo mass relation, and not a linear one. Since B0mq ∝M 2
φ, the external
ﬁeld χ is counted as O(p2) in the chiral expansion.
Although chiral symmetry alone cannot ﬁx the absolute values of the quark masses,
it gives information about quark-mass ratios. Neglecting the tiny O(ε) eﬀects, one gets
the relations
md −mu
md + mu
= (M 2
K0 −M 2
K+) −(M 2
π0 −M 2
π+)
M 2
π0
= 0.29 ,
(3.30)
ms −ˆm
2 ˆm
= M 2
K0 −M 2
π0
M 2
π0
= 12.6 .
(3.31)
In equation (3.30) we have subtracted the pion square-mass diﬀerence, to take into
account the electromagnetic contribution to the pseudoscalar-meson self-energies; in
the chiral limit (mu = md = ms = 0), this contribution is proportional to the square of
the meson charge and it is the same for K+ and π+ (Dashen 1969). The mass formulae
(3.30) and (3.31) imply the quark-mass ratios advocated by Weinberg (1977):
mu : md : ms = 0.55 : 1 : 20.3 .
(3.32)
Quark-mass corrections are therefore dominated by ms, which is large compared
with mu, md. Notice that the diﬀerence md −mu is not small compared with the
individual up- and down-quark masses; in spite of that, isospin turns out to be a
very good symmetry, because isospin-breaking eﬀects are governed by the small ratio
(md −mu)/ms.
The Φ4 interactions in equation (3.24) introduce mass corrections to the ππ
scattering amplitude (3.9),
T(π+π0 →π+π0) = t −M 2
π
f 2
π
,
(3.33)
in perfect agreement with the Current Algebra result (Weinberg 1966). Since f = fπ
is ﬁxed from pion decay, this result is now an absolute prediction of chiral symmetry.
The lowest-order chiral Lagrangian (3.17) encodes in a very compact way all the
Current Algebra results obtained in the sixties (Adler and Dashen 1968, de Alfaro et
al 1973). The nice feature of the chiral approach is its elegant simplicity. Moreover, as
we will see in the next section, the eﬀective ﬁeld theory method allows us to estimate
higher-order corrections in a systematic way.
4. ChPT at O(p4)
At next-to-leading order in momenta, O(p4), the computation of the generating
functional Z[v, a, s, p] involves three diﬀerent ingredients:
1.
The most general eﬀective chiral Lagrangian of O(p4), L4, to be considered at tree
level.
2.
One-loop graphs associated with the lowest-order Lagrangian L2.
3.
The Wess–Zumino (1971)–Witten (1983) functional to account for the chiral
anomaly.
4.1. O(p4) Lagrangian
At O(p4), the most general§ Lagrangian, invariant under parity, charge conjugation
and the local chiral transformations (3.14), is given by (Gasser and Leutwyler 1985)
L4 = L1 ⟨DµU †DµU⟩2 + L2 ⟨DµU †DνU⟩⟨DµU †DνU⟩
+ L3 ⟨DµU †DµUDνU †DνU⟩+ L4 ⟨DµU †DµU⟩⟨U †χ + χ†U⟩
+ L5 ⟨DµU †DµU
 U †χ + χ†U

⟩+ L6 ⟨U †χ + χ†U⟩2
+ L7 ⟨U †χ −χ†U⟩2 + L8 ⟨χ†Uχ†U + U †χU †χ⟩
−iL9 ⟨F µν
R DµUDνU † + F µν
L DµU †DνU⟩+ L10 ⟨U †F µν
R UFLµν⟩
+ H1 ⟨FRµνF µν
R + FLµνF µν
L ⟩+ H2 ⟨χ†χ⟩.
(4.1)
The terms proportional to H1 and H2 do not contain the pseudoscalar ﬁelds
and are therefore not directly measurable. Thus, at O(p4) we need ten additional
coupling constants Li to determine the low-energy behaviour of the Green functions.
These constants parametrize our ignorance about the details of the underlying QCD
dynamics. In principle, all the chiral couplings are calculable functions of ΛQCD and
the heavy-quark masses. At the present time, however, our main source of information
about these couplings is low-energy phenomenology.
