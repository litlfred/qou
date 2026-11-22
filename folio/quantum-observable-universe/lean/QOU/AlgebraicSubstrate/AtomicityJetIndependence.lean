/-
# Atomicity is INDEPENDENT of the jet-compatibility ordering axioms —
# route-1 closure of the PlanckStepAtomicity upgrade question

The atomicity audit
(`docs/audits/2026-07-25-planck-step-atomicity-formalization.md` §3/§6)
named two candidate routes for upgrading `PlanckStepAtomicity` from
PREMISE (§3b-tax primary conjecture, no instance) to THEOREM. Route 1:
derive rank-one-ness of the substrate computation monoid from the
jet-tower ordering structure (`prop:ordering-jet-compatibility`). This
file closes route 1 **honestly negative**, with a Lean-proved
independence witness.

## The jet-compatibility axiom set, abstractly extracted

`prop:ordering-jet-compatibility` (block Lean: `QOU.Torsion`, file
`lifting-and-descent/ordering-jet-compatibility.lean`) asserts four
legs about the braiding-induced ordering on the jet tower:

1. **Extension** — each level's ordering extends the previous
   (`axiom ordering_extends`; in the block Lean this is literally
   tautological — one global `degLex` restricted to levels);
2. **Compatibility** — translation invariance under multiplication
   (`axiom ordering_compatible`);
3. **Well-foundedness** — no infinite descending chains
   (`theorem wellfounded_at_level`, proved);
4. **Direct limit** — every element lives at a finite level, reduction
   terminates (`axiom direct_limit_terminates`).

As literally formalized those axioms live on the fixed monomial carrier
`MonomialBasis = List ℕ` and say NOTHING about an abstract computation
monoid — there is no Lean bridge from `QOU.Torsion` to the
`SubstrateClock` monoid `M`. The charitable strongest structural
reading — the only reading under which route 1 could work at all — is
the abstract shape `JetCompatibleOrder` below: an additive computation
monoid carrying a well-founded, translation-invariant ordering together
with an exhaustive increasing tower of submonoid levels (the jet
filtration), each level's ordering extending the previous.

## The decisive test — a rank-2 model satisfying ALL the axioms

`rankTwoJetOrder` equips the rank-two step monoid `ℕ × ℕ` with a
degree-lexicographic order `degLexPair` (the exact analogue of the
corpus `degLex`: compare total degree first, then the second — "jet" —
coordinate) and the alphabet filtration in which the second generator is
the level-1 jet-prolongation direction, ordered after the first. Every
`JetCompatibleOrder` field is proved, sorry-free. Since
`atomicity_fails_for_two_generators` (PlanckStepAtomicity.lean) proves
`ℕ × ℕ` is NOT atomic, the implication "jet-compatible order ⇒
atomicity" is REFUTED (`planckStepAtomicity_not_forced_by_jet_order`).
Conversely `ℕ` with its usual order is a jet-compatible order on an
atomic monoid (`rankOneJetOrder`, `nat_is_atomic`), so the axiom set
does not refute atomicity either: atomicity is INDEPENDENT of the
jet-compatibility axiom set (`planckStepAtomicity_independent_of_jet_order`
— both directions in one statement).

## Strengthenings that STILL do not suffice

`jet_order_strengthenings_still_insufficient` shows the same rank-2
model additionally satisfies every natural order-theoretic upgrade of
the axiom set:

* the order is TOTAL (`degLexPair_trichotomy`) — so adding totality to
  the axioms cannot force rank-one;
* a genuine "Planck step" EXISTS in the model: `(1,0)` is the unique
  least nonzero element (`e1_least_nonzero`);
* the iterates of that minimal step are COFINAL — every element is
  below some `n • (1,0)` (`e1_iterates_cofinal`) — so even "the minimal
  step's iterates exhaust the order cofinally" cannot force rank-one.

What atomicity adds beyond ANY such order axiom is precisely the
`generates` clause — every segment IS an iterate, not merely bounded by
iterates. No well-founded/total/translation-invariant/cofinal ordering
structure yields that: it is genuinely new content, which STRENGTHENS
the case for carrying it as a §3b-tax primary conjecture class.

Universe note (§7d): the refuted implications quantify over
`M : Type` (Type 0). This suffices: a universe-polymorphic
`∀ (M : Type u), …` would in particular hold at `u = 0`, so its
negation follows from the Type-0 negation; `ℕ × ℕ : Type`.

