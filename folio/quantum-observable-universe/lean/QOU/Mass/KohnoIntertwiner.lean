import QOU.Mass.KohnoWeighted

/-!
# One weight-preserving intertwiner between the KZ and Jimbo representations

`QOU.Mass.KohnoWeighted.trace_res_kz_eq_jimbo` conjugates the KZ and Jimbo representations of
`H_{m+1}(q)` separately on each total-weight space `V_k ⊆ V^{⊗(m+1)}`, but never assembles the
conjugators. This file does:

* **Block assembly** (`asm`): a family of matrices `B k` on the weight spaces `V_k` assembles to a
  block-diagonal matrix on `V^{⊗N}`; it is weight-preserving (`WP_asm`), restricts back to `B k`
  (`res_asm`), and assembly is multiplicative and unital (`asm_mul`, `asm_one`). Two
  weight-preserving matrices are equal as soon as all their restrictions are (`eq_of_res_eq`).
* **The intertwiner** (`kz_jimbo_intertwiner`): for every complex coupling `κ` with
  `q = e^{2πiκ}` not a root of unity there is ONE invertible `U`, preserving every weight space
  (`WP U`, equivalently commuting with every weight projector `wproj N k`), with
  `U · KZ(h) = Jimbo(h) · U` for every `h ∈ H_{m+1}(q)`.
* **Weighted traces by conjugation** (`weighted_trace_kz_eq_jimbo_of_intertwiner`): any operator
  `D = diag(f(cnt a))` commutes with such a `U`, so `Tr(D · Jimbo(h)) = Tr(D · KZ(h))` follows
  from the conjugation alone.
-/

namespace QOU.Mass.KohnoIntertwiner

open QOU.Mass.KohnoWeighted QOU.Mass.KohnoAssembly QOU.IwahoriHecke.TensorEmbed
open QOU.IwahoriHecke.RMatrix QOU.SchurWeyl QOU.Mass.KZHolonomy QOU.Mass.BraidHeckeFactor
open QOU.MathlibExt.Braid Matrix

section Assemble

variable {N : ℕ}

/-- Two weight-preserving matrices with the same restriction to every weight space are equal. -/
theorem eq_of_res_eq {X Y : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ} (hX : WP X) (hY : WP Y)
    (h : ∀ k, res k X = res k Y) : X = Y := by
  ext a b
  by_cases hab : cnt a = cnt b
  · have e := congrFun (congrFun (h (cnt a)) ⟨a, rfl⟩) ⟨b, hab.symm⟩
    simpa [res] using e
  · rw [hX a b hab, hY a b hab]

/-- The block-diagonal matrix with block `B k` on the weight space `V_k`. -/
def asm (B : ∀ k, Matrix (Wt N k) (Wt N k) ℂ) : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ :=
  fun a b => if h : cnt b = cnt a then B (cnt a) ⟨a, rfl⟩ ⟨b, h⟩ else 0

theorem WP_asm (B : ∀ k, Matrix (Wt N k) (Wt N k) ℂ) : WP (asm B) := by
  intro a b hab
  simp only [asm, dif_neg (Ne.symm hab)]

theorem res_asm (B : ∀ k, Matrix (Wt N k) (Wt N k) ℂ) (k : ℕ) : res k (asm B) = B k := by
  ext ⟨a, ha⟩ ⟨b, hb⟩
  subst ha
  simp only [res, Matrix.submatrix_apply, asm, dif_pos hb]

theorem asm_mul (B C : ∀ k, Matrix (Wt N k) (Wt N k) ℂ) :
    asm (fun k => B k * C k) = asm B * asm C :=
  eq_of_res_eq (WP_asm _) ((wpSub N).mul_mem (WP_asm B) (WP_asm C)) fun k => by
    rw [res_mul k (WP_asm B), res_asm, res_asm, res_asm]

theorem asm_one : asm (fun k => (1 : Matrix (Wt N k) (Wt N k) ℂ)) = 1 :=
  eq_of_res_eq (WP_asm _) (wpSub N).one_mem fun k => by
    rw [res_asm]
    ext a b
    simp [res, Matrix.one_apply, Subtype.ext_iff]

/-- Units on the weight spaces assemble to a unit on `V^{⊗N}`. -/
def asmUnit (U : ∀ k, (Matrix (Wt N k) (Wt N k) ℂ)ˣ) : (Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ)ˣ where
  val := asm fun k => (U k : Matrix (Wt N k) (Wt N k) ℂ)
  inv := asm fun k => ((U k)⁻¹ : (Matrix (Wt N k) (Wt N k) ℂ)ˣ)
  val_inv := by rw [← asm_mul]; simp_rw [Units.mul_inv]; exact asm_one
  inv_val := by rw [← asm_mul]; simp_rw [Units.inv_mul]; exact asm_one

