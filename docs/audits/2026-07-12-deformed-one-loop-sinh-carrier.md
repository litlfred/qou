# The deformed 1-loop invariant of 4₁ is e^u × even — the first geometric sinh carrier

**Date:** 2026-07-12 · **Branch:** `claude/ck-qbeta-closure-avenues-mu8471`
**Scope:** c₃ bar-odd `S` frontier, follow-up to the merged NZ parity prune
(PR #3622). Geometric-exact computation; no c_k value proposed; nothing
wired (flip-flop guard §8).

## Question (pre-registered)

The parity prune (#3622) proved the **classical** NZ series has no odd
rung, pushing the odd channel to quantum corrections. First quantum order:
is the deformed Dimofte–Garoufalidis 1-loop invariant τ(u) of 4₁ even in
the deformation u — or does it carry the odd content?

## Verdict: τ(u) = e^u · τ_even(u)

[`qbeta_deformed_one_loop_parity_probe.py`](../../computations/probes/qbeta_deformed_one_loop_parity_probe.py)
→ [`qbeta-deformed-one-loop-parity.witness.json`](../../computations/probes/qbeta-deformed-one-loop-parity.witness.json)
(6/6 assertions, 60 dps, exit 0):

- **τ(u) is NOT even** — max |odd part| 0.069 over the grid (real,
  imaginary, complex rays); leading odd coefficient
  (τ(u)−τ(−u))/(2u) → **√−3/2 = τ(0)** exactly (2.5e-56).
- **The odd content is exactly the factor e^u = M²**: κ(u) := e^{−u}τ(u)
  is even to ≤ 9e-62 on every ray. Taylor:
  τ(u)/τ(0) = e^u·(1 − u²/3 − u⁴/4 − 121u⁶/1080 + O(u⁸)),
  all coefficients recognized as exact small rationals.
- **Convention-irreducible**: a flattening kernel-shift multiplies τ(u) by
  −e^{−2u} = −M⁻⁴ (verified 3e-61), so τ is defined up to ±M^{4ℤ} and the
  parity class "M^{±2} × even" is invariant — no flattening makes it even.
- Hence the odd part of the 1-loop channel is **exactly
  sinh(u)·τ_even(u)** — a pure sinh times an even series: the first
  concrete geometric object on the 4₁ deformation with the bar-odd sinh
  structure the Q_β channel demands (Q_β is the bar-odd sinh partner of
  the bar-even cosh meson scale; KC17: the odd channel is irreducibly
  archimedean — this locates a geometric sinh carrier *at one loop*, not
  in the classical series).

## Validations (all in the witness)

- τ(0) = ±√−3/2 (dev 1.1e-61) — the DG 1-loop of 4₁, matching the
  Garoufalidis–Sabo formula evaluated on the m004 NZ datum.
- **A-polynomial primary cross-check**: M = e^{u/2}, L from the longitude
  row satisfy the CCGLS A-polynomial to ≤ 3.2e-61 at all 14 grid points;
  L(0) = −1.
- Vol(u) even (≤ 3.1e-61) — the classical control channel.
- Datum-independence: a second row-basis NZ datum gives τ₂ = −τ₁ exactly.
- Convention notes recorded in the witness (z″ = 1 − 1/z per the
  Garoufalidis–Sabo `nloop_exact.py`; datum rebuilt from raw m004 gluing
  rows with the meridian row explicit; the gluing matrix is pinned a
  posteriori by the A-polynomial check).

## Relation to the overnight sibling landings (2026-07-12)

The 4₁↔Q_β bridge audit (`3336314582`, merged) establishes the cosh/sinh
skeleton + growth-class obstruction (scope-(b)); the κ-rung extraction
(`095939d2`) finds exact ℚ(√3)·πⁿ rungs with parity alternation; the Borel
probe (`23602938`) quantifies the even-channel Gevrey-1 divergence. This
result plugs the missing piece into that skeleton: **the geometric side
has a canonical sinh(u) odd carrier at 1-loop**, with an exact even
cofactor whose first rungs (−1/3, −1/4, −121/1080) are now on record for
any bridge test. Follow-up candidates (not run here): match
sinh(u)·τ_even(u) against the S targets under the sibling's u-candidates;
n-loop parity (does the e^u factor persist / exponentiate at higher loop).

## Non-derivation disclaimer

All constants are exact geometric data of the 4₁ deformation variety.
No identification with c_k or S is made; the sinh-carrier observation is
a structural hypothesis handed to the Φ_b/bridge searches.
