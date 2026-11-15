---
doc_id: arxiv-1301.6953v1
doc_title: "Chiral Perturbation Theory and Mesons"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-5
source_pdf: 1301.6953v1.pdf
source_sha256: 8c9231d0832df3b6
toc_source: inferred
doc_brief: "Chiral Perturbation Theory and Mesons — 7 sections: Front matter; Chiral Perturbation Theory; Introduction"
---
This talk is dedicated to my friend and collaborator Ximo Prades who died since the previous
Chiral Dynamics in Berne in 2009. For those of you who like to know more I recommend looking
up the slides from my talk at the symposium in Granada in his memory [1]. We have been very
frequent collaborators for a long time.
I will not attempt to give an overview of Chiral Perturbation Theory (ChPT) for mesons in this
talk. Even with the restrictions to mesons the subject is very large. I have given several review talks
earlier [2, 3] as well as written a review article of mesonic ChPT at two-loop order [4]. References
to other reviews and lectures can be found on my ChPT webpage [5], the remainder there has
admittedly a strong bias towards my own work.
I will give a short introduction to ChPT where I emphasize the major ideas underlying the
method. Afterwards I will give an overview of the work that has been happening in Lund in this
area in the last few years. In addition there are many more talks at this conference related to
mesonic ChPT. As far as the plenary talks are concerned these are the experimental tests from
NA48 [6] and KLOE [7], the connection with dispersion relations [8, 9] and the connection with
lattice QCD [10 – 12]. Most of the talks in the working group on Goldstone Bosons also fall under
the topic of this talk.
The remainder is ﬁrst a short introduction to ChPT, then an overview of the latest ﬁt of the
low-energy-constants, a few remarks about hard-pion-ChPT as well as some comments about ap-
plications of ChPT beyond QCD and some leading logarithm calculations to high orders. The
treatment is extremely cursory for all cases.
2. Chiral Perturbation Theory
ChPT in its modern form was introduced by Weinberg [13], and Gasser and Leutwyler [14, 15].
The best way to characterize ChPT is:
Exploring the consequences of the chiral symmetry of QCD
and its spontaneous breaking
using effective ﬁeld theory techniques
A good reference that shows in detail all the underlying assumptions is [16].
For an effective ﬁeld theory, one needs to indicate three things: the relevant degrees of free-
dom, a power-counting principle to have predictivity and the associated range of validity. For ChPT
these are
Degrees of freedom: The Goldstone Bosons from the spontaneous breaking of the chiral symme-
try present in QCD in the massless limit.
Power-counting: Dimensional counting in momenta and masses where meson masses and mo-
menta are counted the same in the standard counting.
Range of validity: The breakdown scale is when effects that are not included become important.
For mesonic ChPT these are clearly the meson resonances in the relevant channels. Mρ is
thus clearly the end of the range.
Chiral Perturbation Theory and Mesons
Johan Bijnens
Figure 1:
We need to pick
a vacuum expectation value
indicated by the arrow. The
massless mode corresponds
to an excitation along the bot-
tom of the valley.
rules:
one loop example:
p2
1/p2
R d4p
p4
(p2)2 (1/p2)2 p4 = p4
(p2)(1/p2) p4 = p4
Figure 2: An example of the power-counting, on the left the rules for
the lowest order vertex, propagator and loop integration. On the right
showing how it leads to the two one-loop diagrams being p4 while the
tree level lowest-order vertex is p2.
Let me show these now in a little more detail. Quantum Chromodynamics (QCD) for nF equal mass
quarks has an obvious global symmetry under the continuous interchange of the quarks SU(nF).
Looking at the purely strong Lagrangian (density)
LQCD = ∑
q=u,d,s
[i ¯qLD/qL +i ¯qRD/qR −mq( ¯qRqL + ¯qLqR)],
(2.1)
we see that in the limit of mq = 0 there is actually the larger SU(nF)×SU(nF)R global symmetry.
Another way to see is that in the massless case left- and right-handed are no longer related by
Lorentz-transformations since we cannot go the rest-frame of a massless particle.
The global chiral symmetry SU(3)L × SU(3)R in QCD is spontaneously broken to the vector
subgroup SU(3)V by the vacuum expectation value ⟨¯qq⟩= ⟨¯qLqR + ¯qRqL⟩̸ = 0. Since in this process
8 generators are broken we get 8 Goldstone Bosons and their interactions vanish at zero momentum.
This is shown pictorially for one broken generator in Fig. 1. The fact that the interaction vanishes at
zero momentum allows us to introduce a proper power-counting along the lines discussed in [13].
This is shown for the example of ππ-scattering at one loop in Fig. 2.
The basic principle just described has been used in very many circumstances. One needs to
decide which chiral perturbation theory is appropriate for the problem at hand. Some examples are
• Which chiral symmetry: SU(Nf)L ×SU(Nf)R, for Nf = 2,3,... and extensions to (partially)
quenched
• Or beyond QCD
• Space-time symmetry: Continuum or broken on the lattice: Wilson, staggered, mixed action
• Volume: Inﬁnite, ﬁnite in space, ﬁnite T
• Which interactions to include beyond the strong one
• Which particles included as non Goldstone Bosons
• My general belief: if it involves soft pions (or soft K,η) some version of ChPT exists.
Chiral Perturbation Theory and Mesons
Johan Bijnens
2 ﬂavour
3 ﬂavour
3+3 PQChPT
p2
F,B
2
F0,B0
2
F0,B0
2
p4
lr
i ,hr
i
7+3
Lr
i,Hr
i
10+2
ˆLr
i, ˆHr
i
11+2
p6
cr
i
52+4
Cr
i
90+4
Kr
i
112+3
Table 1: The number of terms at LO [19], NLO [14, 15]and NNLO [17] for standard mesonic ChPT.
An important technical step is the inclusion of external ﬁelds or sources. This allows to make
the chiral symmetry local1 [14, 15]. The manifold at the bottom of the potential in a symmetry
breakdown SU(nF)L × SU(nF) × SU(nF)V is also an SU(nF) manifold. We thus parametrize this
by an nF ×nF matrix which for nF = 3 is
U(φ) = exp(i
√
2Φ/F0),
with
Φ(x) =








