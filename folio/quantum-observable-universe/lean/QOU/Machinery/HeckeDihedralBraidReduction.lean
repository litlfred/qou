/-
# The exchange/Matsumoto layer, reduced — and the ρ-equivariance of the channels

Two bricks, one on each remaining wall:

**Wall 1 — the general-rank braid relation, reduced to the proved cell.**
The classical Matsumoto/parabolic argument: for an adjacent generator pair
`(sᵢ, sⱼ)` (order 3), the module `W → R` decomposes over the right cosets
`u₀·⟨sᵢ,sⱼ⟩`, lengths are additive along the coset (`ℓ(u₀d) = ℓ(u₀) + ℓ_D(d)`),
and both generator actions are cell-wise — so the braid relation localizes
to the 6-element dihedral cell, where it is EXACTLY the merged, proved
`H3.braid_operator`. This file formalizes the coset datum as a
**`DihedralCosetStructure`** and proves **`braid_of_dihedral`**: every
descent module carrying such a structure satisfies the braid relation. The
n = 3 self-instance (`dihedralSelf`) shows the datum is non-vacuously
inhabited and re-derives the concrete braid. What remains open — sharply
isolated — is that every Coxeter system carries a `DihedralCosetStructure`
for each adjacent pair (the standard parabolic coset decomposition,
Bourbaki Lie IV–VI §1); that combinatorial fact, not the algebra, is now
the entire content of the general-rank braid.

**Wall 2 — the ρ-equivariance of the channel pair (B1 dictionary, module
level).** `mulStep_star`: entrywise conjugation intertwines the generator
action with `h ↦ star h`. `channel_plus_star`: conjugation carries the e₊
channel vector at `q` to the e₊ channel vector at `star q` of the
conjugated state. On the fibre circle `|q| = 1` one has `star q = q⁻¹`, so
conjugation implements the bar-involution `ρ : q ↦ q⁻¹` on the channel
data — **`F ∘ ρ = conj ∘ F` at the module level, at every rank**, matching
the geometric side (`DeckRealityEquivariance`, T3) from the algebraic side.

HONESTY (STRICT): `braid_of_dihedral` is conditional on the coset datum —
the datum's existence for general Coxeter systems is NOT proved here (and
no instance of the general-n classes is declared). The ρ-equivariance is
the equivariance DATUM of the τ-functor target, not the functor's
existence; `TauRhoHodgeLift` stays open. Nothing wired; `1/(8π)` stays
phase-4.

Base ring (§7c): `[CommRing R]` throughout wall 1; `ℂ` enters only in the
star section (conjugation is the point there) — still pre-archimedean
(no ordering, no `ℝ`-analysis).

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.HeckeDescentQuadratic
import Mathlib.Data.Complex.Basic

namespace QOU.Machinery.HeckeGeneral

variable {W : Type*} {R : Type*} [CommRing R]

/-! ## Wall 1 — the dihedral coset structure and the braid reduction -/

/-- **Dihedral (order-3 pair) coset structure**: the parabolic factorization
datum for an adjacent generator pair. `W` factors as `C × Fin 6` (coset
space × the S₃ cell in the merged NF order `[γ, σ₀, σ₁, L₊, L₋, e⁻]`),
lengths are additive along the cell, and the two step maps act cell-wise by
the proved n = 3 tables (`descentH3σ₀.t`, `descentH3σ₁.t`). Every Coxeter
system carries one for each adjacent pair by the standard parabolic coset
decomposition — that fact is the isolated open combinatorial input. -/
structure DihedralCosetStructure (W : Type*) where
  /-- The coset space (minimal-coset-representative labels). -/
  C : Type*
  /-- The parabolic factorization `W ≃ C × (S₃ cell)`. -/
  equiv : W ≃ C × Fin 6
  /-- The global length. -/
  len : W → ℕ
  /-- The length of the minimal coset representative. -/
  len0 : C → ℕ
  /-- Step map of the first generator. -/
  ti : W → W
  /-- Step map of the second generator. -/
  tj : W → W
  /-- Length additivity along the cell: `ℓ(u₀·d) = ℓ(u₀) + ℓ_D(d)`. -/
  len_add : ∀ w, len w = len0 (equiv w).1 + descentH3σ₀.len (equiv w).2
  /-- The first generator acts cell-wise by the proved σ₀ table. -/
  ti_eq : ∀ w, equiv (ti w) = ((equiv w).1, descentH3σ₀.t (equiv w).2)
  /-- The second generator acts cell-wise by the proved σ₁ table. -/
  tj_eq : ∀ w, equiv (tj w) = ((equiv w).1, descentH3σ₁.t (equiv w).2)

