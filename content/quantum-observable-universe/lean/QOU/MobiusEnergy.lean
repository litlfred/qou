import QOU.Basic
import QOU.Glossary
import QOU.KnotTheory
import QOU.QuantumObservableUniverse
import QOU.PathIntegrals
import QOU.MassDerivation
import Mathlib.Data.Real.Basic
import Mathlib.Topology.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.Tactic.Linarith

/-!
# QOU.MobiusEnergy — Categorical Möbius Energy and Self-Avoidance

Formalization of the categorical Möbius energy functional and the
non-self-intersection corollary from Chapter 4, §9 of the QOU manuscript.

## Structure

1. **Categorical Möbius energy** — the functional `E_cat(γ)` built from the
   Frobenius–Hopf comultiplication and q-Hodge star.
2. **Classical limit** — in the limit `q → 1`, `E_cat` recovers the classical
   Möbius energy up to topological normalisation.
3. **Non-self-intersection** — the non-cocommutativity of the Hopf structure
   at `q ≠ 1` provides an energy barrier preventing self-intersection.

## References

- [freedman1994] M. Freedman, Z.-X. He, Z. Wang, "Möbius energy of knots
  and unknots", Annals of Mathematics 139 (1994), 1–50.
- [ohara1991] J. O'Hara, "Energy of a knot", Topology 30 (1991), 241–247.
-/


open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

/-! ## §1  Knot Embedding and Classical Möbius Energy -/

/-- A **knot embedding** `γ : S¹ → M` in the fibre of the realisation functor,
    equipped with smooth parametrisation data.

    In the categorical setting, `γ` takes values in `ω(A)` where `ω` is the
    fibre functor and `A` is the Frobenius–Hopf object. -/
structure KnotEmbedding (M : Type*) where
  /-- The parametrised curve `γ : [0, 1] → M` (periodic). -/
  curve : ℝ → M
  /-- Arc-length distance along the curve. -/
  arcLengthDist : ℝ → ℝ → ℝ
  /-- Arc-length distance is symmetric. -/
  arcLength_symm : ∀ s t, arcLengthDist s t = arcLengthDist t s
  /-- Arc-length distance is non-negative. -/
  arcLength_nonneg : ∀ s t, 0 ≤ arcLengthDist s t

/-- The **classical Möbius energy** of a knot embedding.

    $$E(\gamma) = \iint_{S^1 \times S^1}
      \left(\frac{1}{|\gamma(s) - \gamma(t)|^2}
        - \frac{1}{D(\gamma(s), \gamma(t))^2}\right)
      |\gamma'(s)|\,|\gamma'(t)|\,ds\,dt.$$

    Ref: [freedman1994], [ohara1991]
    LaTeX: `\label{prop:mobius-energy}` (classical part) -/
structure ClassicalMobiusEnergy where
  /-- The energy value `E(γ)`. -/
  value : ℝ
  /-- The energy is non-negative (Freedman–He–Wang). -/
  nonneg : 0 ≤ value
  /-- Whether the underlying knot is the unknot.  Carried as an opaque
      `Prop` because this structure holds no isotopy-class data; it is the
      minimum needed to *state* Freedman–He–Wang rather than assert its
      conclusion. -/
  isUnknot : Prop
  /-- The energy equals 4 if and only if the knot is the unknot
      (Freedman–He–Wang, 1994).

      **This field read `value = 4 ↔ True` until 2026-08-30.** `P ↔ True`
      is `P`, so that spelling forced `value = 4` for *every* instance —
      machine-checked, `c.unknot_iff.mpr trivial : c.value = 4` — which is
      not a weakened form of Freedman–He–Wang but the negation of its
      content: it made the classical Möbius energy blind to the knot, and
      through `CategoricalMobiusEnergy.classicalLimit` made `E_cat` blind
      too (`E_cat = 1 + const` for every knot).  It carried no `sorry`, no
      `axiom` and no tautological *conclusion*, so no vacuity detector saw
      it, and a prior audit (bean `qou-u87j`) cited its presence as
      evidence the library encoding was *stronger* than its content-block
      sibling. -/
  -- Ref: [freedman1994] https://doi.org/10.2307/2946626
  unknot_iff : value = 4 ↔ isUnknot

/-! ## §2  Categorical Möbius Energy -/

/-- **Categorical Möbius energy data** for a knot `γ` in a quantum observable
    universe `(C, A, ω)`.

    The energy functional is
    $$E_{\mathrm{cat}}(\gamma) = \lambda \circ \mathrm{tr}_A
      \iint_{S^1 \times S^1 \setminus \mathrm{diag}}
      (\Delta(\gamma(s)) \otimes \Delta(\gamma(t)))
      \star_q \|d\gamma/ds \wedge_q d\gamma/dt\|\,ds\,dt$$

    where `Δ` is the Hopf comultiplication, `λ` is the Frobenius form,
    and `⋆_q` is the q-Hodge star.

    LaTeX: `\label{prop:mobius-energy}` -/
