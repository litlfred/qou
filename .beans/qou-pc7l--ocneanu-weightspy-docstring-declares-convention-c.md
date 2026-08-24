---
# qou-pc7l
title: ocneanu_weights.py docstring declares convention C while its code runs convention D
status: todo
type: task
priority: normal
created_at: 2026-08-23T18:17:07Z
updated_at: 2026-08-23T18:18:41Z
---

## Evidence

`computations/ocneanu_weights.py` module docstring (lines 6-8):

    Symmetric convention:
        sigma^2 = (q - q^-1) sigma + 1     (eigenvalues  q, -q^-1)
        z = 1 / (q^{1/2} + q^{-1/2})   (Markov parameter)

Its code (line 70):

    z_num = Q0**3 / (Q0**2 + 1)

At the live `q0 = 1.1099785827513808` those are **0.49932033418369445** (declared) and
**0.61268803714646524** (actual) -- a 23 % difference, not a rounding issue. The declared
form is convention **C**; the code runs convention **D**.

Per the owner ruling of 2026-08-15 (AGENTS.md, "q0 anchor convention", R1) **D is
canonical**, so the CODE IS RIGHT and the DOCSTRING IS STALE. Do not "fix" the code to
match the docstring.

## Why this is worth a bean rather than a one-line edit

This is the declared-vs-actual convention hazard catalogued in
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`, in its most misleading form: a
reader who trusts the docstring gets a wrong `z` by 23 %, and every convention *detector*
in the repo keys on how `z` is spelled, so a stale prose declaration beside correct code
is invisible to all of them.

Worth checking at the same time whether the derivation narrative in that docstring (lines
25-50, "DERIVATION (symmetric convention...)", worked at H_2) is also convention-C and
therefore gives C-frame numbers.

## Structural note found while measuring this

Convention D's `z = q^3/(q^2+1)` is not an arbitrary choice: it is exactly the value at
which the per-cell numerator factor of a content-(-2) cell vanishes, so **every partition
with three or more rows carries weight zero at convention D**. The family is
`z = q^{2k+1}/(1 + q^2 + ... + q^{2k})` killing content `-k`; `z = q` (k=1) kills every
2+-row diagram; convention C's `sqrt(q)/(q+1)` is not a member at any integer content and
truncates nothing. Lean-proved sorry-free as
`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows` (PR #5575); probe in
`computations/schurweyl/ocneanu_weight_convention_d_support.py`.
