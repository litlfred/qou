import QOU.MathlibExt.DoublyPeriodicLiouville
import QOU.Common.PeriodicDense

/-!
# Route-B assembly (brick d): meromorphic Faddeev rigidity from the entire ratio

The physical `Φ_b` is **meromorphic**, not entire-nowhere-zero, so the idealized
`FaddeevRigidityReduction.uniqueUpToScalar_of_entire` (which needs `Φ` entire and
nowhere zero) does not apply to it. This file supplies the **meromorphic-route
assembly**: given the two solutions' ratio `r = Ψ/Φ`,

* **the single open analytic input (bricks b/c)** — `r` extends to an **entire**
  function `hr_entire`. For the physical `Φ_b` this is *not* derivable from the
  q-difference equations alone: route-B step 2
  (`QBeta.MeromorphicSameOrder.meromorphicOrderAt_orderDiff_periodic`) shows the
  order-difference `ord Ψ − ord Φ` is doubly periodic, so `r` is an **elliptic**
  function — which may be *nonconstant* (Weierstrass `℘`). Entireness of `r` is the
  independent divisor-rigidity fact that `Φ_b`'s specific zero/pole lattice pins
  (same divisor ⇒ `r` has no poles), and it is honestly carried here as a
  hypothesis, **not** an axiom and **not** assumed of a generic solution;
* **the two periodicities of `r`** — supplied by step 2 together with the merged
  dense-extension core (`QOU.Common.periodic_of_continuous_of_eqOn_dense`): where
  both `Φ` and the prefactor are nonzero, `r(z+c)=Ψ(z+c)/Φ(z+c)=Pψ/PΦ=r(z)`, and
  an entire (continuous) function periodic on the dense complement of the pole
  lattice is periodic everywhere.

Given those, **Liouville for doubly-periodic entire functions**
(`const_of_doublyPeriodic`) forces `r` constant, hence `Ψ = c·Φ` wherever `Φ ≠ 0`.

The proportionality is **derived**; the entire-ratio hypothesis is the genuine
open brick (b/c). This is the §3b-cond non-degenerate shape: the hypothesis
encodes an *input* (the divisor-rigidity analytic fact), and the conclusion
(proportionality) is *composed* from it via the proved Liouville lemma — not a
self-assuming projection.

Verified `lean`-direct against pinned Mathlib (exit 0). Imports only
`DoublyPeriodicLiouville` (in the QOU olean cache); the Meromorphic cone is not
needed for the assembly — it enters only in the step-2 justification of the
periodicity input.

Ref: [leitner2026] docs/audits/2026-07-18-endowment-scope-meromorphic-wall.md §2
-/

open Complex Module
open QOU.MathlibExt.DoublyPeriodicLiouville

namespace QOU.QBeta.FaddeevRigidityMeromorphic

/-- **Route-B brick (d): meromorphic rigidity assembly from the entire ratio.**
Let `Φ, Ψ : ℂ → ℂ` be the two meromorphic solutions and `r` their ratio
(`r z = Ψ z / Φ z` wherever `Φ z ≠ 0`). If

* `r` is **entire** (`hr_entire`) — the open divisor-rigidity input (bricks b/c),
  *not* derivable from the difference equations (the elliptic ratio can be
  nonconstant); and
* `r` is periodic under both vectors of an `ℝ`-basis `bas` of `ℂ` (`hper`) — the
  double periodicity from route-B step 2 plus the dense-extension core,

then `∃ c, Ψ z = c · Φ z` for every `z` with `Φ z ≠ 0`. The doubly-periodic-entire
Liouville lemma supplies the constancy of `r`; proportionality is derived. -/
theorem uniqueUpToScalar_meromorphic
    {Φ Ψ r : ℂ → ℂ} {bas : Basis (Fin 2) ℝ ℂ}
    (hr_entire : Differentiable ℂ r)
    (hr_ratio : ∀ z, Φ z ≠ 0 → r z = Ψ z / Φ z)
    (hper : ∀ i, ∀ z, r (z + bas i) = r z) :
    ∃ c, ∀ z, Φ z ≠ 0 → Ψ z = c * Φ z := by
  obtain ⟨c, hc⟩ := const_of_doublyPeriodic hr_entire hper
  refine ⟨c, fun z hz => ?_⟩
  have hratio : Ψ z / Φ z = c := by rw [← hr_ratio z hz, hc z]
  exact (div_eq_iff hz).mp hratio

