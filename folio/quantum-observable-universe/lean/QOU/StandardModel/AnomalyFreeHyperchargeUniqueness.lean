/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under CC BY 4.0 as described in the repository LICENSE.
-/
import Mathlib.Tactic
import QOU.StandardModel.HopfFramingAndHirzebruchDefect

/-!
# Anomaly freedom forces the hypercharge ratios on one generation

Bean `qou-qvpl` (T2, Open Check A), with `qou-txc1` (the `3/8` trace ratio).

## Setting

One generation of left-handed Weyl multiplets of `SU(3) × SU(2)`, with the representation
content and **five independent abelian charges** `(yQ, yu, yd, yL, ye)` in a field `K`:

| multiplet | `SU(3) × SU(2)` | states | charge |
|---|---|---|---|
| `Q`   | `(3, 2)`  | 6 | `yQ` |
| `u^c` | `(3̄, 1)`  | 3 | `yu` |
| `d^c` | `(3̄, 1)`  | 3 | `yd` |
| `L`   | `(1, 2)`  | 2 | `yL` |
| `e^c` | `(1, 1)`  | 1 | `ye` |

Nothing ties the five charges together a priori: no `SU(5)` embedding, no `Λ²`, no
Gell-Mann–Nishijima formula.  The four perturbative anomaly conditions are polynomial
identities in the charges (index of the fundamental of `SU(N)` normalised to `1`; overall
positive factors dropped):

* `[SU(3)]² U(1)`: `2 yQ + yu + yd = 0`,
* `[SU(2)]² U(1)`: `3 yQ + yL = 0`,
* `[grav]² U(1)`: `6 yQ + 3 yu + 3 yd + 2 yL + ye = 0`,
* `U(1)³`: `6 yQ³ + 3 yu³ + 3 yd³ + 2 yL³ + ye³ = 0`.

## What is proved here

* `anomalyFree_iff` — over any field with `18 ≠ 0`, the four conditions hold **iff** either
  - (chiral) `yL = -3 yQ`, `ye = 6 yQ`, and `{yu, yd} = {-4 yQ, 2 yQ}`, or
  - (vector-like) `yQ = yL = ye = 0` and `yd = -yu`.
  The cubic condition factors as `18 · yQ · (yu + 4 yQ) · (yu - 2 yQ) = 0` once the three
  linear ones are imposed (`cubic_factor`).
* `chiral_is_su5_pattern` — every chiral solution is the `5̄ ⊕ Λ²5` pattern of
  `QOU.StandardModel.BringPrymRiemannRochGenerations` (`L = y₂`, `d^c = y₃`,
  `Q = -y₂ - y₃`, `u^c = -2y₃`, `e^c = -2y₂`, with `2y₂ + 3y₃ = 0`), after naming the
  `3̄` singlet of charge `-4 yQ` as `u^c`.  So the `SU(5)` assignment, which
  `NeutralLeptonFixesCharges` takes as input 1, is **forced** at the level of charges by
  anomaly freedom on the `SU(3) × SU(2)` content.
* `trace_T3_sq`, `trace_Y_sq`, `trace_T3_Y` and `weakTraceRatio_eq` — on the 15 states,
  `Tr T₃² = 2`, `Tr Y² = 120 yQ²`, `Tr T₃Y = 0`, so
  `Tr T₃² / Tr (T₃ + Y)² = 1 / (1 + 60 yQ²)` for every chiral solution.
* `neutral_lepton_iff` and `neutral_lepton_iff_three_eighths` — the doublet `L` has a member of
  zero electric charge `T₃ + Y` iff `yQ = ± 1/6`, iff the trace ratio equals `3/8`.
* `charges_at_one_sixth` — at `yQ = 1/6` the 15 electric charges are those of
  `u, d, u^c, d^c, ν, e, e^c`: `2/3, -1/3, -2/3, 1/3, 0, -1, 1`.

## Honest scope (what this does and does not settle for Open Check A)

Inputs, all structural, none measured:
1. **The representation content** of the table above.  Not derived here.
2. **Anomaly freedom** of the abelian factor, as a consistency condition.  Its categorical
   origin in QOU (a ribbon/modular anomaly) is not formalised here.
