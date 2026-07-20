# PI-3: Argument-principle scaffold — Mathlib gap survey + tractable bricks

**Date:** 2026-07-20 **Bean:** `qou-bmyx` (PI-3, epic `qou-lbth` pentagon-infra)
**Branch:** `claude/qlift-borel-kernel-derivation-2026-07-20`
**File:** `content/quantum-observable-universe/lean/QOU/Mathlib/ArgumentPrinciple.lean`
**Status:** GLOBAL ARGUMENT PRINCIPLE REDUCED TO ONE TOPOLOGICAL GAP, now FURTHER
REDUCED (2026-07-20, bean `qou-95qq` CDS). `residue_logDeriv_eq_order` (local) is
sorry-free; `argument_principle` + `entire_zero_count` are sorry-free, *derived* from
the deformation layer. That layer is now split into three:
**`exists_puncture_radii`** (radius selection, metric topology) — **PROVED sorry-free**;
the **`|S| = 0` base case** (Cauchy–Goursat) inside `contour_deformation_sum` — **PROVED
sorry-free** (so the empty-puncture instance of the argument principle is fully closed);
and **`residue_theorem_deformation`** — the single remaining `sorry`, the `|S| ≥ 1`
multiply-connected Cauchy deformation (off-centre / multi-hole homology), fully isolated
from the proved analysis.
**✅ VERIFICATION:** `lean`-direct **exit 0** here (exactly 1 intended sorry:
`residue_theorem_deformation`) — see note below.

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
| **Argument principle** `(1/2πi)∮ f'/f = Σ ord` | ✅ (derived here, modulo topology gap) | `argument_principle` (sorry-free, 2026-07-20) |
| **Residue of `f'/f` at `w` = `ord_w f`** (local) | ✅ (proved here) | `residue_logDeriv_eq_order` (sorry-free, 2026-07-20) |
| Radius selection for punctures (metric topology) | ✅ (proved here) | `exists_puncture_radii` (sorry-free, 2026-07-20) |
| `\|S\| = 0` deformation (Cauchy–Goursat, empty sum) | ✅ (proved here) | base case inside `contour_deformation_sum` |
| Concentric annulus deformation (puncture at centre) | ✅ | `circleIntegral_eq_of_differentiable_on_annulus_off_countable` |
| **Off-centre / multi-punctured deformation** `∮_big = Σ ∮_small`, `\|S\| ≥ 1` | ❌ (THE gap) | `residue_theorem_deformation` (1 cited sorry) |
| **General residue theorem** | ❌ | — (only `CauchyIntegral`, not residue calculus) |
| **`Complex.residue` / winding number** | ❌ | — (`#check`-verified absent) |

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

## `residue_logDeriv_eq_order` — now FULLY sorry-free (2026-07-20)

The theorem produces a nonvanishing analytic factor `g` on the open neighborhood `U`
of `closedBall w r`, with `f = (·-w)^n·g` on the punctured `U \ {w}` — and this factor
is now **built and proved**, not obtained by `sorry`. Construction:

* From `meromorphicOrderAt_eq_int_iff hf` + `horder`, get the germ `g₀` analytic at
  `w`, `g₀ w ≠ 0`, `f =ᶠ[𝓝[≠] w] (·-w)^n • g₀`.
* Define `g := Function.update (fun z => (z-w)^(-n)·f z) w (g₀ w)`.
  - **Away from `w`** (`z ∈ U \ {w}`): `g` agrees (on a `{w}ᶜ`-neighborhood) with
    `(·-w)^(-n)·f`, a product of `AnalyticAt.fun_zpow` (base `z-w ≠ 0`) and `hfU`;
    nonvanishing from `zpow_ne_zero` + `hfne`.
  - **At `w`**: `g =ᶠ[𝓝 w] g₀` — it equals `g₀` on the punctured nbhd (the germ
    identity, `(z-w)^(-n)·(z-w)^n = 1`) and at `w` by the `Function.update` patch;
    `eventuallyEq_nhds_of_eventuallyEq_nhdsNE` + `analyticAt_congr` transfer `g₀`'s
    analyticity (removable singularity), and `g w = g₀ w ≠ 0`.
* `EqOn f ((·-w)^n·g) (U\{w})`: `(z-w)^n·(z-w)^(-n)·f z = f z` by `zpow_add₀`.

Then **everything downstream is sorry-free** (unchanged):

