---
# qou-27ys
title: 'RT finding: thm:topological-mass is a `theorem` whose Lean is a self-assuming projection and whose own proof says equality is open'
status: in-progress
type: bug
priority: high
created_at: 2026-11-20T08:40:00Z
updated_at: 2026-11-20T09:10:00Z
parent: qou-ncxf
---

Found by the qou-ncxf pass-1 blind round-trip audit (docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md, block B08).

- Statement: `folio/quantum-observable-universe/mass-endomorphism/topological-mass.md`, kind `theorem` (`topological-mass.ts`).
- Lean: `folio/quantum-observable-universe/lean/QOU/Torsion/mass_decomposition_categorical.lean`. The proof term is `ctx.impl_mass_decomposition_categorical ctx.decomposition_active`. The conclusion is a field of `MassDecompositionCategoricalContext` applied to another field of the same class. RT-1 leg A and RT-2 leg B both flagged it independently as projection-of-assumption.
- Narrative proof: `folio/quantum-observable-universe/mass-endomorphism/topological-mass-proof.md`, lines 30–46. It proves only the upper bound m ≤ ‖Hol‖ + Σ Φ_q(z_i), and states that equality in the transient bound "is open". Two further gaps: orthogonality gives additivity of SQUARED norms, not of norms; and Φ_q(z_i) is used as a norm without an absolute value.

So the block's kind (`theorem`), its Lean (a projection) and its proof (a one-sided bound, equality open) disagree. Options: demote the block to `conjecture` (equality) plus a proposition (the ≤ bound); or keep it and state a conditional banner per §3b-cond (which fails rule 5, non-degenerate). This is mass-chapter scope (W1), so it is an owner/W1 decision. Asked on PR #8526. Do NOT close while the equality is open.

## 2026-11-20 owner ruling and implementation (W11)
The owner answered "Y" to the [W11 ask] on #8526, choosing option 1: split. Branch `claude/topological-mass-split-2026-11-20`:
- `thm:topological-mass` is now `conj:topological-mass` (kind conjecture). The projection `lean.ref` is dropped.
- New `prop:topological-mass-upper-bound` with sibling `topological-mass-upper-bound.lean`, declaring `QOU.Torsion.mass_upper_bound_localised`. It is generic seminormed group, sorry-free, lean-direct exit 0, and uses only the axioms propext, Classical.choice and Quot.sound.
- Both proof blocks are retargeted to the new prop. Each claimed norm-additivity from orthogonality; they now conclude `≤`, with the squared-norm caveat.
- All `thm:topological-mass` references are relinked in 21 content files. `prop:mobius-energy` only needed the mass definition, so it now points at `def:mass-identity`.
- Stays in-progress until merged. The equality itself is an open conjecture; follow-up items are in qou-tm3c.
