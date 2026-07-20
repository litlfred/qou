import Mathlib.Analysis.Meromorphic.Divisor
import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Analysis.Calculus.LogDeriv
import Mathlib.Analysis.Calculus.Deriv.Shift
import Mathlib.Analysis.Complex.Basic
import Mathlib.Algebra.Ring.Periodic
import Mathlib.LinearAlgebra.LinearIndependent.Defs
import Mathlib.Data.Fin.VecNotation
import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

/-!
# The elliptic divisor-degree theorem — scaffold (PI-2, bean `qou-toqt`)

For a **nonconstant elliptic function** `f` (doubly-periodic meromorphic on `ℂ`,
with `ℝ`-independent periods `ω₁, ω₂`), the sum of the local orders over one
fundamental parallelogram is **zero**:

$$\sum_{p \in P} \operatorname{ord}_p f \;=\; 0
  \qquad\Longleftrightarrow\qquad \#\{\text{zeros}\} = \#\{\text{poles}\}
  \text{ (with multiplicity).}$$

This is **Liouville's third theorem** (the "degree-zero" theorem). It is the
missing analytic input in the `PentagonRigidity` Φ₁/Φ₂-entire leg
(`docs/audits/2026-07-20-pentagon-entire-leg.md`): the difference equations make
the divisor of the ratio `Ψ/Φ` doubly-periodic
(`QOU.QBeta.MeromorphicSameOrder.meromorphicOrderAt_orderDiff_periodic`), but
degree-zero + a sign input is what forces that periodic divisor to vanish
identically, killing the elliptic-freedom obstruction.

## What is proved here (sorry-free) vs. open

**Proved now (elementary bricks, Mathlib-only cone):**

* `periodic_deriv` / `periodic_logDeriv` — the derivative and **logarithmic
  derivative `f'/f` of a periodic function are periodic**. This is the
  *boundary-integral cancellation* ingredient: on opposite edges of the
  parallelogram (which differ by a period) the integrand `logDeriv f` agrees,
  while the orientations oppose, so the two edge contributions cancel.
* `isElliptic_logDeriv` — the logarithmic derivative of an elliptic function is
  itself elliptic (periodic under **both** `ω₁` and `ω₂`).
* `meromorphicOrderAt_translate` / `divisor_translate` — **the divisor is
  lattice-periodic**: `ord_p f` and hence `(divisor f).p` are invariant under
  each period, so the divisor is determined by its restriction to one cell. (The
  translation brick `meromorphicOrderAt_comp_add` is reproved locally, namespaced,
  to keep this file's dependency cone Mathlib-only and `lean`-direct verifiable;
  the un-namespaced original lives in `QOU.QBeta.MeromorphicSameOrder`.)

* `paraBoundaryLogDeriv` / `paraBoundaryLogDeriv_eq_zero` — **the boundary
  integral `∮_{∂P} logDeriv f` and its vanishing, now PROVED sorry-free**
  (2026-07-20). The four-edge parallelogram contour of `f'/f` is `0` for elliptic
  `f`: opposite edges cancel via `intervalIntegral` change-of-variables + the
  `periodic_logDeriv` established above. This is the *analysis-free* half of the
  classical `Σ ord = (1/2πi)∮_{∂P} f'/f = 0` argument.

**Now DERIVED sorry-free (modulo the single gap `parallelogram_argument_principle`):**

* `elliptic_divisor_degree_zero` — the degree-zero theorem itself, now **derived
  sorry-free** by composing the proved boundary-vanishing `∮_{∂P} logDeriv f = 0`
  with the identity `2πi · Σ ord = ∮_{∂P} logDeriv f` and cancelling the nonzero
  `2πi`. The `sorry` no longer lives in this theorem.

**Stated open (the single remaining analytic core — a genuine Mathlib gap):**

* `parallelogram_argument_principle` — the argument principle over a *parallelogram
  contour*: `2πi · Σ ord = ∮_{∂P} logDeriv f`. Mathlib v4.24.0 has Liouville,
  `meromorphicOrderAt`, `MeromorphicOn.divisor`, `Complex.CauchyIntegral`,
  `circleIntegral`, and the rectangle *vanishing*
  `integral_boundary_rect_eq_zero_of_differentiable_on_off_countable`, but **no
  rectangle-contour residue sum** and no elliptic-function theory. This gap is a
  *sibling* of the circle argument principle's
  `QOU.Mathlib.ArgumentPrinciple.contour_deformation_sum` /
  `residue_theorem_deformation` — the same multiply-connected Cauchy topology, but
  a **distinct** Lean statement (rectangle vs circle contour), so the circle
  `argument_principle` is not reusable verbatim. Carried as one cited `sorry`.

