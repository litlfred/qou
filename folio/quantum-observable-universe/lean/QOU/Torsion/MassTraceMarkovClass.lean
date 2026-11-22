import QOU.Torsion.MassTraceMarkov
import QOU.MathlibExt.MarkovMoves

set_option autoImplicit false

/-!
# The mass identity on braid classes

`QOU.Torsion.MassTraceMarkov` states the mass identity braid by braid: the framing-corrected
Markov trace of the braid a word spells is the site-weighted trace of the word's discrete
multiplicative integral `Hol`. This file states it on **braid classes**: braids on any number of
strands modulo the two Markov moves (conjugation and positive or negative stabilisation). The
statement is then entirely algebraic and complete on its own domain; no topological input is used.

## The tower of Artin braid groups

`QOU.MathlibExt.MarkovMoves` defines the Markov moves on an abstract `BraidTower` and proves that a
functional respecting both moves descends to the quotient, but it constructs no tower on the Artin
groups. Here `artinTower` is that tower: level `n` is `BraidGroupN n` (the braid group on `n+1`
strands), the stabilisation homomorphism is `QOU.IwahoriHecke.BraidTower.braidTower` (add an inert
strand on the right), and the new generator is `σ_{n+1}`, the crossing of the last two strands.

## Theorems

* `jonesTot_isMarkovInvariant` — the framing-corrected trace `jonesFn` at the weight the peel
  forces, `w = (1, q²)`, is invariant under both moves. This assembles `jonesFn_conj`,
  `jonesFn_peel` and `jonesFn_peel_neg`; no new trace identity is proved here.
* `massClass` — the induced function on braid classes, and `massClass_classOf` its value.
* `exists_wordBraid` — every braid is spelled by a word, so every class is the class of a word.
* `massClass_wordBraid` (**the mass identity on braid classes**) — the mass functional of the class
  of a word is `A^{m+1} · B^{writhe} · wi^{m+1} · Tr(K^{⊗(m+1)} · Hol(ℓ))`.
* `holTrace_eq_of_markovEquiv` — Markov-equivalent words have equal framing-corrected
  multiplicative-integral traces, across different strand numbers.

## Scope

The classes here are Markov classes of braids. That they are in bijection with isotopy classes of
oriented links is the Alexander–Markov theorem of low-dimensional topology; it is cited, not used,
and nothing in this file depends on it.

**Base ring (§7c).** `R` is any commutative ring; `q⁻¹` and `(1 + q²)⁻¹` are carried as `qi`, `wi`
with witnessing equations.

## References

- Ref: [alexander1923] https://doi.org/10.1073/pnas.9.3.93 — every link is a braid closure.
- Ref: [markov1936] Markov's theorem: braid closures are isotopic iff the braids are Markov
  equivalent. Cited only.
- Ref: [birman1974] https://doi.org/10.1515/9781400881420 — §2.2, a proof of Markov's theorem.
- Ref: [jones1987] https://doi.org/10.2307/1971403 — the Markov trace on Hecke algebras.
-/

namespace QOU.Torsion.MassTraceMarkovClass

open QOU.IwahoriHecke.BraidGroup QOU.IwahoriHecke.JonesNormalisation
open QOU.IwahoriHecke.QuantumTrace QOU.Torsion.MassTraceMarkov QOU.IwahoriHecke.TensorEmbed

/-! ## The Artin braid tower -/

/-- **The tower of Artin braid groups.** Level `n` is the braid group on `n+1` strands; the
stabilisation homomorphism adds an inert strand on the right, and the new generator is the
crossing of the last two strands. -/
def artinTower : QOU.MathlibExt.MarkovMoves.BraidTower BraidGroupN where
  incl _ := QOU.IwahoriHecke.BraidTower.braidTower
  gen n := braidGen (coxA (n + 1)) (Fin.last n)

/-- Braid classes: braids on any number of strands modulo the two Markov moves. -/
abbrev BraidClass : Type := QOU.MathlibExt.MarkovMoves.MarkovClass artinTower

/-! ## The framing-corrected trace is a Markov invariant -/

variable {R : Type*} [CommRing R] (q qi wi : R)

/-- The framing-corrected trace `jonesFn` as a functional on the whole tower. -/
noncomputable def jonesTot (hqi : q * qi = 1) (w : Fin 2 → R) (hw : (1 + q ^ 2) * wi = 1)
    (p : QOU.MathlibExt.MarkovMoves.Tot BraidGroupN) : R :=
  jonesFn q qi wi hqi w hw p.2

