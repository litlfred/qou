---
doc_id: arxiv-1508.06401v2
doc_title: "Isospin splittings of meson and baryon masses from three-flavor lattice QCD + QED"
section_id: sec-001-2-lattice-matters
section_title: "Lattice matters"
section_number: 2
pages: 4-7
source_pdf: 1508.06401v2.pdf
source_sha256: 354f6e4ea835af6d
toc_source: outline
doc_brief: "Isospin splittings of meson and baryon masses from three-flavor lattice QCD + QED — Lattice QCD simulations are now reaching a precision where isospin breaking eﬀects become important."
---
Lattice matters
The action we are using is
S = S G + S A + S u
F + S d
F + S s
F .
(5)
Here S G is the tree-level Symanzik improved SU(3) gauge action with gauge coupling β = 6/g2,
and S A is the noncompact U(1) gauge action [8, 9] of the photon,
S A = 1
2e2
X
x,µ<ν

Aµ(x) + Aν(x + µ) −Aµ(x + ν) −Aν(x)
2 .
(6)
We employ the nonperturbatively O(a) improved SLiNC fermion action [10] for each quark
ﬂavor,
˜S q
F =
X
x
n1
2
X
µ
¯q(x)(γµ −1)e−ieq Aµ(x) ˜Uµ(x)q(x + ˆµ) −¯q(x)(γµ + 1)eieq Aµ(x−ˆµ) ˜U†
µ(x −ˆµ)q(x −ˆµ)
+ 1
2κq
¯q(x)q(x) −1
4cS W
X
µν
¯q(x)σµνFµν(x)q(x)
o
.
(7)
This action features single iterated mildly stout smeared QCD links with α = 0.1 [5] and un-
smeared QED links in the hopping terms, while the clover term contains unsmeared QCD links
only. We keep the action deliberately local, as excessive smearing will lead to large autocorre-
lation times. Stout smearing is analytic, so a derivative can be taken, which makes the HMC
force well deﬁned. The clover coeﬃcient has been computed nonperturbatively in QCD [10].
We presently neglect electromagnetic modiﬁcations to the clover term. This will leave us with
corrections of O(αEM e2
q a), which turn out to be no larger than the O(a2) corrections from QCD
in our simulations. We check this later by comparing neutral meson masses with diﬀerent quark
charges eq (Fig. 3). Adding an electromagnetic clover term with cEM
S W = 1 would leave us with
corrections of O(αEM e2
q g2a) (to this order in αEM), which is not a signiﬁcant improvement, if at
all. Simulations are performed using the HMC and RHMC [11] algorithms. The gluon ﬁeld and
the EM ﬁeld are updated sequentially.
In this study, we limit our calculations to a single value of the strong coupling constant (lattice
spacing) β = 5.50, where we have our largest sample of dynamical QCD conﬁgurations [12].
4
Furthermore, we restrict ourselves to simulations at the symmetric point, δmu = δmd = δms = 0,
which we deﬁne as X2
π/X2
N = 0.126, where X2
N =

M2
n + M2
p + M2
Σ−+ M2
Σ+ + M2
Ξ−+ M2
Ξ0

