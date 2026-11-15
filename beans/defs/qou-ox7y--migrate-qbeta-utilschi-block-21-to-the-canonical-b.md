---
# qou-ox7y
title: Migrate qbeta_utils.chi_block_21 to the canonical borromean form
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T08:08:28Z
updated_at: 2026-11-15T13:30:00Z
parent: qou-avtq
---


Follow-on from `qou-eddc`, which swapped `chi_block_21` in Lean. `qbeta_utils`
is the numeric mirror of that file and was still returning the grouped form, so
the two disagreed — and `qbeta_utils.delta_tau_M_surrogate` named the Lean
`delta_tau_M_surrogate` as its canonical source while contradicting it.

## Scoping it first

91 files import `qbeta_utils`; only four reach the affected functions, and two
of those only mention them in prose:

| site | reaches | action |
|---|---|---|
| `qbeta_utils.delta_tau_M_canonical_explicit` | yes | pass `intra_order` through |
| `qbeta_delta_tau_M_canonical_explicit_instance.py` | yes | re-run |
| `qbeta_reeb_tower_jacobi_anger.py` | yes | fix + re-run (below) |
| `qbeta_fmap_power_class_prune.py` | comment only | none |
| `qbeta_hecke_mn_character_engine_probe.py` | docstring only | none |

## Done

`chi_block_21`, `delta_tau_M_surrogate` and `delta_tau_M_canonical_explicit`
now take `intra_order`, defaulting to `"borromean"`, with `"grouped"` retained
and a hard `ValueError` on anything else. Checked at two pins in both frames
that the closed form equals the y_λ-weighted block sum to < 1e-45, and that
the borromean value at the proton pin agrees with the sympy path in
`qbeta_c3_multiblock_recursion_attack.py` to every digit printed.

### The Reeb-tower probe broke, correctly, and came back stronger

`qbeta_reeb_tower_jacobi_anger.py` raised `PolynomialError` immediately: its
`sinh_order_coeffs` multiplied by a hardcoded `q**5` because "powers run
|k| ≤ 5 for the H₃ β-characters", which was true only of the grouped frame.
Failing loudly was the right behaviour. Fixed by reading the shift off the
expression instead of hardcoding a wider literal, which would just move the
wall.

What came out is a genuine strengthening, not a repair:

    χ_(3)     orders [3,5]           (unchanged)
    χ_(2,1)   orders [1,3,5,7,9]     (was [1,3])
    χ_(1,1,1) orders [3,5]           (unchanged)

- The **parity claim survives to order 9** — every bar-odd block still has
  only odd sinh-orders. It did not have to; four new orders could each have
  broken it.
- χ_(2,1) now carries five orders **on its own**, so the single-x Bessel
  falsification runs on the ordering-dependent block directly. In the grouped
  frame no single block had three orders, so any (amplitude, x) fitted each
  block exactly and only the unit-weighted sum was falsifiable. Added as a
  second check; it fails at residual 1.478, alongside the sum's 1.404.

The verdict is unchanged in substance and now rests on a strictly stronger
test.

### Provenance, not just numbers

Re-running `qbeta_delta_tau_M_canonical_explicit_instance.py` first produced a
witness with a **weaker** environment block — `pyhecke_native` and
`pyhecke_native_build` dropped, because the module was not installed in this
container. The gate flagged it and says to install rather than commit the
weaker record. `tools/pyhecke-native/target/wheels/` already held a matching
cp311 wheel; installing it restored both fields (build hash differs, being this
container's build of the same 0.9.0). Worth knowing for the next session: that
wheel is in-tree and `pip install --no-index` is enough.

### Paper-facing blocks

`qbeta-per-block-chi-closed-forms.md` and
`qbeta-delta-tau-surrogate-taylor-coefficients.md` both stated the grouped
forms, so they had begun to contradict the Lean they cite. Both restated. The
Taylor table's "formal proof deferred" column is now wrong in the good
direction — every order 0..7 is proved sorry-free — and says so, with the
grouped-frame coefficients kept alongside so the two frames stay comparable.

### The content-block Lean sibling builds after all

`qbeta-per-block-chi-closed-forms.lean` compiles at 0 errors here, contradicting
`qou-lsib`'s "content-block Lean siblings do not build". It was migrated and
re-verified rather than left to diverge. Its scope is much smaller than the
library twin's — it stops at order 1 plus a note — so the swap was four edits.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — pointer

Tracked under carrier M5 (qou-eddc) of epic `qou-d8c7` "Mass endomorphism" (issue litlfred/qou#7547). Parent and status unchanged; the epic body lists what is still open for this item and where it sits in the attack-vector catalogue.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: DONE.** The migration landed in f1291a048a and both affected probes reproduce on main. The bean was reset to todo only by the 2026-10-04 claim sweep, not because work was outstanding.

Evidence: Commit `f1291a048a` (2026-09-07) is on main. `computations/qbeta/qbeta_utils.py:49/133/184`: `chi_block_21`, `delta_tau_M_surrogate` and `delta_tau_M_canonical_explicit` all take `intra_order="borromean"` and raise `ValueError` on anything else. Re-ran `qbeta_reeb_tower_jacobi_anger.py` (exit 0, `allPassed=True`, χ_(2,1) odd orders to 9 as claimed) and `qbeta_delta_tau_M_canonical_explicit_instance.py` (exit 0, 2/2, witness unchanged). The Lean sibling is at `folio/…/mass-endomorphism/qbeta-per-block-chi-closed-forms.lean`.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.

## Closed 2026-11-15 (owner tap, bean triage)

Status set to `completed`: the 2026-10-10 re-audit verdict was DONE, and on `main` (`0d4e4a005e`) `computations/qbeta/qbeta_utils.py::chi_block_21` defaults to the canonical `borromean` form (landed in `f1291a048a`).