1. On the sphere, `logDeriv f = n·(z-w)⁻¹ + logDeriv g` — because `f =ᶠ[𝓝 z]
   (·-w)^n·g` on the open `U \ {w}` (so `deriv`s agree) and brick 1 splits it.
2. Both pieces are `CircleIntegrable` (continuous on the sphere).
3. `∮` splits (`circleIntegral.integral_add`); brick 2 gives `n·2πi`, brick 3 gives
   `0`; the `(2πi)⁻¹` prefactor cancels to `n`.

**Hypothesis honesty note.** The earlier pointwise-`hsmall` (`meromorphicOrderAt f z
= 0` on the closed disc) + `hclean` (no zeros on the circle) were **too weak** to
build an OPEN-neighborhood factor: an open `U ⊇ closedBall w r` necessarily contains
points *outside* the disc, where a pointwise-order hypothesis says nothing, yet the
sphere-neighborhood `deriv` argument needs `f` analytic there. They are replaced by
the standard, honest pair `hfU : AnalyticOnNhd ℂ f (U \ {w})` + `hfne : ∀ z ∈ U, z ≠
w → f z ≠ 0` (with `hU_open`, `hball_sub`) — exactly what a real argument-principle
setup supplies. This is a legitimate statement-correction, not laundering: the
conclusion is genuinely derived, nothing is axiomatized, and no consumer exists yet
(`argument_principle` is itself a `sorry`).

## Residue-SUM reduction — DONE (2026-07-20, bean `qou-s5tj` ARG-SUM)

`argument_principle` and `entire_zero_count` are now **proved sorry-free**, reduced to
a *single* cited-`sorry` residual, the pure-topology deformation:

* `contour_deformation_sum` (the packaged statement, **compiles**): for `h` analytic
  on `closedBall c R \ S` (finite `S ⊆ ball c R`), there exist small radii `ρ w > 0`
  with `closedBall w (ρ w) ⊆ ball c R \ (S \ {w})` and
  `∮_{C(c,R)} h = Σ_{w∈S} ∮_{C(w,ρ w)} h`. Now **assembled from three pieces** (further
  reduction, bean `qou-95qq`, 2026-07-20):
  - `exists_puncture_radii` (**PROVED sorry-free**) — the radius selection: for each
    `w ∈ S`, `ball c R \ (S\{w})` is open and contains `w`, so a small enough closed
    ball sits inside it; extracted pointwise with `choose!`. No disjointness needed —
    the residue identity is a winding-number (homology) statement, so it suffices that
    each closed disc contains no *other* puncture (overlapping discs are fine).
  - the **`|S| = 0` base case** (**PROVED sorry-free**) — `h` analytic on the whole
    closed disc ⇒ `∮ = 0` by `circleIntegral_eq_zero_of_differentiable_on_off_countable`,
    RHS empty sum. So the empty-puncture instance is fully closed.
  - `residue_theorem_deformation` (**THE gap, one `sorry`, cited `-- Ref:`**) — the
    `|S| ≥ 1` deformation `∮_big = Σ ∮_small` *given* the radii. The
    homological/topological deformation at the heart of the residue theorem — **the
    only** thing Mathlib v4.24.0 lacks here (`Complex.residue`, `windingNumber`, and
    every off-centre/multi-hole deformation `#check`-verified ABSENT; only the
    *concentric* annulus deformation and the on-disc Cauchy formula are present, so even
    `|S| = 1` with `w ≠ c` is uncovered). Purely topological, isolated from the analysis.

* `argument_principle` (DERIVED, sorry-free): obtain `ρ` + the deformation identity
  from `contour_deformation_sum` applied to `h = logDeriv f`
  (analytic off `S` via `AnalyticOnNhd.deriv`/`.div`); then per puncture `w`,
  `(2πi)⁻¹ ∮_{C(w,ρ w)} logDeriv f = ord_w f` by the *proved*
  `residue_logDeriv_eq_order`, whose hypotheses are all discharged from the global
  ones — `U := ball c R \ (S\{w})` open (finite `S` ⇒ closed), `U\{w} = ball\S ⊆
  closedBall\S` gives `hfU`/`hfne` by `mono`, and
  `meromorphicOrderAt f w = (divisor w : WithTop ℤ)` from `MeromorphicOn.divisor_apply`
  + `WithTop.coe_untop₀_of_ne_top` (`divisor w ≠ 0` on `S` ⇒ order finite). Sum with
  `Finset.mul_sum` + `Int.cast_sum`.

