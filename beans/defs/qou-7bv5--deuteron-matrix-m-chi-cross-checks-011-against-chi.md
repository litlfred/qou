---
# qou-7bv5
title: Deuteron matrix-M chi cross-checks 0/11 against chi_q_via_gp; helium-3 is 30/30
status: completed
type: task
priority: normal
created_at: 2026-08-16T00:16:17Z
updated_at: 2026-09-08T05:03:36Z
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

## RESOLVED 2026-08-16 — neither path is wrong; the producer under-precises n=6

Ran the matrix-M build in-process with guard digits (`mp.mp.dps = dps + 10`)
and compared to the Rust `chi_q_via_gp` value:

| dps | worst \|matrixM/rust − 1\| | worst λ |
|---|---|---|
| 70 | **9.37e-79** | (3,3) |
| 90 | **3.50e-98** | (3,3) |

It converges cleanly, ~10^-(dps+9). **Both paths compute the same object
correctly.** The earlier 0/11 was never a disagreement between the paths.

**Where the digits go.** The committed `dps=50` cache retains only ~7 good
digits (ratios 1.0000003, scattered, straddling 1) while the identical
computation with guard digits gives 79. So the loss is inside the producer's
compute-and-serialize step, not in either χ path.

**Why n=6 and not n=9.** The matrix-M route takes a *parabolic split* at the
σ₃ bridge (`_split_atom_braid`) and requires exactly one bridge crossing. The
deuteron's split is ill-conditioned enough to eat ~43 digits at working
precision 50; helium-3's is not, which is why it matched 30/30 in the same run.
The worst partition is λ=(3,3) at every precision tested — a rank-5 block —
which is the place to look.

**Fix direction:** raise the working precision above the requested output `dps`
inside `build_chi_cache_at_q0_matrix_m` (guard digits), rather than computing at
exactly `dps`. Then re-emit the deuteron cache and the cross-check should go
11/11. Worth confirming the guard-digit margin needed scales with n before
picking a constant.

**Still true and still worth fixing separately:** the producer prints the 0/11
and exits 0, so the harness cannot see it (same shape as `qou-9d6h`).

## CORRECTION 2026-08-16 — my "under-precises n=6" conclusion was WRONG

I recorded above that the producer loses ~43 digits at n=6. That is not what
happens, and the correction matters because the real defect is worse.

**Measured digit loss at working precision P exactly** (build called directly,
`mp.mp.dps = P`):

| atom | P=51 | P=60 | P=70 |
|---|---|---|---|
| deuteron (n=6) | lost 2.26 | lost 2.29 | lost 2.49 |
| helium-3 (n=9) | lost 4.25 | lost 3.99 | lost 3.71 |

Roughly **constant, ~2–4 digits** — not 43, and not scaling with n. At P=50 a
fresh deuteron build has ~48 good digits, comfortably inside the 1e-45
tolerance. `main()` sets `mp.mp.dps = args.dps` and builds `q_mpf` after it, so
neither the build nor the cross-check is under-precised. **No guard-digit fix
is needed; do not add one.**

## The actual defect: a resume cache that serves stale entries

`build_chi_cache_at_q0_matrix_m` lines 186–206: if the output file exists it
loads existing entries into `already` and **skips recomputing them**, filling
only gaps. So a stale cache is handed straight back, and the producer's own
cross-check then compares those stale entries against a fresh Rust value.

Deleting the deuteron cache and re-running:

```
before   cross-check 0/11 match      tr_M = 1.33178255505578273520...
after    cross-check 11/11 match     tr_M = 2.17544681693623666235...
```

**0 of 11 per-λ χ values were identical**, and `tr_M` moved **63 %**. The cache
was not slightly stale — it was a different object entirely, and every consumer
of that χ cache has been reading it.

**Blast radius is bounded**: tritium 30/30 and helium-4 77/77 on their existing
caches, so the deuteron was the only stale member.

**The severity is the silence.** The producer prints `0/11` and exits 0, so the
harness records `ok`. Two independent detectors — this cross-check and
`qou-9d6h`'s probe — both reported real defects into a channel nothing reads.
That is the pattern worth fixing generally, not the deuteron number.


---

## CLOSED 2026-09-08 — artifact repaired and root cause guarded. The residual this bean calls "the pattern worth fixing generally" is SPLIT OUT to `qou-li9a`, still live.

Verified on `main` `a61496dbc82`, both halves.

### 1. The artifact carries the fresh value

Both deuteron caches — 50 dps and 90 dps — read
`tr_M_at_q0 = 2.17544681693623666235393297…` with 11 partitions. That is this
bean's **post**-repair number, not the stale `1.33178255505578273520…` it opened
on. The 63 % move is landed.

### 2. The root cause is guarded, and guarded the right way

`chi_at_q0_via_matrix_m_mpfr.py:186-206` no longer resumes unconditionally. The
resume is now **q₀-conditional** — it discards the cache when `prev_q` differs
from the requested `q_str` — with an explicit `--fresh` repair path for a cache
that was *already* relabelled. The comment records the incident with this bean's
own measurements (0 of 11, 63 %) and, better, records that the guard was
**ported** from `chi_at_q0_via_hoefsmit_mpfr` rather than invented, *"so the two
producers of the same χ family behave the same way"*. Its quoted line is the
durable part:

> *a stale cache wearing a fresh label is indistinguishable by inspection; only
> recomputation can reveal it*

Which is also why the guard-digit theory this bean investigated and rejected
stays rejected — the table showing a roughly constant 2-4 digit loss (not 43,
not scaling with n) still stands, and nobody should add a guard-digit fix here.

### 3. The silence is NOT fixed — and it is the half this bean says matters

Read at the source rather than inferred. `chi_at_q0_via_matrix_m_mpfr.py:503-523`
computes `n_match` against a 1e-(dps-5) tolerance and **only prints it**; the
function ends

```python
    return 0 if last_record is not None else 1
```

so the exit code turns on whether a record was *produced*, never on whether it
*matched*. `0/11` and `11/11` both exit 0 today.

That is exactly what this bean warned about, and it is why the deuteron staleness
survived: the detector was firing on every run into a channel nothing reads.

**Split out as `qou-li9a`** rather than held here, because it is a different
scope — a contract change on every caller of this producer, not a repair to the
deuteron. `qou-9d6h` (`completed`) is the same defect in
`deuteron_tower_fusion_frame_probe` and is the precedent to follow; the new bean
says to measure the caller set before changing the exit code, and not to widen
the tolerance to keep callers green.

**Blast radius as recorded stands**: tritium 30/30 and helium-4 77/77 on their
existing caches, so the deuteron was the only stale member.
