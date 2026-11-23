import QOU.Mass.GammaGammaSelectionTen

/-!
# The Q_β base under γγ + reading-3 word selection

Beans `qou-ales` (owner ruling 2026-09-08: every canonical braid word is selected by
γγ construction and the confinement SDP at `q₀`, never by census) and `qou-vd7j`.

Three pieces.

1. **Every-level admissibility** (owner 2026-10-11, option 3: reading 3 applies at every
   level of the tower). `TowerFrobeniusFeasible` asks for reading-3 feasibility
   (`FrobeniusFeasible`, owner 2026-09-12) of the whole word at every level of a family of
   Wedderburn data, and `TowerSelected` is cost-minimality among such words. Generic
   `[Ring R] [PartialOrder R]` (§7c).

2. **The `qou-vd7j` demand formulation, made exact.** The 0/3558 admissibility result
   imposed `G x = nf(W)` (and a net row). Under convention D the trace form `G` has a
   radical vector `v`. `demand_infeasible_of_radical`: if `G` is symmetric, `G v = 0` and
   `⟨v, nf⟩ ≠ 0`, no `x` solves `G x = nf`. `net_row_satisfiable` is the D-side half of the
   old over-determination diagnosis: once `G x₀ = nf` holds and `⟨1, v⟩ ≠ 0`, the net row can
   always be met along `v`. So the net row is not the obstruction; the demand rows are, and
   only through the radical pairing. `gammaGamma_demand_infeasible_of_pairing_eq_altChar`
   applies this to γγ words, whose alternating character is `1`. The identification
   `⟨v, nf(W)⟩ = altChar W` is a HYPOTHESIS here (it is measured exactly in
   `computations/probes/frobenius_admissibility_net_row_probe.py`, not proved in Lean).

3. **What the selection gives for `Q_β = |ε(W_n − W_p)|·E₀`.** The γγ grammar on three
   strands has no flavour index, so the proton and neutron candidate data are the same.
   `frobeniusSelected_ten_unique`: on `1 < q ≤ 23/20`, with `y_(2,1) > 0`, the reading-3
   selection over the non-zero vertex powers `k ≤ 10` with crossing-count cost is unique and
   equals `β_Bor`. Hence `qbeta_delta_vanishes_of_frobeniusSelected`: for every functional
   `ε` on words, `ε W_n − ε W_p = 0`, so `|ε W_n − ε W_p| · E₀ = 0` for every `E₀`.
   Negative control, `feasible_pair_delta_ne_zero`: feasibility ALONE does not force this —
   `V³` and `V⁶` are both feasible and the crossing-count functional separates them. The
   vanishing comes from the cost-minimal selection, not from reading 3.

## What is NOT claimed

* Nothing about flavour-carrying letters: the result is about the γγ grammar applied alone.
  It is a scope-(a) statement about that candidate family, not an exclusion of the ruling.
* `ε` is evaluated on words; for a linear `ε` this is `ε(W_n − W_p)`. Linearity is the
  reader's step, as everywhere in the `Q_β` functional.
* No AME, CODATA or census value enters.
-/

namespace QOU.QBeta.GammaGammaSdpQBetaBase

open QOU.Mass.GammaGammaWordSelection
open QOU.Mass.GammaGammaSelectorH3
open QOU.Mass.GammaGammaFrobeniusSelection
open QOU.Mass.GammaGammaSelectionTen

/-! ## 1. Every-level reading-3 admissibility -/

section Tower

variable {R : Type*} [Ring R] [PartialOrder R]
variable {W L : Type*} {ι : L → Type*} {d : ∀ l, ι l → ℕ}

/-- **Every-level reading 3** (owner 2026-10-11, option 3): the whole word `w` is
Frobenius-feasible at every level `l` of the tower. Each level carries its own Wedderburn
data `B l` and Markov weights `y l`; a level imposes nothing on blocks of weight `≤ 0`. -/
def TowerFrobeniusFeasible (B : ∀ l, WedderburnBlocks R W (ι l) (d l)) (y : ∀ l, ι l → R)
    (w : W) : Prop :=
  ∀ l, FrobeniusFeasible (B l) (y l) w

