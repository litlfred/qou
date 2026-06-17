# Jacobi–Anger §4a test with physical Wenzl weights (n=3) — 12.8% → 6.8%, tower gate sharpened

**Date:** 2026-06-17
**Compute:** [`qbeta_reeb_tower_jacobi_anger_physical_weight.py`](../../computations/qbeta/qbeta_reeb_tower_jacobi_anger_physical_weight.py)
**Status:** derive-or-refute result, TIERED. Nothing wired; c_3 stays cal-anchored.

## Context

The n→∞ brane-tower contraction keystone identifies the bar-odd brane-tower sector
with the Hahn–Exton q-Bessel (E_q(2) contraction) matrix coefficient. The sharp
falsifiable test is §4a of
[`2026-06-13-reeb-phase-qbessel-identification.md`](2026-06-13-reeb-phase-qbessel-identification.md):
the bar-odd `sinh((2m+1)η)` coefficients should be the Bessel values `2·J_{2m+1}(x)`
at a single substrate-fixed `x = x(q₀)`, reproduced at both anchors with no refit.

The committed witness `qbeta-reeb-tower-jacobi-anger.witness.json` ran §4a only on the
**unit-weighted** block sum — over-determination residual **0.128 (12.8%)** — with an
explicit note that this is *"NOT the physical Wenzl-weighted Markov trace."* So the
physical version of §4a was an open gap.

## Result

Running §4a with the **physical Wenzl/Jones–Markov weights** `y_λ(q₀)` (the weights
that actually appear in `tr_M = Σ_λ y_λ χ^λ`), at n=3:

| weighting | over-determination residual (single x) |
|---|---|
| unit (committed witness) | 0.128 (12.8%) |
| **physical y_λ (this)** | **0.0684 (6.8%)** |

- Solving `x` from the scale-free ratio `W_3/W_1 = J_3(x)/J_1(x)` gives
  `x* ≈ 4.5249` at both anchors; the predicted `W_5/W_1 = J_5(x)/J_1(x)` then misses
  the actual `W_5/W_1` by **6.8%**.
- Cross-anchor single-x swing is **1.8e-9** (the proton/muon anchors differ by ~1.3e-8,
  so x* tracks q₀ smoothly — no per-anchor refit needed at this truncation).
- The physical bar-odd order-3 coefficient `W_3 ≈ −1/4` is essentially anchor-stable.

## Reading (TIERED — refinement + sharper gate, NOT a closure)

1. **The physical weighting moves toward the q-Bessel structure.** Halving the
   residual (12.8% → 6.8%) when the arbitrary unit weights are replaced by the
   *physical* tr_M weights is supporting evidence that the real object is closer to the
   single-x Bessel form than the unit toy — not proof, but a directional signal.

2. **n=3 truncation alone does NOT close it (6.8% ≫ 1%).** This is exactly the audit's
   own caveat: a single `λ⊢3` trace is a finite sum of a few `sinh(kη)` terms — *not* a
   Bessel function. The Bessel object is the **infinite brane-tower**, carrying orders
   `7, 9, …` from levels `n = 6, 9, 12, …` that the n=3 truncation omits.

3. **The decisive gate is now sharp: does the residual → 0 as the tower extends?**
   The single-x over-determination residual, recomputed with physical weights at
   `n = 3, 6, 9, 12`, must **shrink monotonically toward 0** if the bar-odd tower is
   the q-Bessel contraction object. A residual that **plateaus or grows** with `n` is a
   clean refutation, on the same footing as the f-map and the unit-weighted run,
   quantified. This is the formalize-first gate that should run **before** any
   master-theorem Lean (the `lim_{n→∞} spectrum = q-Bessel zeros` formalization is
   premature until the numerical convergence is established).

## Discipline

- No fit (the ratio solve is a derive-or-refute over-determination check, not a curve
  fit); TIERED; nothing wired; c_3/Q_β stay cal-anchored regardless.
- Bessel here is the **ordinary** `J_ν` of the Jacobi–Anger identity (the proved
  `q→1` backbone, `ReebTowerJacobiAnger.lean`); the Hahn–Exton q-Bessel refinement at
  finite q is the next layer once the ordinary-J tower convergence is settled.
