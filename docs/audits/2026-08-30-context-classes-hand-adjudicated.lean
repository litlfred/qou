/-
  Bean `qou-z9ws` — per-class HAND adjudication of the undecided context classes.

  WHY BY HAND, AND WHY THIS FILE IS SEPARATE FROM THE FIRST GATE

  [`2026-08-30-context-classes-are-inhabited-by-zero.lean`](2026-08-30-context-classes-are-inhabited-by-zero.lean)
  carries the machine result: 26 of 79 context classes inhabited by `Unit` and
  zero, found by
  [`scripts/lean-context-class-inhabitation-probe.py`](../../scripts/lean-context-class-inhabitation-probe.py).
  The other 53 came back `unproven` or `skipped`, which says nothing about them
  — only about the generator's defaults.

  I twice tried to fix the generator into deciding them and twice measured the
  yield: the sibling-import fix converts **1 of 54**, and feeding each claim's
  own constants into the discharge converts **0 of 6**. Both attempts are
  recorded in
  [`2026-08-30-the-remainder-is-vacuous-not-open.md`](2026-08-30-the-remainder-is-vacuous-not-open.md);
  the second was reverted rather than committed. So "keep improving the tool"
  is refuted by measurement, and **per-class hand construction is the only
  method shown to work.** This file is that method applied.

  WHAT A WITNESS HERE MEANS — the same narrow reading as the first gate.  A
  class inhabited with no hypotheses constrains nothing, so a `[C]` binder on
  it assumes nothing and the downstream `[C]`-conditional declaration is
  conditional on nothing.  It does NOT follow that the content block is wrong:
  a class may legitimately name a modelled object whose defining law is used to
  *derive* something downstream (`BorromeanQuark` is the worked case).  The
  discriminator is derive-vs-project, and every class below backs a declaration
  that projects.

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build` — a build
  against a restored cache with `traces=0` evicts it):

      LEAN_PATH=<mathlib libs>:<QOU build lib> \
        lean docs/audits/2026-08-30-context-classes-hand-adjudicated.lean

  Measured 2026-08-30: exit 0, 0 errors.
-/
import QOU.BraidsAndKnots.ew_interface_knot
import QOU.Braiding.fermion_boson_knot_link
import QOU.ParticleInteractions.atomic_lp_stability
import QOU.Archimedean.MassTowerOpenProblemsClasses
import QOU.BraidKnot.spectral_sequence_h3_explicit
import QOU.BraidKnot.terms_2_6_higher_operations
import QOU.BraidKnot.sorting_color_energy
import QOU.BraidKnot.UnstableAtom.decay_channel
import QOU.BraidKnot.schur_weyl_mass_decomposition
import QOU.ParticleInteractions.confinement_frobenius_reciprocity
import QOU.BraidKnot.e_infinity_identifications
import QOU.Hecke.InstanceH2
import QOU.Hecke.MarkovTrace
import QOU.Shared.MarkovTraceClaim
import QOU.BraidsAndKnots.explicit_alpha_k_h4
import QOU.BraidsAndKnots.qmn_recursive_memoized
import QOU.BraidsAndKnots.wedderburn_bratteli_recursion
import QOU.Shared.OperatorSelectionLP
import QOU.BraidsAndKnots.demazure_fiber_markov_trace
import QOU.Shared.ArchimedeanEval
import QOU.Information.toffoli_transfer_matrix
import QOU.BraidKnot.ElectronShell
import QOU.BraidKnot.LevelSufficiency

/-! ## Inhabited with no hypotheses

Each was `unproven` under the generator and is inhabited here.  Note how little
each one costs: the generator's failure was never evidence of difficulty. -/

/-- Every claim is a literal equation the instance is free to satisfy — set
`n_strands := 6` and the "strand-count identity" is `rfl`.  The generator tried
only all-zero and all-one models, which is the whole reason it missed this. -/
example : QOU.BraidsAndKnots.EwInterfaceKnotContext where
  CategoricalObj := Unit
  n_strands := 6
  exp_W := 4
  exp_Z := 6
  exp_H := 8
  claim_i_strand_count := rfl
  claim_ii_ew_carrier_exponents := ⟨rfl, rfl, rfl⟩
  n_adjacent_pair_generators := 2
  n_disjoint_strand_pairs := 3
  claim_iii_bar_self_duality := ⟨rfl, rfl⟩

/-- The fermion/boson ↔ knot/link correspondence holds of `Odd`/`Even`
themselves, so the class asserts nothing about torus knots: `T_2n` is opaque
context data and no field constrains it. -/
example : QOU.Braiding.FermionBosonKnotLinkContext where
  CategoricalObj := Unit
  T_2n := fun _ => Unit
  is_knot := Odd
  is_link := Even
  claim_knot_iff_odd := fun _ _ => Iff.rfl
  claim_link_iff_even := fun _ _ => Iff.rfl
  is_fermion := Odd
  is_boson := Even
  claim_fermion_boson_knot_link := fun _ _ => ⟨Iff.rfl, Iff.rfl⟩

/-- "Bare hydrogen is LP-unstable, the 𝓑₃ dressing stabilises it" is satisfied
by one candidate whose bare volume is `0` and whose dressed volume is `1`.
Both fields are chosen by the instance, so the pair of claims constrains their
*relationship* to nothing. -/
example : QOU.ParticleInteractions.AtomicLPStabilityContext where
  Candidate := Unit
  bareVolume := fun _ => 0
  dressedVolume := fun _ => 1
  normalised := fun _ => True
  bare_unstable := ⟨(), trivial, rfl⟩
  dressed_stable := by rintro ⟨_, _, h⟩; norm_num at h

open QOU.Archimedean.OpenProblems in
/-- The regularised brane-tower sum is "uniformly bounded below the pole" — by
the zero function, with `M = 1 < 1.11`.  This is the q-NS carrier shape exactly:
an existential over a function the instance supplies itself. -/
example : ZHabiroConvergenceClass where
  uniform_bound := by
    refine ⟨fun _ => 0, 1, by norm_num, ?_, fun z _ => by norm_num⟩
    unfold brane_tower_pole; norm_num

/-- Three `Prop`-valued fields with `_holds` witnesses: instantiate each as
`True` and the witnesses are `trivial`.  A `Prop` field with its own proof
field is inhabited by construction — it is `proof-claims-unencoded` wearing a
§3b-cond shape. -/
example : QOU.BraidKnot.SpectralSequenceH3ExplicitContext where
  Z := 1
  N := 0
  n_strands := 3
  claim_strand_count := rfl
  HeckeH3 := Unit
  claim_i_d1_differential := True
  claim_i_d1_differential_holds := trivial
  claim_ii_d2_differential := True
  claim_ii_d2_differential_holds := trivial
  claim_iii_page_identifications_concretised := True
  claim_iii_page_identifications_concretised_holds := trivial

/-- Page indices and Hochschild arities are literals the instance picks. -/
example : QOU.BraidKnot.Terms26HigherOperationsContext where
  CategoricalObj := Unit
  Link := Unit
  HeckeAlgebra := Unit
  target_page_term_2 := 1
  hochschild_arity_term_2 := 2
  claim_term_2_single_generator_brane_tower := ⟨rfl, rfl⟩
  target_page_term_6 := 5
  hochschild_arity_term_6 := 6
  claim_term_6_jet_prefix_correction := ⟨rfl, rfl⟩

/-- The Hecke eigenvalue claim `σ = q on Sym², −q⁻¹ on Λ²` is definitional once
the eigenvalues are context fields: assign them and both conjuncts are `rfl`.
`sigma` itself is never constrained, so nothing here is about a Hecke
generator. -/
example : QOU.BraidKnot.SortingColorEnergyContext ℚ where
  V := Unit
  V_sq := Unit
  Sym2 := Unit
  Wedge2 := Unit
  q := 1
  sigma := id
  sym_eigenvalue := ((1 : ℚˣ) : ℚ)
  wedge_eigenvalue := -(((1 : ℚˣ)⁻¹ : ℚˣ) : ℚ)
  claim_eigenvalues := ⟨rfl, rfl⟩

/-- Uniqueness of the decay channel "off the boundary variety" is vacuous when
the boundary predicate is everything: `on_boundary := fun _ => True` discharges
`claim_ii` by `absurd`, and the phase-crossing existential is witnessed at the
degenerate interval `[0,0]`.  Nothing ties `on_boundary` to the energy `E_λ`. -/
example : QOU.BraidKnot.UnstableAtom.DecayChannelContext where
  Z := 1
  N := 0
  q := 0
  PartitionIdx := Unit
  lam_star := ()
  E_lambda := 1
  claim_i_well_defined := by norm_num
  on_boundary := fun _ => True
  lam_alt := ()
  claim_ii_unique_off_boundary := by intro h; exact absurd trivial h
  q_1 := 0
  q_2 := 0
  claim_iii_phase_boundary_crossing := by
    intro _; exact ⟨0, le_refl 0, le_refl 0, trivial⟩

/-- The Schur–Weyl decomposition `tr_M(𝒜) = Σ_λ s_λ χ_λ / H_q(λ)` holds over
the EMPTY partition set: `partitions` is a context field and no claim requires
it to be the partitions of `3A`, so `Z` and `N` are inert.  The sum identity is
`0 = 0`. -/
example : QOU.BraidKnot.SchurWeylMassContext ℚ 1 0 where
  q := 0
  Partition := Unit
  partitions := ∅
  schurFunction := fun _ => 0
  qHookProduct := fun _ => 1
  chi_atomic := fun _ => 0
  trM_atomic := 0
  qHookProduct_ne_zero := by intro _; norm_num
  claim_schur_weyl_sum := by simp

/-- The "master reciprocity formula" `⟨O⟩_T = Σ_{i,j∈A*} u*ᵢ (G⁻¹)_{ij} ⟨O,bⱼ⟩`
holds when the physical expectation and the Frobenius pairing are both zero —
and both are context fields, so nothing relates them.

Worth noting separately: `strong_duality : primal_obj = dual_obj` is a FIELD,
not a derived fact.  LP strong duality is assumed here, which is consistent with
`HasFiniteLPDuality` elsewhere in the corpus doing the same, and is the honest
reading of what this class provides. -/
example : QOU.ParticleInteractions.ConfinementFrobeniusReciprocityContext where
  d := 1
  G := fun _ _ => 1
  Ginv := fun _ _ => 1
  A_star := Finset.univ
  x_star := fun _ => 1
  u_star := fun _ => 1
  y_0_star := 1
  primal_obj := 0
  dual_obj := 0
  Observable := Unit
  pairing := fun _ _ => 0
  physExp := fun _ => 0
  reciprocity := by intro O; simp
  primal_nontrivial := ⟨0, by norm_num⟩
  y_0_star_pos := by norm_num
  A_star_nonempty := Finset.univ_nonempty
  active_iff_pos_shadow := by
    intro i
    exact ⟨fun _ => by norm_num, fun _ => Finset.mem_univ i⟩
  strong_duality := rfl

/-- All six `E_∞`-page identifications of the unified mass formula hold at zero
pages, zero branes and zero mass.  `n_pages := 0` makes the six-term sum empty,
so the "unified mass formula" claim is `0 = 0 + 0 + 0`; the per-page claims are
`rfl`.  The chirality sign is the one field with real content (`= 1 ∨ = -1`) and
it is satisfied by `1`. -/
example : QOU.BraidKnot.EInfinityIdentificationsContext where
  m_total := 0
  page_pairing := fun _ => 0
  n_pages := 0
  ribbon_closure := 0
  frobenius_co_casimir := 0
  claim_mass_formula_unified := by simp
  trM_T_w_abs := 0
  claim_descended := rfl
  n_branes := 0
  brane_pairing := fun _ => 0
  claim_brane_tower_single := by simp
  brane_pairwise := fun _ _ => 0
  claim_brane_tower_pairwise := by simp
  chirality_sign := 1
  claim_chirality_sign := Or.inl rfl
  claim_wenzl_bridge_correction := True
  claim_wenzl_bridge_correction_holds := trivial

/-! ## The `extends MarkovTraceContext` family, via a degenerate parent

Five of the undecided classes `extends` a shared parent, and the prober skips
them for that reason alone.  They are unlocked by inhabiting the parent —
which, per the header of
[`QOU/Hecke/InstanceH2.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/InstanceH2.lean),
had never been done:

