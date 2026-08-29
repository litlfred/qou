---
doc_id: arxiv-hep-lat-9912004v2
doc_title: "Microscopic Universality and the Chiral Phase Transition in two Flavor QCD F. Farchioni"
section_id: sec-002-i-introduction
section_title: "INTRODUCTION"
section_number: I
pages: 1-2
source_pdf: 9912004v2.pdf
source_sha256: 7033719ec7a8a0bc
doc_brief: "Microscopic Universality and the Chiral Phase Transition in two Flavor QCD F. Farchioni — 9 sections: Hip; B. Lang; INTRODUCTION"
---
It is inherent to the lattice approach to quantum ﬁeld
theory, that one has to extrapolate from ﬁnite lattices, ﬁ-
nite statistics and non-critical coupling parameters to in-
ﬁnite lattices, inﬁnite statistics and critical points. Since
the result supposedly is a non-trivial, non-perturbatively
deﬁned quantum ﬁeld theory, this process is plagued by
uncertainties.
A typical example of such a situation,
where all these aspects combine, is the study of the ther-
mal transition in QCD for small quark masses. One is
interested in the continuum limit (gauge coupling g →0),
small or vanishing fermion masses (m →0), close to crit-
ical temperature (T →Tc) in the thermodynamic limit
(Lx →∞) — a formidable problem.
The extrapolations are always based on assumptions
on the asymptotic behavior. Well known examples are
scaling functions based on renormalization group and chi-
ral perturbation theory — an expansion around a ground
state with Goldstone bosons. Here we will examine an-
other such approach, which should allow the extrapola-
tion to inﬁnite volume and vanishing fermion mass: Chi-
ral Random Matrix Theory (chRMT).
A. Chiral Random Matrix Theory
RMT attempts to identify universal features of ensem-
bles of (random) matrices with common symmetry prop-
erties. Its chiral version, if successful, allows to separate
two aspects of a theory like QCD: the general universal
properties shared with other theories from the model-
speciﬁc “dynamical” content of the theory. Microscopic
eigenvalue distribution shapes are an example for the ﬁrst
aspect, expectation values of the fermion condensate for
the second.
The limitations for validity of the chRMT considera-
tions (for a given T in the phase of broken chiral symme-
try) are set by [1,2]
1
ΛQCD
≪Lx ≪
1
mπ
,
(1.1)
where Lx is the linear size of the system and mπ is the
mass of the lightest (pseudo-)Goldstone boson. The sec-
ond restriction imposes that the pion does not ﬁt into the
space-time volume and it therefore appears to be unphys-
ical. However, various correlators in the Dirac operator
spectrum can be computed precisely in this limit.
chRMT has been proven to give exact analytical pre-
dictions for the spectrum of the Dirac operator in the
microscopic limit [3]. The microscopic scaling region is
simply a blowup of the origin in the spectrum. To be spe-
ciﬁc, one considers eigenvalues λ on the scale
π
V Σ where
Σ is the chiral condensate, related to the spectral den-
sity per unit volume ρ(λ) via the Banks-Casher [4] re-
lation, Σ = limλ→0 limV →∞πρ(λ).
This regime is, by
deﬁnition, only well deﬁned in the spontaneously broken
phase where ρ(0)̸ = 0. In the phase with restored sym-
metry the scale of interest is set by the density of states
in the vicinity of the onset of ρ(λ).
1
Here we present a study of the microscopic correlators
in the spectrum of the staggered Dirac operator in SU(3)
gauge theory with dynamical fermions at ﬁnite tempera-
ture. Speciﬁcally we examine the low lying eigenvalue
statistics at temperatures below, near, and above the
critical temperature of the chiral phase transition.
Our analysis is based on the evaluation of the MILC
collaboration’s gauge conﬁgurations [5,6]. We therefore
concentrate on the new aspects connected to RMT ideas
for the spectral correlators of the Dirac operator. In par-
ticular for T > Tc we study the singularity at the inner
endpoint of the spectral density.
B. Temperature transition
Strictly speaking, in the continuum limit a →0, non-
zero temperature is realized for lattices n3
x × nt with
T = 1/(nt a(βg)) and nt/nx →0.
In that limit, for
vanishing quark mass m, one expects a phase transition
at Tc. In [5] the critical temperature was estimated to lie
between 143 and 154 MeV. For T < Tc chiral symmetry
is broken spontaneously, with massless pseudoscalars and

ψψ

̸
= 0; above Tc we expect restoration of this sym-
metry. Whereas for pure Yang-Mills theory the decon-
ﬁnement transition is associated with a breaking of the
center-symmetry with the Polyakov loop as order param-
eter, this symmetry is explicitly broken by the fermion ac-
tion. Nevertheless, remnants of the original breaking fea-
ture of the Polyakov loop persist even for small fermion
masses.
The nature of the chiral phase transition depends on
the number of ﬂavors Nf. An argument based on a 3D σ-
models analysis [7] predicts a ﬁrst order phase transition
for Nf ≥3. For Nf = 2 one expects a second order phase
transition with SU(2) × SU(2) ≃O(4) scaling behav-
ior. However, even ﬁrst order behavior may be arguable
[8–10]. For staggered fermions at non-vanishing lattice
spacing the correct counting of ﬂavors is unclear since
ﬂavor symmetry is restored only in the continuum limit.
Staggered fermions (as simulated by MILC with the hy-
brid R-algorithm [11]) correspond to the case Nf = 2
in the continuum limit.
On coarse lattices the so de-
ﬁned fermions should show at least U(1) ≃O(2) scaling
behavior.
For a discussion of the various scenarios cf.
[12–14].
It is unclear whether the phase transition at Tc extends
towards m > 0 or whether, when moving from lower to
higher temperature, one just observes crossover-like be-
havior. Some evidence points towards this second sce-
nario [15,12]. In the following, we denote the crossover
(phase transition) position by Tc(m) or simply Tc.
