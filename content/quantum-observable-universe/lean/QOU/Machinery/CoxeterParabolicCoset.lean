/-
# Parabolic coset infrastructure — the Bourbaki lifting lemma, conditional on exchange

The commissioned infra for the coset data of the merged braid (#4059) and
far-commutation (#4081) reductions. Mathlib's Coxeter development (pinned
rev) carries the deletion identity and inversion-sequence machinery but NOT
the exchange condition (BB Thm 1.4.3) — the audited upstream gap. This file
isolates that gap as a single precisely-stated hypothesis and derives the
Bourbaki coset theory from it:

* **`RightExchangeProp`** — the right exchange property in reduced-word
  form: a right descent of `π ω` is realized by deleting one letter of the
  reduced word `ω`. Textbook-true (Bjorner–Brenti Thm 1.4.3; Bourbaki Lie
  IV §1); NOT yet provable from Mathlib's primitives — stated as an
  explicit hypothesis parameter, never as an axiom or a `sorry`.
* **Unconditional tier** — the parabolic subgroup `W_J`, the coset
  relation (with reflexivity/symmetry/transitivity), existence of a
  minimal-length coset representative, and `minRep_not_isRightDescent`
  (a minimal representative has no J-descent).
* **`length_minRep_mul_wordProd`** — **the lifting lemma** (the core of
  Bourbaki Lie IV §1 / BB Prop 2.4.4): for `u` minimal in its coset and
  `p` a reduced word with letters in `J`,
  `ℓ(u · π p) = ℓ(u) + |p|` — CONDITIONAL on `RightExchangeProp` only.
  The proof is the classical two-case deletion argument: a failed ascent
  triggers exchange; deletion in the `u`-part contradicts minimality of
  `u`, deletion in the `p`-part contradicts reducedness of `p`.

Consequence for the merged reductions: the length-additivity fields of
`DihedralCosetStructure` / `CommutingCosetStructure` reduce to
`RightExchangeProp` plus the reducedness of the finitely many alternating
cell words — the opaque per-pair coset hypotheses collapse toward one
standard textbook theorem. The remaining assembly (the cell equivalences)
and the exchange proof itself (the reflection-cocycle route) are the
follow-up tiers.

HONESTY (STRICT): nothing here proves the exchange property; every
conditional theorem carries it as an explicit hypothesis. No class
instance is declared; nothing wired; `1/(8π)` stays phase-4.

Base ring: none — pure Coxeter combinatorics (§7c not applicable).

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import Mathlib.GroupTheory.Coxeter.Length
import Mathlib.Tactic.Group

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd
local prefix:100 "σ" => cs.simple

/-- **The right exchange property** (Bjorner–Brenti Thm 1.4.3, simple
form; Bourbaki Lie IV §1): a right descent of a reduced word's product is
realized by deleting a single letter. Textbook-true; not derivable from
Mathlib's current Coxeter primitives (the audited upstream gap) — used
below only as an explicit hypothesis. -/
def RightExchangeProp : Prop :=
  ∀ ⦃ω : List B⦄, cs.IsReduced ω → ∀ ⦃c : B⦄, cs.IsRightDescent (π ω) c →
    ∃ r, π ω * σ c = π (ω.eraseIdx r)

variable (J : Set B)

/-- The standard parabolic subgroup `W_J = ⟨s_l : l ∈ J⟩`. -/
def parabolic : Subgroup W := Subgroup.closure (cs.simple '' J)

/-- Two elements lie in the same left coset of `W_J`. -/
def SameCosetJ (u x : W) : Prop := u⁻¹ * x ∈ parabolic cs J

theorem sameCosetJ_refl (u : W) : SameCosetJ cs J u u := by
  simp [SameCosetJ, (parabolic cs J).one_mem]

theorem sameCosetJ_symm {u x : W} (h : SameCosetJ cs J u x) :
    SameCosetJ cs J x u := by
  have h2 := (parabolic cs J).inv_mem h
  simpa [SameCosetJ, mul_inv_rev] using h2

theorem sameCosetJ_trans {u x y : W} (h₁ : SameCosetJ cs J u x)
    (h₂ : SameCosetJ cs J x y) : SameCosetJ cs J u y := by
  have h3 := (parabolic cs J).mul_mem h₁ h₂
  simpa [SameCosetJ, mul_assoc] using h3

/-- A word with letters in `J` has product in `W_J`. -/
theorem wordProd_mem_parabolic {p : List B} (hp : ∀ l ∈ p, l ∈ J) :
    π p ∈ parabolic cs J := by
  induction p with
  | nil => simpa using (parabolic cs J).one_mem
  | cons c p ih =>
    rw [wordProd_cons]
    refine (parabolic cs J).mul_mem ?_ (ih fun l hl => hp l (mem_cons_of_mem c hl))
    exact Subgroup.subset_closure ⟨c, hp c mem_cons_self, rfl⟩

/-- `u` is a minimal-length representative of its left `W_J`-coset. -/
def IsMinRep (u : W) : Prop :=
  ∀ x : W, SameCosetJ cs J u x → ℓ u ≤ ℓ x

/-- **Every coset has a minimal-length representative** (unconditional —
well-ordering of the lengths). -/
theorem exists_minRep (w : W) :
    ∃ u, SameCosetJ cs J w u ∧ IsMinRep cs J u := by
  classical
  have hne : ∃ n, ∃ x, SameCosetJ cs J w x ∧ ℓ x = n :=
    ⟨ℓ w, w, sameCosetJ_refl cs J w, rfl⟩
  obtain ⟨x, hx, hxlen⟩ := Nat.find_spec hne
  refine ⟨x, hx, fun y hy => ?_⟩
  rw [hxlen]
  exact Nat.find_min' hne ⟨y, sameCosetJ_trans cs J hx hy, rfl⟩

/-- A minimal representative has no right descent in `J` (unconditional —
the length toggle plus coset closure). -/
theorem minRep_not_isRightDescent {u : W} (hu : IsMinRep cs J u)
    {l : B} (hl : l ∈ J) : ¬ cs.IsRightDescent u l := by
  intro hdesc
  have hcoset : SameCosetJ cs J u (u * σ l) := by
    show u⁻¹ * (u * σ l) ∈ parabolic cs J
    rw [← mul_assoc, inv_mul_cancel, one_mul]
    exact Subgroup.subset_closure ⟨l, hl, rfl⟩
  have hge : ℓ u ≤ ℓ (u * σ l) := hu _ hcoset
  exact absurd hge (not_le.mpr hdesc)

/-- A word stays reduced after dropping its last letter. -/
theorem isReduced_of_isReduced_concat {p : List B} {c : B}
    (h : cs.IsReduced (p ++ [c])) : cs.IsReduced p := by
  have h1 : ℓ (π (p ++ [c])) = p.length + 1 := by
    have := h
    unfold IsReduced at this
    simpa using this
  have h2 : π (p ++ [c]) = π p * σ c := by
    rw [wordProd_append]
    simp [wordProd_cons, wordProd_nil]
  have h3 : p.length + 1 ≤ ℓ (π p) + 1 := by
    calc p.length + 1 = ℓ (π (p ++ [c])) := h1.symm
    _ = ℓ (π p * σ c) := by rw [h2]
    _ ≤ ℓ (π p) + ℓ (σ c) := cs.length_mul_le _ _
    _ = ℓ (π p) + 1 := by rw [cs.length_simple]
  have hle : ℓ (π p) ≤ p.length := cs.length_wordProd_le p
  unfold IsReduced
  omega

/-- **THE LIFTING LEMMA** (Bourbaki Lie IV §1 / BB Prop 2.4.4, core form),
conditional on the exchange property: a minimal coset representative `u`
composes length-additively with every reduced `J`-word,
`ℓ(u · π p) = ℓ(u) + |p|`. A failed ascent triggers exchange on the
concatenated reduced word; deletion in the `u`-part contradicts the
minimality of `u`, deletion in the `p`-part contradicts the reducedness of
`p`. This is the fact the merged coset structures' `len_add` fields
encode. -/
theorem length_minRep_mul_wordProd (hexch : RightExchangeProp cs)
    {u : W} (hu : IsMinRep cs J u)
    {p : List B} (hp : ∀ l ∈ p, l ∈ J) (hred : cs.IsReduced p) :
    ℓ (u * π p) = ℓ u + p.length := by
  induction p using List.reverseRecOn with
  | nil => simp
  | append_singleton p' c ih =>
    have hp' : ∀ l ∈ p', l ∈ J := fun l hl => hp l (mem_append_left _ hl)
    have hc : c ∈ J := hp c (by simp)
    have hred' : cs.IsReduced p' := isReduced_of_isReduced_concat cs hred
    have IH : ℓ (u * π p') = ℓ u + p'.length := ih hp' hred'
    have hsplit : π (p' ++ [c]) = π p' * σ c := by
      rw [wordProd_append]
      simp [wordProd_cons, wordProd_nil]
    rw [hsplit, ← mul_assoc]
    rcases cs.length_mul_simple (u * π p') c with hup | hdown
    · rw [hup, IH]
      simp
      omega
    · -- descent at the last letter: derive False
      exfalso
      obtain ⟨ωu, hωlen, hωeq⟩ := cs.exists_reduced_word u
      have hπcat : π (ωu ++ p') = u * π p' := by
        rw [wordProd_append, ← hωeq]
      have hcat_red : cs.IsReduced (ωu ++ p') := by
        unfold IsReduced
        rw [hπcat, IH]
        simp
        omega
      have hdesc : cs.IsRightDescent (π (ωu ++ p')) c := by
        show ℓ (π (ωu ++ p') * σ c) < ℓ (π (ωu ++ p'))
        rw [hπcat]
        omega
      obtain ⟨r, hr⟩ := hexch hcat_red hdesc
      rw [hπcat] at hr
      rcases lt_or_ge r ωu.length with hrlt | hrge
      · -- deletion in the u-part: contradicts minimality of u
        rw [eraseIdx_append_of_lt_length hrlt, wordProd_append] at hr
        -- hr : u * π p' * σ c = π (ωu.eraseIdx r) * π p'
        set u'' := π (ωu.eraseIdx r) with hu''def
        have hval : u⁻¹ * u'' = π p' * σ c * (π p')⁻¹ := by
          have h5 : u'' = u * π p' * σ c * (π p')⁻¹ := by
            rw [hr]
            group
          rw [h5]
          group
        have hcoset : SameCosetJ cs J u u'' := by
          show u⁻¹ * u'' ∈ parabolic cs J
          rw [hval]
          refine (parabolic cs J).mul_mem ((parabolic cs J).mul_mem ?_ ?_)
            ((parabolic cs J).inv_mem ?_)
          · exact wordProd_mem_parabolic cs J hp'
          · exact Subgroup.subset_closure ⟨c, hc, rfl⟩
          · exact wordProd_mem_parabolic cs J hp'
        have hlt : ℓ u'' < ℓ u := by
          have hb : ℓ u'' ≤ (ωu.eraseIdx r).length :=
            cs.length_wordProd_le _
          have hc2 : (ωu.eraseIdx r).length + 1 = ωu.length :=
            List.length_eraseIdx_add_one hrlt
          omega
        exact absurd (hu u'' hcoset) (not_le.mpr hlt)
      · -- deletion in the p'-part: contradicts reducedness of p' ++ [c]
        rw [eraseIdx_append_of_length_le hrge, wordProd_append, ← hωeq, mul_assoc] at hr
        -- hr : u * (π p' * σ c) = u * π (p'.eraseIdx (r - ωu.length))
        have hcancel : π p' * σ c = π (p'.eraseIdx (r - ωu.length)) :=
          mul_left_cancel hr
        have hLlen : ℓ (π p' * σ c) = p'.length + 1 := by
          rw [← hsplit]
          have h6 := hred
          unfold IsReduced at h6
          simpa using h6
        have hRlen : ℓ (π (p'.eraseIdx (r - ωu.length))) ≤ p'.length :=
          (cs.length_wordProd_le _).trans
            (List.eraseIdx_sublist p' (r - ωu.length)).length_le
        rw [hcancel] at hLlen
        omega
