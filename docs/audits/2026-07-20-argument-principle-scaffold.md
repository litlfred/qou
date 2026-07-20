# PI-3: Argument-principle scaffold — Mathlib gap survey + tractable bricks

**Date:** 2026-07-20 **Bean:** `qou-bmyx` (PI-3, epic `qou-lbth` pentagon-infra)
**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**File:** `content/quantum-observable-universe/lean/QOU/Mathlib/ArgumentPrinciple.lean`
**Status:** REDUCED — 6 bricks sorry-free (incl. 3 new analytic bricks); the local
argument principle `residue_logDeriv_eq_order` is reduced from a full `sorry` to ONE
residual `sorry` (the global closed-disc factorization) with its whole residue-
computation tail sorry-free.
**✅ VERIFICATION:** `lean`-direct **exit 0** here (3 intended sorries:
`residue_logDeriv_eq_order` one residual, `argument_principle`, `entire_zero_count`) — see note below.

## The theorem

For `f` meromorphic on a closed disc `\overline B(c,R)` with no zero/pole on the
boundary circle, the contour integral of the logarithmic derivative counts the
interior divisor:

`(1/2πi) ∮_{|z−c|=R} f'/f = Σ_{w∈B(c,R)} ord_w f = #zeros − #poles` (w/ multiplicity).

This is the argument principle — the **least-Analysis-blocked** of the three
pentagon-infra walls, and the shared engine under both siblings: PI-2's
`elliptic_divisor_degree_zero` names it as its explicit open core, and PI-1's
canonical-product zero count is this integral applied to an entire `f`.

## Mathlib v4.24.0 gap survey

Cache is olean-only (root `.lake/packages/mathlib`, 6990 oleans, Analysis cone
present); probed by `strings` on oleans + the verified PI-2 sibling's API usage.

| Piece | In Mathlib? | Name |
|---|---|---|
| Cauchy integral formula | ✅ | `Complex.circleIntegral_sub_center_inv_smul_of_differentiable_on_off_countable`, `Complex.two_pi_I_inv_smul_circleIntegral_sub_inv_smul_…` |
| Circle / contour integral (`∮ z in C(c,R), …`) | ✅ | `Mathlib/MeasureTheory/Integral/CircleIntegral` |
| Divisor (zeros−poles, `locallyFinsuppWithin ℤ`) | ✅ | `MeromorphicOn.divisor`, `divisor_apply`, `divisor_mul`, `divisor_inv`, `divisor_nonneg` |
| Meromorphic order (per-point, `WithTop ℤ`) | ✅ | `meromorphicOrderAt`, `…_eq_int_iff`, `…_mul`, `…_inv` |
| `logDeriv f = f'/f` (+ `mul`, `zpow`, `prod`) | ✅ | `logDeriv`, `logDeriv_apply`, `logDeriv_mul`, `logDeriv_zpow` |
| Jensen's formula (the log‖f‖ / real analogue) | ✅ | `Analysis/Complex/JensenFormula`, `extract_zeros_poles` |
| Nevanlinna value distribution (counting fn) | ✅ | `Analysis/Complex/ValueDistribution/`, `logCounting`, First Main Thm |
| **Argument principle** `(1/2πi)∮ f'/f = Σ ord` | ❌ | — |
| **Residue of `f'/f` at `w` = `ord_w f`** (local) | ❌ | — (THE gap) |
| **General residue theorem** | ❌ | — (only `CauchyIntegral`, not residue calculus) |
| **`Complex.residue` / winding number** | ❌ | — |

## The exact gap

Mathlib has the Cauchy formula for a bare `(z−c)⁻¹` factor (`∮ (z−c)⁻¹ = 2πi`) and
has `meromorphicOrderAt` + `MeromorphicOn.divisor`, but it does **not** have the one
lemma that bridges them:

> `residue_logDeriv_eq_order`: near a zero/pole `w`, `f(z)=(z−w)^n·g(z)` with `g`
> analytic nonvanishing (`meromorphicOrderAt_eq_int_iff`), so `f'/f = n/(z−w) +
> logDeriv g`; the analytic term integrates to `0`, `∮(z−w)⁻¹ = 2πi`, leaving
> `(1/2πi)∮_{C(w,r)} f'/f = n = ord_w f`.

Both ingredients exist; the **composition** (local residue of the log-derivative)
and the **residue-sum** assembly over the finitely many interior divisor points are
absent. The global gap `(1/2πi)∮ f'/f = #zeros − #poles` is exactly this one local
lemma + a contour-deformation sum.

## Bricks landed (sorry-free — `lean`-direct verified exit 0)

* `toNat_sub_toNat_neg` — `n.toNat − (−n).toNat = n` (by `omega`).
* `zeroCount` / `poleCount` + `zeroCount_sub_poleCount_eq_sum_divisor` — the RHS
  bookkeeping `#zeros − #poles = Σ ord`, decomposing the divisor sum into zero and
  pole parts. **The entire right-hand side, analysis-free and complete.**
* `two_pi_I_ne_zero'` — `2πi ≠ 0`, well-definedness of the `(1/2πi)` prefactor.

