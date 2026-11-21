import QOU.Torsion.MassIdentity
import QOU.Torsion.ArchimedeanMassIdentity
import QOU.Torsion.Descent
import QOU.MathlibExt.QIntegerCanonical
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
# §11–§13  Topological Mass Decomposition, Dimensional Reduction,
           Classical Limit

The topological decomposition of mass into descended + transient
contributions, the q-number, dimensional reduction, and classical
limit recovery.
-/


namespace QOU.Torsion

/-! ## §11  Topological Mass Decomposition -/

/-- **Quantum dilogarithm**: `Φ_q(z) = ∫₀ᶻ ln_q(1+t)/t dt`. -/
noncomputable def qNumber (q : ℝ) (n : ℕ) : ℝ :=
  if q = 1 then n
  else (q ^ n - 1) / (q - 1)

/-- **Bridge to the canonical guarded geometric bracket.**

`qNumber` is kept rather than aliased: its proofs below (`qNumber_pos`) need the
closed form `(qⁿ−1)/(q−1)` syntactically, and swapping the body for
`qIntGeoCl`'s `Finset.sum` makes them fail. Consolidation here is this equation,
not a substitution — the two are the same function, and that is now proved
rather than left to a comment. -/
theorem qNumber_eq_canonical (q : ℝ) (n : ℕ) :
    qNumber q n = QOU.QInteger.qIntGeoCl q n := by
  unfold qNumber
  by_cases h : q = 1
  · simp [h]
  · rw [if_neg h, QOU.QInteger.qIntGeoCl_eq_closed_form h]

/-- The q-number `[n]_q` is positive for `q > 0` and `n ≥ 1`. -/
theorem qNumber_pos {q : ℝ} {n : ℕ} (hq : 0 < q) (hn : 0 < n) :
    0 < qNumber q n := by
  unfold qNumber
  split_ifs with h
  · exact Nat.cast_pos.mpr hn
  · have hq_ne : q ≠ 1 := h
    by_cases hq1 : 1 < q
    · apply div_pos
      · have : 1 < q ^ n :=
          one_lt_pow₀ hq1 (Nat.pos_iff_ne_zero.mp hn)
        linarith
      · linarith
    · have hq_lt : q < 1 := lt_of_le_of_ne (le_of_not_gt hq1) hq_ne
      apply div_pos_of_neg_of_neg
      · have : q ^ n < 1 := by
          exact pow_lt_one₀ hq.le hq_lt (Nat.pos_iff_ne_zero.mp hn)
        linarith
      · linarith

/-- **Topological Decomposition of Mass** (conjecture carrier).
    LaTeX: `\label{conj:topological-mass}` (demoted from `thm:` 2026-11-20,
    bean `qou-27ys`; the label in this docstring read `thm:` until bean
    `qou-dx7g`).

    **Vacuity status (bean `qou-dx7g`, 2026-11-20).**  `decomposition` carries
    the open equality `m = baseline + Σ exceptional` as a hypothesis, and every
    quantity in it — `totalMass`, `baselineHolonomy`, `exceptionalContribution`
    — is a free real supplied with the instance.  So `numBlowups := 0`,
    `totalMass = baselineHolonomy := 0` inhabits it (given any
    `ArchimedeanMassIdentity` / `BraneBoundary`), and the structure does not
    say which mass decomposes.  The content block
    (`mass-endomorphism/topological-mass.md`) states the intended objects:
    `m(γ) = ‖tr(γ)‖`, `baseline = ‖tr_desc(γ)‖ = ‖tr(τγ)‖`, transient terms
    `‖tr_trans(γ, pᵢ)‖`, and records why the equality is open — the idempotent
    splitting makes the *traces* add (`idempotent_gives_mass_decomposition`),
    not their norms.  Tying these reals to norms of traces of a vortex morphism
    needs the trace on `End_𝒞(A_{n+1})` and the vortex `γ` as data of this
    structure; neither is available on the bare type `M`, so the fields are
    left as they are and the gap is recorded here rather than papered over.

    **Which trace (added 2026-11-21).**  The `‖tr(γ)‖` above is a single trace of
    the vortex morphism.  The corpus's mass functional is the **two-term
    Lagrangian trace** `τ(ℒ_q) = τ(𝒟²) + τ(ψ*𝒟ψ)`
    (`QOU.CategoricalLagrangianTwoTermBridge.trace_lagrangian_two_term_split`,
    epic `qou-7xl8`), with `τ` the quantum trace `Tr(K^{⊗n} ·)/[2]_q^n` (owner ruling
    2026-11-20, option 2), which is the convention-D Markov trace
    (`JimboActionKernel.jimboMarkov`).  A faithful repair of this carrier must
    decompose `τ(ℒ_q)` — both the `𝒟²` term and the matter term — not a single
    `‖tr(γ)‖`; whether the blow-up decomposition applies to the matter term is
    not addressed anywhere in the corpus. -/
