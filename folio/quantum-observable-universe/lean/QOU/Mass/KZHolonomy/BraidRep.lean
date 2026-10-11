import QOU.Mass.KZHolonomy.KZForm
import QOU.Mass.KZHolonomy.BraidGeometry
import QOU.MathlibExt.BraidGroup

/-!
# The KZ holonomy representation of the braid group

Fix a complete normed `ℂ`-algebra `A`, a representation `ρ : S_{m+1} →* A` of the symmetric
group, and complex numbers `κ, c`.  The KZ form

    ω(z)(u) = κ Σ_{a,b} (u_a − u_b)/(z_a − z_b) · (ρ(s_ab) − c)

is flat on configuration space (`kzForm_isFlatOn`), hence on the star-shaped region
`D = kzRegion (m+1)`.  Write `Φ(z)` for the transport of `ω` along the segment from the
centre of `D` to `z`, and for a permutation `σ` put

    Ψ(σ) = ρ(σ) Φ(p_σ),     p_σ = (σ 0, …, σ m) ∈ ℝ^{m+1}.

Let `T_j` be the transport of `ω` along the half-turn `γ_j` exchanging the points at
positions `j, j+1`, and `g_j = ρ(s_j) T_j`.

**Key identity** (`gen_mul_psi`).  If `σ⁻¹ j < σ⁻¹ (j+1)` then `g_j Ψ(σ) = Ψ(s_j σ)`.
The permuted half-turn `γ_j ∘ σ` runs inside `D` from `p_σ` to `p_{s_j σ}`, its transport is
`ρ(σ)⁻¹ T_j ρ(σ)` by equivariance of `ω`, and transport inside the star-shaped flat region
depends only on endpoints (`flat_transport_eq`).

**Braid relations.**  Applying both sides of `σ_j σ_{j+1} σ_j = σ_{j+1} σ_j σ_{j+1}`
(resp. `σ_i σ_j = σ_j σ_i`, `|i − j| ≥ 2`) to `Ψ(1)` and using the key identity three
(resp. two) times, each order condition being checked on the strands, both sides send `Ψ(1)`
to `Ψ` of the same permutation.  Since `Ψ(1) = Φ(p_1)` is a unit, the relations hold in `A`.
This yields

    kzBraidRep ρ κ c : BraidGroup m →* Aˣ,     σ_j ↦ ρ(s_j) T_j,

and at `κ = 0` the transport is trivial, so `σ_j ↦ ρ(s_j)` (`kzBraidRep_zero_σ`).
-/

open Set

namespace QOU.Mass.KZHolonomy

open QOU.MathlibExt.Braid

variable {m : ℕ} {A : Type*} [NormedRing A] [NormedAlgebra ℂ A] [CompleteSpace A]