> *"no concrete instance of `QOU.Hecke.HeckeAlgebra` existed anywhere in the
> tree (nor of `QOU.Hecke.MarkovTrace`, nor of
> `QOU.Shared.MarkovTraceContext`)"*

That file supplies the missing piece and names the reason it is easy: its
`rankOneModel` shows `ℚ` itself is a `HeckeAlgebra ℚ n 1 ℚ` **at every `n`**,
because at `q = 1` the Hecke parameter `h = q − q⁻¹` vanishes.  So a hypothesis
`[HeckeAlgebra R n q A]` is far weaker than "`A` is the Hecke algebra" — the
missing axiom being the Iwahori basis (that file's own analysis, bean
`qou-ghak`).

What is added here is the other half: the same rank-one model carries a
**Markov trace**, hence a `MarkovTraceContext`.  Credit for the model is theirs;
this is one step downstream of it. -/

open QOU.Hecke QOU.Hecke.InstanceH2 in
/-- `trace = id`, `z = 1`.  Cyclicity is `mul_comm` in `ℚ`, and both generator
axioms are `rfl` because `embed` is constantly `1`. -/
noncomputable instance rankOneMarkov (n : ℕ) : MarkovTrace n (1 : ℚ) ℚ where
  trace := LinearMap.id
  normalised := rfl
  cyclic := by intro x y; simp [mul_comm]
  z_param := 1
  trace_gen := by intro i; rfl
  trace_prod_gen := by intro i j _; rfl

