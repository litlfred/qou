import QOU.Machinery.CoxeterDeletion

/-!
# Rank-two words: reduced words over two letters are alternating

Matsumoto's theorem reduces, by the classical Tits argument, to one statement about a **rank-two
parabolic**: if `i` and `j` are both right descents of `w`, then `w` has a reduced word whose tail
is the alternating block of length `M i j`. This file develops the rank-two half of that.

## What is here

* **`not_isReduced_concat_self`** — a reduced word has no two adjacent equal letters, because
  `s c s c = 1` deletes them.
* **`isReduced_pair_eq_alternatingWord`** — hence a reduced word all of whose letters lie in
  `{i, j}` **is** one of the two alternating words of its length. This is what makes the rank-two
  case finite-dimensional: there are at most two reduced words of each length.
* **`exists_word_of_mem_parabolic`** / **`exists_reducedWord_of_mem_parabolic`** — every element of
  `W_J` is the product of a `J`-word, and a `J`-word of minimal length is **ambient-reduced**. The
  second is where `CoxeterDeletion.exists_deletion` is spent: without it, a shorter `J`-word need
  not exist and the parabolic could a priori sit non-isometrically inside `W`.
* **`pow_eq_one_of_alternatingWord_eq`** — if the two alternating words of length `k` have the same
  product then `(s i s j)^k = 1`. This is the bridge from words to the **order** of `s i s j`, which
  is the one genuinely missing input (see below).

## 🛑 The input this file does NOT supply

`QOU.Machinery.CoxeterGeometricRepresentationFull` states its own honesty note: it proves
simple-injectivity but **not** "the order of `σᵢσⱼ` being exactly `mᵢⱼ`". That is precisely the
predicate `DihedralExact` isolated here, and it is left as an explicit hypothesis rather than
assumed — it is discharged for `M i j ≤ 3` in `CoxeterDihedralDescent`, which covers type `A`.

-- Ref: [bjornerbrenti2005] Combinatorics of Coxeter Groups, §1.4, §3.3
-- Ref: [humphreys1990] Reflection Groups and Coxeter Groups, §1.6, §5.
-- Ref: [leitner2026] bean qou-06h7
-/

namespace QOU.Machinery.CoxeterRankTwo

open CoxeterSystem List
open QOU.Machinery.CoxeterParabolic QOU.Machinery.CoxeterDeletion

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd
local prefix:100 "σ" => cs.simple

/-! ## A reduced word has no adjacent repeats -/

/-- **`… c c …` is never reduced.** The two copies cancel, so the product is that of a strictly
shorter word. -/
theorem not_isReduced_concat_self (l : List B) (c : B) :
    ¬ cs.IsReduced (l ++ [c] ++ [c]) := by
  intro h
  have hprod : π (l ++ [c] ++ [c]) = π l := by
    rw [cs.wordProd_append, cs.wordProd_append, cs.wordProd_singleton, mul_assoc,
      cs.simple_mul_simple_self, mul_one]
  have h1 : ℓ (π (l ++ [c] ++ [c])) = l.length + 2 := by
    have h2 := h
    unfold CoxeterSystem.IsReduced at h2
    simpa using h2
  rw [hprod] at h1
  have h2 : ℓ (π l) ≤ l.length := cs.length_wordProd_le l
  omega

/-! ## Reduced two-letter words are alternating -/

