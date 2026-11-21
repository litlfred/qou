import QOU.Knot.WhiteheadBraidClosure
import QOU.Mass.QuantumSl2MarkovTrace

/-!
# The Whitehead trace as a Markov invariant

`WhiteheadBraidClosure` writes van der Veen's formula as the framing-corrected trace
`θ · tr(K^{⊗3} β)` of the braid `β = σ₁⁻² σ₂ σ₁⁻¹ σ₂`, with `θ = q^{(N²−1)/2}`. Here that trace is
identified with the quantum trace `qtrace` of `QuantumSl2MarkovTrace` on the word
`whiteheadWord ∈ B₃` (`qtrace_whiteheadWord`). The writhe of `β` is `−1`, so `θ · tr(K^{⊗3} β)`
is exactly the writhe-normalised functional `θ^{−w} τ` of `jonesSl2_isMarkovInvariant`:

    vdvWhiteheadLinkJones q N = [N]⁻¹ · J(β),      J = θ^{−w(·)} τ      (`vdvWhiteheadLinkJones_eq_jones`).

`J` is unchanged by both Markov moves, so van der Veen's formula equals `[N]⁻¹ J(β')` for every
braid `β'` Markov-equivalent to `β` (`vdvWhiteheadLinkJones_eq_jones_of_markovEquiv`). It is an
invariant of the closed braid, not of the chosen word.

Issue #7912.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1
-- Ref: [turaev1988] Turaev, "The Yang–Baxter equation and invariants of links"
-/

namespace QOU.Knot.FigureEightVolume

open Matrix QOU.Mass.QuantumSl2
open QOU.Mass.QuantumSl2.BraidAction
open QOU.Mass.QuantumSl2.MarkovTrace
open QOU.Mass.QuantumSl2.Markov (rCheckInv rCheck_mul_inv theta)
open QOU.IwahoriHecke.TensorEmbed (coxA coxA_symm)
open QOU.IwahoriHecke.BraidGroup (BraidGroupN braidGen)
open QOU.IwahoriHecke.JonesNormalisation (writhe writhe_braidGen)
open QOU.Torsion.MassTraceMarkovClass (artinTower)
open QOU.MathlibExt.MarkovMoves

/-! ### Three sites as a triple product -/

section Sites

variable {𝕜 : Type*} [Field 𝕜] {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- `((a, b), c) ↦ (a, b, c)`: the triple product as functions on three sites. -/
def triEquiv (ι : Type*) : (ι × ι) × ι ≃ (Fin 3 → ι) where
  toFun x := ![x.1.1, x.1.2, x.2]
  invFun a := ((a 0, a 1), a 2)
  left_inv _ := rfl
  right_inv a := by funext k; fin_cases k <;> rfl

omit [Fintype ι] [DecidableEq ι] in
theorem forall_fin3_ne01 (f g : Fin 3 → ι) :
    (∀ k : Fin 3, k ≠ 0 → k ≠ 1 → f k = g k) ↔ f 2 = g 2 :=
  ⟨fun h => h 2 (by decide) (by decide), fun h k h0 h1 => by fin_cases k <;> simp_all⟩

omit [Fintype ι] [DecidableEq ι] in
theorem forall_fin3_ne12 (f g : Fin 3 → ι) :
    (∀ k : Fin 3, k ≠ 1 → k ≠ 2 → f k = g k) ↔ f 0 = g 0 :=
  ⟨fun h => h 0 (by decide) (by decide), fun h k h1 h2 => by fin_cases k <;> simp_all⟩

/-- `σ₁`: the strand operator on strands `0, 1` is the leg `A ⊗ 1`. -/
theorem strandMat_zero_submatrix (M : Matrix (ι × ι) (ι × ι) 𝕜) :
    (strandMat (m := 2) M 0).submatrix (triEquiv ι) (triEquiv ι) = leg12 M := by
  ext x y
  rw [submatrix_apply, leg12_apply, strandMat, pembed_apply]
  have h1 : (0 : Fin 2).castSucc = 0 := rfl
  have h2 : (0 : Fin 2).succ = 1 := rfl
  simp only [h1, h2]
  by_cases h : x.2 = y.2
  · rw [if_pos ((forall_fin3_ne01 _ _).2 (by simpa [triEquiv] using h))]
    simp [triEquiv, one_apply, h]
  · rw [if_neg fun h' => h (by simpa [triEquiv] using (forall_fin3_ne01 _ _).1 h')]
    simp [h]

