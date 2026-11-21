---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-013-92-stabilizer-states
section_title: "Stabilizer states"
section_number: 9.2
pages: 13-14
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
Stabilizer states
Pure stabilizer states |ψS⟩are states generated
by applying Clifford unitaries UC onto the |0⟩
state. Here, Clifford unitaries UC are unitaries
generated from Hadamard, S-gate and CNOT
gates [44].
Clifford unitaries map (under con-
jugation) any n-qubit Pauli operator P to some
n-qubit Pauli operator, P ′, i.e. P ′ = UCPU†
C. It
is known by the Gottesman-Knill theorem that
stabilizer states can be simulated efficiently on
classical computers [1, 43–45].
As shown in Ref. [16], any three-partite sta-
bilizer state |ψS⟩can be decomposed into GHZ
states, Bell states, and product states, dis-
tributed among the three parties, A, B, and C.
That is, |ψ⟩can be written as
|ψS⟩
=
UAUBUC |0⟩⊗sA
A
|0⟩⊗sB
B
|0⟩⊗sC
C
|GHZ⟩⊗gABC
ABC
|EPR⟩⊗eAB
AB
|EPR⟩⊗eAC
AC
|EPR⟩⊗eBC
BC
,
(59)
with UA, UB, UC unitary Clifford operators on
A, B, C, respectively, |EPR⟩AB denotes a two-
qubit EPR pair with one qubit in A and the other
in B (similarly for |EPR⟩AC and |EPR⟩BC), and
|GHZ⟩ABC is a three-qubit GHZ state with one
qubit in each of A, B, and C. Given the decompo-
sition above, one can directly see that the entan-
glement negativity is given by E(ρ) = eAB [93].
It can also be seen that the negativity spectrum
of stabilizer states is constrained to two values
Accepted in Quantum 2026-08-11, click title to verify. Published under CC-BY 4.0.
13
λi = ±√p3, i.e all eigenvalues λi of ρΓ are ei-
ther √p3 or −√p3. One can then obtain the PT
moments of stabilizer states as [21]
p2
=
1
2
gABC+eAC+eBC
p3
=
1
4
eAB 1
4
gABC+eAC+eBC
p4
=
1
4
eAB 1
8
gABC+eAC+eBC
.
(60)
The PT negativity for stabilizer states is then
given by a simple function of the PT moments
as [21]
E(ρ) = ˜E3(ρ)
for all stabilizer states.
(61)
This shows that stabilizer states are PPT iff they
satisfy the p3-PPT condition [40]. Analogously,
we find that
E(ρ) = E4(ρ)
for all stabilizer states.
(62)
Namely, stabilizer states saturate the bound in
Eq. (15). This also follows from the flatness of
the PT spectrum discussed above.
We now consider a tripartite system in a pure
state |ψ⟩∈HA ⊗HB ⊗HC, where |ψ⟩is a ran-
dom stabilizer state.
The entanglement phase
diagram as a function of the partition size can
be obtained using E(ρ) = ˜E3(ρ).
Since stabi-
lizer states form a 3-design [62, 123], we have
ES[p2,3] = EH[p2,3], where ES[.] denotes the av-
erage over stabilizer states.
Therefore, we can
again compute ES[E] by using the upper bounds
in Eq. (55) and obtaining a lower bound to ES[ ˜E3]
using a similar approach as in the Haar random
case.
Note that the upper bounds in Eq. (55)
are obtained from the second moments, and thus
they also apply to stabilizer states. One can then
verify that
ES[E] = ES[ ˜E3] ≃0,
(63)
for nC > nAB,
ES[E] = ES[ ˜E3] ≃1
2(nAB −nC) ln 2,
(64)
for nC < nAB and both nA < n/2 and nB < n/2,
and
ES[E] = ES[ ˜E3] ≃min(nA, nB) ln 2,
(65)
for nC < nAB and either nA > n/2 or nB > n/2.
In particular, the entanglement phase diagram
reproduces that of Haar random states, despite
the fact that stabilizer states do not form a 4-
design [124].
It was shown, for example, that
the quantity ˜r2, which is a function of the PT
moments up to the fourth order (see Eq. (19)),
takes different values across the phase diagram
for Haar random and stabilizer states [21], thus
also highlighting the limitation of ˜r2 in distin-
guishing entanglement phases. We further note
that, since the relation E(ρ) = ˜E3(ρ) is specific to
stabilizer states, the results presented above do
not necessarily extend to other state 3-designs.
Further, the realignment moments of stabilizer
states are given by [117]
rα
=
1
2
SAB+( α
2 −1)(SA+SB)
,
(66)
where SA denotes the entanglement of the sub-
system A. The CCNR negativity for stabilizer
states is then given by
C(ρ) = SA + SB
2
−SAB,
(67)
which also yields
C(ρ) = C4(ρ)
for all stabilizer states,
(68)
thus saturating the bound in Eq. (21). This im-
plies that the singular values of the realignment
matrix are flat.