This is honest scaffolding of a known gap: **not** vacuous `True`, **not**
axiomatized-as-proved. The boundary-cancellation half is fully discharged; only the
parallelogram-contour deformation remains.
See `docs/audits/2026-07-20-pi2-elliptic-divisor-scaffold.md`.

-- Ref: [manuscript] Liouville's third theorem (degree of an elliptic divisor is
--   zero); docs/audits/2026-07-20-pentagon-entire-leg.md (§"exact residual analytic fact").
-/

open Filter Topology Complex

namespace QOU.Mathlib.EllipticDivisorDegree

/-! ### Boundary-cancellation bricks: `f'/f` of a periodic function is periodic -/

/-- **The derivative of a periodic function is periodic.** If `f (·+c) = f`, then
`deriv f (·+c) = deriv f`. This is the pointwise statement that makes the two
horizontal (resp. vertical) edges of a fundamental parallelogram carry the same
`f'/f` integrand up to the period shift. -/
theorem periodic_deriv {f : ℂ → ℂ} {c : ℂ} (hf : Function.Periodic f c) :
    Function.Periodic (deriv f) c := by
  intro x
  have h1 : deriv (fun y => f (y + c)) x = deriv f (x + c) := deriv_comp_add_const f c x
  have h2 : (fun y => f (y + c)) = f := funext fun y => hf y
  rw [h2] at h1
  exact h1.symm

/-- **The logarithmic derivative `f'/f` of a periodic function is periodic.**
Since `logDeriv f = deriv f / f` and both `deriv f` and `f` are periodic, so is
their quotient. On the two edges of `∂P` that differ by the period `c`, the
`logDeriv f` integrand agrees; with opposite orientation the contributions cancel
— the boundary-integral cancellation that drives the degree-zero proof. -/
theorem periodic_logDeriv {f : ℂ → ℂ} {c : ℂ} (hf : Function.Periodic f c) :
    Function.Periodic (logDeriv f) c := by
  intro x
  simp only [logDeriv_apply]
  rw [periodic_deriv hf x, hf x]

/-! ### Elliptic functions and the fundamental parallelogram -/

/-- **An elliptic function**: meromorphic on all of `ℂ` and doubly periodic under
`ω₁, ω₂`. (`ℝ`-independence of the periods — so the lattice is genuinely
rank-2 — is carried as a separate hypothesis where needed, matching
`QOU.MathlibExt.DoublyPeriodicLiouville`.) -/
structure IsElliptic (f : ℂ → ℂ) (ω₁ ω₂ : ℂ) : Prop where
  /-- `f` is meromorphic on the whole plane. -/
  meromorphic : MeromorphicOn f Set.univ
  /-- `f` is periodic under the first period. -/
  periodic₁ : Function.Periodic f ω₁
  /-- `f` is periodic under the second period. -/
  periodic₂ : Function.Periodic f ω₂

/-- **The logarithmic derivative of an elliptic function is elliptic** (periodic
under both periods). This is *exactly* the reason the contour integral of
`logDeriv f` over `∂P` vanishes: opposite edges of the parallelogram are period
translates, so the elliptic (= doubly-periodic) integrand cancels. It is the
formalizable half of the `Σ ord = (1/2πi)∮ f'/f = 0` route. -/
theorem isElliptic_logDeriv {f : ℂ → ℂ} {ω₁ ω₂ : ℂ} (hf : IsElliptic f ω₁ ω₂) :
    Function.Periodic (logDeriv f) ω₁ ∧ Function.Periodic (logDeriv f) ω₂ :=
  ⟨periodic_logDeriv hf.periodic₁, periodic_logDeriv hf.periodic₂⟩

