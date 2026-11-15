/-
  Categorical Higgs mechanism — conjecture carrier.

  Companion: categorical-higgs-mechanism.md
  Path: folio/quantum-observable-universe/mass-theory/

  The categorical formulation of the Higgs mechanism: Goldstone-eating
  ↔ topological linking of closed-braid representatives.  The open
  inputs are encoded as content-bearing class hypotheses (AGENTS.md
  §3b-tax); the class has **no instance**.

  History (bean `qou-08zf`, 2026-09-03).  Until this revision the file
  carried `MassEigenstateCountThree := True`, `CategoricalMassFormula :=
  True`, a "faithful inlined copy" of `WeinbergAngleCategorical` whose
  four fields were all `True` with a global `instance` closing them by
  `trivial`, and a `mkSkeleton` helper that built a
  `CategoricalHiggsMechanism` out of those trivial instances — i.e. the
  conjecture was inhabited for free.  All of that is replaced by
  predicates that state what the `.md` states.

  The previous revision also inlined `CategoricalLinkingOperation`
  from `mass-theory/categorical-linking-operation.lean`.  That copy is
  **dropped** rather than propagated: the linking input the Higgs
  mechanism actually consumes is the linking number `lk` of the
  post-breaking 2-component links, which is what
  `MassEigenstateCountThree` is stated over.

  (Currency, bean `qou-yt29`, 2026-09-04: this note used to add that the
  source file has "two of whose five fields are `True` there and which
  that file closes with a global `instance canonical`".  That is no
  longer its state, and the count was low besides — all **five**
  predicates were extensionally `True`, three of them disguised as ring
  or integer identities.  The source now carries a `LinkingData`
  substrate, proves Properties 1-2 and the pre-trace half of 3 about the
  operation itself, states the rest as class fields, and has no
  instance.)

  Standalone-compile note: a content-block `.lean` sibling cannot
  `import` other content-block siblings, so `EWHoefsmitData` and
  `WeinbergAngleCategorical` are reproduced below as a FAITHFUL inlined
  copy of `nuclear-interactions/weinberg-angle-categorical.lean` (same
  fields, same docstrings, same absence of an instance).

  Refs:
    [kassel1995] Kassel, "Quantum Groups," Springer 1995, §XIV.
    [jones1987] Jones, Ann. Math. 126 (1987) — the Markov trace.
    docs/audits/2026-05-05-path-alpha-bring-refinement.md
-/

import Mathlib.Algebra.Algebra.Basic
import Mathlib.Data.Fintype.Card
import Mathlib.Tactic.DeriveFintype

namespace QOU.BraidsAndKnots

/-- Predicate: `q : R` is a root of unity in `R` (used to state the
    generic-`q` hypothesis as `¬ IsRootOfUnityH q`). -/
def IsRootOfUnityH {R : Type*} [Monoid R] (q : R) : Prop :=
  ∃ n : ℕ, n > 0 ∧ q ^ n = 1

/-! ## The electroweak boson set and the two linking predicates -/

/-- The four electroweak gauge bosons of the `.md`: pre-breaking each is
    a 1-component knot; post-breaking three of them fuse with a Goldstone
    boson into a 2-component link and the photon survives as a knot. -/
inductive EWBoson
  | Wplus
  | Wminus
  | Z
  | photon
  deriving DecidableEq, Fintype

/-- **Three broken generators, as a linking statement** (`.md` §2–3).
    Given the linking number `lk` of each post-breaking boson's
    closed-braid representative with its eaten Goldstone component,
    exactly three bosons carry `lk = 1` (the broken-generator
    multiplicity) and the photon carries `lk = 0` (unbroken, still a
    1-component knot).  Content-bearing: false for most `lk`. -/
def MassEigenstateCountThree (lk : EWBoson → ℤ) : Prop :=
  (Finset.univ.filter fun b => lk b = 1).card = 3 ∧ lk EWBoson.photon = 0

/-- **The categorical mass formula** (`.md` §4): the mass of each
    post-breaking boson `X` is the Markov trace of its new 2-component
    link `β X`, sandwiched by the appropriate Hoefsmit projector `e X`,
    up to the overall scale `scale` (the crossing energy `E_×·μ₀`,
    which this block does not derive):

        m_X = scale · tr_M(e_X · β_X · e_X). -/
def CategoricalMassFormula {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]
    (trM : A →ₗ[R] R) (e β : EWBoson → A) (scale : R) (m : EWBoson → R) : Prop :=
  ∀ X, m X = scale * trM (e X * β X * e X)

/-- **The three linked bosons are exactly the non-photons.**  A genuine
    (if small) consequence of `MassEigenstateCountThree`: the filter
    `{b | lk b = 1}` has three elements and omits the photon, and there
    are four bosons, so it is `univ \ {photon}`. -/