theorem WP_asmUnit (U : ∀ k, (Matrix (Wt N k) (Wt N k) ℂ)ˣ) :
    WP ((asmUnit U : (Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ)ˣ) :
      Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) :=
  WP_asm (fun k => (U k : Matrix (Wt N k) (Wt N k) ℂ))

theorem asmUnit_val (U : ∀ k, (Matrix (Wt N k) (Wt N k) ℂ)ˣ) :
    ((asmUnit U : (Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ)ˣ) :
      Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) = asm fun k => (U k : Matrix (Wt N k) (Wt N k) ℂ) :=
  rfl

/-- Blockwise intertwiners assemble to an intertwiner of weight-preserving matrices. -/
theorem asm_intertwines {X Y : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ} (hX : WP X) (hY : WP Y)
    (U : ∀ k, (Matrix (Wt N k) (Wt N k) ℂ)ˣ)
    (h : ∀ k, (U k : Matrix (Wt N k) (Wt N k) ℂ) * res k X = res k Y * U k) :
    ((asmUnit U : (Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ)ˣ) :
      Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) * X =
      Y * ((asmUnit U : (Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ)ˣ) :
        Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) := by
  rw [asmUnit_val]
  exact eq_of_res_eq ((wpSub N).mul_mem (WP_asm _) hX) ((wpSub N).mul_mem hY (WP_asm _))
    fun k => by rw [res_mul k (WP_asm _), res_mul k hY, res_asm, h k]

/-- A weight-diagonal operator `diag(f(cnt a))` is weight-preserving. -/
theorem WP_diag_cnt (f : ℕ → ℂ) : WP (Matrix.diagonal fun a : Fin N → Fin 2 => f (cnt a)) := by
  intro a b hab
  exact Matrix.diagonal_apply_ne _ fun h => hab (h ▸ rfl)

/-- A weight-preserving matrix commutes with every weight-diagonal operator. -/
theorem commute_diag_cnt_of_WP {X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ} (hX : WP X)
    (f : ℕ → ℂ) : Commute (Matrix.diagonal fun a : Fin N → Fin 2 => f (cnt a)) X := by
  show Matrix.diagonal _ * X = X * Matrix.diagonal _
  ext a b
  rw [Matrix.diagonal_mul, Matrix.mul_diagonal]
  by_cases hab : cnt a = cnt b
  · rw [hab]; ring
  · rw [hX a b hab]; ring

/-- Weight-preservation is equivalent to commuting with every weight projector. -/
theorem WP_iff_commute_wproj (X : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ) :
    WP X ↔ ∀ k, Commute (wproj N k) X :=
  ⟨fun h k => commute_wproj_of_WP h k, WP_of_commute_wproj⟩

end Assemble

section Main

attribute [local instance] Matrix.linftyOpNormedRing Matrix.linftyOpNormedAlgebra

variable {m : ℕ}

/-- **One weight-preserving intertwiner.** For every complex coupling `κ` with `q = e^{2πiκ}`
not a root of unity there is a single invertible `U` on `V^{⊗(m+1)}` that preserves every total
weight space and satisfies `U · KZ(h) = Jimbo(h) · U` for all `h ∈ H_{m+1}(q)`. -/
theorem kz_jimbo_intertwiner (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ)) :
    ∃ U : (Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ)ˣ,
      WP (U : Matrix (Fin (m + 1) → Fin 2) (Fin (m + 1) → Fin 2) ℂ) ∧
      ∀ x : Hecke ℂ (qC κ) (qC κ)⁻¹ m,
        (U : Matrix _ _ ℂ) * kzHeckeC m c κ x =
          jimboRep (qC κ) (qC_ne_zero κ) m x * (U : Matrix _ _ ℂ) := by
  have hk : ∀ k : ℕ, ∃ U : (Matrix (Wt (m + 1) k) (Wt (m + 1) k) ℂ)ˣ,
      ∀ x : Hecke ℂ (qC κ) (qC κ)⁻¹ m, (U : Matrix _ _ ℂ) * res k (kzHeckeC m c κ x) =
        res k (jimboRep (qC κ) (qC_ne_zero κ) m x) * (U : Matrix _ _ ℂ) := fun k =>
    conj_of_eq_at_zero (n := m)
      (fun κ => resHom k (kzHeckeC m c κ) (WP_kzHeckeC c κ))
      (fun κ => resHom k (jimboRep (qC κ) (qC_ne_zero κ) m) (WP_jimboRep _ _))
      (fun j => by
        simp only [resHom_apply]
        exact continuous_res k (continuous_kzHeckeC_σ c j))
      (fun j => by
        simp only [resHom_apply]
        exact continuous_res k (continuous_jimboRepC_σ j))
      (fun j => by simp only [resHom_apply, kzHeckeC_zero_σ c j]) hκ
  choose U hU using hk
  exact ⟨asmUnit U, WP_asmUnit U, fun x =>
    asm_intertwines (WP_kzHeckeC c κ x) (WP_jimboRep _ _ x) U fun k => hU k x⟩

