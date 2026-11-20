---
# qou-27ys
title: 'RT finding: thm:topological-mass is a `theorem` whose Lean is a self-assuming projection and whose own proof says equality is open'
status: todo
type: bug
priority: high
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-20T08:40:00Z
parent: qou-ncxf
---

Found by the qou-ncxf pass-1 blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B08).

- Statement: `folio/quantum-observable-universe/mass-endomorphism/topological-mass.md`, kind `theorem` (`topological-mass.ts`).
- Lean: `folio/quantum-observable-universe/lean/QOU/Torsion/mass_decomposition_categorical.lean`. The proof term is `ctx.impl_mass_decomposition_categorical ctx.decomposition_active`. The conclusion is a field of `MassDecompositionCategoricalContext` applied to another field of the same class. RT-1 leg A and RT-2 leg B both flagged it independently as projection-of-assumption.
- Narrative proof: `folio/quantum-observable-universe/mass-endomorphism/topological-mass-proof.md`, lines 30–46. It proves only the upper bound m ≤ ‖Hol‖ + Σ Φ_q(z_i), and states that equality in the transient bound "is open". Two further gaps: orthogonality gives additivity of SQUARED norms, not of norms; and Φ_q(z_i) is used as a norm without an absolute value.

So the block's kind (`theorem`), its Lean (a projection) and its proof (a one-sided bound, equality open) disagree. Options: demote the block to `conjecture` (equality) plus a proposition (the ≤ bound); or keep it and state a conditional banner per §3b-cond (which fails rule 5, non-degenerate). This is mass-chapter scope (W1), so it is an owner/W1 decision. Asked on PR #8526. Do NOT close while the equality is open.
