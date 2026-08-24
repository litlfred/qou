---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-023-the-oq4-lagrangian-of-gasser-and-leutwyler
section_title: "The O(q4) Lagrangian of Gasser and Leutwyler"
section_number: null
pages: 38-42
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
The most general SU(3)L×SU(3)R-invariant Lagrangian at O(q4) is given by [Gasser and Leutwyler, 1985]
L4 =L1
{
Tr[DµU(DµU)†]
} 2
+L2Tr
[
DµU(DνU)†
]
Tr
[
DµU(DνU)†
]
+L3Tr
[
DµU(DµU)†DνU(DνU)†
]
+L4Tr
[
DµU(DµU)†
]
Tr
(
χU † +Uχ †
)
+L5Tr
[
DµU(DµU)†(χU † +Uχ †)
]
+L6
[
Tr
(
χU † +Uχ †
)] 2
+L7
[
Tr
(
χU † −Uχ †
)] 2
+L8Tr
(
Uχ †Uχ † +χU †χU †
)
−iL9Tr
[
f R
µνDµU(DνU)† +f L
µν(DµU)†DνU
]
+L10Tr
(
Uf L
µνU †f µν
R
)
+H1Tr
(
f R
µνf µν
R +f L
µνf µν
L
)
+H2Tr
(
χχ†
)
. (140)
The numerical values of the low-energy coupling constants Li are not determined by chiral symmetry.
In analogy to F0 andB0 of L2 they are parameters containing information on the underlyi ng dynamics
and should, in principle, be calculable in terms of the (rema ining) parameters of QCD, namely, the
heavy-quark masses and the QCD scale Λ QCD. In practice, they parameterize our inability to solve
the dynamics of QCD in the non-perturbative regime. So far th ey have either been ﬁxed using empiri-
cal input or theoretically using QCD-inspired models, meso n-resonance saturation [Ecker et al., 1989a]
[Pich, 2008], and lattice QCD (see Ref. [Necco, (2009)] for a recent overview).
By construction Eq. (140) represents the most general Lagra ngian at O(q4), and it is thus possible
to absorb the one-loop divergences by an appropriate renorm alization of the coeﬃcients Li and Hi:
Li =Lr
i + Γ i
32π2R (i = 1, · · ·, 10), H i =H r
i + ∆ i
32π2R (i = 1, 2), (141)
where R has already been deﬁned in Eq. (135):
R = 2
n − 4 − [ln(4π) + Γ ′(1) + 1],
with n denoting the number of space-time dimensions and γE = −Γ ′(1) being Euler’s constant. The
constants Γ i and ∆ i are given in Table 7. Except for L3 and L7, the low-energy coupling constants Li
and the “contact terms”—i.e., pure external ﬁeld terms— H1 andH2 are required in the renormalization
of the one-loop graphs. Since H1 andH2 contain only external ﬁelds, they are of no physical relevan ce.
The idea of renormalization consists of adjusting the param eters of the counter terms of the most
general eﬀective Lagrangian so that they cancel the diverge nces of (multi-) loop diagrams. In doing so,
one still has the freedom of choosing a suitable renormaliza tion condition. For example, in the minimal
subtraction scheme (MS) one would ﬁx the parameters of the co unter term Lagrangian such that they
would precisely absorb the contributions proportional to 2 /(n − 4) in R, while the modiﬁed minimal
subtraction scheme of ChPT ( ~MS) would, in addition, cancel the term in the square bracket s.
38
Coeﬃcient Empirical Value Γ i
Lr
1
0.4 ± 0.3 3
32
Lr
2
1.35 ± 0.3 3
16
Lr
3
−3.5 ± 1.1 0
Lr
4
−0.3 ± 0.5 1
8
Lr
5
1.4 ± 0.5 3
8
Lr
6
−0.2 ± 0.3 11
144
Lr
7
−0.4 ± 0.2 0
Lr
8
0.9 ± 0.3 5
48
Lr
9
6.9 ± 0.7 1
4
Lr
10
−5.5 ± 0.7 − 1
4
Table 7: Renormalized low-energy coupling constants Lr
i in units of 10 −3 at the scale µ = Mρ, see
[Bijnens et al., 1995]. ∆ 1 = −1/8, ∆ 2 = 5/24.
The renormalized coeﬃcients Lr
i depend on the scale µ introduced by dimensional regularization
[see Eq. (134)] and their values at two diﬀerent scales µ1 and µ2 are related by
Lr
i (µ2) = Lr
i (µ1) + Γ i
16π2 ln
(
µ1
µ2
)
. (142)
We will see that the scale dependence of the coeﬃcients and th e ﬁnite part of the loop-diagrams
compensate each other in such a way that physical observable s are scale independent.
A discussion of the two-ﬂavor Lagrangian at O(q4) [Gasser and Leutwyler, 1984] can be found in
Appendix D of Ref. [Scherer, 2003]. For the construction of t he O(q6) Lagrangian of even intrinsic
parity, see Refs. [Scherer and Fearing, 1995], [Fearing and Scherer, 1996] and [Bijnens et al., 1999]. For
a status report on mesonic chiral perturbation theory beyon d the one-loop level, we refer the reader to
Ref. [Bijnens, 2007].
3.3.2 The eﬀective Wess-Zumino-Witten action
The Lagrangians discussed so far have a larger symmetry than QCD [Witten, 1983]. For example, if we
consider the case of “pure” QCD, i.e., no external ﬁelds exce pt for the quark-mass term χ = 2B0M, L2
and L4 contain interaction terms with an even number of Goldstone b osons only (even intrinsic parity).
In other words, they cannot describe, e.g, K +K − → π+π−π0. Analogously, L2 and L4 including a
coupling to electromagnetic ﬁelds cannot describe π0 →γγ .
In order to overcome this shortcoming, Witten suggested to a dd the simplest term possible which
breaks the symmetry of having only an even number of Goldston e bosons at the Lagrangian level. For
the case of massless Goldstone bosons without any external ﬁ elds the modiﬁed equation of motion reads
∂µ
(
F 2
0
2 U∂ µU †
)
+λǫµνρσU∂ µU †U∂ νU †U∂ ρU †U∂ σU † = 0, (143)
where λ is a (purely imaginary) constant. For the purpose of writing down an action corresponding to
Eq. (143), we extend the range of deﬁnition of the ﬁelds to a hy pothetical ﬁfth dimension,
U(y) = exp
(
iαφ(x)
F0
)
, y i = (xµ,α ), i = 0, · · ·, 4, 0 ≤α ≤ 1, (144)
39
where Minkowski space is deﬁned as the surface of the ﬁve-dim ensional space for α = 1. The action in
in the absence of external ﬁelds (denoted by a superscript 0) is given by [Witten, 1983]
S0
ano =nS0
WZW, S 0
WZW = − i
240π2
∫ 1
0
dα
∫
d4xǫijklm Tr
(
U L
i · · · UL
m
)
, (145)
where
ǫ01234 = −ǫ01234 = 1, U L
i =U †∂U
∂y i, λ = in
48π2.
A rather unusual and surprising feature of Eq. (145) is that t he action functional corresponding to the
new term cannot be written as the four-dimensional integral of a Lagrangian expressed in terms of U
and its derivatives. Wess and Zumino derived consistency or integrability relations which are satisﬁed by
the anomalous Ward identities and then explicitly construc ted a functional involving the pseudoscalar
octet which satisﬁes the anomalous Ward identities [Wess an d Zumino, 1971]. In particular, Wess and
Zumino emphasized that their interaction Lagrangians cann ot be obtained as part of a chiral invariant
Lagrangian. Using topological arguments Witten showed tha t the constant n appearing in Eq. (145)
must be an integer. However, it was pointed out in Ref. [B¨ ar a nd Wiese, 2001] that the traditional
argument relating n with the number of colors Nc is incomplete. Before discussing this argument, let
us investigate the consequences of S0
WZW.
Expanding the SU(3) matrix U(y) in terms of the Goldstone boson ﬁelds, U(y) = /BD +iαφ(x)/F0 +
O(φ2), one obtains an inﬁnite series of terms, each involving an o dd number of Goldstone bosons, i.e.,
the WZW action S0
WZW is of odd intrinsic parity. For each individual term the α integration can be
performed explicitly resulting in an ordinary action in ter ms of a four-dimensional integral of a local
Lagrangian. For example, the term with the smallest number o f Goldstone bosons reads
S5φ
WZW = 1
240π2F 5
0
∫
d4xǫµνρσ Tr(φ∂µφ∂νφ∂ρφ∂σφ), (146)
which describes, e.g., K +K − →π+π−π0. In particular, the WZW action without external ﬁelds invol ves
at least ﬁve Goldstone bosons [Wess and Zumino, 1971].
The connection to the number of colors Nc is established by introducing a coupling to electromag-
netism [Wess and Zumino, 1971], [Witten, 1983]. In the prese nce of external ﬁelds there will be an
additional term in the anomalous action,
Sano =S0
ano +Sext
ano =n(S0
WZW +Sext
WZW), (147)
given by (see, e.g., Ref. [Bijnens, 1993])
Sext
WZW = − i
48π2
∫
d4xǫ µνρσ Tr(Zµνρσ ) (148)
with
Zµνρσ = 1
2 Ul µU †rνUl ρU †rσ +Ul µlνlρU †rσ −U †rµrνrρUl σ
+iU∂ µlνlρU †rσ −iU †∂µrνrρUl σ +i∂µrνUl ρU †rσ −i∂µlνU †rρUl σ
−iU L
µlνU †rρUl σ +iU R
µrνUl ρU †rσ −iU L
µlνlρlσ +iU R
µrνrρrσ
+ 1
2U L
µU †∂νrρUl σ − 1
2 U R
µU∂ νlρU †rσ + 1
2 U L
µU †rνU∂ ρlσ − 1
2 U R
µUl νU †∂ρrσ
−U L
µ U L
νU †rρUl σ + U R
µ U R
ν Ul ρU †rσ + 1
2 U L
µlνU L
ρlσ − 1
2 U R
µrνU R
ρ rσ
+U L
µlν∂ρlσ − U R
µrν∂ρrσ + U L
µ∂νlρlσ − U R
µ∂νrρrσ
−iU L
µ U L
ν U L
ρlσ +iU R
µ U R
ν U R
ρ rσ, (149)
40
where we deﬁned the abbreviations U L
µ =U †∂µU and U R
µ =U∂ µU †.
As a special case, let us consider a coupling to external elec tromagnetic ﬁelds by inserting
rµ =lµ = −eQAµ,
whereQ is the quark-charge matrix. The terms involving three and fo ur electromagnetic four-potentials
vanish upon contraction with the totally antisymmetric tensorǫµνρσ , because their contributions to Zµνρσ
are symmetric in at least two indices, and we obtain
nLext
WZW = −enAµJ µ +i ne2
48π2ǫµνρσ∂νAρAσTr[2Q2(U∂ µU † −U †∂µU) −QU †Q∂µU +QUQ∂ µU †]. (150)
We note that the current
J µ = ǫµνρσ
48π2 Tr(Q∂νUU †∂ρUU †∂σUU † +QU †∂νUU †∂ρUU †∂σU), ǫ 0123 = 1, (151)
by itself is not gauge invariant and the additional terms of E q. (150) are required to obtain a gauge-
invariant action. The standard procedure of determining n is to investigate the interaction Lagrangian
which is relevant to the decay π0 → γγ by expanding U = /BD +idiag(π0, −π0, 0)/F0 + · · ·. However,
as pointed out by B¨ ar and Wiese, when considering the electr omagnetic interaction for an arbitrary
number of colors one should replace the ordinary quark charg e matrix by
Q =