3. **One neutral lepton** (only for the scale), the same datum as `nu_framing_is_zero`.

What it settles: given 1–2, the hypercharge is **not** a free second datum that must be
selected by `Q_twist = Q` (the circularity recorded in `TwistBatteryVacuity`).  It is unique
up to one scale and the `u ↔ d` label, and 3 fixes the scale.  The strand-twist candidate
`Y_t = 2(T/3 - I₃)` agrees with the forced charges, so the twist route and the anomaly route
meet.  What remains open for Check A is input 1 from the categorical braid words, and input 2
from the QOU axioms.

Base: any field with `18 ≠ 0` (so `ℚ`, `ℝ`, or any characteristic other than `2, 3`).
Reference: the classical uniqueness of Standard Model hypercharge from anomaly cancellation
(Geng–Marshak 1989; Minahan–Ramond–Warner 1990).
-/

namespace QOU.StandardModel.AnomalyFreeHypercharge

variable {K : Type*} [Field K]

/-- Five independent abelian charges on one generation of `SU(3) × SU(2)` Weyl multiplets. -/
structure Charges (K : Type*) where
  yQ : K
  yu : K
  yd : K
  yL : K
  ye : K

/-- `[SU(3)]² U(1)` anomaly (up to a positive factor). -/
def anomSU3 (c : Charges K) : K := 2 * c.yQ + c.yu + c.yd

/-- `[SU(2)]² U(1)` anomaly (up to a positive factor). -/
def anomSU2 (c : Charges K) : K := 3 * c.yQ + c.yL

/-- Mixed gravitational anomaly `Tr Y` over the 15 states. -/
def anomGrav (c : Charges K) : K := 6 * c.yQ + 3 * c.yu + 3 * c.yd + 2 * c.yL + c.ye

/-- Cubic anomaly `Tr Y³` over the 15 states. -/
def anomCubic (c : Charges K) : K :=
  6 * c.yQ ^ 3 + 3 * c.yu ^ 3 + 3 * c.yd ^ 3 + 2 * c.yL ^ 3 + c.ye ^ 3

/-- All four perturbative anomalies vanish. -/
def AnomalyFree (c : Charges K) : Prop :=
  anomSU3 c = 0 ∧ anomSU2 c = 0 ∧ anomGrav c = 0 ∧ anomCubic c = 0

/-- The chiral solution family: `L = -3Q`, `e^c = 6Q`, and `{u^c, d^c} = {-4Q, 2Q}`. -/
def IsChiralSolution (c : Charges K) : Prop :=
  c.yL = -3 * c.yQ ∧ c.ye = 6 * c.yQ ∧
    ((c.yu = -4 * c.yQ ∧ c.yd = 2 * c.yQ) ∨ (c.yu = 2 * c.yQ ∧ c.yd = -4 * c.yQ))

/-- The vector-like solution family: `Q = L = e^c = 0` and `d^c = -u^c`. -/
def IsVectorLikeSolution (c : Charges K) : Prop :=
  c.yQ = 0 ∧ c.yL = 0 ∧ c.ye = 0 ∧ c.yd = -c.yu

/-- With the three linear conditions imposed, the cubic anomaly factors. -/
theorem cubic_factor (c : Charges K) (h3 : anomSU3 c = 0) (h2 : anomSU2 c = 0)
    (hg : anomGrav c = 0) :
    anomCubic c = -18 * c.yQ * (c.yu + 4 * c.yQ) * (c.yu - 2 * c.yQ) := by
  unfold anomSU3 at h3
  unfold anomSU2 at h2
  unfold anomGrav at hg
  have hL : c.yL = -3 * c.yQ := by linear_combination h2
  have hd : c.yd = -2 * c.yQ - c.yu := by linear_combination h3
  have he : c.ye = 6 * c.yQ := by linear_combination hg - 3 * h3 - 2 * h2
  unfold anomCubic
  rw [hL, hd, he]
  ring

