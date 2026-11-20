---
# qou-byzu
title: 'NS vector 5: contact topology / Beltrami flows — the regular Reeb solution and its scope'
status: completed
type: task
priority: normal
created_at: 2026-10-12T20:57:49Z
updated_at: 2026-11-20T08:32:31Z
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

## 2026-10-13: Q3 done (owner "Q3 y"), commit dfd4df94f0 on `ns-q2q3`

The audit section 5 draft is now a content block triple in `fluid-dynamics/`, listed after `torus-ns-regular` in `sec:ns-obstruction-tower-mtc`:
- `prop:reeb-beltrami-regular-flow` (`reeb-beltrami-regular-flow.{ts,md}`). Its `lean.ref` is `qou:QOU.FluidDynamics.BeltramiSteadyEuler.L3.deformation_V`, the existing library declaration; no new sibling `.lean`. The statement gives the `(X,Y,V)` frame, `g_s = diag(1,1,s^2)`, and the curl convention `(curl u)^flat = * d u^flat`, plus the three viscous operators with explicit solutions `aV` (deformation, steady), `a e^{-nu s^2 t} V` (Hodge) and `a e^{-nu s^2 t/2} V` (Bochner).
- `prf:reeb-beltrami-regular-flow`: the hand proof and the Lean lemma list. Not formalised: the descent to `Gamma\PSL2(R)`, the manifold-operator identification, and the PDE reduction.
- `rem:reeb-beltrami-regular-flow-scope`: one family on one manifold, nothing about generic data, regularity on M as open as on `T^3`. Topology carries the solution, so no bundle invariant forces blow-up. The identification of `V` with the cone-link Boothby-Wang Reeb field is inherited, not re-derived. `s` is free and not fitted.
- Gate: render preflight balanced; run-validate shows 8 issues, equal to the baseline; qa-sweep shows 0 fail and 0 warn on all three blocks.
- The proposition is fully proved modulo standard [S] steps, with the identification moved to the remark. No conjecture is closed or introduced. The bean stays in-progress for the owner to close.


**2026-11-20T08:32:31Z — owner-approved status change (coordinator session_01VQDpPdnjTBLBcPi6D5gj61, PR #8542 batch A):** in-progress → completed. Work commits 4daa381f5c7, 258e9121366 are on main.
