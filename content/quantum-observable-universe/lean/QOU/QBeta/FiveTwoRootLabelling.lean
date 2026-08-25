import QOU.QBeta.FiveTwoRootStructure
import QOU.MathlibExt.ImplicitScalar
import Mathlib.Analysis.Calculus.Deriv.MeanValue
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# The real root as a differentiable function of `c` — bean `qou-glbl`

Gap A's last piece. `hasDerivAt_envelopeS` takes the root labelling
`Y₁ Y₂ Y₃ : ℝ → ℂ` as given, differentiable functions; this file builds the one
that carries the real root.

## Why this labelling and no other — Route 36 G9

    Y₁ φ = ((realRoot (cos φ) : ℝ) : ℂ)
    (Y₂ φ, Y₃ φ) = otherRoots (t − 2c) (t² − 2ct + 2c + 1)

is forced, not chosen. Every fact it needs was already proved:

| need | supplied by |
|---|---|
| the root exists | `exists_root_mem_Ioo` |
| it is **unique** in `(0,1)` | `real_root_neg_of_ne` — every other real root is negative |
| the IFT applies | `unitCubic_deriv_ne_zero`, and `∂p/∂y ≥ 7/4` is *tight* |
| the other two are continuous through the collision | `continuous_otherRoots` |

and `Y₁` comes out **real-valued by construction**, which is exactly the shape
`hasDerivAt_log_neg_ofReal` needs. That was the one residue `log_neg_route` left
open: route 2's lemma wants `Y` real-valued *near* `φ`, not merely real *at* `φ`,
and no pointwise fact about roots can supply it. The construction does.

## What uniqueness is for

`exists_hasDerivAt_implicit` is **local**: it produces *some* `g` solving the
equation near `c`, with no claim that `g` is the root anyone else means.
Uniqueness in `(0,1)` is what turns that into a statement about `realRoot` —
`g` is continuous and lands in the open interval `(0,1)`, so it *is* `realRoot`
near `c`, and the derivative transfers.

The bound has to be *strict* because uniqueness is quoted at **nearby**
parameters, not merely at `c` itself.

## The bound is `c < 3/2`, and getting past `c = 1` was the point

A first version carried `hc : c < 1`. That excludes `c = 1`, which is `φ = 0`, an
endpoint of the transport — so it would have cost an **exceptional point**, and
`envelopeS_total` tolerates exactly one, already spent on the collision
`φ₀ = 137.9206708879635°`. Two exceptions would have meant Gap A does *not* close
by assembling what is already proved.

It costs nothing, because uniqueness has a **second and independent proof** near
`c = 1`. `∂p/∂t = 3t² − 4ct + (2c+1)` has discriminant-in-`t` equal to
`16c² − 24c − 12`, negative on `c ∈ (−0.3956…, 1.8956…)`; so on `[1/2, 3/2]` the
cubic is strictly *increasing*, hence injective, hence has at most one real root
anywhere (`strictMono_unitCubic`). No root structure enters.

The two regimes overlap on `[1/2, 1]`: `real_root_neg_of_ne` covers `c ≤ 1`,
monotonicity covers `[1/2, 3/2]`. Together (`eq_realRoot'`) they give uniqueness
for every `c < 3/2` — which contains the entire arc range `[−1,1]` *plus* a
two-sided neighbourhood of the endpoint. So `c = 1` is interior, and `φ = 0`
needs no exception.

`VSide` separately is false at `φ = π` (Route 36 G7) and needs `x.im ≠ 0`, so it
lives on the open arc; this file covers all of `[0,π]`.

## The derivative

    dt/dc = −2t(1−t) / (3t² − 4ct + 2c + 1)

Checked against a numerical derivative at seven values of `c` spanning the arc,
agreeing to `5.7e-42` (Route 36). At `c = 3/4` it is exactly `−2/7`, the point
where `unitCubic_deriv_ge`'s bound `7/4` is attained.

**The 5₂ sum rule is PROVED**: `QOU.QBeta.FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`
and `fiveTwoSaddleSumRule_holds`, sorry-free, standard axioms.
-/

namespace QOU.QBeta.FiveTwoDeformedSaddle

open Set Filter Topology QOU.MathlibExt

/-! ### 1. The root in `(0,1)`, as a function -/

/-- **The root of `unitCubic c` in `(0,1)`.** Single-valued by `eq_realRoot`. -/
noncomputable def realRoot (c : ℝ) : ℝ := (exists_root_mem_Ioo c).choose

theorem realRoot_mem_Ioo (c : ℝ) : realRoot c ∈ Ioo (0 : ℝ) 1 :=
  (exists_root_mem_Ioo c).choose_spec.1

theorem realRoot_pos (c : ℝ) : 0 < realRoot c := (realRoot_mem_Ioo c).1

theorem realRoot_lt_one (c : ℝ) : realRoot c < 1 := (realRoot_mem_Ioo c).2

theorem unitCubic_realRoot (c : ℝ) : unitCubic c (realRoot c) = 0 :=
  (exists_root_mem_Ioo c).choose_spec.2

/-- **Uniqueness, and it is stronger than "unique in `(0,1)`".**

Every *positive* real root of `unitCubic c` equals `realRoot c` — no upper bound
needed, because `real_root_neg_of_ne` makes every root other than `realRoot c`
negative outright. The first draft carried `r < 1` and Lean flagged it as unused;
dropping it is the honest statement.

That also lines up with Route 36 G8, which measures exactly **one** positive real
root at every arc point: this is that fact, in the form a proof can use. It is
what makes `realRoot` a function rather than a choice, and what lets a local IFT
solution be identified with it. -/
theorem eq_realRoot {c r : ℝ} (hc : c ≤ 1) (h0 : 0 < r)
    (hp : unitCubic c r = 0) : r = realRoot c := by
  by_contra hne
  have hneg := real_root_neg_of_ne hc (realRoot_pos c) (realRoot_lt_one c)
    (unitCubic_realRoot c) hp hne
  linarith

/-! ### 1b. A second uniqueness regime, covering `c = 1` on both sides

`real_root_neg_of_ne` carries `c ≤ 1`, so it cannot see a two-sided neighbourhood
of `c = 1` — and `c = 1` is `φ = 0`, an endpoint of the transport. Rather than
spend an exceptional point there, note that uniqueness has a *second* and
entirely different proof nearby.

