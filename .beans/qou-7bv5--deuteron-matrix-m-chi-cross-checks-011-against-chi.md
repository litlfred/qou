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
