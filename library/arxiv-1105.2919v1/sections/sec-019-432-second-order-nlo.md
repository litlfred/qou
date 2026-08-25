---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral effective field theory and nuclear forces"
section_id: sec-019-432-second-order-nlo
section_title: "Second order (NLO)"
section_number: 4.3.2
pages: 32-35
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
doc_brief: "Chiral effective field theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The contact Lagrangian ˆL(2)
NN , Eq. (2.62), which is part of ˆL∆=2, Eq. (2.67), generates the following NN
contact potential
V (2)
ct (⃗p′,⃗ p) = C1q2 +C2k2
+
(
C3q2 +C4k2)
⃗ σ1·⃗ σ2
+ C5
(
−i⃗S· (⃗ q×⃗k)
)
+ C6 (⃗ σ1·⃗ q) (⃗ σ2·⃗ q)
+ C7 (⃗ σ1·⃗k) (⃗ σ2·⃗k). (4.40)
32
The coeﬃcients Ci used here in the contact potential are, of course, related to the coeﬃcients C′
i that occur
in the Lagrangian ˆL(2)
NN , Eq. (2.62). The relation, which is unimportant for our purposes, can be found in
Refs. [54, 64].
There are many ways to perform the partial-wave decomposition of the above potential. We perceive
the method presented by Erkelenz, Alzetta, and Holinde [142] as the most elegant one. Thus, one obtains
V (2)
ct (1S0) = C1S0(p2 +p′2)
V (2)
ct (3P0) = C3P0pp′
V (2)
ct (1P1) = C1P1pp′
V (2)
ct (3P1) = C3P1pp′
V (2)
ct (3S1) = C3S1(p2 +p′2)
V (2)
ct (3S1−3D1) = C3S1−3D1p2
V (2)
ct (3D1−3S1) = C3S1−3D1p′2
V (2)
ct (3P2) = C3P2pp′ (4.41)
with
C1S0 = 4 π
(
C1 + 1
4C2− 3C3− 3
4C4−C6− 1
4C7
)
C3P0 = 4 π
(
−2
3C1 + 1
6C2− 2
3C3 + 1
6C4− 2
3C5 + 2C6− 1
2C7
)
C1P1 = 4 π
(
−2
3C1 + 1
6C2 + 2C3− 1
2C4 + 2
3C6− 1
6C7
)
C3P1 = 4 π
(
−2
3C1 + 1
6C2− 2
3C3 + 1
6C4− 1
3C5− 4
3C6 + 1
3C7
)
C3S1 = 4 π
(
C1 + 1
4C2 +C3 + 1
4C4 + 1
3C6 + 1
12C7
)
C3S1−3D1 = 4 π
(
−2
√
2
3 C6−
√
2
6 C7
)
C3P2 = 4 π
(
−2
3C1 + 1
6C2− 2
3C3 + 1
6C4 + 1
3C5
)
. (4.42)
4.3.3. Fourth order (N 3LO)
The contact potential of order four reads
V (4)
ct (⃗p′,⃗ p) = D1q4 +D2k4 +D3q2k2 +D4 (⃗ q×⃗k)2
+
(
D5q4 +D6k4 +D7q2k2 +D8 (⃗ q×⃗k)2
)
⃗ σ1·⃗ σ2
+
(
D9q2 +D10k2)(
−i⃗S· (⃗ q×⃗k)
)
+
(
D11q2 +D12k2)
(⃗ σ1·⃗ q) (⃗ σ2·⃗ q)
+
(
D13q2 +D14k2)
(⃗ σ1·⃗k) (⃗ σ2·⃗k)
+ D15
(
⃗ σ1· (⃗ q×⃗k)⃗ σ2· (⃗ q×⃗k)
)
. (4.43)
The rather lengthy partial-wave expressions of this order are relegated to Appendix E.
33
4.4. Deﬁnition of NN potential
We have now rounded up everything needed for a realistic nuclear force—long, intermediate, and short
ranged components—and so we can ﬁnally proceed to the lower partial waves. However, here we encounter
another problem. The two-nucleon system at low angular momentum, particularly, in S waves, is character-
ized by the presence of a shallow bound state (the deuteron) and large scattering lengths. Thus, perturbation
theory does not apply. In contrast to π-π and π-N, the interaction between nucleons is not suppressed in
the chiral limit (Q→ 0). Weinberg [50, 51] showed that the strong enhancement of the scattering amplitude
arises from purely nucleonic intermediate states (“infrared enhancement”). He therefore suggested to use
perturbation theory to calculate the NN potential (i.e., the irreducible graphs) and to apply this potential
in a scattering equation to obtain the NN amplitude. We will follow this prescription and discuss potential
problems in the next subsection.
Since the irreducible diagrams that make up the potential are calculated using covariant perturbation
theory (cf. Section 4.1), it is consistent to start from the covariant Bethe-Salpeter (BS) equation [143]
describing two-nucleon scattering. In operator notation, the BS equation reads
T =V +VG T (4.44)
where T denotes the invariant T-matrix ( T = iM withM the invariant amplitude) for the two-nucleon
scattering process, V the sum of all connected two-particle irreducible diagrams, and G is (−i) times the
relativistic two-nucleon propagator. The BS equation is equivalent to a set of two equations
T = V +V gT (4.45)
V = V +V (G− g)V (4.46)
= V +V1π (G− g)V1π +... , (4.47)
whereg is a covariant three-dimensional propagator which preserves relativistic elastic unitarity. We choose
the propagator g proposed by Blankenbecler and Sugar (BbS) [133] (for more details on relativistic three-
dimensional reductions of the BS equation, see Ref. [11]). The ellipsis in Eq. (4.47) stands for terms of
irreducible 3π and higher pion exchanges which we neglect.
Note that when we speak of covariance in conjunction with (heavy baryon) ChPT, we are not referring
to manifest covariance. Relativity and relativistic oﬀ-shell eﬀects are accounted for in terms of a Q/MN
expansion up to the given order and up to the number of pions we take into consideration. Thus, Eq. (4.47)
is evaluated in the following way,
V ≈ V (on-shell) + V1πGV 1π−V1πgV 1π (4.48)
≈ V1π + ~V2π +V1πGV 1π−V1πgV 1π (4.49)
= V1π + V′
2π, (4.50)
whereV1π denotes the relativistic (oﬀ-shell) 1PE, whileV1π is the on-shell 1PE given in Eq. (4.5). ~V2π stands
for the irreducible 2π exchanges calculated (on-shell) in Section 4.1.2, but without the covariant planar box
diagram, which in the above equations is given by V1πGV 1π. Furthermore, V1πgV 1π is the iterated 1PE
discussed in Section 4.1.2. Thus, the term (V1πGV 1π−V1πgV 1π) represents the irreducible part of the box
diagram contribution. Finally, V′
2π subsumes all 2π exchanges without the iterated V1π and is, therefore,
also known as the irreducible 2PE. Since all contributions are calculated on shell, the potential has no energy
dependence.
Adding the short-range contact terms Vct to the above, yields the full NN potential,
V =V1π +V′
2π +Vct. (4.51)
Notice that the pion-exchange part of this potential diﬀers from the perturbative amplitude, Eq. (4.30),
by the absence of the iterative 2PE. The latter is generated automatically when the potential is inserted
into a Schroedinger or Lippmann-Schwinger equation (see below). We also note that adding the contact
34
interactions to the pion interactions will generate loop corrections of the contact terms. This leads to a