`∂p/∂t = 3t² − 4ct + (2c+1)` has discriminant-in-`t` equal to `16c² − 24c − 12`,
negative for `c ∈ (−0.3956…, 1.8956…)`. So on `[1/2, 3/2]` the cubic is strictly
**increasing**, hence has exactly one real root — no root-structure argument
needed. The two regimes overlap on `[1/2, 1]`, so together they give uniqueness
for every `c < 3/2`, and `c = 1` is interior. -/

/-- `d/dt unitCubic c t = 3t² − 4ct + (2c+1)`. -/
theorem hasDerivAt_unitCubic (c t : ℝ) :
    HasDerivAt (unitCubic c) (3 * t ^ 2 - 4 * c * t + 2 * c + 1) t := by
  have h1 : HasDerivAt (fun t : ℝ => t ^ 3) (3 * t ^ 2) t := by
    simpa using hasDerivAt_pow 3 t
  have h2 : HasDerivAt (fun t : ℝ => 2 * c * t ^ 2) (2 * c * (2 * t)) t := by
    simpa using (hasDerivAt_pow 2 t).const_mul (2 * c)
  have h3 : HasDerivAt (fun t : ℝ => (2 * c + 1) * t) (2 * c + 1) t := by
    simpa using (hasDerivAt_id t).const_mul (2 * c + 1)
  have h := ((h1.sub h2).add h3).sub_const 1
  unfold unitCubic
  convert h using 1
  ring

/-- **The `t`-derivative is positive for every `t`, when `1/2 ≤ c ≤ 3/2`.**

Not the same statement as `unitCubic_deriv_ge`, which bounds it *at a root* in
`(0,1)`. Here there is no root hypothesis and no constraint on `t` — which is
what strict monotonicity needs. -/
theorem unitCubic_deriv_pos {c t : ℝ} (h1 : 1 / 2 ≤ c) (h2 : c ≤ 3 / 2) :
    0 < 3 * t ^ 2 - 4 * c * t + 2 * c + 1 := by
  nlinarith [sq_nonneg (3 * t - 2 * c),
    mul_nonneg (by linarith : (0 : ℝ) ≤ c - 1 / 2) (by linarith : (0 : ℝ) ≤ 3 / 2 - c)]