/-- Cost-minimal selection under every-level reading 3. -/
structure TowerSelected (B : ∀ l, WedderburnBlocks R W (ι l) (d l)) (y : ∀ l, ι l → R)
    (cands : Set W) (cost : W → R) (w : W) : Prop where
  mem : w ∈ cands
  feasible : TowerFrobeniusFeasible B y w
  minimal : ∀ w' ∈ cands, TowerFrobeniusFeasible B y w' → cost w ≤ cost w'

theorem TowerSelected.cost_eq {B : ∀ l, WedderburnBlocks R W (ι l) (d l)} {y : ∀ l, ι l → R}
    {cands : Set W} {cost : W → R} {w₁ w₂ : W} (h₁ : TowerSelected B y cands cost w₁)
    (h₂ : TowerSelected B y cands cost w₂) : cost w₁ = cost w₂ :=
  le_antisymm (h₁.minimal w₂ h₂.mem h₂.feasible) (h₂.minimal w₁ h₁.mem h₁.feasible)

/-- With a single level, every-level selection is the reading-3 selection of step 5. -/
theorem towerSelected_unit_iff {ι' : Type*} {d' : ι' → ℕ} {B : WedderburnBlocks R W ι' d'} {y : ι' → R}
    {cands : Set W} {cost : W → R} {w : W} :
    TowerSelected (L := Unit) (fun _ => B) (fun _ => y) cands cost w ↔
      FrobeniusSelected B y cands cost w := by
  constructor
  · intro h
    exact ⟨h.mem, h.feasible (), fun w' hm hf => h.minimal w' hm (fun _ => hf)⟩
  · intro h
    exact ⟨h.mem, fun _ => h.feasible, fun w' hm hf => h.minimal w' hm (hf ())⟩

end Tower

/-! ## 2. The `qou-vd7j` demand formulation -/

section Demand

variable {R : Type*} [CommRing R] {n : ℕ}

/-- **The demand rows are infeasible whenever the radical pairs non-trivially.** For a
symmetric `G` with `G v = 0`, every `G x` is orthogonal to `v`, so `G x = nf` forces
`⟨v, nf⟩ = 0`. -/
theorem demand_infeasible_of_radical (G : Matrix (Fin n) (Fin n) R) (hG : G.transpose = G)
    (v nf : Fin n → R) (hv : G.mulVec v = 0) (hpair : v ⬝ᵥ nf ≠ 0) :
    ¬ ∃ x, G.mulVec x = nf := by
  rintro ⟨x, hx⟩
  apply hpair
  have hvG : Matrix.vecMul v G = 0 := by
    have : Matrix.vecMul v G.transpose = G.mulVec v := Matrix.vecMul_transpose G v
    rw [hG] at this
    rw [this, hv]
  rw [← hx, Matrix.dotProduct_mulVec, hvG, zero_dotProduct]

end Demand

section NetRow

variable {K : Type*} [Field K] {n : ℕ}

/-- **The net row is not the obstruction under convention D.** If `G x₀ = nf`, `G v = 0` and
`⟨1, v⟩ ≠ 0`, then for every target `A` some point `x₀ + t v` satisfies both `G x = nf` and the
net row `⟨1, x⟩ = A`. -/
theorem net_row_satisfiable (G : Matrix (Fin n) (Fin n) K) (v x₀ nf : Fin n → K)
    (hx₀ : G.mulVec x₀ = nf) (hv : G.mulVec v = 0) (h1v : (fun _ => (1 : K)) ⬝ᵥ v ≠ 0)
    (A : K) :
    ∃ x, G.mulVec x = nf ∧ (fun _ => (1 : K)) ⬝ᵥ x = A := by
  set one : Fin n → K := fun _ => 1
  refine ⟨x₀ + ((A - one ⬝ᵥ x₀) / (one ⬝ᵥ v)) • v, ?_, ?_⟩
  · rw [Matrix.mulVec_add, Matrix.mulVec_smul, hv, smul_zero, add_zero, hx₀]
  · rw [dotProduct_add, dotProduct_smul, smul_eq_mul, div_mul_cancel₀ _ h1v]
    ring

end NetRow

section GammaGammaDemand

variable {K : Type*} [Field K] {n : ℕ}

