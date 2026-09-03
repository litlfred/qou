# Covariance-kernel epic (`qou-x631`) — M₁>0 machinery `qou-po72`: the de-poissonized (CS) leading constants in closed form, and `ρ_P = 2√6/5`

**Date:** 2026-08-29 · **Branch:** `claude/m1-tvok-CA-wall-po72-constants-2026-08-29` · **Tier:**
rigorous closed-form derivation (modulo the cited IO Kerov CLT) + numerical + Lean verification ·
**Discipline:** no fit (constants derived in closed form, then checked; `V_D` reported as a precise
measured value, no form claimed); nothing wired; no `c_k`; L2 unchanged. **Epic:** `qou-h315`; gap
`qou-k5r5`; task `qou-po72` (companion to `qou-tvok`).

## Result

The leading-order Cauchy–Schwarz margin `m∞ = ρ_P − √(V_D/V_A)` (the sufficient condition for
`M₁ > 0` at leading order, merged #5896/#5901) has its three ingredients now pinned in **closed
form**, parallel to `qou-tvok` step 1's `v_A`:

| constant | meaning | closed form | value |
|---|---|---|---|
| `V_A` | `Var(Σ\|c\|)/n²` | **`8/(9π²)`** | `0.0900633` |
| `Var(ω₃)` leading | `Var(ω₃)/n³` | **`1/3`** | `0.333…` |
| `P` | `Cov(Σ\|c\|,ω₃)` leading | **`8/(15π)`** | `0.169765` |
| **`ρ_P`** | `Corr(Σ\|c\|, ω₃)` | **`2√6/5`** (exact) | `0.9797959` |
| `V_D` | `Var(ΣD²)/n²` | *no elementary form* | `0.04159748…` |
| `m∞` | leading margin | `2√6/5 − √(V_D/V_A)` | `0.300186 > 0` |

`ρ_P`, `V_A`, `P`, and the `ω₃` variance are exact; `V_D` is summed exactly from closed-form hat
coefficients but has no elementary closed form (tested and none found — see below). The margin
`0.300186` reproduces the merged #5901 measured value `0.30019` to 5 digits, from three independent
routes now (IO Chebyshev sums, descent-DPP Bessel kernel, exact combinatorics to n=78).

## The headline: `ρ_P = 2√6/5`, with π cancelling exactly

`ρ_P = Â₃/√(3 V_A)` with `Â₃ = 8/(5π)` and `V_A = 8/(9π²)`. The striking fact is that **π cancels
entirely in the square**:

> `ρ_P² = Â₃²/(3 V_A) = (64/(25π²)) / (8/(3π²)) = 192/200 = 24/25`,

a purely **rational** number, so `ρ_P = √(24/25) = 2√6/5`. This is the exact RHS of the margin
inequality; the correlation of the content charge and the cubic content power is a clean algebraic
constant.

## Derivation (rigorous modulo the IO Kerov CLT)

1. **IO Kerov CLT (cited, Ivanov–Olshanski):** limiting (co)variance of two content statistics with
   test functions `f, g` is `Σ_{k} f̂_k ĝ_k / k`, with `f̂_k = (2/π)∫₀^π f(2cos t) sin(kt) sin t dt`.

2. **De-poissonization freezes k=1 (the crucial normalisation).** The (CS) margin is a *fixed-n*
   quantity. Gaussian conditioning on `|λ| = n` removes the field mode carrying the conserved `n = R₂`
   — the `k=1` mode — so **every CS variance sums `k ≥ 2` only**:
   > `V_A = Σ_{k≥2} Â_k²/k`, **not** `Σ_{k≥1} Â_k²/k`.
   This is why the (CS) `V_A = 8/(9π²)`, whereas `qou-tvok` step 1's `v_A = 8/π²` is the
   **poissonized** descent-DPP constant (`k ≥ 1`, what the Bessel-kernel sum directly measures).
   **Both are correct for their own ensembles**; the margin needs the conditioned (`k ≥ 2`) one. This
   is a genuine subtlety — `8/π²` is *not* the direct CS quantity — recorded here honestly, and it is
   **not** a numerical error in step 1 (that value is the true poissonized variance; it is a
   different object). The conditioned `Var(ω₃)/n³ = 1/3` matching the exact combinatorial
   `n(n−1)(n−2)/3` independently confirms the `k ≥ 2` normalisation is the physical one.

3. **Closed-form hat coefficients (elementary, `f̂_k = (c_{k−1} − c_{k+1})/2` from the Fourier-cosine
   coefficients of `f(2cos t)`):** for odd `k` (even `k` vanish by `x ↦ −x`):
   - `A(x) = |x|`: `Â_k = 8(−1)^{(k+1)/2}/(π(k²−4))`.
   - `x²`: `(x²)_k = δ_{k,3}` for `k ≥ 2` (the `k=1` mode is the frozen `R₂ = n`).
   - `Ω` (VKLS shape, `Ω(2cos t) = (4/π)(cos t(π/2 − t) + sin t)`):
     `Ω̂_k = (8/π²)[1/k − 1/(2(k−2)) − 1/(2(k+2)) + 1/(2(k−2)²) − 1/(2(k+2)²)]`.
     Reproduces the #5901 anchor `Ω̂₃ = 128/(75π²)` exactly.

4. **`V_A = 8/(9π²)`** via the rational series `Σ_{k odd≥3} 1/[k(k²−4)²] = 1/8 − 1/9 = 1/72`
   (the `qou-tvok` step-1 partial-fraction identity minus its `n=1` term), so
   `V_A = (64/π²)(1/72) = 8/(9π²)`.

5. **`P = Â₃/3 = 8/(15π)`, `Var(ω₃)/n³ = (x²)₃²/3 = 1/3`** (only `k=3` survives in both), whence
   `ρ_P = Â₃/√(3 V_A) = 2√6/5` (step §2 above; `π` cancels in the square).

6. **`V_D = Σ_{k odd≥3}(Ω̂_k − Â_k)²/k`.** Because `Â_k` alternates in sign, the square does not
   collapse; summed to machine precision from the closed-form hats, `V_D = 0.04159748…`. Candidate
   closed forms (`x/π²`, `x/π⁴`, rational multiples of `V_A`) were tested and **none matched**
   (`V_D·π⁴ = 4.052`, not rational-looking); the rational sub-piece `ΣΩ̂²/k` is likewise not clean.
   `V_D` is reported as a precise derived numeric, **no form asserted**. It satisfies the CS ceiling
   `V_D < Â₃²/3 = 64/(75π²) = 0.086461` with room, which is exactly the leading (CS) inequality.

## Verification

- **Numeric (`wlambda_covariance_epic_M1_po72_leading_constants.py`, exit 0, dps 50, NO float64):**
  closed-form hats vs the numerical integral agree to `1e-51` (odd `k ≤ 11`); `V_A`, `P`, `ρ_P` match
  their closed forms to `1e-15`/`1e-51`; the rational series is `1/72`; margin `0.300186` matches
  #5901.
- **Lean (`CSMarginCorrelationConstant.lean`, lean-direct exit 0, sorry-free):**
  - `csMargin_rhoSq_eq {K}[Field K][CharZero K]` — the rational identity `Â₃²/(3 V_A) = 24/25` over a
    generic char-0 field (§7c; `field_simp; ring`). The π-cancellation is the content; perturbing
    either constant breaks it, so it is falsifiable, not a tautology.
  - `csMargin_rho_eq` — the ℝ specialization `Â₃/√(3 V_A) = 2√6/5`, from the rational square plus
    nonnegativity (`Real.sqrt_sq`).

## Scope — what this is and is not

- **Is:** the exact de-poissonized leading constants of the (CS) margin (`V_A = 8/(9π²)`,
  `Var(ω₃)` leading `1/3`, `P = 8/(15π)`, `ρ_P = 2√6/5`), derived in closed form, triple-verified,
  the correlation Lean-proved. This pins the *targets* of the finite-n bounds and the leading-order
  margin `0.300186 > 0`.
- **Is not:** the finite-n bound. The remainder `|V_A/n² − 8/(9π²)| ≤ C_A n^{−p}` (and the analogous
  `C_D`, `C_P`) needs the bulk Euler–Maclaurin + Airy-edge constant derivation — the same
  **Olver-Bessel wall** documented for `qou-tvok`'s `C_A` (the bulk sine-kernel comparison needs
  Olver uniform Bessel asymptotics, genuinely absent from the corpus; the tail is classically
  boundable and the *limits* are free via the cited IO CLT — only the *rates* need Olver). `V_D`'s
  lack of a closed form does not affect the closure — it is a fixed constant `< 0.0416` and the
  margin is `0.300 > 0`.

