# c₃ bar-odd: the arg(u) phase branch-selection is FROZEN on the real substrate ray — the last seat is a WALL (scope-(a))

**Date:** 2026-07-25 · **Axis:** Q_β c₃ (bar-odd `S`) · **Branch:**
`claude/qbeta-argu-phase-branch-selection-2026-07-25` (PR #4293) · **Tier:**
structural (Lean-exact) + measurement (scope-(a)). **No `c_k` wired; nothing
inverts `Q_β`/CODATA; registry untouched; no tier change.**

- **Lean:** [`QOU/QBeta/ArgUPhaseBranchSelection.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/ArgUPhaseBranchSelection.lean) (`lean`-direct exit 0, sorry-free).
- **Probe:** [`qbeta_argu_phase_branch_selection_probe.py`](../../computations/qbeta/qbeta_argu_phase_branch_selection_probe.py) (witness `qbeta-argu-phase-branch-selection.witness.json`, 4/4).

## The question (the deep keystone)

A chain of proved exclusions collapsed the seat of `c₃`'s percent-level bar-odd
anchor-swing to a single channel:

- **#4282** (C1, sorry-free): the bar-odd datum is the ι-odd antisymmetric
  off-diagonal `ω(β,p,q)=β·p−β⁻¹·q`, **anchor-smooth** (4.56 ppm).
- **#4288** (sorry-free): the exact boost-hyperbola bound
  `(barEven/barOdd)²=1+4/barOdd²` forces amplification `ρ≥N` to require
  `barOdd²≤4/(N²−1)`; the `S∝|u|²` **magnitude** channel is anchor-smooth (measured
  swing 0.221 ppm; the substrate is 5.5 orders too far from the compact locus).

The residual was localized to the non-perturbative **phase** `arg(u)` of the
Neumann–Zagier meridian-deformation coordinate `u` — the branch-selection of the
open `conj:algebraic-geometric-dilog-equivalence`. **This session asks the honest
handle-vs-wall question about that last seat.**

The task's live hypothesis was a **handle**: the phase `arg(u)` is an *independent*
DOF from the magnitude `|u|`, so #4288 (which bounds only `|u|`) does not constrain
it; a large phase-sensitivity might carry the swing.

## The formalize-first result

Write the leading Neumann–Zagier imaginary complex-volume (the bar-odd /
Chern–Simons `S = Im 𝔙`) in the meridian-deformation polar coordinates
`(r, φ) = (|u|, arg u)`. From the derived `u=0` quadratic branch
`𝔙(u) ≈ 𝔙(0) − (τ/4)u²`, cusp modulus `τ = 2√−3 = barOdd(ω)`, amphichiral base
`Im 𝔙(0)=0` (`docs/audits/2026-07-11-c3-wall-branch-structure.md §2`), the leading
form is the corpus's:

$$S(r,\varphi) \;=\; \mathrm{nzImVolume}(r,\varphi) \;=\; \tfrac{\sqrt3}{2}\,r^{2}\,\sin(2\varphi).$$

The Chern–Simons / bar-odd part is carried **entirely** by the phase `sin(2φ)`.
Three Lean facts pin the verdict:

1. **The phase suspicion is CORRECT — the phase is a maximal-leverage, independent
   DOF.** `nzImVolume_phase_hasDerivAt` / `_deriv`: `∂S/∂φ|₀ = √3·r² ≠ 0` (for
   `r≠0`). `nzImVolume_quarter_turn`: a quarter turn `φ:0↦π/4` swings `S` across its
   **full** `(√3/2)r²` range. This sensitivity is **NOT** bounded by #4288's
   boost-hyperbola magnitude ratio `ρ=barEven/barOdd` — phase and magnitude are
   genuinely independent degrees of freedom. **So the phase is not excluded by
   being bounded.**

2. **BUT the real substrate freezes the phase.** `substrate_meridian_arg_zero`:
   the substrate meridian coordinate is `u = 2·log q₀`, a **nonnegative real** for
   the physical `q₀ ≥ 1` (the meridian holonomy is multiplication by the real
   `q₀`), so `arg(u) = 0`. `anchor_phase_difference_zero`: both anchors are real
   `q₀ ≥ 1`, so `Δ(arg u) = 0`.

3. **The WALL.** `phase_channel_anchor_swing_zero`: evaluating `S` at two real
   anchors through the phase-frozen coordinate `φ = arg(u) = 0`, the anchor-swing of
   `S` is **exactly 0** — for arbitrary magnitudes. `nzImVolume_real_ray`: `S = 0`
   on the whole real ray (recovering the #3654 amphichirality `Im 𝔙(real)=0`). The
   isolated chain-rule crux `phase_sensitivity_times_frozen_displacement`:
   `(∂S/∂φ)·Δφ = (√3r²)·0 = 0` — the maximal-leverage sensitivity is multiplied by
   the frozen displacement.

## Numeric confirmation (both committed anchors)

| quantity | muon `q₀` | proton `q₀` |
|---|---|---|
| `u = 2·log q₀` | `0.208681463713…` (real) | `0.208681440639…` (real) |
| `arg(u)` | `0` | `0` |
| `S = (√3/2)|u|²·sin(2·arg u)` | `0` | `0` |
| `∂S/∂φ|₀ = √3·|u|²` | `0.07570…` (≠0, unbounded by #4288) | `0.07570…` |

`Δ(arg u) = 0` · **phase-channel anchor-swing `= 0` exactly** · target `c₃` swing
`= 3.47%`. All 4 gates pass.

## Verdict — WALL (scope-(a))

**This is not a handle. It is the genuine wall — and for a subtle, precise reason:
the phase `arg(u)` cannot carry the `c₃` anchor-swing at the observable
(real-`q₀`) level, NOT because it is bounded (it is not; it is a maximal-leverage
DOF orthogonal to #4288), but because the real substrate never MOVES it.** The same
reality of `q₀` that seeds Thurston's Newton onto the degenerate golden branch
(`Vol=0`, `CuspShapeBarParity`'s golden/cusp split) also pins `arg(u)=0`, killing
the phase-swing.

This is a **stronger** negative than the magnitude bound: #4288's magnitude channel
swings a small-but-nonzero 0.221 ppm; the phase channel swings **exactly zero** on
the real ray.

## What this proves vs residual

**Proved (this branch).** The phase leg that #4288 left open: at real `q₀` the phase
channel supplies exactly zero anchor-swing. Combined with **#4282** (`ω`-home
anchor-smooth) + **#4288** (magnitude bounded), **every categorical/geometric DOF at
real `q₀` supplies zero-or-negligible anchor-swing.**

**Residual / consequence.** Therefore `c₃`'s anchor-dependence is genuinely
**non-categorical** — it cannot originate in the categorical/geometric substrate at
the observable level. It is a **fibre-level** `ε = Im(q) ≠ 0` (`#3636`,
`fig8Trace_im_odd`: `sign S = sign ε`, no real `q₀` produces the flip) realized
through the `1/u³` ladder **representation** (`#3636`, `#3654`, `#4064`-refutation
`#3818`). This **confirms and completes** the merged 2026-07-12 wall-resolution
capstone: the observable-level phase is frozen; the phase DOF lives at the fibre
level where `Im q` is free (the `Im q` fibre-vs-observable wall, AGENTS.md), which
the observable anchor comparison structurally cannot access.

**`c₃` is NOT closed.** The branch-selection conjecture
`conj:algebraic-geometric-dilog-equivalence` **stays open** — what is proved is that
whatever branch it selects, the phase it would supply is frozen at the observable
level and cannot be the seat of the observable swing. No new fit; no `c_k` produced.

## Anti-laundering

No `c_k` value produced; `nzImVolume` is the corpus-derived leading NZ form,
*measured* against the committed `c₃` target, never fitted to it; nothing inverts
`Q_β`/CODATA; nothing wired; `c₃` stays a q₀-dependent near-match (SETTLED #1580).
Base ring: `ℝ` (genuinely archimedean — `Real.sin`, `Real.log`, `Complex.arg`,
ordering `1 ≤ q₀`), the correct wall placement (the observable / archimedean side of
the `Im q` wall).

## Cross-references

- #4282 (C1, bar-odd = ι-odd off-diagonal, anchor-smooth): [`2026-07-25-5two-gk-bridge-attack.md`](2026-07-25-5two-gk-bridge-attack.md).
- #4288 (magnitude channel bounded): [`2026-07-25-meridian-holonomy-c3-anchor.md`](2026-07-25-meridian-holonomy-c3-anchor.md).
- Wall-resolution capstone (Im 𝔙(real)=0; `1/u³` representation; ε=Im(q)): [`2026-07-12-c3-wall-resolution-capstone.md`](2026-07-12-c3-wall-resolution-capstone.md), [`2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md`](2026-07-12-c3-hypersensitivity-is-ladder-1-over-u3.md).
- Branch-structure (leading NZ `Im 𝔙 ~ (√3/2)|u|²sin(2 arg u)`; golden-ratio locus): [`2026-07-11-c3-wall-branch-structure.md`](2026-07-11-c3-wall-branch-structure.md).
- Self-dual-pole refutation (swing is a simple zero, not a pole): [`2026-07-19-c3-swing-selfdual-pole-vs-ladder.md`](2026-07-19-c3-swing-selfdual-pole-vs-ladder.md).
- Golden/cusp branch split: [`CuspShapeBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/CuspShapeBarParity.lean).
- Ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md).

-- Ref: [manuscript] docs/coordination/1ppq-qbeta.md
-- Ref: [neumann-zagier1985] https://doi.org/10.1016/0040-9383(85)90004-7