/-- **Both Markov moves leave the framing-corrected trace unchanged** at the weight the peel
forces, `w = (1, q²)`. -/
theorem jonesTot_isMarkovInvariant (hqi : q * qi = 1) (w : Fin 2 → R)
    (hw : (1 + q ^ 2) * wi = 1) (h0 : w 0 = 1) (h1 : w 1 = q ^ 2) :
    QOU.MathlibExt.MarkovMoves.IsMarkovInvariant artinTower (jonesTot q qi wi hqi w hw) where
  conj n a b := by
    have h := jonesFn_conj q qi wi hqi w hw a (b * a)
    simp only [mul_assoc, mul_inv_cancel, mul_one] at h
    exact h
  stab n x := by exact jonesFn_peel q qi wi hqi w hw h0 h1 x
  stabInv n x := by exact jonesFn_peel_neg q qi wi hqi w hw h0 h1 x

/-- **The mass functional on braid classes.** -/
noncomputable def massClass (hqi : q * qi = 1) (w : Fin 2 → R) (hw : (1 + q ^ 2) * wi = 1)
    (h0 : w 0 = 1) (h1 : w 1 = q ^ 2) : BraidClass → R :=
  (jonesTot_isMarkovInvariant q qi wi hqi w hw h0 h1).lift

@[simp]
theorem massClass_classOf (hqi : q * qi = 1) (w : Fin 2 → R) (hw : (1 + q ^ 2) * wi = 1)
    (h0 : w 0 = 1) (h1 : w 1 = q ^ 2) {m : ℕ} (β : BraidGroupN m) :
    massClass q qi wi hqi w hw h0 h1 (QOU.MathlibExt.MarkovMoves.classOf artinTower ⟨m, β⟩)
      = jonesFn q qi wi hqi w hw β := rfl

/-! ## Every braid is spelled by a word -/

/-- The letter with the opposite crossing sign. -/
def flipLetter {m : ℕ} (ℓ : Fin m × Bool) : Fin m × Bool := (ℓ.1, !ℓ.2)

theorem letterBraid_flip {m : ℕ} (ℓ : Fin m × Bool) :
    letterBraid (flipLetter ℓ) = (letterBraid ℓ)⁻¹ := by
  rcases ℓ with ⟨a, _ | _⟩ <;> simp [letterBraid, flipLetter]

