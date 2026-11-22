import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith

/-!
# Light nuclei on the ruled γγ bond: the chain unbinds at every `q > 1`

Issue #9039. Owner ruling 2026-11-22 (reading A, right-hand closure): a γγ bond
`V³ = (σ_{3j−1}σ_{3j}⁻¹)³` enters the newer nucleon. By the chain law
`towerTr_ggChain` (`mass-endomorphism/markov-trace-hecke-functional.lean`, proved)

  `tr W_chain = tr N₀ · ∏_{j ≥ 1} b(N_j)`,   `tr W_free = tr N₀ · ∏_{j ≥ 1} tr N_j`,

with `b(N) = tr(V³ · N↑¹)` the bond factor of the nucleon a bond enters.

What this file proves (no numerical value enters):

* `chain_ratio` — `tr W_chain / tr W_free = ∏ μ_j`, `μ_j = b(N_j)/tr N_j`: the ratio depends
  only on which nucleons the bonds enter, not on the first nucleon or the order;
* `chain_gt_free` — if every block trace is positive and every bond factor exceeds its
  block trace, then `tr W_chain > tr W_free` for any nonempty tail, so
  `B_diff = E₀(tr W_free − tr W_chain) < 0` for every `E₀ > 0`;
* `mu_p_sub_one_pos`, `mu_n_sub_one_pos` — the closed forms of `μ_p − 1`, `μ_n − 1` for the
  production proton and neutron blocks are positive at every `q > 1` in any linearly ordered field. Each is
  `(q² − 1)^k` (`k = 4` for p, `5` for n) times a ratio of polynomials in `y = q² − 1` with
  nonnegative coefficients and positive constant term.
* `trace_closed_forms_positive` — the closed forms of `tr p`, `tr n` are positive for `q > 1`.

**What is not proved here.** That these rational functions *are* the Ocneanu traces at
`z_D = q³/(q² + 1)` of the production blocks is an exact ℚ(q) computation
(`computations/probes/light_nuclei_a2_a3/light_nuclei_a2_a3_probe.py`, sympy over
`QQ(q)`), not a Lean theorem. Combined with it: under the ruling, the γγ chain of
production blocks unbinds for every A ≥ 2, every nucleon order and every `q > 1`.
-/

namespace QOU.Mass.LightNucleiGGChainSign

open List

section Chain

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Products over a list of pairs `(t, b)`: block traces and bond factors. -/
def trProd (l : List (K × K)) : K := (l.map Prod.fst).prod
def bondProd (l : List (K × K)) : K := (l.map Prod.snd).prod
def muProd (l : List (K × K)) : K := (l.map (fun p => p.2 / p.1)).prod

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem bondProd_eq (l : List (K × K)) (hl : ∀ p ∈ l, p.1 ≠ 0) :
    bondProd l = trProd l * muProd l := by
  induction l with
  | nil => simp [bondProd, trProd, muProd]
  | cons p l ih =>
    have hp : p.1 ≠ 0 := hl p (by simp)
    have hr : ∀ r ∈ l, r.1 ≠ 0 := fun r hr => hl r (List.mem_cons_of_mem _ hr)
    simp only [bondProd, trProd, muProd, List.map_cons, List.prod_cons] at ih ⊢
    rw [ih hr]
    field_simp

/-- **Ratio law.** `tr W_chain / tr W_free = ∏ μ_j`; the first nucleon cancels. -/
theorem chain_ratio (t₀ : K) (l : List (K × K)) (h₀ : t₀ ≠ 0) (hl : ∀ p ∈ l, p.1 ≠ 0) :
    (t₀ * bondProd l) / (t₀ * trProd l) = muProd l := by
  have htr : trProd l ≠ 0 := by
    unfold trProd
    induction l with
    | nil => simp
    | cons p l ih =>
      simp only [List.map_cons, List.prod_cons]
      exact mul_ne_zero (hl p (by simp)) (ih fun r hr => hl r (List.mem_cons_of_mem _ hr))
  rw [bondProd_eq l hl]
  field_simp

theorem trProd_pos (l : List (K × K)) (hl : ∀ p ∈ l, 0 < p.1) : 0 < trProd l := by
  induction l with
  | nil => simp [trProd]
  | cons p l ih =>
    simp only [trProd, List.map_cons, List.prod_cons] at ih ⊢
    exact mul_pos (hl p (by simp)) (ih fun r hr => hl r (List.mem_cons_of_mem _ hr))

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem trProd_cons (p : K × K) (l : List (K × K)) : trProd (p :: l) = p.1 * trProd l := by
  simp [trProd]

omit [LinearOrder K] [IsStrictOrderedRing K] in
theorem bondProd_cons (p : K × K) (l : List (K × K)) : bondProd (p :: l) = p.2 * bondProd l := by
  simp [bondProd]

theorem trProd_lt_bondProd (p : K × K) (l : List (K × K))
    (hl : ∀ r ∈ p :: l, 0 < r.1 ∧ r.1 < r.2) : trProd (p :: l) < bondProd (p :: l) := by
  induction l generalizing p with
  | nil => simpa [trProd, bondProd] using (hl p (by simp)).2
  | cons r l ih =>
    have hp := hl p (by simp)
    have hrest : ∀ s ∈ r :: l, 0 < s.1 ∧ s.1 < s.2 := fun s hs => hl s (List.mem_cons_of_mem _ hs)
    have hlt := ih r hrest
    have hT : 0 < trProd (r :: l) := trProd_pos _ fun s hs => (hrest s hs).1
    rw [trProd_cons p, bondProd_cons p]
    calc p.1 * trProd (r :: l) < p.2 * trProd (r :: l) := mul_lt_mul_of_pos_right hp.2 hT
      _ < p.2 * bondProd (r :: l) := mul_lt_mul_of_pos_left hlt (lt_trans hp.1 hp.2)

