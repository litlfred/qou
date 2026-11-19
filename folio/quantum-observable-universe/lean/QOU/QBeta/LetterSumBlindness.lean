/-
  Letter-sum blindness, and the exact scope of that exclusion.

  Formalises the structural assertions of
  `computations/qbeta/qbeta_embedding_energy_can_discriminate_probe.py` (5/5)
  and `computations/qbeta/qbeta_bring_ohara_bridge_probe.py` (7/7), and --
  equally important -- DELIMITS them, so the exclusion is not later cited
  against a route it does not reach.

  THE SETTING, stated for a reader who was not in the session. The canonical
  nucleon is an 11-letter braid word `w = 𝓑₃ · Δ₃(flavour) · G`, where `G` is a
  gluon dressing. Four 2-letter candidates for `G` exist:

      σ₁σ₀ ,  σ₀σ₁ ,  σ₁σ₁ ,  σ₀σ₀

  All four have writhe +2 on 3 strands. Measured (the probes above), their
  Markov traces at `z_D = q³/(q²+1)` are four DISTINCT values: in particular
  `σ₁σ₀` and `σ₀σ₁` have the same letter multiset and the same writhe and
  still differ, by `0.0678` (proton) and `0.0142` (neutron). So the closure is
  ORDER-SENSITIVE.

  THE EXCLUSION (§1-§2). A functional that sums something over the letters is
  invariant under permuting them. The closure is not. So no letter-sum can
  select among these candidates -- for any `q`, any coefficients, any ring.
  This is a scope-(b) STRUCTURAL exclusion with a named invariant
  (permutation-invariance of a list sum), not a scope-(a) numerical negative,
  and it kills two concrete proposals at once:

    * crossing COUNT (the word length), and
    * crossing ENERGY `E_cross` (`def:crossing-energy`: `+q` per positive
      crossing, `-1/q` per negative) -- a sum over letters.

  §3 generalises it: any selector that FACTORS THROUGH a class map is blind
  to everything the class forgets. The Bring→O'Hara bridge is of this shape:
  it sends a word to its cusp-torus lattice class `(m, ℓ) = (writhe, strands)`
  and then the class to an energy. So it inherits the blindness -- and it does
  so for EVERY modulus `τ`, because the modulus enters only in the second
  factor, which is universally quantified in `factorsThrough_blind_forall`.
  The O'Hara energy is innocent; the cusp-torus embedding is the lossy step.

  🛑 §4 IS THE PART THAT MUST NOT BE DROPPED WHEN THIS FILE IS CITED.

  The exclusion above is about a selector that factors through a class map.
  It says NOTHING about a selector whose feasible set depends on the word.
  `objective_blindness_does_not_transfer_to_constrained_optimum` exhibits a
  constrained optimisation whose OBJECTIVE is completely class-blind and
  whose optimal VALUE still separates two words in the same class -- because
  the constraints see the word.

  That is not an idle generality. The corpus's operator-selection LP/SDP
  (`prop:operator-selection-lp`, `pyhecke.lp_dual_solver`) has exactly that
  shape:

      min Σ tᵢ xᵢ   s.t.  Σ xᵢ = n_target,  G x ≥ 0,  xᵢ ≥ -M

  with `G` the Frobenius/Gram matrix -- Hecke-derived and order-sensitive --
  and `t` a free cost vector. Putting a geometric (embedding) energy into `t`
  while the Hecke data supplies `G` is therefore NOT excluded by anything in
  §1-§3, even though that same energy is excluded as a standalone selector.
  Anyone citing this file to rule that route out is over-reading it.

  What §4 does NOT claim: that such an optimum WOULD separate the four
  candidates. §4 establishes only that the exclusion does not reach the route
  -- a prune says what is not forbidden, never what works.

  🛑 A CORRECTION TO THIS FILE'S OWN FIRST DRAFT, which said "`t` is indexed by
  Wedderburn block `λ ⊢ n` while the O'Hara energy is indexed by lattice class,
  and no map between those index sets is in the corpus". THAT WAS WRONG, and it
  was a corpus-grep miss rather than a measurement. `QOU/MobiusEnergy.lean`
  (`prop:mobius-energy`) defines the categorical Möbius energy as

      E_cat(γ) = λ ∘ tr_A ∬ (Δ(γ(s)) ⊗ Δ(γ(t))) ⋆_q ‖dγ/ds ∧_q dγ/dt‖ ds dt

  with `λ` the FROBENIUS FORM and `tr_A` the ALGEBRA TRACE. That composite is
  the object the canonical chain decomposes as `tr_M = Σ_λ y_λ χ_λ`, so the
  categorical energy IS a sum over partition representations -- the
  non-abelian Stokes step being what puts the `S¹ × S¹` double integral into
  `H_n(q)` so that Wedderburn can split it. The per-block pieces are exactly
  the `t_λ` the route needs, and the index mismatch asserted above does not
  exist.

  Two things do stand in the way, and neither is an index mismatch:

  * It is SPECIFIED, NOT IMPLEMENTED. The formula lives in a docstring. In the
    Lean, `energy : ℝ` is a bare structure FIELD; nothing computes the double
    integral and nothing computes `χ_λ` of the resulting element.
  * The classical-limit leg is ASSUMED and has a recorded blindness incident.
    `classicalLimit : energy = (1/4) · classicalEnergy.value + const` is a
    structure field, not a theorem, and that file's own header records a case
    where it made `E_cat` blind -- `E_cat = 1 + const` for EVERY knot, with no
    `sorry` and seen by no detector. Check that leg before building on it
    (bean `qou-pzsi` carries the same warning).

  Sorry-free. No `axiom`, no conditional class, no `native_decide`.

  -- Ref: [leitner2026] computations/qbeta/qbeta_embedding_energy_can_discriminate_probe.py
  -- Ref: [leitner2026] computations/qbeta/qbeta_bring_ohara_bridge_probe.py
  -- Ref: [leitner2026] tools/pyhecke/python/pyhecke/lp_dual_solver.py
  -- Ref: [leitner2026] .beans/qou-99qc , .beans/qou-pzsi , .beans/qou-ales
