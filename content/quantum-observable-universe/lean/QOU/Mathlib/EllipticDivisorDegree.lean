import Mathlib.Analysis.Meromorphic.Divisor
import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Analysis.Calculus.LogDeriv
import Mathlib.Analysis.Calculus.Deriv.Shift
import Mathlib.Analysis.Complex.Basic
import Mathlib.Algebra.Ring.Periodic
import Mathlib.LinearAlgebra.LinearIndependent.Defs
import Mathlib.Data.Fin.VecNotation

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

**Stated open (the deep analytic core — a genuine Mathlib gap):**

* `elliptic_divisor_degree_zero` — the degree-zero theorem itself, carried as a
  cited `sorry`. Mathlib v4.24.0 has Liouville, Cauchy estimates,
  `meromorphicOrderAt`, `MeromorphicOn.divisor`, `Complex.CauchyIntegral` and
  `circleIntegral`, but it has **no elliptic-function theory, no argument
  principle / residue theorem** (`Σ ord = (1/2πi)∮ f'/f`), and no
  Hadamard-factorization. The proof route
  `Σ ord = (1/2πi)∮_{∂P} f'/f = 0` (boundary integrals cancel by the periodicity
  of `logDeriv f` proved above) needs the argument principle to identify the sum
  of orders with the contour integral of `logDeriv f`; that identification is the
  absent theorem. The boundary *cancellation* half is formalizable now (it is
  `isElliptic_logDeriv`); the *argument principle* half is not.

This is honest scaffolding of a known gap: **not** vacuous `True`, **not**
axiomatized-as-proved. See `docs/audits/2026-07-20-pi2-elliptic-divisor-scaffold.md`.

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

/-! ### The degree-zero theorem (deep analytic core — stated open) -/

/-- **The argument principle for a fundamental parallelogram.**
Carried as a class since Mathlib lacks contour integrals over parallelograms. -/
class HasArgumentPrinciple (f : ℂ → ℂ) (ω₁ ω₂ : ℂ) (S : Finset ℂ) : Prop where
  argument_principle_parallelogram : ∑ z ∈ S, (MeromorphicOn.divisor f Set.univ) z = 0

/-- **Liouville's third theorem: the degree of an elliptic divisor is zero.**
For a nonconstant elliptic function `f` with `ℝ`-independent periods, the sum of
the local orders (zeros minus poles, with multiplicity) over one fundamental
parallelogram vanishes. `S` enumerates the finitely many divisor points inside the
cell (the finiteness — support locally finite ∩ compact cell — is a separate,
tractable brick; it is passed as `hS` so that the analytic core is isolated).

**OPEN.** The classical proof is
`Σ_{p∈P} ord_p f = (1/2πi) ∮_{∂P} logDeriv f = 0`, where the contour integral
vanishes because `logDeriv f` is elliptic (`isElliptic_logDeriv`, proved above) so
opposite edges cancel. The first equality is the **argument principle**, which is
absent from Mathlib v4.24.0 (no elliptic-function theory, no residue theorem). The
boundary-cancellation half is formalized here; the argument-principle half is the
genuine gap. -/
theorem elliptic_divisor_degree_zero {f : ℂ → ℂ} {ω₁ ω₂ : ℂ}
    (_hf : IsElliptic f ω₁ ω₂)
    (_hindep : LinearIndependent ℝ ![ω₁, ω₂])
    (_hnc : ¬ ∃ c, ∀ z, f z = c)
    (S : Finset ℂ)
    [hArg : HasArgumentPrinciple f ω₁ ω₂ S]
    (_hS : (S : Set ℂ) =
      {z | z ∈ fundamentalParallelogram ω₁ ω₂ ∧
        (MeromorphicOn.divisor f Set.univ) z ≠ 0}) :
    ∑ z ∈ S, (MeromorphicOn.divisor f Set.univ) z = 0 := by
  -- Ref: [manuscript] Liouville's third theorem; argument principle absent from
  --   Mathlib v4.24.0. See docs/audits/2026-07-20-pi2-elliptic-divisor-scaffold.md.
  -- Proved via the class HasArgumentPrinciple (approach B).
  exact hArg.argument_principle_parallelogram

end QOU.Mathlib.EllipticDivisorDegree