open QOU.Hecke.InstanceH2 in
/-- **`QOU.Shared.MarkovTraceContext` is inhabited**, at `R = A = ℚ`, `q = 1`.
Every `extends MarkovTraceContext` class in the corpus can be built from this,
so the parent contributes nothing to any of them. -/
noncomputable instance degenerateMarkovTraceContext : QOU.Shared.MarkovTraceContext where
  R := ℚ
  ringR := inferInstance
  invR := inferInstance
  q := 1
  n := 3
  A := ℚ
  ringA := inferInstance
  algebraA := inferInstance
  heckeInst := rankOneModel 3
  markovInst := rankOneMarkov 3

/-- First of the family: `p(4) = 5` conjugacy classes.  The claim is `5 = 5`
and the inherited Markov-trace substrate is the degenerate one above. -/
noncomputable example : QOU.BraidsAndKnots.ExplicitAlphaKH4Context where
  toMarkovTraceContext := degenerateMarkovTraceContext
  n_classes := 5
  claim_explicit_alpha_k_h4 := rfl

/-! ### An elaboration note that costs an hour if you don't know it

`degenerateMarkovTraceContext` must be an `instance`, not a `def` or even a
reducible `abbrev`.  A child class whose field types mention the INHERITED ring
— `chi : ℕ → ℕ → R` — elaborates that `R` as `@MarkovTraceContext.R inst` with
`inst` found by *instance search*, not from the term supplied for
`toMarkovTraceContext`.  With a `def` the search fails and every numeral field
reports `failed to synthesize OfNat QOU.Shared.MarkovTraceContext.R 0`, which
reads like a missing algebraic instance and is really a missing context
instance.  Type-ascribing the numerals does not help; nor does `{ ctx with … }`.

