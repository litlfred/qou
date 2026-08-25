---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear effective field theory: status and perspectives"
section_id: sec-003-3-regularization-and-renormalization
section_title: "Regularization and renormalization"
section_number: 3
pages: 11-12
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
doc_brief: "Nuclear effective field theory: status and perspectives — 34 sections: Contents; Two-body scattering amplitude; Power counting"
---
Loops in a quantum ﬁeld theory are often not conver-
gent, and the same in true in Pionless EFT. Observables
are rendered ﬁnite by renormalization. For example, if we
introduce a regulator function f(x), the nucleon bubble
integral becomes
I0(k) =mN
∫ d3q
(2π)3
f(q2/Λ2)
k2− q2 + iε
=−mN
4π
[
θ1Λ−
√
−k2− iε +O(k2/Λ)
]
, (22)
where θ1 is a dimensionless number that depends on the
form of f(x) (for example, θ1 = 2/π for a step function).
With Eq. (12b) truncated at the scattering length as a
renormalization condition, the choice
C0(Λ) = 4π
mN
1
1/a0−θ1Λ (23)
ensures, to this order, that the physical amplitude is in-
dependent of Λ, up to corrections that vanish as Λ→∞ .
The latter can be removed by higher-order LECs, such
as C2(Λ). It is the non-analytic dependence on energy,
which is regulator independent, that characterizes a loop.
The corresponding term in Eq. (22) is an explicit example
of the estimates (15a) and (15b).
a. Schemes and power counting In early stages, there was
much confusion about whether or not the choice of reg-
ularization should be understood to aﬀect the power-
counting scheme. The diﬀerence between the artiﬁcial
regulator parameter Λ and the breakdown scale Mhi of
the theory has not always been appreciated. For exam-
ple, Kaplan et al. (1998a) have argued that C0∝ Λ−1
would again give a theory with a very limited range of
applicability. The need to choose Λ >∼ Mhi in order to
suppress regulator artifacts ∼O (1/Λ) does seem to in-
validate the scalingC0∝M−1
lo , but there are correlations
among the diagrams which are captured by determin-
ingC0(Λ) after resummation, reﬂecting the original Mlo
counting.
If one uses dimensional regularization to render in-
tegrals ﬁnite, the I0 bubble does not have a pole in
four spacetime dimensions, so in the minimal subtraction
scheme there would be no divergence at all. Instead of
this, Kaplan et al. (1998a) advocate explicitly subtract-
ing the pole in three dimensions (corresponding to the
linear divergence in the cutoﬀ scheme), thereby introduc-
ing a renormalization scaleµ, which can be chosen freely,
and giving Eq. (23) withθ1Λ→µ. This procedure, called
“power divergence subtraction” (PDS), makes the need
for resummation of the bubble diagrams more transpar-
ent. Picking µ∼Q, the running coupling C0 scales like
Q−1, implying again that each diagram in Fig. 3 is of
the same order. With this scheme, power counting is
“manifest” in the sense that it is reﬂected by the scal-
ing of coupling constants even after renormalization has
been carried out. Phillips et al. (1999) have shown that if
all poles of a divergent loop integral are subtracted—like
the original PDS, one particular choice of inﬁnitely many
possibly schemes—one recovers exactly the same result
as with a simple momentum cutoﬀ.
Under an appropriate power counting, changing the
low-energy points used as renormalization conditions af-
fects the running of the LECs by 1 /Λ terms, and leads
to the same T matrix up to higher-order terms. Taking
for example the pole position i γ instead of zero energy
generates the LO amplitude with 1 /a0→γ; the relative
diﬀerence is an NLO correction ∼r0/a0 =O(Mlo/Mhi).
While the a priori EFT error estimate is always deter-
mined by neglected higher orders, the freedom to choose
what input parameters are used at a given order can im-
prove agreement of the central values with experimental
data. Gegelia (1999a) discusses the relation of subtrac-
tive renormalization to the other approaches mentioned
above.
It was eventually realized (Lepage, 1997) that cutoﬀ
12
variation can be used (and is particularly useful in nu-
merical calculations) as a diagnostic for missing inter-
actions at a given order, an example of which will be
given in Sec. II.C.2. Long and Yang (2012b) pointed out
that also the leading residual cutoﬀ dependence can be
used to infer the existence of next-order operators. Equa-
tion (22), for example, indicates that C2∝M−1
hi in order
for the residual dependence on Λ >∼ Mhi to be no larger
than NLO. Thus renormalization provides guidance for
the power counting.
b. Subleading resummation Experience with nonsingu-
lar potentials makes it almost automatic to solve the
Schr¨ odinger equation exactly with a truncation of the
potential (16). At LO this is equivalent to the resum-
mation (13). Renormalization of the truncation at the
level of C2, however, leads to r0 <∼ Λ−1 (Cohen, 1997;
Phillips and Cohen, 1997; Scaldeferri et al., 1997), a ver-
sion of the so-called “Wigner bound” (Wigner, 1955).
This is problematic for NN scattering where r0 > 0. At
ﬁrst interpreted as a failure of EFT, this observation re-
veals instead the danger of resumming subleading singu-
lar potentials (van Kolck, 1999b). Such a resummation
includes a subset of arbitrarily high-order contributions
without all the LECs needed for perturbative renormal-
ization, such as C4 when C2 is inserted twice at N 2LO.
It is still possible to work with a ﬁxed cutoﬀ that repro-
duces r0, at the cost of losing the ability to use cutoﬀ
variation Λ >∼ Mhi as a diagnostic for missing interac-
tions. Moreover, there is no guarantee that results for
other observables will be any better than those obtained
from a perturbative treatment of subleading corrections.
An example is given by Stetcu et al. (2010a).
