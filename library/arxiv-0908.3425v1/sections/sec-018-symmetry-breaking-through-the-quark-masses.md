---
doc_id: arxiv-0908.3425v1
doc_title: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer"
section_id: sec-018-symmetry-breaking-through-the-quark-masses
section_title: "Symmetry breaking through the quark masses"
section_number: null
pages: 25-27
source_pdf: 0908.3425v1.pdf
source_sha256: 5e88d45bbc1c1b9b
doc_brief: "Chiral Perturbation Theory: Introduction and Recent Resul ts in the One-Nucleon Sector S. Scherer — We provide an introduction to the basic concepts of chiral pe rturbation theory and discuss some"
---
Up to now, we have assumed a perfect SU(3) L × SU(3)R symmetry. As has been discussed in Section
2.1.5, the quark-mass term of QCD results in an explicit symm etry breaking,
LM = −¯qRMqL − ¯qLM†qR, M =



mu 0 0
0 md 0
0 0 ms


. (99)
In order to incorporate the consequences of Eq. (99) into the eﬀective-Lagrangian framework, one makes
use of the following argument [Georgi, 1984]: Although M is in reality just a constant matrix and does
not transform along with the quark ﬁelds, LM of Eq. (99) would be invariant if M transformed as
M ↦→RML†. (100)
25
One then constructs the most general Lagrangian L(U, M) which is invariant under Eqs. (85) and (100)
and expands this function in powers of M. At lowest order in M one obtains
Ls.b. = F 2
0B0
2 Tr(MU † +UM†), (101)
where the subscript s.b. refers to symmetry breaking. In ord er to interpret the new parameter B0, let
us consider the Hamiltonian density corresponding to the su m of the Lagrangians of Eq. (90) and (101):
Heﬀ = F 2
0
4 Tr( ˙U ˙U †) + F 2
0
4 Tr(⃗∇U ·⃗∇U †) − Ls.b..
Since the ﬁrst two terms are always larger or equal to zero, Heﬀ is minimized by constant and uniform
ﬁelds. Using the ansatz
φ =φ0 + 1
F 2
0
φ2 + 1
F 4
0
φ4 + · · ·
for the minimizing ﬁeld values and organizing the individua l terms in powers of 1 /F 2
0 , one ﬁnds φ = 0
as the classical solution even in the presence of quark-mass terms. Now consider the energy density of
the ground state ( Umin =U0 = /BD ),
⟨Heﬀ ⟩min = −F 2
0B0(mu +md +ms), (102)
and compare its derivative with respect to (any of) the light quark masses mq with the corresponding
quantity in QCD,
∂⟨0|HQCD|0⟩
∂mq
⏐
⏐
⏐
⏐
⏐
mu=md=ms=0
= 1
3 ⟨0|¯qq|0⟩0 = 1
3 ⟨¯qq⟩0,
where ⟨¯qq⟩0 is the chiral quark condensate of Eq. (78). Within the framew ork of the lowest-order
eﬀective Lagrangian, the constant B0 is thus related to the chiral quark condensate as
3F 2
0B0 = −⟨¯qq⟩0. (103)
Let us add a few remarks.
1. A term Tr( M) by itself is not invariant.
2. The combination Tr( MU † −UM†) has the wrong behavior under parity φ(t,⃗ x) → −φ(t, −⃗ x).
3. Because M = M†, Ls.b. contains only terms even in φ.
In order to determine the masses of the Goldstone bosons, we i dentify the terms of second order in the
ﬁelds in Ls.b.,
Ls.b = −B0
2 Tr(φ2M) + · · ·. (104)
For the sake of simplicity we consider the isospin-symmetri c limit mu =md = ˆm so that the π0η term
vanishes and there is no π0-η mixing. The masses of the Goldstone bosons, to lowest order i n the quark
masses, are then given by
M 2
π = 2 B0 ˆm, (105)
M 2
K = B0( ˆm +ms), (106)
M 2
η = 2
3B0 ( ˆm + 2ms). (107)
26
Heisenberg ferromagnet QCD
Symmetry of Hamiltonian O(3) SU(3)L × SU(3)R
Symmetry of |0⟩ O(2) SU(3)V
Vacuum expectation value ⟨⃗M ⟩ ⟨¯qq⟩0
Explicit symmetry breaking External magnetic ﬁeld Quark masses
Interaction −⟨⃗M ⟩ ·⃗H ⟨Heﬀ ⟩of Eq. (102)
Table 6: Comparison between the symmetry-breaking pattern s of a Heisenberg ferromagnet and QCD.
These results, in combination with Eq. (103), B0 = −⟨¯qq⟩0/(3F 2
0 ), correspond to relations obtained
in Ref. [Gell-Mann et al., 1968] and are referred to as the Gel l-Mann, Oakes, and Renner relations.
Without additional input regarding the numerical value of B0, Eqs. (105) - (107) do not allow for
an extraction of the absolute values of the quark masses ˆ m and ms, because re-scaling B0 → λB0 in
combination with mq → mq/λ leaves the relations invariant. For the ratio of the quark ma sses one
obtains, using the empirical values Mπ = 135 MeV, MK = 496 MeV, and Mη = 547 MeV,
M 2
K
M 2π
= ˆm +ms
2 ˆm ⇒ ms
ˆm = 25.9,
M 2
η
M 2
π
= 2ms + ˆm
3 ˆm ⇒ ms
ˆm = 24.3. (108)
Let us conclude this section with a remark on ⟨¯qq⟩0. A non-vanishing quark condensate in the chiral
limit is a suﬃcient but not a necessary condition for a sponta neous chiral symmetry breaking. The
eﬀective Lagrangian term of Eq. (101) not only results in a sh ift of the vacuum energy but also in ﬁnite
Goldstone boson masses and both eﬀects are proportional to t he parameter B0. We recall that it was a
symmetry argument which excluded a term Tr( M) which, at leading order in M, would decouple the
vacuum energy shift from the Goldstone boson masses. The sce nario underlying Ls.b. of Eq. (101) is
similar to that of a Heisenberg ferromagnet which exhibits a spontaneous magnetization ⟨⃗M ⟩, breaking
the O(3) symmetry of the Heisenberg Hamiltonian down to O(2) . In the present case the analogue of
the order parameter ⟨⃗M⟩is the quark condensate ⟨¯qq⟩0. In the case of the ferromagnet, the interaction
with an external magnetic ﬁeld ⃗H is given by −⟨⃗M ⟩ ·⃗H, which corresponds to Eq. (102), with the
quark masses playing the role of the external ﬁeld ⃗H (see Table 6). However, in principle, it is also
possible that B0 vanishes or is rather small. In such a case the quadratic mass es of the Goldstone
bosons might be dominated by terms which are nonlinear in the quark masses, i.e., by higher-order
terms in the expansion of L(U, M). Such a scenario is the origin of the so-called generalized chiral
perturbation theory [Knecht et al., 1995]. The analogue wou ld be an antiferromagnet which shows a
spontaneous symmetry breaking but with ⟨⃗M ⟩= 0. The analysis of the s-waveππ-scattering lengths
[Colangelo et al., 2000], [Colangelo et al., 2001a] support s the conjecture that the quark condensate is
indeed the leading order parameter of the spontaneously bro ken chiral symmetry (see also Sec. 3.2.4).
