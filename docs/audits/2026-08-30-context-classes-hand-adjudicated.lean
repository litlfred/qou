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
