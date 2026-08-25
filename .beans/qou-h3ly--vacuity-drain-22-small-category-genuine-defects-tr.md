---
# qou-h3ly
title: 'VACUITY drain: 22 small-category genuine defects (trivial-true / docstring-sorry-mismatch / unused-hypothesis-rfl)'
status: completed
type: task
priority: normal
created_at: 2026-08-21T16:50:59Z
updated_at: 2026-08-21T21:28:39Z
---

## Tranche plan (22 defects / 17 files), grouped by fix pattern

- **G5 stale-docstring (2)** — doc-only: qou_obstruction_reduction::kappa_vanishes_iff_chi, nsi_q_deformed_kernel::nsi_q_kernel_identification
- **G1 `∃ X, True` (6)** — Conjectures::exists_knot, NonAbelianStokes::yekutieli_finite_slice_substrate, UpstreamSubstrateBridge::{lie_valued_stokes,markov_axiom_h1_to_h2,markov_axiom_h2_to_h3,yekutieli_finite_slice}_discharged
- **G2 reflexive X=X (6)** — CyclotomicCl3OrbitSum::orbit_sum_general, CyclotomicTrilogImaginary::closed_form_holds, H4Cyclicity::trM4_cyc_{1_1,2_2,6_6}, MmuR9V9Closure::universal_habiro_closure
- **G3 tautology-on-literal (7)** — descartes-braid-structure::colour_sector_count, c-equals-bar-iff-all-1dim::exactly_two_one_dim_irreps, DeltaMaxNumericalScale, PlancherelViaRecipe, ChannelSeparation::kahler_differentials_no_sym_component, GradedFrobeniusHopf::degree_zero_dim_one, meson-kaon-pion-hecke-seifert::meson_squaring_exponent
- **G4 placeholder-True (1)** — WallCrossing::primitive_KS_is_pentagon

Honest dispositions only (AGENTS §1a): prove / state-with-sorry+Ref / demote. No fabrication; where the real content is open, demote or name-as-predicate rather than invent a claim.

## DONE 2026-08-21 — all 22 drained (PR #5408)

Dispositions: 8 restated against real content, 7 demoted to named `def` +
a falsifiable companion, 6 dropped (restating would have relabelled the
defect, not fixed it), 1 deferred with a bean.

**Three findings worth more than the count:**
1. **Self-certifying carriers.** `NonAbelianStokes` / `LieValuedStokes`
   declare `p : Prop` *and* `p_witness : p`, so they are inhabited by
   taking `p := True` — which their own instances do. No existence or
   `Nonempty` claim about such a class is falsifiable, so those defects
   cannot be fixed by de-`True`-ing them. Bean qou-ewc4.
2. **A shadowing stub with a mis-aimed content ref.** Two declarations
   share the name `QOU.BraidsAndKnots.plancherel_via_recipe`; the real one
   is in y-lambda-recipe-from-partition.lean and a `.ts` `lean.ref` points
   at the vacuous twin. Bean qou-sz98.
3. **A false theorem, and a file broken on main.**
   c-equals-bar-iff-all-1dim.lean had 5 pre-existing errors;
   `c_equals_bar_on_one_dim_eigenvalue_neg_q_inv` is false (-3q = q).
   Bean qou-citp.

Ledger genuine count should drop 155 -> 133 on re-seed. Remaining tranches:
proof-no-provable-axiom (10) and proof-no-self-assuming-projection (123).
