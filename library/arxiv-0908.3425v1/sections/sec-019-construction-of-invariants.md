---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-019-construction-of-invariants
section_title: "Construction of invariants"
section_number: null
pages: 27-33
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
So far, we have discussed the lowest-order eﬀective Lagrang ian for a global SU(3)L × SU(3)R symmetry.
In Sec. 2.1.6 we stated that the Ward identities of QCD are obt ained from a locally invariant generating
functional involving a coupling to external ﬁelds. Therefo re, following Refs. [Gasser and Leutwyler, 1984],
27
[Gasser and Leutwyler, 1985], we will promote the global sym metry of the eﬀective Lagrangian to a local
one,
L →VL(x), R→VR(x),
and introduce a coupling to the same external ﬁelds v, a, s, and p as in QCD [see Eq. (47)]. The
transformation behavior of the special unitary matrix U of Eqs. (86) and (88) under G = SU(3) L ×
SU(3)R, parity P , and charge conjugation C is given by
U G↦→VRUV †
L, U (⃗ x,t) P↦→U †(−⃗ x,t), U C↦→U T.
Given an object A transforming as VRAV †
L , such as U or χ, the covariant derivative of A, DµA, is
deﬁned as
DµA ≡∂µA −irµA +iAlµ ↦→D′
µA′ =VR(DµA)V †
L. (109)
The deﬁning property is that the covariant derivative shoul d transform as the object it acts on. In
particular, the covariant derivative of U is given by
DµU =∂µU −irµU +iUl µ. (110)
For the external ﬁelds we introduce corresponding ﬁeld stre ngth tensors in matrix form as
f R
µν ≡ ∂µrν −∂νrµ −i[rµ,r ν] G↦→VRf R
µνV †
R, (111)
f L
µν ≡ ∂µlν −∂νlµ −i[lµ,l ν] G↦→VLf L
µνV †
L. (112)
They are traceless, because Tr( lµ) = Tr( rµ) = 0 and the trace of any commutator vanishes. Fi-
nally, we introduce the linear combination χ = 2 B0(s + ip), where, e.g., pure QCD is given by
χ = 2B0diag(mu,m d,m s).
The eﬀective Lagrangian is constructed in terms of U, U †, χ, χ†, f R
µν, f L
µν and covariant derivatives
of these objects. Suppose we have matrices A,B,C, · · ·, all of which transform as
A G↦→VRAV †
L, B G↦→VRBV †
L, · · ·.
Invariants may be formed by “multiplying” in the following w ay:
Tr(AB†) G↦→ Tr(VRAV †
LVL/bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
/BD
B†V †
R) = Tr(V †
RVRAB†) = Tr(AB†),
where the generalization to a longer string of terms is obvio us and the product of invariant traces is
also invariant:
Tr(AB†CD †), Tr(AB†)Tr(CD †), · · ·. (113)
In the chiral counting scheme the elements count as
U = O(q0), D µU = O(q), r µ,l µ = O(q), f L/R
µν = O(q2), χ = O(q2).
Any additional covariant derivative counts as O(q). The list of objects A up to and including order q2
which transform as A′ =VRAV †
L reads
U, DµU, DµDνU, χ, UfL
µν, fR
µνU.
The construction of chirally invariant expressions up to an d including order q2 proceeds as follows. At
O(q0) the only invariant term is a constant, Tr
(
UU †
)
= Tr( /BD ) = const. Because of Tr
(
DµUU †
)
= 0,
terms of the type Tr[ O(q)] × Tr(· · ·) are excluded. At O(q2) we have
Tr
(
DµDνUU †
)
= −Tr
[
DνU(DµU)†
]
, Tr
[
DµU(DνU)†
]
, Tr
[
U(DµDνU)†
]
= −Tr
[
DµU(DνU)†
]
,
Tr
(
χU †
)
, Tr
(
Uχ †
)
, Tr
[
(Uf L
µν)U †
]
= Tr
(
f L
µν
)
= 0, Tr
(
f R
µν
)
= 0.
28
Because of Lorentz invariance, indices have to be contracte d and the remaining three candidates are
Tr
[
DµU(DµU)†
]
, Tr
(
χU † ±Uχ †
)
.
Finally, due to parity conservation,
L(⃗ x,t) P↦→ L(−⃗ x,t).
Tr(χU † −Uχ †) has to be excluded because of the wrong parity. At O(q2), charge conjugation does not
generate any additional constraint.
The locally invariant lowest-order Lagrangian L2 is given by
L2 = F 2
0
4 Tr
[
DµU(DµU)†
]
+ F 2
0
4 Tr
(
χU † +Uχ †
)
. (114)
At O(q2) it contains two parameters: the SU(3) chiral limit of the Go ldstone boson decay constant
F0 ≈ 93 MeV, and, hidden in the deﬁnition of χ, B0 = −⟨0|¯qq|0⟩0/(3F 2
0 ).
The lowest-order equation of motion corresponding to Eq. (1 14) is obtained by considering small
variations of the SU(3) matrix,
U ′(x) = U(x) +δU (x) =
(
/BD +i
8∑
a=1
∆ a(x)λa
)
U(x), (115)
where the ∆ a(x) are real functions. The matrix U ′ satisﬁes both conditions U ′U ′† = /BD and det(U ′) = 1
up to and including terms linear in ∆ a. Applying the principle of stationary action, the variatio n of the
action reads
δS =iF 2
0
4
∫ t2
t1
dt
∫
d3x
8∑
a=1
∆ a(x)Tr
{
λa[DµDµUU † −U(DµDµU)† −χU † +Uχ †]
}
,
where we made use of partial integration, the standard bound ary conditions ∆ a(t1,⃗ x) = ∆ a(t2,⃗ x) = 0,
the divergence theorem, and the deﬁnition of the covariant d erivative of Eq. (109). Since the test
functions ∆ a(x) may be chosen arbitrarily, we obtain eight Euler-Lagrange equations
Tr
{
λa[D2UU † −U(D2U)† −χU † +Uχ †]
}
= 0, a = 1, · · ·, 8, (116)
which may be combined into a compact matrix form
O(2)
EOM(U) ≡D2UU † −U(D2U)† −χU † +Uχ † + 1
3 Tr(χU † −Uχ †) = 0. (117)
The trace term in Eq. (117) appears, because Eq. (116) contai ns eight and not nine independent
equations.
3.2.4 Two simple applications: Pion decay and ππ scattering
The Lagrangian L2 of Eq. (114) has predictive power, once the low-energy coupl ing constant F0 is
identiﬁed. This LEC may be obtained from the weak decay of the pion, π+ →µ+νµ. For that purpose
we insert the corresponding external ﬁelds of Eq. (52), desc ribing the interaction of quarks with the
massive charged weak bosons, into L2. The coupling of a single W boson to a single Goldstone boson
originates from the covariant derivatives in L2,
F 2
0
4 Tr[DµU(DµU)†] = iF 2
0
2 Tr(lµ∂µU †U) + · · · = F0
2 Tr(lµ∂µφ) + · · ·,
29
and is given by
LW φ = − g
√
2
F0
2 Tr[(W +
µT++W −
µT−)∂µφ] = −gF0
2 [W +
µ (Vud∂µπ−+Vus∂µK −)+W −
µ (Vud∂µπ++Vus∂µK +)].
(118)
The invariant amplitude of the weak pion decay is of the struc ture “leptonic vertex ×W propagator ×
hadronic vertex,”
M =i
[
− g
2
√
2 ¯uνµγρ(1 −γ5)vµ+
]
igρσ
M 2
W
i
[
−gF0
2 Vud(−ipσ)
]
= −GFVudF0 ¯uνµp /(1 −γ5)vµ+, (119)
where GF is the Fermi constant of Eq. (53) and p denotes the four-momentum of the pion. In the
gauge-boson propagator, momenta p have been neglected in comparison to the gauge-boson mass MW .
The corresponding decay rate is
1
τ = G2
FV 2
ud
4π F 2
0Mπm2
µ
(
1 − m2
µ
M 2π
)2
.
The constant F0 is referred to as the pion-decay constant in the chiral limit . It measures the strength of
the matrix element of the axial-vector current operator bet ween a one-Goldstone-boson state and the
vacuum [see Eq. (81)]. Since the interaction of the W boson with the quarks is of the V −A type and
the vector current operator does not contribute to the matri x element between a single pion and the
vacuum, pion decay is completely determined by the axial-ve ctor current. The degeneracy of a single
coupling constant F0 is removed at next-to-leading order, O(q4) [Gasser and Leutwyler, 1985], once
SU(3) symmetry breaking is taken into account. The empirica l numbers for Fπ and FK are 92.4 MeV
and 113 MeV, respectively [Amsler et al., 2008].
Now that the LEC F0 has been identiﬁed, we will show how the lowest-order Lagran gian predicts the
prototype of a Goldstone-boson reaction, namely, ππ scattering. We consider L2 in the SU(2) L ×SU(2)R
sector with rµ =lµ = 0,
L2 = F 2
4 Tr
(
∂µU∂ µU †
)
+ F 2
4 Tr
(
χU † +Uχ †
)
,
where
χ = 2B
(
ˆm 0
0 ˆ m
)
, U = exp
(
iφ
F
)
, φ =
3∑
i=1
φiτi ≡
(
π0 √
2π+
√
2π− −π0
)
.
In the SU(2) L × SU(2)R sector it is common to express quantities in the chiral limit without index 0,
e.g., F and B. By this one means the SU(2) L × SU(2)R chiral limit, i.e., mu = md = 0 but ms at its
physical value. In the SU(3) L × SU(3)R sector the quantities F0 and B0 denote the chiral limit for all
three quarks: mu =md =ms = 0. Using the substitution U ↔U †, we see that L2 contains even powers
of φ only:
L2 = L2φ
2 + L4φ
2 + · · ·.
Since L2 does not produce a vertex with three Goldstone bosons, there are no s-, u-, and t-channel
pole diagrams, i.e., at D = 2, ππ scattering is entirely generated by a four-Goldstone-boso n-interaction
term. Expanding
U = /BD +iφ
F − 1
2
φ2
F 2 − i
6
φ3
F 3 + 1
24
φ4
F 4 + · · ·,
the interaction term L4φ
2 is identiﬁed as
L4φ
2 = 1
48F 2
[
Tr([φ,∂ µφ][φ,∂ µφ]) + 2BTr(Mφ4)
]
.
30
/D4
/CP
/BN /CP
/D4
/CQ
/BN /CQ
/D4