/-- **No γγ word is demand-admissible**, given the measured identification of the radical
pairing with the alternating character. The γγ alternating character is exactly `1`
(`altChar_eq_one`), so the pairing is `1 ≠ 0`. This is a statement about the `G x = nf`
formulation of `qou-vd7j`, not about reading 3. -/
theorem gammaGamma_demand_infeasible_of_pairing_eq_altChar {q : K} (hq : q ≠ 0)
    (G : Matrix (Fin n) (Fin n) K) (hG : G.transpose = G) (v : Fin n → K)
    (hv : G.mulVec v = 0) (nf : Word → Fin n → K)
    (hpairing : ∀ w, v ⬝ᵥ nf w = altChar q w) {w : Word} (hw : GammaGammaWord w) :
    ¬ ∃ x, G.mulVec x = nf w := by
  refine demand_infeasible_of_radical G hG v (nf w) hv ?_
  rw [hpairing, altChar_eq_one hq hw]
  exact one_ne_zero

end GammaGammaDemand

/-! ## 3. The selection and `Q_β` -/

section Selection

/-- **The reading-3 selection over ten vertices is unique**: on `1 < q ≤ 23/20` with
`y_(2,1) > 0`, any cost-minimal Frobenius-feasible non-zero vertex power with `k ≤ 10` is
`β_Bor = V³`. -/
theorem frobeniusSelected_ten_unique {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (y : H3Block → ℝ) (hy : 0 < y .std) {w : Word}
    (hw : FrobeniusSelected (hoefsmitH3 q) y (vertexPowCands 10) (fun w => (w.length : ℝ)) w) :
    w = borromean := by
  have hc := hw.cost_eq (frobeniusSelected_borromean_ten hq1 hq2 y hy)
  obtain ⟨k, _, _, rfl⟩ := hw.mem
  have hlen : ((vertexPow k).length : ℝ) = ((vertexPow 3).length : ℝ) := by
    simpa [vertexPow_three] using hc
  rw [vertexPow_length, vertexPow_length] at hlen
  have : k = 3 := by
    have : (2 * k : ℕ) = 2 * 3 := by exact_mod_cast hlen
    omega
  rw [this, vertexPow_three]

/-- **`Q_β` on the γγ + reading-3 base is zero.** The proton and neutron words are each
reading-3-selected from the same data (the γγ grammar on three strands has no flavour index),
so they coincide, and every functional `ε` takes the same value on both. Hence
`|ε W_n − ε W_p| · E₀ = 0` for every `E₀`, in particular for the ruled `ε` (Markov trace at
`z_D`) and the tower-summed `E₀`. -/
theorem qbeta_delta_vanishes_of_frobeniusSelected {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (y : H3Block → ℝ) (hy : 0 < y .std) {wp wn : Word}
    (hp : FrobeniusSelected (hoefsmitH3 q) y (vertexPowCands 10) (fun w => (w.length : ℝ)) wp)
    (hn : FrobeniusSelected (hoefsmitH3 q) y (vertexPowCands 10) (fun w => (w.length : ℝ)) wn)
    (ε : Word → ℝ) (E₀ : ℝ) :
    |ε wn - ε wp| * E₀ = 0 := by
  rw [frobeniusSelected_ten_unique hq1 hq2 y hy hp, frobeniusSelected_ten_unique hq1 hq2 y hy hn]
  simp

/-- **Negative control: feasibility alone does not force the vanishing.** `V³` and `V⁶` are
both reading-3-feasible on the interval, and the crossing-count functional separates them
(`12 − 6 = 6`). The zero above therefore comes from the cost-minimal selection. -/
theorem feasible_pair_delta_ne_zero {q : ℝ} (hq1 : 1 < q) (hq2 : q ≤ 23 / 20)
    (y : H3Block → ℝ) (hy : 0 < y .std) :
    FrobeniusFeasible (hoefsmitH3 q) y (vertexPow 3) ∧
      FrobeniusFeasible (hoefsmitH3 q) y (vertexPow 6) ∧
      ((vertexPow 6).length : ℝ) - ((vertexPow 3).length : ℝ) ≠ 0 := by
  refine ⟨(vertexPow_frobeniusFeasible_iff_three_dvd hq1 hq2 y hy 3 (by norm_num)
      (by norm_num)).2 ⟨1, rfl⟩,
    (vertexPow_frobeniusFeasible_iff_three_dvd hq1 hq2 y hy 6 (by norm_num)
      (by norm_num)).2 ⟨2, rfl⟩, ?_⟩
  rw [vertexPow_length, vertexPow_length]
  norm_num

end Selection

end QOU.QBeta.GammaGammaSdpQBetaBase
