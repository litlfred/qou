# z→c_k f-map — I-B cyclotomic re-basing scope (bean `ciei`, multi-session)

**Date:** 2026-07-06 · **Branch:** `claude/z-c-k-f-map-keystone-ub5yix` (PR #3449)
· **Ledger:** [`z-ck-fmap-keystone.md`](../coordination/z-ck-fmap-keystone.md) §4-bis/§4-ter
· **Status:** SCOPE ONLY — no probe run; kill criteria to be pre-stated at execution.

## 1. Why I-B is now the load-bearing route

The session's three decisive negatives all point the same way:

1. **c4qz:** the raw pointwise slot `α₁ = −a₁/a₂` fails slot bar-parity — the
   middle coefficient's bar-covariance carries an intrinsic **non-monomial**
   factor.
2. **T1 (`7vfu`):** pair-symmetrizing over the golden locus `{φ², φ⁻²}` does
   **not** repair it — no evaluation choice can; the defect lives in the
   function space, not the evaluation point.
3. **T3 (`pxvo`):** the naive Z3 combination `f(z)·κ_{(2,1)}` is order-blocked
   at q=1 (odd total order `3−2k` vs the finite nonzero shadow `a₁(1) = 2`).

What survives is re-basing the operator itself: push the 4₁ recurrence from
the color basis `J_N` into the **Habiro cyclotomic basis** and only then read
off kernel slots — the parity and the q=1 order structure transform with the
basis, which is exactly what the pointwise routes could not access.

## 2. Inputs available (all landed)

- **4₁ cyclotomic expansion (Habiro):** `J_{4₁,N} = Σ_n C_n·∏_{j=1}^{n}
  (q^{(N+j)/…}−…)(…)` — the Habiro `(q;q)_n`-type basis; for 4₁ the
  coefficients are famously `C_n = 1` (Habiro's formula), making it the
  cleanest possible test knot.
- **4₁ order-2 qZeilberger certificate** (exact, verified N=1..12):
  `computations/aj_figure_eight_certificate.py`.
- **Borromean Habiro transcription + recurrence-existence certificates**
  (sibling n920 arc, landed on main 2026-07-06:
  `habiro_borromean_colored_jones.py`, `borromean_diagonal_recurrence_hunt.py`)
  — reusable machinery for expressing recurrences against Habiro-basis data.
- **The `(u;u)_m → u^k` change of basis** — already Lean-proved as the
  conditional in `prop:q-beta-c-k-recursion-from-habiro-q-difference`.
- **This branch's parity atoms** (`ZBarParity.lean`) for slot-parity gates
  after re-basing.

## 3. Plan (one probe per step, each with pre-stated kills)

1. **Step B1 — induced recurrence on the cyclotomic index.** For 4₁ with
   `C_n ≡ 1`, derive the recurrence satisfied by the cyclotomic *tail sums*
   under the order-2 operator (finite elimination; qZeilberger-style, exact).
   Kill: no finite-order induced recurrence at bounded degree.
2. **Step B2 — slot parity after re-basing.** Re-run the K2-style gate on the
   induced kernel's coefficients. Kill: non-monomial bar-covariance again
   (would indicate the defect is basis-independent — a strong structural
   verdict against Z4 via 4₁).
3. **Step B3 — q=1 shadow + `(u;u)_m → u^k` composition.** Compose with the
   proved change of basis; check the `c₂ = −1` identity and `c₃ → −2` locus
   transfer. Only after B1–B3 pass does any anchor-level question arise
   (owner-gated, registry §8).

**T3-2 dependency (🟡):** the owner ruling on the parity-vs-shadow tension
(exact-odd vs odd-part reading of #1887; see ledger §4-ter) determines what
"pass" means in B2 — pre-state both readings' criteria if unresolved.

## 4. Effort estimate

B1 is the hard step (symbolic elimination against Habiro-basis sums; the n920
arc measured operator coefficient q-degrees ~218 for the Borromean — 4₁
should be far smaller but still nontrivial). Multi-session; not started here.