/-- **The half-open fundamental parallelogram** `{ s·ω₁ + t·ω₂ : s, t ∈ [0,1) }`
of the lattice `⟨ω₁, ω₂⟩`. A single such cell contains exactly one representative
of each lattice coset (the `Int.fract` reduction of
`QOU.MathlibExt.DoublyPeriodicLiouville.const_of_doublyPeriodic`), so summing a
lattice-periodic divisor over it is the "degree over a fundamental domain". -/
def fundamentalParallelogram (ω₁ ω₂ : ℂ) : Set ℂ :=
  {z | ∃ s t : ℝ, s ∈ Set.Ico (0 : ℝ) 1 ∧ t ∈ Set.Ico (0 : ℝ) 1 ∧ z = s • ω₁ + t • ω₂}

/-! ### The divisor is lattice-periodic (a provable structural brick)

`meromorphicOrderAt_comp_add` is the translation invariance of the meromorphic
order, reproved locally (namespaced) so this file needs only the Mathlib cone. -/

/-- Translation `z ↦ z + c` tends within punctured neighborhoods. -/
private theorem tendsto_add_right_nhdsWithin_ne (x c : ℂ) :
    Tendsto (fun z => z + c) (𝓝[≠] x) (𝓝[≠] (x + c)) := by
  rw [tendsto_nhdsWithin_iff]
  refine ⟨((continuous_id.add continuous_const).continuousAt).mono_left nhdsWithin_le_nhds, ?_⟩
  filter_upwards [self_mem_nhdsWithin] with z hz
  simp only [Set.mem_compl_iff, Set.mem_singleton_iff] at hz ⊢
  exact fun h => hz (add_right_cancel h)

/-- Meromorphy is preserved by the translation `z ↦ z + c`. -/
private theorem meromorphicAt_comp_add {g : ℂ → ℂ} {x c : ℂ}
    (hg : MeromorphicAt g (x + c)) : MeromorphicAt (fun z => g (z + c)) x := by
  obtain ⟨n, hn⟩ := hg
  refine ⟨n, ?_⟩
  have hshift : AnalyticAt ℂ (fun z : ℂ => z + c) x := by fun_prop
  have hcomp : AnalyticAt ℂ (fun z : ℂ => ((z + c) - (x + c)) ^ n • g (z + c)) x :=
    AnalyticAt.comp (g := fun w : ℂ => (w - (x + c)) ^ n • g w)
      (f := fun z : ℂ => z + c) hn hshift
  have hfun : (fun z : ℂ => (z - x) ^ n • g (z + c))
      = (fun z : ℂ => ((z + c) - (x + c)) ^ n • g (z + c)) := by
    funext z; congr 2; ring
  rw [hfun]
  exact hcomp

private theorem meromorphicAt_comp_add_iff {g : ℂ → ℂ} {x c : ℂ} :
    MeromorphicAt (fun z => g (z + c)) x ↔ MeromorphicAt g (x + c) := by
  constructor
  · intro hF
    have h := meromorphicAt_comp_add (g := fun z => g (z + c)) (x := x + c) (c := -c)
      (by simpa using hF)
    simpa using h
  · exact meromorphicAt_comp_add

/-- **Translation invariance of the meromorphic order** (local copy of
`QOU.QBeta.MeromorphicSameOrder.meromorphicOrderAt_comp_add`). -/
private theorem meromorphicOrderAt_comp_add (g : ℂ → ℂ) (x c : ℂ) :
    meromorphicOrderAt (fun z => g (z + c)) x = meromorphicOrderAt g (x + c) := by
  by_cases hg : MeromorphicAt g (x + c)
  · have hFm : MeromorphicAt (fun z => g (z + c)) x := meromorphicAt_comp_add hg
    rcases eq_or_ne (meromorphicOrderAt g (x + c)) ⊤ with htop | hfin
    · rw [htop, meromorphicOrderAt_eq_top_iff]
      rw [meromorphicOrderAt_eq_top_iff] at htop
      exact (tendsto_add_right_nhdsWithin_ne x c).eventually htop
    · obtain ⟨n, hn⟩ := WithTop.ne_top_iff_exists.mp hfin
      rw [← hn, meromorphicOrderAt_eq_int_iff hFm]
      obtain ⟨G, hGan, hGne, hGeq⟩ := (meromorphicOrderAt_eq_int_iff hg).mp hn.symm
      refine ⟨fun z => G (z + c), ?_, ?_, ?_⟩
      · exact AnalyticAt.comp (g := G) (f := fun z => z + c) hGan (by fun_prop)
      · exact hGne
      · have h2 := (tendsto_add_right_nhdsWithin_ne x c).eventually hGeq
        filter_upwards [h2] with z hz
        show g (z + c) = (z - x) ^ n • G (z + c)
        rw [hz]
        have hb : (z + c) - (x + c) = z - x := by ring
        rw [hb]
  · rw [meromorphicOrderAt_of_not_meromorphicAt (mt meromorphicAt_comp_add_iff.mp hg),
        meromorphicOrderAt_of_not_meromorphicAt hg]

