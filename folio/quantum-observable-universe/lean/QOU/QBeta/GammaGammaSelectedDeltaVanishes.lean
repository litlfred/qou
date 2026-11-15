/-
# A γγ-selected `Δ` is invisible to every one-dimensional block

`qou-99qc`, applying the owner's word-selection ruling to the DECAY channel.

The owner ruled (2026-09-08, bean `qou-ales`): *"All selection of great words
should be done through gamma gamma production and the semi-definite product
solutions at q_0. Shouldn't use census."* That ruling has been applied to the
mass/binding channel (`QOU.Mass.GammaGammaSelectorH3`). It has not been applied
to the decay channel, where `Q_β = |ε(Δ)|·E₀` needs an element
`Δ = 𝓑_n − 𝓑_p`.

This is the first step of that application, and it is a **formalize-first
prune**: it rules a whole class of answers out *before* any number is computed.

## What is proved

`oneDim_annihilates_gammaGamma_difference` — any functional that is
multiplicative over concatenation and takes the value `1` on a pair-production
vertex takes the value `1` on **every** γγ-produced word
(`unit_on_vertices_eq_one`), hence **annihilates every difference of two
γγ-produced words**.

Both one-dimensional blocks of `H₃` are of exactly this shape:

* the `(1³)` alternating character `altChar` — `altChar_append`,
  `altChar_vertex` in `QOU.Mass.GammaGammaWordSelection`;
* the `(3)` trivial character `trivChar` — `trivChar_append`,
  `trivChar_vertex` in `QOU.Mass.GammaGammaSelectorH3`.

`altChar_difference_vanishes` instantiates it on the one this file imports.

## Why it matters, in two steps

**Level 1 — the augmentation gives exactly zero.** Under convention D the
augmentation is the Markov trace at `z = q`, and its block support is `y_(3) = 1`
with `y_(2,1) = y_(1³) = 0` (`qbeta_augmentation_is_a_markov_trace_probe`,
merged). So at level 1 the functional *is* a multiple of the `(3)` character,
which the theorem annihilates. **Any γγ-selected `Δ` predicts `Q_β = 0` exactly,
for every choice of the two words.** Not a small number — zero, identically, with
no computation to do.

**Level 2 — the ruled functional is carried by one block.** At `z_D` the support
is `y_(3), y_(2,1) ≠ 0` and `y_(1³) = 0`. The `(3)` contribution vanishes by the
theorem, so

    tr_{z_D}(Δ)  =  y_(2,1) · χ_(2,1)(Δ)      for any γγ-produced Δ

— the **entire** decay prediction from a γγ-selected element comes from the
two-dimensional block alone. That is what makes the accompanying probe's scan
one-dimensional and finite rather than a search.

## Why this is a prune and not a negative result about the ruling

The vanishing is a statement about **γγ-produced words**, which carry no flavour
index — `Crossing` is `⟨gen, pos⟩` and nothing else. A selection principle with
no flavour input cannot distinguish a proton word from a neutron word, so the
question this file settles is what happens if one applies it *alone*. The honest
reading is that the γγ+SDP principle **underdetermines `Δ`** and must be
supplemented by the flavour letters — which is the open point
`GammaGammaSelectorH3`'s own summary names ("the non-γγ quark/gluon letters").

Base ring is a generic `CommRing` for the general lemma; the `altChar`
instantiation inherits `Field` from the imported definition.

-- Ref: [leitner2026] bean `qou-ales`, owner ruling 2026-09-08
-/
import Mathlib.Tactic
import QOU.Mass.GammaGammaWordSelection

namespace QOU.QBeta.GammaGammaDelta

open QOU.Mass.GammaGammaWordSelection

/-- **A unit-on-vertices multiplicative functional is `1` on every γγ-word.**

