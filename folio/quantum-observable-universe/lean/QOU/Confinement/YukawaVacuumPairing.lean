import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.Order.Field.Power
import Mathlib.Tactic

/-!
# A Yukawa-type pairing of the Higgs vacuum with doublet strands (route Y)

Bean `qou-99qc`. Owner route Y (Carl, 2026-11-21). Pre-registered in
`computations/probes/qbeta_yukawa_higgs_pairing/PREREGISTRATION.md` (commit `76ddb991d3`).

PR #8676 (`HyperchargeGradingNoGo.total_eq_iff`) showed that a per-strand energy `χ` separates
`n ⊗ ν = (q u)(q d)(q d)(ℓ u)` from `p ⊗ e⁻ = (q u)(q u)(q d)(ℓ d)` iff
`χ(q,d) + χ(ℓ,u) ≠ χ(q,u) + χ(ℓ,d)` — a strand-type × flavour interaction. The corpus has the
Higgs vacuum as a point / copoint pair with idempotent `e_H`, residual `1 − e_H` and `tr e_H = 1`
(`QuantumObservableUniverses/HiggsVacuumResidual.lean`), but no action on a doublet strand. This
file builds the minimal pairings and records what is forced and what is free.

## Results (generic field `R`, §7c; an ordered field only where stated)

**Part 1 — the unbroken grading forces weight-diagonal operators.** Doublet grading
`Kg a b = diag(a, b)`, `a ≠ b`.
* `eq_diag_of_commute` : an operator commuting with `Kg a b` is `E₀₀ • Pu + E₁₁ • Pd`.
* `idem_commute_trace_one` : a trace-one idempotent commuting with `Kg a b` is `Pu` or `Pd`.
  So `e_H` restricted to a doublet is a weight projector and `1 − e_H` is the other one.

**Part 2 — `tr e_H = 1` forces the vev slot to have grading weight 0.**
* `qtrace_Pu`, `qtrace_Pd` : `Tr(Kg a b * P_u) = a`, `Tr(Kg a b * P_d) = b`.
* `qtrace_weight_eq_one_iff` : with `a = q^{n_u}`, `b = q^{n_d}` and `q` not a root of unity,
  the pivotal trace of the vev projector is 1 iff the vev slot has weight exponent 0.
* `no_vev_on_bare_T3` : on the bare `K = q^{2T³}` (`n = ±1`) no weight projector has trace 1.
  The owner's `tr e_H = 1` therefore needs a hypercharge-shifted Higgs doublet with a neutral slot.
* `vev_charge_zero_of_trace_one` : for the charge grading `diag(q^{cH 0}, q^{cH 1})` on the Higgs
  doublet, `tr e_H = 1` puts the vev in a charge-0 slot (the input Part 4 uses).
* `not_root_of_unity_of_one_lt` : `1 < q` on an ordered field supplies the hypothesis.

**Part 3 — every type-blind pairing gives zero split.**
* `split_general` : per-type energies `a_t` (vev slot `d`) and `b_t` (slot `u`) give
  `split = (a_q − b_q) − (a_ℓ − b_ℓ)`. Four free numbers; one combination enters.
* `split_typeBlind` : if the energy does not depend on strand type, the split is 0.
* `compress_vev_d`, `compress_vev_u` : compressing the `U_q(gl₂)`-invariant `a·1 + b·Ř` (Jimbo
  `Ř`, matter ⊗ Higgs) by the vev gives `diag(a, a + b q)` (vev in `d`) and
  `diag(a + b q, a + b(q − q⁻¹))` (vev in `u`). Flavour-asymmetric (T³ is broken), type-blind.

**Part 4 — the charge selection rule (the one candidate that is not type-blind).**
A bilinear pairing `B : Higgs ⊗ matter → 𝟙` (a `Fin 2 × Fin 2` matrix) invariant under the
unbroken grading `q^{3Q}` (charges cleared to integers) satisfies `B i j ≠ 0 → cH i + cM j = 0`.
* `pairing_selection` : with the vev slot of charge 0, `B vev j = 0` for every charged slot `j`.
* `pairing_quark_zero` : with the Standard-Model charges (`3Q`: u 2, d −1) the vacuum pairing with
  a quark strand vanishes identically.