lemma IsFlatOn.mono {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    {ω : E → E →L[ℝ] A} {ω' : E → E →L[ℝ] E →L[ℝ] A} {D D' : Set E}
    (h : IsFlatOn ω ω' D) (hD : D' ⊆ D) : IsFlatOn ω ω' D' :=
  ⟨fun y hy => h.hasFDerivAt y (hD hy), h.continuousOn.mono hD, fun y hy => h.flat y (hD hy)⟩

/-- The adjacent transposition `s_j = (j  j+1)` on `m + 1` strands. -/
def adjSwap (j : Fin m) : Equiv.Perm (Fin (m + 1)) := Equiv.swap j.castSucc j.succ

variable (ρ : Equiv.Perm (Fin (m + 1)) →* A) (κ c : ℂ)

lemma kz_isFlatOn_region :
    IsFlatOn (kzForm ρ κ c) (kzForm' ρ κ c) (kzRegion (m + 1)) :=
  (kzForm_isFlatOn ρ κ c).mono (kzRegion_subset_injective _)

lemma genPath_mem (j : Fin m) {t : ℝ} (ht : t ∈ Icc (0:ℝ) 1) :
    genPath j t ∈ kzRegion (m + 1) := by
  simpa using genPath_comp_mem j 1 (by simpa using Fin.castSucc_lt_succ j) ht

lemma continuousOn_genCoeff (j : Fin m) :
    ContinuousOn (fun t => kzForm ρ κ c (genPath j t) (genPath' j t)) (Icc 0 1) :=
  continuousOn_transportCoeff
    (fun t ht => ((kz_isFlatOn_region ρ κ c).hasFDerivAt _ (genPath_mem j ht)).continuousAt)
    (fun t _ => (hasDerivAt_genPath j t).continuousAt.continuousWithinAt)
    (continuous_genPath' j).continuousOn

/-- The transport of the KZ connection along the half-turn `γ_j`, as a function of time. -/
noncomputable def genFund (j : Fin m) : ℝ → A :=
  Classical.choose (exists_isFundSol (continuousOn_genCoeff ρ κ c j))

lemma genFund_spec (j : Fin m) :
    IsTransport (kzForm ρ κ c) (genPath j) (genPath' j) (genFund ρ κ c j) :=
  Classical.choose_spec (exists_isFundSol (continuousOn_genCoeff ρ κ c j))

/-- The image `g_j = ρ(s_j) T_j` of the `j`-th Artin generator. -/
noncomputable def genImage (j : Fin m) : A := ρ (adjSwap j) * genFund ρ κ c j 1

/-- `Ψ(σ) = ρ(σ) Φ(p_σ)`. -/
noncomputable def psi (σ : Equiv.Perm (Fin (m + 1))) : A :=
  ρ σ * radialTransport (kzForm ρ κ c) (kzCenter (m + 1)) (basePt σ)

lemma rho_mul_inv (σ : Equiv.Perm (Fin (m + 1))) : ρ σ * ρ σ⁻¹ = 1 := by
  rw [← map_mul, mul_inv_cancel, map_one]

/-- **Key identity.** If `σ⁻¹ j < σ⁻¹ (j+1)` then `g_j Ψ(σ) = Ψ(s_j σ)`. -/
theorem gen_mul_psi (j : Fin m) (σ : Equiv.Perm (Fin (m + 1)))
    (hσ : σ⁻¹ j.castSucc < σ⁻¹ j.succ) :
    genImage ρ κ c j * psi ρ κ c σ = psi ρ κ c (adjSwap j * σ) := by
  have hV := (genFund_spec ρ κ c j).comp_perm σ
  have key := flat_transport_eq (isOpen_kzRegion (m + 1)) (starConvex_kzRegion (m + 1))
    (kz_isFlatOn_region ρ κ c) (fun t ht => genPath_comp_mem j σ hσ ht)
    (fun t _ => (hasDerivAt_genPath_comp j σ t).hasDerivWithinAt)
    (continuous_genPath'_comp j σ).continuousOn hV
  simp only [genPath_zero, genPath_one, basePt_comp, one_mul] at key
  unfold genImage psi
  rw [map_mul, ← key, adjSwap]
  calc ρ (Equiv.swap j.castSucc j.succ) * genFund ρ κ c j 1 *
        (ρ σ * radialTransport (kzForm ρ κ c) (kzCenter (m + 1)) (basePt σ))
      = ρ (Equiv.swap j.castSucc j.succ) * (ρ σ * ρ σ⁻¹) * genFund ρ κ c j 1 * ρ σ *
          radialTransport (kzForm ρ κ c) (kzCenter (m + 1)) (basePt σ) := by
        rw [rho_mul_inv, mul_one]; simp only [mul_assoc]
    _ = _ := by simp only [mul_assoc]

lemma isUnit_rho_adjSwap (j : Fin m) : IsUnit (ρ (adjSwap j)) :=
  isUnit_of_mul_eq_one _ _ (by rw [← map_mul, adjSwap, Equiv.swap_mul_self, map_one])

lemma isUnit_genImage (j : Fin m) : IsUnit (genImage ρ κ c j) :=
  (isUnit_rho_adjSwap ρ j).mul
    (IsFundSol.isUnit (continuousOn_genCoeff ρ κ c j) (genFund_spec ρ κ c j) 1
      ⟨zero_le_one, le_rfl⟩)

lemma isUnit_psi_one : IsUnit (psi ρ κ c 1) := by
  unfold psi
  rw [map_one, one_mul]
  exact isUnit_radialTransport (starConvex_kzRegion (m + 1)) (kz_isFlatOn_region ρ κ c)
    (basePt_mem 1)

/-! ### Order conditions on strands -/

/-- Evaluation of an adjacent transposition on values. -/
lemma adjSwap_val (j : Fin m) (x : Fin (m + 1)) :
    ((adjSwap j x : Fin (m + 1)) : ℕ) =
      if (x : ℕ) = j then (j : ℕ) + 1 else if (x : ℕ) = (j : ℕ) + 1 then j else x := by
  unfold adjSwap
  rw [Equiv.swap_apply_def]
  split_ifs with h1 h2 h3 h4 h3 h4 <;> simp_all [Fin.ext_iff]

lemma adjSwap_inv (j : Fin m) : (adjSwap j)⁻¹ = adjSwap j := Equiv.swap_inv _ _

lemma adjSwap_conj (i : Fin m) (a b : Fin (m + 1)) :
    adjSwap i * Equiv.swap a b * adjSwap i = Equiv.swap (adjSwap i a) (adjSwap i b) := by
  rw [Equiv.swap_apply_apply, adjSwap_inv]

lemma adjSwap_braid (i k : Fin m) (hk : (k : ℕ) = i + 1) :
    adjSwap i * adjSwap k * adjSwap i = adjSwap k * adjSwap i * adjSwap k := by
  have hci : ((i.castSucc : Fin (m + 1)) : ℕ) = i := rfl
  have hsi : ((i.succ : Fin (m + 1)) : ℕ) = i + 1 := rfl
  have hck : ((k.castSucc : Fin (m + 1)) : ℕ) = k := rfl
  have hsk : ((k.succ : Fin (m + 1)) : ℕ) = k + 1 := rfl
  have e1 : adjSwap i k.castSucc = i.castSucc := by
    rw [Fin.ext_iff, adjSwap_val]; simp only [hck, hci]; split_ifs <;> omega
  have e2 : adjSwap i k.succ = k.succ := by
    rw [Fin.ext_iff, adjSwap_val]; simp only [hsk]; split_ifs <;> omega
  have e3 : adjSwap k i.castSucc = i.castSucc := by
    rw [Fin.ext_iff, adjSwap_val]; simp only [hci]; split_ifs <;> omega
  have e4 : adjSwap k i.succ = k.succ := by
    rw [Fin.ext_iff, adjSwap_val]; simp only [hsi, hsk]; split_ifs <;> omega
  conv_lhs => rw [show adjSwap k = Equiv.swap k.castSucc k.succ from rfl, adjSwap_conj, e1, e2]
  conv_rhs => rw [show adjSwap i = Equiv.swap i.castSucc i.succ from rfl, adjSwap_conj, e3, e4]

lemma adjSwap_comm (i j : Fin m) (h : (i : ℕ) + 2 ≤ j) :
    adjSwap i * adjSwap j = adjSwap j * adjSwap i := by
  have hci : ((i.castSucc : Fin (m + 1)) : ℕ) = i := rfl
  have hsi : ((i.succ : Fin (m + 1)) : ℕ) = i + 1 := rfl
  have hcj : ((j.castSucc : Fin (m + 1)) : ℕ) = j := rfl
  have hsj : ((j.succ : Fin (m + 1)) : ℕ) = j + 1 := rfl
  have e1 : adjSwap i j.castSucc = j.castSucc := by
    rw [Fin.ext_iff, adjSwap_val]; simp only [hcj]; split_ifs <;> omega
  have e2 : adjSwap i j.succ = j.succ := by
    rw [Fin.ext_iff, adjSwap_val]; simp only [hsj]; split_ifs <;> omega
  have key : adjSwap i * adjSwap j * adjSwap i = adjSwap j := by
    conv_lhs => rw [show adjSwap j = Equiv.swap j.castSucc j.succ from rfl, adjSwap_conj, e1, e2]
    rfl
  calc adjSwap i * adjSwap j = adjSwap i * adjSwap j * adjSwap i * adjSwap i := by
        rw [mul_assoc _ (adjSwap i), show adjSwap i * adjSwap i = 1 from Equiv.swap_mul_self _ _,
          mul_one]
    _ = adjSwap j * adjSwap i := by rw [key]

/-- Order test for `gen_mul_psi`, phrased on values. -/
lemma order_of_val (j : Fin m) (σ : Equiv.Perm (Fin (m + 1)))
    (h : ((σ⁻¹ j.castSucc : Fin (m + 1)) : ℕ) < ((σ⁻¹ j.succ : Fin (m + 1)) : ℕ)) :
    σ⁻¹ j.castSucc < σ⁻¹ j.succ := h

/-! ### The representation -/

lemma psi_cancel {x y : A} (h : x * psi ρ κ c 1 = y * psi ρ κ c 1) : x = y :=
  (isUnit_psi_one ρ κ c).mul_right_cancel h

lemma gen_braid (i k : Fin m) (hk : (k : ℕ) = i + 1) :
    genImage ρ κ c i * genImage ρ κ c k * genImage ρ κ c i =
      genImage ρ κ c k * genImage ρ κ c i * genImage ρ κ c k := by
  refine psi_cancel ρ κ c ?_
  have hci : ((i.castSucc : Fin (m + 1)) : ℕ) = i := rfl
  have hsi : ((i.succ : Fin (m + 1)) : ℕ) = i + 1 := rfl
  have hck : ((k.castSucc : Fin (m + 1)) : ℕ) = k := rfl
  have hsk : ((k.succ : Fin (m + 1)) : ℕ) = k + 1 := rfl
  have L1 := gen_mul_psi ρ κ c i 1 (by simpa using Fin.castSucc_lt_succ i)
  have L2 := gen_mul_psi ρ κ c k (adjSwap i * 1) (by
    apply order_of_val
    simp only [mul_one, adjSwap_inv, adjSwap_val, hci, hsi, hck, hsk]
    split_ifs <;> omega)
  have L3 := gen_mul_psi ρ κ c i (adjSwap k * (adjSwap i * 1)) (by
    apply order_of_val
    simp only [mul_one, mul_inv_rev, adjSwap_inv, Equiv.Perm.coe_mul, Function.comp_apply,
      adjSwap_val, hci, hsi, hck, hsk]
    split_ifs <;> omega)
  have R1 := gen_mul_psi ρ κ c k 1 (by simpa using Fin.castSucc_lt_succ k)
  have R2 := gen_mul_psi ρ κ c i (adjSwap k * 1) (by
    apply order_of_val
    simp only [mul_one, adjSwap_inv, adjSwap_val, hci, hsi, hck, hsk]
    split_ifs <;> omega)
  have R3 := gen_mul_psi ρ κ c k (adjSwap i * (adjSwap k * 1)) (by
    apply order_of_val
    simp only [mul_one, mul_inv_rev, adjSwap_inv, Equiv.Perm.coe_mul, Function.comp_apply,
      adjSwap_val, hci, hsi, hck, hsk]
    split_ifs <;> omega)
  calc genImage ρ κ c i * genImage ρ κ c k * genImage ρ κ c i * psi ρ κ c 1
      = genImage ρ κ c i * (genImage ρ κ c k * (genImage ρ κ c i * psi ρ κ c 1)) := by
        simp only [mul_assoc]
    _ = psi ρ κ c (adjSwap i * (adjSwap k * (adjSwap i * 1))) := by rw [L1, L2, L3]
    _ = psi ρ κ c (adjSwap k * (adjSwap i * (adjSwap k * 1))) := by
        simp only [mul_one, ← mul_assoc, adjSwap_braid i k hk]
    _ = genImage ρ κ c k * (genImage ρ κ c i * (genImage ρ κ c k * psi ρ κ c 1)) := by
        rw [R1, R2, R3]
    _ = _ := by simp only [mul_assoc]

lemma gen_comm (i j : Fin m) (h : (i : ℕ) + 2 ≤ j) :
    genImage ρ κ c i * genImage ρ κ c j = genImage ρ κ c j * genImage ρ κ c i := by
  refine psi_cancel ρ κ c ?_
  have hci : ((i.castSucc : Fin (m + 1)) : ℕ) = i := rfl
  have hsi : ((i.succ : Fin (m + 1)) : ℕ) = i + 1 := rfl
  have hcj : ((j.castSucc : Fin (m + 1)) : ℕ) = j := rfl
  have hsj : ((j.succ : Fin (m + 1)) : ℕ) = j + 1 := rfl
  have L1 := gen_mul_psi ρ κ c j 1 (by simpa using Fin.castSucc_lt_succ j)
  have L2 := gen_mul_psi ρ κ c i (adjSwap j * 1) (by
    apply order_of_val
    simp only [mul_one, adjSwap_inv, adjSwap_val, hci, hsi, hcj, hsj]
    split_ifs <;> omega)
  have R1 := gen_mul_psi ρ κ c i 1 (by simpa using Fin.castSucc_lt_succ i)
  have R2 := gen_mul_psi ρ κ c j (adjSwap i * 1) (by
    apply order_of_val
    simp only [mul_one, adjSwap_inv, adjSwap_val, hci, hsi, hcj, hsj]
    split_ifs <;> omega)
  calc genImage ρ κ c i * genImage ρ κ c j * psi ρ κ c 1
      = genImage ρ κ c i * (genImage ρ κ c j * psi ρ κ c 1) := mul_assoc _ _ _
    _ = psi ρ κ c (adjSwap i * (adjSwap j * 1)) := by rw [L1, L2]
    _ = psi ρ κ c (adjSwap j * (adjSwap i * 1)) := by
        simp only [mul_one, adjSwap_comm i j h]
    _ = genImage ρ κ c j * (genImage ρ κ c i * psi ρ κ c 1) := by rw [R1, R2]
    _ = _ := (mul_assoc _ _ _).symm

/-- The generator images as units. -/
noncomputable def genUnit (j : Fin m) : Aˣ := (isUnit_genImage ρ κ c j).unit

lemma genUnit_val (j : Fin m) : (genUnit ρ κ c j : A) = genImage ρ κ c j := rfl

lemma lift_genUnit_relators :
    ∀ r ∈ braidRelators m, FreeGroup.lift (genUnit ρ κ c) r = 1 := by
  rintro r (⟨i, j, hij, rfl⟩ | ⟨i, h, rfl⟩)
  · have hc : genUnit ρ κ c i * genUnit ρ κ c j = genUnit ρ κ c j * genUnit ρ κ c i :=
      Units.ext (by simpa [genUnit_val] using gen_comm ρ κ c i j hij)
    simp only [map_mul, map_inv, FreeGroup.lift_apply_of]
    rw [hc]; group
  · set k : Fin m := ⟨(i : ℕ) + 1, h⟩
    have hb : genUnit ρ κ c i * genUnit ρ κ c k * genUnit ρ κ c i =
        genUnit ρ κ c k * genUnit ρ κ c i * genUnit ρ κ c k :=
      Units.ext (by simpa [genUnit_val] using gen_braid ρ κ c i k rfl)
    simp only [map_mul, map_inv, FreeGroup.lift_apply_of]
    rw [hb, mul_inv_cancel]

/-- **The KZ holonomy representation** `θ : B_{m+1} → Aˣ`, `σ_j ↦ ρ(s_j) T_j`. -/
noncomputable def kzBraidRep : BraidGroup m →* Aˣ :=
  PresentedGroup.toGroup (lift_genUnit_relators ρ κ c)

@[simp] theorem kzBraidRep_σ (j : Fin m) :
    (kzBraidRep ρ κ c (σ j) : A) = ρ (adjSwap j) * genFund ρ κ c j 1 := by
  unfold kzBraidRep σ
  rw [PresentedGroup.toGroup.of]
  rfl

/-- At `κ = 0` the connection vanishes, so the holonomy representation is the
symmetric-group representation `ρ` pulled back along `σ_j ↦ s_j`. -/
theorem kzBraidRep_zero_σ (j : Fin m) :
    (kzBraidRep ρ 0 c (σ j) : A) = ρ (adjSwap j) := by
  rw [kzBraidRep_σ]
  have hU := genFund_spec ρ 0 c j
  have hX : ContinuousOn (fun t => kzForm ρ 0 c (genPath j t) (genPath' j t)) (Icc 0 1) :=
    continuousOn_genCoeff ρ 0 c j
  have h1 := linear_eqOn_of_hasDerivWithinAt hX hU.2
    (W' := fun _ => (1 : A)) (fun t _ => by
      simpa [kzForm_zero] using (hasDerivWithinAt_const t (Icc (0:ℝ) 1) (1 : A)))
    hU.1 ⟨zero_le_one, le_rfl⟩
  rw [h1, mul_one]

end QOU.Mass.KZHolonomy
