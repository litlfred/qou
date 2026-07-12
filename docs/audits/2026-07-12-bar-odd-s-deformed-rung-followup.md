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

**The bug.** Dividing a series `a` by a series `b` when both have s-valuation
≥ 1 was done inline as `ser_mul(a[1:]+[0], ser_inv(b[1:]+[0]))`. Shifting
`a` and `b` down by one and padding a `0` at the top means the top coefficient
of the quotient is computed from a fabricated `a[ORD+1] = 0` — it is garbage
by construction. A genuine power-series quotient `a/b` with `b` of valuation
`vb` is determined only through order `ORD − vb`; the rows above need the
`vb` coefficients the truncation threw away.

**The fix.** Added a valuation-aware `ser_div(a, b) → (quo, valid_top)` to the
shared helper
[`qbeta_ck_sseries_exact_rational.py`](../../computations/qbeta/qbeta_ck_sseries_exact_rational.py):
it computes the valuation `vb` of `b`, checks `a`'s valuation is `≥ vb`,
strips the common `s^vb`, divides, then **zeroes and reports** the `vb`
invalid top rows so a caller cannot read past `valid_top`. Also added
`ser_valuation`.

**Re-audit — three sibling probes read the artifact top row.** Each ran the
same object as different truncations, and each drew a conclusion off the
padded top:

| Probe (bean) | Old artifact reading | Corrected |
|---|---|---|
| [`qbeta_barodd_d_ladder_ord17_probe.py`](../../computations/qbeta/qbeta_barodd_d_ladder_ord17_probe.py) | (already the correcting probe; now routes O/h through `ser_div`) | d₁…d₉, 9 over-determining orders zero — unchanged |
| [`qbeta_even_channel_bar_split_probe.py`](../../computations/qbeta/qbeta_even_channel_bar_split_probe.py) (ai81) | "TWO-VARIABLE FORM **FAILS** at order 11" (`firstG` scanned `G[11]`) | **HOLDS** through s^10; `two_variable_form_holds_to_ORD: true` |
| [`qbeta_bar_split_ord17_probe.py`](../../computations/qbeta/qbeta_bar_split_ord17_probe.py) (08ds) | "margin-1" `h³F` discriminant (the one over-determining row was `G[17]`) | margin-0 after dropping the artifact row → **no discriminating power at ORD 17**; the refutation is moot, not a refutation |

The fourth toucher,
[`qbeta_zeta4_faithful_odd_probe.py`](../../computations/qbeta/qbeta_zeta4_faithful_odd_probe.py),
already sidesteps the bug (it solves the single tower directly on `O`, no
division) and documents it in its docstring — no change needed. This
re-scoping is all scope-(a): the numerical coefficients were always correct;
only the top-row *readings* were invalid.

## Route 2 — the exact D-ladder generating function

_(pending)_

## Route 1 — meridian-corrected Borel–Padé on the deformed rungs

_(pending)_

## Honest scope (anti-laundering)

Everything here is 4₁ asymptotics / exact q-series structure. Nothing closes
`S`, wires a `c_k`, or changes any tier.
