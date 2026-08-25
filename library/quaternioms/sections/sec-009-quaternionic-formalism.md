---
doc_id: quaternioms
doc_title: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations"
section_id: sec-009-quaternionic-formalism
section_title: "Quaternionic Formalism"
section_number: null
pages: 8-9
source_pdf: quaternioms.pdf
source_sha256: becedcbc858611dd
doc_brief: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations — 40 sections: Introduction; Extended Related Work; Introduction: Bridging"
---
Many of the structural ingredients of this subsection are st andard in the literature
on quaternionic quantum mechanics and quaternionic quantu m computing. In par-
ticular, our use of right H-modules and adjoints follows the foundational treatments
in [ 3,4], while the existence of simulations of quaternionic circu its and channels by
complex ones builds on [ 6– 8]. Our contribution here is to package these ingredients int o
a self-contained circuit model tailored to quantum informa tion, and to connect them
explicitly to the complexity-theoretic results of Section 3.
State space and inner product on right H-modules.
We model an n-quaternionic qubit register by a ﬁnite-dimensional right H-Hilbert
module (H(n)
H , ⟨·, ·⟩). Single-quaternionic qubit pure states are as follows:
|φ ⟩ = q1|0⟩ + q2|1⟩, qi ∈ H, ∥q1∥2 + ∥q2∥2 = 1,
with quaternion-valued inner product (anti-linear in the ﬁrst slot, right-linear in the second):
⟨φ , ψ ⟩ = q1 p1 + q2 p2, P(ψ |φ ) = ∥⟨ψ , φ ⟩∥2 ∈ R≥0. (1)
Mixed states are positive trace-class R-linear functionals ρ on H(n)
H normalized by Tr(ρ ) = 1,
with Born’s rule computed from ( 1).
States versus operations.
In what follows we use the term “quaternionic state” to refer to a vector in a right
H-module (with components in H) and “quaternionic operation” to refer to a right- H-
Quantum Rep. 2025, 7, 55 8 of 40
linear map (gate) acting on such states. Whenever we pass from statements about states
(amplitudes, inner products) to statements about operations (unitaries, channels), we will
indicate this explicitly to avoid confusion between the two levels.
Observables, adjoints, and unitary dynamics.
Right H-linear maps A : H → H admit adjoints A† deﬁned by ⟨ψ , Aφ ⟩ = ⟨A† ψ , φ ⟩.
Self-adjoint observables satisfy A† = A and generate one-parameter unitary groups
as follows:
U(t) = exp
(
− i
¯h Ht
)
, U† U = I.
Projective/POVM measurements are deﬁned as in the complex case, with effects {Ej}
obeying 0 ≤ Ej ≤ I, ∑ j Ej = I and probabilities pj = Tr
(
Ejρ
)
.
Tensor products and multipartite structure.
Given right H-modules (H1, ⟨·, ·⟩1) and (H2, ⟨·, ·⟩2), we use the algebraic tensor prod-
uct over H and complete under the inner product:
⟨u1⊗u2, v1⊗v2⟩ := ⟨u1, v1⟩1 ⟨u2, v2⟩2, (2)
extended sesquilinearly . Associativity of H implies the canonical unitary reassociation
(H1 ⊗ H2) ⊗ H3 ∼= H1 ⊗ (H2 ⊗ H3), so multipartite composition and entanglement are
well-deﬁned (cf. Theorem 1).
Matrix embedding and gate synthesis.
We employ the multiplicative embedding ι : H֒→M2(C) which maps unit quater-
nions to SU(2) and satisﬁes ι(q1q2) = ι(q1)ι(q2) and ∥ι(q)∥2
F = 2∥q∥2. At the register level,
each k-quaternionic qubit gate U is compiled to a complex gate ι(U) acting on 2 k qubits
with constant-depth gadgets per elementary operation. This yields the following:
• Single-quaternionic qubit layer: ι identiﬁes unit quaternions with native SU(2) rotations
on the encoded pair, so calibrated single-qubit pulses implement quaternionic rotations
exactly (Lemma 1).
• Two-quaternionic qubit entanglers: Any standard entangling gate (e.g., CNOT/CZ) on
the encoded pairs realizes an entangler over H; universality follows from a dense
single-quaternionic qubit set plus one ﬁxed entangler (Proposition 1).
Universal sets and compilation ﬂow.
We adopt the universal library
GH = {R ˆn(θ ) on one encoded pair } ∪ { CNOT between encoded pairs },
where R ˆn(θ ) = exp(−iθ ˆn ·⃗σ /2) and ˆn ∈ S2. Arbitrary k-quaternionic qubit unitaries are
decomposed via standard (complex) synthesis on ι(U) (e.g., KAK/COSY/Solovay–Kitaev),
then mapped back to GH at constant overhead per gate. Measurement statistics are pre-
served because (A1) respects inner products up to a global scalar.
Implementation notes (encoded control).
On platforms with native SU(2) control (superconducting transmons, trapped ions,
NV centers, photonics), we target the encoded pair as the controllable SU(2) subsystem;
two-body couplings (e.g., cross-resonance, Mølmer–Sørensen, photonic beamsplitters)
serve as entanglers between encoded pairs. The layout sketches the superconducting case;
analogous mappings apply to other platforms. Gate ﬁdelities are those of the underlying
complex implementation (Section 3 discusses representative values).