-/
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Data.List.Perm.Basic
import Mathlib.Tactic.NormNum

namespace QOU.QBeta.LetterSumBlindness

/-! ### 1. A letter-sum is permutation-invariant -/

/-- **Any sum over letters is invariant under reordering them.**

`f` is an arbitrary per-letter weight into an arbitrary commutative monoid:
the crossing count (`f ≡ 1`), the crossing energy (`f` = `+q` or `-1/q` by
sign), the writhe (`f` = `±1`), a `q`-dependent weight, anything. The
conclusion is the same for all of them. -/
theorem letterSum_perm_invariant {α β : Type*} [AddCommMonoid β] (f : α → β)
    {l l' : List α} (h : l.Perm l') :
    (l.map f).sum = (l'.map f).sum :=
  (h.map f).sum_eq

/-- **No letter-sum functional separates two words that are reorderings of
each other.** The contrapositive form, which is how the exclusion is used:
if a selector is defined by summing a weight over the letters, then it takes
the same value on `σ₁σ₀` and `σ₀σ₁`, whose closures are measurably
different links. -/
theorem no_letterSum_separates {α β γ : Type*} [AddCommMonoid β]
    (f : α → β) (g : β → γ) {l l' : List α} (h : l.Perm l') :
    g ((l.map f).sum) = g ((l'.map f).sum) := by
  rw [letterSum_perm_invariant f h]

/-! ### 2. The two concrete casualties -/

/-- Crossing COUNT is a letter-sum (with `f ≡ 1`), hence permutation-blind.
This is the invariant behind the owner's objection that the selection rule
should not be minimum crossing number. -/
theorem crossingCount_perm_blind {α : Type*} {l l' : List α} (h : l.Perm l') :
    l.length = l'.length := by
  simpa using letterSum_perm_invariant (fun _ : α => (1 : ℕ)) h

/-- Crossing ENERGY is a letter-sum (with `f` the per-crossing weight `+q` or
`-1/q`), hence permutation-blind by the same invariant. Stated over a generic
commutative ring so it is a fact about the SHAPE of the functional, not about
the particular values `q` and `-1/q`. -/
theorem crossingEnergy_perm_blind {α R : Type*} [CommRing R] (weight : α → R)
    {l l' : List α} (h : l.Perm l') :
    (l.map weight).sum = (l'.map weight).sum :=
  letterSum_perm_invariant weight h

/-! ### 3. The general form: a selector that factors through a class map is
blind to whatever the class forgets -/

/-- **Factoring through a class map is blindness.**

`cls` is the lossy step (for the Bring→O'Hara bridge: word ↦ lattice class
`(m, ℓ) = (writhe, strands)`); `energy` is anything computed downstream of it.
Two words with the same class get the same value. -/
theorem factorsThrough_blind {W C E : Type*} (cls : W → C) (energy : C → E)
    {w w' : W} (h : cls w = cls w') :
    energy (cls w) = energy (cls w') := by
  rw [h]

/-- **No choice of downstream function repairs it — in particular, no
modulus.**

In the bridge, the cusp modulus `τ` enters only when the lattice class is
turned into a geodesic and the geodesic into an energy, i.e. entirely inside
`energy`. Universally quantifying over `energy` therefore says: deforming `τ`
— to the Neumann-Zagier deformed cusp shape, or to anything else, inside that
family or outside it — cannot separate two words that already share a class.

This is the Lean form of the probe's `no_modulus_can_fix_the_bridge_order_blindness`,
and it is strictly stronger than the numerical statement: it quantifies over
all moduli rather than sampling three. -/
theorem factorsThrough_blind_forall {W C E : Type*} (cls : W → C)
    {w w' : W} (h : cls w = cls w') :
    ∀ energy : C → E, energy (cls w) = energy (cls w') :=
  fun energy => factorsThrough_blind cls energy h

/-- The lattice class used by the bridge is itself letter-sum-type in its
first coordinate (`m` = exponent sum) and constant in its second (`ℓ` = strand
count), so it is permutation-blind — which is what puts the bridge in the
scope of §3 in the first place. -/
theorem bridgeClass_perm_blind {α : Type*} (exponent : α → ℤ) (strands : ℕ)
    {l l' : List α} (h : l.Perm l') :
    ((l.map exponent).sum, strands) = ((l'.map exponent).sum, strands) := by
  rw [letterSum_perm_invariant exponent h]

/-! ### 4. 🛑 THE SCOPE. A class-blind OBJECTIVE over a word-dependent
FEASIBLE SET is not blind -/

/-- **The exclusion does not reach a constrained optimum whose constraints
see the word.**

Exhibited concretely: an objective that cannot see the word at all (`obj`
takes only a point of `X`), two words in the SAME class (`cls` is constant),
and yet two different optimal values — because the feasible sets differ.

This is why §1–§3 do not rule out using an embedding energy as the COST
VECTOR `t` of the operator-selection LP/SDP while the Hecke Gram matrix `G`
supplies the constraints. The four gluon candidates have different Markov
traces, hence different `G`, hence different feasible sets; minimising even a
completely class-blind objective over four different feasible sets can give
four different answers.

Read this as a prune that does NOT fire, not as a positive result. It says
the route is not excluded. It does not say the route works, and it does not
supply the per-block geometric cost `t_λ` that the route would need. -/
theorem objective_blindness_does_not_transfer_to_constrained_optimum :
    ∃ (W X : Type) (cls : W → Unit) (feasible : W → X → Prop) (obj : X → ℕ)
      (w w' : W) (a a' : X),
      cls w = cls w' ∧
      feasible w a ∧ feasible w' a' ∧
      (∀ x, feasible w x → obj a ≤ obj x) ∧
      (∀ x, feasible w' x → obj a' ≤ obj x) ∧
      obj a ≠ obj a' := by
  refine ⟨Bool, ℕ, fun _ => (), fun b x => x = cond b 0 1, id,
          true, false, 0, 1, rfl, rfl, rfl, ?_, ?_, by decide⟩
  · intro x _
    exact Nat.zero_le x
  · intro x hx
    exact le_of_eq hx.symm

end QOU.QBeta.LetterSumBlindness