## Consequence for the closure

The leading-order (CS) margin is now `m∞ = 2√6/5 − √(V_D/V_A) = 0.300186 > 0` with every ingredient
either exact or a precise derived numeric. Combined with `qou-tvok` (rate `θ^{−1}` for `V_A`,
resolved), the remaining rigorous gap for `M₁ > 0` all-n is: (i) the explicit finite-n remainder
constants `C_A, C_D, C_P` (the Olver-Bessel wall), and (ii) the exact check to `n=78` to bridge the
finite range — item (ii) is tractable in-corpus, item (i) needs the one cited Bessel-asymptotics
lemma.

## Compute + Lean

- [`wlambda_covariance_epic_M1_po72_leading_constants.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_po72_leading_constants.py) (exit 0; NO float64).
- [`CSMarginCorrelationConstant.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/CSMarginCorrelationConstant.lean) (lean-direct exit 0; sorry-free).

## Cross-references

- `qou-tvok` step 1 (poissonized `v_A = 8/π²`): [`2026-08-29-covariance-kernel-M1-tvok-leading-constant-vA.md`](2026-08-29-covariance-kernel-M1-tvok-leading-constant-vA.md)
- `qou-tvok` step 2 (`V_A` remainder rate `θ^{−1}`): [`2026-08-29-covariance-kernel-M1-tvok-remainder-rate.md`](2026-08-29-covariance-kernel-M1-tvok-remainder-rate.md)
- Machinery inventory + the Olver-Bessel wall: [`2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md`](2026-08-29-covariance-kernel-M1-machinery-inventory-and-route.md)
- Leading (CS) derivation (measured constants): `wlambda_covariance_epic_M1_io_leading_cs.py` (merged #5901)
- Epic `qou-h315`/`qou-x631`; task `qou-po72`; gap `qou-k5r5`.