/-- **Anomaly freedom forces the hypercharge ratios.**  Over a field with `18 ≠ 0`, the four
perturbative anomaly conditions hold iff the charges are a chiral solution
`(yQ, yu, yd, yL, ye) ∈ yQ · {(1, -4, 2, -3, 6), (1, 2, -4, -3, 6)}` or vector-like. -/
theorem anomalyFree_iff (h18 : (18 : K) ≠ 0) (c : Charges K) :
    AnomalyFree c ↔ IsChiralSolution c ∨ IsVectorLikeSolution c := by
  constructor
  · rintro ⟨h3, h2, hg, hc⟩
    have hfac := cubic_factor c h3 h2 hg
    rw [hc] at hfac
    unfold anomSU3 at h3
    unfold anomSU2 at h2
    unfold anomGrav at hg
    have hL : c.yL = -3 * c.yQ := by linear_combination h2
    have hd : c.yd = -2 * c.yQ - c.yu := by linear_combination h3
    have he : c.ye = 6 * c.yQ := by linear_combination hg - 3 * h3 - 2 * h2
    have hprod : c.yQ * (c.yu + 4 * c.yQ) * (c.yu - 2 * c.yQ) = 0 := by
      have h' : (-18 : K) * (c.yQ * (c.yu + 4 * c.yQ) * (c.yu - 2 * c.yQ)) = 0 := by
        linear_combination -hfac
      rcases mul_eq_zero.mp h' with h | h
      · exact absurd (neg_eq_zero.mp h) h18
      · exact h
    rcases mul_eq_zero.mp hprod with h | h
    · rcases mul_eq_zero.mp h with hQ | hu
      · right
        refine ⟨hQ, ?_, ?_, ?_⟩
        · rw [hL, hQ]; ring
        · rw [he, hQ]; ring
        · rw [hd, hQ]; ring
      · left
        refine ⟨hL, he, Or.inl ⟨?_, ?_⟩⟩
        · linear_combination hu
        · linear_combination hd - hu
    · left
      refine ⟨hL, he, Or.inr ⟨?_, ?_⟩⟩
      · linear_combination h
      · linear_combination hd - h
  · rintro (⟨hL, he, ⟨hu, hd⟩ | ⟨hu, hd⟩⟩ | ⟨hQ, hL, he, hd⟩)
    · refine ⟨?_, ?_, ?_, ?_⟩ <;>
        simp only [anomSU3, anomSU2, anomGrav, anomCubic, hL, he, hu, hd] <;> ring
    · refine ⟨?_, ?_, ?_, ?_⟩ <;>
        simp only [anomSU3, anomSU2, anomGrav, anomCubic, hL, he, hu, hd] <;> ring
    · refine ⟨?_, ?_, ?_, ?_⟩ <;>
        simp only [anomSU3, anomSU2, anomGrav, anomCubic, hQ, hL, he, hd] <;> ring

/-- The non-degenerate case: if `yQ ≠ 0` the solution is chiral. -/
theorem anomalyFree_chiral_of_ne_zero (h18 : (18 : K) ≠ 0) (c : Charges K)
    (hc : AnomalyFree c) (hQ : c.yQ ≠ 0) : IsChiralSolution c := by
  rcases (anomalyFree_iff h18 c).mp hc with h | h
  · exact h
  · exact absurd h.1 hQ

/-- The `5̄ ⊕ Λ²5` charge pattern of `BringPrymRiemannRochGenerations`, with `u^c` the `3̄`
singlet of the `Λ²` part. -/
def IsSU5Pattern (c : Charges K) : Prop :=
  ∃ y2 y3 : K, 2 * y2 + 3 * y3 = 0 ∧ c.yL = y2 ∧ c.yd = y3 ∧ c.yQ = -y2 - y3 ∧
    c.yu = -2 * y3 ∧ c.ye = -2 * y2

/-- **The `SU(5)` pattern is forced.**  A chiral solution with `u^c` labelled as the singlet of
charge `-4 yQ` is exactly the `5̄ ⊕ Λ²5` pattern with `y₂ = -3 yQ`, `y₃ = 2 yQ`. -/
theorem chiral_is_su5_pattern (c : Charges K) (hL : c.yL = -3 * c.yQ) (he : c.ye = 6 * c.yQ)
    (hu : c.yu = -4 * c.yQ) (hd : c.yd = 2 * c.yQ) : IsSU5Pattern c :=
  ⟨-3 * c.yQ, 2 * c.yQ, by ring, hL, hd, by ring, by rw [hu]; ring, by rw [he]; ring⟩

