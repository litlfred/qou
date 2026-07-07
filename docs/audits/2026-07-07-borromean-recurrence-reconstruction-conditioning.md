# Borromean diagonal recurrence — phase-2 reconstruction: conditioning diagnosis

**Date:** 2026-07-07
**Branch:** `claude/aj-conjecture-qou-uz5m6x` (PR #3450)
**Bean:** `n920` (phase-2 tail)
**Lineage:** follow-up to PR #3443 (existence certificate + Habiro transcription)
and PR #3434 (trefoil strong-AJ sorry-free).

## What is solid (merged, unaffected by anything below)

The **existence** of a q-difference recurrence annihilating the Borromean
diagonal colored-Jones tower `J_{B,n}` is certified — the first such
evidence anywhere (link-AJ is formulated-only: Sawabe 2024, Hopf +
Whitehead; no Borromean recurrence/A_q-ideal is published). Witness
[`computations/borromean-diagonal-recurrence-hunt.witness.json`](../../computations/borromean-diagonal-recurrence-hunt.witness.json):

| order `r` | window `W` | nullity |
|---|---|---|
| 5 | 13 | 2 |
| 6 | 11 | **1** (unique operator up to scale) |
| 7 | 10 | 1 |

Certificate per window: null vector solved on `unknowns+20` fit rows
survives 30 rows beyond the fit range at every one of 9/9 (prime, base)
samples (accidental-survival odds ~`p^-30 ≈ 10^-550` per sample); orders
`r ≤ 4` are empty for all `W ≤ 14`, so order 5 is minimal in the searched
region.

## Phase-2 goal and the method that hit a wall

Phase 2 seeks the **explicit** operator over `Z[q^{±1}]`:
`Σ_{i=0}^{6} a_i(q, m) J_{B,n+i} = b(q, m)`, `m = q^n`, at the unique
`(r,W)=(6,11)` window (184 unknown coefficient entries `a_{i,k}, b_k`,
`k ∈ [-11,11]`).

**Method used** (`tools/borromean-recurrence-crt` +
`computations/borromean_recurrence_crt_driver.py`): sample the RREF
nullspace of the fit system mod several ~61-bit primes at many base
points `s` (so `q = s²` varies), interpolate each of the 184 matrix
columns as a rational function `P_c(q)/Q_c(q)`, CRT + Wang-lift the
residues to `Q`, then run the claim-bearing exact symbolic annihilation
against the verified Habiro tower.

## The conditioning diagnosis (why it stalled)

**Root cause — RREF entries are ratios, hence high degree.** The RREF
nullspace normalizes by a free column, so entry `v[c] = a_c / a_free` is a
**ratio** of two true operator coefficients. Measured degree distribution
over `q` (single-prime full bisection, 640 samples): **min 0, max 252,
median 208.** The *true* operator coefficients (in a common-denominator-
cleared primitive form) are roughly half that; the factor-two inflation is
the `a_free` denominator carried into every entry. Reconstructing 184
degree-~250 rational functions needs many samples per prime and enough CRT
primes for the integer coefficients of those high-degree polynomials.

**Secondary — a genuinely low-degree column destabilizes the CRT
consensus.** Column 181 (a `b`-block entry) fits at degree ~1, far below
its neighbors (~192–198). At a prime `p` dividing that column's true
leading coefficient, its minimal degree *shifts*, so a naive "pin p0's
degrees at every other prime" contract makes every other prime look
"non-generic" and get rejected — the observed 23-prime skip cascade was
this single column, not 23 bad primes.

**Fix applied (committed, PR #3450), pipeline now:**
- `--degrees` entries are **bisection hints** (upper bound + slack), not
  pins — each prime converges to its own minimal *unique reduced* form
  (canonical by monic-`Q` at the minimal degree, gated by a nullity-1
  check);
- the driver CRTs each column only across runs agreeing on the **modal**
  `(deg P, deg Q)` shape, so a genuinely non-generic prime is excluded
  *per column* instead of aborting the whole lift.

**Validation status: gated on compute, not yet green.** A clean run is a
~30 min prime-0 bisection (184 columns × 640 samples) + ~2 min/prime for
2–3 more primes + the symbolic gate. Container reclaim (~1–2 h cadence in
this environment) destroyed three successive runs mid-flight — including
one that truncated the prime-0 cache to 0 bytes and fed the driver an
empty file. The driver now checkpoints the lifted operator to disk
immediately on lift success (`borromean-recurrence-lifted-operator.json`)
and prime-0 regen uses an atomic move, so the *next* uninterrupted run is
restart-robust.

## Why not just solve for the operator scalars directly?

The obvious ratio-free alternative — posit `a_i(q,m) = Σ_{k,d} c_{i,k,d}
q^d m^k` and solve one big system for the scalars `c_{i,k,d}` — is **not**
cheaper. With true degree `D ~ 126`, the scalar count is
`8·23·127 ≈ 2.3×10^4`, giving a dense `~2.3×10^4`-square mod-`p`
elimination (`~10^{13}` field ops) per prime — hours even in optimized
Rust. The sample-and-interpolate (RREF) approach is the correct
*complexity* choice; it just produces high-degree ratio interpolants that
must be reconstructed carefully. The fix above keeps that complexity and
repairs the reconstruction.

## Recommendation (two clean routes; both fresh-tranche)

1. **Finish the fixed CRT pipeline** on an uninterrupted run (the fix is
   committed; the failure was environmental, not mathematical). If the
   symbolic gate passes, the deliverable is the explicit operator + its
   `q→1` diagonal A-polynomial candidate.
2. **qZeilberger creative telescoping** — the proof-grade route, mirroring
   the corpus's successful 4₁ certificate
   ([`computations/aj_figure_eight_certificate.py`](../../computations/aj_figure_eight_certificate.py)).
   It yields the operator directly with controlled degrees and a
   telescoping certificate that is the natural input to a Lean
   formalization (as the 4₁ and trefoil certificates were). Preferred if
   the goal is the machine-checkable analogue of the two knot operators
   already sorry-free in the corpus.

Neither is a blocker on anything: the existence certificate is the
standing result. This audit is the read-first record for whoever picks up
the explicit-operator tranche.