That is why `ExplicitAlphaKH4Context` above went through immediately while the
two below did not: its only field is `n_classes : ℕ`, a type that never mentions
the parent's `R`. -/

/-- Memoised Murnaghan–Nakayama: the cache identity holds when the character
and its recursion are both zero, and the cache invariant holds vacuously with
`cache_get` returning `none` everywhere — so "the stored result is faithful"
constrains nothing when nothing is ever stored. -/
noncomputable example : QOU.BraidsAndKnots.QmnRecursiveMemoizedContext :=
  { degenerateMarkovTraceContext with
    chi := fun _ _ => (0 : ℚ)
    chi_recursion := fun _ _ => (0 : ℚ)
    claim_i_looks_up_cache := fun _ _ => rfl
    claim_ii_miss_computes_via := True
    claim_ii_miss_computes_via_holds := trivial
    cache_get := fun _ _ => (none : Option ℚ)
    claim_iii_stores_result_cache := by intro _ _ v h; simp at h }

/-- Bratteli recursion: per-row monotonicity, sign tracking and the ε-N limit
all hold at the constant-zero ratio with `z_real := 0`.  The limit claim is the
only one with analytic shape and it is satisfied by a constant sequence. -/
noncomputable example : QOU.BraidsAndKnots.WedderburnBratteliRecursionContext :=
  { degenerateMarkovTraceContext with
    y_lambda := fun _ _ => (0 : ℚ)
    ratio := fun _ => 0
    claim_i_per_row_monotonicity := fun _ => le_refl 0
    q_content_sign := fun _ => 0
    claim_ii_sign_tracking_added := by intro _; norm_num
    z_real := 0
    diagonal_ratio_n := fun _ => 0
    claim_iii_trivial_rep_limit := by
      intro ε hε; exact ⟨0, fun n _ => by simpa using hε⟩ }