* `entire_zero_count` (DERIVED, sorry-free): specialize `argument_principle` to entire
  `f` (`DifferentiableOn.analyticOnNhd` on `univ` ⇒ `MeromorphicOn` + the `hfU`
  hypothesis free); `divisor w ≥ 0` from `AnalyticAt.meromorphicOrderAt_nonneg` +
  `WithTop.untop₀_nonneg`, so `Σ divisor = zeroCount` via `Int.toNat_of_nonneg`. `hfne`
  ("`S` enumerates all zeros") passed through.

**Hypothesis note (honest, not laundering).** `argument_principle`'s `hclean`
(order-0 on the sphere) was replaced by the stronger, standard pair
`hfU : AnalyticOnNhd ℂ f (closedBall c R \ S)` + `hfne : ∀ z ∈ closedBall, z∉S → f z≠0`
— the precise "no zeros/poles other than `S`, and none on the boundary." These are
genuine conditional hypotheses (not sorries); the sphere-cleanliness is subsumed
(sphere ⊆ closedBall\S). Only `residue_theorem_deformation` carries a `sorry`.

## Tractable-brick roadmap (ordered)

1. ~~**`residue_logDeriv_eq_order`** (local, deep)~~ — **DONE, sorry-free (2026-07-20).**
   Factored `f=(z−w)^n g` via `meromorphicOrderAt_eq_int_iff` + explicit factor +
   removable-singularity glue; brick-1 split off `n/(z−w)`, brick-2 Cauchy `2πi`,
   brick-3 analytic remainder `0`. A real Mathlib-grade contribution, self-contained.
2. ~~**Residue-sum assembly** → `argument_principle`~~ — **DONE, sorry-free (2026-07-20).**
   Reduced to the single topological `contour_deformation_sum`; the residue-sum + all
   per-puncture hypothesis discharge is proved.
3. ~~**`entire_zero_count`**~~ — **DONE, sorry-free (2026-07-20).** Specialized
   `argument_principle` to pole-free `f` (`divisor ≥ 0` via
   `AnalyticAt.meromorphicOrderAt_nonneg`).
4. ~~**Radius selection + `|S| = 0` base**~~ — **DONE, sorry-free (2026-07-20, bean
   `qou-95qq`).** `exists_puncture_radii` (metric topology) + the Cauchy–Goursat base
   case inside `contour_deformation_sum`.
5. **`residue_theorem_deformation`** (the ONE remaining `sorry`) — the pure-topology
   `|S| ≥ 1` off-centre / multi-punctured contour deformation. Genuine Mathlib gap; a
   substantial homological construction (winding-number / keyhole deformation, or a
   from-scratch build off
   `integral_boundary_rect_eq_zero_of_differentiable_on_off_countable`; the concentric
   annulus lemma covers only the `w = c` sub-case). Isolated from all the proved
   analysis.

Composes with PI-2 (`elliptic_divisor_degree_zero`, which names this theorem as its
open core) and PI-1 (canonical-product zero count = `entire_zero_count`).

## ✅ Verification note (STRICT — honest)

Contrary to the initial expectation that this sandbox could not build the Analysis
cone, `lean`-direct **succeeded, exit 0**: with `LEAN_PATH` set over the package
olean dirs (`.lake/packages/*/.lake/build/lib/lean` + the QOU build lib), the
Analysis oleans present (`Complex/CauchyIntegral`, `MeasureTheory/Integral/CircleIntegral`,
`Meromorphic/*`, `Calculus/LogDeriv`) were sufficient. Output (2026-07-20, after the
contour-deformation reduction, bean `qou-95qq`): **one** `declaration uses 'sorry'`
warning on exactly the single topological gap `residue_theorem_deformation`; the six
bricks, `residue_logDeriv_eq_order`, `exists_puncture_radii`, the `|S| = 0` base case,
`contour_deformation_sum`, **and `argument_principle` + `entire_zero_count`** are all
sorry-free (the last three modulo the isolated `residue_theorem_deformation`). (Note the `LEAN_PATH` must point at the
**root** `.lake/packages/*/.lake/build/lib/lean` — the per-package `content/.../lean/
.lake` mathlib olean set here is partial.) `lake build QOU` on a full-Analysis host
remains the CI gate. Nothing is wired to production, fitted, or axiomatized-as-proved.