2
3 0 0
0 − 1
3 0
0 0 − 1
3


 →



1
2Nc
+ 1
2 0 0
0 1
2Nc
− 1
2 0
0 0 1
2Nc
− 1
2


.
The corresponding eﬀective Lagrangian for π0 →γγ decay,
Lπ0γγ = − n
Nc
e2
32π2ǫµνρσ FµνFρσ
π0
F0
,
results in the decay rate
Γ π0→γγ = α2M 3
π0
64π3F 2
0
n2
N 2c
= 7.6 eV ×
(n
Nc
)2
in good agreement with the experimental value (7 .7 ± 0.6) eV for n = Nc. However, the result is no
indication for Nc = 3 [B¨ ar and Wiese, 2001]. The conclusion from their analysi s is that one should
rather consider three-ﬂavor processes such as η → π+π−γ or Kγ → Kπ to test the expected Nc
dependence in a low-energy reaction. For example, the Lagra ngian relevant to the decay η →π+π−γ is
given by
Lηπ+π−γ = ien
12
√
3π2F 3
0
(Qu −Qd)ǫµνρσ Aµ∂νη∂ρπ+∂σπ−,
where the quark-charge diﬀerence Qu −Qd = 1 is independent of Nc. However, by investigating the
corresponding η and η′ decays up to next-to-leading order in the framework of the co mbined 1/Nc and
chiral expansions, Borasoy and Lipartia have concluded tha t the number of colors cannot be determined
from these decays due to the importance of sub-leading terms which are needed to account for the
experimental decay widths and photon spectra [Borasoy and L ipartia, 2005].
For a discussion of the O(q6) Lagrangian of odd intrinsic parity see Refs. [Ebertsh¨ aus er et al., 2002]
and [Bijnens et al., 2002].
41
4 2
Figure 8: Self-energy diagrams at O(q4). Vertices derived from L2n are denoted by 2n in the interaction
blobs.
/BP
/B7
/B7
/B7
/A1 /A1 /A1
Figure 9: Unrenormalized propagator as the sum of irreducib le self-energy diagrams. Hatched and cross-
hatched “vertices” denote one-particle-reducible and one -particle-irreducible contributions, respectively.