/-- **The meromorphic order is invariant under a period.** If `f` is periodic
under `c`, then `ord_{z+c} f = ord_z f`. Hence the order — the local
zero/pole multiplicity — is a lattice-periodic function of the base point. -/
theorem meromorphicOrderAt_translate {f : ℂ → ℂ} {c : ℂ}
    (hf : Function.Periodic f c) (z : ℂ) :
    meromorphicOrderAt f (z + c) = meromorphicOrderAt f z := by
  have hfun : (fun w => f (w + c)) = f := funext fun w => hf w
  calc meromorphicOrderAt f (z + c)
      = meromorphicOrderAt (fun w => f (w + c)) z := (meromorphicOrderAt_comp_add f z c).symm
    _ = meromorphicOrderAt f z := by rw [hfun]

/-- **The divisor is lattice-periodic.** For `f` meromorphic on `ℂ` and periodic
under `c`, `(divisor f).(z+c) = (divisor f).z`. So `Σ_cell ord` over any one
fundamental parallelogram is the full "degree over a fundamental domain", and the
degree-zero theorem below is a statement about a single cell. -/
theorem divisor_translate {f : ℂ → ℂ} {c : ℂ}
    (hf : MeromorphicOn f Set.univ) (hper : Function.Periodic f c) (z : ℂ) :
    (MeromorphicOn.divisor f Set.univ) (z + c) = (MeromorphicOn.divisor f Set.univ) z := by
  rw [MeromorphicOn.divisor_apply hf (Set.mem_univ _),
      MeromorphicOn.divisor_apply hf (Set.mem_univ _),
      meromorphicOrderAt_translate hper z]

/-! ### The parallelogram boundary integral and its periodicity-cancellation

The classical proof of the degree-zero theorem is
`Σ_{p∈P} ord_p f = (1/2πi) ∮_{∂P} logDeriv f = 0`. The second equality — the
**boundary-integral cancellation** — is now proved sorry-free below
(`paraBoundaryLogDeriv_eq_zero`): it is *pure periodicity*, needing no analysis
beyond `periodic_logDeriv`. The first equality (the argument principle over a
parallelogram contour) is the single remaining gap, isolated as
`parallelogram_argument_principle`. -/

/-- **The contour integral of `logDeriv f` over the boundary `∂P` of the
fundamental parallelogram** anchored at corner `a`, traversed counterclockwise
`a → a+ω₁ → a+ω₁+ω₂ → a+ω₂ → a`. Each of the four edges is a real
`intervalIntegral` of `logDeriv f · (edge tangent)`; the two return edges carry the
`(1-t)` parametrization and the `-ω_i` tangent (opposite orientation). This is the
`∮_{∂P} f'/f` that the argument principle equates with `2πi · Σ ord`. -/
noncomputable def paraBoundaryLogDeriv (f : ℂ → ℂ) (a ω₁ ω₂ : ℂ) : ℂ :=
    (∫ t in (0:ℝ)..1, logDeriv f (a + (t:ℝ) • ω₁) * ω₁)
  + (∫ t in (0:ℝ)..1, logDeriv f (a + ω₁ + (t:ℝ) • ω₂) * ω₂)
  + (∫ t in (0:ℝ)..1, logDeriv f (a + ω₂ + ((1:ℝ) - t) • ω₁) * (-ω₁))
  + (∫ t in (0:ℝ)..1, logDeriv f (a + ((1:ℝ) - t) • ω₂) * (-ω₂))