theorem linked_iff_ne_photon (lk : EWBoson → ℤ) (h : MassEigenstateCountThree lk) :
    ∀ b, lk b = 1 ↔ b ≠ EWBoson.photon := by
  obtain ⟨hcard, hγ⟩ := h
  have hsub : (Finset.univ.filter fun b => lk b = 1) ⊆ Finset.univ.erase EWBoson.photon := by
    intro b hb
    rw [Finset.mem_filter] at hb
    rw [Finset.mem_erase]
    refine ⟨?_, Finset.mem_univ _⟩
    rintro rfl
    rw [hγ] at hb
    exact zero_ne_one hb.2
  have hcard' : (Finset.univ.erase EWBoson.photon).card = 3 := by decide
  have heq : (Finset.univ.filter fun b => lk b = 1) = Finset.univ.erase EWBoson.photon :=
    Finset.eq_of_subset_of_card_le hsub (by rw [hcard, hcard'])
  intro b
  constructor
  · intro hb
    rintro rfl
    rw [hγ] at hb
    exact zero_ne_one hb
  · intro hb
    have hmem : b ∈ Finset.univ.erase EWBoson.photon :=
      Finset.mem_erase.mpr ⟨hb, Finset.mem_univ _⟩
    rw [← heq, Finset.mem_filter] at hmem
    exact hmem.2

/-! ## FAITHFUL inlined copy of `EWHoefsmitData` / `WeinbergAngleCategorical`
   (source: nuclear-interactions/weinberg-angle-categorical.lean).
   Same fields, same docstrings; no instance there, none here. -/

/-- **The Hecke-eigenvalue data of the electroweak triplet at `n = 6`**
    (inlined copy — see the source file for the full docstring). -/
structure EWHoefsmitData (R : Type*) [CommRing R] (A : Type*) [Ring A] [Algebra R A] where
  /-- The Markov trace `tr_M : A → R` (an `R`-linear functional). -/
  trM : A →ₗ[R] R
  /-- Hoefsmit idempotent `e_W⁺` — symmetric channel of the `W` slot. -/
  eW : A
  /-- Hoefsmit idempotent `e_B⁺` — symmetric channel of the pre-EWSB `B` slot. -/
  eB : A
  /-- Braid generator `σ₁` (the `W` slot carries `σ₁⁴`). -/
  σ₁ : A
  /-- Braid generator `σ₅` (the `H`/pre-mixing `B` slot carries `σ₅⁸`). -/
  σ₅ : A

namespace EWHoefsmitData

variable {R : Type*} [CommRing R] {A : Type*} [Ring A] [Algebra R A]

/-- `tr_M(e_W⁺ · σ₁⁴)` — the `W`-slot trace scalar. -/
def trW (d : EWHoefsmitData R A) : R := d.trM (d.eW * d.σ₁ ^ 4)

/-- `tr_M(e_B⁺ · σ₅⁸)` — the pre-EWSB `B`-slot trace scalar. -/
def trB (d : EWHoefsmitData R A) : R := d.trM (d.eB * d.σ₅ ^ 8)

end EWHoefsmitData

/-- **Conjecture carrier (primary, content-bearing, NO instance)** —
    inlined copy of `conj:weinberg-angle-categorical`'s class; the
    identification `cot θ_W · tr_M(e_B⁺σ₅⁸) = tr_M(e_W⁺σ₁⁴)` over genuine
    Hecke data.  Tower status: ORDER-ZERO-ONLY (single ratio at `n = 6`). -/
-- Ref: [leitner2026] conj:weinberg-angle-categorical
-- Ref: [jones1987] https://doi.org/10.2307/1971403
class WeinbergAngleCategorical
    (R : Type*) [Field R] (q : R)
    (A : Type*) [Ring A] [Algebra R A]
    (d : EWHoefsmitData R A) (cotW : R) : Prop where
  /-- Markov-trace cyclicity `tr_M(ab) = tr_M(ba)`. -/
  trM_cyclic : ∀ a b : A, d.trM (a * b) = d.trM (b * a)
  /-- Hoefsmit cell content: `e_W⁺` is a projector. -/
  eW_idem : d.eW * d.eW = d.eW
  /-- Hoefsmit cell content: `e_B⁺` is a projector. -/
  eB_idem : d.eB * d.eB = d.eB
  /-- Hecke relation `σ₁² = (q − q⁻¹) σ₁ + 1`. -/
  hecke_σ₁ : d.σ₁ ^ 2 = algebraMap R A (q - q⁻¹) * d.σ₁ + 1
  /-- Hecke relation `σ₅² = (q − q⁻¹) σ₅ + 1`. -/
  hecke_σ₅ : d.σ₅ ^ 2 = algebraMap R A (q - q⁻¹) * d.σ₅ + 1
  /-- The `B`-slot scalar is non-zero, so the ratio is defined. -/
  trB_ne_zero : d.trB ≠ 0
  /-- **The identification — the conjecture's claim.** -/
  cot_identification : cotW * d.trB = d.trW

/-! ## The categorical Higgs-mechanism conjecture -/

/-- **Conjecture carrier (dependent on `WeinbergAngleCategorical`; NO
    instance).**  `CategoricalHiggsMechanism R q A d cotW lk e β scale m`
    packages the inputs the `.md` names, each as a genuine constraint:

    * `[WeinbergAngleCategorical R q A d cotW]` — the upstream conjecture,
      taken as an explicit instance binder: that binder **is** the
      dependency edge (§3b-tax), so this carrier is classified *dependent*
      by the vacuity audit's conjecture graph, matching the block's
      `uses: ["conj:weinberg-angle-categorical"]`;
    * `q_generic` — the substrate parameter is not a root of unity;
    * `mass_eigenstate_count` — three bosons fuse with a Goldstone into a
      2-component link with `lk = 1`; the photon does not;
    * `mass_formula` — each mass is the Hoefsmit-projected Markov trace of
      its post-breaking link;
    * `photon_massless` — the unbroken photon's link is trivial, so its
      mass vanishes: the Markov trace of the surviving 1-component knot
      sandwiched by its projector is `0` in the mass channel.

    **Tower status (owner ruling 2026-09-03): ORDER-ZERO-ONLY** — one
    Hoefsmit projection per boson at fixed `n`; the full `H_n(q)` tower
    is not used.

    No instance: constructing the Goldstone-eating linking and the
    post-breaking Markov traces from the substrate is the open content
    of `conj:categorical-higgs-mechanism` (Steps A–D of the `.md`). -/
-- Ref: [leitner2026] conj:categorical-higgs-mechanism
-- Ref: [kassel1995] §XIV (ribbon-category braiding; linking of closed braids)
class CategoricalHiggsMechanism
    (R : Type*) [Field R] (q : R)
    (A : Type*) [Ring A] [Algebra R A]
    (d : EWHoefsmitData R A) (cotW : R)
    [WeinbergAngleCategorical R q A d cotW]
    (lk : EWBoson → ℤ) (e β : EWBoson → A) (scale : R) (m : EWBoson → R) : Prop where
  /-- Generic-`q` hypothesis: `q` is NOT a root of unity in `R`. -/
  q_generic : ¬ IsRootOfUnityH q
  /-- Three broken generators: three `lk = 1` links, photon unlinked. -/
  mass_eigenstate_count : MassEigenstateCountThree lk
  /-- Mass = Hoefsmit-projected Markov trace of the post-breaking link. -/
  mass_formula : CategoricalMassFormula d.trM e β scale m
  /-- The unbroken photon is massless. -/
  photon_massless : m EWBoson.photon = 0

/-- **Conditional consequence (§3b-cond).**  *If* the categorical Higgs
    mechanism holds, then the photon's Hoefsmit-projected Markov trace
    vanishes whenever the scale is non-zero — derived from `mass_formula`
    and `photon_massless`, not read off a field. -/
theorem photon_projected_trace_eq_zero
    {R : Type*} [Field R] {q : R} {A : Type*} [Ring A] [Algebra R A]
    {d : EWHoefsmitData R A} {cotW : R} [WeinbergAngleCategorical R q A d cotW]
    {lk : EWBoson → ℤ} {e β : EWBoson → A} {scale : R} {m : EWBoson → R}
    [inst : CategoricalHiggsMechanism R q A d cotW lk e β scale m]
    (hscale : scale ≠ 0) :
    d.trM (e EWBoson.photon * β EWBoson.photon * e EWBoson.photon) = 0 := by
  have h := inst.mass_formula EWBoson.photon
  rw [inst.photon_massless] at h
  rcases mul_eq_zero.mp h.symm with h0 | h0
  · exact absurd h0 hscale
  · exact h0

/-- **Conditional consequence (§3b-cond).**  *If* the categorical Higgs
    mechanism holds, the linked bosons are exactly `W⁺, W⁻, Z`. -/
theorem linked_iff_ne_photon_of_higgs
    {R : Type*} [Field R] {q : R} {A : Type*} [Ring A] [Algebra R A]
    {d : EWHoefsmitData R A} {cotW : R} [WeinbergAngleCategorical R q A d cotW]
    {lk : EWBoson → ℤ} {e β : EWBoson → A} {scale : R} {m : EWBoson → R}
    [inst : CategoricalHiggsMechanism R q A d cotW lk e β scale m] :
    ∀ b, lk b = 1 ↔ b ≠ EWBoson.photon :=
  linked_iff_ne_photon lk inst.mass_eigenstate_count

end QOU.BraidsAndKnots
