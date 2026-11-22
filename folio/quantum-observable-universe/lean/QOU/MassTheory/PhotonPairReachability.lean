import Mathlib.Tactic

/-!
# Two photons cannot move a marked strand far: a reachability obstruction

Chip on the six-strand γγ pair test (`computations/probes/six_strand_photon_pair/`, PR #9050).
The photon on three consecutive strands `i, i+1, i+2` is (owner ruling 2026-11-20, constant term
fixed to 1 by ruling 2026-11-22)

  `γᵢ(a, b, c) = 1 + a·σᵢ + b·σᵢ₊₁ + c·σᵢσᵢ₊₁⁻¹`.

We work in the **one-marked-strand sector** of the Jimbo representation of the Hecke algebra on
`(K²)^{⊗n}`: the span of the basis vectors `e_p` with exactly one strand marked, at site `p`.
There `σᵢ` acts by

  `σᵢ e_{i+1} = e_i`, `σᵢ e_i = e_{i+1} + h e_i`, `σᵢ e_p = q e_p` (`p ∉ {i, i+1}`),

with `h = q − q⁻¹`, and `σᵢ⁻¹` by `σᵢ⁻¹ e_i = e_{i+1}`, `σᵢ⁻¹ e_{i+1} = e_i − h e_{i+1}`,
`σᵢ⁻¹ e_p = q⁻¹ e_p`. Vectors are modelled as functions `ℕ → K` (only finitely many sites matter).

**The obstruction.** A photon `γᵢ` only mixes the three sites of its block `Bᵢ = {i, i+1, i+2}`
and multiplies every other site by the same scalar `κ = 1 + aq + bq + c·q·q⁻¹`
(`photon_apply_off`). So a product of two photons `γᵢγⱼ` can move the marked strand from `s` only
inside `Bⱼ` and then inside `Bᵢ` (`photonPair_apply_eq_zero`). If a braid word moves it from `s`
to a site `r` outside that reach with nonzero amplitude, the word is not a nonzero multiple of
`γᵢγⱼ` (`not_photonPair_mul`), whatever the weights `a, b, c, a', b', c'`.

Everything is generic: any commutative ring `K`, any `q, qi` (no relation `q·qi = 1` is needed
for the obstruction itself).

-- Ref: [leitner2026] computations/probes/six_strand_photon_pair/six_strand_pair_probe.py
-- Ref: [leitner2026] folio/quantum-observable-universe/brings-surface/photon.md
-/

namespace QOU.MassTheory.PhotonPairReachability

variable {K : Type*} [CommRing K]

/-- `σᵢ` on the one-marked-strand sector. -/
def sig (q qi : K) (i : ℕ) (v : ℕ → K) : ℕ → K := fun p =>
  if p = i then v (i + 1) + (q - qi) * v i
  else if p = i + 1 then v i
  else q * v p

/-- `σᵢ⁻¹` on the one-marked-strand sector. -/
def sigInv (q qi : K) (i : ℕ) (v : ℕ → K) : ℕ → K := fun p =>
  if p = i then v (i + 1)
  else if p = i + 1 then v i - (q - qi) * v (i + 1)
  else qi * v p

/-- The photon `γᵢ(a, b, c) = 1 + a σᵢ + b σᵢ₊₁ + c σᵢ σᵢ₊₁⁻¹` acting on the sector. -/
def photon (q qi a b c : K) (i : ℕ) (v : ℕ → K) : ℕ → K := fun p =>
  v p + a * sig q qi i v p + b * sig q qi (i + 1) v p
    + c * sig q qi i (sigInv q qi (i + 1) v) p

/-- The scalar by which `γᵢ(a, b, c)` acts on sites outside its block. -/
def kappa (q qi a b c : K) : K := 1 + a * q + b * q + c * (q * qi)

/-- The block `Bᵢ = {i, i+1, i+2}` of the photon at `i`. -/
def InBlock (i p : ℕ) : Prop := p = i ∨ p = i + 1 ∨ p = i + 2

instance (i p : ℕ) : Decidable (InBlock i p) := by unfold InBlock; infer_instance

/-- Off its block, a photon is the scalar `κ`. -/
theorem photon_apply_off (q qi a b c : K) (i : ℕ) (v : ℕ → K) {p : ℕ}
    (hp : ¬ InBlock i p) : photon q qi a b c i v p = kappa q qi a b c * v p := by
  unfold InBlock at hp
  push_neg at hp
  obtain ⟨h0, h1, h2⟩ := hp
  have h1' : p ≠ i + 1 + 1 := by omega
  simp [photon, sig, sigInv, kappa, h0, h1, h1']
  ring

/-- A vector vanishing on the block is scaled by `κ`. -/
theorem photon_of_vanish (q qi a b c : K) (i : ℕ) (v : ℕ → K)
    (hv : ∀ p, InBlock i p → v p = 0) (p : ℕ) :
    photon q qi a b c i v p = kappa q qi a b c * v p := by
  by_cases hp : InBlock i p
  · have e0 : v i = 0 := hv i (Or.inl rfl)
    have e1 : v (i + 1) = 0 := hv (i + 1) (Or.inr (Or.inl rfl))
    have e2 : v (i + 1 + 1) = 0 := hv (i + 2) (Or.inr (Or.inr rfl))
    rw [hv p hp]
    rcases hp with rfl | rfl | rfl
    · simp [photon, sig, sigInv, e0, e1, e2]
    · simp [photon, sig, sigInv, e0, e1, e2]
    · simp [photon, sig, sigInv, e0, e1, e2]
  · exact photon_apply_off q qi a b c i v hp

/-- The basis vector `e_s`: the marked strand at site `s`. -/
def basisVec (s : ℕ) : ℕ → K := fun p => if p = s then 1 else 0

/-- At the top site `i+2`, a photon only sees `v (i+1)` and `v (i+2)`. In particular `γᵢ e_i`
vanishes at `i+2`: the bottom strand of a block cannot jump to the top in one photon. -/
theorem photon_top_eq_zero (q qi a b c : K) (i : ℕ) (v : ℕ → K)
    (h1 : v (i + 1) = 0) (h2 : v (i + 2) = 0) : photon q qi a b c i v (i + 2) = 0 := by
  have h2' : v (i + 1 + 1) = 0 := h2
  have n0 : i + 2 ≠ i := by omega
  have n1 : i + 2 ≠ i + 1 := by omega
  simp [photon, sig, sigInv, n0, n1, h1, h2, h2']

/-- First stage of the reach: where `γⱼ e_s` can be nonzero. -/
def Reach1 (j s p : ℕ) : Prop :=
  if s = j then (p = j ∨ p = j + 1)
  else if InBlock j s then InBlock j p else p = s

instance (j s p : ℕ) : Decidable (Reach1 j s p) := by unfold Reach1; infer_instance

/-- Second stage: where `γᵢ γⱼ e_s` can be nonzero. -/
def Reach2 (i j s r : ℕ) : Prop :=
  Reach1 j s r
    ∨ ((r = i ∨ r = i + 1) ∧ (Reach1 j s i ∨ Reach1 j s (i + 1) ∨ Reach1 j s (i + 2)))
    ∨ (r = i + 2 ∧ (Reach1 j s (i + 1) ∨ Reach1 j s (i + 2)))

instance (i j s r : ℕ) : Decidable (Reach2 i j s r) := by unfold Reach2; infer_instance

/-- `γⱼ e_s` vanishes outside `Reach1`. -/
theorem photon_basis_eq_zero (q qi a b c : K) (j s p : ℕ) (hp : ¬ Reach1 j s p) :
    photon q qi a b c j (basisVec s) p = 0 := by
  unfold Reach1 at hp
  by_cases hsj : s = j
  · rw [if_pos hsj] at hp
    push_neg at hp
    obtain ⟨hp0, hp1⟩ := hp
    subst hsj
    by_cases hb : InBlock s p
    · have hp2 : p = s + 2 := by unfold InBlock at hb; omega
      subst hp2
      exact photon_top_eq_zero q qi a b c s _ (by simp [basisVec]) (by simp [basisVec])
    · rw [photon_apply_off q qi a b c s _ hb]
      simp [basisVec, hp0]
  · rw [if_neg hsj] at hp
    by_cases hs : InBlock j s
    · rw [if_pos hs] at hp
      rw [photon_apply_off q qi a b c j _ hp]
      have : p ≠ s := fun h => hp (h ▸ hs)
      simp [basisVec, this]
    · rw [if_neg hs] at hp
      rw [photon_of_vanish q qi a b c j (basisVec s)
        (fun p' hp' => by
          have : p' ≠ s := fun h => hs (h ▸ hp')
          simp [basisVec, this]) p]
      simp [basisVec, hp]

/-- **Reachability.** `γᵢ(a,b,c) γⱼ(a',b',c') e_s` vanishes at every site outside `Reach2`. -/
theorem photonPair_apply_eq_zero (q qi a b c a' b' c' : K) (i j s r : ℕ)
    (hr : ¬ Reach2 i j s r) :
    photon q qi a b c i (photon q qi a' b' c' j (basisVec s)) r = 0 := by
  unfold Reach2 at hr
  push_neg at hr
  obtain ⟨h1, h2, h3⟩ := hr
  have hu : ∀ p, ¬ Reach1 j s p → photon q qi a' b' c' j (basisVec s) p = 0 :=
    fun p hp => photon_basis_eq_zero q qi a' b' c' j s p hp
  by_cases hb : InBlock i r
  · rcases hb with rfl | rfl | rfl
    · obtain ⟨n0, n1, n2⟩ := h2 (Or.inl rfl)
      rw [photon_of_vanish q qi a b c r _ (fun p hp => by
        rcases hp with rfl | rfl | rfl
        · exact hu _ n0
        · exact hu _ n1
        · exact hu _ n2) r, hu r h1, mul_zero]
    · obtain ⟨n0, n1, n2⟩ := h2 (Or.inr rfl)
      rw [photon_of_vanish q qi a b c i _ (fun p hp => by
        rcases hp with rfl | rfl | rfl
        · exact hu _ n0
        · exact hu _ n1
        · exact hu _ n2) (i + 1), hu _ h1, mul_zero]
    · obtain ⟨n1, n2⟩ := h3 rfl
      exact photon_top_eq_zero q qi a b c i _ (hu _ n1) (hu _ n2)
  · rw [photon_apply_off q qi a b c i _ hb, hu r h1, mul_zero]

/-! ### The sector is a Hecke module

The maps `sig`/`sigInv` satisfy the defining relations of the Iwahori–Hecke algebra
(`σᵢ² = h σᵢ + 1`, braid relations, far commutation, `σᵢσᵢ⁻¹ = 1`) when `q·qi = 1`. -/

theorem sig_sigInv (q qi : K) (hqi : q * qi = 1) (i : ℕ) (v : ℕ → K) :
    sig q qi i (sigInv q qi i v) = v := by
  funext p
  simp only [sig, sigInv]
  split_ifs <;> subst_vars <;> first | omega | ring_nf | skip
  all_goals linear_combination (v p) * hqi

theorem sigInv_sig (q qi : K) (hqi : q * qi = 1) (i : ℕ) (v : ℕ → K) :
    sigInv q qi i (sig q qi i v) = v := by
  funext p
  simp only [sig, sigInv]
  split_ifs <;> subst_vars <;> first | omega | ring_nf | skip
  all_goals linear_combination (v p) * hqi

/-- The Hecke quadratic relation `σᵢ² = (q − qi)σᵢ + 1`. -/
theorem sig_quadratic (q qi : K) (hqi : q * qi = 1) (i : ℕ) (v : ℕ → K) :
    sig q qi i (sig q qi i v) = fun p => (q - qi) * sig q qi i v p + v p := by
  funext p
  simp only [sig]
  split_ifs <;> subst_vars <;> first | omega | ring_nf | skip
  all_goals linear_combination (v p) * hqi

/-- The braid relation `σᵢσᵢ₊₁σᵢ = σᵢ₊₁σᵢσᵢ₊₁`. -/
theorem sig_braid (q qi : K) (hqi : q * qi = 1) (i : ℕ) (v : ℕ → K) :
    sig q qi i (sig q qi (i + 1) (sig q qi i v)) =
      sig q qi (i + 1) (sig q qi i (sig q qi (i + 1) v)) := by
  funext p
  simp only [sig]
  split_ifs <;> subst_vars <;>
    first | omega | ring1 | linear_combination ((qi - q) * v p) * hqi | linear_combination ((q - qi) * v p) * hqi

/-- Far commutation `σᵢσₖ = σₖσᵢ` for `i + 2 ≤ k`. -/
theorem sig_comm (q qi : K) (i k : ℕ) (hik : i + 2 ≤ k) (v : ℕ → K) :
    sig q qi i (sig q qi k v) = sig q qi k (sig q qi i v) := by
  funext p
  simp only [sig]
  split_ifs <;> subst_vars <;> first | omega | ring

/-- A braid word acting on the sector: `(k, true)` is `σₖ`, `(k, false)` is `σₖ⁻¹`; the first
letter acts last, as in a product of operators. -/
def wordAct (q qi : K) : List (ℕ × Bool) → (ℕ → K) → (ℕ → K)
  | [], v => v
  | (k, true) :: w, v => sig q qi k (wordAct q qi w v)
  | (k, false) :: w, v => sigInv q qi k (wordAct q qi w v)

/-- **No factorisation through two photons.** If a map `W` on the sector (the image of a braid
word) moves the marked strand from `s` to a site `r` outside the reach of `γᵢγⱼ`, with nonzero
amplitude, then `γᵢγⱼ = μ·W` has no solution with `μ ≠ 0`, for any weights, over a domain. -/
theorem not_photonPair_eq_smul [IsDomain K] (q qi a b c a' b' c' μ : K) (i j s r : ℕ)
    (W : (ℕ → K) → (ℕ → K)) (hr : ¬ Reach2 i j s r) (hW : W (basisVec s) r ≠ 0)
    (hμ : μ ≠ 0) :
    ¬ ∀ v, photon q qi a b c i (photon q qi a' b' c' j v) = fun p => μ * W v p := by
  intro h
  have := congrFun (h (basisVec s)) r
  rw [photonPair_apply_eq_zero q qi a b c a' b' c' i j s r hr] at this
  exact mul_ne_zero hμ hW this.symm

end QOU.MassTheory.PhotonPairReachability