/-- Conversely every `5̄ ⊕ Λ²5` pattern is anomaly-free (the `N_q = N_ℓ = 1` case of
`exterior_su5_anomaly_identities`, re-proved here on independent charges). -/
theorem su5Pattern_anomalyFree (c : Charges K) (h : IsSU5Pattern c) : AnomalyFree c := by
  obtain ⟨y2, y3, htr, hL, hd, hQ, hu, he⟩ := h
  refine ⟨?_, ?_, ?_, ?_⟩
  · simp only [anomSU3, hQ, hu, hd]; linear_combination -htr
  · simp only [anomSU2, hQ, hL]; linear_combination -htr
  · simp only [anomGrav, hQ, hu, hd, hL, he]; linear_combination -3 * htr
  · simp only [anomCubic, hQ, hu, hd, hL, he]
    linear_combination (-6 * y2 ^ 2 - 9 * y3 ^ 2) * htr

/-! ## The 15 states, the weak trace ratio, and the neutral lepton -/

/-- The 15 left-handed Weyl states of one generation, by multiplet and `SU(2)` index. -/
inductive State : Type
  | Q (colour : Fin 3) (iso : Fin 2)
  | u (colour : Fin 3)
  | d (colour : Fin 3)
  | L (iso : Fin 2)
  | e
  deriving DecidableEq, Fintype

/-- Twice the weak isospin `2 T₃`: `+1` on the upper and `-1` on the lower doublet member,
`0` on singlets. -/
def twoT3 : State → K
  | .Q _ 0 => 1
  | .Q _ 1 => -1
  | .L 0 => 1
  | .L 1 => -1
  | _ => 0

/-- The abelian charge of a state. -/
def hyp (c : Charges K) : State → K
  | .Q _ _ => c.yQ
  | .u _ => c.yu
  | .d _ => c.yd
  | .L _ => c.yL
  | .e => c.ye

/-- Electric charge `T₃ + Y`. -/
def charge (c : Charges K) (s : State) : K := twoT3 s / 2 + hyp c s

/-- Sum over the 15 states, unfolded multiplet by multiplet. -/
theorem sum_state (f : State → K) :
    ∑ s : State, f s =
      (∑ a : Fin 3, ∑ i : Fin 2, f (.Q a i)) + (∑ a : Fin 3, f (.u a)) +
        (∑ a : Fin 3, f (.d a)) + (∑ i : Fin 2, f (.L i)) + f .e := by
  let e : State ≃ (Fin 3 × Fin 2) ⊕ Fin 3 ⊕ Fin 3 ⊕ Fin 2 ⊕ Unit :=
    { toFun := fun
        | .Q a i => .inl (a, i)
        | .u a => .inr (.inl a)
        | .d a => .inr (.inr (.inl a))
        | .L i => .inr (.inr (.inr (.inl i)))
        | .e => .inr (.inr (.inr (.inr ())))
      invFun := fun
        | .inl (a, i) => .Q a i
        | .inr (.inl a) => .u a
        | .inr (.inr (.inl a)) => .d a
        | .inr (.inr (.inr (.inl i))) => .L i
        | .inr (.inr (.inr (.inr ()))) => .e
      left_inv := by intro s; cases s <;> rfl
      right_inv := by
        intro x
        rcases x with ⟨a, i⟩ | a | a | i | ⟨⟩ <;> rfl }
  rw [← e.symm.sum_comp]
  simp [Fintype.sum_sum_type, Fintype.sum_prod_type, e, add_assoc]

/-- `Tr T₃² = 2` on one generation. -/
theorem trace_T3_sq (h2 : (2 : K) ≠ 0) :
    ∑ s : State, (twoT3 s / 2 : K) ^ 2 = 2 := by
  rw [sum_state]
  simp [Fin.sum_univ_succ, twoT3]
  field_simp
  norm_num

/-- `Tr Y² = 6 yQ² + 3 yu² + 3 yd² + 2 yL² + ye²` on one generation. -/
theorem trace_Y_sq_general (c : Charges K) :
    ∑ s : State, hyp c s ^ 2 =
      6 * c.yQ ^ 2 + 3 * c.yu ^ 2 + 3 * c.yd ^ 2 + 2 * c.yL ^ 2 + c.ye ^ 2 := by
  rw [sum_state]
  simp [hyp]
  ring

