---
# qou-5pgl
title: 'AUDIT: hecke_core.z flipped C->D under every importer — 8 files carry constants calibrated before it'
status: todo
type: task
priority: normal
created_at: 2026-08-24T13:23:16Z
updated_at: 2026-08-24T13:29:48Z
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


## Candidates CONFIRMED pre-flip (dates, 2026-08-24)

    D migration landed          5046347e53   2026-08-16
    both candidate constants    f9ad94d750   2026-08-01     (15 days earlier)

      1.2999219630934102  multiterm_cost_he3_l6a4_probe_algebraic.py
      3.74446989          sweeps/paper_six_term_isotope_sweep.py

So both were calibrated under convention C and have had the ground moved under
them. That upgrades them from "suspected" to **confirmed pre-flip**; what is
still unmeasured is how far each one now disagrees with its own compute, which
needs the producer run.

**And `f9ad94d750` is the same commit that introduced `alpha_high_precision.py`
and wrote α* ≈ 0.305807** (`qou-l1gv`). So this is not three unrelated files —
it is **one 2026-08-01 landing whose constants were all calibrated in convention
C**, with the 2026-08-16 migration moving the ground under the whole set. The
one member already measured drifted **+14.74 %**.

That sharpens the queue definition considerably: the candidate set is
*constants introduced by `f9ad94d750` in files that import `z` from a
D-migrated module*. Worth checking whether `f9ad94d750` touched other such
files beyond the three found by the literal scan — a constant can be
C-calibrated without being a bare decimal literal (it may be built from an
expression), which the literal detector cannot see. **The 8-of-17 count is a
floor, not a total.**


## 🛑 RETRACTION (same session): the "one 2026-08-01 landing" narrative is a SHALLOW-CLONE ARTIFACT

The note above says both candidate constants were "introduced by `f9ad94d750` on
2026-08-01", and infers **"one landing whose constants were all calibrated in
convention C"**. That inference is **withdrawn.**

    $ git rev-parse --is-shallow-repository    ->  true
    $ git log --reverse | head -1              ->  f9ad94d750  2026-08-01
    $ git show --name-only f9ad94d750 | wc -l  ->  28348

`f9ad94d750` is the **shallow-clone boundary** — the oldest commit this clone
has. A grafted root appears to add the entire tree, which is why it "touches"
28,348 files and why **all 17** z-importers are in it. Co-occurrence there is
evidence of nothing: everything is in it.

Likewise `git log -S<constant>` terminating at `f9ad94d750` means only *"the
constant is present at the clone boundary"* — not that it was authored there.

**What survives, and it is the part that matters:** the constants exist at
2026-08-01 and the D migration (`5046347e53`) landed 2026-08-16, so they **do**
predate the flip. The candidates are still confirmed pre-flip. What is withdrawn
is the stronger story that they form one deliberately co-calibrated set.

This is the exact hazard AGENTS.md names — *"a sha can be missing merely because
the history was never fetched"* — and I walked into it by reading a boundary as
a landing. **Do not date-reason from `git log` in this clone without checking
`--is-shallow-repository` first.**