/6. We
may use either Xπ or XN to set the scale [5]. After several tuning runs carried out on 243 × 48
lattices we arrived at the κ values ¯κu = 0.124362 , ¯κd = ¯κs = 0.121713. At these κ values, we
study three diﬀerent volumes, 243×48, 323×64 and 483×96, with O(2000) to O(500) trajectories.
We like to add that simulations at the symmetric point already catch the essential features of the
physical QCD + QED vacuum, as ﬂavor singlet quantities vary slowly along the ¯m = constant
trajectory [5].
On these ensembles we have computed PQ pseudoscalar meson and octet baryon masses for
a variety of quark masses ranging from mPS/mN = 0.22 to 0.5, with eq = −1/3, 0 and +2/3. This
leads to about 40 pseudoscalar masses and 70 baryon masses per ensemble. The baryons include
several artiﬁcial states containing the ﬁctitious n quark and charge 2 baryons with ﬂavor structure
uuu′.
The action (5) is invariant under U(1) gauge transformations
Aµ(x) →Aµ(x) + ∆µ α(x) ,
q(x) →eieqα(x) q(x) .
(8)
However, this is not the case for propagators of charged particles, which demands ﬁxing the
gauge, as in perturbation theory. We choose the Landau gauge, which is deﬁned by the condition
¯∆µAµ(x) = 0, where ∆µ ( ¯∆µ) is the forward (backward) lattice derivative. The Landau gauge does
not eliminate all gauge degrees of freedom, but allows for shifts ∆µα(x) of the photon ﬁeld with
∆2α(x) = 0, where ∆2 = ∆µ ¯∆µ [9]. To maintain (anti-)periodicity of the quark ﬁelds, α(x) must
be periodic up to a transformation of the form
eqα(x) =
X
µ
2π
Lµ
nµxµ ,
nµ ∈Z ,
0
0.002
0.004
0.006
0.008
0
200
400
600
800
1000
1200⃗
B2/9
Trajectory Number
Bin3
Bin1
Bin2
0.21
0.22
0.23
0.24
0
0.001
0.002
0.003
0.004
0.005
aMπ+
⟨⃗B2⟩/9
Bin3
Bin1
Bin2
EnAv
0.21
0.22
0.23
0.24
0
0.001
0.002
0.003
0.004
0.005
aMπ+
⟨⃗B2⟩/9
Bin3
Bin1
Bin2
EnAv
0.21
0.22
0.23
0.24
0
0.001
0.002
0.003
0.004
0.005
aMπ+
⟨⃗B2⟩/9
Bin3
Bin1
Bin2
EnAv
0.21
0.22
0.23
0.24
0
0.001
0.002
0.003
0.004
0.005
aMπ+
⟨⃗B2⟩/9
Bin3
Bin1
Bin2
EnAv
0.21
0.22
0.23
0.24
0
0.001
0.002
0.003
0.004
0.005
aMπ+
⟨⃗B2⟩/9
Bin3
Bin1
Bin2
EnAv
Figure 2: Left panel: The background ﬁeld on the 243 × 48 lattice divided into three bins of
approximately constant⃗B2. Right panel: The bin averaged energy of the charged pion at rest
against the bin averaged ⟨⃗B2⟩. The black square (■) indicates the ensemble average (EnAv) of
both aMπ+ and ⟨⃗B2⟩. The line is a one-parameter linear ﬁt through the three mass points.
5
where Lµ is the extent of the lattice in µ direction. This gauge ﬁeld redundancy can be eliminated
by adding multiples of 2π/eqLµ to Aµ(x), such that
−
π
|eq|Lµ
< Bµ ≤
π
|eq|Lµ
,
Bµ = 1
V
X
x
Aµ(x) .
(9)
Taking eq = −1/3 in (9) serves both charges. The advantage of this procedure is that it leaves
the fermion determinant and Polyakov loops for all quark ﬂavors unchanged. In other popular
gauges [3] this is not the case, but results in a permanent Polyakov loop Πxν,ν,µ LEM
µ (xν) = 1,
which we would not know how to correct for in a simple manner.
The constant background ﬁeld can be factored out from the link matrices, conﬁguration by
conﬁguration, and absorbed into the quark momenta by straightforward algebra.1 This leaves us
with photon propagators that are devoid of zero modes. In the presence of a constant background
ﬁeld Bµ the correlator of a single hadron H thus becomes [9]
⟨0|H(t) ¯H(0)|0⟩≃|ZH|2 e−
q
M2
H+
⃗
p+eH⃗B
2t ,
(10)
where MH,⃗p and eH are mass, three-momentum and electric charge of the hadron, respectively.
This amounts to a shift of the rest energy of the charged hadrons, MH →
q
M2
H + e2
H⃗B2 ≃MH +
e2
H⃗B2/2MH. We determine the ensemble average of⃗B2 directly on each of our three volumes. The
result is 0.024, 0.0079 and 0.000095 for the smallest to largest volumes, respectively. To extract
masses, we remove the inﬂuence of the background ﬁeld eﬀect by subtracting the associated
kinetic energy from the ensemble averaged lattice energy. To demonstrate the validity of this
procedure, we have divided a subset of our 243 × 48 ensemble into three bins of approximately
constant background ﬁeld in Fig. 2 and plot the corresponding lattice energies for each of these
bins against the corresponding⃗B2. It shows that both the energies of the individual bins as well as
the ensemble averaged energy fall on a single straight line, in line with our subtraction method.
On the 483×96 lattice the eﬀect of the background ﬁeld is comparable to our statistical precision.
With the zero modes removed, we then can employ established methods, such as [13], to correct
for the remaining electromagnetic ﬁnite size eﬀects associated with the long-range tail of the
photon ﬁeld. Any residual eﬀect of the background ﬁeld will only act to modify the recoil energy
of any charged hadron propagator within loops.
Our strategy is to simulate at an artiﬁcial coupling e2 = 1.25, and then interpolate between this
point and pure QCD to the physical ﬁne structure constant αEM = 1/137. This value is chosen so
that electromagnetic eﬀects can be easily seen, but is still small enough that they scale linearly in
e2 and we do not need to consider higher order terms. Most importantly, Z3 = 0.94(3), obtained
from the vacuum polarization. Furthermore, in Figs. 4 and 5 of [6] we have plotted 1/κc
q , 1/¯κq
and the bare quark mass at the symmetric point, 1/2¯κq−1/2κc
q, against e2
q for eq = −1/3, 0 and 2/3
and found that all three quantities lie on a straight line. In addition, we ﬁnd that the coeﬃcients
α and α1, α2 in (3) and (4) agree to a good precision with the corresponding numbers in pure
QCD [5]. This rules out signiﬁcant higher order corrections in e2.
1Note that the transformation q(x) →ei∆x q(x) , ¯q(x) →¯q(x) e−i∆x amounts to a shift of quark momenta p →
p + ∆.
6
0
0.5
1
1.5
2
2.5
3
-0.01
0
0.01
0.02
0.03
M 2
PS (a¯a)/X2
π
−δµs
−δµu
δµa
π0
K0
ηs
0
0.5
1
1.5
2
2.5
3
-0.01
0
0.01
0.02
0.03
M 2
PS (a¯a)/X2
π
−δµs
−δµu
δµa
π0
K0
ηs
0
0.5
1
1.5
2
2.5
3
-0.01
0
0.01
0.02
0.03
M 2
PS (a¯a)/X2
π
−δµs
−δµu
δµa
π0
K0
ηs
0
0.5
1
1.5
2
2.5
3
-0.01
0
0.01
0.02
0.03
M 2
PS (a¯a)/X2
π
−δµs
−δµu
δµa
π0
K0
ηs
0
0.5
1
1.5
2
2.5
3
-0.01
0
0.01
0.02
0.03
M 2
PS (a¯a)/X2
π
−δµs
−δµu
δµa
π0
K0
ηs
0
0.5
1
1.5
2
2.5
3
-0.01
0
0.01
0.02
0.03
M 2
PS (a¯a)/X2
π
−δµs
−δµu
δµa
π0
K0
ηs
0
0.5
1
1.5
2
2.5
3
-0.01
0
0.01
0.02
0.03
M 2
PS (a¯a)/X2
π
−δµs
−δµu
δµa
π0
K0
ηs
0
0.5
1
1.5
2
2.5
3
-0.01
0
0.01
0.02
0.03
M 2
PS (a¯a)/X2
π
−δµs
−δµu
δµa
π0
K0
ηs
0
0.5
1
1.5
2
2.5
3
-0.01
0
0.01
0.02
0.03
M 2
PS (a¯a)/X2
π
−δµs
−δµu
δµa
π0
K0
ηs
0
0.5
1
1.5
2
2.5
3
-0.01
0
0.01
0.02
0.03
M 2
PS (a¯a)/X2
π
−δµs
−δµu
δµa
π0
K0
ηs
0
0.5
1
1.5
2
2.5
3
-0.01
0
0.01
0.02
0.03
M 2
PS (a¯a)/X2
π
−δµs
−δµu
δµa
π0
K0
ηs
Figure 3: The neutral pseudoscalar meson masses M2
PS(a¯a) on the 483 × 96 lattice as a function
of δµD
a for quark charges ea = −1/3 (blue), 0 (green) and 2/3 (red). Solid (open) symbols refer
to unitary (PQ) masses. The horizontal lines display the physical π0, K0 and ηs meson masses,
the vertical lines indicate the physical u and s quark masses.
