# Lever-1: the coral E_q Gauss–Manin connection, and an (a)-negative on the transport reading of θ_binding

**Date:** 2026-06-25
**Owner reversal:** the narrow s5-so3 keystone reversal (2026-06-19, PRs #2503/#2524) is **extended** by explicit owner sign-off (2026-06-25) to the **λ_SW Seiberg–Witten-period side** of the same keystone — the coral `E_q` elliptic factor. Ledger: [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md). Parameter-free; not a fit-based q₀ derivation.
**Probe:** [`computations/substrate/lever1_coral_eq_lambda_sw_rapidity.py`](../../computations/substrate/lever1_coral_eq_lambda_sw_rapidity.py)
**Witness:** [`computations/substrate/lever1-coral-eq-lambda-sw-rapidity.witness.json`](../../computations/substrate/lever1-coral-eq-lambda-sw-rapidity.witness.json)
**Status:** one new validated object (the PF connection) + one clean (a)-scope negative. No closure; no fit; nothing wired.

## 0. Context — what was open

The binding kernel is `R = x² − τx + 1`, `det = 1` (proved), `τ = tr B = 2cosh θ`,
`τ(q₀) = 3(3q⁴+8q²+3)/(4q(q+1)²) = 2.6424`, `θ_binding = 0.78145`. Every prior probe
set `θ = acosh(τ_binding/2)` from the **wired anchor** value — circular. The genuine
question: does the coral `E_q` *geometry* produce `θ_binding` without that input? The
prior session [`2026-06-24-lever1-coral-eq-monodromy-integrality.md`](2026-06-24-lever1-coral-eq-monodromy-integrality.md)
identified the curve (`j(q₀)=129.86`) and proved `B` is **not** the topological
Gauss–Manin monodromy (that is `SL₂(ℤ)`, integer trace; `2.6424 ∉ ℤ`), then punted the
explicit `λ_SW` connection holonomy as owner-gated. No script in the corpus had ever
written down the Picard–Fuchs connection of the family.

## 1. New: the explicit Gauss–Manin connection N(q) (Griffiths–Dwork)

For the family `E_q : y² = x³ + p(q)x + r(q)` (coral/descartes coefficients), on the
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
**not** a structural exclusion. It does **not** exclude the coral `E_q` (the curve is
confirmed), and the connection `N(q)` is a **permanent correct contribution**
(PF-validated). What is excluded is only the *transport-integral* identification of
`θ_binding`.

## 3. The keystone, sharpened

`θ_binding` is now caught between two failed natural geometric constructions:

1. **topological monodromy** (closed `q`-loop) — `SL₂(ℤ)`, integer trace, `2.6424 ∉ ℤ`
   ([prior session](2026-06-24-lever1-coral-eq-monodromy-integrality.md));
2. **abelianised transport** (open path `1 → q₀`) — too small by ~55× (this session).

So the object producing `θ_binding` is **neither** the loop monodromy **nor** the path
transport of the (now explicit) Gauss–Manin connection. The remaining candidate class is
a **curve-intrinsic** quantity at `q₀` (a period/regulator of `λ_SW` itself, not of the
`q`-family connection) — the genuine residual of the keystone. Testing intrinsic
curve-invariant combinations was **not** attempted here: without a pre-registered
principled prescription it would be numerology (AGENTS.md §formalize-first). The next
disciplined step is to pin that prescription (which `λ_SW` period/regulator at `q₀`),
then test it once.

## 4. Net

- **Delivered (new, validated):** the explicit Picard–Fuchs / Gauss–Manin connection
  `N(q)` of the coral `E_q` family — trace-free `sl₂` (re-derives `det B = 1`),
  PF-validated to `1.2×10⁻⁵`, hyperbolic on `[1, q₀]`.
- **(a)-negative:** the abelianised transport integral `∫√(−det N) dq = 0.0141 ≠ θ_binding`
  (undershoots ~55×). Rules out the transport reading; constrains, does not exclude.
- **Keystone sharpened:** `θ_binding` is neither loop-monodromy (integer trace) nor
  path-transport (too small) — it is a curve-intrinsic `λ_SW` period/regulator at `q₀`,
  still open. No fit; nothing wired; no tier change to any production quantity.
