import QOU.Mathlib.PrincipalSchurHook
import QOU.SchurWeyl.HookDivisibility

/-!
# QOU.Mathlib.MajFormula — the `maj` generating function of standard Young tableaux

**Theorem** (`fmaj_mul_hook`).  For every Young diagram `μ` with `n` cells, in `ℤ[X]`,

`(∑_{S ∈ SYT(μ)} X^{maj S}) · ∏_{c ∈ μ} (1 − X^{h(c)}) = X^{n(μ)} · ∏_{m=1}^{n} (1 − X^m)`,

i.e. `∑_S q^{maj S} = q^{n(μ)} [n]_q! / ∏_c [h(c)]_q` (Stanley, *EC2* Cor. 7.21.5), cleared of
denominators.

The proof is the standard one, assembled from three corpus results:

* `MajStandardization.stdEquivSigma` — reverse semistandard tableaux are pairs
  (standard tableau, weakly decreasing sequence) with `|T| = maj S + |b|`;
* `PrincipalSchur.hook_mul_bsum_principal` — the hook-content formula
  `H(μ) · B_N(μ) = X^{e(μ)} · E_N(μ)`, where `B_N(μ)` is the sum over reverse tableaux with
  entries `< N` and `E_N(μ) ≡ 1 mod X^{N+1−ℓ(μ)}`;
* the same for the one-row diagram, whose unique standard tableau has `maj = 0`.

Comparing the two below degree `N` and letting `N` grow gives the identity.

| | |
|---|---|
| `bsum_sub_dvd` | `X^N ∣ B_N(μ) − f_μ · D_N(n)` — standardization, truncated |
| `dvd_prod_sub_one` | `X^K ∣ E_N(μ) − 1` once `K + ℓ(μ) ≤ N + 1` |
| `fmaj_rowYD` | the one-row diagram has `f = 1` |
| `fmaj_mul_hook` | **the `maj` formula** |
| `fmaj_mul_qHook` | the same in `q`-integers: `f_μ · ∏_c [h(c)] = X^{n(μ)} · [n]!` |
| `qFactorial_eq_schurElt_mul_fmaj` | `[n]_Q! = c_λ(Q) · f_λ(Q)` for the Schur element `c_λ` |
| `coeff_fmaj_nonneg` | so `[n]_Q!/c_λ` has nonnegative integer coefficients (bean `qou-q3q2`) |

## Base ring (§7c)

`ℤ[X]`: the statement is an identity of integer polynomials, so it specialises to every
commutative ring.  The intermediate congruences are generic.

LaTeX label: `thm:maj-hook-formula`
-/

namespace QOU.Mathlib.MajFormula

open Finset YoungDiagram Polynomial QOU.Mathlib.MajStandardization QOU.Mathlib.RSSYTSchur
  QOU.Mathlib.PrincipalSchur

noncomputable instance (μ : YoungDiagram) : Fintype (SYTe μ) := by
  classical
  exact Fintype.ofInjective (fun S : SYTe μ => S.e) (fun S S' h => SYTe.ext' h)

/-- `f_μ = ∑_{S ∈ SYT(μ)} X^{maj S}`. -/
noncomputable def fmaj (μ : YoungDiagram) : ℤ[X] := ∑ S : SYTe μ, X ^ S.maj

/-- `D_N(n)`: weakly decreasing sequences of length `n` with entries `< N`, weighted by `X^{|b|}`. -/
noncomputable def DN (N n : ℕ) : ℤ[X] := by
  classical
  exact ∑ b ∈ univ.filter (fun b : Fin n → Fin N => Antitone (fun k => (b k : ℕ))),
    X ^ (∑ k, (b k : ℕ))

theorem part_le_sum {μ : YoungDiagram} (x : Σ _ : SYTe μ, DecSeq μ.cells.card)
    (k : Fin μ.cells.card) : x.2.1 k ≤ ∑ c, (stdEquivSigma μ x).1 c := by
  rw [sum_stdEquivSigma]
  exact le_add_left (single_le_sum (fun _ _ => Nat.zero_le _) (mem_univ k))

theorem entry_le_sum {μ : YoungDiagram} (y : RSSYT μ) (c : Cell μ) : y.1 c ≤ ∑ c', y.1 c' :=
  single_le_sum (fun _ _ => Nat.zero_le _) (mem_univ c)