/-- `Tr T₃ Y = 0`: each doublet has `T₃` summing to zero. -/
theorem trace_T3_Y (c : Charges K) :
    ∑ s : State, (twoT3 s / 2) * hyp c s = 0 := by
  rw [sum_state]
  simp [Fin.sum_univ_succ, twoT3, hyp]
  ring

/-- On a chiral solution, `Tr Y² = 120 yQ²`. -/
theorem trace_Y_sq (c : Charges K) (hc : IsChiralSolution c) :
    ∑ s : State, hyp c s ^ 2 = 120 * c.yQ ^ 2 := by
  rw [trace_Y_sq_general]
  obtain ⟨hL, he, ⟨hu, hd⟩ | ⟨hu, hd⟩⟩ := hc <;> rw [hL, he, hu, hd] <;> ring

/-- `Tr Q² = Tr T₃² + Tr Y²` (the cross term vanishes). -/
theorem trace_charge_sq (h2 : (2 : K) ≠ 0) (c : Charges K) :
    ∑ s : State, charge c s ^ 2 = 2 + ∑ s : State, hyp c s ^ 2 := by
  have hsplit : ∀ s : State, charge c s ^ 2 =
      (twoT3 s / 2 : K) ^ 2 + 2 * ((twoT3 s / 2) * hyp c s) + hyp c s ^ 2 := by
    intro s; unfold charge; ring
  simp only [hsplit, Finset.sum_add_distrib, ← Finset.mul_sum, trace_T3_sq h2, trace_T3_Y]
  ring

