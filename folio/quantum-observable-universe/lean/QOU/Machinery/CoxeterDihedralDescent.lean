import QOU.Machinery.CoxeterRankTwo
import QOU.Machinery.CoxeterGeometricRepresentationFull
import QOU.Machinery.CoxeterDihedralOrder

/-!
# The dihedral descent lemma — the heart of Matsumoto's theorem

If `i` and `j` are **both** right descents of `w`, then `w` has a reduced word whose tail is the
alternating block of length `M i j` — in **both** spellings. One braid move at that tail therefore
converts a reduced word for `w` ending in `i` into one ending in `j`, which is the step the Tits
induction turns on.

## The argument

Cut `w = u · v` with `u` the minimal representative of `w W_J`, `J = {i, j}`
(`CoxeterParabolic.exists_minRep`, `length_minRep_mul_wordProd'`). Length is additive across the
cut, so **both descents pass to `v`**, and the whole question moves into the rank-two parabolic.

There `CoxeterRankTwo` takes over. A reduced word for `v` over two letters is alternating, and a
descent at `c` means some reduced word ends in `c` — so *both* alternating spellings of length
`k = ℓ(v)` are reduced words for `v`. Two spellings with one product force `(s_i s_j)^k = 1`; the
word is reduced so `k ≤ M i j`; the descents make `k ≥ 1`. Exactness of the dihedral order closes
the interval and `k = M i j`.

## Both side conditions are now DERIVED, not assumed

These statements used to carry two hypotheses, `DihedralExact cs` and `M i j ≠ 0`.
`QOU.Machinery.CoxeterDihedralOrder` discharges both from the geometric representation, and this
file spends that input rather than propagating the hypotheses:

* `dihedralExact_full` — the Chebyshev/cosine argument: `⟨αᵢ, (fᵢfⱼ)^k αᵢ⟩ = cos(2πk / m)`, which
  is `1` only at `k = 0` in the range `0 < k < m`.
* `bond_ne_zero_of_pow_eq_one` — the infinite-bond half: at `m = 0` the rotation is a shear whose
  `αᵢ`-coefficient is `1 + 2k`, so `(σᵢσⱼ)^k = 1` with `k > 0` is impossible. That is exactly what
  refutes the `M i j = 0` branch here, where the old `hm` hypothesis excluded it by fiat.

Consequence: the whole Matsumoto/Bruhat arc downstream of this file is unconditional for **every**
Coxeter system, not only type `A` and not only the finite-bond ones.

`dihedralExact_le_three` is kept below. It is now superseded as an *input* — nothing in the arc
needs it — but it is a genuinely different and much more elementary proof of the `M i j ≤ 3` case,
resting only on `CoxeterGeometricRepresentationFull`'s two unconditional cell-faithfulness results
with no trigonometry.

-- Ref: [bjornerbrenti2005] Combinatorics of Coxeter Groups, §3.3
-- Ref: [humphreys1990] Reflection Groups and Coxeter Groups, §5.
-- Ref: [leitner2026] beans qou-06h7, qou-1u90
-/

namespace QOU.Machinery.CoxeterDihedralDescent

open CoxeterSystem List
open QOU.Machinery.CoxeterParabolic QOU.Machinery.CoxeterRankTwo
open QOU.Machinery.CoxeterDihedralOrder

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd
local prefix:100 "σ" => cs.simple

/-! ## Length is additive across a minimal-representative cut -/

