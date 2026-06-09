# Non-abelian Stokes = SW-period: already proved & live; the deprecation was a supersession

**Date:** 2026-06-08 · **Branch:** `claude/vigilant-fermat-SROph` · **PR:** #1995
**Status:** audit (corpus-grep finding). The "non-abelian Stokes ⊃ SW-period"
program (queue item 2) is **largely already proved and live** — writing a fresh
derivation would have duplicated `brings-surface/`. The honest verdict on
un-deprecation: **selective, not wholesale.**

## What's already live (no new derivation needed)

The chain the owner proposed (`non-abelian Stokes → abelian restriction → SW
period`) is **proved and live** in `brings-surface/`:

1. **`prop:mi-sw-abelianisation`** — the *multiplicative integral* (= Yekutieli
   **non-abelian Stokes**) **abelianised** to the Seiberg–Witten differential
   `λ_SW^(n)`. This *is* the "commutative case" the owner named — non-abelian
   Stokes restricted to the abelian (Cartan / `T_q`) direction.
2. **`prop:sw-period-residue-sum`** — the SW period
   `a_D^(n) = ∮_{𝒮_c} λ_SW^(n) = 2πi Σ_p Res_p λ_SW^(n)` is an **algebraic
   residue sum** on the exceptional divisor `𝒮_c ≅ ℙ¹(ℂ)`; the residue family at
   jet level `n` is indexed by rank-`n` weight data and carries the **body-order
   grading**, each residue a per-block quantum-dimensional weight on the
   Wedderburn decomposition.

So **"non-abelian Stokes = SW period (commutative/abelianised case)" is a theorem
in the repo**, in the cleaner *algebraic-residue* form. The toroidal-knot handle
the owner cited is the jet-degree `n` (= body order) indexing the residue support.

## Why the thimble content was deprecated (supersession, not error)

The deprecated `sw-period-thimble-equivalence` is itself a **proved proposition**:
*Markov–Frobenius pairing `≡` SW residue period*, with **Step 1 = the non-abelian
Stokes theorem** (`⟨tr_M, T_w⟩ = MI∫_Σ α_{T_w}`, `∂Σ = ϱ`). Its own note:

> *"The historical Lefschetz-decomposition hypothesis (A2.3) is no longer
> required — the algebraic residue formulation makes thimble decomposition
> unnecessary."*

So the **Picard–Lefschetz / thimble-flow** machinery (`picard-lefschetz-thimble`,
`sw-3root-rational-integrand`, `morse-wall-q-moduli`, `sdp-as-thimble-flow`,
`gb-reduction-pl-thimble-bijection`, …) was deprecated because the **algebraic
residue sum superseded it** — same numerical answer via `τ`, fewer hypotheses.
Not wrong: *retired in favour of the cleaner form.*

## Un-deprecation verdict: selective

- **Do NOT un-deprecate the thimble-*flow* blocks.** They are genuinely
  superseded; reviving them re-introduces the eliminated Lefschetz hypothesis and
  the contour/thimble machinery the residue sum removed.
- **DO re-home the *bridge* result if it is not already live.** The valuable core
  of `sw-period-thimble-equivalence` is the **`Markov–Frobenius pairing ≡ SW
  residue period`** equivalence (its Step-1 non-abelian-Stokes identity + Steps
  2–4 residue reduction), which is *independent of* the thimble framing. **Check**
  whether this equivalence is already stated live (candidates:
  `prop:gs-archimedean-agreement-trace`, `prop:e-infinity-page-identifications`,
  `prop:categorical-mass-markov` + `prop:sw-period-residue-sum`). *If not*,
  re-state it as a **live proposition** (the `tr_M = ` SW-residue-period bridge),
  citing the live residue-sum + abelianisation, **shorn of the thimble
  decomposition.** That is the owner's "un-deprecate and explain", done
  surgically.

## The one genuinely open piece

**`E_q` = the Seiberg–Witten curve.** `λ_SW` lives on `𝒮_c ≅ ℙ¹` with the elliptic
structure of [`descartes-elliptic-curve`](../../content/quantum-observable-universe/brings-surface/descartes-elliptic-curve.md)
(`E_q`). Verifying `E_q =` a Seiberg–Witten curve (match `j`-invariant / period
lattice; the `(m,n)` torus-knot winding = the period cycles) is the remaining
non-trivial identification — and the cleanest statement of "the SW period *is*
the QOU period."

## Unification (ties the session's threads together)

- `τ` is the map **`SW(Schur–Weyl, algebraic Markov–Frobenius) → SW(Seiberg–
  Witten, residue period)`** — now both legs are *named live blocks*.
- The residue sum's **jet-degree-`n` / body-order grading** is the same tower as
  the **perpetual obstruction** (`κ_n ≠ 0 ∀n`) and its `ε^ω` surreal grade: the
  SW residue at level `n` is the `n`-body/depth contribution. So the
  **SW-period / perpetual-obstruction / `ε^ω`-surreal** threads are one object —
  the geometric (period) leg — with `τ`/`std` to the archimedean side.

## Action items (for queue item 2)

1. Check whether `Markov–Frobenius ≡ SW-residue-period` is already live; if not,
   re-state it as a live proposition (surgical un-deprecation).
2. Cross-link the LQG/SW-double-pun + spin-network material to
   `sw-period-residue-sum`, `mi-sw-abelianisation`, `descartes-elliptic-curve`.
3. Open piece: `E_q = ` SW-curve `j`-invariant/period verification.
