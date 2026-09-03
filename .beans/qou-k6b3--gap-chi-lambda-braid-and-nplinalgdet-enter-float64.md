---
# qou-k6b3
title: 'GAP: chi_lambda_braid and np.linalg.det enter float64 — blocks 2 producers from the proton migration'
status: completed
type: task
priority: normal
created_at: 2026-08-29T09:40:22Z
updated_at: 2026-08-29T15:28:21Z
---

Parent: qou-cds3. Surfaced by the proton migration (PR #5992), which had to
DEFER two producers because of it.

## What is wrong

Two producers compute in float64 and it is not a display cast:

  * computations/chi_lambda_he4_full_partition_table.py:159-160
      chi = pn.chi_lambda_braid(shape, BETA_HE4, q0_f64)
    enters the **f64 Rust kernel**, so every one of the 77 chi values in
    chi-lambda-he4-full-partition-table.witness.json is float64.

  * computations/gram_matrix_seminormal_n.py:190,195
      sigma_k_dets = [float(np.linalg.det(M)) for M in sigma_k_at_q]
      w0_det = float(np.linalg.det(w0_at_q))
    numpy determinants are float64 by construction. Consumed by
    gram_matrix_seminormal_h6.py -> option-e-phase1-gram-h6.witness.json,
    and by any other consumer of that shared module.

## How it surfaced — worth keeping, the mechanism is general

Migrating those two producers to the proton pin turned the raw-float64
ratchet RED:

    chi-lambda-he4-full-partition-table   194 -> 196
    option-e-phase1-gram-h6               130 -> 131

**The migration did not add float64.** Those fields were always float64. At
the MUON pin they evaluated to exactly 1.0, -1.0 and 1.0 — which the ratchet's
integral-valued carve-out does not count — and at the PROTON pin they are
1.000000000000009, -0.9999999999999999 and 0.9999999999999998, which it does.
An anchor change moved three pre-existing float64 results across the
integrality boundary and thereby made them visible.

Generalisation: **the ratchet's integral carve-out hides float64 error
whenever the true value is an integer.** Determinants of ±1, characters that
should be exact counts, any quantity whose exact value is whole — the error is
there at the muon pin too, it just lands on the nose. Do not read a clean
ratchet on such a field as evidence the arithmetic is exact.

## The fix the corpus already names

f64_into_mpmath_audit.py's own test cases state it:

    ("a wrapper call omitting precision= gets the f64 default",
     "c = chi_lambda_braid(shape, word)", "F64_ENGINE_ENTRY"),
    ("passing precision= is the fix, so it is NOT flagged",
     "c = chi_lambda_braid(shape, word, precision='mpfr_50dps')", None),

and computations/hecke/hecke_characters.py:610 provides
`chi_lambda_braid_mpf(shape, signed_word, q_value=None, dps=None)` returning
an mpmath.mpf directly. For the determinants, an mpmath det over the exact
seminormal matrices replaces np.linalg.det.

## Why it was NOT done in PR #5992

It changes the COMPUTE PATH, so every value in both witnesses moves — not just
the three at the boundary. That is a larger and scientifically different change
than an anchor re-pin, and mixing it into the migration diff would make the
migration unreviewable. gram_matrix_seminormal_n.py is also SHARED, so the
determinant fix reaches consumers beyond the H6 producer and needs its own
blast-radius check.

## What unblocks when this lands

chi_lambda_he4_full_partition_table and gram_matrix_seminormal_h6 can then
migrate to physical_proton, completing the direct-reader set (18 of 20 landed
in #5992).

Downstream care: chi_lambda_he4_full_partition_table sorts and takes ratios on
`abs_chi` (lines 185-192) and prints with `:>+18.6f`, so an mpf conversion must
keep a sortable numeric internally and serialize with `_precision.fmt` at write
time rather than casting at the point of use.


## 2026-08-29 — FIXED (PR #6001), and it completed the cds3 direct-reader set

### The fix

`mp.det` is LU-based and runs directly on the mpmath matrices these already
are — the determinants never needed the numpy round trip. The h6 site's comment
declared all FOUR telemetry fields "float64 by construction"; that is true of
`cond` (a binary64 SVD) and NOT of `det`. Only the two cond fields keep the
declaration.

For the characters, `chi_lambda_braid(..., precision="mpfr_50dps")` — the fix
f64_into_mpmath_audit's own test cases name. The mpfr path returns a decimal
STRING so nothing is lost crossing the boundary; re-enter mpmath from it.

Measured drain, reported by the ratchet as DRAINED not merely non-regressing:

    chi-lambda-he4-full-partition-table   194 -> 1
    option-e-phase1-gram-h6               130 -> 59

The field that started it — chi_lambda at partition 76 of 12:

    before (f64):  1.000000000000009
    after  (mpfr): 1.0000000000000000000000000000000000000000000000000000000

exactly 1 to 59 digits. Determinants that read -0.9999999999999999 are now
-1.000000000000000000000000000000000000000000000000003 (error 1e-16 -> 3e-51).

The h6 residue of 59 is the CONDITION NUMBERS. Draining those needs an mpmath
SVD and is a genuinely separate change; not attempted.

### Three things that bit, worth keeping

1. **`w0_det` comes back `mpc`.** The first version serialized `1.3675... +
   0.0j`. `_real_det` now REFUSES a non-negligible imaginary part rather than
   silently taking the real part — the discipline `_eval_matrix` already
   applies entrywise.
2. **The wrapper returns a STRING at mpfr precision, not an mpf.** Deliberate
   (no precision lost at the boundary), but `abs()` on it raises.
3. **Downstream arithmetic on now-serialized fields.** Sort key, ratio, sums,
   AND a T-conjugate cross-check at :242 doing
   `abs(r["chi_lambda_he4"] - r_T["chi_lambda_he4"])`. Unserialized `_chi_mp` /
   `_abs_mp` keys carry the arithmetic and are popped before save. The
   consumer `probe_option_e_h6_entry_point.py` also needed `mp.mpf(repr(d))` ->
   `mp.mpf(str(d))`, since `repr` of a str adds quotes.

### What it unblocked, and a finding in its own right

Both deferred producers migrated to proton: **20 of 20 direct readers done.**

And the migration exposed that **the source edit for
chi_lambda_he4_full_partition_table had been on main since #5992 doing
NOTHING** — the stem sat in `ideal_muon`, so `q_parameter` resolved muon and
the witness kept stamping muon under migrated source. This is #5992's
"half the change is a no-op" finding, observed live rather than reasoned about.

`gram_matrix_seminormal_h6` was the mirror: in NEITHER list, so correct by the
runtime DEFAULT rather than by declaration. Now declared explicitly.


## FOLLOW-UP LANDED 2026-08-29 — the condition numbers, and my own incomplete report

Closed as 'dets + characters drained' with the h6 condition numbers deferred as
"needs an mpmath SVD, a genuinely separate change". mpmath has `svd_r`; it was a
small change. Commit `6e08f1f570`.

**h6 residue 59 -> 2.** The 2 are `compute_time_s` at h3 and h6 and STAY: wall-clock
is a genuine float64 measurement, and padding it to 50 digits with `fmt` is exactly
what the float64-padding ratchet forbids. Draining them trades one gate for another.

**MEASURED: kappa_2(rho_lambda(sigma_k)) = q_0^2** for all 47 generators in every
block of dim > 1, across lambda |- 3 and lambda |- 6, max relative deviation
9.2e-51. New witness assertion `generator_condition_number_equals_q0_squared`.

This is a TRAP worth keeping, and it is not the same trap as the integral carve-out
already recorded here. In float64 the SAME quantity was serialized under THREE
different spellings (1.232052482785027 / ...0272 / ...0274 at the muon pin). The
noise was larger than the structure, so there was no constant to recognise. A
float64 field does not merely lose digits — it can destroy the evidence that a
quantity is constant at all.

STATED AS OBSERVATION, NOT DERIVATION: q^2 = |q| / |-q^-1| is the ratio of the two
Hecke eigenvalue magnitudes, which is what kappa_2 would be for a NORMAL matrix.
Hoefsmit-seminormal rho_lambda(sigma_k) is real but NOT symmetric, so normality (or
an orthogonal-form conjugation supplying it) is NOT established. Mechanism open.

**AND A CORRECTION TO MY OWN CLOSING REPORT.** I wrote that the consumer
`probe_option_e_h6_entry_point.py` "needed mp.mpf(repr(d)) -> mp.mpf(str(d))",
implying it then worked. It did not, and it did not work on main either: the file
had FIVE such calls, and the producer's `_c` has serialized matrix entries as
STRINGS on main all along, so `repr` wrapped them in quotes and mpmath raised
`invalid literal for int()` at line 113 — BEFORE reaching the field I fixed. I
fixed the one site the det change forced me to notice and reported the consumer as
handled without running it. All five are now `str`; the probe exits 0.

Generalisable: when a serializer change forces a consumer fix, grep the consumer for
EVERY instance of the pattern and RUN it. One site compiling is not the consumer
working.
