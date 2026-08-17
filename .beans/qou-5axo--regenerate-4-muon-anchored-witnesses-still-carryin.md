---
# qou-5axo
title: Regenerate 4 muon-anchored witnesses still carrying the proton-y_lambda straddle
status: completed
type: task
priority: normal
created_at: 2026-08-17T01:01:34Z
updated_at: 2026-08-17T01:54:38Z
---

## Origin (PR #5260, bean qou-tzsp)

`tr_M_via_wenzl_bridge_mpfr` defaulted its y_λ table to the **proton** witness
(`_Y_LAMBDA_DEFAULT`), so every caller evaluating at the **muon** pin combined
proton y_λ with muon χ. Fixed at the producer on #5260 — the bridge now selects
the table by the layer of `q_str`.

`atomic-tr-m-mpfr-50dps.witness.json` was regenerated there and its
bridge-vs-peel gap collapsed from ~1e-9 to the 50-dps floor on all five atoms.
**Four muon-anchored witnesses from the same 14 importers were NOT regenerated**
and still carry values computed under the straddle:

  * `binding-canonical.witness.json`         (binding_canonical.py)
  * `mass-table-comprehensive.witness.json`  (mass_table_comprehensive.py)
  * `wedderburn-lp-ew-wiring.witness.json`   (wedderburn_lp_ew_wiring.py)
  * `ame-2020-binding-energies.witness.json`

Expected size of the correction, from the atomic case: ~3e-10 to ~2.2e-9
absolute on tr_M, i.e. the 11.54 ppb μ–p tension propagated through y_λ. That
is **above** the L1 1 ppQ compute-precision target, so these are not
below-noise; whether any downstream *conclusion* moves is unmeasured and is the
first thing to check per witness.

Not done on #5260 because each needs its producer re-run and its own
before/after diff read, and #5260 was already carrying three unrelated items.
Not a blocker for it: the defect is fixed at the producer, so anything
regenerated from here on is correct.

Check the q₀-anchor stamp on each before assuming it is muon — the list came
from `q0Anchor == "muon"`, and witnesses without the stamp were not surveyed,
so this list is a lower bound.


---

## PREMISE REFUTED — nothing to regenerate (measured 2026-08-17)

**This bean should not have been filed as written, and the blast-radius number
that produced it was wrong.** None of the four witnesses carries the straddle.

I selected them by `q0Anchor == "muon"` — a **recorded stamp** — instead of by
**the q their producer actually passes to the bridge**. All three producers
(`binding_canonical.py`, `mass_table_comprehensive.py`,
`wedderburn_lp_ew_wiring.py`) call `tr_M_via_wenzl_bridge_mpfr` with
`q_parameter.Q_50_DIGIT_STR`, and that value is **proton**
(`1.1099785827513808…`, `anchor_of_q0` -> `proton`). The fix therefore selects
the proton table, which is exactly what the old `_Y_LAMBDA_DEFAULT` already
did: **no change, by construction.**

Confirmed by running rather than by arguing:

| producer | witnesses | result |
|---|---|---|
| `binding_canonical.py` | binding-canonical, ame-2020-binding-energies | env drift only; ame-2020 byte-identical |
| `wedderburn_lp_ew_wiring.py` | wedderburn-lp-ew-wiring | changed — but see below, NOT from this fix |

So `atomic-tr-m-mpfr-50dps` was the **only** witness affected, and it was
already regenerated on #5260. The corrected blast radius is **1, not 5**.

This is the same error shape I spent the session correcting elsewhere:
trusting a recorded label over the computation it claims to describe.

## Two real findings surfaced while refuting this one

**(a) Four witnesses are stamped `muon` but computed at `proton`.**
`binding_canonical.py:65` does `from q_parameter import Q_MP as q0`, and
`Q_MP` is **proton** at runtime (verified) — yet the witness it writes records
`q0Anchor: muon` AND `parameters.q0` = the muon value, on a **fresh** run.
So the stamp does not describe the computation. `q0_anchor_consistency_audit`
reports `Q0_FLIP: 0` because it checks `q0Anchor` against `q0Value` for
*internal* consistency — both say muon, so it is self-consistent and wrong.
Not diagnosed further here; it is a separate investigation with its own blast
radius, and it is NOT fixed by the bridge change.

**(b) `wedderburn-lp-ew-wiring.witness.json` is stale on main.** Re-running its
producer moves `t_legacy_matrix_entries` 0.6003377 -> 0.6803697 (~13%).
Verified **pre-existing**: it reproduces with this branch's changes stashed, so
it is not caused by the bridge fix. A 13 % move is far too large to be the
1e-9 straddle and needs its own diagnosis.

Both are filed separately rather than folded in here.


---

## The CONCLUSION stands; the REASON I gave for it was wrong (2026-08-17)

Blast radius is still **1**, but not for the reason recorded above.

I wrote: "all three producers call the bridge with `Q_50_DIGIT_STR`, and that
value is proton". **False.** `q_parameter` auto-selects by the running
producer's stem, and all three are in the manifest's `ideal_muon`, so in a real
producer run that constant is **muon** — see bean qou-l1wd, refuted for the
same reason.

The actual reason those four witnesses are unaffected: **the bridge is never
called.** `binding_canonical.py` reaches `tr_M_via_wenzl_bridge_mpfr` only
under `use_closed_form`, which defaults to **False**; its default run's log has
zero bridge mentions, as does `wedderburn_lp_ew_wiring`'s.

Re-verified the right way — running each producer with and without the branch's
changes and diffing the witnesses modulo ephemeral fields:

    wedderburn_lp_ew_wiring:  with-fix == without-fix  -> True

So: unaffected because they do not exercise the changed code path, not because
they compute at a different pin. Same conclusion, sound basis.
