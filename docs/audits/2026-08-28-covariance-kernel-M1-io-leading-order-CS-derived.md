# Covariance-kernel epic (`qou-x631`) — M₁>0: the (CS) condition is DERIVED at leading order (52% margin)

**Date:** 2026-08-28 · **Branch:** `claude/m1-io-leading-order-cs-2026-08-28` · **Tier:** analytic
derivation (scope-(a) POSITIVE; rigorous modulo the Ivanov–Olshanski CLT theorem, cited not re-proved)
· **Discipline:** **no fit** (analytic Chebyshev-mode integrals; 52% margin; matches exact data);
nothing wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`.

## Result

The Cauchy–Schwarz sufficient condition for `M₁>0` (PR #5896),
`(CS)  σ(ΣD²)/σ(Σ|c|) < ρ(Σ|c|, ω₃)`, holds **at leading order** with a large margin. Via the IO Kerov
CLT (same field that derived `κ = Ω̂₃/3 = 128/(225π²)`), (CS) reduces to the scalar inequality

> **`V_D := Σ_{k≥3 odd} (Ω̂_k − Â_k)² / k  <  Â₃²/3`**,

where `Â_k`, `Ω̂_k` are the Chebyshev-mode coefficients of `|x|` and of the VKLS shape `Ω(x)`. Computed
at 40 dps (`wlambda_covariance_epic_M1_io_leading_cs.py`, exit 0, NO float64):

| quantity | value | check |
|---|---|---|
| `V_D` | `0.0415974…` | — |
| `Â₃²/3` | `0.0864607…` | — |
| **margin `Â₃²/3 − V_D`** | `0.0448633` (**relative 51.9 %**) | **(CS) holds, large margin** |
| `ρ(Σ|c|,ω₃) → Â₃/√(3V_A)` | `0.979796` | exact-data asymptote `≈0.98` ✓ |
| `σ(ΣD²)/σ(Σ|c|) → √(V_D/V_A)` | `0.679610` | exact-data asymptote `≈0.67` ✓ |
| `Ω̂₃` vs `128/(75π²)` | agree to `2.9e-42` | field normalisation ✓ |
| `κ = Ω̂₃/3` | `0.05764049558…` | `= 128/(225π²)` ✓ |
| even-`k` `Â_k` (`k=2,4,6`) | `< 2e-47` | `x→−x` symmetry ✓ |

## Derivation (rigorous modulo the IO CLT)

The three (CS) ingredients are functionals of the single content profile `D(u)` (`D(u)=#{□:c(□)=u}`):

- `Σ|c| = Σ_u |u| D(u)` — linear, test function `A(x) = |x|`, `δ = n·∫A dΔ`.
- `ΣD² = Σ_u D(u)²` — quadratic; linearises to `2⟨D⟩δD`, test function `Ω(x) − |x|` (`= 2D_∞`),
  `δ = n·∫(Ω−|x|)dΔ` (dropped `Σ(δD)²` is `O(√n) ≪ n`).
- `ω₃ = Σ_u u² D(u) − C(n,2)` — linear, test function `x²`, the **pure `k=3` mode** (`k=1` frozen
  `= R₂=n`), `δ = n^{3/2}·(ξ₃/√3)`.

The IO field `Δ(2cosθ) = (1/π)Σ_{k≥2}(ξ_k/√k)sin kθ` gives `Cov(∫f,∫g) = Σ_k f̂_k ĝ_k/k`, hence
`Var(Σ|c|)/n² → V_A = Σ Â_k²/k`, `Var(ΣD²)/n² → V_D = Σ(Ω̂_k−Â_k)²/k`, `Var(ω₃)/n³ → 1/3`,
`P = Cov(Σ|c|,ω₃)/n^{5/2} → Â₃/3`. Then `σ_D/σ_A → √(V_D/V_A)`, `ρ_P → Â₃/√(3V_A)`, and
`(CS) ⟺ √(V_D/V_A) < Â₃/√(3V_A) ⟺ V_D < Â₃²/3`. (As a consistency check the same modes give
`M₁ = P − N = n^{5/2}·Ω̂₃/3 = κ n^{5/2}`, reproducing the merged κ derivation.)

`Â_k`, `Ω̂_k` decay like `1/k²` (the `|x|` kink), so `V_A, V_D` converge as `Σ 1/k⁵`; truncating at
`k=61` leaves a tail `< 1e-6`, negligible against the 52 % margin.

## What this proves, and the one remaining gap

- **Leading-order (CS) is DERIVED**, not fitted: an analytic integral with 52 % relative margin, whose
  two byproduct constants (`0.9798`, `0.6796`) independently match the exact finite-n data. This gives
  **`M₁ > 0` for all `n ≥ N₀`** via the soft (correlation/variance) route — **not** the intractable
  rate `κ_n − κ`, which every literature tool failed to sign.
- **Remaining (now crude):** a rigorous finite-n error bound showing the (CS) margin stays positive for
  `n ≥ N₀`, to connect the asymptotic to the exact check. The exact data already gives (CS) for **all
  `4 ≤ n ≤ 32`** with a stable `≈0.30` margin, and `M₁>0` exact to **n=78**; the leading margin is
  **52 %**, so the correction would have to be enormous to flip it. A crude `O(n^{-1/2})`-type bound
  suffices — the delicacy that defeated the rate is gone.
- **Honest scope.** "Rigorous modulo the IO CLT theorem (published) + a crude finite-n bound." Not yet
  a complete all-n proof, but the first route with the leading order *proved* and only a soft,
  large-headroom remainder. Gap `qou-k5r5` stays **OPEN** — but materially advanced.

## Compute

- [`wlambda_covariance_epic_M1_io_leading_cs.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_io_leading_cs.py)
  (exit 0; mpmath 40 dps; Chebyshev-mode integrals; NO float64; validated against κ, `Ω̂₃`, and the
  exact-data asymptotes).

## Cross-references

- (CS) reduction: [`2026-08-28-covariance-kernel-M1-cauchy-schwarz-margin-reduction.md`](2026-08-28-covariance-kernel-M1-cauchy-schwarz-margin-reduction.md)
- κ leading-order derivation (machinery reused): [`2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md`](2026-08-21-covariance-kernel-M1-kappa-analytic-IO-derivation.md)
- Revised workplan: [`../workplans/2026-08-28-M1-arc-revised-workplan.md`](../workplans/2026-08-28-M1-arc-revised-workplan.md)
- Gap bean `qou-k5r5`.