namespace DihedralCosetStructure

variable (S : DihedralCosetStructure W)

/-- The first generator's descent structure, induced from the cell tables
(involution and rank-toggle inherited from the `decide`-checked
`descentH3σ₀`). -/
def Di : DescentStructure W where
  t := S.ti
  len := S.len
  t_invol := fun w => by
    apply S.equiv.injective
    rw [S.ti_eq, S.ti_eq, descentH3σ₀.t_invol]
  len_ne := fun w => by
    rw [S.len_add (S.ti w), S.len_add w, S.ti_eq]
    dsimp only
    have h := descentH3σ₀.len_ne (S.equiv w).2
    omega

/-- The second generator's descent structure. -/
def Dj : DescentStructure W where
  t := S.tj
  len := S.len
  t_invol := fun w => by
    apply S.equiv.injective
    rw [S.tj_eq, S.tj_eq, descentH3σ₁.t_invol]
  len_ne := fun w => by
    rw [S.len_add (S.tj w), S.len_add w, S.tj_eq]
    dsimp only
    have h : descentH3σ₀.len (descentH3σ₁.t (S.equiv w).2)
        ≠ descentH3σ₀.len (S.equiv w).2 := descentH3σ₁.len_ne (S.equiv w).2
    omega

@[simp] lemma Di_t : S.Di.t = S.ti := rfl
@[simp] lemma Di_len : S.Di.len = S.len := rfl
@[simp] lemma Dj_t : S.Dj.t = S.tj := rfl
@[simp] lemma Dj_len : S.Dj.len = S.len := rfl

/-- The fibre restriction of a state: the cell values over a fixed coset. -/
def fib (v : W → R) (c : S.C) : Fin 6 → R := fun e => v (S.equiv.symm (c, e))

lemma ti_symm (c : S.C) (e : Fin 6) :
    S.ti (S.equiv.symm (c, e)) = S.equiv.symm (c, descentH3σ₀.t e) := by
  apply S.equiv.injective
  rw [S.ti_eq]
  simp [Equiv.apply_symm_apply]

lemma tj_symm (c : S.C) (e : Fin 6) :
    S.tj (S.equiv.symm (c, e)) = S.equiv.symm (c, descentH3σ₁.t e) := by
  apply S.equiv.injective
  rw [S.tj_eq]
  simp [Equiv.apply_symm_apply]

lemma len_symm (c : S.C) (e : Fin 6) :
    S.len (S.equiv.symm (c, e)) = S.len0 c + descentH3σ₀.len e := by
  rw [S.len_add]
  simp [Equiv.apply_symm_apply]

/-- **Cell-restriction of the first generator's action**: over a fixed
coset, `mulStep S.Di` IS the proved n = 3 σ₀ action on the fibre. -/
theorem restrict_i (h : R) (v : W → R) (c : S.C) (e : Fin 6) :
    mulStep S.Di h v (S.equiv.symm (c, e))
      = mulStep descentH3σ₀ h (S.fib v c) e := by
  simp only [mulStep, Di_t, Di_len, fib, ti_symm, len_symm]
  congr 1
  exact if_congr (by omega) rfl rfl

/-- **Cell-restriction of the second generator's action.** -/
theorem restrict_j (h : R) (v : W → R) (c : S.C) (e : Fin 6) :
    mulStep S.Dj h v (S.equiv.symm (c, e))
      = mulStep descentH3σ₁ h (S.fib v c) e := by
  simp only [mulStep, Dj_t, Dj_len, fib, tj_symm, len_symm]
  congr 1
  refine if_congr ?_ rfl rfl
  show S.len0 c + descentH3σ₀.len (descentH3σ₁.t e) < S.len0 c + descentH3σ₀.len e
      ↔ descentH3σ₀.len (descentH3σ₁.t e) < descentH3σ₀.len e
  omega

/-- The braid relation on the cell, in `mulStep` form — the merged
`H3.braid_operator` transported through the table bridges. -/
theorem cell_braid (h : R) (V : Fin 6 → R) :
    mulStep descentH3σ₀ h (mulStep descentH3σ₁ h (mulStep descentH3σ₀ h V))
      = mulStep descentH3σ₁ h (mulStep descentH3σ₀ h (mulStep descentH3σ₁ h V)) := by
  simp only [← h3_mulσ₀_eq_mulStep, ← h3_mulσ₁_eq_mulStep]
  exact H3.braid_operator h V