/-! ### A second parent: `OperatorSelectionLPContext`

Same story one class over.  Note its `strong_duality` is a **field** — as in
`ConfinementFrobeniusReciprocityContext` and `HasFiniteLPDuality` — so LP strong
duality is assumed in a third independent place. -/

noncomputable instance degenerateLPContext : QOU.Shared.OperatorSelectionLPContext where
  n := 0
  d := 0
  n_target := 0
  t := fun _ => 0
  G := fun _ _ => 0
  x_star := fun _ => 0
  y_0_star := 0
  y_star := fun _ => 0
  A_star := ∅
  strong_duality := by simp

/-- Demazure-fibre Markov trace.  `T^Dem(λ; w_0) = y_λ` holds at the constant
`1`; Plancherel completeness `Σ f_λ T^Dem(λ;w_0) = 1` holds over one partition
with `f_λ = 1`.  The Bruhat-order sub-claim is an opaque `Prop` carrying its own
witness, so it is `True`/`trivial` — the same shape as
`SpectralSequenceH3ExplicitContext`. -/
noncomputable example : QOU.BraidsAndKnots.DemazureFiberMarkovTraceContext :=
  { degenerateLPContext with
    T_Dem := fun _ _ => 1
    y_lambda := fun _ => 1
    w_0 := 0
    claim_i_standard_jones_markov := fun _ => rfl
    claim_ii_bruhat_order_structural := True
    claim_ii_bruhat_order_structural_holds := trivial
    f_lambda := fun _ => 1
    n_partitions := 1
    claim_iii_plancherel_completeness := by simp }

/-! ### A third parent: `ArchimedeanEval`, and the last of the `extends` family

`ArchimedeanEval` is `MarkovTraceContext` plus a ring hom `R →+* ℝ`.  Over the
degenerate context (`R = ℚ`, `q = 1`) that is `Rat.castHom ℝ`, so `q_real = 1`
by `rfl`. -/

noncomputable instance degenerateArchimedeanEval : QOU.Shared.ArchimedeanEval :=
  { degenerateMarkovTraceContext with eval := Rat.castHom ℝ }

