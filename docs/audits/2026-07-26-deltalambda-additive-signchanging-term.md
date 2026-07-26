# Δ_λ magnitude: the additive sign-changing many-body term M(A) — sign is DERIVED, magnitude is a FIT

**Date:** 2026-07-26 · **Branch:** `claude/deltalambda-additive-signchanging-term-2026-07-26`
· **PR:** #4316 · **Axis:** per-isotope binding `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` — the
**magnitude** wall.
**Tier:** derivation probe → **scope-(a) PARTIAL** (sign-change mechanism located and
structurally certified; magnitude closure open). **No fit wired.** Gate: Δ_λ
open-for-all for derivation routes (owner reversals 2026-07-11 / 2026-07-13); the
anti-fit / anti-laundering discipline is orthogonal and STILL STANDS.

- Lean (sorry-free, `lean`-direct exit 0, v4.24.0):
  [`QOU/MassTheory/AdditiveSignChangingTerm.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/AdditiveSignChangingTerm.lean)
- Probe: [`computations/deltalambda/deltalambda_additive_signchanging_term_probe.py`](../../computations/deltalambda/deltalambda_additive_signchanging_term_probe.py)
  · witness `deltalambda-additive-signchanging-term.witness.json`

## 0. The target inherited from #4307 (the two-point residual)

#4307 ([`DampingNonMonotoneWall.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/DampingNonMonotoneWall.lean))
proved sorry-free that the pure-**damping** class is walled: the residual
`M(A) = ρ_strong(A) − ρ_grad(A)` **changes sign**, so the Δ_λ magnitude closure is
an **additive** many-body term, not a suppression factor. At the fixed canonical
substrate `q₀ ≈ 1.10998` (muon-canonical computations layer):

| A | `ρ_grad(A)` | `ρ_strong(A)` (AME, targets only) | `M(A) = ρ_strong − ρ_grad` |
|---|-------------|-----------------------------------|----------------------------|
| 3 | `[3]_{q₀} = 3.3420` | 3.8128 | **+0.4708** (positive) |
| 4 | `[3][4]_{q₀} = 15.7396` | 13.0316 | **−2.7080** (negative) |