/-- **The rank-two structure theorem.** A reduced word whose letters all lie in `{i, j}` is one of
the two alternating words of its length — so a rank-two parabolic has at most two reduced words per
length, which is what makes the dihedral analysis finite. -/
theorem isReduced_pair_eq_alternatingWord {i j : B} :
    ∀ ω : List B, cs.IsReduced ω → (∀ l ∈ ω, l = i ∨ l = j) →
      ω = alternatingWord i j ω.length ∨ ω = alternatingWord j i ω.length := by
  intro ω
  induction ω using List.reverseRecOn with
  | nil => intro _ _; left; rfl
  | append_singleton ω' c ih =>
    intro hred hmem
    have hred' : cs.IsReduced ω' := isReduced_of_isReduced_concat cs hred
    have hmem' : ∀ l ∈ ω', l = i ∨ l = j := fun l hl => hmem l (mem_append_left _ hl)
    have hc : c = i ∨ c = j := hmem c (by simp)
    have hlen : (ω' ++ [c]).length = ω'.length + 1 := by simp
    rcases Nat.eq_zero_or_pos ω'.length with hn | hn
    · have hnil : ω' = [] := List.length_eq_zero_iff.mp hn
      subst hnil
      rcases hc with rfl | rfl
      · right; rw [hlen]; rfl
      · left; rw [hlen]; rfl
    · obtain ⟨n, hn'⟩ : ∃ n, ω'.length = n + 1 := ⟨ω'.length - 1, by omega⟩
      rcases ih hred' hmem' with hIH | hIH
      · -- `ω' = alternatingWord i j |ω'|`, which ends in `j`.
        rcases hc with rfl | rfl
        · right
          rw [hlen, hIH, length_alternatingWord, alternatingWord_succ, List.concat_eq_append]
        · exfalso
          rw [hn'] at hIH
          have hsplit : ω' = alternatingWord c i n ++ [c] := by
            rw [hIH, alternatingWord_succ]; simp
          exact not_isReduced_concat_self cs (alternatingWord c i n) c (by
            rw [← hsplit]; exact hred)
      · -- `ω' = alternatingWord j i |ω'|`, which ends in `i`.
        rcases hc with rfl | rfl
        · exfalso
          rw [hn'] at hIH
          have hsplit : ω' = alternatingWord c j n ++ [c] := by
            rw [hIH, alternatingWord_succ]; simp
          exact not_isReduced_concat_self cs (alternatingWord c j n) c (by
            rw [← hsplit]; exact hred)
        · left
          rw [hlen, hIH, length_alternatingWord, alternatingWord_succ, List.concat_eq_append]

/-! ## Parabolic subgroups are spanned by words, isometrically -/

/-- Every element of `W_J` is the product of a word with letters in `J`. -/
theorem exists_word_of_mem_parabolic {J : Set B} {v : W} (hv : v ∈ parabolic cs J) :
    ∃ p : List B, (∀ l ∈ p, l ∈ J) ∧ π p = v := by
  refine Subgroup.closure_induction
    (p := fun x _ => ∃ p : List B, (∀ l ∈ p, l ∈ J) ∧ π p = x) ?_ ?_ ?_ ?_ hv
  · rintro x ⟨l, hl, rfl⟩
    exact ⟨[l], by simpa using hl, by simp⟩
  · exact ⟨[], by simp, by simp⟩
  · rintro x y _ _ ⟨p, hp, rfl⟩ ⟨p', hp', rfl⟩
    refine ⟨p ++ p', ?_, by rw [cs.wordProd_append]⟩
    intro l hl
    rcases List.mem_append.mp hl with h | h
    · exact hp l h
    · exact hp' l h
  · rintro x _ ⟨p, hp, rfl⟩
    exact ⟨p.reverse, fun l hl => hp l (List.mem_reverse.mp hl), by rw [cs.wordProd_reverse]⟩

/-- **The parabolic embeds isometrically.** An element of `W_J` has a `J`-word that is reduced in
the **ambient** system — so its `W_J`-length and its `W`-length agree.

This is where the deletion condition is spent: a `J`-word that is not ambient-reduced admits a
two-letter deletion, and the result is again a `J`-word, so a minimal-length `J`-word is reduced. -/
theorem exists_reducedWord_of_mem_parabolic {J : Set B} {v : W} (hv : v ∈ parabolic cs J) :
    ∃ p : List B, (∀ l ∈ p, l ∈ J) ∧ cs.IsReduced p ∧ π p = v := by
  classical
  have hne : ∃ n, ∃ p : List B, (∀ l ∈ p, l ∈ J) ∧ π p = v ∧ p.length = n := by
    obtain ⟨p, hp, hpv⟩ := exists_word_of_mem_parabolic cs hv
    exact ⟨p.length, p, hp, hpv, rfl⟩
  set n := Nat.find hne with hn
  obtain ⟨p, hp, hpv, hplen⟩ := Nat.find_spec hne
  refine ⟨p, hp, ?_, hpv⟩
  by_contra hnr
  obtain ⟨a, b, hab, hb, heq⟩ := exists_deletion cs p hnr
  set p' := (p.eraseIdx b).eraseIdx a with hp'
  have hsub : p' <+ p := ((p.eraseIdx b).eraseIdx_sublist a).trans (p.eraseIdx_sublist b)
  have hlb : (p.eraseIdx b).length = p.length - 1 := List.length_eraseIdx_of_lt hb
  have ha2 : a < (p.eraseIdx b).length := by omega
  have hla : p'.length = (p.eraseIdx b).length - 1 := List.length_eraseIdx_of_lt ha2
  have hlt : p'.length < n := by omega
  exact absurd (Nat.find_min' hne
    ⟨p', fun l hl => hp l (hsub.mem hl), by rw [← heq]; exact hpv, rfl⟩) (by omega)

/-! ## From two spellings to the order of `s i · s j` -/

/-- **The alternating-word product, closed form** — the even case. -/
theorem wordProd_alternatingWord_two_mul (i j : B) (p : ℕ) :
    π (alternatingWord i j (2 * p)) = (σ i * σ j) ^ p := by
  rw [cs.prod_alternatingWord_eq_mul_pow, if_pos ⟨p, by ring⟩, one_mul]
  congr 1
  omega

/-- The odd case. -/
theorem wordProd_alternatingWord_two_mul_add_one (i j : B) (p : ℕ) :
    π (alternatingWord i j (2 * p + 1)) = σ j * (σ i * σ j) ^ p := by
  rw [cs.prod_alternatingWord_eq_mul_pow, if_neg (by simp [parity_simps])]
  congr 2
  omega

/-- `s j · s i` is the inverse of `s i · s j`. -/
theorem simple_mul_simple_inv (i j : B) : (σ i * σ j)⁻¹ = σ j * σ i := by
  rw [mul_inv_rev, cs.inv_simple, cs.inv_simple]

/-- **The two spellings agree only at a power that is trivial.** If the two alternating words of
length `k` have the same product, then `(s i s j)^k = 1`.

This is the step that converts the word-level ambiguity into a statement about the **order** of
`s i s j`, and it is the reason `DihedralExact` below is exactly the input Matsumoto needs. -/
theorem pow_eq_one_of_alternatingWord_eq {i j : B} {k : ℕ}
    (h : π (alternatingWord i j k) = π (alternatingWord j i k)) :
    (σ i * σ j) ^ k = 1 := by
  rcases Nat.even_or_odd k with ⟨p, hp⟩ | ⟨p, hp⟩
  · have hk : k = 2 * p := by omega
    subst hk
    rw [wordProd_alternatingWord_two_mul, wordProd_alternatingWord_two_mul] at h
    have hinv : (σ j * σ i) ^ p = ((σ i * σ j) ^ p)⁻¹ := by
      rw [← simple_mul_simple_inv, inv_pow]
    rw [hinv] at h
    rw [show 2 * p = p + p by ring, pow_add]
    nth_rewrite 2 [h]
    exact mul_inv_cancel _
  · have hk : k = 2 * p + 1 := by omega
    subst hk
    rw [wordProd_alternatingWord_two_mul_add_one, wordProd_alternatingWord_two_mul_add_one] at h
    -- `s j · g^p = s i · (g⁻¹)^p` with `g = s i * s j`
    have hinv : (σ j * σ i) ^ p = ((σ i * σ j) ^ p)⁻¹ := by
      rw [← simple_mul_simple_inv, inv_pow]
    rw [hinv] at h
    have h2 : (σ i * σ j) * (σ i * σ j) ^ p = ((σ i * σ j) ^ p)⁻¹ := by
      calc (σ i * σ j) * (σ i * σ j) ^ p
          = σ i * (σ j * (σ i * σ j) ^ p) := by rw [mul_assoc]
        _ = σ i * (σ i * ((σ i * σ j) ^ p)⁻¹) := by rw [h]
        _ = ((σ i * σ j) ^ p)⁻¹ := by
            rw [← mul_assoc, cs.simple_mul_simple_self, one_mul]
    have h3 : (σ i * σ j) ^ (p + 1) * (σ i * σ j) ^ p = 1 := by
      rw [pow_succ']
      rw [h2, inv_mul_cancel]
    rw [← pow_add] at h3
    rw [show 2 * p + 1 = p + 1 + p by ring]
    exact h3

/-! ## The missing input, isolated -/

/-- **`s i · s j` has order exactly `M i j`.** One direction — `(s i s j)^{M i j} = 1` — is the
defining relation and holds always; what this predicate adds is that no **smaller** positive power
is trivial.

`CoxeterGeometricRepresentationFull` proves simple-injectivity and says in its own honesty note
that it does **not** prove this. It is therefore carried as a hypothesis and discharged where it can
be: `M i j ≤ 3`, which is every off-diagonal entry of type `A`. -/
def DihedralExact : Prop :=
  ∀ i j : B, i ≠ j → ∀ k : ℕ, 0 < k → k < M i j → (cs.simple i * cs.simple j) ^ k ≠ 1

end QOU.Machinery.CoxeterRankTwo
