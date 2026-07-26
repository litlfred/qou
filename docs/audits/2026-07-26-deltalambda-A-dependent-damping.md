# Δ_λ magnitude: the A-dependent DAMPING route is walled (residual non-monotone in A)

**Date:** 2026-07-26 · **Branch:** `claude/deltalambda-A-dependent-damping-2026-07-26`
· **PR:** #4307 · **Axis:** per-isotope binding
`B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` — the **magnitude** wall.
**Tier:** derivation probe → **honest WALL** (scope-(b) structural exclusion of the
pure-damping class). **No fit; nothing wired.** Gate: Δ_λ open-for-all for derivation
routes (owner reversals 2026-07-11 / 2026-07-13); anti-fit discipline STILL STANDS.

- Lean (sorry-free, `lean`-direct exit 0, v4.24.0):
  [`QOU/MassTheory/DampingNonMonotoneWall.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/DampingNonMonotoneWall.lean)
- Probe (6 assertions, exit 0):
  [`computations/deltalambda/deltalambda_damping_nonmonotone_wall_probe.py`](../../computations/deltalambda/deltalambda_damping_nonmonotone_wall_probe.py)
  · witness `deltalambda-damping-nonmonotone-wall.witness.json`

## 0. The wall inherited, and the route this session tested

#4300 ([`JetFiltrationTwoAnchorNoGo.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/JetFiltrationTwoAnchorNoGo.lean),
`a671b52f`) proved sorry-free that the single-knob `q`-scaled coinvariant graded
dimension `ρ_grad(A) = [A]_q!/[2]_q!` cannot land both light-nucleus anchors
(step-lock `[4]_q ≥ 4`, monotone in `q`, two-anchor no-go). The
[jet-filtration magnitude audit §4](2026-07-18-deltalambda-jet-filtration-magnitude.md)
placed the true magnitude in a **two-sided bracket**

```
sub-extensive  −ln det   (ρ_A ≤ C(A,2); too flat, caps below both targets)
        <   true binding magnitude   <
super-extensive  [A]_q!   (too steep; overshoots the A=3→A=4 growth)
```

and concluded the correct object is a **damped** `[A]_q!`. The task proposed two
damping realisations:
- **(a)** an A-locked **parabolic/skew quotient** of `[A]_q!` (graded dimension of a
  quotient of a positively-graded coinvariant algebra is `≤` the full one);
- **(b)** a **Demazure sub-crystal** (§7b) — a Bruhat-prefix **sub-sum** of `[A]_q!`,
  `≤` the full sum.

Both are **dampings**: a factor `D(A) ≤ 1` on `ρ_grad(A)`. This session asks whether
*any* such damping, driven by a derived principle (the isotope coordination-graph /
≥4-body-bond edge structure, or the Demazure level = nucleon count), lands both
anchors without a per-A fit.

## 1. The formalize-first principle, stated and tested

**Principle under test.** A damping factor `D(A) ≤ 1`, applied to the coinvariant
graded ratio at the **fixed canonical substrate** `q₀` (muon-canonical computations
layer, `q₀ ≈ 1.10998`), yields the corrected ratio `ρ̃(A) = D(A)·ρ_grad(A)`.

`q₀` is **fixed** — it is pinned by the three calibrations, **not** a free knob.
(Re-solving `q ≈ 1.26` to reach A=3, as the two-anchor no-go's Python solve did, is
*not* admissible as a canonical evaluation.) So the honest question is asked at `q₀`.

