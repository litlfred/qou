---
# qou-ti1n
title: 10 committed probes import build_hoefsmit_mpfr from an untracked scratch module; the canonical Hoefsmit builder is not in the repo
status: completed
type: bug
priority: normal
created_at: 2026-08-24T08:24:39Z
updated_at: 2026-08-24T08:29:39Z
---


## What was wrong

Ten committed probes under `computations/probes/` did

    from probe_staircase_ew_k3_categorical import build_hoefsmit_mpfr

and that module is **not in the repository**. It lived in one of the five
root-level agent-scratch dirs untracked by `0763606e4f`, so every one of those
probes has been unrunnable in a fresh clone ever since — their committed
witnesses could not be reproduced by anyone. Found while re-running producers
for the q₀ migration: 10 of 24 failures were this single `ModuleNotFoundError`.

`hoefsmit_seminormal_form_probe.py` states the stakes itself: *"A failure here
would invalidate every probe that uses canonical Hoefsmit downstream (the
entire H_n cluster of PR #818 and beyond)."* The gate for the cluster could
not run.

The repo already knew about the **class**: `producer-importability-audit`
records *"72 producers cannot import a module that lives in this repo … Each
one owns at least one committed witness that cannot be regenerated, so no
staleness check can ever fire on it"* — and closes **"Reported, not fixed."**
This closes the `probe_staircase_ew_k3_categorical` slice, 10 of the 72.

## Fix

`computations/hecke/hoefsmit_mpfr.py` — `build_hoefsmit_mpfr(shape, q)`, an
mpmath transcription of `_hoefsmit_build` from the live symbolic builder
`hecke_character_symbolic.py`. Not a guess: `_selftest` builds symbolically in
a sympy Symbol, substitutes q₀, and compares entrywise on every λ ⊢ n for
n = 2..6.

    4166 entries agree with the symbolic builder at 40 dps
    worst relative difference 2.64e-40   (the precision floor)

Three of the ten then failed on a display-only bug — `f"{mpf:.2e}"`, which
mpmath does not support — in their summary prints. The math had completed.
Wrapped in `float()`, matching each file's own idiom on adjacent lines.

## Measured

All ten run, **28 assertions, all passing** — quadratic relation, braid
relation, character closure, Markov transitions, amphicheirality. Those are
independent of the entrywise check: they verify the generators really are
Hoefsmit, not merely that two implementations agree.

The regenerated witnesses differ from the committed ones in two ways, both
expected:

1. **q₀ moved.** `q_0_50dps` 1.10997859555418… → 1.10997858275138…: these
   stems are not in `ideal_muon`, so they resolve to the proton pin, and the
   old witnesses carried the superseded muon value. Dependent values move at
   the 9th digit (`chi_21_single` −0.9106773300 → −0.9106773503), which is
   exactly the muon-proton separation.
2. **Every relation residue improved by ~20 orders of magnitude.**

```
max_hecke_quadratic_residue    5.35e-51 -> 3.62e-71
max_braid_relation_residue     2.67e-51 -> 1.81e-71
max_residue_across_tests       1.60e-50 -> 7.24e-71
max_1d_character_residue       3.21e-50 -> 8.15e-71
max_self_conj_residue          7.48e-50 -> 2.03e-69
```

The residues are the direct measure of "are these really Hoefsmit generators".
Building in mpf rather than substituting into a cancelled rational and
evaluating through sympy's float path is what buys those twenty orders — which
also says something about what the lost module was doing.

One entry looked alarming in a first pass — `chi_33_h6_residue` 5.35e-51 →
7.2445… — and was a **display truncation in my own diff tool**, which cut the
string at 44 characters and dropped the `e-71`. The real value is
7.244543263061369894…e-71, in line with every other residue, and now carried
as a 50-dps string rather than a float.