Base ring (§7c): no field is needed anywhere in this file — generic
`{M : Type*} [AddCommMonoid M]` for the abstract shape; concrete
witnesses on `ℕ × ℕ` and `ℕ`. No `Real.*`, no archimedean construct.

Scope discipline: this file creates NO instance of
`PlanckStepAtomicity` (the trivially-true `ℕ`-atomicity is stated as a
raw existential, `nat_is_atomic`, deliberately NOT as a class instance —
the class's no-instance discipline is about the substrate's monoid and
is easiest to audit when the instance count stays zero). Refutation
scope per §"Before declaring refuted": this is a PROVED structural
exclusion of the *implication* "JetCompatibleOrder → atomicity" (a Lean
counterexample model), not a scope-limited numerical negative; it does
not exclude that a FUTURE, stronger formalization of the jet tower
(one carrying the `generates` clause itself) implies atomicity — but
any such formalization would be assuming the conclusion.

-- Ref: [leitner2026] lifting-and-descent, prop:ordering-jet-compatibility;
--      information-theory, rem:discrete-planck-step;
--      docs/audits/2026-07-25-planck-step-atomicity-formalization.md §3/§6;
--      docs/audits/2026-07-25-atomicity-upgrade-route.md
-/

import QOU.AlgebraicSubstrate.PlanckStepAtomicity
import Mathlib.Order.WellFounded

namespace QOU.AlgebraicSubstrate.SubstrateClock

/-! ## The abstract jet-compatibility shape -/

/-- Abstract extraction of the `prop:ordering-jet-compatibility` axiom
set for an additive computation monoid `M` — the strongest structural
reading under which the jet-tower ordering could bear on
`PlanckStepAtomicity` at all:

* `lt` — the braiding-induced ordering (one GLOBAL relation, exactly as
  the block Lean's `degLex`; per-level orderings are its restrictions,
  which is why the block's `axiom ordering_extends` is tautological
  there and the extension leg is the derived `ltAt_extends` here);
* `level` — the jet filtration `A₀ ⊆ A₁ ⊆ …`: an increasing exhaustive
  tower of submonoids (`zero_mem`/`add_mem` = subalgebra closure,
  `level_mono` = the prolongation embeddings `ℓ_n`, `level_exhausts` =
  the direct-limit leg);
* `compat` — leg 2, translation invariance (`ordering_compatible`);
* `wf` — leg 3, well-foundedness (`wellfounded_at_level`, globally).

This is a `structure`, not a class: an ordering is a CHOICE of data, and
a monoid may carry several. -/
structure JetCompatibleOrder (M : Type*) [AddCommMonoid M] where
  /-- The braiding-induced ordering (global; levels restrict it). -/
  lt : M → M → Prop
  /-- The jet filtration: membership in the level-`n` subalgebra. -/
  level : ℕ → M → Prop
  /-- Each level contains the empty computation. -/
  zero_mem : ∀ n : ℕ, level n 0
  /-- Each level is closed under composition (subalgebra closure). -/
  add_mem : ∀ (n : ℕ) (a b : M), level n a → level n b → level n (a + b)
  /-- The tower is increasing: the prolongation `ℓ_n` embeds level `m`
  into every later level. -/
  level_mono : ∀ {m n : ℕ}, m ≤ n → ∀ a : M, level m a → level n a
  /-- Direct-limit leg: every element lives at some finite level. -/
  level_exhausts : ∀ a : M, ∃ n : ℕ, level n a
  /-- Leg 2 (`ordering_compatible`): two-sided translation invariance. -/
  compat : ∀ a b c d : M, lt a b → lt (c + a + d) (c + b + d)
  /-- Leg 3 (`wellfounded_at_level`, globally): no infinite descent. -/
  wf : WellFounded lt

namespace JetCompatibleOrder

variable {M : Type*} [AddCommMonoid M] (J : JetCompatibleOrder M)

/-- The level-`n` restriction of the ordering — the block Lean's
`degLex w w' ∧ ∀ g ∈ w, g < n` shape. -/
def ltAt (n : ℕ) (a b : M) : Prop :=
  J.lt a b ∧ J.level n a ∧ J.level n b

