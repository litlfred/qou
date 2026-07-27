# Δ_λ A=3 magnitude — the GENUINE geometric W_λ (`d_q²/D²`) re-weight: corrects the sibling normalizer, still WALL(scope-a)

**Date:** 2026-07-27
**Branch:** `claude/deltalambda-s5so3-geometric-wlambda-2026-07-27` · **PR #4392**
**Axis:** Δ_λ A=3 magnitude source (Route 1, geometric) / s5-so3 keystone `W_λ` · Subgoal-2
**Tier:** forward probe (0-fit) + formalize-first Lean · **Discipline:** no fit, nothing wired, WALL classified scope-(a).

## The gap and the distinct angle

`#4364` (`BorromeanMagnitudeLift`) lifted the derived A=3 Borromean 3-body cluster to the
`H₉` joint-trace level via width-3 cabling, reaching `c₃(y_λ) = +0.297 MeV = 0.63× μ₃`
(`μ₃ = +0.4708`), 0-fit, `O(h⁴)` — a `~1.6×` near-miss. `lift_is_coefficient_ratio` proved
the residual is a **coefficient** question (a re-weight rescales `κ`; the shared `h⁴`
cancels). The s5-so3 keystone posits the block weight should be the **geometric** `W_λ`.

The sibling (`claude/deltalambda-a3-magnitude-source-walls-2026-07-26`, Route 1;
`S5So3WLambdaLift.lean` #4376) re-weighted with the **q-Plancherel proxy**
`W^{raw}_λ = d_q(λ)²/[n]_q!` and got `r_raw = c₃(W^{raw})/c₃(y_λ) = 52.62` (33× overshoot,
WALL). **My distinct angle:** that proxy is **not a probability measure** at the substrate
anchor — `Σ_λ d_q²/[n]_q! = D²/[n]_q! = 1.1109 ≠ 1` (witnessed). The corpus's own
[`WLambdaMTCLocalizationObligation.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/WLambdaMTCLocalizationObligation.lean)
states the genuine Beasley–Witten / RT localization weight on `S³/2I` is

$$
W^{\text{geom}}_\lambda = \frac{d_q(\lambda)^2}{D^2},\qquad D^2 = \sum_{\lambda\vdash n} d_q(\lambda)^2
\qquad\Bigl(\textstyle\sum_\lambda W^{\text{geom}}_\lambda = 1,\ \text{the C1 normalization}\Bigr),
$$

with `D² = Σ d_q²` "the genuine Plancherel normaliser, **NOT** `[n]_q!`" (that file's words).
So the genuine geometric measure is the sibling's raw weight divided by its own sum
`S = D²/[n]_q! = 1.1109`.

## Result — forward, 0-fit (all three weightings on the identical #4364 word)

| weight system | `Σ_λ` | `c₃` (MeV) | `r = c₃/c₃(y_λ)` | vs needed `r*≈1.585` |
|---|---|---|---|---|
| production `y_λ` (Wenzl principal spec) | 0.03175 | +0.29696 | 1.0 | baseline (`0.63× μ₃`) |
| sibling `d_q²/[n]_q!` | 1.11092 | +15.6267 | 52.62 | 33.2× overshoot |
| **genuine BW `d_q²/D²`** | **1.00000** | **+14.0664** | **47.37** | **29.9× overshoot** |

`r_geom = r_raw / S = 52.6226 / 1.11092 = 47.3684` (guard: computed both ways, agree). Same
`E₀`, same `|χ_λ|`, same cabled Borromean word `(Δ_A·Δ_B⁻¹)³` — only the weight system changes.

**Verdict: WALL(scope-a).** The correct normalizer (`D²`, not `[n]_q!`) shifts the number
by 11 % but does **not** change the verdict — the geometric measure overshoots the A=3
residual by ~30×, the wrong order, not the missing `1.585×`. `μ₃`, AME, CODATA never
inverted; 0 free parameters; nothing wired.

## Why there is no *other* geometric W_λ to try — the route converges on this wall

This is not "one more geometric guess failed"; `d_q²/D²` **is** the geometric W_λ, and the
corpus already proves there is no distinct free-scale geometric amplitude:

- **Self-duality `S⁴=1` (2026-07-17 synthesis).** The value-map legs
  (`keystone_value_map_pinned`, `KeystoneSelfDualSpectralNarrowing.lean`) show a positive
  normalised fusion-ground `S`-eigenvector **is** `d_q`; leg (C)'s `S⁴=1` narrowing
  **structurally excludes** any free-scale (WRT/Ẑ/F_K/q-Bessel) family from carrying the
  self-dual `d_q` vacuum row. The geometric route to the *value map* is comprehensively
  closed and structurally excluded — running an Ẑ/F_K-style "different geometric W_λ" is the
  laundering trap that audit names.
- **Framing collapse (2026-07-12 three-vectors,
  [`KeystoneModularTwist.lean`](../../content/quantum-observable-universe/lean/QOU/BraidKnot/KeystoneModularTwist.lean)).**
  Every framed colored-WRT weight `S_{0λ}·θ_λ^f` either breaks the **proved** `W_{λ′}=W_λ`
  symmetry (`θ_{λ′}=θ_λ⁻¹`) or, in the squared modulus at `|q|=1`, collapses to exactly the
  Verlinde–Plancherel measure `S_{0λ}² = d_q²/D²`.

So the geometric localization index localizes to `d_q²/D²`, and that measure walls. The
A=3 Δ_λ magnitude source is **not** the geometric block weight.

## Declined fit-trap (inoculation for the next agent)

`Σ y_λ = 0.03175 ≠ 1` — the production weights are not a probability measure. Putting **both**
weight systems on a common `Σ=1` (rescaling `y_λ` up by `1/Σy_λ ≈ 31.5`) gives
`r_both = r_geom·Σy_λ = 47.37·0.03175 = 1.504`, a tantalizing **5.1 % short** of `r*≈1.585`.
This is **not** a derivation: it is a normalization-convention choice `ρ_F` does not make (it
uses raw `y_λ`), and any exact-closing rescale `c = μ₃/(r_geom·c₃_y) = 0.0335` is
`μ₃`-inverted — a free parameter, hence a FIT. Declined ("no seventh fit-based ansatz").
`route_closes_with_rescale_iff` formalizes the `μ₃`-inversion dependence.

## Artifacts

- **Lean** (lean-direct **exit 0, sorry-free**):
  [`S5So3GeometricWLambda.lean`](../../content/quantum-observable-universe/lean/QOU/MassTheory/S5So3GeometricWLambda.lean)
  — `reweight_is_coefficient_ratio`, `geom_ratio_eq_raw_ratio_div_sum` (`r_geom = r_raw/S`),
  `geom_measure_normalized` (C1 `Σ=1`), `geomRoute_closes_iff`, `geom_route_walls`
  (`r_geom=47.369 ≠ 1.585`), `geom_cluster_overshoots` (`14.069 > μ₃`),
  `route_closes_with_rescale_iff` (the declined fit-trap).
- **Probe + witness:**
  [`s5so3_geometric_wlambda_borromean_lift_probe.py`](../../computations/deltalambda/s5so3_geometric_wlambda_borromean_lift_probe.py)
  → `computations/deltalambda/s5so3-geometric-wlambda-borromean-lift.witness.json`
  (`r_geom_derived=47.368`, `r_needed=1.585`, `closes=false`, `free_parameters=0`).

## Net

Three prior 0-fit routes walled the A=3 magnitude (sibling 2026-07-26). This adds the
**correctly-normalized** geometric Route 1: `d_q²/D²` (Σ=1) gives `r=47.37`, correcting the
sibling's `52.62` (which used the wrong `[n]_q!` normalizer) — **verdict unchanged, WALL(scope-a)**.
Combined with the self-duality + framing-collapse corpus results, the geometric block-weight
route **converges on this wall**: there is no distinct geometric `W_λ` amplitude left to try.
The A=3 Δ_λ exact-closure coefficient remains a genuine scope-(a) open — no derived substrate
value (weight `y_λ`/`W^{raw}`/`W^{geom}`, cable width `w=3`, brane-tower level) supplies it.

## Cross-references

- Sibling three-walls audit: [`2026-07-26-deltalambda-a3-magnitude-source-three-walls.md`](2026-07-26-deltalambda-a3-magnitude-source-three-walls.md)
- Geometric-route-closed synthesis: [`2026-07-17-wlambda-geometric-route-closed-real-gap-is-leg-b.md`](2026-07-17-wlambda-geometric-route-closed-real-gap-is-leg-b.md)
- Three-vectors framing synthesis: [`2026-07-12-keystone-wlambda-construction-three-vectors.md`](2026-07-12-keystone-wlambda-construction-three-vectors.md)
- Keystone ledger: [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md)
- Option-E ledger: [`docs/coordination/option-e.md`](../coordination/option-e.md)