**What the data needs at `q₀`** (`ρ_strong` = isospin/Coulomb-corrected AME,
#3986/#3990; consumed as comparison bounds only):

| A | `ρ_grad(A)(q₀)` | `ρ_strong(A)` | residual `ρ_strong − ρ_grad` | needed `D(A)` |
|---|-----------------|---------------|------------------------------|---------------|
| 2 | 1 (ref) | 1 (ref) | 0 | 1 |
| 3 | `[3]_{q₀} = 3.3420` | 3.8128 | **+0.4708** (graded **under**shoots) | **1.1409 (amplify)** |
| 4 | `[3][4]_{q₀} = 15.7396` | 13.0316 | **−2.7080** (graded **over**shoots) | 0.8280 (damp) |

## 2. The wall — the required correction is NOT a damping

The residual **changes sign** between A=3 and A=4:

- **A=3 needs `D(3) = 1.1409 > 1` — amplification.** The graded dimension *already
  undershoots* the A=3 anchor at `q₀`. A damping `D(A) ≤ 1` only *decreases*
  `ρ_grad(3)`, moving *away* from the target. **No damping closes A=3.**
- **A=4 needs `D(4) = 0.8280 < 1` — damping.** Here damping is the right sign.

So the correction is `+` at A=3 and `−` at A=4. A **multiplicative damping
`D(A) ≤ 1` supplies a non-positive correction at every A** — it structurally cannot
produce a sign change. The two-sided-bracket "damp it down" intuition is **correct
for A=4 but wrong for A=3** at the physical substrate: the bracket
`det < true < graded` holds at A=4 (`6 < 13.03 < 15.74`), but at A=3 it is
`det < graded < true` (`3 < 3.34 < 3.81`) — the graded object *crosses* the true
value between A=3 and A=4.

This **generalises** the Demazure-only A=3 obstruction
([`DemazureSubcrystalGradedDim.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/DemazureSubcrystalGradedDim.lean),
`demazure_A3_family_le_full`: a Bruhat sub-sum `≤` full) from Demazure sub-sums to
the **entire pure-damping class** — covering route (a) parabolic/skew quotients and
any coordination-graph ≥4-body-bond suppression (which is trivial for A ≤ 3, so
`D(3) = 1`, and still leaves the A=3 undershoot) alike.

## 3. Lean certificate (sorry-free)

`QOU.MassTheory.DampingNonMonotoneWall`, over the rational substrate window
`q ∈ [1.109, 1.11]` (`q₀` lies inside):

- `damping_cannot_close_A3 (q) (1 ≤ q) (q ≤ 1.11) (d) (0 ≤ d) (d ≤ 1) : d·[3]_q < 3.8128`
  — monotonicity gives `[3]_q ≤ [3]_{1.11} = 3.3421`, and `d ≤ 1` with `[3]_q ≥ 0`
  gives `d·[3]_q ≤ [3]_q`; chain `< 3.8128`. **No damping reaches the A=3 target.**
- `substrate_A4_overshoots (q) (1.109 ≤ q) (q ≤ 1.11) : 13.0316 < [3]_q·[4]_q`
  — each factor is `≥` its value at the lower endpoint; product `≥ 15.702 > 13.0316`.
- `damping_route_walled` — packages both: at any window `q`, `d·[3]_q < ρ_strong(3)`
  while `ρ_strong(4) < [3]_q·[4]_q`. The `+`/`−` residual sign change is the wall.

## 4. Anchor robustness

The conclusion does **not** depend on the isospin/Coulomb correction. (U) needs only
`ρ_strong(3) > [3]_{1.11} = 3.3421`, true for the *raw* AME ratio
`B(³H)/B(²H) = 3.814`; (O) needs only `ρ_strong(4) < [3][4]_{1.109} = 15.702`, true
for the raw `B(⁴He)/B(²H) = 12.72`. Probe assertion `sign_change_robust_to_raw_ame`
confirms `r_raw(3) = +0.472 > 0`, `r_raw(4) = −3.017 < 0` — same sign pattern. The
wall is robust to the anchor values (used as one-sided bounds only).

## 5. Verdict (STRICT scope classification)

**(b) Structural exclusion of the pure-damping class.** Cited invariant: the
monotone-`≤ 1` action of a damping (`d·x ≤ x` for `x ≥ 0`, `d ≤ 1`) together with the
`q₀` A=3 undershoot `[3]_{q₀} < ρ_strong(3)`. No `D(A) ≤ 1` — parabolic/skew quotient
(route a) **or** Demazure sub-crystal (route b) — closes the A=3 anchor at the
canonical substrate. Both named routes are **walled**.

**What is NOT excluded (permanence principle).** `[A]_q!` remains a valid ingredient.
The exclusion is of *multiplicative damping*, not of A-dependence. The correction the
data requires is **sign-changing in A** — `+` at A=3, `−` at A=4 — which per the
permanence principle is an **additive many-body term** re-weighting `[A]_q!`, not a
suppression factor. That additive term is the remaining open target, and it is
scope-(a) (not shown impossible). **Nothing wired.**

**Anti-fit.** `ρ_strong(3) = 3.8128`, `ρ_strong(4) = 13.0316` are DERIVED-ELSEWHERE
comparison constants, consumed only as one-sided bounds; no `q` and no `d` solved from
them; no AME point inverted; PROBE-4 KL-positivity prune stays pruned; no seventh
fit-based ansatz.

## Cross-references

- Inherited no-go: [`JetFiltrationTwoAnchorNoGo.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/JetFiltrationTwoAnchorNoGo.lean) (#4300);
  escape: [`JetFiltrationGradedDimEscape.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/JetFiltrationGradedDimEscape.lean) (#4012).
- Demazure A=3 obstruction (the special case this generalises):
  [`DemazureSubcrystalGradedDim.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/DemazureSubcrystalGradedDim.lean).
- Two-sided bracket: [`2026-07-18-deltalambda-jet-filtration-magnitude.md §4`](2026-07-18-deltalambda-jet-filtration-magnitude.md).
- Determinant-family no-gos: [`2026-07-18-deltalambda-exchange-determinant-family-nogo.md`](2026-07-18-deltalambda-exchange-determinant-family-nogo.md).
- Coordination ledger: [`docs/coordination/2026-07-26-deltalambda-A-dependent-damping.md`](../coordination/2026-07-26-deltalambda-A-dependent-damping.md).
