---
# qou-0rp2
title: 'Salvage(gemini q-saddle): review real ''spherical partition algebra'' (arXiv 2402.01890, Ormeno-Bastias/Martin/Ryom-Hansen — NOT Bowman-Orellana) as driver-(x) grounding for nu_SDP'
status: todo
type: task
created_at: 2026-08-02T13:07:40Z
updated_at: 2026-08-02T13:07:40Z
---

## Source
Salvaged from the Gemini "q-deformed saddle-offsets" brainstorm (2026-08-02).
Gemini proposed identifying ν_SDP with the dimension of the idempotent
truncation of the "spherical partition algebra" (its "Option B"), citing
arXiv:2402.01890.

## Verification / CORRECTION
- Paper arXiv:2402.01890 **"On the spherical partition algebra" is REAL**
  (math.RT, 2024). It defines an idempotent subalgebra SP_k of the partition
  algebra P_k via the trivial-rep embedding of S_n.
- **Gemini HALLUCINATED the authors.** Actual authors: **Katherine Ormeño
  Bastías, Paul Martin, Steen Ryom-Hansen** — NOT "Bowman & Orellana".
  (Bowman–Orellana do have partition-algebra work, but not this paper.)
- Therefore Gemini's specific claims ("dimension = cardinality of MacMahon
  bipartite partitions", "Schur–Weyl duality with H_n(q)", "bimodule
  isomorphism to the active SDP constraint set") are **Gemini's paraphrase,
  NOT verified against the actual paper.** Read the real paper before adopting
  any of it.

## Task
1. Read arXiv:2402.01890 (Ormeño Bastías–Martin–Ryom-Hansen). Extract the ACTUAL
   dim SP_k formula and its combinatorial index set (verify or refute the
   "bipartite MacMahon" characterisation Gemini asserted).
2. Assess whether SP_k's dimension can *derive* ν_SDP as a partition-algebra
   count — this is the categorical home already claimed for
   `conj:kashaev-density-equals-sdp-multiplicity` under driver (x)
   "MacMahon-style partition-algebra identities". If it does, it upgrades
   ρ_F=ν_SDP from a 3-point coincidence toward a representation-theoretic count.
3. If it genuinely grounds the count, add ref + a Lean formalization angle
   (finite combinatorics is tractable in Mathlib). If not, record the negative.

## Priority / caveats
- LOWER priority than the 1-loop-torsion probe `qou-r307` (that one is a
  concrete number check; this is a lit-read + structural assessment).
- Anti-laundering: building SP_k in Lean and taking a class instance is NOT a
  proof of ρ_F=ν_SDP. Only a derivation is. Keep the conjecture conditional.
- The "q_0≈1.11 vs classical q=1 rigidity" gap Gemini waved at (its "Option C",
  Kazhdan–Lusztig SDP, arXiv:2604.18894) is NOT beaned: that arXiv id is
  unverified and Gemini could not name its authors — treat as likely
  fabricated until confirmed.