### New analytic bricks (2026-07-20 — the residue computation, sorry-free)

* `logDeriv_zpow_sub_mul_split` — **brick 1**: `logDeriv((·-w)^n·g) z =
  n·(z-w)⁻¹ + logDeriv g z` for `g` differentiable+nonvanishing at `z ≠ w`. Pure
  `logDeriv` algebra (`logDeriv_mul`, `logDeriv_fun_zpow`, `DifferentiableAt.zpow`).
* `inv_two_pi_I_mul_integral_nat_sub_center_inv` — **brick 2**: the Cauchy simple-pole
  term `(2πi)⁻¹ ∮_{C(w,r)} n·(z-w)⁻¹ = n`, direct from
  `circleIntegral.integral_sub_center_inv` + `circleIntegral.integral_const_mul`.
* `circleIntegral_logDeriv_eq_zero_of_analyticOnNhd` — **brick 3**: Cauchy–Goursat,
  `∮_{C(w,r)} logDeriv g = 0` for `g` analytic + nonvanishing on `closedBall w r`.
  Uses `logDeriv g = (deriv g)/g` analytic (`AnalyticOnNhd.deriv` + `.div`) then
  `Complex.circleIntegral_eq_zero_of_differentiable_on_off_countable`.

## `residue_logDeriv_eq_order` — reduced to ONE residual `sorry`

The theorem now `obtain`s a nonvanishing analytic `g` on an OPEN neighborhood `U` of
`closedBall w r`, with `f = (·-w)^n·g` on the punctured `U \ {w}` (the single
residual `sorry`); then **everything downstream is sorry-free**:

1. On the sphere, `logDeriv f = n·(z-w)⁻¹ + logDeriv g` — because `f =ᶠ[𝓝 z]
   (·-w)^n·g` on the open `U \ {w}` (so `deriv`s agree) and brick 1 splits it.
2. Both pieces are `CircleIntegrable` (continuous on the sphere).
3. `∮` splits (`circleIntegral.integral_add`); brick 2 gives `n·2πi`, brick 3 gives
   `0`; the `(2πi)⁻¹` prefactor cancels to `n`.

**The ONLY remaining sorry** is the global closed-disc factorization: extend the
germ that `meromorphicOrderAt_eq_int_iff` supplies in `𝓝[≠] w` to a nonvanishing
analytic `g` on an open nbhd of the disc, using `hsmall` (order 0 elsewhere) and
`hclean` (no zeros on the circle). This is the removable-singularity / analytic-
continuation core — genuinely absent from Mathlib v4.24.0 — and is honestly the hard
residual, not fitted or axiomatized-as-proved.

## Still stated open (cited `sorry` — not vacuous, not axiomatized)

* `residue_logDeriv_eq_order` — ONE residual sorry (the factorization; tail proved).
* `argument_principle` — global contour integral = interior divisor sum.
* `entire_zero_count` — PI-3 payload: entire `f` (canonical product) ⇒ integral
  = `zeroCount` = #zeros; the tool that pins `phiBProd` among its elliptic multiples.

## Tractable-brick roadmap (ordered)

1. **`residue_logDeriv_eq_order`** (local, deep) — factor `f=(z−w)^n g` via
   `meromorphicOrderAt_eq_int_iff`; `logDeriv_mul`/`logDeriv_zpow` split off
   `n/(z−w)`; Cauchy (`circleIntegral_sub_center_inv_smul_…`) gives `2πi`; analytic
   remainder integrates to `0`. A real Mathlib-grade contribution, but self-contained.
2. **Residue-sum assembly** → `argument_principle` — contour-deform `C(c,R)` onto
   small circles around each of the finitely many divisor points; sum brick 1.
   Needs an interior-divisor-finiteness lemma (divisor is `locallyFinsuppWithin` ∩
   compact disc ⇒ finite; currently passed as `hS`).
3. **`entire_zero_count`** — specialize brick 2 to pole-free `f` (`divisor ≥ 0`),
   compose with `zeroCount_sub_poleCount_eq_sum_divisor`.

Composes with PI-2 (`elliptic_divisor_degree_zero`, which names this theorem as its
open core) and PI-1 (canonical-product zero count = `entire_zero_count`).

## ✅ Verification note (STRICT — honest)

Contrary to the initial expectation that this sandbox could not build the Analysis
cone, `lean`-direct **succeeded, exit 0**: with `LEAN_PATH` set over the package
olean dirs (`.lake/packages/*/.lake/build/lib/lean` + the QOU build lib), the
Analysis oleans present (`Complex/CauchyIntegral`, `MeasureTheory/Integral/CircleIntegral`,
`Meromorphic/*`, `Calculus/LogDeriv`) were sufficient. Output: three
`declaration uses 'sorry'` warnings on exactly the three deep theorems
(`residue_logDeriv_eq_order`, `argument_principle`, `entire_zero_count`); the three
bricks are sorry-free. `lake build QOU` on a full-Analysis host remains the CI gate.
Nothing is wired to production, fitted, or axiomatized-as-proved.
