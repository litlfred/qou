# Covariance-kernel epic (`qou-x631`) — M₁ Track A: `Σh ∉ A`, so the character genus expansion does not directly apply

**Date:** 2026-08-28 · **Branch:** `claude/m1-genus-source-unblock-2026-08-28` (PR #5882) · **Tier:**
exact structural obstruction (scope-(a), with proof) + a normalisation correction · **Discipline:**
scope-(a); no fit; nothing wired; no `c_k`; L2 unchanged. **Epic:** `qou-x631`; gap `qou-k5r5`.

## What Track A set out to do

Execute the genus-1 second-order correction to `M₁ = Cov_Planch(Σh, ω₃)` via the Śniady genus
expansion (Thm 4.14), to read off the sign of `κ_n − κ` (the open nub). Thm 4.14 expresses the
**characters `Σ_k`** — elements of the algebra `A` of polynomial functions on Young diagrams — in the
free cumulants `R_k` of the transition measure, to second (genus-1) order. Step A1 was: write both legs
of the covariance in `R_k`.

## Two exact findings (transition measure + free cumulants over ℚ)

Producer: [`wlambda_covariance_epic_M1_A1_sigmah_in_free_cumulants.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_A1_sigmah_in_free_cumulants.py)
(exact `Fraction`; transition-measure atoms via Kerov interlacing weights; free cumulants via the
non-crossing moment–cumulant recursion; exit 0). All verified on **every** `λ ⊢ n` up to the stated `n`.

### 1. Normalisation: `R₄ = 3ω₃ − n` (not `ω₃ − n`)

`R₂ = n` on every `λ` (`n ≤ 8`). The 4th free cumulant is `R₄ = 3ω₃ − n`, i.e.
`Σ₃ = R₄ + R₂ = 3ω₃` and **`ω₃ = (R₄ + R₂)/3`**. The `r4Value := 3·omega3 − k` in
`YoungDiagramKernel.lean` is correct; the "`ω₃ = R₄ + R₂`" prose in the 2026-08-23 genus-source-unblock
audit was wrong by ×3 and is corrected there. Consequence: `M₁ = (1/3)·Cov(Σh, R₄)` — the sign is
unchanged (positive scalar), so every positivity conclusion in this arc stands.

### 2. `Σh = ½(p₂+p₂')` is NOT a polynomial in the free cumulants

Exact rational linear algebra over all `λ ⊢ n`, `n ≤ 10`, against every `R`-monomial of gradation
degree `≤ 8`: **no identity exists** for `Σh`. Its transpose-antisymmetric partner **does**:
`½(p₂ − p₂') = ½·R₃` exactly. The obstruction is structural, not a degree ceiling:

- Transposition acts on free cumulants by `R_k(λ') = (−1)^k R_k(λ)` (the transition measure of `λ'` is
  the reflection `x ↦ −x` of that of `λ`). A monomial `R_{k₁}···R_{k_m}` therefore has parity
  `(−1)^{deg}`, `deg = Σ k_i`.
- `Σh` is **transpose-invariant** (`p₂+p₂'` is symmetric in `λ ↔ λ'`), so if `Σh ∈ A` it is a sum of
  **even**-degree `R`-monomials, giving `E_Planch[Σh] ~ n^{(even)/2} = n^{integer}`.
- But `E_Planch[Σh] ~ C·n^{3/2}` (measured: `E/n^{3/2} → ≈0.977`, flat and converging; `E/n²` falls
  monotonically) — **odd** leading gradation degree 3.

Odd leading degree for a transpose-invariant function is impossible for an `R`-polynomial. **Hence
`Σh ∉ A`.**

## Consequence — the naive genus route is obstructed (redirect, not dead)

Śniady Thm 4.14 expands `A`-elements. `ω₃ = (R₄+R₂)/3 ∈ A` (degree-4, transpose-invariant, fine), but
**`Σh ∉ A`**, so Thm 4.14 does **not** directly give the second-order correction to `Cov(Σh, ω₃)`. This
is the exact analogue — one algebra up — of why the genus route was eliminated for the *dim-tilt*
kernel (`dim λ ∉ A`); here it is `Σh`, not `dim`, that escapes the algebra. The 2026-08-23 audit's
claim that "`Σh ∈ A`, so the polynomial-polynomial covariance is genus-accessible" is **retracted**:
one leg is not in `A`.

Why the **leading** order (`κ`) still came out (IO Kerov-CLT): the IO CLT is a statement about the
**rescaled-diagram shape field**, which handles linear statistics of the shape — a broader class than
`A`-polynomials — so `Cov(Σh, ω₃) ~ κ n^{5/2}` was legitimately obtained. The *second-order* correction
for a non-`A` linear statistic needs the **shape-field / linear-statistic second-order theory**
(Dołęga–Féray / Śniady "approximate factorization" and Gaussian-fluctuation-of-Young-diagrams,
`arxiv-1402.4615` / `1704.02352`), **not** the character genus expansion Thm 4.14.

## Honest status

- **Track A (genus via Thm 4.14 on `Σh`): obstructed** — scope-(a), with a proved reason (`Σh ∉ A`).
  Not "refuted for all routes": the *character* genus expansion is the wrong handle; the
  *shape-linear-statistic* second-order theory is the right one and is not excluded.
- **Redirect:** (i) continue Track A via the shape-field second-order (linear statistics of the VKLS
  fluctuation, where `Σh` is a legitimate test function), and/or (ii) lean on **Track D** (Fulman
  exchangeable-pair / Stein), which works on the up-down chain and never needs `Σh ∈ A`.
- Gap `qou-k5r5` stays **OPEN**. Nothing wired; sign/order still not claimed.

## Redirect reconnaissance — the shape-field papers give the LIMIT, not the RATE (2026-08-28)

The redirect above points at the shape-field / linear-statistic second-order theory (Dołęga–Féray
`1402.4615`, Dołęga–Śniady `1704.02352`). Extracted both (pymupdf) and read the main theorems. **They
do not close the sign either, for a new reason:**

- Both are stated for **Jack measure / Jack characters `θ^{(α)}_k`** — again character-algebra
  observables (`W_k(λ) = √k·θ^{(α)}_{(k,1^{n-k})}/n^{…}`), so `Σh ∉ A` bites here too.
- More fundamentally, their **"second-order asymptotics" IS the CLT**: first order = LLN (limit shape
  `Ω`), second order = **Gaussian fluctuations around `Ω`** (Kerov CLT). That CLT *is* the limiting
  covariance — i.e. **`κ` itself**, which this arc already derived. The papers give the **limit**
  `κ_n → κ`, **not the finite-n correction `κ_n − κ`** whose *sign* is the open nub.

So the three standard literature tools each fall short, each for a distinct reason:

| Tool | What it gives | Why it misses the sign |
|---|---|---|
| Śniady genus expansion (Thm 4.14) | 2nd-order expansion of **A-elements** in `R_k` | `Σh ∉ A` (this audit) |
| Fulman Stein / exchangeable pair | Berry–Esseen for a **marginal** distribution | a magnitude/distance bound, not a covariance **sign** (PR #5887) |
| Dołęga–Féray / Dołęga–Śniady | the **CLT limit** (= `κ`) | gives `κ`, not the finite-n **rate** `κ_n − κ` |

**Honest consolidated verdict.** The sign of `κ_n − κ` is a **bespoke rate-of-convergence result** —
the finite-n correction to a limiting Plancherel covariance whose two `~n^{5/2}` pieces (`P`, `N`)
nearly cancel — and it is **not** delivered by any off-the-shelf tool surveyed. This matches the
`qou-k5r5` bean's standing assessment (a "genuine analysis project, not closeable by probe-driven exact
computation"). The defensible arc status remains: **`κ > 0` derived + `M₁ > 0` exact to n≤67 (extending)
+ Lean `k ≤ 8`** — an *asymptotic-positivity + exact-finite-check* result, with the all-n sign an
explicitly-scoped open rate problem.

## Cross-references

- Genus source unblock (corrected here): [`2026-08-23-covariance-kernel-M1-genus-source-unblock.md`](2026-08-23-covariance-kernel-M1-genus-source-unblock.md)
- Correction-order / genus applicability (the "both legs polynomial" claim this audit narrows):
  [`2026-08-23-covariance-kernel-M1-correction-bulk-not-edge.md`](2026-08-23-covariance-kernel-M1-correction-bulk-not-edge.md)
- Revised workplan: [`../workplans/2026-08-28-M1-arc-revised-workplan.md`](../workplans/2026-08-28-M1-arc-revised-workplan.md)
- Gap bean `qou-k5r5`.
