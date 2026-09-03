/-
  Bean `qou-z9ws` — the gate for the self-assuming-projection REMAINDER.

  WHAT THIS FILE ESTABLISHES, AND WHY IT MATTERS

  The self-assuming-projection drain ended at **90 genuine** findings, and the
  sizing audit
  [`2026-08-30-sizing-the-self-assuming-projection-drain.md`](2026-08-30-sizing-the-self-assuming-projection-drain.md)
  recorded the remainder as week-shaped on this reasoning:

  > *"Constructing a witness means supplying the mathematics the context class
  > was standing in for.  For many of these — `KnotOperatorSelectionContext`,
  > `HoefsmitScatteringPipelineContext`, `NucleonOrderingFactorizationContext`
  > — that IS the open research, not a formalisation chore."*

  **That was asserted, never measured, and for `KnotOperatorSelectionContext`
  it is false.**  The witnesses below inhabit five of these classes with `Unit`
  and zero, no hypotheses of any kind.  A class inhabited that cheaply
  constrains nothing, so a `[C]` binder on it assumes nothing and the
  downstream `[C]`-conditional declaration is not conditional on anything.

  This is the same defect the q-NS carriers in `ConditionalClasses.lean` had
  before 2026-08-30 — every field an existential over data the instance itself
  picked — and it is caught the same way, by asking what the class RULES OUT
  rather than by asking whether it compiles.  See
  [`2026-08-30-qns-carriers-are-refutable.lean`](2026-08-30-qns-carriers-are-refutable.lean)
  for the refutability half.

  🛑 INHABITED DOES NOT MEAN THE BLOCK IS BAD.  State this narrowly or the
  finding over-reaches.  A class may legitimately NAME a modelled object and
  its defining law, with the real work downstream.  `BorromeanQuark`
  (`brings-surface/orbital-fourier-decomposition.lean`) is the worked
  counter-example: it carries `orbitalDim n = Σ_{ℓ<n} modeSpaceDim ℓ` as its
  single modelling input and the file then DERIVES `orbital_dim_eq_square :
  Σ_{ℓ<n} modeSpaceDim ℓ = n²` unconditionally.  It is inhabitable — by the
  corpus's own theorem — and that is correct, not a defect.

  The discriminator is what the downstream declaration DOES with the field:

    - DERIVES something from it   -> §3b-cond working as intended (BorromeanQuark);
    - PROJECTS it verbatim        -> §3b-cond item 5, and if the class is also
                                     inhabited by zero then the declaration is
                                     conditional on nothing and states nothing.

  All five classes below are of the second kind.

  A SECOND, DIFFERENT FINDING — `Term7ShellCorrectionClass`.  Not vacuous:
  PROVABLE.  Its field is `∃ a, a < 0 ∧ a = alpha5_value`, and
  `alpha5_value : ℝ := -1` is a literal, so the class asserts `-1 < 0` and
  `norm_num` discharges it.  Carrying a proved fact as a class hypothesis is
  harmless in itself; what makes it a finding is that the source's own comment
  on that literal reads *"sign-constraint witness; magnitude awaits
  derivation"* — so the genuinely open part, the MAGNITUDE, is encoded
  nowhere, while the part that is encoded is a theorem.  That is the
  `proof-claims-unencoded` shape, not the self-assuming-projection one.

  THE MACHINE VERSION.  These six were done by hand; the sweep is
  [`scripts/lean-context-class-inhabitation-probe.py`](../../scripts/lean-context-class-inhabitation-probe.py),
  whose `--selftest` pins exactly the five inhabitation witnesses below.  That
  guard is load-bearing: the script's first version found only TWO of the five,
  because it could not resolve a field whose type was another field of the same
  class (`mass : CategoricalObj → ℝ`) and so read `Finset Partition` as `∅`,
  turning a satisfiable `Σ w = 1` into `0 = 1`.  Both misses were reported as
  `unproven`/`skipped` — i.e. as "no finding" — which is how a detector reports
  a tree it never looked at.  Hence: a PASS is decisive, a FAILURE is
  inconclusive, and the sweep's count is a LOWER BOUND that must never be
  complemented into a count of contentful classes.

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build` — a build
  against a restored cache with `traces=0` evicts it):

      LEAN_PATH=<mathlib libs>:<QOU build lib> \
        lean docs/audits/2026-08-30-context-classes-are-inhabited-by-zero.lean

  Measured 2026-08-30: exit 0, 0 errors.
-/
import QOU.BraidKnot.six_term_mass_formula_complete
import QOU.BraidKnot.jet_prefix_gb_filtration
import QOU.Braiding.reidemeister_mass_invariance
import QOU.Braiding.r_matrix_braiding_structure
import QOU.BraidKnot.knot_factor_spectral_derivation
import QOU.Archimedean.MassTowerOpenProblemsClasses

/-! ## Inhabited with no hypotheses — the gate -/

/-- The six-term mass decomposition `𝔪(ϱ) = Σ term_i` holds of six zeros. -/
example : QOU.BraidKnot.SixTermMassFormulaContext ℕ where
  term1 := 0; term2 := 0; term3 := 0; term4 := 0; term5 := 0; term6 := 0
  cat_mass := 0
  claim_six_term_sum := by norm_num

/-- `JetOrder = GbDepth` holds of `0 = 0`. -/
example : QOU.BraidKnot.JetPrefixGbFiltrationContext where
  CategoricalObj := Unit
  JetOrder := 0
  GbDepth := 0
  claim_jet_prefix_eq_gb_depth := rfl

/-! **`ReidemeisterMassInvarianceContext` — witness removed 2026-08-31 with its
subject.**  The class and its projection were gutted from
`QOU/Braiding/reidemeister_mass_invariance.lean` (0 importers; the block
resolves to its substantive sibling per AGENTS.md §0a).  The finding stands as
recorded: `CategoricalObj := Unit`, `mass := fun _ => 0`, all three moves
`id`, discharged `claim_reidemeister_mass_invariance` by `rfl` — so the binder
assumed nothing.  It cannot be re-run, because the class is gone; unlike the
`R`-matrix case below, the finding lived entirely in the class's own shape and
has no statement to survive into. -/

/-- Deliberately NOT the trivial model: a *commutative* one, where the
Yang–Baxter equation holds by `mul_comm`.  So `[RMatrixBraidingContext]`
assumes nothing specific to a quantum `R`-matrix — anything commutative
satisfies it.  The file's own docstring already says the converse half
correctly ("YBE fails for a general assignment, so it may not be strengthened
to a global `axiom`"); both are true and they are different facts.

**Witness restated 2026-08-31.**  `RMatrixBraidingContext` was removed with the
rest of `QOU/Braiding/r_matrix_braiding_structure.lean` (0 importers), and the
content-block sibling now *names* the Yang–Baxter equation as
`YangBaxterHolds comp R12 R13 R23` instead of asserting it.  The measurement
below is the same one, spelled out without the class, so the evidence survives
its subject: at `V3 := ℕ`, `comp := (· * ·)`, `R12 := 2`, `R13 := 3`,
`R23 := 5`, the equation `comp (comp R12 R13) R23 = comp (comp R23 R13) R12`
holds by `ring`. -/
example : (2 * 3 : ℕ) * 5 = (5 * 3) * 2 := by ring

/-- One partition carrying weight `1` and unit character.  Note this one needs
the all-ONE model, not the all-zero one: `Σ_λ w_λ = 1` rejects all-zero.  That
is why the prober tries both before reporting, and why a single-model prober
would have called this class contentful. -/
example : QOU.BraidKnot.KnotFactorSpectralContext 3 where
  q := 1
  Partition := Unit
  partitions := Finset.univ
  plancherelWeight := fun _ => 1
  chi_beta := fun _ => 0
  chi_beta_mirror := fun _ => 0
  chi_one := fun _ => 1
  chi_one_ne_zero := by intro _; norm_num
  knotFactor := 0
  claim_plancherel_sum_one := by simp
  claim_knot_factor_spectral := by simp

/-! ## Not vacuous — provable.  A different finding. -/

open QOU.Archimedean.OpenProblems in
/-- `alpha5_value` is the literal `-1`, so this class asserts `-1 < 0`. -/
example : Term7ShellCorrectionClass where
  alpha5_derived := ⟨-1, by norm_num, by unfold alpha5_value; norm_num⟩

open QOU.Archimedean.OpenProblems in
/-- The same content with no class in sight: it is a theorem, so a
`[Term7ShellCorrectionClass]` binder downstream assumes nothing that is not
already proved.  The open item — the *magnitude* of `α₅`, per the source's own
comment on the literal — is not encoded by this class at all. -/
example : ∃ a : ℝ, a < 0 ∧ a = alpha5_value :=
  ⟨-1, by norm_num, by unfold alpha5_value; norm_num⟩