The three hypotheses are exactly the structure both one-dimensional characters
of `H₃` have: a value on the empty word, multiplicativity over concatenation,
and the value `1` on a pair-production vertex (the vertex pairs `σᵢ` with
`σᵢ₊₁⁻¹`, so the two eigenvalues cancel). -/
theorem unit_on_vertices_eq_one {R : Type*} [CommRing R] {f : Word → R}
    (hnil : f [] = 1) (hmul : ∀ u v, f (u ++ v) = f u * f v)
    (hvert : ∀ i, f (vertex i) = 1)
    {w : Word} (h : GammaGammaWord w) : f w = 1 := by
  induction h with
  | nil => exact hnil
  | cons i _ ih => rw [hmul, hvert, ih, one_mul]

/-- **Hence it annihilates every difference of two γγ-produced words.**

This is the prune: a functional supported on the one-dimensional blocks cannot
see *any* γγ-selected `Δ`, whatever the two words are. No scan over candidate
words can change the answer, because the answer does not depend on them. -/
theorem oneDim_annihilates_gammaGamma_difference {R : Type*} [CommRing R]
    {f : Word → R} (hnil : f [] = 1) (hmul : ∀ u v, f (u ++ v) = f u * f v)
    (hvert : ∀ i, f (vertex i) = 1)
    {u v : Word} (hu : GammaGammaWord u) (hv : GammaGammaWord v) :
    f u - f v = 0 := by
  rw [unit_on_vertices_eq_one hnil hmul hvert hu,
      unit_on_vertices_eq_one hnil hmul hvert hv, sub_self]

/-- The `(1³)` alternating character satisfies the hypotheses. -/
theorem altChar_nil {R : Type*} [Field R] (q : R) : altChar q [] = 1 := by
  simp [altChar]

/-- **Instantiation: the alternating block cannot see a γγ difference.** -/
theorem altChar_difference_vanishes {R : Type*} [Field R] {q : R} (hq : q ≠ 0)
    {u v : Word} (hu : GammaGammaWord u) (hv : GammaGammaWord v) :
    altChar q u - altChar q v = 0 :=
  oneDim_annihilates_gammaGamma_difference (altChar_nil q) (altChar_append q)
    (fun i => altChar_vertex hq i) hu hv

/-- **The level-1 statement, in the form the decay ansatz uses.**

At Wenzl level 1 the Markov trace is supported on the `(3)` block alone, so the
functional is `c · χ_(3)` for a scalar `c`. On a γγ-selected `Δ` that is `c · 0`.
Stated for a general scalar and a general unit-on-vertices character so it
applies to whichever one-dimensional block carries the support. -/
theorem scaled_oneDim_annihilates {R : Type*} [CommRing R] {f : Word → R}
    (hnil : f [] = 1) (hmul : ∀ u v, f (u ++ v) = f u * f v)
    (hvert : ∀ i, f (vertex i) = 1) (c : R)
    {u v : Word} (hu : GammaGammaWord u) (hv : GammaGammaWord v) :
    c * f u - c * f v = 0 := by
  rw [← mul_sub, oneDim_annihilates_gammaGamma_difference hnil hmul hvert hu hv,
      mul_zero]

/-- **The Borromean core is γγ-produced**, so it is one of the words this prune
covers — recorded because it is the word `GammaGammaSelectorH3` selects as the
minimal non-zero survivor, and therefore the one a reader would reach for. -/
theorem borromean_is_covered {R : Type*} [Field R] {q : R} (hq : q ≠ 0) :
    altChar q borromean - altChar q borromean = 0 :=
  altChar_difference_vanishes hq borromean_gammaGamma borromean_gammaGamma

/-! ## The ruling DECIDES the braid ordering the corpus owed

`qou-99qc` / #7188 measured that under the ruled functional at `z_D` the braid
ORDER of the nucleon word is visible and unconstrained, and concluded that the
corpus owes a *derivation* of it. The γγ ruling supplies one, and the lemmas
below are what make it a derivation rather than a preference.

The census carries two orderings of the same eleven-letter multiset
(`qbeta_delta_candidate_census_probe.py`). Their confinement cores are:

* **interleaved** — `nuc9`'s `for _ in range(3): σ₀ ; (σ₁ − h)`, and
  `σ₁ − h = σ₁⁻¹` by the Hecke relation
  (`QOU.QBeta.NucleonFlavour.skein_letter_inv`), so the core is `(σ₀σ₁⁻¹)³`
  — which is `vertex 0` three times, i.e. **γγ-produced**;
* **gen-grouped** — `_GEN_CHAINS`, all `σ₀` letters first, so the core is
  `σ₀σ₀σ₀σ₁⁻¹σ₁⁻¹σ₁⁻¹`, whose first two letters are both **positive**.

`not_gammaGamma_of_snd_pos` excludes the second. So the ruling selects the
interleaved order, and that is a structural exclusion, not a scope-(a) miss.

🛑 **The ruled order is the LESS accurate one**, and that is the correct
outcome under AGENTS.md §NO FITTING ("rank by derivational cleanliness first,
and treat accuracy as a diagnostic"). Measured at the proton pin, convention D:
interleaved **−17.4959 %** against gen-grouped **−15.4514 %**. The ruling costs
2.04 points of residual and buys the one thing the residual cannot: the order
is no longer an unstated modelling choice.
-/

/-- **The second letter of a γγ-word is a negative crossing.**

Immediate from the constructor — `vertex i` is `⟨i, true⟩ :: ⟨i+1, false⟩ :: _`
— but it is the whole content of the ordering exclusion below. -/
theorem gammaGamma_snd_neg {c₀ c₁ : Crossing} {t : Word}
    (h : GammaGammaWord (c₀ :: c₁ :: t)) : c₁.pos = false := by
  cases h with
  | cons i _ => rfl

/-- **A word whose SECOND crossing is positive is not γγ-produced.**

This is the lemma that rules out the gen-grouped ordering. It was first stated
with both of the first two letters positive as hypotheses; the linter caught
that the first is never used, so the lemma is strictly stronger than the
exclusion needs — the sign of `c₀` is irrelevant. A γγ-word's letters come in
`(positive, negative)` pairs, so *any* positive letter in second position is
already impossible. -/
theorem not_gammaGamma_of_snd_pos {c₀ c₁ : Crossing} {t : Word}
    (h₁ : c₁.pos = true) : ¬ GammaGammaWord (c₀ :: c₁ :: t) := by
  intro h
  rw [gammaGamma_snd_neg h] at h₁
  exact Bool.noConfusion h₁

/-- The interleaved confinement core `(σ₀σ₁⁻¹)³`, as the census's `nuc9` builds
it: three pair-production vertices on strands `(0,1,2)`. -/
def interleavedCore : Word := vertex 0 ++ (vertex 0 ++ (vertex 0 ++ []))

/-- The gen-grouped core — the **same six letters**, all `σ₀` first. -/
def genGroupedCore : Word :=
  [⟨0, true⟩, ⟨0, true⟩, ⟨0, true⟩, ⟨1, false⟩, ⟨1, false⟩, ⟨1, false⟩]

/-- **The interleaved core IS γγ-produced.** -/
theorem interleavedCore_isGammaGamma : GammaGammaWord interleavedCore :=
  GammaGammaWord.cons 0 (GammaGammaWord.cons 0
    (GammaGammaWord.cons 0 GammaGammaWord.nil))

/-- **The gen-grouped core is NOT γγ-produced**, so the ruling excludes it.

Together with `interleavedCore_isGammaGamma` this settles the ordering: of the
census's two models, exactly one has a γγ-produced core. -/
theorem not_gammaGamma_genGroupedCore : ¬ GammaGammaWord genGroupedCore := by
  intro h
  exact not_gammaGamma_of_snd_pos (c₀ := ⟨0, true⟩) (c₁ := ⟨0, true⟩) rfl h

/-- **The two cores are different elements, not merely different spellings** —
recorded so a reader does not assume the orderings are interchangeable. They
share a letter multiset; `H₃(q)` is noncommutative across generators, and the
measured traces differ by a factor of 5.5 (`0.9986` against `0.1801` at the
proton `q₀`). The Lean statement is the weaker, decidable one: the two words
are not equal as lists. -/
theorem cores_ne : interleavedCore ≠ genGroupedCore := by decide

/-! ## How far the ruling can reach — a parity bound

The ordering result above settles the **core**. This settles how much of the
nucleon word the γγ principle can settle *at all*, and the answer is bounded
by parity rather than by effort.

Every vertex contributes exactly two letters, so **a γγ-word has even length**
(`gammaGamma_length_even`). The nucleon crossing budget is **11** (`qou-1qsw`),
which is odd. So no 11-crossing word is γγ-produced — not this one, not any
reordering of it, not any other candidate with that budget
(`eleven_not_gammaGamma`). At least one letter necessarily lies outside the
principle's reach, and that is a structural fact about the budget, not a gap in
the construction.

Concretely, for the census word `core(6) + quark(3) + gluon(2)`:

| block | letters | γγ-produced? |
|---|---|---|
| core `(σ₀σ₁⁻¹)³` | 6 | **yes** — `interleavedCore_isGammaGamma` |
| quark | 3 | no — odd length |
| gluon `σ₀σ₀` | 2 | no — second letter positive |

So the ruling reaches **6 of 11** letters. The remaining five are the freedom
that survives it, and the two gluon letters are excluded twice over: by
`gluonPair_not_gammaGamma` directly, and by the parity of the quark block they
follow.

**Scope-(b) throughout** — each exclusion cites a proved invariant (vertex
length, or the vertex sign pattern), never a measured miss.
-/

/-- **A γγ-word has even length.** Each pair-production vertex contributes
exactly two letters, so the length of any concatenation of them is even. -/
theorem gammaGamma_length_even {w : Word} (h : GammaGammaWord w) :
    2 ∣ w.length := by
  induction h with
  | nil => simp
  | cons i _ ih =>
      simp only [vertex, List.length_append, List.length_cons, List.length_nil]
      omega

/-- **Odd length excludes γγ production.** The contrapositive, in the form the
crossing-budget argument uses. -/
theorem not_gammaGamma_of_odd_length {w : Word} (h : ¬ (2 ∣ w.length)) :
    ¬ GammaGammaWord w := fun hg => h (gammaGamma_length_even hg)

/-- **No 11-crossing word is γγ-produced.**

`qou-1qsw` fixes the nucleon crossing budget at 11, which is odd. So the γγ
ruling cannot determine a nucleon word in full — for *any* candidate at that
budget, in any order. This bounds the principle's reach from above without
computing anything. -/
theorem eleven_not_gammaGamma {w : Word} (h : w.length = 11) :
    ¬ GammaGammaWord w := by
  refine not_gammaGamma_of_odd_length ?_
  rw [h]; decide

/-- The two-letter gluon block `σ₀σ₀` of the census word. -/
def gluonPair : Word := [⟨0, true⟩, ⟨0, true⟩]

/-- **The gluon pair is not γγ-produced** — both its letters are positive, and
a vertex pairs a positive crossing with a negative one. So the ruling does not
reach the gluon letters even though their block has even length. -/
theorem gluonPair_not_gammaGamma : ¬ GammaGammaWord gluonPair := by
  intro h
  exact not_gammaGamma_of_snd_pos (c₀ := ⟨0, true⟩) (c₁ := ⟨0, true⟩) rfl h

/-- **The quark block's length is odd**, so it is not γγ-produced either. Stated
for a general three-letter word since the census's quark block is three typed
crossings whose generators are not fixed by the corpus. -/
theorem three_not_gammaGamma {w : Word} (h : w.length = 3) :
    ¬ GammaGammaWord w := by
  refine not_gammaGamma_of_odd_length ?_
  rw [h]; decide

end QOU.QBeta.GammaGammaDelta