/-- **Corollary — proportionality of the entire ratio itself.** Under the same
hypotheses the ratio `r` is the constant `c`, so on the nonvanishing locus of `Φ`
the two solutions agree up to that one scalar. This is the form fed back into the
`FaddeevPhi` rigidity statement once bricks (b/c) pin `hr_entire` for `Φ_b`. -/
theorem ratio_const_meromorphic
    {Φ Ψ r : ℂ → ℂ} {bas : Basis (Fin 2) ℝ ℂ}
    (hr_entire : Differentiable ℂ r)
    (hr_ratio : ∀ z, Φ z ≠ 0 → r z = Ψ z / Φ z)
    (hper : ∀ i, ∀ z, r (z + bas i) = r z) :
    ∃ c, (∀ z, r z = c) ∧ (∀ z, Φ z ≠ 0 → Ψ z = c * Φ z) := by
  obtain ⟨c, hc⟩ := const_of_doublyPeriodic hr_entire hper
  refine ⟨c, hc, fun z hz => ?_⟩
  have hratio : Ψ z / Φ z = c := by rw [← hr_ratio z hz, hc z]
  exact (div_eq_iff hz).mp hratio

/-- **Sharper reduction — periodicity only on a dense set (bricks b/c internalized).**
The existing `FaddeevPhi` ratio lemmas (`CyclicDilogPentagon.ratio_ib_periodic`,
`ratio_ibinv_periodic`) give the two periodicities of `r = Ψ/Φ` only **where the
shared quasi-period prefactor is nonzero** — a *dense* locus, not all of `ℂ`. This
theorem consumes exactly that: `r` entire, and `r` periodic under each basis vector
on a **dense** set `Sᵢ`. The merged dense-extension core
(`QOU.Common.periodic_of_continuous_of_eqOn_dense`) promotes each dense-set
periodicity to everywhere (a continuous function periodic on a dense set is periodic
everywhere), then `uniqueUpToScalar_meromorphic` finishes.

After this, the **sole** genuinely-open analytic input for the meromorphic `Φ_b` is
`hr_entire` — that `r` extends across the removable singularities to an entire
function (the divisor-rigidity fact bricks b/c name). The periodicity is no longer an
input: it is derived from the difference equations on the dense prefactor-nonzero
locus and promoted by continuity. Density of that locus is a discreteness fact about
`Φ_b`'s zero/pole lattice, folded into the `Dense Sᵢ` hypotheses and gated — like
`hr_entire` — on the `PhiBProd` construction; neither is axiomatized here. -/
theorem uniqueUpToScalar_of_ratio_dense_periodic
    {Φ Ψ r : ℂ → ℂ} {bas : Basis (Fin 2) ℝ ℂ}
    (hr_entire : Differentiable ℂ r)
    (hr_ratio : ∀ z, Φ z ≠ 0 → r z = Ψ z / Φ z)
    {S₀ S₁ : Set ℂ} (hS₀ : Dense S₀) (hS₁ : Dense S₁)
    (hper₀ : ∀ z ∈ S₀, r (z + bas 0) = r z)
    (hper₁ : ∀ z ∈ S₁, r (z + bas 1) = r z) :
    ∃ c, ∀ z, Φ z ≠ 0 → Ψ z = c * Φ z := by
  have h0 : ∀ z, r (z + bas 0) = r z :=
    QOU.Common.periodic_of_continuous_of_eqOn_dense hr_entire.continuous hS₀ hper₀
  have h1 : ∀ z, r (z + bas 1) = r z :=
    QOU.Common.periodic_of_continuous_of_eqOn_dense hr_entire.continuous hS₁ hper₁
  have hper : ∀ i, ∀ z, r (z + bas i) = r z := by
    intro i z; fin_cases i
    · exact h0 z
    · exact h1 z
  exact uniqueUpToScalar_meromorphic hr_entire hr_ratio hper

end QOU.QBeta.FaddeevRigidityMeromorphic