structure CategoricalMobiusEnergy (M : Type*) where
  /-- The substrate parameter governing the q-deformation. -/
  sp : ArchimedeanSubstrateField M
  /-- A chosen base point for evaluating the substrate field. -/
  basepoint : M
  /-- The q-parameter value at the base point. -/
  q : ℝ := sp.field basepoint
  /-- `q > 1` (non-classical regime). -/
  q_gt_one : q > 1
  /-- The knot embedding in the fibre space. -/
  knot : KnotEmbedding M
  /-- The categorical energy value `E_cat(γ)`. -/
  energy : ℝ
  /-- The classical Möbius energy of the same knot. -/
  classicalEnergy : ClassicalMobiusEnergy
  /-- The categorical energy of the knot after applying the Möbius
      transform with parameter `g ∈ PSL(2, ℂ)` (parametrised here by a
      real coordinate on the group, acting on the `ℂP¹` fibre via the
      gauge group fixed by the categorical volume constraint). -/
  energyUnderMobius : ℝ → ℝ
  /-- **Möbius invariance**: `E_cat(γ)` is invariant under the full Möbius
      group `PSL(2, ℂ)`. Encoded as: the transformed energy equals the
      base energy for every group element `g` — the energy functional is
      constant along every Möbius orbit (categorical: invariance under
      `Aut⊗(ω)`). -/
  mobiusInvariant : ∀ g : ℝ, energyUnderMobius g = energy
  /-- **Classical limit**: as `q → 1`, the categorical energy recovers the
      classical Möbius energy up to topological normalisation.
      Encoded as: `E_cat = (1/4) · E_classical + const`. -/
  classicalLimitConst : ℝ
  classicalLimit : energy = (1 / 4) * classicalEnergy.value + classicalLimitConst

/-- The quantum Planck constant at a given substrate parameter value. -/
noncomputable def hbar_q (q : ℝ) : ℝ := 1 - q⁻¹

/-- The quantum integer `[2]_q = q + q⁻¹`. -/
noncomputable def quantumTwo (q : ℝ) : ℝ := q + q⁻¹

/-! ## §3  Möbius Energy Recovery (Proposition) -/

/-- **Proposition: Categorical recovery of Möbius energy.**

    In the classical limit `q → 1`, the categorical Möbius energy recovers
    the classical Möbius energy up to a topological normalisation:
    $$\lim_{q \to 1} E_{\mathrm{cat}}(\gamma) = \frac{1}{4} E(\gamma) + \mathrm{const}.$$

    The proof proceeds in three steps:
    1. **Gauge fixing** — the categorical volume constraint fixes `G = SU(2)`,
       ensuring `E_cat` is Möbius-invariant.
    2. **Frobenius–Hopf kernel expansion** — at `q = 1`, the comultiplication
       becomes cocommutative and the Frobenius pairing reduces to the Killing
       form, yielding the `1/r²` repulsive kernel.
    3. **Self-energy subtraction** — the diagonal regularisation matches the
       arc-length subtraction via the antipode `S`.

    Stated along the whole Möbius orbit rather than at the base energy
    alone. In that form it is **derived** from two fields — invariance
    carries the transformed energy back to `E_cat`, and the classical
    limit then applies — rather than returned verbatim.

    The base case is `cme.classicalLimit` itself, which is what this
    declaration used to restate: `theorem MobiusEnergy … :=
    cme.classicalLimit`, the structure field under a second name. Use
    the field directly when the orbit plays no part.

    LaTeX: `\label{prop:mobius-energy}` -/
theorem MobiusEnergy {M : Type*} (cme : CategoricalMobiusEnergy M) (g : ℝ) :
    cme.energyUnderMobius g
      = (1 / 4) * cme.classicalEnergy.value + cme.classicalLimitConst := by
  rw [cme.mobiusInvariant g]
  exact cme.classicalLimit

/-- The categorical Möbius energy is non-negative (inheriting from the
    classical bound and the normalisation). -/
theorem MobiusEnergy_nonneg {M : Type*} (cme : CategoricalMobiusEnergy M)
    (h_const_nonneg : 0 ≤ cme.classicalLimitConst) :
    0 ≤ cme.energy := by
  rw [cme.classicalLimit]
  have := cme.classicalEnergy.nonneg
  linarith