/-- **Extension leg (leg 1), derived.** The level-`(n)` ordering extends
to every later level — the non-tautological content of the block's
`axiom ordering_extends`, recovered here from `level_mono` because the
ordering is one global relation restricted to levels. -/
theorem ltAt_extends {m n : ℕ} (hmn : m ≤ n) {a b : M}
    (h : J.ltAt m a b) : J.ltAt n a b :=
  ⟨h.1, J.level_mono hmn a h.2.1, J.level_mono hmn b h.2.2⟩

/-- **Per-level well-foundedness**, mirroring the block's
`wellfounded_at_level`: each restriction of a well-founded relation is
well-founded. -/
theorem ltAt_wellFounded (n : ℕ) : WellFounded (J.ltAt n) :=
  Subrelation.wf (fun h => h.1) J.wf

/-- A well-founded relation is irreflexive (self-contained; used for the
termination leg). -/
theorem lt_irrefl (a : M) : ¬ J.lt a a := by
  induction a using J.wf.induction with
  | _ a ih => exact fun h => ih a h h

/-- **Direct-limit termination leg (leg 4), derived.** The block's
`axiom direct_limit_terminates` concludes `∃ w', ¬ degLex w' w`; that
shape follows from irreflexivity alone (take `w' = w`). -/
theorem terminates (a : M) : ∃ b : M, ¬ J.lt b a :=
  ⟨a, J.lt_irrefl a⟩

end JetCompatibleOrder

/-! ## The rank-2 model: `ℕ × ℕ` with degree-lexicographic order -/

/-- Degree-lexicographic order on the rank-two step monoid `ℕ × ℕ` —
the exact analogue of the block's `degLex` (length first, then lex):
compare total degree first, then the second ("jet-direction")
coordinate. At fixed degree the pair is determined by its second
coordinate, so this IS the full lex tie-break. Note the new generator
`(0,1)` is ordered AFTER the old one `(1,0)`, exactly as the jet
prolongation orders new Ω¹ directions after all old generators. -/
def degLexPair (a b : ℕ × ℕ) : Prop :=
  a.1 + a.2 < b.1 + b.2 ∨ (a.1 + a.2 = b.1 + b.2 ∧ a.2 < b.2)

/-- `degLexPair` is well-founded — the same length-first factoring
through `Prod.Lex` as the block's `degLex_wf_unrestricted`. -/
theorem degLexPair_wf : WellFounded degLexPair := by
  have key : WellFounded (Prod.Lex (· < · : ℕ → ℕ → Prop) (· < · : ℕ → ℕ → Prop)) :=
    WellFounded.prod_lex Nat.lt_wfRel.wf Nat.lt_wfRel.wf
  have hsub : Subrelation degLexPair
      (InvImage (Prod.Lex (· < ·) (· < ·))
        (fun p : ℕ × ℕ => (p.1 + p.2, p.2))) := by
    rintro a b (h | ⟨heq, hlt⟩)
    · exact Prod.Lex.left _ _ h
    · show Prod.Lex (· < ·) (· < ·) (a.1 + a.2, a.2) (b.1 + b.2, b.2)
      rw [heq]
      exact Prod.Lex.right _ hlt
  exact Subrelation.wf hsub (InvImage.wf _ key)

/-- `degLexPair` is translation-invariant — leg 2
(`ordering_compatible`) for the rank-2 model. -/
theorem degLexPair_compat (a b c d : ℕ × ℕ) (h : degLexPair a b) :
    degLexPair (c + a + d) (c + b + d) := by
  rcases h with h | ⟨heq, hlt⟩
  · exact Or.inl (by simp only [Prod.fst_add, Prod.snd_add]; omega)
  · exact Or.inr ⟨by simp only [Prod.fst_add, Prod.snd_add]; omega,
      by simp only [Prod.snd_add]; omega⟩

/-- **The rank-2 model.** `ℕ × ℕ` satisfies EVERY leg of the
jet-compatibility axiom set: `degLexPair` order, alphabet filtration in
which the second generator `(0,1)` is the level-1 jet-prolongation
direction (level 0 = the submonoid on the first generator; level ≥ 1 =
everything). All fields proved, sorry-free. -/
def rankTwoJetOrder : JetCompatibleOrder (ℕ × ℕ) where
  lt := degLexPair
  level n a := a.2 = 0 ∨ 1 ≤ n
  zero_mem n := Or.inl rfl
  add_mem n a b ha hb := by
    rcases ha with ha | ha
    · rcases hb with hb | hb
      · exact Or.inl (by simp only [Prod.snd_add]; omega)
      · exact Or.inr hb
    · exact Or.inr ha
  level_mono hmn a ha := by
    rcases ha with ha | ha
    · exact Or.inl ha
    · exact Or.inr (le_trans ha hmn)
  level_exhausts a := ⟨1, Or.inr le_rfl⟩
  compat := degLexPair_compat
  wf := degLexPair_wf