/-- **Every chain with at least one bond is heavier than its free word** when each bond
    factor exceeds its block trace. -/
theorem chain_gt_free (t₀ : K) (l : List (K × K)) (hne : l ≠ [])
    (h₀ : 0 < t₀) (hl : ∀ p ∈ l, 0 < p.1 ∧ p.1 < p.2) :
    t₀ * trProd l < t₀ * bondProd l := by
  apply mul_lt_mul_of_pos_left _ h₀
  cases l with
  | nil => exact absurd rfl hne
  | cons p l => exact trProd_lt_bondProd p l hl

/-- `B_diff = E₀ (tr W_free − tr W_chain) < 0`: the chain unbinds. -/
theorem chain_unbinds (E₀ t₀ : K) (l : List (K × K)) (hne : l ≠ []) (hE : 0 < E₀)
    (h₀ : 0 < t₀) (hl : ∀ p ∈ l, 0 < p.1 ∧ p.1 < p.2) :
    E₀ * (t₀ * trProd l - t₀ * bondProd l) < 0 :=
  mul_neg_of_pos_of_neg hE (sub_neg.mpr (chain_gt_free t₀ l hne h₀ hl))

end Chain

/-! ## The closed forms are positive for `q > 1` -/

section ClosedForms

variable {K : Type*} [Field K]

/-- Denominator polynomial of `tr p` (in `q`). -/
def Dp (q : K) : K := q^18 - 3*q^16 + 7*q^14 - 8*q^12 + 10*q^10 - 9*q^8 + 10*q^6 - 6*q^4 + 3*q^2 - 1
/-- Numerator polynomial of `μ_p − 1` after the factor `(q² − 1)⁴ (q⁴ + q² + 1)`. -/
def Pp (q : K) : K := q^10 - q^8 + 4*q^6 - 4*q^4 + 2*q^2 - 1
/-- Denominator polynomial of `tr n`. -/
def Dn (q : K) : K := q^14 - 3*q^12 + 4*q^10 - 4*q^8 + 5*q^6 - 4*q^4 + 3*q^2 - 1

theorem Dp_y (q : K) : Dp q = let y := q^2 - 1;
    4 + 21*y + 49*y^2 + 75*y^3 + 82*y^4 + 67*y^5 + 41*y^6 + 19*y^7 + 6*y^8 + y^9 := by
  simp only [Dp]; ring

theorem Pp_y (q : K) : Pp q = let y := q^2 - 1;
    1 + 7*y + 12*y^2 + 10*y^3 + 4*y^4 + y^5 := by
  simp only [Pp]; ring

theorem Dn_y (q : K) : Dn q = let y := q^2 - 1;
    1 + 3*y + 3*y^2 + 4*y^3 + 6*y^4 + 7*y^5 + 4*y^6 + y^7 := by
  simp only [Dn]; ring

variable [LinearOrder K] [IsStrictOrderedRing K] {q : K} (hq : 1 < q)
include hq

theorem y_pos : 0 < q^2 - 1 := by nlinarith

theorem Dp_pos : 0 < Dp q := by
  rw [Dp_y]; have := y_pos hq; positivity
theorem Pp_pos : 0 < Pp q := by
  rw [Pp_y]; have := y_pos hq; positivity
theorem Dn_pos : 0 < Dn q := by
  rw [Dn_y]; have := y_pos hq; positivity

/-- `tr p = (q⁴+1) Dp / (4 q⁹ (q²+1)²)` and `tr n = (q⁴+1) Dn / (4 q⁹)` are positive. -/
theorem trace_closed_forms_positive :
    0 < (q^4 + 1) * Dp q / (4 * q^9 * (q^2 + 1)^2) ∧ 0 < (q^4 + 1) * Dn q / (4 * q^9) := by
  have hq0 : 0 < q := by linarith
  have := Dp_pos hq; have := Dn_pos hq
  constructor <;> positivity

/-- `μ_p − 1 = (q²−1)⁴ (q⁴+q²+1) Pp / (q² (q²+1) Dp) > 0` for `q > 1`. -/
theorem mu_p_sub_one_pos :
    0 < (q^2 - 1)^4 * (q^4 + q^2 + 1) * Pp q / (q^2 * (q^2 + 1) * Dp q) := by
  have := y_pos hq; have := Pp_pos hq; have := Dp_pos hq
  positivity

/-- `μ_n − 1 = (q²−1)⁵ (q⁴+q²+1)(q⁴−q²+1) / (q² (q²+1) Dn) > 0` for `q > 1`. -/
theorem mu_n_sub_one_pos :
    0 < (q^2 - 1)^5 * (q^4 + q^2 + 1) * (q^4 - q^2 + 1) / (q^2 * (q^2 + 1) * Dn q) := by
  have hy := y_pos hq; have := Dn_pos hq
  have h4 : 0 < q^4 - q^2 + 1 := by nlinarith [sq_nonneg (q^2 - 1)]
  positivity

end ClosedForms

end QOU.Mass.LightNucleiGGChainSign