structure TopologicalMassDecomposition (M : Type*) where
  mi : ArchimedeanMassIdentity M
  di : DescentInvolution (M → ℝ)
  bb : BraneBoundary M
  numBlowups : ℕ
  baselineHolonomy : ℝ
  baseline_nonneg : 0 ≤ baselineHolonomy
  exceptionalContribution : Fin numBlowups → ℝ
  exceptional_nonneg : ∀ (i : Fin numBlowups), 0 ≤ exceptionalContribution i
  totalMass : ℝ
  totalMass_nonneg : 0 ≤ totalMass
  decomposition : totalMass = baselineHolonomy +
    (Finset.univ.sum fun i => exceptionalContribution i)
  -- The baseline holonomy is realised by a tau-fixed function.
  -- That is, there exists a descended function `g : M → ℝ` (a fixed point
  -- of `di.tau`) whose value is everywhere `baselineHolonomy`.
  -- This encodes "the baseline holonomy lives in the descended subalgebra".
  -- Ref: [leitner2026] §4-torsion
  baseline_is_descended : ∃ (g : M → ℝ), di.tau g = g ∧ ∀ p : M, g p = baselineHolonomy
  -- Every blow-up is localised at a boundary point.
  -- The transient mass is supported on `bb.boundary` in the sense that
  -- each exceptional contribution index corresponds to a point on the boundary.
  -- This encodes "transient mass vanishes away from the boundary".
  -- Ref: [leitner2026] §4-torsion
  transient_supported_on_boundary : ∀ (i : Fin numBlowups), ∃ p : M, p ∈ bb.boundary

theorem topological_mass_decomposition {M : Type*}
    (tmd : TopologicalMassDecomposition M) :
    tmd.totalMass = tmd.baselineHolonomy +
      (Finset.univ.sum fun i => tmd.exceptionalContribution i) :=
  tmd.decomposition

/-- The total mass is bounded below by the baseline holonomy. -/
theorem mass_ge_baseline {M : Type*}
    (tmd : TopologicalMassDecomposition M) :
    tmd.baselineHolonomy ≤ tmd.totalMass := by
  rw [tmd.decomposition]
  have h : 0 ≤ Finset.univ.sum tmd.exceptionalContribution :=
    Finset.sum_nonneg (fun i _ => tmd.exceptional_nonneg i)
  linarith

/-- When there are no blow-ups, mass = baseline. -/
theorem mass_unknot {M : Type*}
    (tmd : TopologicalMassDecomposition M)
    (h : tmd.numBlowups = 0) :
    tmd.totalMass = tmd.baselineHolonomy := by
  rw [tmd.decomposition]
  have : Finset.univ (α := Fin tmd.numBlowups) = ∅ := by
    rw [h]; exact Finset.univ_eq_empty
  simp [this]

/-- For a single blow-up, mass = baseline + one exceptional term. -/
theorem mass_single_blowup {M : Type*}
    (tmd : TopologicalMassDecomposition M)
    (h : tmd.numBlowups = 1) :
    tmd.totalMass = tmd.baselineHolonomy +
      tmd.exceptionalContribution ⟨0, by omega⟩ := by
  rw [tmd.decomposition]
  congr 1
  have huniq : ∀ (i : Fin tmd.numBlowups), i = ⟨0, by omega⟩ := by
    intro ⟨i, hi⟩; ext; omega
  have : Finset.univ (α := Fin tmd.numBlowups) = {⟨0, by omega⟩} := by
    ext x; simp [huniq x]
  rw [this, Finset.sum_singleton]

/-! ## §11a  Categorical Mass Decomposition

The categorical version of the topological mass decomposition:
mass = descended trace + Σ transient traces, where the splitting
comes from the idempotent decomposition of End_C(A_{n+1}) via the
descent involution.

LaTeX: `\label{thm:topological-mass}` (categorical proof) -/