/-- `σ₂`: the strand operator on strands `1, 2` is the leg `1 ⊗ A`. -/
theorem strandMat_one_submatrix (M : Matrix (ι × ι) (ι × ι) 𝕜) :
    (strandMat (m := 2) M 1).submatrix (triEquiv ι) (triEquiv ι) = leg23 M := by
  ext x y
  rw [submatrix_apply, leg23_apply, strandMat, pembed_apply]
  have h1 : (1 : Fin 2).castSucc = 1 := rfl
  have h2 : (1 : Fin 2).succ = 2 := rfl
  simp only [h1, h2]
  by_cases h : x.1.1 = y.1.1
  · rw [if_pos ((forall_fin3_ne12 _ _).2 (by simpa [triEquiv] using h))]
    simp [triEquiv, one_apply, h]
  · rw [if_neg fun h' => h (by simpa [triEquiv] using (forall_fin3_ne12 _ _).1 h')]
    simp [h]

omit [DecidableEq ι] in
theorem submatrix_tri_mul (A B : Matrix (Fin 3 → ι) (Fin 3 → ι) 𝕜) :
    (A * B).submatrix (triEquiv ι) (triEquiv ι)
      = A.submatrix (triEquiv ι) (triEquiv ι) * B.submatrix (triEquiv ι) (triEquiv ι) :=
  (submatrix_mul_equiv A B _ (triEquiv ι) _).symm

end Sites

/-! ### The Whitehead word in `B₃` -/

/-- The Whitehead braid `σ₁⁻² σ₂ σ₁⁻¹ σ₂` as a word in the Artin group `B₃`. -/
def whiteheadWord : BraidGroupN 2 :=
  (braidGen (coxA 2) 0)⁻¹ * (braidGen (coxA 2) 0)⁻¹ * braidGen (coxA 2) 1
    * (braidGen (coxA 2) 0)⁻¹ * braidGen (coxA 2) 1

/-- The writhe of the Whitehead braid is `−1`. -/
theorem writhe_whiteheadWord :
    artinFraming.w 2 whiteheadWord = Multiplicative.ofAdd (-1 : ℤ) := by
  show writhe (coxA 2) coxA_symm _ = _
  simp [whiteheadWord]

section Closure

variable (σ : ℂ) (hσ : σ ≠ 0) (m : ℕ) (hq2 : σ ^ 2 - (σ ^ 2)⁻¹ ≠ 0)
  (hint : ∀ i, 0 < i → i ≤ 2 * m + 1 → qint (σ ^ 2) i ≠ 0)

theorem hint_le (hint : ∀ i, 0 < i → i ≤ 2 * m + 1 → qint (σ ^ 2) i ≠ 0) :
    ∀ i, 0 < i → i ≤ 2 * m → qint (σ ^ 2) i ≠ 0 :=
  fun i h1 h2 => hint i h1 (by omega)

theorem qWt_eq (r : Fin (m + 1)) : qWt σ m r = (σ ^ 2) ^ wt m r := by
  rw [qWt, zpow_mul]; norm_cast