/BN 
/D4
/CS
/BN /CS
/BE
Figure 3: Lowest-order Feynman diagram for ππ scattering. The vertex is derived from L2, denoted by
2 in the interaction blob.
We note that substituting F → F0, B → B0 and the relevant expressions for φ and the quark-mass
matrix M the corresponding formula for SU(3) L × SU(3)R looks identical. Inserting φ = φiτi and
working out the traces yields
L4φ
2 = 1
6F 2 (φi∂µφi∂µφjφj −φiφi∂µφj∂µφj) + M 2
24F 2φiφiφjφj,
whereM 2 = 2B ˆm. The Feynman rule derived from L4φ
2 for Cartesian isospin indices a,b,c, and d reads
(see Fig. 3)
M = i
[
δabδcd
s −M 2
F 2 +δacδbd
t −M 2
F 2 +δadδbc
u −M 2
F 2
]
− i
3F 2 (δabδcd +δacδbd +δadδbc) (Λ a + Λ b + Λ c + Λ d), (120)
where Λ k =p2
k −M 2 and s, t, and u are the usual Mandelstam variables,
s = (pa +pb)2, t = (pa −pc)2, u = (pa −pd)2.
In general, the T -matrix element for the scattering process πa(pa) + πb(pb) → πc(pc) + πd(pd) can be
parameterized as
T ab;cd(pa,p b;pc,p d) = δabδcdA(s,t,u ) +δacδbdA(t,s,u ) +δadδbcA(u,t,s ), (121)
where the function A satisﬁes A(s,t,u ) = A(s,u,t ) [Weinberg, 1966]. Since the last line of the Feynman
rule of Eq. (120 ) disappears, if the external lines satisfy o n-mass-shell conditions, at O(q2) the prediction
for the function A is given by
A(s,t,u ) = s −M 2
π
F 2π
. (122)
In Eq. (122) we substituted Fπ for F and Mπ forM, because the diﬀerence is of O(q4) in T . Equation
(122) illustrates an important general property of Goldsto ne-boson interactions. If we consider the
(theoretical) limit M 2
π,s,t,u → 0, the T matrix vanishes, T → 0. In other words, the strength of
Goldstone-boson interactions vanishes in the zero-energy and mass limit.
Usually,ππ scattering is discussed in terms of its isospin decompositi on. Since the pions form an
isospin triplet, the two isovectors of both the initial and ﬁ nal states may be coupled to I = 0, 1, 2.
Formu = md = ˆm the strong interactions are invariant under isospin transf ormations, implying that
scattering matrix elements can be decomposed as
⟨I ′,I ′
3|T |I,I 3⟩=T IδII ′δI3I ′
3. (123)
31
For the case of ππ scattering the three isospin amplitudes are given in terms o f the invariant amplitude
A of Eq. (121) by [Gasser and Leutwyler, 1984]
T I=0 = 3 A(s,t,u ) +A(t,u,s ) +A(u,s,t ),
T I=1 = A(t,u,s ) −A(u,s,t ),
T I=2 = A(t,u,s ) +A(u,s,t ). (124)
For example, the physical π+π+ scattering process is described by T I=2. Other physical processes are
obtained using the appropriate Clebsch-Gordan coeﬃcients .
Evaluating the T matrices at threshold, one obtains the s-waveππ-scattering lengths
T I=0|thr = 32πa0
0, T I=2|thr = 32πa2
0, (125)
where the subscript 0 refers to s wave and the superscript to the isospin. ( T I=1|thr vanishes because of
Bose symmetry). The convention in ChPT diﬀers by a factor ( −Mπ) from the usual deﬁnition of a scat-
tering length in the eﬀective range expansion. The current- algebra prediction of Ref. [Weinberg, 1966]
is identical with the lowest-order result obtained from Eq. (122),
a0
0 = 7M 2
π
32πF 2π
= 0.159, a 2
0 = − M 2
π
16πF 2π
= −0.0454, (126)
where we made use of the numerical values Fπ = 92.4 MeV and Mπ =Mπ+ = 139.57 MeV. In order to
obtain the results of Eq. (126), use has been made of sthr = 4M 2
π and tthr =uthr = 0. Equations (126)
represent an absolute prediction of chiral symmetry. Once Fπ is known (from pion decay), the scat-
tering lengths are predicted. The s-waveππ-scattering lengths have been calculated at next-to-leadi ng
(NL) order [Gasser and Leutwyler, 1984] and at next-to-next -to-leading order [Bijnens et al., 1996],
[Bijnens et al., 1997]. By matching the chiral representati on of the scattering amplitude with a dis-
persive representation [Roy 1971], [Ananthanarayan et al. , 2001], the predictions for the s-wave ππ-
scattering lengths are [Colangelo et al., 2000], [Colangel o et al., 2001b]
a0
0 = 0.220 ± 0.005, a 2
0 = −0.0444 ± 0.0010. (127)
The empirical results for the s-waveππ-scattering lengths have been obtained from various source s. In
the Ke4 decay K + → π+π−e+νe, the connection with low-energy ππ scattering stems from a partial-
wave analysis of the form factors relevant for the Ke4 decay in terms of ππ angular momentum eigen-
states. In the low-energy regime the phases of these form fac tors are related by (a generalization of)
Watson’s theorem [Watson, 1954] to the corresponding phase s of I = 0 s-wave and I = 1 p-wave elas-
tic scattering [Colangelo et al., 2001a]. Using eﬀective ﬁe ld theory techniques, isospin-breaking eﬀects
generated by real and virtual photons, and by the mass diﬀere nce of the up and down quarks were
discussed in Ref. [Colangelo et al., 2009]. Performing a com bined analysis of the Geneva-Saclay data
[Rosselet et al., 1977], the BNL-E865 data [Pislak et al., 20 01], [Pislak et al., 2003], and the NA48/2
data [Batley et al., 2008] results in [Colangelo et al., 2009 ]
a0
0 = 0.217 ± 0.008exp ± 0.006th (128)
which is in excellent agreement with the prediction of Eq. (1 27). The π±p →π±π+n reactions require an
extrapolation to the pion pole to extract the ππ amplitude and are thus regarded to contain more model
dependence, a0
0 = 0.204 ± 0.014 (stat) ± 0.008 (syst) [Kermani et al., 1998]. The DIRAC Collaboration
[Adeva et al., 2005] makes use of a lifetime measurement of pi onium to extract |a0
0 −a2
0| = 0.264+0.033
−0.020.
Finally, in the K ± →π±π0π0 decay, isospin-symmetry breaking leads to a cusp structure ∼a0 −a2 in
the π0π0 invariant mass distribution near sπ0π0 ≈ 4M 2
π+ [Cabibbo, 2004], [Cabibbo and Isidori, 2005].
32
k
Figure 4: Generic one-loop diagram. The black box denotes so me unspeciﬁed vertex structure which is
irrelevant for the discussion.
Based on the model of [Cabibbo and Isidori, 2005], the NA48/2 Collaboration extract a0
0 −a2
0 = 0.268 ±
0.010 (stat)± 0.004 (syst)± 0.013 (ext). A more sophisticated analysis of the cusps in K → 3π within an
eﬀective ﬁeld theory framework can be found in Refs. [Colang elo et al., 2006], [Bissegger et al., 2008],
and [Bissegger et al., 2009].
In particular, when analyzing the data of Ref. [Pislak et al. , 2001] in combination with the Roy equa-
tions, an upper limit |¯l3| ≤ 16 was obtained in Ref. [Colangelo et al., 2001a] for the scal e-independent
low-energy coupling constant which is related to l3 of the SU(2) L × SU(2)R Lagrangian of Gasser and
Leutwyler [Gasser and Leutwyler, 1984]. The great interest generated by this result is to be understood
in the context of the pion mass at O(q4)
M 2
π =M 2 −
¯
l3
32π2F 2M 4 + O(M 6), (129)
where M 2 = 2 ˆmB. Recall that the constant B is related to the scalar quark condensate in the chiral
limit and that a non-vanishing quark condensate is a suﬃcien t criterion for spontaneous chiral sym-
metry breakdown in QCD. If the expansion of M 2
π in powers of the quark masses is dominated by
the linear term in Eq. (129), the result is often referred to a s the Gell-Mann-Oakes-Renner relation
[Gell-Mann et al., 1968]. If the terms of order ˆ m2 were comparable or even larger than the linear terms,
a diﬀerent power counting or bookkeeping in ChPT would be req uired [Knecht et al., 1995]. The es-
timate |¯l3| ≤ 16 implies that the Gell-Mann-Oakes-Renner relation is ind eed a decent starting point,
because the contribution of the second term of Eq. (129) to th e pion mass is approximately given by
−
¯l3M 2
π
64π2F 2π
Mπ = −0.054Mπ for ¯l3 = 16,
i.e., more than 94 % of the pion mass must stem from the quark co ndensate [Colangelo et al., 2001a].
