# Lever-1: color E_q Gauss–Manin connection + three (a)-negatives → θ_binding's geometric origin is the W_λ side, not an elliptic period

**Date:** 2026-06-25
**Owner reversal:** the narrow s5-so3 keystone reversal (2026-06-19, PRs #2503/#2524) is **extended** by explicit owner sign-off (2026-06-25) to the **λ_SW Seiberg–Witten-period side** of the same keystone — the color `E_q` elliptic factor. Ledger: [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md). Parameter-free; not a fit-based q₀ derivation.
**Probe:** [`computations/substrate/lever1_color_eq_lambda_sw_rapidity.py`](../../computations/substrate/lever1_color_eq_lambda_sw_rapidity.py)
**Witness:** [`computations/substrate/lever1-color-eq-lambda-sw-rapidity.witness.json`](../../computations/substrate/lever1-color-eq-lambda-sw-rapidity.witness.json)
**Status:** one new validated object (the PF connection) + one clean (a)-scope negative. No closure; no fit; nothing wired.

## 0. Context — what was open

The binding kernel is `R = x² − τx + 1`, `det = 1` (proved), `τ = tr B = 2cosh θ`,
`τ(q₀) = 3(3q⁴+8q²+3)/(4q(q+1)²) = 2.6424`, `θ_binding = 0.78145`. Every prior probe
set `θ = acosh(τ_binding/2)` from the **wired anchor** value — circular. The genuine
question: does the color `E_q` *geometry* produce `θ_binding` without that input? The
prior session [`2026-06-24-lever1-color-eq-monodromy-integrality.md`](2026-06-24-lever1-color-eq-monodromy-integrality.md)
identified the curve (`j(q₀)=129.86`) and proved `B` is **not** the topological
Gauss–Manin monodromy (that is `SL₂(ℤ)`, integer trace; `2.6424 ∉ ℤ`), then punted the
explicit `λ_SW` connection holonomy as owner-gated. No script in the corpus had ever
written down the Picard–Fuchs connection of the family.

## 1. New: the explicit Gauss–Manin connection N(q) (Griffiths–Dwork)

For the family `E_q : y² = x³ + p(q)x + r(q)` (color/descartes coefficients), on the
de Rham basis `(ω = dx/y, ϖ = x dx/y)`, Griffiths–Dwork reduction gives the connection
`d/dq [ω, ϖ]ᵀ = N(q) [ω, ϖ]ᵀ` with

```
N(q) = −1/(2D) · [[ A , Bc ], [ Cc , −A ]],     D = (4a³ + 27b²)/6  (= −Δ/96),
  A  = a²a′/3 + (3/2) b b′,
  Bc = a b′ − (3/2) a′ b,
  Cc = −(1/2) a a′ b + a² b′/3,        a = p(q), b = r(q), ′ = d/dq.
```

**Two checks confirm it (no fit):**

- **`tr N = 0` exactly** (residual `0.0`) ⇒ `N ∈ sl₂`. This *re-derives geometrically*
  the proved `det B = 1` (`prop:sl2-prolongation-recurrence`): the monodromy of an
  `sl₂` connection is in `SL₂`.
- **The first-kind period `ω(q) = ∮ dx/y` satisfies the 2nd-order Picard–Fuchs ODE**
  that `N` implies (`w″ = c₁w′ + c₀w`, `c₁ = N₁₁+N₂₂+N₁₂′/N₁₂`,
  `c₀ = N₁₁′ − N₁₁N₁₂′/N₁₂ + N₁₂N₂₁ − N₁₁N₂₂`), with **relative residual `1.2×10⁻⁵`**
  (mpmath 30 dps, `ω` from the numerically integrated real period; `ϖ` eliminated since
  its naive integral is 2nd-kind / divergent). This validates the connection against an
  independent numerical period.
- **`−det N(q₀) = 0.0173 > 0`** along the whole path `[1, q₀]` ⇒ the connection is
  **hyperbolic** (real eigenvalues `±√(−det N)`), matching `τ > 2`.

This is the concrete object the M-workplan ([`2026-06-06`](../workplans/2026-06-06-deriving-bring-M-abelianisation-scalar.md)) and the prior probes named but never wrote down.

## 2. (a)-negative: the abelianised **transport** integral is NOT θ_binding

The natural reading of "abelianised (Cartan) `λ_SW` holonomy" is the spectral
eigenvalue 1-form integrated along the substrate path:

```
θ_spec = ∫₁^{q₀} √(−det N(q)) dq = 0.01410        (target θ_binding = 0.78145)
```

This is a **clean miss** — and decisively so:

| quantity | value |
|---|---|
| `θ_spec` (this construction) | **0.0141** |
| `2·θ_spec` (full-period convention) | 0.0282 |
| `θ_torus = 2 log q₀` (substrate calibration) | 0.2087 |
| **`θ_binding` (target)** | **0.7815** |

`θ_spec` undershoots the target by **~55×**, and is even **below the torus rapidity** —
so it is not a convention (×2) discrepancy but a wrong *scale*. The reason is structural:
the connection is weak (`√(−det N) ≈ 0.13`) and the substrate interval is short
(`Δq ≈ 0.11`), so **no q-transport over `[1, q₀]` can source the large binding rapidity
`θ_binding = 0.78`**.

**Scope — (a), per AGENTS.md §"Before declaring refuted":** this is a *scope-limited
negative on one construction* (the transport integral of the derived connection),
**not** a structural exclusion. It does **not** exclude the color `E_q` (the curve is
confirmed), and the connection `N(q)` is a **permanent correct contribution**
(PF-validated). What is excluded is only the *transport-integral* identification of
`θ_binding`.

## 2c. (a)-negative: the curve-intrinsic Tate-period candidate also misses

The one principled *intrinsic* candidate (probe
[`lever1_color_eq_intrinsic_tau_rapidity.py`](../../computations/substrate/lever1_color_eq_intrinsic_tau_rapidity.py),
witness `lever1-color-eq-intrinsic-tau-rapidity.witness.json`): the **Tate / multiplicative
period** `θ_cand = 2π·Im(τ_E)`, calibrated by the substrate torus where
`θ_torus = 2 log q₀ = 2π·Im(τ_torus)` (Tate parameter `q₀²`). `τ_E` validated by
`1728·kleinj(τ_E) = j` to `<10⁻⁶`.

| | q = 1 (classical) | q₀ (substrate) |
|---|---|---|
| `Im(τ_E)` | 0.93030 | 0.93058 |
| `θ_cand = 2π·Im(τ_E)` | 5.8452 | **5.8470** |
| `θ_binding = acosh(τ_binding/2)` | 0.7713 | **0.7815** |

**Clean miss, two ways.** (i) *Value:* `5.847` vs `0.7815` — **6.5× too large**. (ii)
*q-slope:* `θ_binding` rises `1.0×10⁻²` from q=1 to q₀, but `θ_cand` rises only
`1.8×10⁻³` — **~6× too flat**. The reason is structural: `Im(τ_E) ≈ 0.93` puts the color
`E_q` **deep in the fundamental domain** (a *generic* curve), **not** near the Tate/cusp
regime (`Im ≈ 0.03`) where the torus calibration lives — and the curve barely deforms
over `[1, q₀]` (`j: 128 → 129.86`), so no single-curve invariant carries `θ_binding`'s
q-sensitivity. **Scope (a):** this rules out *this* principled candidate, not literally
every intrinsic invariant (a `j`-tuned one could be forced — but that is fishing,
AGENTS.md §formalize-first).

## 3. The keystone, sharpened — three geometric candidates, three misses → redirect

`θ_binding` has now been confronted with the three natural geometric constructions on the
color `E_q` / `λ_SW` side, and **all three miss**:

| # | construction | result |
|---|---|---|
| 1 | **loop monodromy** (closed q-loop of `N`) | `SL₂(ℤ)`, integer trace, `2.6424 ∉ ℤ` — [prior session](2026-06-24-lever1-color-eq-monodromy-integrality.md) |
| 2 | **abelianised transport** (path `1→q₀` of `N`) | `0.0141`, ~55× too small — §2 |
| 3 | **intrinsic Tate period** (`2π·Im τ_E`) | `5.847`, 6.5× too large, 6× too q-flat — §2c |

So the geometric origin of `θ_binding` is **not a color-`E_q` period quantity at all** —
neither family (monodromy/transport) nor single-curve (intrinsic). This **redirects** the
keystone: `θ_binding` lives on the **`W_λ`-side Plancherel/MTC localization** (keystone
**residual (i)** — pin the Beasley–Witten gauge datum on `S³/2I` to the Hecke
`Rep U_q(sl_N)` blocks so `W_λ = d_q²/D²` is provably our category's Plancherel measure),
which is the corpus's already-open frontier and the active subject of the `W_λ`-defect
ladder (#2744, just landed on `main`). The color `E_q` is the correct *curve* (the rank-2
`W`), but `θ_binding = log λ₊` is read off the **representation-theoretic** `tr B`
(the selection rule), whose geometric face is the `W_λ` index — not an elliptic period.

## 4. Net

- **Delivered (new, validated):** the explicit Picard–Fuchs / Gauss–Manin connection
  `N(q)` of the color `E_q` family — trace-free `sl₂` (re-derives `det B = 1`),
  PF-validated to `1.2×10⁻⁵`, hyperbolic on `[1, q₀]`; and `τ_E(q)` validated by the
  Klein `j`-function.
- **Three (a)-negatives** on the three natural geometric constructions: loop monodromy
  (integer trace), abelianised transport (`0.0141`, ~55× small), intrinsic Tate period
  (`5.847`, 6.5× large + 6× too q-flat). Each constrains, none excludes the curve.
- **Redirect (the useful outcome):** `θ_binding` is **not** a color-`E_q` period — its
  geometric origin is the **`W_λ`-side Plancherel/MTC localization** (keystone residual i,
  the open frontier of #2744). The color `E_q` is the right *curve* (rank-2 `W`); the
  rapidity is read off the rep-theoretic `tr B`, whose geometric face is the `W_λ` index.
- No fit; nothing wired; no tier change to any production quantity.