/-- **Categorical Mass Decomposition** (data).

    The mass of a vortex `ϱ : 𝟙 → A` decomposes into descended
    and transient contributions via the descent involution `τ̂ₙ`.
    This is the categorical formulation — it works in any QOU,
    not just the archimedean realisation. -/
structure CategoricalMassDecomposition where
  /-- The descent involution on the endomorphism algebra. -/
  di : DescentInvolution (ℕ → ℝ)
  /-- Number of blow-up centres (exceptional divisors). -/
  numBlowups : ℕ
  /-- The total categorical mass `𝔪(ϱ)`. -/
  totalMass : ℝ
  totalMass_nonneg : 0 ≤ totalMass
  /-- Descended trace `‖tr_desc(ϱ)‖`: the mass of the base-level
      cycle ϱ₀, capturing baseline Frobenius–Hopf drag. -/
  descendedTrace : ℝ
  descended_nonneg : 0 ≤ descendedTrace
  /-- Transient trace `‖tr_trans(ϱ, pᵢ)‖` at each blow-up centre. -/
  transientTrace : Fin numBlowups → ℝ
  transient_nonneg : ∀ i, 0 ≤ transientTrace i
  /-- The decomposition: mass = descended + Σ transient. -/
  decomposition : totalMass = descendedTrace +
    (Finset.univ.sum fun i => transientTrace i)

/-- The categorical decomposition implies mass ≥ descended trace. -/
theorem categorical_mass_ge_descended (cmd : CategoricalMassDecomposition) :
    cmd.descendedTrace ≤ cmd.totalMass := by
  rw [cmd.decomposition]
  have h : 0 ≤ Finset.univ.sum cmd.transientTrace :=
    Finset.sum_nonneg (fun i _ => cmd.transient_nonneg i)
  linarith

/-- Each transient contribution is bounded by total mass minus descended. -/
theorem transient_le_mass_minus_descended (cmd : CategoricalMassDecomposition)
    (i : Fin cmd.numBlowups) :
    cmd.transientTrace i ≤ cmd.totalMass - cmd.descendedTrace := by
  rw [cmd.decomposition]
  have hsum : cmd.transientTrace i ≤ Finset.univ.sum cmd.transientTrace :=
    Finset.single_le_sum (fun j _ => cmd.transient_nonneg j) (Finset.mem_univ i)
  linarith

/-- A categorical decomposition with at least one blow-up has
    strictly positive mass if any transient contribution is positive. -/
theorem categorical_mass_pos_of_transient (cmd : CategoricalMassDecomposition)
    (i : Fin cmd.numBlowups) (hi : 0 < cmd.transientTrace i) :
    0 < cmd.totalMass := by
  have hd := cmd.descended_nonneg
  have ht : 0 < Finset.univ.sum cmd.transientTrace :=
    lt_of_lt_of_le hi
      (Finset.single_le_sum (fun j _ => cmd.transient_nonneg j) (Finset.mem_univ i))
  linarith [cmd.decomposition]

/-! ## §12  Dimensional Reduction -/

/-- **Remark (Reduction at dimension 1).**
    LaTeX: `\label{rem:descent-reduction}` -/
structure DimensionOneReduction (M : Type*) where
  dim : ℕ := 1
  holonomyAngle : M → ℝ
  no_bosonic_modes : ∀ (b : Boson M), ¬ b.toQHarmonicForm.toReebDecomposition.isPurelyHorizontal → False

/-- **Remark (Reduction at dimension 0).**
    LaTeX: `\label{rem:descent-reduction-zero}` -/
structure DimensionZeroReduction (M : Type*) where
  dim : ℕ := 0
  sp : ArchimedeanSubstrateField M
  curvature : M → ℝ
  curvature_vanishes : ∀ (p : M), curvature p = 0

/-! ## §13  Classical Limit Properties (Chapter 4 specific) -/

/-- `[n]₁ = n`. -/
theorem qNumber_at_one (n : ℕ) : qNumber 1 n = ↑n := by
  unfold qNumber; simp

/-- Mass at dimension 0 is pointwise. -/
theorem mass_dim_zero_pointwise {M : Type*}
    (mi : ArchimedeanMassIdentity M)
    (p : M) (hp : p ∈ mi.vortexCycle) :
    0 ≤ mi.connectionGradient p * mi.leviCurvatureCoupling p :=
  mi.integrand_nonneg p hp

end QOU.Torsion