/-- **`unitCubic c` is strictly increasing for `1/2 ≤ c ≤ 3/2`**, hence injective,
hence has at most one real root anywhere. -/
theorem strictMono_unitCubic {c : ℝ} (h1 : 1 / 2 ≤ c) (h2 : c ≤ 3 / 2) :
    StrictMono (unitCubic c) :=
  strictMono_of_hasDerivAt_pos (f' := fun t => 3 * t ^ 2 - 4 * c * t + 2 * c + 1)
    (fun t => hasDerivAt_unitCubic c t) (fun _ => unitCubic_deriv_pos h1 h2)

/-- **Uniqueness on `c < 3/2`** — the two regimes combined.

`c ≤ 1` goes through `real_root_neg_of_ne`; `1 < c < 3/2` goes through strict
monotonicity, which needs no root structure. The overlap is what lets `c = 1` be
an interior point rather than an endpoint. -/
theorem eq_realRoot' {c r : ℝ} (hc : c < 3 / 2) (h0 : 0 < r)
    (hp : unitCubic c r = 0) : r = realRoot c := by
  rcases le_or_gt c 1 with h | h
  · exact eq_realRoot h h0 hp
  · exact (strictMono_unitCubic (c := c) (by linarith) (by linarith)).injective
      (by rw [hp, unitCubic_realRoot])

/-! ### 2. `unitCubic` as a function of the pair -/

/-- The strict derivative of `(c,t) ↦ unitCubic c t`, with partials
`∂/∂c = −2t² + 2t` and `∂/∂t = 3t² − 4ct + 2c + 1`. -/
theorem hasStrictFDerivAt_unitCubic (c₀ t₀ : ℝ) :
    HasStrictFDerivAt (fun q : ℝ × ℝ => unitCubic q.1 q.2)
      ((-2 * t₀ ^ 2 + 2 * t₀) • ContinuousLinearMap.fst ℝ ℝ ℝ
        + (3 * t₀ ^ 2 - 4 * c₀ * t₀ + 2 * c₀ + 1) • ContinuousLinearMap.snd ℝ ℝ ℝ)
      (c₀, t₀) := by
  have hc : HasStrictFDerivAt (fun q : ℝ × ℝ => q.1)
      (ContinuousLinearMap.fst ℝ ℝ ℝ) (c₀, t₀) := hasStrictFDerivAt_fst
  have ht : HasStrictFDerivAt (fun q : ℝ × ℝ => q.2)
      (ContinuousLinearMap.snd ℝ ℝ ℝ) (c₀, t₀) := hasStrictFDerivAt_snd
  -- `unitCubic c t = ((t³ − (2c)·t²) + (2c+1)·t) − 1`, matching the definition's parse
  have h := (((ht.pow 3).sub ((hc.const_mul (2 : ℝ)).mul (ht.pow 2))).add
      (((hc.const_mul (2 : ℝ)).add_const 1).mul ht)).sub_const 1
  simp only [unitCubic]
  convert h using 1
  refine ContinuousLinearMap.ext fun v => ?_
  simp
  ring

/-! ### 3. `realRoot` is differentiable -/

/-- **`realRoot` is differentiable, with the implicit-function derivative.**

    d/dc realRoot c = −2·t·(1−t) / (3t² − 4ct + 2c + 1),    t = realRoot c

`hc : c < 1` is strict on purpose — see the module docstring. -/
theorem hasDerivAt_realRoot {c : ℝ} (hc : c < 3 / 2) :
    HasDerivAt realRoot
      (-(-2 * realRoot c ^ 2 + 2 * realRoot c)
        / (3 * realRoot c ^ 2 - 4 * c * realRoot c + 2 * c + 1)) c := by
  have hB : (3 * realRoot c ^ 2 - 4 * c * realRoot c + 2 * c + 1) ≠ 0 := by
    have h := unitCubic_deriv_ne_zero (realRoot_pos c) (realRoot_lt_one c)
      (unitCubic_realRoot c)
    intro hz
    exact h (by linarith)
  have hB' : ((-2 * realRoot c ^ 2 + 2 * realRoot c) • ContinuousLinearMap.fst ℝ ℝ ℝ
      + (3 * realRoot c ^ 2 - 4 * c * realRoot c + 2 * c + 1) • ContinuousLinearMap.snd ℝ ℝ ℝ)
      ((0 : ℝ), (1 : ℝ)) ≠ 0 := by simpa using hB
  obtain ⟨g, hg0, hgsol, hgd⟩ :=
    exists_hasDerivAt_implicit (hasStrictFDerivAt_unitCubic c (realRoot c))
      (by simpa using unitCubic_realRoot c) hB'
  -- the local solution IS `realRoot` near `c`: it is continuous, lands in `(0,1)`,
  -- and the root there is unique
  have hmem : ∀ᶠ x in 𝓝 c, g x ∈ Ioo (0 : ℝ) 1 := by
    refine hgd.continuousAt ?_
    rw [hg0]
    exact Ioo_mem_nhds (realRoot_pos c) (realRoot_lt_one c)
  have hlt : ∀ᶠ x in 𝓝 c, x < 3 / 2 := Iio_mem_nhds hc
  have heq : realRoot =ᶠ[𝓝 c] g := by
    filter_upwards [hgsol, hmem, hlt] with x hx1 hx2 hx3
    exact (eq_realRoot' hx3 hx2.1 hx1).symm
  have := hgd.congr_of_eventuallyEq heq
  simpa using this

/-- `realRoot` is continuous wherever it is differentiable. -/
theorem continuousAt_realRoot {c : ℝ} (hc : c < 3 / 2) : ContinuousAt realRoot c :=
  (hasDerivAt_realRoot hc).continuousAt

/-! ### 4. Along the arc — and `Y₁` is real-valued *as a function*

`c = cos φ ≤ 1 < 3/2` for **every** `φ`, so the arc never leaves the regime of
§3 and there is no side condition to carry here at all. -/

/-- The real root along the transport arc, as a function of `φ`. -/
noncomputable def realRootPath (φ : ℝ) : ℝ := realRoot (Real.cos φ)

theorem realRootPath_pos (φ : ℝ) : 0 < realRootPath φ := realRoot_pos _

theorem realRootPath_lt_one (φ : ℝ) : realRootPath φ < 1 := realRoot_lt_one _

/-- **`realRootPath` is differentiable at every `φ`** — no exceptional point.

`cos φ ≤ 1 < 3/2` unconditionally, so `hasDerivAt_realRoot` applies everywhere on
the arc and the chain rule does the rest. This is where the widened bound of §1b
pays: with `c < 1` this statement would have had to exclude `φ = 0`. -/
theorem hasDerivAt_realRootPath (φ : ℝ) :
    HasDerivAt realRootPath
      ((-(-2 * realRoot (Real.cos φ) ^ 2 + 2 * realRoot (Real.cos φ))
        / (3 * realRoot (Real.cos φ) ^ 2 - 4 * Real.cos φ * realRoot (Real.cos φ)
            + 2 * Real.cos φ + 1)) * (-Real.sin φ)) φ := by
  have hc : Real.cos φ < 3 / 2 := by
    have := Real.cos_le_one φ; linarith
  exact (hasDerivAt_realRoot hc).comp φ (Real.hasDerivAt_cos φ)

/-- **`Y₁`, the labelling's real branch.**

Written as `((· : ℝ) : ℂ)` of a *real* function on purpose, not as a `ℂ`-valued
function that happens to take real values. `hasDerivAt_log_neg_ofReal` — route 2
of `log_neg_route`, the only route available at the positive real root — is
stated for exactly this shape, and no pointwise fact about roots can supply it.
Route 36 G8/G9: the positive real root is where route 1 is *impossible*, and this
is the root that carries it. -/
noncomputable def Yreal (φ : ℝ) : ℂ := ((realRootPath φ : ℝ) : ℂ)

theorem hasDerivAt_Yreal (φ : ℝ) :
    HasDerivAt Yreal
      ((((-(-2 * realRoot (Real.cos φ) ^ 2 + 2 * realRoot (Real.cos φ))
        / (3 * realRoot (Real.cos φ) ^ 2 - 4 * Real.cos φ * realRoot (Real.cos φ)
            + 2 * Real.cos φ + 1)) * (-Real.sin φ) : ℝ)) : ℂ) φ :=
  (Complex.ofRealCLM.hasFDerivAt.comp_hasDerivAt φ (hasDerivAt_realRootPath φ))

/-- `Yreal` never vanishes — it is a root in `(0,1)`. -/
theorem Yreal_ne_zero (φ : ℝ) : Yreal φ ≠ 0 := by
  simp only [Yreal, ne_eq, Complex.ofReal_eq_zero]
  exact (realRootPath_pos φ).ne'

/-- `Yreal` solves the cubic — the reason it is a *root* path and not just a
smooth curve. -/
theorem unitCubic_realRootPath (φ : ℝ) :
    unitCubic (Real.cos φ) (realRootPath φ) = 0 := unitCubic_realRoot _

theorem continuous_realRootPath : Continuous realRootPath :=
  continuous_iff_continuousAt.mpr fun φ => (hasDerivAt_realRootPath φ).continuousAt

/-! ### 5. The other two branches

`Y₂` and `Y₃` are the roots of the quadratic cofactor, whose coefficients are the
*symmetric* functions `β = t − 2c` and `γ = t² − 2ct + 2c + 1`. Those are smooth
in `φ` wherever `t` is — with **no exceptional point** — which is the whole reason
Gap A is tractable: only the *splitting* of the pair degenerates at `φ₀`, not the
pair itself. -/

/-- `d/dφ realRootPath` — named so the statements below stay readable. -/
noncomputable def realRootPath' (φ : ℝ) : ℝ :=
  (-(-2 * realRoot (Real.cos φ) ^ 2 + 2 * realRoot (Real.cos φ))
    / (3 * realRoot (Real.cos φ) ^ 2 - 4 * Real.cos φ * realRoot (Real.cos φ)
        + 2 * Real.cos φ + 1)) * (-Real.sin φ)

theorem hasDerivAt_realRootPath' (φ : ℝ) :
    HasDerivAt realRootPath (realRootPath' φ) φ := hasDerivAt_realRootPath φ

/-- The quadratic cofactor's coefficients along the arc: `Y² + βY + γ`. -/
noncomputable def pairBeta (φ : ℝ) : ℝ := realRootPath φ - 2 * Real.cos φ

noncomputable def pairGamma (φ : ℝ) : ℝ :=
  realRootPath φ ^ 2 - 2 * Real.cos φ * realRootPath φ + 2 * Real.cos φ + 1

theorem hasDerivAt_pairBeta (φ : ℝ) :
    HasDerivAt pairBeta (realRootPath' φ + 2 * Real.sin φ) φ := by
  have h := (hasDerivAt_realRootPath' φ).sub
    ((Real.hasDerivAt_cos φ).const_mul (2 : ℝ))
  unfold pairBeta
  convert h using 1
  ring

theorem hasDerivAt_pairGamma (φ : ℝ) :
    HasDerivAt pairGamma
      (2 * realRootPath φ * realRootPath' φ
        - (2 * (-Real.sin φ) * realRootPath φ + 2 * Real.cos φ * realRootPath' φ)
        + 2 * (-Real.sin φ)) φ := by
  have h := ((((hasDerivAt_realRootPath' φ).pow 2).sub
      (((Real.hasDerivAt_cos φ).const_mul (2 : ℝ)).mul (hasDerivAt_realRootPath' φ))).add
      ((Real.hasDerivAt_cos φ).const_mul (2 : ℝ))).add_const 1
  unfold pairGamma
  convert h using 1
  ring

/-- The pair's discriminant along the arc. Its sign flips exactly at the
collision `φ₀` (Route 36 G5), so both branches of `otherRoots` are live. -/
noncomputable def pairDisc (φ : ℝ) : ℝ := pairBeta φ ^ 2 - 4 * pairGamma φ

theorem continuous_pairBeta : Continuous pairBeta :=
  continuous_iff_continuousAt.mpr fun φ => (hasDerivAt_pairBeta φ).continuousAt

theorem continuous_pairGamma : Continuous pairGamma :=
  continuous_iff_continuousAt.mpr fun φ => (hasDerivAt_pairGamma φ).continuousAt

theorem continuous_pairDisc : Continuous pairDisc :=
  (continuous_pairBeta.pow 2).sub (continuous_const.mul continuous_pairGamma)

/-- The colliding pair, as a function of `φ`. -/
noncomputable def Ypair (φ : ℝ) : ℂ × ℂ := otherRoots (pairBeta φ) (pairGamma φ)

/-- **The pair is continuous on the whole arc, collision included.**

`continuous_otherRoots` is continuous *through* the branch collision — at
`β² = 4γ` both of its branches give `(−β/2, −β/2)` — and the coefficients are
continuous because `realRootPath` is. So `envelopeS`'s continuity hypothesis on
`Icc 0 π` is available with no exceptional point; only the *derivative* needs one,
and `envelopeS_total` is built to tolerate exactly that asymmetry. -/
theorem continuous_Ypair : Continuous Ypair := by
  have ht : Continuous realRootPath := continuous_realRootPath
  have hcos : Continuous fun φ : ℝ => 2 * Real.cos φ :=
    continuous_const.mul Real.continuous_cos
  have h1 : Continuous fun φ : ℝ => realRootPath φ - 2 * Real.cos φ := ht.sub hcos
  have h2 : Continuous fun φ : ℝ =>
      realRootPath φ ^ 2 - 2 * Real.cos φ * realRootPath φ + 2 * Real.cos φ + 1 :=
    (((ht.pow 2).sub (hcos.mul ht)).add hcos).add continuous_const
  exact continuous_otherRoots.comp (h1.prodMk h2)

/-! ### 5b. Differentiating the pair, off the collision

`otherRoots` splits on the sign of `β² − 4γ`, and Route 36 G5 shows that sign
genuinely flips on the arc — at `φ₀`, where the discriminant vanishes. So each
branch has to be differentiated separately, under a hypothesis pinning which one
is active. The hypothesis is not decoration: at `φ₀` the pair is *not*
differentiable, which is precisely the exceptional point `envelopeS_total` allows.

This section does the branch where the pair is genuinely complex (`β² < 4γ`),
which Route 36 G5 measures as 153 of the 199 arc points. -/

/-- `4γ − β²`, positive exactly where the pair is genuinely complex. -/
noncomputable def pairNegDisc (φ : ℝ) : ℝ := 4 * pairGamma φ - pairBeta φ ^ 2

/-- `d/dφ` of the above, named to keep the statements readable. -/
noncomputable def pairNegDisc' (φ : ℝ) : ℝ :=
  4 * (2 * realRootPath φ * realRootPath' φ
      - (2 * (-Real.sin φ) * realRootPath φ + 2 * Real.cos φ * realRootPath' φ)
      + 2 * (-Real.sin φ))
    - 2 * pairBeta φ * (realRootPath' φ + 2 * Real.sin φ)

theorem hasDerivAt_pairNegDisc (φ : ℝ) :
    HasDerivAt pairNegDisc (pairNegDisc' φ) φ := by
  have h := ((hasDerivAt_pairGamma φ).const_mul (4 : ℝ)).sub ((hasDerivAt_pairBeta φ).pow 2)
  unfold pairNegDisc pairNegDisc'
  convert h using 1
  ring

/-- The imaginary half-width of the complex pair. -/
noncomputable def pairIm (φ : ℝ) : ℝ := Real.sqrt (pairNegDisc φ) / 2

/-- Differentiable exactly where the pair has not collided — `√` is the only
thing in the way, and `pairNegDisc φ > 0` is what clears it. -/
theorem hasDerivAt_pairIm {φ : ℝ} (h : 0 < pairNegDisc φ) :
    HasDerivAt pairIm
      (pairNegDisc' φ / (2 * Real.sqrt (pairNegDisc φ)) / 2) φ :=
  ((hasDerivAt_pairNegDisc φ).sqrt (ne_of_gt h)).div_const 2

/-- **The complex branch, identified.** `pairDisc φ < 0` selects `otherRoots`'
second case. -/
theorem Ypair_of_disc_neg {φ : ℝ} (h : pairDisc φ < 0) :
    Ypair φ = (((-pairBeta φ / 2 : ℝ) : ℂ) + ((pairIm φ : ℝ) : ℂ) * Complex.I,
               ((-pairBeta φ / 2 : ℝ) : ℂ) - ((pairIm φ : ℝ) : ℂ) * Complex.I) := by
  have hlt : ¬ (0 ≤ pairBeta φ ^ 2 - 4 * pairGamma φ) := by
    unfold pairDisc at h; linarith
  unfold Ypair otherRoots
  rw [if_neg hlt]
  unfold pairIm pairNegDisc
  norm_num

/-- `pairDisc < 0` on a whole neighbourhood — needed because `HasDerivAt` is a
statement about the function *near* `φ`, not at it. -/
theorem eventually_disc_neg {φ : ℝ} (h : pairDisc φ < 0) :
    ∀ᶠ u in 𝓝 φ, pairDisc u < 0 :=
  continuous_pairDisc.continuousAt (Iio_mem_nhds h)

theorem pairNegDisc_eq_neg (φ : ℝ) : pairNegDisc φ = -pairDisc φ := by
  unfold pairNegDisc pairDisc; ring

/-- **`Y₂` is differentiable wherever the pair has not collided.**

The hypothesis `pairDisc φ < 0` is doing two separate jobs, and both are needed:
it selects `otherRoots`' complex branch, and it keeps `√` away from `0`. At `φ₀`
both fail at once — which is exactly why `φ₀` is the exceptional point
`envelopeS_total` is built to tolerate, rather than an artefact of this proof. -/
theorem hasDerivAt_Ypair_fst {φ : ℝ} (h : pairDisc φ < 0) :
    HasDerivAt (fun u => (Ypair u).1)
      (((-(realRootPath' φ + 2 * Real.sin φ) / 2 : ℝ) : ℂ)
        + ((pairNegDisc' φ / (2 * Real.sqrt (pairNegDisc φ)) / 2 : ℝ) : ℂ) * Complex.I) φ := by
  have hneg : 0 < pairNegDisc φ := by rw [pairNegDisc_eq_neg]; linarith
  have hb : HasDerivAt (fun u : ℝ => ((-pairBeta u / 2 : ℝ) : ℂ))
      (((-(realRootPath' φ + 2 * Real.sin φ) / 2 : ℝ) : ℂ)) φ :=
    Complex.ofRealCLM.hasFDerivAt.comp_hasDerivAt φ
      ((hasDerivAt_pairBeta φ).neg.div_const 2)
  have hi : HasDerivAt (fun u : ℝ => ((pairIm u : ℝ) : ℂ) * Complex.I)
      (((pairNegDisc' φ / (2 * Real.sqrt (pairNegDisc φ)) / 2 : ℝ) : ℂ) * Complex.I) φ :=
    (Complex.ofRealCLM.hasFDerivAt.comp_hasDerivAt φ (hasDerivAt_pairIm hneg)).mul_const _
  have heq : (fun u : ℝ => (Ypair u).1) =ᶠ[𝓝 φ]
      fun u : ℝ => ((-pairBeta u / 2 : ℝ) : ℂ) + ((pairIm u : ℝ) : ℂ) * Complex.I := by
    filter_upwards [eventually_disc_neg h] with u hu
    rw [Ypair_of_disc_neg hu]
  exact (hb.add hi).congr_of_eventuallyEq heq

/-! ### 4c. The **real**-pair regime, past the collision

`hasDerivAt_Ypair_fst`/`_snd` carry `pairDisc φ < 0` and so cover only
`Ioo 0 φ₀`. Past `φ₀ = 137.9206708879635°` the pair is genuinely **real**
(Route 36 G5: all three roots real at 46 of 199 arc points) and `otherRoots` is
in its `√d` branch.

⚠ This gap was invisible until the transport was assembled. Every statement about
the pair had `pairDisc φ < 0` written into it, so it never surfaced as a *missing
hypothesis* — it surfaced as a theorem silently covering part of the arc. The
proof is the mirror of the complex branch: `√` is differentiable away from `0`,
and here it is `pairDisc φ > 0` that keeps it away. -/

theorem eventually_disc_pos {φ : ℝ} (h : 0 < pairDisc φ) :
    ∀ᶠ u in 𝓝 φ, 0 < pairDisc u :=
  continuous_pairDisc.continuousAt (Ioi_mem_nhds h)

theorem hasDerivAt_pairDisc (φ : ℝ) : HasDerivAt pairDisc (-pairNegDisc' φ) φ := by
  have hfun : pairDisc = -pairNegDisc := by
    funext u
    simp only [Pi.neg_apply, pairNegDisc_eq_neg, neg_neg]
  rw [hfun]
  exact (hasDerivAt_pairNegDisc φ).neg

theorem Ypair_of_disc_pos {φ : ℝ} (h : 0 ≤ pairDisc φ) :
    Ypair φ = ((((-pairBeta φ + Real.sqrt (pairDisc φ)) / 2 : ℝ) : ℂ),
               (((-pairBeta φ - Real.sqrt (pairDisc φ)) / 2 : ℝ) : ℂ)) := by
  have hle : 0 ≤ pairBeta φ ^ 2 - 4 * pairGamma φ := by unfold pairDisc at h; linarith
  unfold Ypair otherRoots
  rw [if_pos hle]
  unfold pairDisc
  norm_num

/-- **`Y₂` on the real branch.** -/
theorem hasDerivAt_Ypair_fst_real {φ : ℝ} (h : 0 < pairDisc φ) :
    HasDerivAt (fun u => (Ypair u).1)
      ((((-(realRootPath' φ + 2 * Real.sin φ)
          + -pairNegDisc' φ / (2 * Real.sqrt (pairDisc φ))) / 2 : ℝ) : ℂ)) φ := by
  have hr : HasDerivAt (fun u : ℝ => (-pairBeta u + Real.sqrt (pairDisc u)) / 2)
      ((-(realRootPath' φ + 2 * Real.sin φ)
        + -pairNegDisc' φ / (2 * Real.sqrt (pairDisc φ))) / 2) φ :=
    (((hasDerivAt_pairBeta φ).neg).add
      ((hasDerivAt_pairDisc φ).sqrt (ne_of_gt h))).div_const 2
  have hb : HasDerivAt (fun u : ℝ => (((-pairBeta u + Real.sqrt (pairDisc u)) / 2 : ℝ) : ℂ))
      ((((-(realRootPath' φ + 2 * Real.sin φ)
        + -pairNegDisc' φ / (2 * Real.sqrt (pairDisc φ))) / 2 : ℝ) : ℂ)) φ :=
    Complex.ofRealCLM.hasFDerivAt.comp_hasDerivAt φ hr
  refine hb.congr_of_eventuallyEq ?_
  filter_upwards [eventually_disc_pos h] with u hu
  rw [Ypair_of_disc_pos hu.le]

/-- **`Y₃` on the real branch.** -/
theorem hasDerivAt_Ypair_snd_real {φ : ℝ} (h : 0 < pairDisc φ) :
    HasDerivAt (fun u => (Ypair u).2)
      ((((-(realRootPath' φ + 2 * Real.sin φ)
          - -pairNegDisc' φ / (2 * Real.sqrt (pairDisc φ))) / 2 : ℝ) : ℂ)) φ := by
  have hr : HasDerivAt (fun u : ℝ => (-pairBeta u - Real.sqrt (pairDisc u)) / 2)
      ((-(realRootPath' φ + 2 * Real.sin φ)
        - -pairNegDisc' φ / (2 * Real.sqrt (pairDisc φ))) / 2) φ :=
    (((hasDerivAt_pairBeta φ).neg).sub
      ((hasDerivAt_pairDisc φ).sqrt (ne_of_gt h))).div_const 2
  have hb : HasDerivAt (fun u : ℝ => (((-pairBeta u - Real.sqrt (pairDisc u)) / 2 : ℝ) : ℂ))
      ((((-(realRootPath' φ + 2 * Real.sin φ)
        - -pairNegDisc' φ / (2 * Real.sqrt (pairDisc φ))) / 2 : ℝ) : ℂ)) φ :=
    Complex.ofRealCLM.hasFDerivAt.comp_hasDerivAt φ hr
  refine hb.congr_of_eventuallyEq ?_
  filter_upwards [eventually_disc_pos h] with u hu
  rw [Ypair_of_disc_pos hu.le]

/-! ### 5a'. Vieta for the concrete labelling

`logSumA_eq_log` and `logSumB_eq_neg_log` — the `hA`/`hB` inputs to
`hasDerivAt_envelopeS` — take the three symmetric functions as hypotheses, in the
`x`-cleared form `x·e₁ = x²+1`, `x·e₂ = x²+x+1`, `e₃ = 1`. All three are
available here, and the first two reduce to the *same* fact: `2·(Re x)·x = x²+1`,
which is `unitCircle_quadratic`. The third is `gamma_rel`. -/

theorem Ypair_sum (φ : ℝ) : (Ypair φ).1 + (Ypair φ).2 = -((pairBeta φ : ℝ) : ℂ) :=
  otherRoots_sum _ _

theorem Ypair_prod (φ : ℝ) : (Ypair φ).1 * (Ypair φ).2 = ((pairGamma φ : ℝ) : ℂ) :=
  otherRoots_prod _ _

/-- `e₁ = t + y₂ + y₃ = 2c`. -/
theorem vieta_e1 (φ : ℝ) :
    ((realRootPath φ : ℝ) : ℂ) + (Ypair φ).1 + (Ypair φ).2
      = 2 * ((Real.cos φ : ℝ) : ℂ) := by
  have h := Ypair_sum φ
  unfold pairBeta at h
  push_cast [-Complex.ofReal_cos] at h ⊢
  linear_combination h

/-- `e₂ = t·y₂ + t·y₃ + y₂y₃ = 2c + 1`. -/
theorem vieta_e2 (φ : ℝ) :
    ((realRootPath φ : ℝ) : ℂ) * (Ypair φ).1 + ((realRootPath φ : ℝ) : ℂ) * (Ypair φ).2
      + (Ypair φ).1 * (Ypair φ).2 = 2 * ((Real.cos φ : ℝ) : ℂ) + 1 := by
  have hs := Ypair_sum φ
  have hp := Ypair_prod φ
  unfold pairBeta at hs
  unfold pairGamma at hp
  push_cast [-Complex.ofReal_cos] at hs hp ⊢
  linear_combination ((realRootPath φ : ℝ) : ℂ) * hs + hp

/-- `e₃ = t·y₂·y₃ = 1` — this is `gamma_rel`, and it is the one with content. -/
theorem vieta_e3 (φ : ℝ) :
    ((realRootPath φ : ℝ) : ℂ) * (Ypair φ).1 * (Ypair φ).2 = 1 := by
  have hp := Ypair_prod φ
  have hγ : (realRootPath φ : ℝ) * pairGamma φ = 1 := by
    have := gamma_rel (unitCubic_realRootPath φ)
    unfold pairGamma
    linear_combination this
  have hγc : ((realRootPath φ : ℝ) : ℂ) * ((pairGamma φ : ℝ) : ℂ) = 1 := by
    exact_mod_cast congrArg (fun r : ℝ => (r : ℂ)) hγ
  rw [mul_assoc, hp]
  exact hγc

/-- **`hv₁` in the form `logSumA_eq_log` wants it.** Both this and `hv₂` collapse
to `unitCircle_quadratic`; the labelling contributes only `e₁ = 2c`. -/
theorem vieta_hv1 {x : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) {φ : ℝ}
    (hre : x.re = Real.cos φ) :
    x * (((realRootPath φ : ℝ) : ℂ) + (Ypair φ).1 + (Ypair φ).2) = x ^ 2 + 1 := by
  rw [vieta_e1 φ, ← hre]
  linear_combination unitCircle_quadratic hx

/-- **`hv₂`.** -/
theorem vieta_hv2 {x : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) {φ : ℝ}
    (hre : x.re = Real.cos φ) :
    x * (((realRootPath φ : ℝ) : ℂ) * (Ypair φ).1 + ((realRootPath φ : ℝ) : ℂ) * (Ypair φ).2
      + (Ypair φ).1 * (Ypair φ).2) = x ^ 2 + x + 1 := by
  rw [vieta_e2 φ, ← hre]
  linear_combination unitCircle_quadratic hx

/-! ### 5b'. Toward `heⱼ` at the pair — the first tight bound

Route 36 G13. `heⱼ` for the pair needs `k = 0` in `dVdy·y ∈ 2πi·ℤ`
(`exists_int_dVdy_mul`), because `Re(dVdy·Y′) = k·2π·Im(Y′/y)`. The real root
does **not** need it — there `dVdy` is purely imaginary and `Y′` is real, which
is `re_dVdy_mul_eq_zero_of_real`.

The pinning quantity is

    S = arg(1−y) + [arg(1−xy) + arg(1−y/x) − 2·arg(−y)] = 2πk

and `k = 0` follows from `|S| < 2π`. **Bounding the four terms separately does
not work** — G13 measures their ranges as `1.4076 + 3.1133 + 3.1133 + 2·2.1115 =
11.857 > 2π`. That route is closed; the correlations are what carry it.

Two *groupings* are tight instead, each measured under `π/2`, and their bounds
sum to `2.8152 < 2π`. This section proves the first, which is the elementary one:
`|arg(1−y)| < π/2` iff `Re(1−y) > 0` iff `Re y < 1`, and at the pair
`Re y = cos φ − t/2` with `cos φ ≤ 1` and `t > 0`. The second grouping remains
open. -/

/-- At the pair, `Re y = cos φ − t/2` — both members share it, being conjugates. -/
theorem re_Ypair_eq {φ : ℝ} (h : pairDisc φ < 0) :
    ((Ypair φ).1).re = Real.cos φ - realRootPath φ / 2 ∧
    ((Ypair φ).2).re = Real.cos φ - realRootPath φ / 2 := by
  rw [Ypair_of_disc_neg h]
  unfold pairBeta
  constructor <;> · simp [Complex.cos_ofReal_re]; ring

/-- **`Re y < 1` at the pair.** `cos φ ≤ 1` and `t > 0`; nothing else is needed. -/
theorem re_Ypair_lt_one {φ : ℝ} (h : pairDisc φ < 0) :
    ((Ypair φ).1).re < 1 ∧ ((Ypair φ).2).re < 1 := by
  obtain ⟨h1, h2⟩ := re_Ypair_eq h
  have hc : Real.cos φ ≤ 1 := Real.cos_le_one φ
  have ht : 0 < realRootPath φ := realRootPath_pos φ
  exact ⟨by rw [h1]; linarith, by rw [h2]; linarith⟩

/-- **`1 − y` is off `log`'s cut at the pair**, which is `|arg(1−y)| < π/2` — the
first of G13's two tight groupings, and the one that is elementary. -/
theorem one_sub_Ypair_mem_slitPlane {φ : ℝ} (h : pairDisc φ < 0) :
    (1 - (Ypair φ).1) ∈ Complex.slitPlane ∧ (1 - (Ypair φ).2) ∈ Complex.slitPlane := by
  obtain ⟨h1, h2⟩ := re_Ypair_lt_one h
  refine ⟨Or.inl ?_, Or.inl ?_⟩ <;> simp <;> linarith

/-! ### 5b''. The four sign facts `hA`/`hB` need

`logSumA_eq_log` wants `(x·y₃).im ≤ 0` and `π/2 < φ → (x·y₂).im ≤ 0`;
`logSumB_eq_neg_log` wants `0 < (y₂/x).im` and `π/2 < φ → 0 < (y₃/x).im`.

The first pair is `im_mul_otherRoots_snd_neg` / `_fst_neg` verbatim — the
labelling's `pairBeta`/`pairGamma` *are* those theorems' `β`/`γ`.

The second pair needs no new work either, and that is the point of stating it
here: on `|x| = 1` and for a **conjugate** pair,

    Im(y/x) = −Im(x·conj y),

so `0 < Im(y₂/x)` is `Im(x·y₃) < 0` — the same two facts read through the
conjugation. Route 36 G12's `pairDisc φ < 0` is what makes the pair conjugate. -/

/-- The pair are complex conjugates off the collision. -/
theorem Ypair_conj {φ : ℝ} (h : pairDisc φ < 0) :
    (starRingEnd ℂ) (Ypair φ).1 = (Ypair φ).2 := by
  rw [Ypair_of_disc_neg h]
  simp only [map_add, map_mul, Complex.conj_ofReal, Complex.conj_I]
  ring

/-- `Im(y/x) = −Im(x·conj y)` on the unit circle. -/
theorem im_div_eq_neg_im_mul_conj {x y : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) :
    (y / x).im = -(x * (starRingEnd ℂ) y).im := by
  have hns : Complex.normSq x = 1 := by rw [Complex.normSq_apply]; nlinarith
  simp only [Complex.div_im, Complex.mul_im, Complex.conj_re, Complex.conj_im, hns, div_one]
  ring

theorem im_mul_Ypair_snd_neg {φ : ℝ} {x : ℂ} (hre : x.re = Real.cos φ) (hxim : 0 < x.im)
    (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) : (x * (Ypair φ).2).im < 0 :=
  im_mul_otherRoots_snd_neg (Real.cos_le_one φ) (realRootPath_pos φ)
    (realRootPath_lt_one φ) (unitCubic_realRootPath φ) hre hxim hxnorm

theorem im_mul_Ypair_fst_neg {φ : ℝ} (hcneg : Real.cos φ < 0) {x : ℂ}
    (hre : x.re = Real.cos φ) (hxim : 0 < x.im)
    (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) : (x * (Ypair φ).1).im < 0 :=
  im_mul_otherRoots_fst_neg (Real.cos_le_one φ) hcneg (realRootPath_pos φ)
    (realRootPath_lt_one φ) (unitCubic_realRootPath φ) hre hxim hxnorm

/-- **`logSumB`'s first sign fact**, from `logSumA`'s second via conjugation. -/
theorem im_div_Ypair_fst_pos {φ : ℝ} (hd : pairDisc φ < 0) {x : ℂ}
    (hre : x.re = Real.cos φ) (hxim : 0 < x.im)
    (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) : 0 < ((Ypair φ).1 / x).im := by
  rw [im_div_eq_neg_im_mul_conj hxnorm, Ypair_conj hd]
  exact neg_pos.mpr (im_mul_Ypair_snd_neg hre hxim hxnorm)

/-- **`logSumB`'s second sign fact**, likewise. -/
theorem im_div_Ypair_snd_pos {φ : ℝ} (hd : pairDisc φ < 0) (hcneg : Real.cos φ < 0)
    {x : ℂ} (hre : x.re = Real.cos φ) (hxim : 0 < x.im)
    (hxnorm : x.re ^ 2 + x.im ^ 2 = 1) : 0 < ((Ypair φ).2 / x).im := by
  have hconj : (starRingEnd ℂ) (Ypair φ).2 = (Ypair φ).1 := by
    rw [← Ypair_conj hd]; simp
  rw [im_div_eq_neg_im_mul_conj hxnorm, hconj]
  exact neg_pos.mpr (im_mul_Ypair_fst_neg hcneg hre hxim hxnorm)

/-! ### 5c. The branches solve the CURVE, not merely `unitCubic`

Everything downstream — `vSide_of_root`, `hasDerivAt_envelopeS` — is stated for
`curve x y = 0`. On `|x| = 1` that is `x · unitCubic (Re x) y`
(`curve_eq_unitCubic`), so each conversion is one rewrite. It still has to be
made: a labelling that solves the real cubic but not the curve would satisfy
every statement in §1–5b and none downstream, and would typecheck the whole way. -/

/-- **`Y₁` is a root of the curve.** -/
theorem curve_Yreal {x : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) {φ : ℝ}
    (hre : x.re = Real.cos φ) : curve x (Yreal φ) = 0 := by
  have hz : Yreal φ ^ 3 - 2 * ((x.re : ℝ) : ℂ) * Yreal φ ^ 2
      + (2 * ((x.re : ℝ) : ℂ) + 1) * Yreal φ - 1 = 0 := by
    rw [hre]
    have h := unitCubic_realRootPath φ
    unfold unitCubic at h
    have hc : ((realRootPath φ ^ 3 - 2 * Real.cos φ * realRootPath φ ^ 2
        + (2 * Real.cos φ + 1) * realRootPath φ - 1 : ℝ) : ℂ) = 0 := by
      rw [h]; norm_num
    unfold Yreal
    push_cast [-Complex.ofReal_cos] at hc
    linear_combination hc
  unfold curve
  rw [curve_eq_unitCubic hx (Yreal φ), hz, mul_zero]

/-- **The quadratic cofactor vanishes at both members of the pair** — Vieta,
via `otherRoots_factor`. -/
theorem pair_quadratic_zero (φ : ℝ) :
    (Ypair φ).1 ^ 2 + (pairBeta φ : ℂ) * (Ypair φ).1 + (pairGamma φ : ℂ) = 0 ∧
    (Ypair φ).2 ^ 2 + (pairBeta φ : ℂ) * (Ypair φ).2 + (pairGamma φ : ℂ) = 0 := by
  constructor <;>
    · rw [otherRoots_factor (pairBeta φ) (pairGamma φ)]
      unfold Ypair
      ring

/-- **`Y₂` and `Y₃` are roots of the curve.**

`unitCubic c Y = (Y − t)(Y² + βY + γ)` with `β = t − 2c`, `γ = t² − 2ct + 2c + 1`
— an identity whose constant term needs `gamma_rel`, `t·γ = 1`. So a root of the
cofactor is a root of the cubic, hence of the curve. -/
theorem curve_Ypair {x : ℂ} (hx : x.re ^ 2 + x.im ^ 2 = 1) {φ : ℝ}
    (hre : x.re = Real.cos φ) :
    curve x (Ypair φ).1 = 0 ∧ curve x (Ypair φ).2 = 0 := by
  have hγ : (realRootPath φ : ℝ) * (pairGamma φ) = 1 := by
    have := gamma_rel (unitCubic_realRootPath φ)
    unfold pairGamma
    linear_combination this
  have key : ∀ Y : ℂ, Y ^ 2 + (pairBeta φ : ℂ) * Y + (pairGamma φ : ℂ) = 0 →
      Y ^ 3 - 2 * ((x.re : ℝ) : ℂ) * Y ^ 2 + (2 * ((x.re : ℝ) : ℂ) + 1) * Y - 1 = 0 := by
    intro Y hY
    have hγc : ((realRootPath φ : ℝ) : ℂ) * ((pairGamma φ : ℝ) : ℂ) = 1 := by
      exact_mod_cast congrArg (fun r : ℝ => (r : ℂ)) hγ
    rw [hre]
    unfold pairBeta pairGamma at hY hγc
    push_cast [-Complex.ofReal_cos] at hY hγc ⊢
    linear_combination (Y - ((realRootPath φ : ℝ) : ℂ)) * hY + hγc
  obtain ⟨h1, h2⟩ := pair_quadratic_zero φ
  constructor
  · unfold curve; rw [curve_eq_unitCubic hx _, key _ h1, mul_zero]
  · unfold curve; rw [curve_eq_unitCubic hx _, key _ h2, mul_zero]

/-- **`Y₃`, the conjugate branch.** Same hypothesis, opposite sign on the
imaginary part. -/
theorem hasDerivAt_Ypair_snd {φ : ℝ} (h : pairDisc φ < 0) :
    HasDerivAt (fun u => (Ypair u).2)
      (((-(realRootPath' φ + 2 * Real.sin φ) / 2 : ℝ) : ℂ)
        - ((pairNegDisc' φ / (2 * Real.sqrt (pairNegDisc φ)) / 2 : ℝ) : ℂ) * Complex.I) φ := by
  have hneg : 0 < pairNegDisc φ := by rw [pairNegDisc_eq_neg]; linarith
  have hb : HasDerivAt (fun u : ℝ => ((-pairBeta u / 2 : ℝ) : ℂ))
      (((-(realRootPath' φ + 2 * Real.sin φ) / 2 : ℝ) : ℂ)) φ :=
    Complex.ofRealCLM.hasFDerivAt.comp_hasDerivAt φ
      ((hasDerivAt_pairBeta φ).neg.div_const 2)
  have hi : HasDerivAt (fun u : ℝ => ((pairIm u : ℝ) : ℂ) * Complex.I)
      (((pairNegDisc' φ / (2 * Real.sqrt (pairNegDisc φ)) / 2 : ℝ) : ℂ) * Complex.I) φ :=
    (Complex.ofRealCLM.hasFDerivAt.comp_hasDerivAt φ (hasDerivAt_pairIm hneg)).mul_const _
  have heq : (fun u : ℝ => (Ypair u).2) =ᶠ[𝓝 φ]
      fun u : ℝ => ((-pairBeta u / 2 : ℝ) : ℂ) - ((pairIm u : ℝ) : ℂ) * Complex.I := by
    filter_upwards [eventually_disc_neg h] with u hu
    rw [Ypair_of_disc_neg hu]
  exact (hb.sub hi).congr_of_eventuallyEq heq


end QOU.QBeta.FiveTwoDeformedSaddle
