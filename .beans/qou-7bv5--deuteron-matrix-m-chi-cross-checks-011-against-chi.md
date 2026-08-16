---
# qou-7bv5
title: Deuteron matrix-M chi cross-checks 0/11 against chi_q_via_gp; helium-3 is 30/30
status: todo
type: task
created_at: 2026-08-16T00:16:17Z
updated_at: 2026-08-16T00:16:17Z
---


## Measured 2026-08-16

`chi_at_q0_via_matrix_m_mpfr.py` prints a per-atom cross-check of the matrix-M
χ against the Rust `chi_q_via_gp` path at tol 1e-45:

```
deuteron    n=6   11 parts    cross-check: 0/11 match     <-- every partition
helium-3    n=9   30 parts    cross-check: 30/30 match
```

**Pre-existing, not caused by the convention-D work.** A re-run here reproduced
`main`'s deuteron `tr_M_at_q0` bit-identically:
`1.331782555055782735209145221967158590016601407687`.

**Why the obvious explanation does not fit.** The producer's docstring says the
two paths "represent different braid encodings", which would predict a mismatch
at *every* atom. It is 30/30 at helium-3. So either the deuteron braid word
differs between the two paths specifically, or one path is wrong at n=6.

Worth resolving because both paths feed χ caches that downstream binding and
Δ_λ compute consume, and a silent 0/11 is exactly the shape of a defect that a
green exit code hides — the producer exits 0 with this printed.

Next step: dump both paths' per-λ χ at n=6 and compare against the seminormal
`global_wedderburn_sum_q_hecke_seminormal` as an independent third path.

## Diagnosis sharpened 2026-08-16 — it is NOT a convention or a braid word

Both obvious explanations are ruled out by measurement.

**Not "different braid encodings"** (the producer's own docstring guess). Both
sides of the cross-check use the *same* word: the check calls
`_word_for_braid_word_3a(Z, N)` and feeds that identical `word` to
`chi_rust_at_q_mpf`. There is no second encoding in the comparison.

**Not staleness.** Both caches were rewritten in the same run (mtime 00:13),
both record `dps=50`, both carry 48-digit `chi_lambda` strings, both at the same
q₀. The deuteron numbers are fresh.

**What it actually looks like — numerical noise at the 7th digit:**

```
λ            matrixM/rust
(6,)         1.000000265
(5,1)        1.000000289
(4,2)        1.000000305
(4,1,1)      1.000000077
(3,3)        0.999997454      <- below 1
(2,2,2)      0.9999998158     <- below 1
```

The ratio is **non-constant and straddles 1**. A convention difference or a
wrong braid word produces a *structured* factor; this is scatter. Magnitude
~3e-7 is single-precision territory — far worse than f64, and nowhere near the
`dps=50` both files claim.

**Deuteron-specific.** helium-3 (n=9, 30 partitions) matches at 1e-45 on every
partition, same code path, same run.

**Hoefsmit cannot adjudicate.** `chi-deuteron-h6-at-q0-50dps.witness.json` gives
ratios swinging 0.1415 → 48.07 per partition against both — it is the
colour-weighted convention, a genuinely different object from sign-only, exactly
as the producer's header warns.

### Next step for whoever picks this up

A third *sign-only* path is needed; Hoefsmit is not one. Options: evaluate the
matrix-M product at `mp.mp.dps = 100` and see whether it converges toward the
Rust value (⇒ matrix-M loses precision at n=6) or stays put (⇒ Rust is the
imprecise side); or compute χ^λ(σ-word) symbolically in ℚ(q) at n=6 and
evaluate, which settles it outright. The n=6-only character of the defect is the
strongest clue and should be explained, not worked around.

**Severity:** the producer prints this and **exits 0**, so a 0/11 mismatch is
invisible to the harness — the same silent-failure shape as `qou-9d6h`.