Ratio `M(3)/M(4) = −0.1738`. `ρ_strong` are the isospin/Coulomb-corrected AME
ratios `B(³H)/B(²H)`, `B(⁴He)/B(²H)` (#3986/#3990), consumed **only** as targets —
never inverted into a weight.

## 1. Scout (corpus-grep, `.lake` excluded)

- **Interface operator / PROBE-2** (`2026-06-23-interface-operator-derivation-and-4body-assembly.md`):
  the per-bond Markov factor is categorically DERIVED (z, z−h, z−h/2; zero params).
  The A=4 interface operator's scalar `ρ_F` extraction is **open and Rust-gated**
  (`2026-06-01-he4-multi-nucleon-interface-research-state.md`), so PROBE-2 does not
  yet hand us a computable M(A) directly. What it *does* give is the structural
  handle used here: nucleons occupy a **simplex** K_A whose bonds (edges) and
  frustrated 3-cycles (triangular faces) count differently across A — the
  bond/anti-bond crossing this session tests.
- **`conj:s5-so3-fiber-action`** (keystone ledger, `s5-so3-keystone.md`): the
  fibre-action level = nucleon-count route is real but reduces to the open colored
  Σ(2,3,5) WRT / `W_λ` geometric-realization object — not a computable additive
  M(A) at this session's granularity.
- **Corpus-grep for an additive many-body term here:** the interface audit's
  candidate #1 (additive/log linked-cluster) improves A-scaling but was recorded as
  "right A-scaling, wrong curvature", *and* it was tested against the **absolute**
  binding, not against the #4307 **two-point ratio residual** with the sign
  constraint. No prior artifact derives or bounds a *sign-changing* M(A) against the
  +0.4708/−2.7080 target. This is the distinct handle #4316 brings.

## 2. The formalize-first attack — the bond−frustration simplex term

**Principle under test.** On the A-nucleon coordination graph `K_A`, edges `C(A,2)`
are the 2-body bonds (attractive) and triangular faces `C(A,3)` are
geometrically-frustrated 3-cycles (a competing, sign-opposed contribution). The
natural additive many-body correction is

```
M(A) = s · (C(A,2) − κ · C(A,3)),   s > 0,   κ ≥ 0.
```

At A=3 (`C(3,2)=3, C(3,3)=1`): `M(3) = s(3 − κ)`.
At A=4 (`C(4,2)=6, C(4,3)=4`): `M(4) = s(6 − 4κ)`.
The **sign change comes from the structure**: triangles grow faster than edges
(`C(A,3)/C(A,2) = (A−2)/3`), so a fixed frustration weight `κ` that leaves A=3
bond-dominated (positive) can flip A=4 frustration-dominated (negative).

**Lean certificate (sorry-free, `AdditiveSignChangingTerm.lean`):**

- **(W) Structural sign-change window.** `signChange_iff_window`: for `s > 0`,
  `M(3) > 0 ∧ M(4) < 0 ↔ 3/2 < κ < 3`. The mechanism reproduces the #4307 sign
  pattern (`+` at A=3, `−` at A=4) on a genuine open interval — a **parameter-free
  structural capability**, established without touching the residual magnitudes.
- **(V) Anti-fit identifiability.** `fit_hits_any_target` + `fit_is_unique`: the map
  `(s, t) ↦ (3s − t, 6s − 4t)` (with `t = κs` the raw triangle weight) is a linear
  **isomorphism** (`det = 3·(−4) − (−1)·6 = −6 ≠ 0`). For **any** target pair there
  is a **unique** `(s, t)` reproducing it — so matching both residuals is
  *guaranteed* and carries **zero** predictive content.
  `fit_hits_physical_residuals` exhibits the instance at `(0.4708, −2.7080)`.

## 3. The derivation-vs-fit test — explicit free-parameter count

The honest discriminator is the free-parameter count against the **2-point** target:

| Form | free params vs 2-pt target | sign-changes? | lands both? | verdict |
|------|:-:|:-:|:-:|---------|
| `s·C(A,2)` (bonds only) | 1 (scale) | no | no | sign-wrong |
| `s·(edges − κ·tri)`, κ∈{1,2,3,[3]_q} | 1 (scale) | κ=2 only | **no** | sign-ok / magnitude-miss |
| `s·(edges − 4·tetra)` | 1 (scale) | no | no | tetra=0 at A=3 |
| `s·edges − t·tri` (**FIT**) | **2** | yes | **yes** | **FIT — vacuous, not wired** |

- **Sign needs 0 free parameters** (window W is structural).
- **Magnitude needs 2 free parameters** (V: the 2×2 system is invertible, so the
  match is automatic). The fitted `κ = t/s = 2.385` lands inside `(3/2, 3)` — the
  mechanism is *capable* of the sign at that magnitude, but capability at a fitted
  magnitude is **not a magnitude derivation**.
- **No 0/1-parameter derived form lands both residuals.** The probe's pre-registered
  0-shape-param candidates (including `κ = [3]_q`, the triangle's own q-integer —
  the most "canonical" un-tuned weight) all miss the ratio `−0.1738`.

A genuine derivation would fix `κ` (and the scale) from structure to 0–1 free
parameters, converting `M(3)/M(4)` into a *prediction*. That did not happen.

## 4. Verdict (STRICT scope classification)

**Scope-(a) PARTIAL — sign derived, magnitude open.**

- **(+) The sign-change mechanism is located and structurally certified.** The
  bond−frustration simplex term reproduces the #4307 `(+, −)` residual sign for the
  parameter-free window `κ ∈ (3/2, 3)` (Lean `signChange_iff_window`). This is a
  real, 0-parameter structural lead: the additive term the damping-wall demands
  *can* come from the simplex bond/anti-bond (edge vs frustrated-triangle) crossing.
- **(−) The magnitude closure is a fit, not a derivation.** Landing both residuals
  requires the two-weight form, whose match is *guaranteed* by the invertible 2×2
  map (Lean `fit_hits_any_target` / `fit_is_unique`) — a 2-parameter fit to 2 points,
  **non-evidential**. The fitted weights are not canonical Markov factors.

**Not claimed:** Δ_λ closed (this is per-λ-blind, a ratio-level A-scaling term, and
2 anchors ≠ all A). **Nothing wired.** `[A]_q!` remains valid (permanence
principle); the additive M(A) *re-weights* it.

**Anti-fit (STRICT).** `ρ_strong(3)=3.8128`, `ρ_strong(4)=13.0316` appear only as
targets and (in Lean `(V″)`) as an arbitrary point of the surjective fit map; no `q`,
`κ`, or scale solved from them into a canonical weight. "No seventh fit-based ansatz"
upheld — the two-weight match is explicitly *labelled* a fit, not offered as an
ansatz. PROBE-4 KL-positivity prune untouched. Base ring `ℝ` per §7c.

## 5. Where a real derivation would come from (open)

The sign is now cheap; the *magnitude* needs `κ` derived. Two non-fit routes:
1. **PROBE-2 A=4 interface operator `ρ_F`** (Rust-gated): if the H₃⁴→H₁₂ interface
   scalar supplies the frustrated-triangle weight `κ` directly, the ratio becomes a
   prediction. Blocked on the Rust kernel `ρ_F` extraction.
2. **s5-so3 fibre-action level = nucleon count**: if the level selection fixes the
   edge/triangle balance geometrically, likewise. Blocked on the colored WRT `W_λ`
   keystone.

Until one of those fixes `κ` to 0–1 free params, the magnitude stays open and no
M(A) is wired.

## Cross-references
- Inherited wall: [`DampingNonMonotoneWall.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/DampingNonMonotoneWall.lean) (#4307);
  single-q no-go: [`JetFiltrationTwoAnchorNoGo.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/JetFiltrationTwoAnchorNoGo.lean) (#4300).
- Interface operator / simplex bond structure:
  [`2026-06-23-interface-operator-derivation-and-4body-assembly.md`](2026-06-23-interface-operator-derivation-and-4body-assembly.md).
- s5-so3 keystone: [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md).
- Coordination ledger: [`docs/coordination/2026-07-26-deltalambda-additive-signchanging-term.md`](../coordination/2026-07-26-deltalambda-additive-signchanging-term.md).