/-- `ℓ(u · v) = ℓ(u) + ℓ(v)` for `u` a minimal coset representative and `v ∈ W_J`. The element
form of `length_minRep_mul_wordProd'`, obtained by choosing an ambient-reduced `J`-word for `v`. -/
theorem length_minRep_mul (J : Set B) {u : W} (hu : IsMinRep cs J u)
    {v : W} (hv : v ∈ parabolic cs J) : ℓ (u * v) = ℓ u + ℓ v := by
  obtain ⟨p, hp, hred, rfl⟩ := exists_reducedWord_of_mem_parabolic cs hv
  rw [length_minRep_mul_wordProd' cs J hu hp hred]
  exact congrArg _ hred.symm

/-- **Descents pass through the cut.** A right descent of `u · v` lying in `J` is a right descent
of `v`. -/
theorem isRightDescent_of_minRep_mul (J : Set B) {u : W} (hu : IsMinRep cs J u)
    {v : W} (hv : v ∈ parabolic cs J) {c : B} (hc : c ∈ J)
    (h : cs.IsRightDescent (u * v) c) : cs.IsRightDescent v c := by
  have hσ : σ c ∈ parabolic cs J := Subgroup.subset_closure ⟨c, hc, rfl⟩
  have h1 := length_minRep_mul cs J hu hv
  have h2 := length_minRep_mul cs J hu ((parabolic cs J).mul_mem hv hσ)
  have h3 : ℓ (u * v * σ c) < ℓ (u * v) := h
  rw [mul_assoc] at h3
  show ℓ (v * σ c) < ℓ v
  omega

/-! ## Both spellings are reduced words for a doubly-descending rank-two element -/

private theorem append_singleton_inj {l₁ l₂ : List B} {a b : B}
    (h : l₁ ++ [a] = l₂ ++ [b]) : a = b := by
  have h2 := congrArg List.getLast? h
  simpa using h2

/-- A right descent is witnessed by a reduced `J`-word ending in that letter, when the element
lies in `W_J`. -/
theorem exists_reducedWord_concat (J : Set B) {v : W} (hv : v ∈ parabolic cs J)
    {c : B} (hc : c ∈ J) (h : cs.IsRightDescent v c) :
    ∃ p : List B, (∀ l ∈ p, l ∈ J) ∧ cs.IsReduced (p ++ [c]) ∧ π (p ++ [c]) = v := by
  have hσ : σ c ∈ parabolic cs J := Subgroup.subset_closure ⟨c, hc, rfl⟩
  obtain ⟨p, hp, hred, hpv⟩ :=
    exists_reducedWord_of_mem_parabolic cs ((parabolic cs J).mul_mem hv hσ)
  have hprod : π (p ++ [c]) = v := by
    rw [cs.wordProd_append, cs.wordProd_singleton, hpv, mul_assoc,
      cs.simple_mul_simple_self, mul_one]
  refine ⟨p, hp, ?_, hprod⟩
  have hlen : p.length = ℓ v - 1 := by
    have h1 : ℓ (v * σ c) = p.length := hred.symm ▸ congrArg cs.length hpv.symm
    have h2 : ℓ (v * σ c) < ℓ v := h
    have h3 : ℓ v ≤ ℓ (v * σ c) + 1 := by
      have := cs.length_mul_le (v * σ c) (σ c)
      rw [mul_assoc, cs.simple_mul_simple_self, mul_one, cs.length_simple] at this
      exact this
    omega
  have hvpos : 0 < ℓ v := by
    have h2 : ℓ (v * σ c) < ℓ v := h
    omega
  show ℓ (π (p ++ [c])) = (p ++ [c]).length
  rw [hprod]
  have h1 : ℓ (v * σ c) = p.length := hred.symm ▸ congrArg cs.length hpv.symm
  have h2 : ℓ (v * σ c) < ℓ v := h
  have h3 : ℓ v ≤ ℓ (v * σ c) + 1 := by
    have := cs.length_mul_le (v * σ c) (σ c)
    rw [mul_assoc, cs.simple_mul_simple_self, mul_one, cs.length_simple] at this
    exact this
  simp only [List.length_append, List.length_singleton]
  omega

/-- **The rank-two core.** An element of `W_{i,j}` with both `i` and `j` as right descents is the
product of **both** alternating words of length `M i j`, each of them reduced. -/
theorem alternatingWord_reduced_of_both_descents
    {i j : B} (hij : i ≠ j) {v : W}
    (hv : v ∈ parabolic cs ({i, j} : Set B))
    (hi : cs.IsRightDescent v i) (hj : cs.IsRightDescent v j) :
    0 < M i j ∧
      cs.IsReduced (alternatingWord i j (M i j)) ∧
      π (alternatingWord i j (M i j)) = v ∧
      cs.IsReduced (alternatingWord j i (M i j)) ∧
      π (alternatingWord j i (M i j)) = v := by
  classical
  set J : Set B := ({i, j} : Set B) with hJ
  have hiJ : i ∈ J := by simp [hJ]
  have hjJ : j ∈ J := by simp [hJ]
  -- A reduced `J`-word ending in `i`, and one ending in `j`.
  obtain ⟨pi, hpi, hpired, hpiv⟩ := exists_reducedWord_concat cs J hv hiJ hi
  obtain ⟨pj, hpj, hpjred, hpjv⟩ := exists_reducedWord_concat cs J hv hjJ hj
  set k : ℕ := ℓ v with hk
  have hlen_i : (pi ++ [i]).length = k := by
    have := hpired; unfold CoxeterSystem.IsReduced at this; rw [hpiv] at this; omega
  have hlen_j : (pj ++ [j]).length = k := by
    have := hpjred; unfold CoxeterSystem.IsReduced at this; rw [hpjv] at this; omega
  have hmem_i : ∀ l ∈ pi ++ [i], l = i ∨ l = j := by
    intro l hl
    rcases List.mem_append.mp hl with h | h
    · have := hpi l h; simpa [hJ] using this
    · simp at h; exact Or.inl h
  have hmem_j : ∀ l ∈ pj ++ [j], l = i ∨ l = j := by
    intro l hl
    rcases List.mem_append.mp hl with h | h
    · have := hpj l h; simpa [hJ] using this
    · simp at h; exact Or.inr h
  -- `k ≥ 1`, so both alternating words have a last letter.
  have hkpos : 0 < k := by
    have h2 : ℓ (v * σ i) < ℓ v := hi
    omega
  obtain ⟨k', hk'⟩ : ∃ k', k = k' + 1 := ⟨k - 1, by omega⟩
  -- Identify each word by its last letter.
  have hAi : pi ++ [i] = alternatingWord j i k := by
    rcases isReduced_pair_eq_alternatingWord cs (i := i) (j := j) _ hpired hmem_i with h | h
    · exfalso
      rw [hlen_i, hk', alternatingWord_succ, List.concat_eq_append] at h
      exact hij (append_singleton_inj h)
    · rwa [hlen_i] at h
  have hAj : pj ++ [j] = alternatingWord i j k := by
    rcases isReduced_pair_eq_alternatingWord cs (i := i) (j := j) _ hpjred hmem_j with h | h
    · rwa [hlen_j] at h
    · exfalso
      rw [hlen_j, hk', alternatingWord_succ, List.concat_eq_append] at h
      exact hij (append_singleton_inj h).symm
  -- Both spellings are reduced words for `v`.
  have hredAi : cs.IsReduced (alternatingWord j i k) := hAi ▸ hpired
  have hredAj : cs.IsReduced (alternatingWord i j k) := hAj ▸ hpjred
  have hprodAi : π (alternatingWord j i k) = v := hAi ▸ hpiv
  have hprodAj : π (alternatingWord i j k) = v := hAj ▸ hpjv
  -- Hence `(s i s j)^k = 1`, and `k` is squeezed onto `M i j`.
  have hpow : (σ i * σ j) ^ k = 1 :=
    pow_eq_one_of_alternatingWord_eq cs (hprodAj.trans hprodAi.symm)
  -- The bond is finite: an infinite bond has `fᵢfⱼ` of infinite order, contradicting `hpow`.
  have hm : M i j ≠ 0 := bond_ne_zero_of_pow_eq_one cs hij hkpos hpow
  have hkle : k ≤ M i j := by
    by_contra hcon
    exact cs.not_isReduced_alternatingWord i j hm (by omega) hredAj
  have hkeq : k = M i j := by
    rcases Nat.lt_or_ge k (M i j) with hlt | hge
    · exact absurd hpow (dihedralExact_full cs i j hij k hkpos hlt)
    · omega
  refine ⟨hkeq ▸ hkpos, ?_⟩
  rw [← hkeq]
  exact ⟨hredAj, hprodAj, hredAi, hprodAi⟩

/-! ## The descent lemma proper -/

/-- **The dihedral descent lemma.** If `i` and `j` are both right descents of `w`, then the bond
order `M i j` is finite and positive, and `w` has a reduced word whose tail is the alternating
block of length `M i j` — in both spellings, with the same prefix. A single braid move at that tail
moves between them.

The `0 < M i j` conjunct is *derived*, not assumed: two distinct descents give `(σᵢσⱼ)^k = 1` for
`k = ℓ(v) > 0`, and `CoxeterDihedralOrder.bond_ne_zero_of_pow_eq_one` refutes that at an infinite
bond. It is returned rather than left to the caller because the caller needs it to split off the
tail's last letter. -/
theorem exists_reduced_alternating_tail
    {i j : B} (hij : i ≠ j) {w : W}
    (hi : cs.IsRightDescent w i) (hj : cs.IsRightDescent w j) :
    0 < M i j ∧ ∃ l₁ : List B,
      cs.IsReduced (l₁ ++ alternatingWord i j (M i j)) ∧
        π (l₁ ++ alternatingWord i j (M i j)) = w ∧
        cs.IsReduced (l₁ ++ alternatingWord j i (M i j)) ∧
        π (l₁ ++ alternatingWord j i (M i j)) = w := by
  classical
  set J : Set B := ({i, j} : Set B) with hJ
  have hiJ : i ∈ J := by simp [hJ]
  have hjJ : j ∈ J := by simp [hJ]
  obtain ⟨u, hcos, hmin⟩ := exists_minRep cs J w
  -- `w = u * v` with `v = (w⁻¹ u)⁻¹ ∈ W_J`.
  set v : W := (w⁻¹ * u)⁻¹ with hvdef
  have hv : v ∈ parabolic cs J := (parabolic cs J).inv_mem hcos
  have hwuv : w = u * v := by
    rw [hvdef, mul_inv_rev, inv_inv, ← mul_assoc, mul_inv_cancel, one_mul]
  -- Both descents pass to `v`.
  have hvi : cs.IsRightDescent v i :=
    isRightDescent_of_minRep_mul cs J hmin hv hiJ (by rw [← hwuv]; exact hi)
  have hvj : cs.IsRightDescent v j :=
    isRightDescent_of_minRep_mul cs J hmin hv hjJ (by rw [← hwuv]; exact hj)
  obtain ⟨hmpos, hredA, hprodA, hredB, hprodB⟩ :=
    alternatingWord_reduced_of_both_descents cs hij hv hvi hvj
  obtain ⟨l₁, hl₁len, hl₁⟩ := cs.exists_reduced_word u
  have hlu : ℓ (u * v) = ℓ u + ℓ v := length_minRep_mul cs J hmin hv
  have hkey : ∀ A : List B, cs.IsReduced A → π A = v →
      cs.IsReduced (l₁ ++ A) ∧ π (l₁ ++ A) = w := by
    intro A hA hAv
    have hprod : π (l₁ ++ A) = w := by
      rw [cs.wordProd_append, ← hl₁, hAv, ← hwuv]
    refine ⟨?_, hprod⟩
    show ℓ (π (l₁ ++ A)) = (l₁ ++ A).length
    rw [hprod, hwuv, hlu]
    have hAlen : A.length = ℓ v := by
      have := hA; unfold CoxeterSystem.IsReduced at this; rw [hAv] at this; omega
    simp only [List.length_append, hl₁len, hAlen]
  exact ⟨hmpos, l₁, (hkey _ hredA hprodA).1, (hkey _ hredA hprodA).2,
    (hkey _ hredB hprodB).1, (hkey _ hredB hprodB).2⟩

/-! ## `DihedralExact` for `M i j ≤ 3` — an elementary proof, no longer load-bearing -/

/-- **`s_i s_j` has order exactly `M i j` whenever `M i j ≤ 3`.**

Both cases come from `CoxeterGeometricRepresentationFull`'s unconditional cell faithfulness:
`[i, j]` reduced at `M i j = 2` and `[i, j, i]` reduced at `M i j = 3`. If a smaller power were
trivial the corresponding word would collapse to something of length `≤ 1`.

**Superseded as an input** by `CoxeterDihedralOrder.dihedralExact_full`, which proves the same
predicate for every `M i j`. Kept because the argument is independent and elementary — no
trigonometry, no Chebyshev recursion — so it is a cheap cross-check on the general result at the
only bond orders type `A` ever uses. -/
theorem dihedralExact_le_three (hle : ∀ i j : B, M i j ≤ 3) : DihedralExact cs := by
  intro i j hij k hkpos hklt
  have hne1 : M i j ≠ 1 := M.off_diagonal i j hij
  have hm : M i j = 2 ∨ M i j = 3 := by
    have h1 := hle i j
    omega
  -- `s i * s j ≠ 1` in both cases.
  have hne : σ i * σ j ≠ 1 := by
    intro hcon
    have hsij : σ i = σ j := by
      have := congrArg (· * σ j) hcon
      simpa [mul_assoc, cs.simple_mul_simple_self] using this
    rcases hm with h2 | h3
    · have hr := QOU.Machinery.CoxeterParabolic.isReduced_ij_unconditional cs h2
      have : ℓ (π [i, j]) = 2 := by
        have := hr; unfold CoxeterSystem.IsReduced at this; simpa using this
      rw [show π [i, j] = σ i * σ j by simp [cs.wordProd_cons], hcon] at this
      simp at this
    · have hr := QOU.Machinery.CoxeterParabolic.isReduced_iji_unconditional cs h3
      have h3' : ℓ (π [i, j, i]) = 3 := by
        have := hr; unfold CoxeterSystem.IsReduced at this; simpa using this
      have hval : π [i, j, i] = σ i := by
        rw [show π [i, j, i] = σ i * σ j * σ i by simp [cs.wordProd_cons, mul_assoc], hcon,
          one_mul]
      rw [hval, cs.length_simple] at h3'
      omega
  rcases hm with h2 | h3
  · -- `k < 2` forces `k = 1`.
    have hk1 : k = 1 := by omega
    rw [hk1, pow_one]
    exact hne
  · -- `k < 3` forces `k = 1` or `k = 2`.
    rcases (by omega : k = 1 ∨ k = 2) with hk1 | hk2
    · rw [hk1, pow_one]; exact hne
    · rw [hk2]
      intro hcon
      have hr := QOU.Machinery.CoxeterParabolic.isReduced_iji_unconditional cs h3
      have h3' : ℓ (π [i, j, i]) = 3 := by
        have := hr; unfold CoxeterSystem.IsReduced at this; simpa using this
      -- `(s i s j)^2 = 1` means `s i s j s i = s j`, a length-1 element.
      have hval : π [i, j, i] = σ j := by
        -- `(s i s j)² = 1` says `s i s j` is its own inverse, i.e. equals `s j s i`.
        have hgg : σ i * σ j = (σ i * σ j)⁻¹ :=
          mul_eq_one_iff_eq_inv.mp (by rwa [pow_two] at hcon)
        rw [show π [i, j, i] = σ i * σ j * σ i by simp [cs.wordProd_cons, mul_assoc], hgg,
          mul_inv_rev, cs.inv_simple, cs.inv_simple, mul_assoc, cs.simple_mul_simple_self,
          mul_one]
      rw [hval, cs.length_simple] at h3'
      omega

end QOU.Machinery.CoxeterDihedralDescent
