---
# qou-5pgl
title: 'AUDIT: hecke_core.z flipped C->D under every importer — 8 files carry constants calibrated before it'
status: todo
type: task
priority: normal
created_at: 2026-08-24T13:23:16Z
updated_at: 2026-08-24T13:24:08Z
---

Generalises the `alpha_high_precision` finding (`qou-l1gv`) from one file to its
class. Filed from PR #5622 (`qou-cds1`).

## The mechanism

`hecke_core` / `pyhecke.gram` were migrated to convention D (`5046347e53`,
`fcf09d2ff6`). Every file importing `z` from them therefore had its `z` change
by **+22.70 %** with **no edit to the file itself** — a file-local `git diff`
shows nothing. This is the import-cone drift class.

Confirmed instance: `alpha_high_precision.py`'s α* moved **+14.74 %** while the
producer sat at one unchanged commit, and the corpus still records the
pre-migration value (`docs/canonicalization-review.md` α* ≈ 0.305807).

**17 files import `z` from a D-migrated module.** Inheriting D is *correct* —
that is the ruling. The hazard is a **hardcoded constant calibrated before the
flip**, which now silently disagrees with the compute around it. That is the
same defect as the `6.17` (fa94034954), the `0.3948` (a24fdac8a1) and α* itself.

## Candidates — a HIGH-RECALL list, not a verdict

    3  computations/multiterm_cost_he3_l6a4_probe_algebraic.py   0.998367, 1.2999219630934102
    3  computations/multiterm_cost_deuteron_hopf_probe.py        2.224566, 1.1007832370743025, 1.636
    2  computations/alpha/alpha_high_precision.py                0.30, 0.32          <- CONFIRMED (qou-l1gv)
    1  computations/sweeps/paper_six_term_isotope_sweep.py       3.74446989
    1  computations/proton_residual_rootcause.py                 1.0
    1  computations/pn_alpha_lp_dual.py                          2.22452
    1  computations/mass_formula_6term.py                        0.0
    1  computations/hh-trefoil-corrected.py                      1.0

Triage by eye before spending a run on any of them:

- **Likely calibrated, worth checking first**: `1.2999219630934102` (17 digits —
  no physical constant is written that way by hand) and `3.74446989` (9 digits).
- **Experimental, convention-INDEPENDENT — do not chase**: `2.224566` / `2.22452`
  are the deuteron binding energy from AME, and `1.1007832370743025` is a q-like
  value. These are inputs, not calibrated outputs.
- **Trivial**: the `0.0` / `1.0` entries are almost certainly initialisers.

So the real queue is ~3 files, not 8.

## Method note — my FIRST detector reported a false clean

The first pass keyed on `expected=`, `assert abs(...) <`, and
`TARGET|REF|EXPECTED|CORPUS` names. It returned **0 of 17**, including for
`alpha_high_precision.py` — a file I had already *verified by hand* carries
`a_hi = mp.mpf('0.32')`. None of those spellings match a bare bracket bound.

Had I not had a known positive to check it against, I would have reported the
whole class clean. The rewritten detector carries a `SELFTEST` assertion on that
exact string and refuses to run if it stops matching. **Do not re-report this
list from a detector without a known-positive selftest** — this is the
thirteen-blind-spellings problem in AGENTS.md, and it caught me on the first
try here.

## Next step

Per candidate: `git log` the constant's introducing commit, check whether it
predates `5046347e53`, then run the producer and compare. Cheap for the three
real candidates. Do NOT mass-run all 17.