/-! ## §4  Non-Self-Intersection Corollary -/

/-- **q-Deformed repulsion kernel**.

    At `q ≠ 1`, the classical `1/r²` kernel is replaced by
    $$\frac{[2]_q}{r^2 - \hbar_q^2}$$
    which has a hard singularity at `r = ℏ_q`, creating an energy barrier. -/
noncomputable def qRepulsionKernel (q r : ℝ) : ℝ :=
  quantumTwo q / (r ^ 2 - hbar_q q ^ 2)

/-- At the pole itself the kernel evaluates to `0` — **Lean's `x / 0 = 0`
    junk value, not a statement about the singularity.**

    This declaration was named `qRepulsionKernel_singular` and documented as
    "the q-deformed kernel diverges at `r = ℏ_q`" while concluding `= 0`,
    proved by `div_zero`.  The name and the docstring asserted a divergence;
    the statement asserted its opposite, and the proof established only the
    division convention.  Renamed and re-documented 2026-08-30; the genuine
    divergence is `qRepulsionKernel_unbounded_near_pole` below, and it is
    that lemma — not this one — that the non-self-intersection corollary
    needs. -/
theorem qRepulsionKernel_junk_value_at_pole (q r : ℝ)
    (hr : r ^ 2 - hbar_q q ^ 2 = 0) :
    qRepulsionKernel q r = 0 := by
  unfold qRepulsionKernel
  rw [hr, div_zero]

/-- The quantum Planck constant is positive when `q > 1`. -/
theorem hbar_q_pos (q : ℝ) (hq : q > 1) : 0 < hbar_q q := by
  unfold hbar_q
  have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  linarith

/-- The quantum integer `[2]_q` is positive when `q > 0`. -/
theorem quantumTwo_pos (q : ℝ) (hq : q > 0) : 0 < quantumTwo q := by
  unfold quantumTwo
  have : 0 < q⁻¹ := inv_pos.mpr hq
  linarith

/-- **The genuine divergence.**  For `q > 1` the kernel exceeds every bound
    at radii strictly outside the exclusion radius `ℏ_q`, so it is unbounded
    as `r ↘ ℏ_q`.  This is the energy barrier the non-self-intersection
    corollary rests on; `qRepulsionKernel_junk_value_at_pole` above is not. -/
theorem qRepulsionKernel_unbounded_near_pole (q : ℝ) (hq : q > 1) (B : ℝ) :
    ∃ r : ℝ, hbar_q q < r ∧ B < qRepulsionKernel q r := by
  have hh : 0 < hbar_q q := hbar_q_pos q hq
  have hc : 0 < quantumTwo q := quantumTwo_pos q (by linarith)
  set M : ℝ := max B 1 + 1 with hM
  have hM1 : 1 < M := by
    have : (1 : ℝ) ≤ max B 1 := le_max_right _ _
    simp only [hM]; linarith
  have hMpos : 0 < M := by linarith
  have hMB : B < M := by
    have : B ≤ max B 1 := le_max_left _ _
    simp only [hM]; linarith
  set d : ℝ := quantumTwo q / M with hd
  have hdpos : 0 < d := div_pos hc hMpos
  refine ⟨Real.sqrt (hbar_q q ^ 2 + d), ?_, ?_⟩
  · have h1 : hbar_q q ^ 2 < hbar_q q ^ 2 + d := by linarith
    have h2 : Real.sqrt (hbar_q q ^ 2) < Real.sqrt (hbar_q q ^ 2 + d) :=
      Real.sqrt_lt_sqrt (sq_nonneg _) h1
    rwa [Real.sqrt_sq hh.le] at h2
  · have hsq : Real.sqrt (hbar_q q ^ 2 + d) ^ 2 = hbar_q q ^ 2 + d :=
      Real.sq_sqrt (by positivity)
    have hden : Real.sqrt (hbar_q q ^ 2 + d) ^ 2 - hbar_q q ^ 2 = d := by
      rw [hsq]; ring
    have hcancel : quantumTwo q / d = M := by
      rw [hd]; field_simp
    unfold qRepulsionKernel
    rw [hden, hcancel]
    exact hMB

/-- **Corollary: Obstruction to self-intersection.**

    For `q ≠ 1`, the non-cocommutativity of the Hopf structure provides a
    categorical obstruction to knot self-intersection: the energy diverges
    whenever two non-adjacent strands approach within distance `ℏ_q`.

    The mechanism:
    - The universal R-matrix `R ∈ U_q(su(2)) ⊗̂ U_q(su(2))` controls the
      failure of cocommutativity: `σ ∘ Δ ≠ Δ`.
    - The q-deformed commutator `[X̂, P̂]_q = iℏ_q` replaces the `1/r²`
      kernel with `[2]_q / (r² − ℏ_q²)`.
    - This kernel has a hard singularity at `r = ℏ_q`, creating an energy
      barrier of infinite height — the "quantum exclusion zone".

    Physically, the vortex filament `γ` cannot pass through itself because
    doing so would require infinite categorical energy. This is the
    knot-theoretic analogue of the Pauli exclusion principle.

    LaTeX: `\label{cor:non-self-intersection}` -/