/-- **The boundary integral vanishes — pure periodicity, sorry-free.** For an
elliptic `f`, `∮_{∂P} logDeriv f = 0`: the "top" edge (`←ω₁`) cancels the "bottom"
edge (`→ω₁`) after the substitution `s = 1-t` and the `ω₂`-periodicity of
`logDeriv f`, and the "left" edge (`←ω₂`) cancels the "right" edge (`→ω₂`) via
`ω₁`-periodicity. This is exactly the "opposite edges of a period-parallelogram
carry the same doubly-periodic integrand with opposite orientation" cancellation
(`isElliptic_logDeriv`), made fully rigorous with only `intervalIntegral`
change-of-variables + the proved `periodic_logDeriv`. No argument principle, no
residue theory. -/
theorem paraBoundaryLogDeriv_eq_zero {f : ℂ → ℂ} {ω₁ ω₂ : ℂ}
    (hf : IsElliptic f ω₁ ω₂) (a : ℂ) :
    paraBoundaryLogDeriv f a ω₁ ω₂ = 0 := by
  have hp1 : Function.Periodic (logDeriv f) ω₁ := periodic_logDeriv hf.periodic₁
  have hp2 : Function.Periodic (logDeriv f) ω₂ := periodic_logDeriv hf.periodic₂
  unfold paraBoundaryLogDeriv
  -- top edge (`←ω₁`) = −(bottom edge `→ω₁`), via `s = 1-t` + `ω₂`-periodicity.
  have he3 : (∫ t in (0:ℝ)..1, logDeriv f (a + ω₂ + ((1:ℝ) - t) • ω₁) * (-ω₁))
      = -(∫ t in (0:ℝ)..1, logDeriv f (a + (t:ℝ) • ω₁) * ω₁) := by
    rw [intervalIntegral.integral_comp_sub_left
          (fun s : ℝ => logDeriv f (a + ω₂ + s • ω₁) * (-ω₁)) 1]
    simp only [sub_self, sub_zero]
    rw [← intervalIntegral.integral_neg]
    apply intervalIntegral.integral_congr
    intro s _
    simp only [mul_neg]
    congr 2
    rw [show a + ω₂ + s • ω₁ = (a + s • ω₁) + ω₂ by ring]
    exact hp2 (a + s • ω₁)
  -- left edge (`←ω₂`) = −(right edge `→ω₂`), via `s = 1-t` + `ω₁`-periodicity.
  have he4 : (∫ t in (0:ℝ)..1, logDeriv f (a + ((1:ℝ) - t) • ω₂) * (-ω₂))
      = -(∫ t in (0:ℝ)..1, logDeriv f (a + ω₁ + (t:ℝ) • ω₂) * ω₂) := by
    rw [intervalIntegral.integral_comp_sub_left
          (fun s : ℝ => logDeriv f (a + s • ω₂) * (-ω₂)) 1]
    simp only [sub_self, sub_zero]
    rw [← intervalIntegral.integral_neg]
    apply intervalIntegral.integral_congr
    intro s _
    simp only [mul_neg]
    congr 2
    rw [show a + ω₁ + s • ω₂ = (a + s • ω₂) + ω₁ by ring]
    exact (hp1 (a + s • ω₂)).symm
  rw [he3, he4]; ring

/-! ### The degree-zero theorem — REDUCED to the parallelogram argument principle -/

/-- **The parallelogram (rectangle-contour) argument principle — the single
remaining gap.** For an elliptic `f`, some corner-translate `a` of the fundamental
cell has no divisor points on `∂P`, and there the contour integral of `f'/f`
counts the interior divisor: `2πi · Σ_{z∈S} ord_z f = ∮_{∂P} logDeriv f`.