* `pairing_lepton` : on a lepton strand (`3Q`: ν 0, e⁻ −3) it vanishes on `e⁻`; only the `ν`
  coupling is unconstrained.
* `split_neutral` : the induced energy `χ(t,f) = B_t(vev, f)²` gives `split = B_ℓ(vev, ν)²`.
  Forced: three of the four couplings are 0. Free: one, `y_ν = B_ℓ(vev, ν)`. No `q` enters.

## What is NOT claimed

* No coupling, no energy scale is derived. `y_ν` is free; with the idempotent normalisation
  (`χ(ℓ,u) = 1`) the split is `1` in units of an undetermined scale.
* Part 4 gives energy to `ν`, not to `e⁻`: the opposite of the Standard Model, where the 3-point
  vertex `L̄ Φ e_R` with a right-handed singlet gives `e⁻` its mass. No single strand is a
  right-handed singlet. The corpus does have one two-strand candidate, the right line of the
  matter ⊗ Higgs crossing (`RightHandedSingletChannel.lean`, route Y step 2); reading it as `e_R`
  is an owner decision.
* The Standard-Model electric charges are inputs (labels), as in #8676. Premise L (lepton = fourth
  doublet strand) is assumed in Parts 3–4 and is undecided by the owner.
* Nothing here identifies any split with `Q_β`.

-- Ref: [jimbo1986] https://doi.org/10.1007/BF00400222
-- Ref: [kassel1995] Quantum Groups, Springer GTM 155, §VII–VIII
-/

namespace QOU.QuarkState.YukawaVacuumPairing

open Matrix

variable {R : Type*} [Field R]

/-! ## Part 1: operators commuting with the unbroken grading -/

/-- Doublet grading `diag(a, b)` (slot 0 = `u`, slot 1 = `d`). -/
def Kg (a b : R) : Matrix (Fin 2) (Fin 2) R := !![a, 0; 0, b]

/-- Weight projector on the `u` slot. -/
def Pu : Matrix (Fin 2) (Fin 2) R := !![1, 0; 0, 0]

/-- Weight projector on the `d` slot. -/
def Pd : Matrix (Fin 2) (Fin 2) R := !![0, 0; 0, 1]

