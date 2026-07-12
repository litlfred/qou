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

**Probe:**
[`qbeta_dladder_generating_function_structure_probe.py`](../../computations/qbeta/qbeta_dladder_generating_function_structure_probe.py)
(+ witness). Rebuilds the ladder (default ORD 31 → d₁…d₁₅; the analysis below
used a 21-term ORD-43 run to sharpen the extrapolations) with O/h through the
route-3 `ser_div`, so every `d_k ∈ ℚ(√3)` is exact — this hunts *exact*
structure, not floats.

**1 — exact parity structure.** Write `d_k = a_k + b_k√3`, `a_k, b_k ∈ ℚ`. The
part carrying the *small* denominator alternates by parity:

| k | small-denominator part | example |
|---|---|---|
| odd | the √3-part `b_k` | `d_1 = 1/8 − √3` (den `b`=1, den `a`=8) |
| even | the rational part `a_k` | `d_2 = −97/6 + 5√3/288` (den `a`=6, den `b`=288) |

Holds at every tested k through d₂₁.

**2 — Ohtsuki/Habiro-type smooth denominators.** The simple-denominator
interleaved sequence `s_k` (odd k → `b_k`, even k → `a_k`) has 3-smooth
denominators: only primes {2, 3, 5, 7}, with 5 first entering at k≈7 and 7 at
k≈10 (prime p first divides near index ~p). The 3-adic valuations
`v₃(den s_k) = 0,1,3,4,5,7,8,9,12,13,…` climb ≈ `3k/2`. This is the signature
of a factorial / q-factorial (Ohtsuki–Habiro) normalization.

**3 — D(ũ) is super-exponentially DIVERGENT (radius → 0).**
> **CORRECTED 2026-07-12** (PR #3720). This section originally read "D(ũ) is
> convergent, radius ρ≈0.143, a sharp contrast with the divergent κ-tower." That
> was a **finite-n shadow artifact** — a Domb–Sykes 1/k radius fit gives a
> spurious finite ρ, but no singularity of `log R(q(ũ))` exists there (nearest is
> 0.45–0.78), the root test `|dₖ|^{1/k}` rises without plateau (4.4→6.1 through
> k=27), and `log|dₖ| = A + B·k + C·k·log k` fits with **C ≈ 0.05–0.08 > 0**
> (super-exponential, ~50–300× tighter than a constant-radius law). So the
> D-ladder is super-exponentially **divergent** (radius → 0, q-Gevrey at `q₀`),
> in the **same** resurgent family as the κ-tower — *not* a convergent contrast.
> Full correction:
> [`2026-07-12-dladder-divergence-correction.md`](2026-07-12-dladder-divergence-correction.md).

**4 — no holonomic recurrence.** No P-finite recurrence of order ≤ 3 / degree
≤ 4 fits `a_k` or `b_k` (the 21-term run rules out order ≤ 4 / degree ≤ 5 too).
`D(ũ)` is not hypergeometric or P-finite at accessible order.

**5 — singularity origin (not a simple real value).** The sqrt branch points
`q⁴+q²+1=0` and the `ũ'(q)=0` folds all map to `ũ=0` (they fold back to the
expansion origin), and the nearest real singularity of `R(q)` — the `QA` zero
`q=1+√2` — sits at `|ũ|=0.775 ≫ ρ`. So the branch point at ρ is a **complex**
singularity of `log R(q(ũ))`, left unidentified. ρ lands within ~1 % of both
`√3/12 = 0.1443` and `1/7 = 0.1429`, but the slow Domb–Sykes convergence (small
exponent) makes a 0.3–0.7 % match meaningless — reported as data, **not** an
identification (anti-fit).

**Conclusion.** The D-ladder generating function has an exact parity +
smooth-denominator arithmetic and is a convergent algebraic-branch-point series
(radius ≈ 0.143), structurally distinct from the divergent κ-tower — but no
elementary or P-finite closed form emerges at 15–21 terms.

## Route 1 — meridian-corrected Borel–Padé on the deformed rungs

**Probe:**
[`qbeta_c3_borel_pade_deformed_rungs_probe.py`](../../computations/qbeta/qbeta_c3_borel_pade_deformed_rungs_probe.py)
(+ witness). Reruns #3692's Borel–Padé + Laplace on the deformed complex rungs
κ̃₁…κ̃₄ (read from the merged tall-ladder witness) instead of the real u=0 rungs.

**A — meridian-corrected Im 𝔙_b.** The u=0 rungs are real, so only the odd
rungs fed `Im 𝔙_b = Im Σ κ_n (i·t)ⁿ`. The deformed rungs are complex (u≠0
breaks the reality of `J_N`), so the *even* rungs now contribute through their
imaginary parts:

| term | value |
|---|---|
| `t·Re κ̃₁` | 0.06128383 |
| `−t²·Im κ̃₂` | +0.00066036 |
| `−t³·Re κ̃₃` | −0.00449417 |
| `t⁴·Im κ̃₄` | −0.00039236 |
| **Im 𝔙_b (all 4, truncation)** | **0.05705766** |
| Im 𝔙_b (odd only) | 0.05678966 |
| **Im 𝔙_b (Borel–Padé[2/2] resummed)** | **0.05854999** |
| #3692 u=0 (truncation / resummed) | 0.05481 / 0.05545 |

The even-rung imaginary parts add +0.00027 to the odd-only value; the meridian
correction lifts the resummed `Im 𝔙_b` from #3692's 0.05545 to ≈ 0.0585.

**B — DECISIVE: the deformation does not move the Borel singularity onto the
imaginary substrate ray.** #3692's decisive point was that the u=0 Borel
singularity sits at real `ξ = A = Vol(4₁)/π = 0.6461` (arg 0), off the imaginary
Laplace ray, so the Borel sum is single-valued (no Stokes split, no `e^{−A/x}`
trans-series) and `Im 𝔙_b` carries no anchor-dependent piece. The deformed
Padé[2/2] denominator roots:

| ξ_pole (Borel plane) | \|ξ\| | arg ξ | induced s-pole `−i·ξ/t` |
|---|---|---|---|
| instanton | 0.6313 | 0.0106·π | arg −0.4894·π |
| (Padé descendant) | 7.727 | 0.0106·π | arg −0.4894·π |

The deformation rotates the singularity only **0.011·π (≈ 1.9°)** off the real
axis and shifts its magnitude only ~2.3 % from `Vol(4₁)/π` — the instanton
action is essentially unchanged. The nearest s-plane pole is **0.489·π** off
the positive-real Laplace ray (vs the maximally-safe 0.5·π at u=0), i.e. it
moves toward the dangerous ray by only ~0.011·π. So the Borel sum stays
single-valued even at the deformed meridian.

**Conclusion.** #3692's result survives the deformation: the meridian-corrected
`Im 𝔙_b` is the exact smooth value, and there is *no* resummable,
anchor-dependent Stokes contribution the deformation could have introduced. The
odd-S sign-flip remains the `1/u³` ladder representation (#3636) —
representational / experimental-Q_β-limited, not a resummable physical effect.
**Caveat:** 4 rungs → Padé[2/2] is few, so the resummed `Im 𝔙_b` value is
indicative; the singularity-arg statement (B) is the robust deliverable.

## Honest scope (anti-laundering)

Everything here is 4₁ asymptotics / exact q-series structure. Nothing closes
`S`, wires a `c_k`, or changes any tier.