/-! ## The rank-1 sanity model: `ℕ` -/

/-- **The rank-1 model.** `ℕ` with its usual order also satisfies every
leg (trivial one-generator filtration) — so the axiom set is consistent
with atomicity as well as with its failure. -/
def rankOneJetOrder : JetCompatibleOrder ℕ where
  lt := (· < ·)
  level _ _ := True
  zero_mem _ := trivial
  add_mem _ _ _ _ _ := trivial
  level_mono _ _ _ := trivial
  level_exhausts _ := ⟨0, trivial⟩
  compat a b c d h := by omega
  wf := Nat.lt_wfRel.wf

/-- `ℕ` IS atomic: the step `1` generates freely. Stated as a raw
existential — deliberately NOT a `PlanckStepAtomicity` instance, to
keep the class's instance count at zero (its no-instance discipline is
the honest open-state marker for the substrate's monoid). -/
theorem nat_is_atomic :
    ∃ g : ℕ, (∀ a : ℕ, ∃ n : ℕ, a = n • g) ∧
      (∀ n m : ℕ, n • g = m • g → n = m) :=
  ⟨1, fun a => ⟨a, by simp⟩, fun n m h => by simpa using h⟩

/-! ## The independence theorems -/

/-- **Route 1 closes negative (proved, sorry-free, unconditional).**
The jet-compatibility axiom set does NOT force atomicity: it is
refutable to claim that every additive monoid carrying a
jet-compatible order is atomic. Witness: `rankTwoJetOrder` on `ℕ × ℕ`
satisfies every leg, yet `ℕ × ℕ` has no single generating step
(`atomicity_fails_for_two_generators`). Consequently there is no
theorem `JetCompatibleOrder M → PlanckStepAtomicity M`, and
`prop:ordering-jet-compatibility`'s order structure cannot upgrade
`PlanckStepAtomicity` from premise to theorem. -/
theorem planckStepAtomicity_not_forced_by_jet_order :
    ¬ ∀ (M : Type) [AddCommMonoid M], JetCompatibleOrder M →
      ∃ g : M, (∀ a : M, ∃ n : ℕ, a = n • g) ∧
        (∀ n m : ℕ, n • g = m • g → n = m) := by
  intro h
  obtain ⟨g, hgen, _hfree⟩ := h (ℕ × ℕ) rankTwoJetOrder
  exact atomicity_fails_for_two_generators ⟨g, hgen⟩

/-- **Full independence (proved, sorry-free, unconditional).** The
jet-compatibility axiom set neither proves nor refutes atomicity:
`ℕ × ℕ` carries a jet-compatible order and is not atomic
(`planckStepAtomicity_not_forced_by_jet_order`), while `ℕ` carries a
jet-compatible order and is atomic (`rankOneJetOrder`,
`nat_is_atomic`). Atomicity is genuinely NEW content beyond the
jet-tower ordering structure — which is exactly the situation the
§3b-tax primary-conjecture-class representation of
`PlanckStepAtomicity` is designed for. -/
theorem planckStepAtomicity_independent_of_jet_order :
    (¬ ∀ (M : Type) [AddCommMonoid M], JetCompatibleOrder M →
        ∃ g : M, (∀ a : M, ∃ n : ℕ, a = n • g) ∧
          (∀ n m : ℕ, n • g = m • g → n = m)) ∧
    (¬ ∀ (M : Type) [AddCommMonoid M], JetCompatibleOrder M →
        ¬ ∃ g : M, (∀ a : M, ∃ n : ℕ, a = n • g) ∧
          (∀ n m : ℕ, n • g = m • g → n = m)) :=
  ⟨planckStepAtomicity_not_forced_by_jet_order,
    fun h => h ℕ rankOneJetOrder nat_is_atomic⟩

/-! ## Strengthenings that still do not suffice -/

