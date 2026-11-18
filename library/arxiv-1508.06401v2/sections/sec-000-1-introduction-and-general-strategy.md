---
doc_id: arxiv-1508.06401v2
doc_title: "Isospin splittings of meson and baryon masses from three-flavor lattice QCD + QED"
section_id: sec-000-1-introduction-and-general-strategy
section_title: "Introduction and general strategy"
section_number: 1
pages: 2-4
source_pdf: 1508.06401v2.pdf
source_sha256: 354f6e4ea835af6d
toc_source: outline
doc_brief: "Isospin splittings of meson and baryon masses from three-flavor lattice QCD + QED — Lattice QCD simulations are now reaching a precision where isospin breaking eﬀects become important."
---
Introduction and general strategy
Isospin breaking eﬀects are crucial for the existence of our Universe. Our Universe would not
exist in the present form if the n −p mass diﬀerence would only be slightly diﬀerent. If it would
be larger than the binding energy of the deuteron, no fusion would take place. If it would be a
little smaller, all hydrogen would have been burned to helium. Isospin breaking in hadron masses
has two sources, the mass diﬀerence of up and down quarks, and electromagnetic interactions.
Both eﬀects are of the same order of magnitude and cannot be separated unambiguously due
to the nonperturbative nature of the strong interactions. This makes a direct calculation from
QCD + QED necessary [1, 2, 3]. While substantial progress has been made, [3] is the only other
published work to report simulations with fully dynamical QCD + QED.
In [4, 5] we have outlined a program to systematically investigate the pattern of ﬂavor sym-
metry breaking in three-ﬂavor lattice QCD for Wilson-type fermions. Our strategy was to start
from the SU(3) symmetric point with all three quark masses equal, mu = md = ms, and ex-
trapolate towards the physical point keeping the average sea quark mass ¯m = (mu + md + ms) /3
constant. For this trajectory to reach the physical quark masses, ¯m is tuned to the physical value
of the average pseudoscalar meson mass X2
π =

M2
K0 + M2
K+ + 2M2
π0 −M2
π+