π0
√
2
+ η8
√
6
π+
K+
π−
−π0
√
2
+ η8
√
6
K0
K−
¯K0
−2η8
√
6








.
(2.2)
The lowest-order (LO) Lagrangian is
L2 = F2
0
4 {⟨DµU†DµU⟩+⟨χ†U + χU†⟩},
(2.3)
with the covariant derivative DµU = ∂µU −irµU + iUlµ , and the left and right external cur-
rents/ﬁelds/sources: r(l)µ = vµ + (−)aµ. The scalar and pseudo-scalar external densities are in-
clude via χ = 2B0(s + ip). The latter allow the inclusion of quark masses via the scalar density:
s = M +···. The notation implies a ﬂavour trace ⟨A⟩= TrF (A). The next-to-leading-order (NLO)
Lagrangian was worked out by Gasser and Leutwyler [14, 15] and has 10+2 terms. The next-to-
next-to-leading-order (NNLO) Lagrangian is also known [17] as well as its inﬁnities [18]. The
number of terms is summarized in Tab. 1. All the cases listed above have extra terms in the La-
grangian with the exception of ﬁnite volume and temperature and in most cases the Lagrangian
is known to NLO. The constants in the Lagrangian are often referred to as low-energy-constants
(LECs).
So, what does ChPT really predict given the large number of free constants. It relates processes
with different numbers of pseudo-scalars and includes isospin and the eightfold way (SU(3)V). The
chiral logarithms can be seen in the two-ﬂavour ChPT NLO expression for the pion mass[14]
m2
π = 2B ˆm+
2B ˆm
F
2 
1
32π2 log (2B ˆm)
µ2
+2lr
3(µ)

+···
(2.4)
with M2 = 2B ˆm and remember that B̸ = B0, F̸ = F0, the constants in two and three ﬂavour ChPT
are not necessarily the same. The chiral logarithm is the log(2B ˆm) term. The inﬁnities are treated
by the relation between the bare and renormalized couplings and the renormalized couplings do
depend on the renormalization scale µ and the scheme used.
1It is not a gauge symmetry since no kinetic terms for the external ﬁelds are included.
Chiral Perturbation Theory and Mesons
Johan Bijnens
In two-ﬂavour ChPT [14] one uses conventionally the quantities ¯li = 32π2
γi lr
i (µ) −log M2
π
µ2 .
which are independent of the scale µ. For 3 and more ﬂavours, some of the γi are zero and one uses
the renormalized constants Lr
i(µ) directly. The result is in principle independent of µ but when
estimating some of the constants some choices might be better than others. The most standard
value is µ = mρ = 0.77 GeV since if we choose µ ≈mπ, mK the chiral logarithms vanish and if we
pick a larger scale of about 1 GeV then Lr
5(µ) ≈0 and arguments using a large number of colours,
Nc →∞are strongly violated.
A question which often comes up is in which quantities to expand, in particular whether to use
lowest-order or physical quantities. I would like to stress here that the expansion is in momenta and
masses but that it is not unique. There simply is no best way to do the expansion since relations
between the masses, e.g. the Gell-Mann–Okubo relation, exist. But even more, often there are
relations between the kinematical quantities and masses. An example is πK scattering with s +
t + u = m2
π + m2
K, or one can even use the scattering angle as a kinematical quantity. A related
note is that there can be remaining µ-dependence in a calculation where the µ-dependence is then
higher order. A naive example was discussed in the talk and can be found in [20] showing that the
apparent convergence of the chiral series can differ very much depending on what quantities one
expands in. In general, I prefer using the physical masses since thresholds are correct and the chiral
logarithms do come from physical particles propagating. However, sometimes there are simply too
many choices of physical masses possible, especially in partially quenched and staggered ChPT,
and for the sake of simplicity it might be easier to keep lowest-order masses everywhere.