/-- The rank-2 model order is TOTAL: trichotomy holds. So upgrading the
jet-compatibility axioms from "admissible ordering" to "total
translation-invariant well-order" still cannot force atomicity. -/
theorem degLexPair_trichotomy (a b : ℕ × ℕ) :
    degLexPair a b ∨ a = b ∨ degLexPair b a := by
  obtain ⟨a1, a2⟩ := a
  obtain ⟨b1, b2⟩ := b
  rcases Nat.lt_trichotomy (a1 + a2) (b1 + b2) with h | h | h
  · exact Or.inl (Or.inl h)
  · rcases Nat.lt_trichotomy a2 b2 with h2 | h2 | h2
    · exact Or.inl (Or.inr ⟨h, h2⟩)
    · refine Or.inr (Or.inl ?_)
      have h1 : a1 = b1 := by omega
      rw [h1, h2]
    · exact Or.inr (Or.inr (Or.inr ⟨h.symm, h2⟩))
  · exact Or.inr (Or.inr (Or.inl h))

/-- Iterates of the first generator: `n • (1,0) = (n,0)`. -/
theorem nsmul_e1 (n : ℕ) : n • ((1, 0) : ℕ × ℕ) = (n, 0) := by
  induction n with
  | zero => rw [zero_nsmul]; rfl
  | succ k ih => rw [succ_nsmul, ih, Prod.mk_add_mk]

/-- The model even has a genuine "Planck step": `(1,0)` is the LEAST
nonzero element of the total order `degLexPair`. -/
theorem e1_least_nonzero (a : ℕ × ℕ) (ha : a ≠ 0) :
    a = (1, 0) ∨ degLexPair (1, 0) a := by
  obtain ⟨a1, a2⟩ := a
  have h0 : a1 + a2 ≠ 0 := by
    intro h
    exact ha (by
      have h1 : a1 = 0 := by omega
      have h2 : a2 = 0 := by omega
      rw [h1, h2]; rfl)
  rcases Nat.lt_or_ge 1 (a1 + a2) with h | h
  · exact Or.inr (Or.inl (by simp only []; omega))
  · -- degree exactly 1: either (1,0) itself or (0,1), which is later
    rcases Nat.eq_zero_or_pos a2 with h2 | h2
    · left
      have h1 : a1 = 1 := by omega
      rw [h1, h2]
    · exact Or.inr (Or.inr ⟨by simp only []; omega, by simp only []; omega⟩)

/-- The minimal step's iterates are COFINAL: every element is strictly
below some `n • (1,0)`. Even "the Planck step's iterates exhaust the
order cofinally" does not force atomicity. -/
theorem e1_iterates_cofinal (a : ℕ × ℕ) :
    ∃ n : ℕ, degLexPair a (n • ((1, 0) : ℕ × ℕ)) := by
  refine ⟨a.1 + a.2 + 1, ?_⟩
  rw [nsmul_e1]
  exact Or.inl (by simp only []; omega)

/-- **The strengthened axiom set is STILL insufficient (proved,
sorry-free, unconditional).** One and the same rank-2 model satisfies
the full jet-compatibility axiom set PLUS totality PLUS the existence
of a least nonzero step PLUS cofinality of that step's iterates — and
is still not atomic. So no order-theoretic strengthening of
`prop:ordering-jet-compatibility` along these natural axes can close
route 1: what atomicity adds is precisely the `generates` clause (every
segment IS an iterate of the step, not merely comparable to iterates),
and any jet-tower formalization strong enough to imply it would have to
carry that clause as an assumption — i.e. assume the conclusion. -/
theorem jet_order_strengthenings_still_insufficient :
    ∃ J : JetCompatibleOrder (ℕ × ℕ),
      (∀ a b : ℕ × ℕ, J.lt a b ∨ a = b ∨ J.lt b a) ∧
      (∃ g₀ : ℕ × ℕ, g₀ ≠ 0 ∧
        (∀ a : ℕ × ℕ, a ≠ 0 → a = g₀ ∨ J.lt g₀ a) ∧
        (∀ a : ℕ × ℕ, ∃ n : ℕ, J.lt a (n • g₀))) ∧
      ¬ ∃ g : ℕ × ℕ, ∀ a : ℕ × ℕ, ∃ n : ℕ, a = n • g :=
  ⟨rankTwoJetOrder, degLexPair_trichotomy,
    ⟨(1, 0), by simp, e1_least_nonzero, e1_iterates_cofinal⟩,
    atomicity_fails_for_two_generators⟩

end QOU.AlgebraicSubstrate.SubstrateClock
