# GAP-A-4: A=3 Δ_λ magnitude from the coordination-EDGE structure — the braid-order WALL

**Date:** 2026-08-01
**Branch:** `claude/deltalambda-gap-a4-brane-tower-level-2026-08-01` (PR #4472)
**Axis:** per-isotope binding `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` — the A=3 3-body **magnitude**.
**Tier:** derivation probe. **Verdict: WALL(scope-a).** 0 fit; μ₃ never inverted; nothing wired.
**Gate:** Δ_λ open-for-all for derivation routes (owner reversal 2026-07-13); Subgoal-2 open-for-all (2026-07-11).

- Lean: [`QOU/MassTheory/BraneTowerLevelAmplitude.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/BraneTowerLevelAmplitude.lean) — sorry-free, `lean`-direct exit 0.
- Probe: [`computations/deltalambda/brane_tower_level_coordination_edge_probe.py`](../../computations/deltalambda/brane_tower_level_coordination_edge_probe.py)
  · witness `brane-tower-level-coordination-edge.witness.json`.

## The gap

`#4364` (`BorromeanMagnitudeLift`, merged) lifted the derived A=3 Borromean 3-body cluster
to the `H₉` joint-trace level via width-3 cabling of `(Δ_A·Δ_B⁻¹)³`, reaching
`c₃ = E₀·κ·h⁴ = +0.297 MeV = 0.63× μ₃` (`μ₃ = +0.4708`, `AdditiveResidualSimplex` #4320) —
a `~1.6×` NEAR-MISS. The missing factor is `r* = μ₃/0.297 = 1.585×`.
`lift_is_coefficient_ratio` (#4364) proved a LEVEL lift is a pure coefficient rescale (the
shared `h⁴` cancels), and the **three-walls audit** (2026-07-26) closed every LEVEL/WIDTH
route: geometric `W_λ` overshoots ~30× (#4392, `S⁴=1` ⇒ no other geometric measure);
derived color cable width `w=3` **is** #4364's `H₉` near-miss; the alternate level rule
`n★ = ℓ·n₀+k` is a refuted overshoot (10⁵–10⁷ %). So the missing `1.585×` is **not** any
derived tower LEVEL.

## The route attacked here — the coordination-graph EDGE structure

Per the mission redirect (GAP-A-4, the last un-excluded reading): not the level/width, but
the **jet-filtration depth / coordination-graph edge structure**. The structural
observation:

> `#4364`'s cabled word `(Δ_A·Δ_B⁻¹)³` uses only **two** of the three cable-pairs —
> `Δ_A` bonds cables `{0,1}`, `Δ_B` bonds `{1,2}`. The non-adjacent bond `{0,2}` is
> **absent**. A braid **linearly orders** its strands, so the coordination graph
> realizable by *adjacent* block-transpositions is the **path `P₃`** (`A−1 = 2` edges),
> not the physical triton's complete **`K₃`** (`C(A,2) = 3` edges, every pair bonded).

The forward-derived, 0-fit candidate factor is the edge ratio
`|E(K₃)|/|E(P₃)| = 3/2 = 1.5` — and it converges with the geometric route's own
both-Σ=1 fit-trap value `1.504` (#4392), ~5 % short of `r* ≈ 1.585`.

## Result — the edge factor has NO Brunnian-order-preserving braid realization

The probe adds the third (wraparound) bond `Δ_C = (1 2)(0 1)(1 2) = Δ_B·Δ_A·Δ_B`
(the standard adjacent-transposition decomposition of the non-adjacent swap — a
principled convention, stated, not tuned) and MEASURES the deficit + leading
`h`-exponent of three candidate words, all 0 fit, same `E₀` + `y_λ` normalization as `ρ_F`:

| word | coordination | deficit | measured `h`-order | `c₃` (MeV) | reading |
|---|---|---:|---:|---:|---|
| `(Δ_A·Δ_B⁻¹)³` | path `P₃`, 2 edges | `+0.0494` | **4.098** | `+0.207` | `O(h⁴)`, reproduces #4364 bare (deficit `0.049`) |
| `(Δ_A·Δ_B⁻¹·Δ_C)³` | triangle `K₃`, 3 edges | `−45.2` | **1.776** | `−189` | **breaks Brunnian → `O(h²)`, overshoots ~400×, sign flip** |
| `(Δ_A·Δ_B⁻¹)(Δ_B·Δ_C⁻¹)(Δ_C·Δ_A⁻¹)` | cyclic `S₃`-symm | `−10⁻¹⁴` | 0.30 | `−4×10⁻¹⁴` | **bar-balanced ⇒ cancels to `0`** |

- The **path** baseline reproduces #4364's bare `H₉` Borromean deficit (`0.049`) and order
  (`4.098`) exactly — the machinery is validated (my bare `c₃ = 0.207`; #4364's published
  `0.297` is the atom-dressed T/³He mean, so the gap `μ₃/0.297 = 1.585` is quoted against
  #4364's dressed value).
- The **triangle** (naive third edge as a genuine link) makes the `{0,2}` sub-link
  **non-trivial** → it contributes at `O(h²)`, so the deficit's leading exponent drops
  `4.098 → 1.776` and the magnitude **overshoots ~400× with a sign flip**. This is exactly
  the reference-probe warning: the *individual* channels `(Δ_A)³ = −0.125`,
  `(Δ_B⁻¹)³ = +0.973` are large/non-Brunnian; only the specific pairwise-cancelling
  combination is the small `O(h⁴)` value.
- The **cyclic** bar-balanced symmetrization (each edge once `+`, once `−`) **cancels to
  `0`**.

**So there is no braid word that adds the third coordination edge while keeping the
`O(h⁴)` Brunnian order *and* scaling the amplitude by `3/2`.** The `3/2` edge count is a
graph-combinatorial fact that does **not** translate into a `3/2` amplitude: the
`lift_is_coefficient_ratio` (#4364) cancellation needs a **shared `h⁴`**, which the
order-breaking third bond destroys. The braid **linear-order obstruction** is genuine —
the physical `K₃` coordination is not Brunnian-realizable as a third braid edge.

## Verdict — WALL(scope-a)

The coordination-edge reading of GAP-A-4 **walls**. This is a *scope-limited negative*
(the specific braid realization of the third bond, alone, does not supply an
order-preserving `3/2`), **not** a structural exclusion of the edge-count *ingredient* in
general — the graph fact `|E(K₃)|/|E(P₃)| = 3/2` stands (Lean `edge_ratio_A3`), and even
granting the (refuted) linear rule the `3/2` arithmetic gives `0.4455 ≠ 0.4708 = μ₃`
(`edge_scaling_near_miss`), still `~5 %` short. What is *refuted at the braid level* is the
**premise** that a third coordination edge can be added while preserving `O(h⁴)`
(`edge_reweight_requires_brunnian`: measured order `1.776 ≠ 4`).

Together with the three prior walls this **brackets the A=3 magnitude source completely**:
the missing `1.585×` is neither a derived LEVEL (three-walls 2026-07-26), nor a geometric
`W_λ` re-weight (#4392), nor a coordination-EDGE factor (this) — every 0-fit structural
quantity probed either matches the near-miss, overshoots, or breaks the order. The A=3 Δ_λ
exact magnitude closure remains **open** (scope-a), now with the coordination-edge route
closed.

## Lean (sorry-free, lean-direct exit 0)

`QOU.MassTheory.BraneTowerLevelAmplitude`:
- `pathEdges`/`completeEdges`, `braid_order_gap_A3` (`K₃ = P₃ + 1` edge), `edge_ratio_A3`
  (`= 3/2`) — the structural edge counts.
- `levelMagnitude` (generic `CommRing`, §7c), `edge_reweight_is_ratio` (a `ρ`-reweight
  scales magnitude by `ρ`, `h⁴` cancels).
- `CoordinationEdgeAmplitude` (§3b-cond class carrying the **open** edge-scaling RULE as
  the hypothesis field `ruleLinear`) + `fullCoordAmplitude_eq` (conditional corollary,
  no `sorry`). Conditional-proved ≠ premise-established: the probe refutes the premise.
- `edge_scaling_near_miss` (`3/2 × 0.297 ≠ μ₃`), `edge_scaling_residual_pos`,
  `edge_reweight_requires_brunnian` (the measured order-break `1.776 ≠ 4` that voids the
  rule) — the WALL.

## Anti-fit / honesty ledger

- **0 free parameters** throughout; `μ₃`, AME, CODATA never inverted. `Δ_C` convention
  stated `(0 2)=(1 2)(0 1)(1 2)`; no word chosen to hit `+0.4708`.
- Verdict **WALL(scope-a)** — not a structural (b) exclusion of the edge-count ingredient;
  the graph fact and the conditional arithmetic stand, only the braid *realization* of the
  premise is refuted (order fact, Lean-carried as hypothesis).
- Nothing wired. "No seventh fit-based ansatz" + PROBE-4 KL-prune stand. Formalize-first
  honoured: the WALL claim is a sorry-free Lean statement (parent-verified lean-direct
  exit 0).

## Cross-references

- Near-miss lifted: `BorromeanMagnitudeLift.lean` (#4364);
  `borromean_h9_magnitude_lift_probe.py`.
- Three prior walls: [`docs/audits/2026-07-26-deltalambda-a3-magnitude-source-three-walls.md`](2026-07-26-deltalambda-a3-magnitude-source-three-walls.md).
- Geometric `W_λ` wall: #4392; `S5So3GeometricWLambda.lean`.
- Target moment: `AdditiveResidualSimplex.lean` (#4320) — `μ₂=0, μ₃=+0.4708, μ₄=−4.591`.
- Conjecture: `conj:binding-manybody-eq-jet-filtration`
  ([`binding-manybody-jet-filtration.md`](../../content/quantum-observable-universe/mass-theory/binding-manybody-jet-filtration.md));
  edge-set hand-off [`docs/workplans/2026-07-11-binding-edge-set-geometry-handoff.md`](../workplans/2026-07-11-binding-edge-set-geometry-handoff.md).
- Option-E ledger: [`docs/coordination/option-e.md`](../coordination/option-e.md).