section Truncation

variable {μ : YoungDiagram} {N d : ℕ}

/-- The standardization of a bounded tableau of weight `d < N`, with `b` bounded by `N`. -/
noncomputable def toPair (hd : d < N) (T : Cell μ → Fin N)
    (hT : IsBT T ∧ d = ∑ c, (T c : ℕ)) : SYTe μ × (Fin μ.cells.card → Fin N) :=
  let x := (stdEquivSigma μ).symm ⟨fun c => (T c : ℕ), hT.1⟩
  (x.1, fun k => ⟨x.2.1 k, by
    have := part_le_sum x k
    rw [Equiv.apply_symm_apply] at this
    have h := hT.2
    dsimp only at this
    omega⟩)

/-- The inverse: `Φ(S, b)` with entries bounded by `N`. -/
noncomputable def toTab (hd : d < N) (p : SYTe μ × (Fin μ.cells.card → Fin N))
    (hp : Antitone (fun k => (p.2 k : ℕ)) ∧ d = p.1.maj + ∑ k, (p.2 k : ℕ)) : Cell μ → Fin N :=
  let y := stdEquivSigma μ ⟨p.1, ⟨fun k => (p.2 k : ℕ), hp.1⟩⟩
  fun c => ⟨y.1 c, by
    have := entry_le_sum y c
    rw [sum_stdEquivSigma] at this
    have h := hp.2
    dsimp only at this
    omega⟩

theorem toTab_isBT (hd : d < N) (p : SYTe μ × (Fin μ.cells.card → Fin N))
    (hp : Antitone (fun k => (p.2 k : ℕ)) ∧ d = p.1.maj + ∑ k, (p.2 k : ℕ)) :
    IsBT (toTab hd p hp) ∧ d = ∑ c, (toTab hd p hp c : ℕ) := by
  refine ⟨(stdEquivSigma μ ⟨p.1, ⟨fun k => (p.2 k : ℕ), hp.1⟩⟩).2, ?_⟩
  have hs := sum_stdEquivSigma (μ := μ) ⟨p.1, ⟨fun k => (p.2 k : ℕ), hp.1⟩⟩
  have h := hp.2
  unfold toTab
  dsimp only at hs ⊢
  omega

theorem toPair_mem (hd : d < N) (T : Cell μ → Fin N) (hT : IsBT T ∧ d = ∑ c, (T c : ℕ)) :
    Antitone (fun k => ((toPair hd T hT).2 k : ℕ)) ∧
      d = (toPair hd T hT).1.maj + ∑ k, ((toPair hd T hT).2 k : ℕ) := by
  have hs := sum_stdEquivSigma ((stdEquivSigma μ).symm ⟨fun c => (T c : ℕ), hT.1⟩)
  rw [Equiv.apply_symm_apply] at hs
  refine ⟨((stdEquivSigma μ).symm ⟨fun c => (T c : ℕ), hT.1⟩).2.2, ?_⟩
  have h := hT.2
  unfold toPair
  dsimp only at hs ⊢
  omega

theorem toTab_toPair (hd : d < N) (T : Cell μ → Fin N) (hT : IsBT T ∧ d = ∑ c, (T c : ℕ)) :
    toTab hd (toPair hd T hT) (toPair_mem hd T hT) = T := by
  funext c
  apply Fin.ext
  unfold toTab toPair
  exact congrArg (fun y : RSSYT μ => y.1 c) ((stdEquivSigma μ).apply_symm_apply ⟨fun c => (T c : ℕ), hT.1⟩)

theorem toPair_toTab (hd : d < N) (p : SYTe μ × (Fin μ.cells.card → Fin N))
    (hp : Antitone (fun k => (p.2 k : ℕ)) ∧ d = p.1.maj + ∑ k, (p.2 k : ℕ)) :
    toPair hd (toTab hd p hp) (toTab_isBT hd p hp) = p := by
  have e : (stdEquivSigma μ).symm (stdEquivSigma μ ⟨p.1, ⟨fun k => (p.2 k : ℕ), hp.1⟩⟩)
      = ⟨p.1, ⟨fun k => (p.2 k : ℕ), hp.1⟩⟩ := Equiv.symm_apply_apply _ _
  unfold toPair toTab
  refine Prod.ext ?_ ?_
  · exact congrArg Sigma.fst e
  · funext k
    apply Fin.ext
    exact congrFun (congrArg (fun x : Σ _ : SYTe μ, DecSeq μ.cells.card => x.2.1) e) k

