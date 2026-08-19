---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral effective field theory and nuclear forces"
section_id: sec-005-221-relativistic-formulation
section_title: "Relativistic formulation"
section_number: 2.2.1
pages: 10-12
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
doc_brief: "Chiral effective field theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The next step in our EFT program is to build the most general Lagrangian consistent with the (broken)
symmetries discussed above. An elegant formalism for the construction of such Lagrangians was developed
by Callan, Coleman, Wess, and Zumino (CCWZ) [40] who worked out the group-theoretical foundations
of non-linear realizations of chiral symmetry. 3 It is characteristic for these non-linear realizations that,
whenever functions of the Goldstone bosons appear in the Lagrangian, they are always accompanied with
at least one space-time derivative. The Lagrangians given below are built upon the CCWZ formalism.
As discussed, the relevant degrees of freedom are pions (Goldstone bosons) and nucleons. Since the
interactions of Goldstone bosons must vanish at zero momentum transfer and in the chiral limit ( mπ→ 0),
the low-energy expansion of the Lagrangian is arranged in powers of derivatives and pion masses. The hard
scale is the chiral-symmetry breaking scale, Λχ≈ 1 GeV. Thus, the expansion is in terms of powers of Q/Λχ
where Q is a (small) momentum or pion mass. This is chiral perturbation theory (ChPT).
The eﬀective Lagrangian can formally be written as,
Leﬀ =Lππ +LπN + ... , (2.26)
3An accessible introduction into the rather involved CCWZ formalism can be found in Ref. [113].
10
whereLππ deals with the dynamics among pions,LπN describes the interaction between pions and a nucleon,
and the ellipsis stands for terms that involve pions and two or more nucleons. The individual Lagrangians
are organized as follows:
Lππ =L(2)
ππ +L(4)
ππ +... (2.27)
and
LπN =L(1)
πN +L(2)
πN +L(3)
πN +..., (2.28)
where the superscript refers to the number of derivatives or pion mass insertions (chiral dimension) and the
ellipsis stands for terms of higher dimensions.
To construct chiral Lagrangians, we introduce the followingSU (2) matrixU in ﬂavor space which collects
the Goldstone pion ﬁelds, π:
U = 1 + i
fπ
τ·π− 1
2f2π
π2− iα
f3π
(τ·π)3 + 8α− 1
8f4π
π4 +... , (2.29)
where fπ denotes the pion decay constant. In this expansion, the coeﬃcient of the term linear in the pion
ﬁeldπ is ﬁxed such as to produce the correct kinetic term in the ππ Lagrangian, below, and the coeﬃcient
of the quadratic term is chosen to satisfy the unitary condition U†U = 1, at second order in the pion
ﬁeld. However, the coeﬃcient α of the third order is arbitrary because of our freedom of choice for the
interpolating pion ﬁelds (constrained only by U unitary and detU = 1). The coeﬃcient of the fourth order
is then dictated by the unitarity condition, U†U = 1, at fourth order. Note that (on-shell) observables must
not depend on the choice for the pion ﬁelds or, in other words, they must not depend on the (unphysical)
parameter α (and there are more such parameters as you continue to higher orders in the above expansion
of U). Therefore, diagrams with vertices that involve three or four pions must always be grouped together
such that the α dependence drops out. For more on this issue, see the calculation of the two-loop 2 π and
3π contributions, below, where those vertices enter. Popular choices for the pion ﬁelds are the exponential
parametrization U = exp(iτ·π/fπ) which corresponds to α = 1/6 and the so-called sigma representation
U = (σ +iτ·π)/fπ with σ =
√
f2π−π2 which is equivalent to α = 0.
The leading order (LO) ππ Lagrangian is now given by [48]
L(2)
ππ = f2
π
4 tr
[
∂µU∂µU† +m2
π(U +U†)
]
, (2.30)
where tr denotes the trace in ﬂavor space and mπ is the pion mass. Since Goldstone bosons can interact
only when they carry momentum, the interaction between pions comes in powers of ∂µU. Only even powers
are allowed because of Lorentz invariance. Note that the U ﬁeld transforms under global chiral rotations via
U↦−→gLUg†
R (2.31)
with gR and gL elements of SU (2)R and SU (2)L, respectively, cf. Eqs. (2.11) and (2.12). Since we consider
global chiral rotations, gR and gL do not depend on space-time and, therefore, ∂µU transforms in the same
way as U. Thus, the ﬁrst term in Eq. (2.30) is clearly chiral invariant. The second term breaks chiral
symmetry explicitly with the coeﬃcient chosen such as to reproduce the correct mass term, which can be
seen by inserting U and expanding in numbers of pion ﬁelds:
L(2)
ππ = 1
2∂µπ·∂µπ− 1
2m2
ππ2 (2.32)
+1− 4α
2f2π
(π·∂µπ)(π·∂µπ)− α
f2π
π2∂µπ·∂µπ + 8α− 1
8f2π
m2
ππ4 + O(π6), (2.33)
where we dropped the constant term f2
πm2
π, since it does not contribute to the dynamics.
Baryon ﬁelds can also be incorporated into the eﬀective ﬁeld theory in a chirally consistent manner.
Gasser et al. [49] have derived the LO relativistic πN Lagrangian to be
L(1)
πN = ¯Ψ
(
iγµDµ−MN + gA
2 γµγ5uµ
)
Ψ (2.34)
11
with
Dµ =∂µ + Γµ (2.35)
the chirally covariant derivative which introduces the so-called chiral connection (an analogy to a gauge
term)
Γµ = 1
2
[
ξ†,∂µξ
]
= 1
2
(
ξ†∂µξ +ξ∂µξ†)
(2.36)
= i
4f2π
τ· (π×∂µπ) + O(π4), (2.37)
representing a vector current that leads to a coupling of even numbers of pions with the nucleon. Besides
this, the Lagrangian includes a coupling term which involves the axial vector
uµ = i
{
ξ†,∂µξ
}
=i
(
ξ†∂µξ−ξ∂µξ†)
(2.38)
= − 1
fπ
τ·∂µπ + 4α− 1
2f3π
(τ·π)(π·∂µπ) + α
f3π
π2 (τ·∂µπ) + O(π5), (2.39)
which couples an odd number of pions to the nucleon. The deﬁnition of ξ used in the above is
ξ =
√
U = 1 + i
2fπ
τ·π− 1
8f2π
π2− i(8α− 1)
16f3π
(τ·π)3 +... . (2.40)
Note that ξξ† = 1; therefore, ∂µ(ξξ†) = (∂µξ)ξ† +ξ∂µξ† = 0, which is applied in Eqs. (2.36) and (2.38).
Thus, more explicitly, the LO relativistic πN Lagrangian, Eq. (2.34), reads
L(1)
πN = ¯Ψ
(
iγµ∂µ−MN− 1
4f2π
γµτ· (π×∂µπ)− gA
2fπ
γµγ5τ·∂µπ +...
)
Ψ. (2.41)
In this equation, Ψ is the relativistic four-component Dirac spinor ﬁeld representing the nucleon,MN denotes
the nucleon mass and gA the axial-vector coupling constant. Numerical values will be given later. The term
proportional to gA/2fπ is the familiar axial-vector coupling of one pion to the nucleon, while the nonlinear
term proportional to 1 /4f2
π is known as the Weinberg-Tomozawa coupling (a 2 π contact term) [37, 38],
which is crucial for π-N s-wave scattering at threshold.
