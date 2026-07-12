# Bar-odd S, deformed-rung follow-up: meridian Borel–Padé, the exact D-ladder generating function, and the O/h shift-padding fix

**Date:** 2026-07-12 · **Branch:** `claude/bar-odd-s-deformed-followup-2026-07-12` ·
**Axis:** Q_β c₃ bar-odd `S` (post-capstone) · follow-up to
[`2026-07-12-bar-odd-s-three-routes.md`](2026-07-12-bar-odd-s-three-routes.md)
(PR #3691) · **Tier:** numerical-derived + exact structure-hunt ·
**Discipline:** scope-(a); no fit to QOU data; no c_k wired; no tier change;
registry untouched.

Three follow-up items off the merged three-routes PR:

1. **Rerun #3692's Borel–Padé resummation on the deformed rungs.** #3691 landed
   the deformed Ohtsuki rungs κ̃₁…κ̃₄ at the substrate meridian (complex, unlike
   the real u=0 rungs #3692 resummed). This reruns the Borel–Padé + Laplace on
   the *deformed* tower to get the meridian-corrected `Im 𝔙_b`, and — the
   physically decisive question — checks whether the meridian deformation moves
   the Borel singularity onto the imaginary substrate ray (which would introduce
   a resummable, anchor-dependent Stokes piece, contra #3636).

2. **Structure-hunt the exact D-ladder generating function.** With the top-order
   artifact gone, `D(ũ) = Σ dₖ ũᵏ` is an exact ℚ(√3) power series; #3691 gave
   d₁…d₉. This extends the ladder and hunts for exact structure (holonomic
   recurrence, denominator arithmetic, growth/singularity).

3. **Fix the O/h shift-padding in the shared series helper + re-audit
   top-order readers.** The `G = ser_mul(O[1:]+[0], ser_inv(h[1:]+[0]))`
   shift-padding silently makes the top coefficient depend on the unknown
   `O[ORD+1]`. This adds a valuation-aware `ser_div` to the shared helper and
   sweeps sibling probes for the same foot-gun.

## Route 3 (foundational) — the O/h shift-padding fix

_(pending)_

## Route 2 — the exact D-ladder generating function

_(pending)_

## Route 1 — meridian-corrected Borel–Padé on the deformed rungs

_(pending)_

## Honest scope (anti-laundering)

Everything here is 4₁ asymptotics / exact q-series structure. Nothing closes
`S`, wires a `c_k`, or changes any tier.