theorem wordBraid_append {m : ℕ} (ℓs ℓs' : List (Fin m × Bool)) :
    wordBraid (ℓs ++ ℓs') = wordBraid ℓs * wordBraid ℓs' := by
  simp [wordBraid, List.map_append, List.prod_append]

/-- The inverse word: reversed, with every crossing sign flipped. -/
theorem wordBraid_inv {m : ℕ} (ℓs : List (Fin m × Bool)) :
    wordBraid (ℓs.map flipLetter).reverse = (wordBraid ℓs)⁻¹ := by
  induction ℓs with
  | nil => simp [wordBraid]
  | cons ℓ ℓs ih =>
    rw [List.map_cons, List.reverse_cons, wordBraid_append, ih]
    have h1 : wordBraid [flipLetter ℓ] = (letterBraid ℓ)⁻¹ := by
      simp [wordBraid, letterBraid_flip]
    have h2 : wordBraid (ℓ :: ℓs) = letterBraid ℓ * wordBraid ℓs := by simp [wordBraid]
    rw [h1, h2, mul_inv_rev]

/-- **Every braid is spelled by a word.** -/
theorem exists_wordBraid {m : ℕ} (β : BraidGroupN m) : ∃ ℓs, wordBraid ℓs = β := by
  have hβ : β ∈ Subgroup.closure (Set.range (PresentedGroup.of (rels := artinRels (coxA m)))) := by
    rw [PresentedGroup.closure_range_of]; trivial
  induction hβ using Subgroup.closure_induction with
  | mem x hx =>
    obtain ⟨a, rfl⟩ := hx
    exact ⟨[(a, true)], by simp [wordBraid, letterBraid, braidGen]⟩
  | one => exact ⟨[], by simp [wordBraid]⟩
  | mul x y _ _ hx hy =>
    obtain ⟨ℓs, rfl⟩ := hx
    obtain ⟨ℓs', rfl⟩ := hy
    exact ⟨ℓs ++ ℓs', wordBraid_append ℓs ℓs'⟩
  | inv x _ hx =>
    obtain ⟨ℓs, rfl⟩ := hx
    exact ⟨(ℓs.map flipLetter).reverse, wordBraid_inv ℓs⟩

/-- Every braid class is the class of a word. -/
theorem exists_word_of_braidClass (c : BraidClass) :
    ∃ (m : ℕ) (ℓs : List (Fin m × Bool)),
      QOU.MathlibExt.MarkovMoves.classOf artinTower ⟨m, wordBraid ℓs⟩ = c := by
  induction c using Quot.ind with
  | mk p =>
    obtain ⟨m, β⟩ := p
    obtain ⟨ℓs, rfl⟩ := exists_wordBraid β
    exact ⟨m, ℓs, rfl⟩

/-! ## The mass identity on braid classes -/

/-- **The mass identity on braid classes.** The mass functional of the class of a word on `m+1`
strands is the site-weighted trace of the word's discrete multiplicative integral, times the
strand and writhe framing factors:
`m([β_ℓ]) = A^{m+1} · B^{writhe ℓ} · wi^{m+1} · Tr(K^{⊗(m+1)} · Hol(ℓ))`. -/
theorem massClass_wordBraid (hqi : q * qi = 1) (w : Fin 2 → R) (hw : (1 + q ^ 2) * wi = 1)
    (h0 : w 0 = 1) (h1 : w 1 = q ^ 2) {m : ℕ} (ℓs : List (Fin m × Bool)) :
    massClass q qi wi hqi w hw h0 h1
        (QOU.MathlibExt.MarkovMoves.classOf artinTower ⟨m, wordBraid ℓs⟩)
      = ((strandFactor q qi wi hqi hw ^ (m + 1) : Rˣ) : R)
          * ((writheFactor q qi hqi ^ signedLength ℓs : Rˣ) : R)
          * (wi ^ (m + 1) * Matrix.trace (siteWeight w * hol q qi ℓs)) := by
  rw [massClass_classOf, jonesFn_wordBraid]

/-- **The mass identity on braid classes, Temperley–Lieb state-sum form (Option 3).**
    The framing-corrected mass functional of the braid class of `wordBraid ℓs` expands over all
    Temperley–Lieb states `s : Fin ℓs.length → Bool`. -/
theorem massClass_wordBraid_eq_tlStateSum (hqi : q * qi = 1) (w : Fin 2 → R)
    (hw : (1 + q ^ 2) * wi = 1) (h0 : w 0 = 1) (h1 : w 1 = q ^ 2) {m : ℕ}
    (ℓs : List (Fin m × Bool)) :
    massClass q qi wi hqi w hw h0 h1
        (QOU.MathlibExt.MarkovMoves.classOf artinTower ⟨m, wordBraid ℓs⟩)
      = ((strandFactor q qi wi hqi hw ^ (m + 1) : Rˣ) : R)
          * ((writheFactor q qi hqi ^ signedLength ℓs : Rˣ) : R)
          * (∑ s : Fin ℓs.length → Bool,
              tlStateWeight q qi ℓs s *
                (wi ^ (m + 1) * Matrix.trace (siteWeight w * tlStateMatrix q qi ℓs s))) := by
  rw [massClass_classOf, jonesFn_wordBraid_eq_tlStateSum]

/-- **Markov-equivalent words have equal framing-corrected multiplicative-integral traces**,
including words on different numbers of strands. -/
theorem holTrace_eq_of_markovEquiv (hqi : q * qi = 1) (w : Fin 2 → R)
    (hw : (1 + q ^ 2) * wi = 1) (h0 : w 0 = 1) (h1 : w 1 = q ^ 2) {m m' : ℕ}
    (ℓs : List (Fin m × Bool)) (ℓs' : List (Fin m' × Bool))
    (h : QOU.MathlibExt.MarkovMoves.MarkovEquiv artinTower ⟨m, wordBraid ℓs⟩ ⟨m', wordBraid ℓs'⟩) :
    ((strandFactor q qi wi hqi hw ^ (m + 1) : Rˣ) : R)
        * ((writheFactor q qi hqi ^ signedLength ℓs : Rˣ) : R)
        * (wi ^ (m + 1) * Matrix.trace (siteWeight w * hol q qi ℓs))
      = ((strandFactor q qi wi hqi hw ^ (m' + 1) : Rˣ) : R)
        * ((writheFactor q qi hqi ^ signedLength ℓs' : Rˣ) : R)
        * (wi ^ (m' + 1) * Matrix.trace (siteWeight w * hol q qi ℓs')) := by
  rw [← massClass_wordBraid q qi wi hqi w hw h0 h1, ← massClass_wordBraid q qi wi hqi w hw h0 h1,
    QOU.MathlibExt.MarkovMoves.classOf_eq_iff.mpr h]

end QOU.Torsion.MassTraceMarkovClass