include hq2 hint in
/-- The action of the Whitehead word is the Whitehead braid of `WhiteheadBraidClosure`. -/
theorem rCheckRep_whiteheadWord :
    ((rCheckRep σ hσ m hq2 (hint_le σ m hint) 2 whiteheadWord :
        (Matrix (Fin 3 → Fin (m + 1)) (Fin 3 → Fin (m + 1)) ℂ)ˣ) :
          Matrix (Fin 3 → Fin (m + 1)) (Fin 3 → Fin (m + 1)) ℂ).submatrix
        (triEquiv _) (triEquiv _)
      = whiteheadBraid σ hσ m := by
  have hinv : (rCheckMat σ hσ m m)⁻¹ = rCheckInv σ hσ m :=
    Matrix.inv_eq_right_inv (rCheck_mul_inv σ hσ m)
  simp only [whiteheadWord, map_mul, Units.val_mul]
  rw [rCheckRep_braidGen_inv, rCheckRep_braidGen, submatrix_tri_mul, submatrix_tri_mul,
    submatrix_tri_mul, submatrix_tri_mul, strandMat_zero_submatrix, strandMat_one_submatrix,
    whiteheadBraid, hinv]

include hq2 hint in
/-- **The quantum trace of the Whitehead word** is the braid-closure trace `tr(K^{⊗3} β)`. -/
theorem qtrace_whiteheadWord :
    qtrace σ hσ m hq2 (hint_le σ m hint) ⟨2, whiteheadWord⟩
      = trace (kTri (σ ^ 2) m * whiteheadBraid σ hσ m) := by
  rw [← rCheckRep_whiteheadWord σ hσ m hq2 hint]
  simp only [qtrace, wtrace, trace, diag, kTri, diagonal_mul, submatrix_apply]
  refine (Fintype.sum_equiv (triEquiv _) _ _ fun x => ?_).symm
  simp [siteWt, Fin.prod_univ_three, triEquiv, qWt_eq]

include hq2 hint in
/-- **van der Veen's formula is the coloured Jones functional of the Whitehead braid.**
With `J = θ^{−w(·)} τ` the writhe-normalised quantum trace of `jonesSl2_isMarkovInvariant`,
`vdvWhiteheadLinkJones q N = [N]⁻¹ · J(σ₁⁻² σ₂ σ₁⁻¹ σ₂)`, `N = m + 1`, `q = σ²`. -/
theorem vdvWhiteheadLinkJones_eq_jones :
    vdvWhiteheadLinkJones (σ ^ 2) (m + 1)
      = (qint (σ ^ 2) (m + 1))⁻¹ * normalise artinFraming (thetaU σ hσ m)⁻¹ 1
          (qtrace σ hσ m hq2 (hint_le σ m hint)) ⟨2, whiteheadWord⟩ := by
  rw [normalise_apply, writhe_whiteheadWord, toAdd_ofAdd, zpow_neg_one, inv_inv, one_pow,
    mul_one, qtrace_whiteheadWord σ hσ m hq2 hint, vdvWhiteheadLinkJones_eq_braidTrace σ hσ m hq2 hint]
  have hθ : ((thetaU σ hσ m : ℂˣ) : ℂ) = σ ^ (m * (m + 2)) := by
    rw [thetaU, Units.val_mk0, theta]
    have hk : ((m : ℤ) * (m + 2)) = ((m * (m + 2) : ℕ) : ℤ) := by push_cast; ring
    rw [hk, zpow_natCast]
  rw [hθ]; ring

include hq2 hint in
/-- **The Whitehead formula is an invariant of the closed braid.** For every braid `p`
Markov-equivalent to `σ₁⁻² σ₂ σ₁⁻¹ σ₂`, `vdvWhiteheadLinkJones q N = [N]⁻¹ · J(p)`. -/
theorem vdvWhiteheadLinkJones_eq_jones_of_markovEquiv {p : Tot BraidGroupN}
    (h : MarkovEquiv artinTower ⟨2, whiteheadWord⟩ p) :
    vdvWhiteheadLinkJones (σ ^ 2) (m + 1)
      = (qint (σ ^ 2) (m + 1))⁻¹ * normalise artinFraming (thetaU σ hσ m)⁻¹ 1
          (qtrace σ hσ m hq2 (hint_le σ m hint)) p := by
  rw [vdvWhiteheadLinkJones_eq_jones σ hσ m hq2 hint,
    (jonesSl2_isMarkovInvariant σ hσ m hq2 (hint_le σ m hint)).descends h]

end Closure

end QOU.Knot.FigureEightVolume