theorem degenerateArchimedeanEval_q_real :
    QOU.Shared.ArchimedeanEval.q_real degenerateArchimedeanEval = 1 := by
  -- `rfl` alone suffices in a file importing only this instance, but not here:
  -- with the other degenerate contexts in scope the projection does not reduce
  -- definitionally.  Unfolding first is robust either way.
  unfold QOU.Shared.ArchimedeanEval.q_real
  exact map_one (Rat.castHom ℝ)

/-- The Toffoli transfer matrix.  Two of its claims mention the archimedean
`q_real`, and at `q_real = 1` both are satisfied by zero amplitudes: the
classical-limit claim `q_real = 1 → P_flip k = 0` becomes `rfl`, and the
diagonal formula `P₇₇ = (q + √q − 1)/(q + 1)` evaluates to `1/2`.

Worth noting what this shows and does not.  The block's own source already
records (bean `qou-3j5m`) that its sub-claim (i) was REMOVED because the three
target-flip amplitudes it asserted equal are measurably different.  This witness
is about the class that remains: even after that correction, nothing in it ties
`P_flip` to the transfer matrix, so the surviving claims hold of the zero
amplitude. -/
noncomputable example : QOU.Information.ToffoliTransferMatrixContext :=
  { degenerateArchimedeanEval with
    P_flip := fun _ => 0
    c := fun _ => 0
    z_real := 0
    V_hat_1 := fun _ => 0
    d := fun _ => 0
    claim_ii_generator_crossing_traced := by intro k; norm_num
    claim_v_classical_limit := by intro k _; rfl
    P_7_7 := 1/2
    claim_vi_diagonal_formula := by
      rw [degenerateArchimedeanEval_q_real, Real.sqrt_one]; norm_num }

/-! ### The structure-valued bucket, and a distinction it forces

The prober skipped 17 classes because it could not synthesise a value of a repo
structure.  Those structures are plain records: `ConfinedParticle` is a name, a
level and a `MarkovClass`; `MarkovClass` is a strand count and a
`BraidWord n = List (Fin (n-1) × Bool)`, so `[]` serves at every `n`.

**A data-only class is vacuous even though it is parameterised.**  My earlier
correction says inhabiting `C x₀` for one `x₀` shows satisfiability, not vacuity.
That is right when `C` has Prop fields.  `HasMarkovTrace P q` has exactly one
field, `value : R_q`, and no claim at all — so it is inhabited at *every* `P`
and `q` by supplying a value, and `[HasMarkovTrace P q]` assumes nothing
anywhere.  It is a "hand me a value" carrier, not a hypothesis.  Same for
`HasBindingMultiplicity S` (`mu : R_q → ℕ`). -/

namespace HandAdjudicated
open QOU.BraidKnot QOU.Archimedean

/-- A confined particle: a name, a level, and a Markov class. -/
def probeParticle : ConfinedParticle := ⟨"probe", 0, ⟨0, []⟩⟩

/-- An electron shell at the noble-gas count `Z = 2`. -/
def probeShell : ElectronShell :=
  { nucleus := probeParticle, nElectrons := 2, nStrandsTotal := 2,
    cabling := rfl, bindingWord := [] }

/-- No Prop fields: inhabited at every `(P, q)`. -/
noncomputable example : HasMarkovTrace probeParticle 0 where
  value := 0

/-- Likewise no Prop fields. -/
instance probeShellMult : HasBindingMultiplicity probeShell where
  mu := fun _ => 2

/-- **The pair is jointly vacuous, which neither is alone.**
`NobleGasMultiOperator` does carry a claim — `bindingMultiplicity S q ≥ 2` at
noble-gas `Z` — but it constrains the `[HasBindingMultiplicity S]` instance,
and that instance is unconstrained data.  Choosing `mu := fun _ => 2` above
satisfies it, so the two together assert nothing: the claim is real, and the
thing it is a claim *about* is free. -/
noncomputable example : NobleGasMultiOperator probeShell 0 (by decide) where
  multi := by decide

end HandAdjudicated