end Truncation

/-- **Standardization, truncated below degree `N`.** -/
theorem bsum_sub_dvd (μ : YoungDiagram) (N : ℕ) :
    (X : ℤ[X]) ^ N ∣ bsum μ N (fun i : Fin N => (X : ℤ[X]) ^ (i : ℕ)) - fmaj μ * DN N μ.cells.card := by
  classical
  rw [X_pow_dvd_iff]
  intro d hd
  rw [coeff_sub, sub_eq_zero]
  have h1 : (bsum μ N (fun i : Fin N => (X : ℤ[X]) ^ (i : ℕ))).coeff d
      = ((univ.filter (fun T : Cell μ → Fin N => IsBT T ∧ d = ∑ c, (T c : ℕ))).card : ℤ) := by
    unfold bsum
    rw [finset_sum_coeff]
    simp_rw [prod_pow_eq_pow_sum, coeff_X_pow]
    rw [sum_boole, filter_filter]
  have h2 : (fmaj μ * DN N μ.cells.card).coeff d
      = ((univ.filter (fun p : SYTe μ × (Fin μ.cells.card → Fin N) =>
            Antitone (fun k => (p.2 k : ℕ)) ∧ d = p.1.maj + ∑ k, (p.2 k : ℕ))).card : ℤ) := by
    unfold fmaj DN
    rw [sum_mul_sum, ← sum_product', finset_sum_coeff]
    simp_rw [← pow_add, coeff_X_pow]
    rw [sum_boole]
    congr 2
    ext p
    simp only [mem_filter, mem_product, mem_univ, true_and]
  rw [h1, h2]
  congr 1
  refine card_bij' (fun T hT => toPair hd T (mem_filter.1 hT).2)
    (fun p hp => toTab hd p (mem_filter.1 hp).2)
    (fun T hT => mem_filter.2 ⟨mem_univ _, toPair_mem hd T _⟩)
    (fun p hp => mem_filter.2 ⟨mem_univ _, toTab_isBT hd p _⟩)
    (fun T hT => toTab_toPair hd T _) (fun p hp => toPair_toTab hd p _)

/-! ## `E_N(μ) ≡ 1` -/

theorem dvd_prod_sub_one' {R : Type*} [CommRing R] (Q : R) (K : ℕ) (s : Finset ℕ) (g : ℕ → R)
    (hg : ∀ i ∈ s, Q ^ K ∣ g i - 1) : Q ^ K ∣ (∏ i ∈ s, g i) - 1 := by
  induction s using Finset.induction_on with
  | empty => simp
  | insert a s ha ih =>
    rw [prod_insert ha]
    have h1 := hg a (mem_insert_self a s)
    have h2 := ih (fun i hi => hg i (mem_insert_of_mem hi))
    have e : g a * ∏ i ∈ s, g i - 1 = g a * ((∏ i ∈ s, g i) - 1) + (g a - 1) := by ring
    rw [e]
    exact dvd_add (dvd_mul_of_dvd_right h2 _) h1

/-- **`E_N(μ) ≡ 1 mod Q^K`** once `K + ℓ(μ) ≤ N + 1`: every exponent `N − i + t` has `i < ℓ(μ)`. -/
theorem dvd_prod_sub_one {R : Type*} [CommRing R] (Q : R) (N K : ℕ) (μ : YoungDiagram)
    (hK : K + μ.colLen 0 ≤ N + 1) :
    Q ^ K ∣ (∏ i ∈ range N, ∏ t ∈ range (μ.rowLen i), (1 - Q ^ (N - i + t))) - 1 := by
  refine dvd_prod_sub_one' Q K _ _ fun i _ => dvd_prod_sub_one' Q K _ _ fun t ht => ?_
  rw [mem_range] at ht
  have hc : i < μ.colLen 0 := by
    rw [← mem_iff_lt_colLen]
    exact μ.up_left_mem (le_refl i) (Nat.zero_le t) (mem_iff_lt_rowLen.2 ht)
  rw [sub_sub_cancel_left]
  exact (dvd_neg).2 (pow_dvd_pow Q (by omega))

/-! ## The one-row diagram -/

/-- The diagram with one row of length `n`. -/
def rowYD (n : ℕ) : YoungDiagram where
  cells := {0} ×ˢ range n
  isLowerSet := by
    rintro ⟨i2, j2⟩ ⟨i1, j1⟩ ⟨hi : i1 ≤ i2, hj : j1 ≤ j2⟩ h
    simp only [coe_product, coe_singleton, coe_range, Set.mem_prod, Set.mem_singleton_iff,
      Set.mem_Iio] at h ⊢
    omega

theorem mem_rowYD {n : ℕ} {c : ℕ × ℕ} : c ∈ rowYD n ↔ c.1 = 0 ∧ c.2 < n := by
  show c ∈ ({0} ×ˢ range n : Finset (ℕ × ℕ)) ↔ _
  rw [mem_product, mem_singleton, mem_range]

theorem cells_rowYD (n : ℕ) : (rowYD n).cells = {0} ×ˢ range n := rfl

theorem card_rowYD (n : ℕ) : (rowYD n).cells.card = n := by
  rw [cells_rowYD, card_product, card_singleton, card_range, one_mul]

theorem rowLen_rowYD_zero (n : ℕ) : (rowYD n).rowLen 0 = n := by
  have h : ∀ j, j < (rowYD n).rowLen 0 ↔ j < n := fun j => by
    rw [← mem_iff_lt_rowLen, mem_rowYD]
    simp
  exact le_antisymm (not_lt.1 fun hlt => lt_irrefl n ((h n).1 hlt))
    (not_lt.1 fun hlt => lt_irrefl _ ((h _).2 hlt))

theorem rowLen_rowYD_pos (n : ℕ) {i : ℕ} (hi : 0 < i) : (rowYD n).rowLen i = 0 := by
  by_contra h
  have := mem_rowYD.1 (mem_iff_lt_rowLen.2 (Nat.pos_of_ne_zero h))
  omega

theorem colLen_rowYD (n : ℕ) {j : ℕ} (hj : j < n) : (rowYD n).colLen j = 1 := by
  have h : ∀ i, i < (rowYD n).colLen j ↔ i < 1 := fun i => by
    rw [← mem_iff_lt_colLen, mem_rowYD]
    simp only
    omega
  exact le_antisymm (not_lt.1 fun hlt => lt_irrefl 1 ((h 1).1 hlt))
    (not_lt.1 fun hlt => lt_irrefl _ ((h _).2 hlt))

theorem colLen_rowYD_le (n : ℕ) : (rowYD n).colLen 0 ≤ 1 := by
  by_contra h
  have := mem_rowYD.1 (mem_iff_lt_colLen.2 (show 1 < (rowYD n).colLen 0 by omega))
  simp at this

theorem eExp_rowYD (N n : ℕ) : eExp N (rowYD n) = 0 := by
  refine sum_eq_zero fun j _ => ?_
  rcases Nat.eq_zero_or_pos j with h | h
  · rw [h, zero_mul]
  · rw [rowLen_rowYD_pos n h, mul_zero]

theorem hook_rowYD {R : Type*} [CommRing R] (Q : R) (n : ℕ) :
    ∏ c ∈ (rowYD n).cells, (1 - Q ^ QOU.QBeta.WenzlWeight.hook (rowYD n) c)
      = ∏ m ∈ range n, (1 - Q ^ (m + 1)) := by
  rw [cells_rowYD, prod_product, prod_singleton, ← prod_range_reflect (fun m => 1 - Q ^ (m + 1)) n]
  refine prod_congr rfl fun j hj => ?_
  rw [mem_range] at hj
  rw [QOU.QBeta.WenzlWeight.hook, rowLen_rowYD_zero, colLen_rowYD n hj]
  congr 2
  omega

namespace SYTe

theorem maj_rowYD {n : ℕ} (S : SYTe (rowYD n)) : S.maj = 0 := by
  have hrow : ∀ k, S.rowN k = 0 := fun k => by
    unfold SYTe.rowN
    split
    · exact (mem_rowYD.1 (S.e.symm _).2).1
    · rfl
  unfold SYTe.maj
  rw [filter_false_of_mem fun k _ hk => by
    have := hk.2
    rw [hrow, hrow] at this
    exact lt_irrefl 0 this]
  rfl

/-- The unique standard tableau of a row: entry `j` in column `j`. -/
def rowStd (n : ℕ) : SYTe (rowYD n) where
  e := {
    toFun := fun c => ⟨c.1.2, by rw [card_rowYD]; exact (mem_rowYD.1 c.2).2⟩
    invFun := fun k => ⟨(0, k), mem_rowYD.2 ⟨rfl, by
      have := k.2; have := card_rowYD n; show (k : ℕ) < n; omega⟩⟩
    left_inv := fun c => by
      apply Subtype.ext
      ext
      · exact (mem_rowYD.1 c.2).1.symm
      · rfl
    right_inv := fun k => rfl }
  row_lt := fun c c' _ h => h
  col_lt := fun c c' _ h => by
    have := (mem_rowYD.1 c.2).1
    have := (mem_rowYD.1 c'.2).1
    omega

theorem e_rowYD {n : ℕ} (S : SYTe (rowYD n)) (c : Cell (rowYD n)) : (S.e c : ℕ) = c.1.2 := by
  set m := (rowYD n).cells.card
  have hm : m = n := card_rowYD n
  let g : Fin m → Fin m := fun k => S.e ⟨(0, k), mem_rowYD.2 ⟨rfl, by have := k.2; omega⟩⟩
  have hg : StrictMono g := fun k k' h => S.row_lt _ _ rfl h
  have hr : Set.range g = Set.range id := by
    rw [Set.range_id]
    refine Set.eq_univ_of_forall fun y => ⟨⟨(S.e.symm y).1.2, by
      have := (mem_rowYD.1 (S.e.symm y).2).2; omega⟩, ?_⟩
    have hc : (⟨(0, (S.e.symm y).1.2), mem_rowYD.2 ⟨rfl, (mem_rowYD.1 (S.e.symm y).2).2⟩⟩ :
        Cell (rowYD n)) = S.e.symm y := by
      apply Subtype.ext
      ext
      · exact (mem_rowYD.1 (S.e.symm y).2).1.symm
      · rfl
    show S.e _ = y
    rw [hc, Equiv.apply_symm_apply]
  have hgid := (hg.range_inj strictMono_id).1 hr
  have hc : c = ⟨(0, c.1.2), mem_rowYD.2 ⟨rfl, (mem_rowYD.1 c.2).2⟩⟩ := by
    apply Subtype.ext
    ext
    · exact (mem_rowYD.1 c.2).1
    · rfl
  have := congrArg Fin.val (congrFun hgid ⟨c.1.2, by have := (mem_rowYD.1 c.2).2; omega⟩)
  rw [hc]
  exact this

end SYTe

theorem fmaj_rowYD (n : ℕ) : fmaj (rowYD n) = 1 := by
  have hu : ∀ S : SYTe (rowYD n), S = SYTe.rowStd n := fun S => SYTe.ext' (Equiv.ext fun c =>
    Fin.ext ((SYTe.e_rowYD S c).trans (SYTe.e_rowYD (SYTe.rowStd n) c).symm))
  have hcard : Fintype.card (SYTe (rowYD n)) = 1 := Fintype.card_eq_one_iff.2 ⟨_, hu⟩
  unfold fmaj
  simp_rw [SYTe.maj_rowYD, pow_zero]
  rw [sum_const, card_univ, hcard, one_smul]

/-! ## The formula -/

/-- `e(μ) = ∑_{j<N} j · μ_j` is `n(μ) = ∑_{c ∈ μ} c₁` once `N` covers every row. -/
theorem eExp_eq_nPart (N : ℕ) (μ : YoungDiagram) (hμ : μ.colLen 0 ≤ N) :
    eExp N μ = QOU.QBeta.WenzlWeight.nPart μ := by
  unfold eExp QOU.QBeta.WenzlWeight.nPart
  rw [← sum_fiberwise_of_maps_to' (s := μ.cells) (t := range N) (g := Prod.fst)
    (fun x hx => ?_) (fun j => j)]
  · refine sum_congr rfl fun j _ => ?_
    rw [sum_const, smul_eq_mul, rowLen_eq_card, mul_comm]
    rfl
  · rw [mem_range]
    have : x.1 < μ.colLen 0 := by
      rw [← mem_iff_lt_colLen]
      exact μ.up_left_mem (le_refl _) (Nat.zero_le _) ((mem_cells (μ := μ) x).1 hx)
    omega

theorem one_sub_X_pow_ne_zero {k : ℕ} (hk : 0 < k) : (1 - X ^ k : ℤ[X]) ≠ 0 := by
  intro h
  have := congrArg (fun p : ℤ[X] => p.coeff k) h
  simp [coeff_one, coeff_X_pow, hk.ne'] at this

/-- **The `maj` formula** (Stanley, *EC2* Cor. 7.21.5), division-free:

`(∑_{S ∈ SYT(μ)} X^{maj S}) · ∏_{c ∈ μ} (1 − X^{h(c)}) = X^{n(μ)} · ∏_{m=1}^{|μ|} (1 − X^m)`. -/
theorem fmaj_mul_hook (μ : YoungDiagram) :
    fmaj μ * ∏ c ∈ μ.cells, (1 - X ^ QOU.QBeta.WenzlWeight.hook μ c)
      = X ^ QOU.QBeta.WenzlWeight.nPart μ * ∏ m ∈ range μ.cells.card, (1 - X ^ (m + 1)) := by
  set n := μ.cells.card
  set H : ℤ[X] := ∏ c ∈ μ.cells, (1 - X ^ QOU.QBeta.WenzlWeight.hook μ c)
  set Hr : ℤ[X] := ∏ c ∈ (rowYD n).cells, (1 - X ^ QOU.QBeta.WenzlWeight.hook (rowYD n) c)
    with hHr
  have hQk : ∀ k : ℕ, 0 < k → (1 : ℤ[X]) - X ^ k ≠ 0 := fun k hk => one_sub_X_pow_ne_zero hk
  have hall : ∀ K : ℕ, (X : ℤ[X]) ^ K ∣
      fmaj μ * H - X ^ QOU.QBeta.WenzlWeight.nPart μ * Hr := by
    intro K
    set N := K + μ.colLen 0 + 1
    have A1 := hook_mul_bsum_principal (X : ℤ[X]) X_ne_zero hQk N μ (by omega)
    rw [eExp_eq_nPart N μ (by omega)] at A1
    have hr := colLen_rowYD_le n
    have A2 := hook_mul_bsum_principal (X : ℤ[X]) X_ne_zero hQk N (rowYD n) (by omega)
    rw [eExp_rowYD, pow_zero, one_mul] at A2
    have G1 := bsum_sub_dvd μ N
    have G2 := bsum_sub_dvd (rowYD n) N
    rw [fmaj_rowYD, one_mul, card_rowYD] at G2
    have E1 := dvd_prod_sub_one (X : ℤ[X]) N K μ (by omega)
    have E2 := dvd_prod_sub_one (X : ℤ[X]) N K (rowYD n) (by omega)
    have hKN : (X : ℤ[X]) ^ K ∣ X ^ N := pow_dvd_pow X (by omega)
    set Bμ := bsum μ N (fun i : Fin N => (X : ℤ[X]) ^ (i : ℕ))
    set Br := bsum (rowYD n) N (fun i : Fin N => (X : ℤ[X]) ^ (i : ℕ))
    set D := DN N n
    set Eμ : ℤ[X] := ∏ i ∈ range N, ∏ t ∈ range (μ.rowLen i), (1 - X ^ (N - i + t))
    set Er : ℤ[X] := ∏ i ∈ range N, ∏ t ∈ range ((rowYD n).rowLen i), (1 - X ^ (N - i + t))
    have e : fmaj μ * H - X ^ QOU.QBeta.WenzlWeight.nPart μ * Hr
        = fmaj μ * H * Hr * (Br - D) - Hr * H * (Bμ - fmaj μ * D)
          + Hr * X ^ QOU.QBeta.WenzlWeight.nPart μ * (Eμ - 1) - fmaj μ * H * (Er - 1) := by
      linear_combination (-(fmaj μ * H)) * A2 + Hr * A1
    rw [e]
    exact dvd_sub (dvd_add (dvd_sub (dvd_mul_of_dvd_right (hKN.trans G2) _)
      (dvd_mul_of_dvd_right (hKN.trans G1) _)) (dvd_mul_of_dvd_right E1 _))
      (dvd_mul_of_dvd_right E2 _)
  have hz : fmaj μ * H - X ^ QOU.QBeta.WenzlWeight.nPart μ * Hr = 0 := by
    by_contra hp
    have := natDegree_le_of_dvd (hall (natDegree (fmaj μ * H - X ^ QOU.QBeta.WenzlWeight.nPart μ * Hr) + 1)) hp
    rw [natDegree_X_pow] at this
    omega
  rw [sub_eq_zero] at hz
  rw [hz, hHr, hook_rowYD]

/-! ## In `q`-integers, and the Schur element -/

open QOU.SchurWeyl.HookDivisibility in
/-- **The `maj` formula in `q`-integers**: `f_μ · ∏_c [h(c)] = X^{n(μ)} · [n]!` in `ℤ[X]`. -/
theorem fmaj_mul_qHook (μ : YoungDiagram) :
    (∏ c ∈ μ.cells, qIntPoly ℤ (QOU.QBeta.WenzlWeight.hook μ c)) * fmaj μ
      = X ^ QOU.QBeta.WenzlWeight.nPart μ * ∏ m ∈ range μ.cells.card, qIntPoly ℤ (m + 1) := by
  have hq : ∀ k : ℕ, (1 - X ^ k : ℤ[X]) = (1 - X) * qIntPoly ℤ k := fun k => by
    rw [qIntPoly, mul_neg_geom_sum]
  have h := fmaj_mul_hook μ
  simp_rw [hq, prod_mul_distrib, prod_const, card_range] at h
  have h1 : ((1 : ℤ[X]) - X) ^ μ.cells.card ≠ 0 :=
    pow_ne_zero _ (by simpa using one_sub_X_pow_ne_zero (k := 1) one_pos)
  apply mul_left_cancel₀ h1
  linear_combination h

open QOU.SchurWeyl.HookDivisibility in
/-- **`[n]_Q! / c_λ(Q)` is the `maj` generating function.**  For `Q ≠ 0, 1` in a field,
`[n]_Q! = c_λ(Q) · ∑_{S ∈ SYT(λ)} Q^{maj S}`.  So `[n]_Q!/c_λ` is a polynomial in `Q` with
nonnegative integer coefficients (`coeff_fmaj`). -/
theorem qFactorial_eq_schurElt_mul_fmaj {F : Type*} [Field F] (μ : YoungDiagram) (Q : F)
    (hQ0 : Q ≠ 0) (hQ1 : Q ≠ 1) :
    ∏ m ∈ range μ.cells.card, (1 - Q ^ (m + 1)) / (1 - Q)
      = QOU.SchurWeyl.schurElt Q μ * aeval Q (fmaj μ) := by
  have h := congrArg (aeval Q) (fmaj_mul_qHook μ)
  simp only [map_mul, map_prod, aeval_qIntPoly hQ1, map_pow, aeval_X] at h
  rw [QOU.SchurWeyl.schurElt_eq]
  have hQn : Q ^ QOU.QBeta.WenzlWeight.nPart μ ≠ 0 := pow_ne_zero _ hQ0
  field_simp
  linear_combination (-1 : F) * h

/-- The coefficients of `f_μ` count standard tableaux by `maj`; in particular they are `≥ 0`. -/
theorem coeff_fmaj (μ : YoungDiagram) (d : ℕ) :
    (fmaj μ).coeff d = ((univ.filter (fun S : SYTe μ => d = S.maj)).card : ℤ) := by
  classical
  unfold fmaj
  rw [finset_sum_coeff]
  simp_rw [coeff_X_pow]
  rw [sum_boole]

theorem coeff_fmaj_nonneg (μ : YoungDiagram) (d : ℕ) : 0 ≤ (fmaj μ).coeff d := by
  rw [coeff_fmaj]
  exact Nat.cast_nonneg _

end QOU.Mathlib.MajFormula