/-- **THE BRAID RELATION AT GENERAL RANK, from the coset datum**:
`σᵢσⱼσᵢ = σⱼσᵢσⱼ` on any descent module carrying a dihedral coset
structure. The proof localizes to the fibres (three applications of the
restriction lemmas) and closes with the proved n = 3 cell braid — the
Matsumoto reduction, formalized: the general braid's entire remaining
content is the existence of the coset datum. -/
theorem braid_of_dihedral (h : R) (v : W → R) :
    mulStep S.Di h (mulStep S.Dj h (mulStep S.Di h v))
      = mulStep S.Dj h (mulStep S.Di h (mulStep S.Dj h v)) := by
  funext w
  have hw : w = S.equiv.symm ((S.equiv w).1, (S.equiv w).2) := by
    simp [Prod.mk.eta, Equiv.symm_apply_apply]
  rw [hw]
  set c := (S.equiv w).1
  set e := (S.equiv w).2
  have fib_i : ∀ u : W → R, S.fib (mulStep S.Di h u) c
      = mulStep descentH3σ₀ h (S.fib u c) :=
    fun u => funext fun e' => S.restrict_i h u c e'
  have fib_j : ∀ u : W → R, S.fib (mulStep S.Dj h u) c
      = mulStep descentH3σ₁ h (S.fib u c) :=
    fun u => funext fun e' => S.restrict_j h u c e'
  rw [S.restrict_i, S.restrict_j, fib_j, fib_i, fib_i, fib_j]
  exact congrFun (cell_braid h (S.fib v c)) e

end DihedralCosetStructure

/-- The n = 3 self-instance: `W = Fin 6` with the trivial coset space —
the datum is non-vacuously inhabited, and `braid_of_dihedral` re-derives
the concrete n = 3 braid. -/
def dihedralSelf : DihedralCosetStructure (Fin 6) where
  C := PUnit
  equiv := (Equiv.punitProd (Fin 6)).symm
  len := descentH3σ₀.len
  len0 := fun _ => 0
  ti := descentH3σ₀.t
  tj := descentH3σ₁.t
  len_add := fun w => by simp [Equiv.punitProd]
  ti_eq := fun w => by simp [Equiv.punitProd]
  tj_eq := fun w => by simp [Equiv.punitProd]

/-! ## Wall 2 — ρ-equivariance of the generator action and the channels -/

section RhoEquivariance

/-- **Conjugation intertwines the generator action with `h ↦ star h`**:
`star ∘ σ(h) = σ(star h) ∘ star`, entrywise, at every rank. The descent
test is real (a length comparison), so conjugation passes straight
through the length rule. -/
theorem mulStep_star (D : DescentStructure W) (h : ℂ) (v : W → ℂ) (u : W) :
    star (mulStep D h v u) = mulStep D (star h) (fun x => star (v x)) u := by
  simp only [mulStep]
  split <;> simp [star_add, star_mul, mul_comm]

/-- **ρ-equivariance of the e₊ channel (B1 dictionary, module level)**:
conjugation carries the e₊ channel vector at `q` to the e₊ channel vector
at `star q` of the conjugated state — at every rank. On the fibre circle
`|q| = 1` one has `star q = q⁻¹`, so this says the bar-involution
`ρ : q ↦ q⁻¹` and complex conjugation implement the SAME move on the
channel data: `F ∘ ρ = conj ∘ F` at the module level, the algebraic twin
of the geometric `deck_eigenspace_exchange` (T3). -/
theorem channel_plus_star (D : DescentStructure W) (q : ℂ) (v : W → ℂ) (u : W) :
    star ((mulStep D (q - q⁻¹) v + q⁻¹ • v) u)
      = (mulStep D (star q - (star q)⁻¹) (fun x => star (v x))
          + (star q)⁻¹ • (fun x => star (v x))) u := by
  simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul, star_add, star_mul]
  rw [mulStep_star]
  have hpar : star (q - q⁻¹) = star q - (star q)⁻¹ := by
    rw [star_sub, star_inv₀]
  rw [hpar, star_inv₀, mul_comm]

/-- **ρ-equivariance of the e₋ channel.** Together with `channel_plus_star`
the full channel pair is ρ-equivariant at every rank. -/
theorem channel_minus_star (D : DescentStructure W) (q : ℂ) (v : W → ℂ) (u : W) :
    star ((mulStep D (q - q⁻¹) v - q • v) u)
      = (mulStep D (star q - (star q)⁻¹) (fun x => star (v x))
          - (star q) • (fun x => star (v x))) u := by
  simp only [Pi.sub_apply, Pi.smul_apply, smul_eq_mul, star_sub, star_mul]
  rw [mulStep_star]
  have hpar : star (q - q⁻¹) = star q - (star q)⁻¹ := by
    rw [star_sub, star_inv₀]
  rw [hpar, mul_comm]

end RhoEquivariance

end QOU.Machinery.HeckeGeneral