/3. We denote the
distance from ¯m by δmq = mq −¯m (q = u, d, s) . This implies δmu + δmd + δms = 0 on our quark
mass trajectory. To describe how physical quantities depend on the quark masses, we Taylor
expand about the symmetric point [5]. This results in polynomials in ¯m and δmq, which we clas-
sify into representations of the SU(3) and S3 ﬂavor groups. As we keep ¯m constant and change
only the octet part of the mass matrix, to ﬁrst order in δmq ﬂavor symmetry is broken by an SU(3)
octet, leading to Gell-Mann–Okubo mass relations. We follow a similar approach here with QED
added [2].
The symmetry of the electromagnetic current is similar to the symmetry of the quark mass
matrix. The simpliﬁcations that come from δmu+δmd+δms = 0 in the mass case are analogous to
the simpliﬁcations we get from the identity eu+ed +es = 0. A diﬀerence between quark mass and
electromagnetic expansions is that in the mass expansion we can have both odd and even powers
of δmq, whereas only even powers of the quark charges eq are allowed. We consider contributions
of O(e2
q) only. Hence, QED corrections can be simply read oﬀfrom the mass expansion presented
in [5], dropping the linear terms and changing masses to charges.
For the masses of octet mesons with the ﬂavor structure a¯b, and all annihilation diagrams
turned oﬀ, we ﬁnd to leading order in αEM
M2(a¯b) = M2
0 + α (δma + δmb) + βEM
0
(e2
u + e2
d + e2
s) + βEM
1
(e2
a + e2
b) + βEM
2
(ea −eb)2
+ γEM
0
(e2
uδmu + e2
dδmd + e2
sδms) + γEM
1
(e2
aδma + e2
bδmb)
+ γEM
2
(ea −eb)2 (δma + δmb) + γEM
3
(e2
a −e2
b) (δma −δmb)
+ γEM
4
(e2
u + e2
d + e2
s) (δma + δmb) + γEM
5
(ea + eb) (euδmu + edδmd + esδms)
(1)
up to corrections of O(δm2
q). Several of the coeﬃcients in (1) can be matched up with diﬀerent
classes of Feynman diagrams shown in Fig. 1. The ﬁrst diagram, with both ends of the photon
attached to the same valence quark, contributes to (βEM
1
+ βEM
2 ). The second diagram, with the
photon crossing between the valence lines, contributes to βEM
2 . The last diagram, with the photon
being attached to the sea quarks, is an example of a diagram contributing to βEM
0 . It would be
2
Figure 1: Examples of Feynman diagrams contributing to the meson electromagnetic mass to
O(e2
q). Wavy lines are photons, curly lines are gluons.
missed out if the electromagnetic ﬁeld was quenched instead of dynamical. Similar assignments
hold for the mixed (charge squared times mass) terms. For a single choice of sea quark masses,
the βEM
0
and γEM
4
terms can be absorbed into the constant M2
0 and the α term. However, for a
combined ﬁt of both QCD and QCD + QED data we will need these coeﬃcients. More details
can be found in [6]. Similarly, for octet baryons with the ﬂavor structure aab we ﬁnd to leading
order in αEM
M2(aab) = M2
0 + α1 (2δma + δmb) + α2 (δma −δmb)
+ βEM
0
(e2
u + e2
d + e2
s) + βEM
1
(2e2
a + e2
b) + βEM
2
(ea −eb)2 + βEM
3
(e2
a −e2
b)
(2)
up to corrections of O(δm2
q). This excludes the case of baryons with three diﬀerent quarks, as
in the Σ0 −Λ system [7]. Again, the βEM
0
term can be absorbed into the mass term M2
0. The
coeﬃcients βEM
1 , βEM
2
and βEM
3
can be matched up with distinct classes of Feynman diagrams
similar to the ones in Fig. 1.
Our goal is to compute the mass splittings of pseudoscalar mesons and octet baryons at the
physical point for QCD + QED. This amounts to determining the coeﬃcients α, βEM and γEM
in (1) and (2). It greatly helps to vary valence and sea quark masses independently [5], which
is referred to as partial quenching (PQ). In this case the sea quark masses remain constrained
by ¯m = constant, while the valence quark masses µu, µd and µs are unconstrained. Deﬁning
δµq = µq −¯m, the resulting modiﬁcation of Eq. (1) to PQ octet mesons is
M2(a¯b) = M2
0 + α (δµa + δµb) + βEM
0
(e2
u + e2
d + e2
s) + βEM
1
(e2
a + e2
b) + βEM
2
(ea −eb)2
+ γEM
0
(e2
uδmu + e2
dδmd + e2
sδms) + γEM
1
(e2
aδµa + e2
bδµb)
+ γEM
2
(ea −eb)2 (δµa + δµb) + γEM
3
(e2
a −e2
b) (δµa −δµb)
+ γEM
4
(e2
u + e2
d + e2
s) (δµa + δµb) + γEM
5
(ea + eb) (euδmu + edδmd + esδms) .
(3)
For octet baryons Eq. (2) becomes
M2(aab) = M2
0 + α1 (2δµa + δµb) + α2 (δµa −δµb)
+ βEM
0
(e2
u + e2
d + e2
s) + βEM
1
(2e2
a + e2
b) + βEM
2
(ea −eb)2 + βEM
3
(e2
a −e2
b) .
(4)
The coeﬃcients α, βEM and γEM in (3) and (4) are identical to those in (1) and (2). This is to say
that hadron mass splittings are unaﬀected by PQ at this order, as PQ moves (e.g.) all octet mesons
3
and baryons by the same amount. We would have to expand to cubic terms to see PQ errors in the
splittings [5]. Hence, PQ calculations oﬀer a computationally cheaper way of obtaining them.
In QCD + QED there is some ambiguity in the deﬁnition of the symmetric point. The deﬁ-
nition we have chosen is that the electrically neutral pseudoscalar mesons have the same masses,
M2(u¯u) = M2(d ¯d) = M2(s¯s) = M2(d ¯s) = M2(s ¯d) = M2(n¯n) , where n is a ﬁctitious electrically
neutral quark. As annihilation diagrams are neglected, diﬀerent neutral mesons do not mix. We
denote the Wilson hopping parameter κ (introduced in (7) below) marking the symmetric point
by ¯κq. We then have δmq = (mq −¯m) = 1/2κsea
q
−1/2¯κq and δµq = (µq −¯m) = 1/2κval
q −1/2¯κq,
setting the lattice spacing a = 1. It should be noted that even when all three quark masses are
equal we do not have full SU(3) symmetry. Because of their diﬀerent charges, the u quark is
always distinguishable from the d and s quark.
