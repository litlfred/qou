---
doc_id: quaternioms
doc_title: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations"
section_id: sec-014-cayleydickson-product
section_title: "Cayley–Dickson Product"
section_number: null
pages: 14-16
source_pdf: quaternioms.pdf
source_sha256: becedcbc858611dd
doc_brief: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations — 40 sections: Introduction; Extended Related Work; Introduction: Bridging"
---
Writing (a, b), (c, d) ∈ H ⊕ He6,
(a, b) · (c, d) = ( ac − ¯d b, dc + b ¯c),
exposes quaternionic subalgebras and clarifies how non-associativity emerges beyondH [2,5].
2.11. Associative Subalgebras and Conﬁnement
Each embedded copy of H in O is associative. Conﬁning states and gates to such a
sector restores well-deﬁned composition; switching sectors incurs control overheads [ 5].
Construction: Choose a triple from the Fano plane and ﬁx an embedding as follows:
Quantum Rep. 2025, 7, 55 14 of 40
H ∼= spanR{1, ei, ej, ek}.
Implement all gates within this sector using the quaternionic toolset of Section 2.6; switching
sectors is effected by explicit sector-change pulses that map one quaternionic copy to another
(compiled as products of associative factors).
T rade-offs: Sector switches add depth and calibration overhead; strict conﬁnement
limits reachable unitaries unless multiple sectors are orchestrated.
(M2) G2-invariant coding.
Goal: Detect excursions that activate associators by encoding into subspaces stabilized
by Aut(O) ∼= G2.
Construction: Pick stabilizers whose action commutes with the chosen associative
sector; design syndrome measurements whose nontrivial outcomes ﬂag associator-inducing
components. Logical operations are compiled to respect G2-invariance.
T rade-offs:Detection ̸= full correction; tensor non-canonicity persists, so large-scale
composition still rides on (M1)/(M4).
(M3) Associator-suppressing dynamical decoupling (ASD).
Goal: Cancel coherent associator contributions in U(t) order-by-order.
Cycle: Within a ﬁxed H ⊂ O, apply a symmetric cycle as follows:
(
Ux Uy Uz
)
free evol. ∆ t
(
U†
z U†
y U†
x
)
,
with Uα fast H-rotations and timing chosen so ﬁrst nontrivial associator terms average to
(near) zero over the cycle (Algorithm A1 in Appendix C).
Performance characterization: Short-time process ﬁdelity improves relative to associative-
agnostic baselines; residual higher-order terms and ﬁnite-width pulses limit asymptotics.
(Representative summaries appear in Figures 3 and 4 of the main text.)
(M4) Seven-factor algebraic synthesis.
Goal: Compile a target transformation U as a product of gates, each conﬁned to an
associative subalgebra, thereby making parenthesization explicit and controllable.
Ansatz:
U ≈ U1U2 · · · U7, Uℓ ∈ exp(hℓ), hℓ ⊂ O associative,
with the hℓ selected (e.g., via Fano-plane guided heuristics) to minimize cumulative associ-
ator growth. Each Uℓ compiles with the quaternionic pipeline of Section 2.6.
T rade-offs: Increased depth and error accumulation across factors; well-suited as a
simulation/veriﬁcation tool rather than a native octonionic architecture.
Figure 3. Process ﬁdelity vs. time under CDD 2-like ASD sequences: Associative-constrained (S) vs.
associative-agnostic (A). Short-time gains are consistent with Theorem 4. Adapted from [ 72].
Quantum Rep. 2025, 7, 55 15 of 40
Figure 4. Process-ﬁdelity decay as a function of total control time T (a) and control amplitude α
(b) under associator-affected dynamics. ASD attenuates leading decay slopes at small T for moderate
α . Adapted from [ 73].
Resource and ﬁdelity accounting.
For each strategy , we track: (i) depth overhead ∆ D vs. complex/quaternionic baselines;
(ii) width/ancilla usage (notably for G2 syndromes); (iii) calibration load (sector switches, ASD
pulses); (iv) ﬁdelity impact modeled at the process level (SPAM-corrected) using the same
ﬁgures of merit as in the quaternionic embedding. These metrics are reported alongside