/-- **Weighted traces from the intertwiner.** If a weight-preserving unit `U` intertwines two
matrices, every weight-diagonal operator has the same weighted trace against both. -/
theorem weighted_trace_eq_of_intertwiner {N : ℕ}
    (U : (Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ)ˣ) (hU : WP (U : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ))
    {X Y : Matrix (Fin N → Fin 2) (Fin N → Fin 2) ℂ}
    (h : (U : Matrix _ _ ℂ) * X = Y * (U : Matrix _ _ ℂ))
    (f : ℕ → ℂ) :
    (Matrix.diagonal (fun a => f (cnt a)) * X).trace =
      (Matrix.diagonal (fun a => f (cnt a)) * Y).trace := by
  refine trace_eq_of_conj U ?_
  rw [← mul_assoc, ← (commute_diag_cnt_of_WP hU f).eq, mul_assoc, h, mul_assoc]

/-- `weighted_trace_kz_eq_jimbo` recovered by conjugation with the single intertwiner. -/
theorem weighted_trace_kz_eq_jimbo_of_intertwiner (c κ : ℂ)
    (hκ : GenericParameter.NotRootOfUnity (qC κ)) (f : ℕ → ℂ) (x : Hecke ℂ (qC κ) (qC κ)⁻¹ m) :
    (Matrix.diagonal (fun a => f (cnt a)) * kzHeckeC m c κ x).trace =
      (Matrix.diagonal (fun a => f (cnt a)) * jimboRep (qC κ) (qC_ne_zero κ) m x).trace := by
  obtain ⟨U, hW, hU⟩ := kz_jimbo_intertwiner c κ hκ
  exact weighted_trace_eq_of_intertwiner U hW (hU x) f

/-- The site-weighted trace identity, by conjugation with the single intertwiner. -/
theorem siteWeight_trace_kz_eq_jimbo_of_intertwiner (c κ : ℂ)
    (hκ : GenericParameter.NotRootOfUnity (qC κ)) (w : Fin 2 → ℂ)
    (x : Hecke ℂ (qC κ) (qC κ)⁻¹ m) :
    (QOU.IwahoriHecke.QuantumTrace.siteWeight w * kzHeckeC m c κ x).trace =
      (QOU.IwahoriHecke.QuantumTrace.siteWeight w * jimboRep (qC κ) (qC_ne_zero κ) m x).trace := by
  rw [siteWeight_eq_diag_cnt (N := m + 1)]
  exact weighted_trace_kz_eq_jimbo_of_intertwiner c κ hκ (fun k => w 0 ^ (m + 1 - k) * w 1 ^ k) x

open QOU.IwahoriHecke.Balanced QOU.IwahoriHecke.BraidGroup in
/-- **The KZ-side mass identity as a corollary of the intertwiner**: same statement as
`KohnoWeighted.braidTrace_eq_kz`, obtained from conjugation by the weight-preserving `U` of
`kz_jimbo_intertwiner` rather than from per-weight-space trace equalities. -/
theorem braidTrace_eq_kz_of_intertwiner (c κ : ℂ) (hκ : GenericParameter.NotRootOfUnity (qC κ))
    (w : Fin 2 → ℂ) (wi : ℂ) (β : BraidGroupN m) :
    braidTrace (qC κ) (qC κ)⁻¹ (mul_inv_cancel₀ (qC_ne_zero κ)) w wi β =
      wi ^ (m + 1) * (QOU.IwahoriHecke.QuantumTrace.siteWeight w *
        kzHeckeC m c κ ((JimboActionKernel.skeinCoxAEquiv (qC κ) (qC_ne_zero κ) m).symm
          ((heckeRep (coxA m) (mul_inv_cancel₀ (qC_ne_zero κ)) coxA_symm β :
            (BalancedHecke (coxA m) (qC κ))ˣ) : BalancedHecke (coxA m) (qC κ)))).trace := by
  rw [siteWeight_trace_kz_eq_jimbo_of_intertwiner c κ hκ, jimboRep_eq_jimbo,
    JimboActionKernel.jimbo_apply, AlgEquiv.apply_symm_apply, braidTrace,
    QOU.IwahoriHecke.MarkovNormalized.markovTr, QOU.IwahoriHecke.QuantumTrace.qTrace]

end Main

end QOU.Mass.KohnoIntertwiner
