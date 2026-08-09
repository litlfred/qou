---
# qou-xblo
title: 'The 5₂ sum rule is an EXTENDED Bloch statement — Σ R̂(y_σ; ε_σ, 0) = −π²/6, flattening supplied by the cubic'
status: in-progress
type: task
created_at: 2026-08-09T10:30:00Z
updated_at: 2026-08-09T10:30:00Z
---

Claimed by the session on `claude/fivetwo-level7-ladder-numerators` (restarted
from `main` after #4701 merged). Split out of `qou-0yqu`, which stays the parent
gap; this bean is the **route**, not the gap.

## The reformulation, measured

With `L(z) = Li₂(z) + ½·log z·log(1−z)` the Rogers dilogarithm and

    R̂(z; p, q) = L(z) − (πi/2)·( p·log(1−z) + q·log z )

Neumann's **flattened** Rogers dilogarithm, the 5₂ saddle roots satisfy

    Σ_σ R̂(y_σ ; ε_σ , 0) = −π²/6            residual 0.0 at 60 dps

where `ε = (+1, −1, 0)` is **not fitted** — it is the cubic's own branch data,

    ε_j = ( 2·log y_j − 3·log(1−y_j) ) / (2πi)

measured as exactly `(1, −1, 0)`. That those are integers is already a
sorry-free Lean theorem on `main`: `branch_data_of_cubic` in
`QOU/QBeta/FiveTwoSaddleSumRule.lean`, proved from the cubic alone with no
dilogarithm involved. **The flattening the extended Bloch group needs is
already a theorem in the corpus.**

Equivalent to the sum rule, not weaker: `Σ V_j` and `3·Σ R̂` differ by an
elementary term computable from the cubic, verified to 50 dps.

## Why this is the right home — the ordinary Bloch group provably is not

Route 42 measured the obstruction. `D(y₁)` carries the entire 5₂ volume
(`Vol(5₂) = 3·D(y₁) = 6·D(c₁)`), but `Σ_σ D(σ y) = 0` **identically** — `y₂ = ȳ₁`,
`D(z̄) = −D(z)`, real root gives `0`. `D` is exactly the ordinary Bloch group's
regulator, so that machinery evaluates to zero on a Galois-summed dilogarithm
and can carry no information about `A`. Routes 1–5, 40 and 41 could not have
closed.

The extended Bloch group keeps what `D` discards: its regulator is the complex
volume `Vol + i·CS`, and `R̂` is well defined on it modulo `π²/6`.

## The quantisation signature

    −3π²/2  =  −9 · (π²/6)          the sum rule, in V-normalisation
    Σ_σ R̂   =  −1 · (π²/6)          the same statement, flattened

while the individual `Re(V_j)/(π²/6)` are `−2.1615…`, `−2.1615…`, `−4.6769…` —
irrational separately, integral only in the sum. That is the signature of a
Chern–Simons-type invariant, whose indeterminacy is exactly `π²/6`, and it is
the strongest evidence so far that the avenue is right.

## What is open — this is a reformulation, NOT a proof

The target is now: **show `Σ_σ [y_σ; ε_σ, 0]` is torsion in `ℬ̂(ℂ)`.** By
Neumann's theory that forces `Σ R̂` into `(π²/6)·ℤ`, and the sum rule is the
statement that the integer is `−1`.

⚠ Honest limits on what is measured:

* Neumann's **parity / geometric conditions** on a flattening are NOT imposed
  here. `ε` was found to work by search over `p, q ∈ {−2..2}` and then
  recognised as the branch data; a second assignment `(p,q) = (−2,2)` also
  gives an integer (`11`). So the measured claim is "the cubic's branch data,
  used as a flattening, makes the Galois sum an exact integer multiple of
  `π²/6`" — not "the geometric flattening does".
* Nothing here derives the integer `−1`. Getting it is the proof.
* No Lean. `R̂` and `ℬ̂(ℂ)` are not formalised in the corpus.

## Next

1. Impose Neumann's flattening conditions and check `ε` satisfies them — that
   turns the search hit into the geometric object.
2. Finish `qou-0yqu` Route 41's gated `G4` branch bookkeeping (pentagon over the
   three embeddings missed `3π²/2` by 6.4718; the real embedding is exact, the
   two complex ones deviate by `−3.2359 ± 1.3251i`, which is **not** a multiple
   of `π²/6` under principal branches — as expected, since the quantisation is a
   statement about the flattened form).
3. The five-term relation lifted to `ℬ̂(ℂ)`, then redo Route 41's rank
   computation there. The ordinary-Bloch rank result (46→47, 153→154) says
   nothing about the extended one.
4. Coordinate with **#4824** (`claude/extended-bloch-tetrahedron-wx3mc4`),
   already in extended-Bloch territory. Do not duplicate.

**Do not retry:** distribution (rank 4→5) or the ordinary five-term/Bloch ladder
over the `c^m` orbits. Anything reducing to an ordinary Bloch-group computation
is blind here, for the reason above.

Probe: `computations/probes/qbeta_5two_route43_flattened_rogers_probe.py`.

**The 5₂ sum rule remains verified to 80 dps, unproved.**
