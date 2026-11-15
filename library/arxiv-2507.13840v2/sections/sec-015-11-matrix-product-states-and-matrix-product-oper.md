---
doc_id: arxiv-2507.13840v2
doc_title: "Quantifying mixed-state entanglement via partial transpose and realignment moments"
section_id: sec-015-11-matrix-product-states-and-matrix-product-oper
section_title: "Matrix product states and matrix product operators algorithms"
section_number: 11
pages: 15-15
source_pdf: q-2026-08-19-2194.pdf
source_sha256: 34ad8ede52fbf42e
toc_source: outline
doc_brief: "Quantifying mixed-state entanglement via partial transpose and realignment moments — 37 sections: Front matter; Preliminaries; Quantitative"
---
product operators algorithms
Here, we introduce algorithms to compute par-
tial transpose and realignment moments for ma-
trix product states (MPS) and matrix product
operators (MPO).
Let us consider a system of n qubits in a pure
state |ψ⟩given by an MPS of bond dimension χ:
|ψ⟩=
X
s1,s2,··· ,sn
As1
1 As2
2 · · · Asn
n |s1, s2, · · · sn⟩
(73)
with Asi
i being χ × χ matrices, except at the left
(right) boundary where As1
1 (Asn
n ) is a 1×χ (χ×
1) row (column) vector.
Here si ∈{0, 1} is a
local computational basis.
We then study the
entanglement within ρ = trC(|ψ⟩⟨ψ|), where C
is a subsystem of |ψ⟩. The case of translation-
invariant MPS is discussed in Appendix M.
We also consider a density matrix ρ of n qubits
represented in the following MPO form
ρ =
X
s,s′
W
s1,s′
1
1
W
s2,s′
2
2
· · · W sn,s′
n
n
|s1, · · · , sn⟩⟨s′
1, · · · , s′
n|
(74)
with W
si,s′
i
i
being χ × χ matrices, except at the
left (right) boundary where W s1,s′
1 (or W sn,s′
n) is
a 1 × χ (χ × 1) row (column) vector.