/-- **An operator commuting with the grading is weight-diagonal.** -/
theorem eq_diag_of_commute (a b : R) (hab : a ≠ b) (E : Matrix (Fin 2) (Fin 2) R)
    (h : Kg a b * E = E * Kg a b) : E = E 0 0 • Pu + E 1 1 • Pd := by
  have h01 := congrFun (congrFun h 0) 1
  have h10 := congrFun (congrFun h 1) 0
  simp [Kg, Matrix.mul_apply, Fin.sum_univ_two] at h01 h10
  have hab' : a - b ≠ 0 := sub_ne_zero.mpr hab
  have e01 : E 0 1 = 0 := by
    have : (a - b) * E 0 1 = 0 := by linear_combination h01
    rcases mul_eq_zero.mp this with h | h
    · exact absurd h hab'
    · exact h
  have e10 : E 1 0 = 0 := by
    have : (b - a) * E 1 0 = 0 := by linear_combination h10
    rcases mul_eq_zero.mp this with h | h
    · exact absurd h (by intro h'; exact hab' (by linear_combination -h'))
    · exact h
  ext i j; fin_cases i <;> fin_cases j <;> simp [Pu, Pd, e01, e10]

/-- **A trace-one idempotent commuting with the grading is a weight projector.** -/
theorem idem_commute_trace_one (a b : R) (hab : a ≠ b) (e : Matrix (Fin 2) (Fin 2) R)
    (hc : Kg a b * e = e * Kg a b) (hi : e * e = e) (ht : trace e = 1) :
    e = Pu ∨ e = Pd := by
  have hd := eq_diag_of_commute a b hab e hc
  set x := e 0 0
  set y := e 1 1
  have hx : x * x = x := by
    have := congrFun (congrFun hi 0) 0
    rw [hd] at this
    simpa [Pu, Pd, Matrix.mul_apply, Fin.sum_univ_two] using this
  have hy : y * y = y := by
    have := congrFun (congrFun hi 1) 1
    rw [hd] at this
    simpa [Pu, Pd, Matrix.mul_apply, Fin.sum_univ_two] using this
  have hxy : x + y = 1 := by
    rw [hd] at ht
    simpa [Matrix.trace, Fin.sum_univ_two, Pu, Pd] using ht
  have hx' : x = 0 ∨ x = 1 := by
    have : x * (x - 1) = 0 := by linear_combination hx
    rcases mul_eq_zero.mp this with h | h
    · exact Or.inl h
    · exact Or.inr (sub_eq_zero.mp h)
  rcases hx' with h0 | h1
  · right
    have hy1 : y = 1 := by linear_combination hxy - h0
    rw [hd, h0, hy1]; simp
  · left
    have hy0 : y = 0 := by linear_combination hxy - h1
    rw [hd, h1, hy0]; simp

/-! ## Part 2: the pivotal trace of the vev projector -/

theorem qtrace_Pu (a b : R) : trace (Kg a b * Pu) = a := by
  simp [Kg, Pu, Matrix.trace, Fin.sum_univ_two]

theorem qtrace_Pd (a b : R) : trace (Kg a b * Pd) = b := by
  simp [Kg, Pd, Matrix.trace, Fin.sum_univ_two]

/-- **`tr e_H = 1` iff the vev slot has weight exponent 0**, for `q` not a root of unity. -/
theorem qtrace_weight_eq_one_iff (q : R) (hq : ∀ n : ℤ, q ^ n = 1 → n = 0) (n : ℤ) :
    q ^ n = 1 ↔ n = 0 := by
  constructor
  · exact hq n
  · intro h; rw [h, zpow_zero]

/-- **No vacuum point on the bare `q^{2T³}` doublet.** With weights `q, q⁻¹`, neither weight
projector has pivotal trace 1. -/
theorem no_vev_on_bare_T3 (q : R) (hq : ∀ n : ℤ, q ^ n = 1 → n = 0) :
    trace (Kg (q ^ (1 : ℤ)) (q ^ (-1 : ℤ)) * Pu) ≠ 1 ∧
      trace (Kg (q ^ (1 : ℤ)) (q ^ (-1 : ℤ)) * Pd) ≠ 1 := by
  rw [qtrace_Pu, qtrace_Pd]
  exact ⟨fun h => by have := hq 1 h; norm_num at this,
    fun h => by have := hq (-1) h; norm_num at this⟩

/-- Weight projector on slot `v`. -/
def Pslot (v : Fin 2) : Matrix (Fin 2) (Fin 2) R := if v = 0 then Pu else Pd

/-- **Link to Part 4: `tr e_H = 1` for the charge grading `q^{cH}` puts the vev in a charge-0
slot.** If the Higgs doublet is graded by `diag(q^{cH 0}, q^{cH 1})` and the vev projector on slot
`v` has pivotal trace 1, then `cH v = 0`. -/
theorem vev_charge_zero_of_trace_one (q : R) (hq : ∀ n : ℤ, q ^ n = 1 → n = 0)
    (cH : Fin 2 → ℤ) (v : Fin 2)
    (ht : trace (Kg (q ^ (cH 0)) (q ^ (cH 1)) * Pslot v) = 1) : cH v = 0 := by
  by_cases hv : v = 0
  · subst hv
    rw [Pslot, if_pos rfl, qtrace_Pu] at ht; exact hq _ ht
  · have hv1 : v = 1 := by omega
    subst hv1
    rw [Pslot, if_neg hv, qtrace_Pd] at ht; exact hq _ ht

/-- On an ordered field, `1 < q` means `q` is not a root of unity (for integer powers). -/
theorem not_root_of_unity_of_one_lt {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L]
    (q : L) (hq : 1 < q) : ∀ n : ℤ, q ^ n = 1 → n = 0 := by
  intro n h
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have := zpow_right_injective₀ hq0 (ne_of_gt hq)
  apply this
  simpa using h

/-! ## Part 3: per-strand energies, the general split, and type-blind pairings -/

/-- Strand type. -/
inductive Ty | quark | lepton
  deriving DecidableEq

/-- Strand flavour (doublet slot): `u` = slot 0, `d` = slot 1. -/
inductive Fl | u | d
  deriving DecidableEq

/-- Released energy `E(n ⊗ ν) − E(p ⊗ e⁻)` of a per-strand additive energy, on the states
`n ⊗ ν = (q u)(q d)(q d)(ℓ u)` and `p ⊗ e⁻ = (q u)(q u)(q d)(ℓ d)` of #8676. -/
def split (χ : Ty → Fl → R) : R :=
  (χ .quark .u + χ .quark .d + χ .quark .d + χ .lepton .u) -
    (χ .quark .u + χ .quark .u + χ .quark .d + χ .lepton .d)

/-- The split reduces to the type × flavour interaction (#8676 `total_eq_iff`). -/
theorem split_eq_interaction (χ : Ty → Fl → R) :
    split χ = (χ .quark .d - χ .quark .u) - (χ .lepton .d - χ .lepton .u) := by
  unfold split; ring

/-- Diagonal per-type energy: `a t` on the vev slot `d`, `b t` on `u`. -/
def diagEnergy (a b : Ty → R) : Ty → Fl → R
  | t, .u => b t
  | t, .d => a t

/-- **General split: four free numbers, one combination enters.** -/
theorem split_general (a b : Ty → R) :
    split (diagEnergy a b) = (a .quark - b .quark) - (a .lepton - b .lepton) := by
  rw [split_eq_interaction]; rfl

/-- **A type-blind energy gives zero split.** -/
theorem split_typeBlind (ε : Fl → R) : split (fun _ f => ε f) = 0 := by
  unfold split; ring

/-- Jimbo `Ř` on `V ⊗ V`, basis `uu, ud, du, dd` (first factor = matter, second = Higgs). -/
def Rc (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- Compression of a `V ⊗ V` operator by a vev in Higgs slot `s` (`0 = u`, `1 = d`):
`E_{ij} = M_{(i,s),(j,s)}`, index `(i, s) ↦ 2i + s`. -/
def compress (M : Matrix (Fin 4) (Fin 4) R) (s : Fin 2) : Matrix (Fin 2) (Fin 2) R :=
  fun i j => M ⟨2 * i.val + s.val, by omega⟩ ⟨2 * j.val + s.val, by omega⟩

/-- **Vev in `d`:** `a·1 + b·Ř` compresses to `diag(a, a + b q)`. -/
theorem compress_vev_d (q a b : R) :
    compress (a • (1 : Matrix (Fin 4) (Fin 4) R) + b • Rc q) 1 = !![a, 0; 0, a + b * q] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [compress, Rc]

/-- **Vev in `u`:** `a·1 + b·Ř` compresses to `diag(a + b q, a + b(q − q⁻¹))`. -/
theorem compress_vev_u (q a b : R) :
    compress (a • (1 : Matrix (Fin 4) (Fin 4) R) + b • Rc q) 0 =
      !![a + b * q, 0; 0, a + b * (q - q⁻¹)] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [compress, Rc]

/-- **The compressed `Ř` pairing is type-blind, so its split is 0** (vev in `d`). -/
theorem split_compress_vev_d (q a b : R) :
    split (fun _ f => match f with | .u => a | .d => a + b * q) = 0 :=
  split_typeBlind _

/-! ## Part 4: the charge selection rule -/

/-- `B` is invariant under the grading `q^{c}` with integer charges `cH` (Higgs slots) and `cM`
(matter slots): `B(g x, g y) = B(x, y)` on weight vectors. -/
def Invariant (q : R) (cH cM : Fin 2 → ℤ) (B : Matrix (Fin 2) (Fin 2) R) : Prop :=
  ∀ i j, q ^ (cH i) * q ^ (cM j) * B i j = B i j

/-- **Selection rule:** an invariant pairing is nonzero only where the charges cancel. -/
theorem charge_cancel (q : R) (hq0 : q ≠ 0) (hq : ∀ n : ℤ, q ^ n = 1 → n = 0)
    (cH cM : Fin 2 → ℤ) (B : Matrix (Fin 2) (Fin 2) R) (hB : Invariant q cH cM B)
    (i j : Fin 2) (hne : B i j ≠ 0) : cH i + cM j = 0 := by
  apply hq
  have h := hB i j
  rw [← zpow_add₀ hq0] at h
  have : (q ^ (cH i + cM j) - 1) * B i j = 0 := by linear_combination h
  rcases mul_eq_zero.mp this with h' | h'
  · exact sub_eq_zero.mp h'
  · exact absurd h' hne

/-- **The neutral vev pairs only with neutral strand slots.** -/
theorem pairing_selection (q : R) (hq0 : q ≠ 0) (hq : ∀ n : ℤ, q ^ n = 1 → n = 0)
    (cH cM : Fin 2 → ℤ) (B : Matrix (Fin 2) (Fin 2) R) (hB : Invariant q cH cM B)
    (v : Fin 2) (hv : cH v = 0) (j : Fin 2) (hj : cM j ≠ 0) : B v j = 0 := by
  by_contra hne
  have := charge_cancel q hq0 hq cH cM B hB v j hne
  rw [hv, zero_add] at this
  exact hj this

/-- `3Q` on a quark strand: `u ↦ 2`, `d ↦ −1`. -/
def cQuark : Fin 2 → ℤ := ![2, -1]

/-- `3Q` on a lepton strand under premise L: `ν ↦ 0` (slot `u`), `e⁻ ↦ −3` (slot `d`). -/
def cLepton : Fin 2 → ℤ := ![0, -3]

/-- **The vacuum pairing with a quark strand vanishes identically.** -/
theorem pairing_quark_zero (q : R) (hq0 : q ≠ 0) (hq : ∀ n : ℤ, q ^ n = 1 → n = 0)
    (cH : Fin 2 → ℤ) (B : Matrix (Fin 2) (Fin 2) R) (hB : Invariant q cH cQuark B)
    (v : Fin 2) (hv : cH v = 0) : ∀ j, B v j = 0 := by
  intro j
  apply pairing_selection q hq0 hq cH cQuark B hB v hv j
  fin_cases j <;> decide

/-- **On a lepton strand the vacuum pairing vanishes on `e⁻`.** -/
theorem pairing_lepton (q : R) (hq0 : q ≠ 0) (hq : ∀ n : ℤ, q ^ n = 1 → n = 0)
    (cH : Fin 2 → ℤ) (B : Matrix (Fin 2) (Fin 2) R) (hB : Invariant q cH cLepton B)
    (v : Fin 2) (hv : cH v = 0) : B v 1 = 0 :=
  pairing_selection q hq0 hq cH cLepton B hB v hv 1 (by decide)

/-- Flavour → slot. -/
def slot : Fl → Fin 2
  | .u => 0
  | .d => 1

/-- Induced per-strand energy of the vacuum pairing: `χ(t, f) = B_t(vev, f)²`. -/
def pairEnergy (Bq Bl : Matrix (Fin 2) (Fin 2) R) (v : Fin 2) : Ty → Fl → R
  | .quark, f => Bq v (slot f) ^ 2
  | .lepton, f => Bl v (slot f) ^ 2

/-- **Split of the charge-conserving vacuum pairing: `B_ℓ(vev, ν)²`.** Three couplings are
forced to 0; the `ν` coupling is free. -/
theorem split_neutral (q : R) (hq0 : q ≠ 0) (hq : ∀ n : ℤ, q ^ n = 1 → n = 0)
    (cH : Fin 2 → ℤ) (Bq Bl : Matrix (Fin 2) (Fin 2) R)
    (hBq : Invariant q cH cQuark Bq) (hBl : Invariant q cH cLepton Bl)
    (v : Fin 2) (hv : cH v = 0) :
    split (pairEnergy Bq Bl v) = Bl v 0 ^ 2 := by
  have hq' := pairing_quark_zero q hq0 hq cH Bq hBq v hv
  have hl := pairing_lepton q hq0 hq cH Bl hBl v hv
  rw [split_eq_interaction]
  simp [pairEnergy, slot, hq', hl]

/-- The `ν` coupling is genuinely free: for every `y` there is an invariant lepton pairing with
`B(vev, ν) = y` (vev in a charge-0 Higgs slot). -/
theorem nu_coupling_free (q y : R) (cH : Fin 2 → ℤ) (v : Fin 2) (hv : cH v = 0) :
    ∃ B : Matrix (Fin 2) (Fin 2) R, Invariant q cH cLepton B ∧ B v 0 = y := by
  refine ⟨fun i j => if i = v ∧ j = 0 then y else 0, ?_, by simp⟩
  intro i j
  by_cases h : i = v ∧ j = 0
  · obtain ⟨rfl, rfl⟩ := h
    simp [hv, cLepton]
  · simp [h]

end QOU.QuarkState.YukawaVacuumPairing
