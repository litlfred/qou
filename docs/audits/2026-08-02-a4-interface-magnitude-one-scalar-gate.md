# A=4 (⁴He) interface-operator magnitude: the wall is a ONE-SCALAR gate (2026-08-02)

**Branch:** `claude/a4-interface-magnitude-2026-08-02`
**Lean:** [`QOU/MassTheory/A4InterfaceMagnitude.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/A4InterfaceMagnitude.lean) (sorry-free, lean-direct exit 0, v4.24.0)
**Witness:** [`computations/deltalambda/a4-interface-magnitude-one-scalar-gate.witness.json`](../../computations/deltalambda/a4-interface-magnitude-one-scalar-gate.witness.json)
**Verdict:** WALL(scope-(a)) — magnitude open, surviving mechanism pinned to one scalar; plus a scope-(b) exclusion of the naive uniform `z`.

## Starting point

PR #4526 (`GeometricWLambdaA4Helium.lean`) left the A=4 magnitude at **WALL(scope-(a))**:
the s5-so3 normalized color-tube reweight brackets both AME targets with two 0-fit
endpoints — production `y_λ` (undershoot 0.243 MeV) and geometric `d_q²/D²` (overshoot
60.33 MeV) — but neither lands, and the normalized-measure bound `E₀·max|χ| = 266 MeV`
lies above the target, so it is not scope-(b) excluded.

Separately, the merged #3924 result (probe `b4-slater-antisymmetrizer-exchange-sign`)
gives a **sharper, parameter-free** form for the ≥4-body term: the ⁴He `[1⁴]`
complete-graph exchange matrix `G` has the exact spectrum `{±√5, ±1}`, so with one
per-pair bond magnitude `m` the eigenvalues are `{±m√5, ±m}`, giving

  `det(I + G) = (1 − 5m²)(1 − m²)`,  `b₄(m) = −ln det(I + G)`,

with the derived physicality ceiling `m < 1/√5` (writhe cap). The one open object is `m`
— precisely the standing Δ_λ magnitude gate.

## What this session proves (the push forward)

The two framings meet: both reduce to the **same single under-determined scalar** (the
per-pair magnitude `m` ≡ one intermediate normalized weight). The Lean file establishes,
sorry-free:

1. **`detG_eq_spectral_product`** — `det(I+G) = (1+m√5)(1−m√5)(1+m)(1−m) = (1−5m²)(1−m²)`
   is *derived* from the spectrum `{±√5,±1}` (not asserted).
2. **`magnitude_form_surjective`** (MAIN) — for **every** positive target `t`, there is an
   `m ∈ (0, 1/√5)` with `b₄(m) = t`, via the closed form
   `m*(t) = √((6 − √(16 + 20·e^{−t}))/10)` (proved algebraically: `det(I+G)(m*) = e^{−t}`
   exactly, no IVT). So the derived form reaches the **entire positive axis** in its one
   scalar. This is the sharp statement of the wall: matching an AME target is vacuous
   unless an independent categorical driver fixes `m`. The reaching `m` is a function of
   the target — an anchor-inversion = **FIT** — so this is a *reachability* result (⇒ not
   scope-(b) excluded), never a derivation, never wired.
3. **`b4_strictMono_on`** — `b₄` is strictly increasing on `(0, 1/√5)` ⇒ the gate is
   *exactly one* scalar and `m*` is unique.
4. **`naive_z_unphysical` / `detG_neg_of_above_ceiling`** — the framework's naive uniform
   per-pair magnitude `z ≈ 0.499` has `5z² > 1`, so `det(I+G)(z) < 0`: the attractive
   `−ln det` branch does not exist there. This is a **scope-(b) structural exclusion** of
   the naive-uniform-`z` mechanism, citing a proved invariant (the exchange spectrum
   `{±√5,±1}` ⇒ most-negative scaled eigenvalue `−m√5` ⇒ `det = (1−5m²)(1−m²)`).
5. **`documented_targets_all_reachable`** — each of `b₄ ≈ 9.243`, `|μ₄| ≈ 4.591`,
   `B(⁴He) ≈ 28.296` MeV is positive, hence reachable — each match is a fit.

## Reading vs #4526

#4526 read the obstruction as "the target sits between two normalized measures." This
session sharpens it: **the bracket width was never the obstruction.** With the derived
spectrum fixed, the magnitude functional is monotone and *surjective onto (0,∞)*; the
obstruction is that its single scalar `m` is free. Both the geometric-`W` overshoot
(#4526) and the naive-`z` overshoot (#3426, here excluded scope-(b)) run *past* the
physical value — so the surviving mechanism is a categorical principle fixing `m` strictly
**below** the naive `z` (equivalently a normalized `W` strictly below the geometric
`d_q²/D²`).

## Honest verdict

The A=4 ≥4-body magnitude is **open at scope-(a)**, surviving mechanism = one scalar
`m ∈ (0, 1/√5)` fixed by an as-yet-unidentified categorical driver. The naive uniform `z`
is scope-(b) excluded. No inversion is wired; `μ₄`/`B(⁴He)`/`b₄` never enter production;
`free_parameters = 0`. A GAP bean is filed for the surviving scalar `m`.
