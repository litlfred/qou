---
# qou-argp
title: 'Argument principle on an annulus — the single missing lemma for the converse theta zero locus'
status: in-progress
type: task
priority: high
created_at: 2026-08-08T08:00:00Z
updated_at: 2026-08-08T10:00:00Z
---

Split out of `qou-c1ln` row 2, which is otherwise closed. Everything the
converse zero locus needs is proved except one named lemma.

## Where it stands

`QOU/QBeta/C1ConnectionPoles.lean` proves, all sorry-free:

| | |
|---|---|
| `θ_p` holomorphic on `ℂ*` | `differentiableOn_qThetaC` |
| `θ_p(pw) = w·θ_p(w)` over `ℂ` | `qThetaC_functional_equation` |
| differentiated, and in log form | `deriv_…`, `logDeriv_qThetaC_functional_equation` |
| **the contour identity** | `qTheta_winding_step` |
| `θ_p(−p^k) = 0` | `qTheta_neg_zpow_eq_zero` |

`qTheta_winding_step` is `∮_{|z|=pρ} θ'/θ = 2πi + ∮_{|z|=ρ} θ'/θ` — the exact
form the argument principle consumes. What is missing is only the inference

> winding difference over an annulus = number of zeros inside, with multiplicity

after which: exactly one zero per fundamental annulus, `qTheta_neg_zpow_eq_zero`
supplies it at `−p^k`, so it is simple and the only one, so the zero set is
exactly `−p^ℤ` and the C1 pole divisor is exact rather than `⊇`.

Checked to hold at our substrate in `computations/qbeta/c3_w2_c1_theta_zero_count.py`
(5/5) — so this is a formalisation gap, not a mathematical doubt.

## What Mathlib has and lacks

**Lacks** (name scan at HEAD, 2026-08-07): `argumentPrinciple`, any
`windingNumber`, any complex residue (every `residue` hit is `IsLocalRing`),
`countZeros`.

**Has**: the full `circleIntegral` API including
`Complex.circleIntegral_eq_of_differentiable_on_annulus_off_countable` (annulus
Cauchy), `circleIntegral.integral_sub_center_inv` (`∮ (z−c)⁻¹ = 2πi`),
`circleIntegral.integral_add`, `circleIntegrable_sub_zpow_iff`,
`Analysis/Meromorphic/{Divisor, IsolatedZeros, Order}`, `AnalyticAt.order`,
`AnalyticOnNhd.deriv`. Plus, from this arc,
`C1ConnectionPoles.circleIntegral_scale` — change of variables for
`circleIntegral`, which Mathlib does not have at all.

## The decomposition, in the order to attempt it

1. ✅ **DONE 2026-08-08 — argument principle GIVEN a factorisation.** If `f = (∏_j (z − a_j)^{m_j}) · u` on a neighbourhood of the closed
   annulus with `u` holomorphic and non-vanishing there, then
   `(1/2πi)[∮_R − ∮_ρ] f'/f = Σ_j m_j·[ρ < |a_j| < R]`. Every ingredient exists:
   `logDeriv_mul` / `logDeriv_prod` split the integrand; `u'/u` is holomorphic on
   the annulus so its two circle integrals agree by the annulus Cauchy theorem;
   each `(z − a_j)⁻¹` contributes `2πi` when `|a_j| < R` (ball case) and `0` when
   `|a_j| > R` (holomorphic in the disc). `argumentPrinciple_annulus_single` in `C1ConnectionPoles.lean`: for
   `f = (·−a)^m·u` with `u` analytic and non-vanishing on an open `A` containing
   the closed annulus, and `r < ‖a‖ < R`,

       ∮_{|z|=R} f'/f − ∮_{|z|=r} f'/f = m·2πi.

   Supporting lemmas, all `θ`-free and upstreamable: `integral_inv_sub_inside`
   (`∮(z−a)⁻¹ = 2πi` inside), `integral_inv_sub_outside` (`= 0` outside),
   `logDeriv_pow_sub_mul` (the split `m/(z−a) + u'/u`). All sorry-free,
   `[propext, Classical.choice, Quot.sound]`.

   **And the payoff is proved**: `multiplicity_eq_one_of_winding_step` composes
   it with `qTheta_winding_step` (winding difference `= 2πi`) to force `m = 1`.
   So *conditional only on the factorisation existing*, the zero in each
   fundamental annulus is **simple**, and with `qTheta_neg_zpow_eq_zero` it is
   `−p^k` and there is no other. The converse zero locus now hangs on step 2 and
   on nothing else.
2. **Existence of the factorisation** — the real work. Zeros of a non-identically-zero
   holomorphic function on a compact annulus are finite (`AnalyticOnNhd` +
   isolated zeros + compactness), each has a finite order (`AnalyticAt.order`),
   and dividing them out leaves a non-vanishing holomorphic factor. Mathlib has
   the single-point factorisation; the global-on-a-compact-set version is the
   gap.
3. **Assemble** into the annulus argument principle, then apply to `θ_p`.

## Honest cost — revised after doing (1)

(1) took one session, as estimated, and is landed. (3) collapsed into it:
`multiplicity_eq_one_of_winding_step` already performs the assembly, so there is
no separate step 3 left.

**Everything now rests on (2) alone**: given `θ_P` holomorphic and not
identically zero on a neighbourhood of a closed annulus, produce
`θ_P = (·−a)^m·u` there with `u` analytic and non-vanishing. Mathlib has the
single-point factorisation (`AnalyticAt.order`, `IsolatedZeros`); what is
missing is the global-on-a-compact-set version — finitely many zeros by
compactness plus discreteness, then divide them all out. That is the
multi-session, upstreamable piece, and it is now the *only* thing between this
corpus and an exact C1 pole divisor.

## What it unlocks

The converse zero locus, hence an exact C1 pole divisor. Note `qou-c1wr`
established that **nothing consumes the divisor** — so this is worth doing for
the Mathlib contribution and for closing a named gap honestly, not because a
downstream number depends on it. Do not let it displace work that is consumed.

Relates: `qou-c1ln` (row 2), `qou-c1wr`, `qou-wgnx`.