**OPEN.** This is the argument principle for a *parallelogram* contour. It is the
sibling of `QOU.Mathlib.ArgumentPrinciple.contour_deformation_sum` (the *circle*
argument principle), but a **distinct** Lean statement: it deforms `∂P` — a
rectangle/parallelogram contour, not a circle — onto small circles around the
interior punctures. Mathlib v4.24.0 has the rectangle *vanishing*
(`integral_boundary_rect_eq_zero_of_differentiable_on_off_countable`, for a
holomorphic integrand) but **no** rectangle-contour residue sum, so the circle
`argument_principle` cannot be reused verbatim; the same multiply-connected Cauchy
topology that `residue_theorem_deformation` isolates is what this needs. Left as a
single cited `sorry`; the boundary-vanishing half (`paraBoundaryLogDeriv_eq_zero`)
is proved sorry-free above. -/
theorem parallelogram_argument_principle {f : ℂ → ℂ} {ω₁ ω₂ : ℂ}
    (hf : IsElliptic f ω₁ ω₂)
    (hindep : LinearIndependent ℝ ![ω₁, ω₂])
    (hnc : ¬ ∃ c, ∀ z, f z = c)
    (S : Finset ℂ)
    (hS : (S : Set ℂ) =
      {z | z ∈ fundamentalParallelogram ω₁ ω₂ ∧
        (MeromorphicOn.divisor f Set.univ) z ≠ 0}) :
    ∃ a : ℂ, (2 * (Real.pi : ℂ) * Complex.I) *
        ((∑ z ∈ S, (MeromorphicOn.divisor f Set.univ) z : ℤ) : ℂ)
      = paraBoundaryLogDeriv f a ω₁ ω₂ := by
  -- Ref: [manuscript] argument principle over a fundamental-parallelogram contour
  --   (Ahlfors, *Complex Analysis*, Ch. 7 §2, elliptic functions; the rectangle
  --   analogue of the circle residue theorem). Absent from Mathlib v4.24.0 — the
  --   multiply-connected Cauchy deformation of a parallelogram contour, sibling of
  --   `QOU.Mathlib.ArgumentPrinciple.residue_theorem_deformation`. See
  --   docs/audits/2026-07-20-pi2-elliptic-divisor-scaffold.md.
  sorry

/-- **Liouville's third theorem: the degree of an elliptic divisor is zero.**
For a nonconstant elliptic function `f` with `ℝ`-independent periods, the sum of
the local orders (zeros minus poles, with multiplicity) over one fundamental
parallelogram vanishes. `S` enumerates the finitely many divisor points inside the
cell (the finiteness — support locally finite ∩ compact cell — is a separate,
tractable brick; it is passed as `hS` so that the analytic core is isolated).

**DERIVED (sorry-free modulo the single gap `parallelogram_argument_principle`).**
The proof composes the two halves of the classical argument
`Σ_{p∈P} ord_p f = (1/2πi) ∮_{∂P} logDeriv f = 0`:

* the boundary-integral cancellation `∮_{∂P} logDeriv f = 0`
  (`paraBoundaryLogDeriv_eq_zero`) is **proved sorry-free** — pure periodicity; and
* the identity `2πi · Σ ord = ∮_{∂P} logDeriv f` is
  `parallelogram_argument_principle`, the *single* remaining gap (the
  parallelogram-contour argument principle, absent from Mathlib v4.24.0).

Given both, `2πi · Σ ord = 0`, and since `2πi ≠ 0` the (integer-cast) divisor sum
vanishes. The gap is a **rectangle-contour** residue-deformation — a *sibling* of
the circle argument principle's `contour_deformation_sum`, not literally it. -/
theorem elliptic_divisor_degree_zero {f : ℂ → ℂ} {ω₁ ω₂ : ℂ}
    (hf : IsElliptic f ω₁ ω₂)
    (hindep : LinearIndependent ℝ ![ω₁, ω₂])
    (hnc : ¬ ∃ c, ∀ z, f z = c)
    (S : Finset ℂ)
    (hS : (S : Set ℂ) =
      {z | z ∈ fundamentalParallelogram ω₁ ω₂ ∧
        (MeromorphicOn.divisor f Set.univ) z ≠ 0}) :
    ∑ z ∈ S, (MeromorphicOn.divisor f Set.univ) z = 0 := by
  obtain ⟨a, ha⟩ := parallelogram_argument_principle hf hindep hnc S hS
  rw [paraBoundaryLogDeriv_eq_zero hf a] at ha
  -- `ha : 2πi · (Σ ord : ℂ) = 0`; cancel the nonzero `2πi`.
  have h2 : (2 * (Real.pi : ℂ) * Complex.I) ≠ 0 := by
    have hpi : (Real.pi : ℂ) ≠ 0 := by exact_mod_cast Real.pi_ne_zero
    exact mul_ne_zero (mul_ne_zero two_ne_zero hpi) Complex.I_ne_zero
  have hcast : (((∑ z ∈ S, (MeromorphicOn.divisor f Set.univ) z : ℤ)) : ℂ) = 0 :=
    (mul_eq_zero.mp ha).resolve_left h2
  exact_mod_cast hcast

end QOU.Mathlib.EllipticDivisorDegree
