---
# qou-okl8
title: Two producers write per-irrep-pole-deuteron-h6.witness.json (schema-lossy collision)
status: completed
type: task
priority: normal
created_at: 2026-08-16T21:23:41Z
updated_at: 2026-08-16T23:14:26Z
---

## Evidence (found while draining the deuteron chi cache, PR #5260)

Two producers emit the SAME witness filename with DIFFERENT schemas:

| producer | line | name emitted |
|---|---|---|
| `per_irrep_pole_atom.py` | 364 | `f"per-irrep-pole-{atom_name}-h{n}"` -> `per-irrep-pole-deuteron-h6` |
| `per_irrep_pole_deuteron_h6.py` | 226 | `"per-irrep-pole-deuteron-h6"` |

Whichever runs last wins, and the atom producer's schema is strictly richer.
Running the deuteron-specific script over a committed atom-produced witness
DELETES, among others:

    cemetery_class_signed_power_projection   net_signed_power
    is_pure_power_in_cemetery                per-gen_idx crossing breakdown
    sigma / sigma_inv / averaged counts       total_crossings

Measured on this branch: 230 deletions vs 39 insertions. I triggered it, caught
it in the diff, and restored from HEAD; nothing was lost. But nothing WARNED —
`WitnessBuilder` happily overwrites, so the loss is silent and the next agent
may not diff before committing.

Note the two agree on the physics (both give per-term poles 46/42/30/10 for the
colour-weighted word), so this is purely a schema/ownership defect, not a
numerical disagreement.

**Fix options:** (a) give the deuteron-specific script a distinct name, e.g.
`per-irrep-pole-deuteron-h6-poleonly`; (b) delete it as superseded by the
generalised atom producer (its docstring already says "same recipe as
per_irrep_pole_proton_h3 / per_irrep_pole_deuteron_h6"); (c) have
`WitnessBuilder.save()` refuse to shrink a witness whose committed copy carries
keys the new payload lacks, unless passed an explicit override. (c) is the
general guard and would catch the whole class.


---

## RESOLVED (PR #5260, 2026-08-16)

Fixed in two parts, and **my own proposed fix (c) was wrong on its keying**.

This bean proposed: *"(c) have `WitnessBuilder.save()` refuse to shrink a
witness whose committed copy carries keys the new payload lacks... (c) is the
general guard and would catch the whole class."* Refusing to **shrink** is the
wrong rule — ordinary schema evolution drops fields, so a shrink-guard fires
constantly on legitimate work and gets silenced. The signal is **ownership
change**, which `scriptFile` already records on every witness. Shipped guard
requires BOTH: a different `scriptFile`, AND field loss. A different producer
writing an equal-or-richer witness is a legitimate consolidation and passes
with a note.

The bean also called this "the whole class". Measured: a scan of every
`WitnessBuilder(...)` name in `computations/` found **zero** literal-vs-literal
collisions and exactly **two** template-vs-literal ones — both the same
generalised-supersedes-specific shape (`per-irrep-pole-deuteron-h6`,
`per-irrep-pole-proton-h3`). A small bounded family, not a widespread class, so
the guard is written to stay quiet.

**Measured false-positive risk before committing, not after a bug report:**
`save()` writes a bare `.name`, but 32 committed witnesses carry a
path-qualified `scriptFile` (`computations/foo.py`), 29 of which still resolve
to a live file. Raw string comparison would have flagged all 29 on their next
run. Comparison normalises to basename; regression test pins it. Nested payload
keys are deliberately not walked — per-partition tables change shape run to run.

Part 2: the two superseded scripts now **delegate** to
`per_irrep_pole_atom.run_atom(Z, N)` rather than colliding. The guard alone
would have left them permanently unable to write. `negative_q_pole_order` stays
at module level in the proton file — `per_irrep_pole_atom.py:69` imports it, so
that file is a library for the very producer that supersedes it as a script;
removing it broke the atom producer's import, which is how the dependency was
found.

Both docstrings' "**Verified result**" claims were stale and were removed
rather than carried: the deuteron named λ=(4,1,1) as maximizer (three rows ⇒
y_λ ≡ 0 ⇒ pole 0; actual (4,2) at 46), the proton claimed ord = 19 (actual 18).
Both are INCONCLUSIVE, not verified.

Escape hatch: `QOU_WITNESS_ALLOW_PRODUCER_TAKEOVER=1`.
7 new tests; full qou-substrate suite 59 passed; blocking precision gates green.

**Noted, not fixed (out of scope):** `scripts/sync-qou-mass-vendor.py --check`
reports 5 pre-existing drifted modules + 1 missing data file. Confirmed
pre-existing by re-running with this branch's changes stashed; none of the
drifted modules were touched here.