/-- **The weak trace ratio on a chiral solution:** `Tr T₃² / Tr Q² = 1 / (1 + 60 yQ²)`. -/
theorem weakTraceRatio_eq (h2 : (2 : K) ≠ 0) (c : Charges K) (hc : IsChiralSolution c)
    (hden : 1 + 60 * c.yQ ^ 2 ≠ 0) :
    (∑ s : State, (twoT3 s / 2 : K) ^ 2) / (∑ s : State, charge c s ^ 2) =
      1 / (1 + 60 * c.yQ ^ 2) := by
  rw [trace_T3_sq h2, trace_charge_sq h2, trace_Y_sq c hc]
  have h2' : (2 : K) + 120 * c.yQ ^ 2 = 2 * (1 + 60 * c.yQ ^ 2) := by ring
  rw [h2', div_eq_div_iff (mul_ne_zero h2 hden) hden]
  ring

/-- The doublet `L` has a member of zero electric charge. -/
def HasNeutralLepton (c : Charges K) : Prop := ∃ i : Fin 2, charge c (.L i) = 0

/-- **One neutral lepton fixes the scale:** on a chiral solution, `L` has a neutral member iff
`yQ = 1/6` or `yQ = -1/6`. -/
theorem neutral_lepton_iff [CharZero K] (c : Charges K) (hc : IsChiralSolution c) :
    HasNeutralLepton c ↔ c.yQ = 1 / 6 ∨ c.yQ = -1 / 6 := by
  obtain ⟨hL, -, -⟩ := hc
  unfold HasNeutralLepton charge
  constructor
  · rintro ⟨i, hi⟩
    fin_cases i <;> simp only [twoT3, hyp, hL] at hi
    · left; linear_combination (-1 / 3 : K) * hi
    · right; linear_combination (-1 / 3 : K) * hi
  · rintro (h | h)
    · refine ⟨0, ?_⟩; simp only [twoT3, hyp, hL, h]; norm_num
    · refine ⟨1, ?_⟩; simp only [twoT3, hyp, hL, h]; norm_num

/-- **Neutral lepton iff `3/8`:** on a chiral solution (over a field of characteristic zero),
`L` has a neutral member iff the weak trace ratio equals `3/8`. -/
theorem neutral_lepton_iff_three_eighths [CharZero K] (c : Charges K) (hc : IsChiralSolution c)
    (hden : 1 + 60 * c.yQ ^ 2 ≠ 0) :
    HasNeutralLepton c ↔
      (∑ s : State, (twoT3 s / 2 : K) ^ 2) / (∑ s : State, charge c s ^ 2) = 3 / 8 := by
  rw [neutral_lepton_iff c hc, weakTraceRatio_eq two_ne_zero c hc hden,
    div_eq_div_iff hden (by norm_num)]
  constructor
  · rintro (h | h) <;> rw [h] <;> ring
  · intro h
    have hsq : (c.yQ - 1 / 6) * (c.yQ + 1 / 6) = 0 := by linear_combination -h / 180
    rcases mul_eq_zero.mp hsq with h' | h'
    · left; linear_combination h'
    · right; linear_combination h'

/-- **The forced first-generation charges.**  At `yQ = 1/6` with `u^c` the `-4 yQ` singlet, the
electric charges are `u_L = 2/3`, `d_L = -1/3`, `u^c = -2/3`, `d^c = 1/3`, `ν = 0`, `e = -1`,
`e^c = 1`. -/
theorem charges_at_one_sixth [CharZero K] (c : Charges K) (hQ : c.yQ = 1 / 6)
    (hL : c.yL = -3 * c.yQ) (he : c.ye = 6 * c.yQ) (hu : c.yu = -4 * c.yQ)
    (hd : c.yd = 2 * c.yQ) (a : Fin 3) :
    charge c (.Q a 0) = 2 / 3 ∧ charge c (.Q a 1) = -1 / 3 ∧ charge c (.u a) = -2 / 3 ∧
      charge c (.d a) = 1 / 3 ∧ charge c (.L 0) = 0 ∧ charge c (.L 1) = -1 ∧
      charge c .e = 1 := by
  simp only [charge, twoT3, hyp, hL, he, hu, hd, hQ]
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> norm_num

/-- **Summary for `qou-qvpl` Open Check A.**  On the `SU(3) × SU(2)` content of one generation,
any anomaly-free abelian charge with a neutral lepton is, up to the `u ↔ d` label of the two
`3̄` singlets, the Standard Model hypercharge at `yQ = ± 1/6`, and its weak trace ratio is
`3/8`.  No measured number enters. -/
theorem anomalyFree_neutral_forces_hypercharge [CharZero K] (c : Charges K)
    (hc : AnomalyFree c) (hn : HasNeutralLepton c) :
    IsChiralSolution c ∧ (c.yQ = 1 / 6 ∨ c.yQ = -1 / 6) ∧
      (∑ s : State, (twoT3 s / 2 : K) ^ 2) / (∑ s : State, charge c s ^ 2) = 3 / 8 := by
  have h18 : (18 : K) ≠ 0 := by norm_num
  have hch : IsChiralSolution c := by
    rcases (anomalyFree_iff h18 c).mp hc with h | ⟨hQ, hL, -, -⟩
    · exact h
    · exfalso
      obtain ⟨i, hi⟩ := hn
      fin_cases i <;> simp [charge, twoT3, hyp, hL] at hi
  have hscale := (neutral_lepton_iff c hch).mp hn
  have hden : 1 + 60 * c.yQ ^ 2 ≠ 0 := by
    rcases hscale with h | h <;> rw [h] <;> norm_num
  exact ⟨hch, hscale, (neutral_lepton_iff_three_eighths c hch hden).mp hn⟩

/-! ## The existing Open-Check-A carrier is vacuous

`CategoricalRibbonHyperchargeDerivationHypothesis` (in `HopfFramingAndHirzebruchDefect`) is
documented as a zero-instance Rule-13a carrier for Open Check A.  Its only field,
`∀ T twoI3, ∃ Y3, Y3 = 2T - 3·twoI3`, is provable by `rfl`, so the class is inhabited and
records no open content.  This is a proof term, not an `instance`; it does not add a global
instance, it only shows that one could be written.  The open content of Check A is the two
inputs listed in the module docstring above (representation content and anomaly freedom from
the QOU axioms), which the carrier does not mention. -/
theorem categoricalRibbonHyperchargeDerivationHypothesis_trivial :
    QOU.StandardModel.HopfFramingAndHirzebruchDefect.CategoricalRibbonHyperchargeDerivationHypothesis :=
  ⟨fun _ _ => ⟨_, rfl⟩⟩

end QOU.StandardModel.AnomalyFreeHypercharge