structure NonSelfIntersection (M : Type*) where
  /-- The categorical Möbius energy data. -/
  cme : CategoricalMobiusEnergy M
  /-- Ambient separation between the strand points at parameters `s` and `t`.

      `KnotEmbedding` carries only `arcLengthDist` — an *intrinsic* distance
      along the curve — so the ambient separation that the `1/r²` kernel is a
      function of does not exist anywhere upstream.  It is carried here
      because the barrier cannot be stated without it. -/
  separation : ℝ → ℝ → ℝ
  /-- **Energy barrier.**  If some pair of strand points came within the
      exclusion radius `ℏ_q`, the categorical energy would exceed every
      bound.  Stated as an implication, so an inhabitant is a configuration
      that keeps every pair *outside* `ℏ_q` — which is the physical content
      ("the filament cannot pass through itself"), recovered as
      `separation_ge_exclusionRadius` below.

      **This field asserted the consequent unconditionally until
      2026-08-30**, as `∀ E₀ : ℝ, ∃ ε : ℝ, ε > 0 ∧ (∀ _s _t : ℝ, cme.energy
      > E₀)`.  The two `_s _t` binders were unused, so the inner `∀` was a
      constant and the field reduced to `∀ E₀ : ℝ, cme.energy > E₀` — the
      energy exceeds every real.  Instantiating at `E₀ := cme.energy` gives
      `cme.energy > cme.energy`, so `NonSelfIntersection M` was
      **uninhabitable for every `M`** (machine-checked: `IsEmpty
      (NonSelfIntersection M)`), and every result conditional on it was
      vacuous.  The docstring's own quantifier order (`∀ ε, ∃ E₀`) was the
      reverse of the code's, and the proximity antecedent it describes was
      never written as a hypothesis at all. -/
  energyBarrier : ∀ s t : ℝ, separation s t < hbar_q cme.q →
    ∀ E₀ : ℝ, cme.energy > E₀

/-- The exclusion radius: `ℏ_q = 1 − q⁻¹`, derived from the categorical
    Möbius energy data. Not a free parameter — it is always `hbar_q cme.q`. -/
noncomputable def NonSelfIntersection.exclusionRadius {M : Type*}
    (nsi : NonSelfIntersection M) : ℝ := hbar_q nsi.cme.q

/-- The exclusion radius is exactly `ℏ_q`. -/
theorem exclusionRadius_eq {M : Type*}
    (nsi : NonSelfIntersection M) :
    nsi.exclusionRadius = hbar_q nsi.cme.q := rfl

/-- The exclusion radius is positive — **derived** from `cme.q_gt_one`
    through `hbar_q_pos`, not carried.  It was a structure field
    (`exclusionRadius_pos`) until 2026-08-30; a hypothesis that follows from
    another field is an assumption wearing a theorem's name.  Matches the
    repair already made to the content-block sibling
    `climax-volume-mass/non-self-intersection-proof.lean`. -/
theorem exclusionRadius_pos {M : Type*} (nsi : NonSelfIntersection M) :
    0 < nsi.exclusionRadius :=
  hbar_q_pos nsi.cme.q nsi.cme.q_gt_one

/-- **The exclusion, derived rather than assumed.**  No two strand points of
    an inhabitant come within the exclusion radius: if one pair did, the
    barrier field would make the energy exceed itself. -/
theorem separation_ge_exclusionRadius {M : Type*}
    (nsi : NonSelfIntersection M) (s t : ℝ) :
    hbar_q nsi.cme.q ≤ nsi.separation s t := by
  by_contra h
  push_neg at h
  exact absurd (nsi.energyBarrier s t h nsi.cme.energy) (lt_irrefl _)

/-- The exclusion radius vanishes in the classical limit `q → 1`. -/
theorem hbar_q_classical_limit : hbar_q 1 = 0 := by
  unfold hbar_q
  simp [inv_one]

/-- At `q > 1`, the exclusion zone has positive radius, providing
    a genuine obstruction to self-intersection. -/
theorem exclusionZone_positive (q : ℝ) (hq : q > 1) :
    0 < hbar_q q :=
  hbar_q_pos q hq

end QOU
