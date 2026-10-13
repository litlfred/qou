---
# qou-byzu
title: 'NS vector 5: contact topology / Beltrami flows — the regular Reeb solution and its scope'
status: in-progress
type: task
priority: normal
created_at: 2026-10-12T20:57:49Z
updated_at: 2026-10-13T00:00:00Z
parent: qou-vo9t
---

Owner (2026-10-12): pursue NS attack vectors 1, 2, 3 and 5 (unforced NS). This bean is v5. Formalize first: a genuine Lean core lemma where one exists, honest conditional statements otherwise, and an audit doc.

## 2026-10-13: v5 result (branch `ns-v5`)

**Lean.** `QOU/FluidDynamics/BeltramiSteadyEuler.lean`: lean-direct exit 0, 0 sorry. The 18 key declarations depend only on `[propext, Classical.choice, Quot.sound]`.
- (A) Flat ℝ³ in coordinates, with Mathlib `deriv`:
  - the Lamb identity;
  - Beltrami + div-free ⇒ steady Euler with `p = −|u|²/2`;
  - Beltrami + `Δu = −μu` ⇒ `e^{−νμt}u` is an exact NS solution.
- (B) ABC on T³: `curl = id`, `div = 0`, `Δ = −id`, 2π-periodic, all computed. Hence `e^{−νt}u_ABC` is an exact global NS solution (`abc_ns_exact`).
- (C) The metric Lie algebra `(sl₂, diag(1,1,s²))`:
  - brackets checked as matrices;
  - the Koszul connection is torsion-free and metric;
  - `V` is Killing, `∇_V V = 0`, `curl V = −sV`;
  - `Ric V = (s²/2)V` and `∇*∇V = (s²/2)V`;
  - Weitzenböck holds on V, and `(Δ_H − 2Ric)V = 0`.

**Correction to the parent audit.** Under the deformation (Ebin–Marsden/Taylor) convention, V is a **steady** NS solution with no decay. Hodge gives `e^{−νs²t}V` and Bochner gives `e^{−νs²t/2}V`. The parent's `e^{−νt}V` is the Hodge case with `s = 1`.

**Not formalized [S].** The descent of left-invariant data to `Γ\PSL₂(ℝ) = UT(Σ₄)`. The identification of the model's Reeb field with V is inherited and not proved.

**Audit:** `docs/audits/2026-10-12-ns-v5-beltrami-reeb.md`. §5 is the draft proposition for the owner; it was NOT added as a content block.

**Status stays `in-progress`.** Adding the proposition is an owner decision. The underlying regularity question on M stays open.
