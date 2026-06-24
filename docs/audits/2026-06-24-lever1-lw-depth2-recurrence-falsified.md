# Lever-1 option 3: the depth-2 constant-coefficient recurrence is FALSIFIED for `lw(c)` beyond the seed — `θ_binding` is a 3-point fit

**Date:** 2026-06-24
**Probe:** [`computations/substrate/lever1_lw_depth2_recurrence_test.py`](../../computations/substrate/lever1_lw_depth2_recurrence_test.py)
**Witness:** [`computations/substrate/lever1-lw-depth2-recurrence-test.witness.json`](../../computations/substrate/lever1-lw-depth2-recurrence-test.witness.json) (7/7)
**Status:** the "derive `θ_binding`" step (option 3), with a decisive negative. No fit; symbolic in `q` + 50-dps at `q₀`; not owner-gated (pure recurrence arithmetic). Follows [`2026-06-24-lever1-coral-eq-monodromy-integrality.md`](2026-06-24-lever1-coral-eq-monodromy-integrality.md).

## The question

Lever-1 reduces to `τ = tr B` with `B ∈ SL₂`, `det = 1`, so the prolonged periods obey the
depth-2 recurrence `a_D⁽ⁿ⁺²⁾ = τ·a_D⁽ⁿ⁺¹⁾ − a_D⁽ⁿ⁾`, and `θ_binding = arccosh(τ/2)` is its rate.
The identification is `a_D⁽ⁿ⁾ = lw(n−1)`, `lw(c) = (1/(c+1))·Σ_{λ⊢c+1} dim_q(λ)`. **`τ` is solved from
the n=2,3,4 seed**, so the n≥5 checks are the only real test — and any genuine `a_D⁽ⁿ⁾ = φ(Mⁿv₀)`
**must** satisfy the recurrence *exactly* (Cayley–Hamilton: `M² = τM − I`).

## The result — it fails, and increasingly

With `dim_q(λ) = [n]_q!/∏_{cells}[hook]_q` (symmetric `[k]_q`; convention validated:
`lw(2) = (q+1)²/(3q)` and `lw(3) = Family-A = (3q²+4+3q⁻²)/4` match the corpus exactly):

| `c` | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| `lw(c)` @ q₀ | 1 | 1.3370 | 2.5328 | 5.3761 | 13.560 | 37.368 |

`τ` from the seed (n=2,3,4) = **2.6424** (= the closed form `3(3q⁴+8q²+3)/(4q(q+1)²)`, exact). But the
recurrence `lw(c+1) = τ·lw(c) − lw(c−1)` with this `τ`:

| check (`a_D` index) | residual `lw(c+1) − (τ·lw(c) − lw(c−1))` | relative |
|---|---|---|
| n=5 (`c=3`) | **0.0205** | 0.4 % of `lw(4)` |
| n=6 (`c=4`) | **1.887** | 14 % of `lw(5)` |
| n=7 (`c=5`) | **6.914** | 18 % of `lw(6)` |

And the **windowed kernel is not constant** (a constant-coefficient depth-2 recurrence has a
window-independent kernel `τ_k = (a_D⁽ᵏ⁾+a_D⁽ᵏ⁺²⁾)/a_D⁽ᵏ⁺¹⁾`):

| window | `n=2,3,4` | `n=3,4,5` | `n=4,5,6` |
|---|---|---|---|
| `τ_k` | **2.6424** | **2.6505** | **2.9933** |

The consecutive ratios `lw(c+1)/lw(c)` = 1.34, 1.89, 2.12, 2.52, 2.76 are **increasing**, not
tending to a constant `λ`: `lw(c)` grows **super-geometrically** (like the involution numbers
`I(n) = Σ_{λ⊢n} f^λ` it q-deforms), so it cannot be `A·λᶜ + B·λ⁻ᶜ` for any fixed `λ`.

## Interpretation (strict (a)/(b) scope)

- **(b)-exclusion:** `lw(c)` does **not** satisfy a constant-coefficient depth-2 recurrence —
  *invariant cited: a constant-coefficient linear recurrence has a window-independent kernel, and
  the windowed `τ` drifts 2.6424 → 2.6505 → 2.9933.* Equivalently, `lw(n−1) ≠ φ(Mⁿv₀)` for any fixed
  2×2 `M` (Cayley–Hamilton would force an exact recurrence).
- **Consequence:** `θ_binding = arccosh(τ/2) = 0.7815` is a **3-point seed-fit artifact**, not a
  derived recurrence rate. The `a_D = lw` identification is exact only at the n=2,3,4 anchors — a
  cross-anchor **near-match** (0.4 % at n=5), exactly the pattern the canonical-distance discipline
  flags, not a derivation. The M-workplan's posited "verification at n=5" does **not** hold for the
  selection-rule values.
- **What this does NOT refute** (scope guard): it does **not** refute the
  `Jac(Bring) ~ E⁴` isogeny (sibling branch `mass-open-keystone-w-l2-root`,
  `2026-06-24-keystone-bring-jacobian-E4-elliptic-W-plane.md` — correct and complementary), nor the
  existence of a 2×2 `M` on the elliptic factor, nor the coral `E_q` curve identification
  (`j(q₀)=129.86`, confirmed). It refutes that the **selection-rule `lw` values ARE that `M`'s
  prolonged periods** beyond the seed.

## Implication for the keystone path

Deriving `θ_binding` as the rate of an `a_D = lw` depth-2 recurrence is a **dead end** — the
recurrence is over-determined (3 anchors, 1 kernel) and fails on the 4th. Two honest continuations
remain:

1. **Drop `a_D = lw` beyond the seed.** Compute the *genuine* prolonged periods of the abelianised
   `λ_SW` connection on the coral `E_q` (the sibling's elliptic factor `E = Bring/S₄`); they will be
   *some* sequence whose depth-2 `M` is exact by construction — and `lw` is then only the c=1,2,3
   physical anchors, not the period sequence.
2. **Accept `a_D = lw` and drop depth-2-constant.** Then `B` is not a fixed `SL₂` element; the
   "monodromy" is a genuinely `q`/`n`-dependent (variable-kernel) object — consistent with the
   super-geometric growth, but it forfeits the clean `τ = 2cosh θ` rapidity.

Either way, `τ_binding = 2.6424` stands only as the **seed (c=1,2,3) kernel**, and `θ_binding` is
not a keystone-derived constant. **Not a closure; a falsification that redirects the path.** No fit;
nothing wired; no tier change. Coordinated with `mass-open-keystone-w-l2-root` (whose open `j(E)` is
answered by the coral `j(q₀)=129.86`).
