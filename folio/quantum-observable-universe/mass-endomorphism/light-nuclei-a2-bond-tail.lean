import MassEndomorphism.MarkovTraceRecursiveReducer
import Mathlib.Tactic.FieldSimp

/-!
# The A = 2 γγ bond on the four-strand tail

By `towerTr_disjoint` the first nucleon factors out of the A = 2 trace, so a single bond
(nucleon 0 into nucleon 1) acts on a four-strand tail: the receiving nucleon's word on
`σ_1, σ_2`, followed by the bond `V³ = (σ_0 σ_1⁻¹)³` on `σ_0, σ_1`.

Letters are `σ_i + b` with `b = 0` (`σ`), `b = -h` (`σ⁻¹ = σ - h`) and `b = -h/2`.
The trace is `trWord`, which equals every Markov trace (`isMarkovTrace_eq_trWord`); the
Markov parameter `z` and `h = q - q⁻¹` are free elements of a field with `2 ≠ 0`.

Main results, all exact identities in `z` and `h`:
* `proton_free`, `neutron_free`: the free tail traces.
* `bond_into_proton`: the bond changes the trace by
  `h⁴ (z² - h z - 1)(-h⁷ + h⁶ z - 4h⁵ + 3h⁴ z - 6h³ + 2h² z - 3h - 2z) / 4`.
* `bond_into_neutron`: by `h⁵ (h² + 1)(h² + 4)(h z - h² - 1)(z² - h z - 1) / 4`.
* `bond_into_proton_vanishes`, `bond_into_neutron_vanishes`: both changes vanish when
  `z² - h z - 1 = 0`.

Method: `ME` is a merging evaluator (it collects like basis terms after each letter);
`ME_eq_P` proves it equals the plain expansion `P`, and `tail_eq_trWord` writes `P` as a sum of
`trWord` over the positive-word expansion of the letters.

Ref: [jones1987] Hecke algebra representations of braid groups, Ann. Math. 126 (1987).
-/

open QOU.BraidKnot
namespace QOU.LightNucleiBond

variable {R : Type*} [CommRing R] (z h : R)

/-- Trace functional on a formal sum of basis elements `T_w` of `H_N`. -/
def tsum (N : ℕ) (e : List (R × List ℕ)) : R :=
  (e.map fun p => p.1 * trBasis z h N p.2).sum

/-- Trace of `e · ∏ (σ_i + b)`, expanded letter by letter (no merging). -/
def P (N : ℕ) : List (R × List ℕ) → List (R × ℕ) → R
  | e, [] => tsum z h N e
  | e, (b, i) :: L => P N (mulGen h e i) L + b * P N e L

/-- Add `c · T_w` to a formal sum, merging with an equal basis element. -/
def addTerm (c : R) (w : List ℕ) : List (R × List ℕ) → List (R × List ℕ)
  | [] => [(c, w)]
  | (d, v) :: rest => if v = w then (d + c, v) :: rest else (d, v) :: addTerm c w rest

def collect (e : List (R × List ℕ)) : List (R × List ℕ) :=
  e.foldr (fun p acc => addTerm p.1 p.2 acc) []

/-- One letter `σ_i + b`, then merge like terms. -/
def stepL (e : List (R × List ℕ)) (bi : R × ℕ) : List (R × List ℕ) :=
  collect (mulGen h e bi.2 ++ e.map fun p => (bi.1 * p.1, p.2))

/-- The merging evaluator. -/
def ME (N : ℕ) (e : List (R × List ℕ)) (L : List (R × ℕ)) : R :=
  tsum z h N (L.foldl (stepL h) e)

section Lemmas

theorem mulGen_cons (e : List (R × List ℕ)) (p : R × List ℕ) (i : ℕ) :
    mulGen h (p :: e) i = mulGen h [p] i ++ mulGen h e i := by
  simp [mulGen, List.flatMap_cons]

theorem mulGen_append (e₁ e₂ : List (R × List ℕ)) (i : ℕ) :
    mulGen h (e₁ ++ e₂) i = mulGen h e₁ i ++ mulGen h e₂ i := by
  simp [mulGen, List.flatMap_append]

theorem mulGen_scale (b : R) (i : ℕ) : ∀ e : List (R × List ℕ),
    mulGen h (e.map fun p => (b * p.1, p.2)) i = (mulGen h e i).map fun p => (b * p.1, p.2)
  | [] => by simp [mulGen]
  | p :: e => by
    rw [List.map_cons, mulGen_cons, mulGen_cons h e p, mulGen_scale b i e, List.map_append]
    congr 1
    simp only [mulGen, List.flatMap_cons, List.flatMap_nil, List.append_nil]
    split_ifs <;> simp [mul_assoc]

theorem P_append (N : ℕ) : ∀ (L : List (R × ℕ)) (e₁ e₂ : List (R × List ℕ)),
    P z h N (e₁ ++ e₂) L = P z h N e₁ L + P z h N e₂ L
  | [], e₁, e₂ => by
    simp only [P, tsum, List.map_append]
    induction e₁ with
    | nil => simp
    | cons p e ih => simp only [List.map_cons, List.cons_append, List.sum_cons] at ih ⊢; rw [ih]; ring
  | (b, i) :: L, e₁, e₂ => by
    simp only [P]; rw [mulGen_append, P_append N L, P_append N L]; ring

theorem P_scale (N : ℕ) (b : R) : ∀ (L : List (R × ℕ)) (e : List (R × List ℕ)),
    P z h N (e.map fun p => (b * p.1, p.2)) L = b * P z h N e L
  | [], e => by
    simp only [P, tsum]
    induction e with
    | nil => simp
    | cons p e ih => simp only [List.map_cons, List.sum_cons] at ih ⊢; rw [ih]; ring
  | (c, i) :: L, e => by
    simp only [P]; rw [mulGen_scale, P_scale N b L, P_scale N b L]; ring

theorem P_single (N : ℕ) (L : List (R × ℕ)) (c : R) (w : List ℕ) :
    P z h N [(c, w)] L = c * P z h N [(1, w)] L := by
  have := P_scale z h N c L [(1, w)]; simpa using this

theorem P_cons (N : ℕ) (L : List (R × ℕ)) (p : R × List ℕ) (e : List (R × List ℕ)) :
    P z h N (p :: e) L = P z h N [p] L + P z h N e L := by
  rw [← P_append]; rfl

theorem P_nil (N : ℕ) : ∀ L : List (R × ℕ), P z h N [] L = 0
  | [] => by simp [P, tsum]
  | (b, i) :: L => by simp [P, mulGen, P_nil N L]

theorem P_addTerm (N : ℕ) (L : List (R × ℕ)) (c : R) (w : List ℕ) :
    ∀ acc : List (R × List ℕ), P z h N (addTerm c w acc) L = P z h N [(c, w)] L + P z h N acc L
  | [] => by simp [addTerm, P_nil]
  | (d, v) :: rest => by
    by_cases hv : v = w
    · subst hv
      simp only [addTerm, if_true]
      rw [P_cons z h N L (d + c, v) rest, P_cons z h N L (d, v) rest, P_single z h N L (d + c), P_single z h N L d,
        P_single z h N L c]; ring
    · simp only [addTerm, hv, if_false]
      rw [P_cons z h N L (d, v) (addTerm c w rest), P_addTerm N L c w rest,
        P_cons z h N L (d, v) rest]; ring

theorem P_collect (N : ℕ) (L : List (R × ℕ)) :
    ∀ e : List (R × List ℕ), P z h N (collect e) L = P z h N e L
  | [] => rfl
  | p :: e => by
    have := P_collect N L e
    simp only [collect, List.foldr_cons] at this ⊢
    rw [P_addTerm, this, P_cons z h N L p e]

/-- The merging evaluator computes the expanded trace. -/
theorem ME_eq_P (N : ℕ) : ∀ (L : List (R × ℕ)) (e : List (R × List ℕ)),
    ME z h N e L = P z h N e L
  | [], e => rfl
  | (b, i) :: L, e => by
    simp only [ME, List.foldl_cons] at *
    have := ME_eq_P N L (stepL h e (b, i))
    simp only [ME] at this
    rw [this, stepL, P_collect, P_append, P_scale, P]


/-- Expansion of `∏ (σ_i + b)` into positive words: each letter is either kept (`σ_i`) or
replaced by its scalar `b`. -/
def subwords : List (R × ℕ) → List (R × List ℕ)
  | [] => [(1, [])]
  | (b, i) :: L => (subwords L).map (fun p => (p.1, i :: p.2)) ++ (subwords L).map (fun p => (b * p.1, p.2))

theorem sum_map_append' (f : R × List ℕ → R) (a b : List (R × List ℕ)) :
    ((a ++ b).map f).sum = (a.map f).sum + (b.map f).sum := by
  induction a with
  | nil => simp
  | cons p a ih => simp only [List.cons_append, List.map_cons, List.sum_cons, ih]; ring

theorem sum_map_mul' (b : R) (f : R × List ℕ → R) (a : List (R × List ℕ)) :
    (a.map fun p => b * f p).sum = b * (a.map f).sum := by
  induction a with
  | nil => simp
  | cons p a ih => simp only [List.map_cons, List.sum_cons, ih]; ring

/-- `P` is the sum over subwords of the trace of the prefix followed by the subword. -/
theorem P_subwords (N : ℕ) (init : List (R × List ℕ)) :
    ∀ (L : List (R × ℕ)) (pre : List ℕ),
      P z h N (mulGens h init pre) L =
        ((subwords L).map fun p => p.1 * tsum z h N (mulGens h init (pre ++ p.2))).sum
  | [], pre => by simp [P, subwords]
  | (b, i) :: L, pre => by
    simp only [P, subwords]
    have h1 : mulGen h (mulGens h init pre) i = mulGens h init (pre ++ [i]) := by
      simp [mulGens, List.foldl_append]
    rw [h1, P_subwords N init L (pre ++ [i]), P_subwords N init L pre, sum_map_append']
    simp only [List.map_map, Function.comp_def, List.append_assoc, List.singleton_append]
    rw [← sum_map_mul']
    congr 1
    apply congrArg; apply List.map_congr_left; intro p _; ring

end Lemmas


section Tail
variable {K : Type*} [Field K] (z h : K)

def lS (i : ℕ) : K × ℕ := (0, i)
def lI (i : ℕ) : K × ℕ := (-h, i)
def lA (i : ℕ) : K × ℕ := (-h / 2, i)
def V3w (k : ℕ) : List (K × ℕ) := [lS k, lI h (k+1), lS k, lI h (k+1), lS k, lI h (k+1)]
def protonW (k : ℕ) : List (K × ℕ) := V3w h k ++ [lS k, lA h k, lA h (k+1), lS k, lS k]
def neutronW (k : ℕ) : List (K × ℕ) := V3w h k ++ [lA h k, lA h k, lI h (k+1), lS k, lS k]
theorem trB_zero (w : List ℕ) : trBasis z h 0 w = 1 := rfl

theorem trB_cons (m a : ℕ) (l : List ℕ) : trBasis z h (m + 1) (a :: l) =
    if (a :: l).getD m 0 = m then trBasis z h m ((a :: l).take m)
    else z * ((mulGens h [(1, ((List.range' ((a :: l).idxOf m) (m - (a :: l).idxOf m)).foldl swapAt
        (a :: l)).take m)] (List.range' ((a :: l).idxOf m) (m - 1 - (a :: l).idxOf m)).reverse).map
          fun p => p.1 * trBasis z h m p.2).sum := by
  rw [trBasis]

def tail (L : List (K × ℕ)) : K := ME z h 4 [(1, [0,1,2,3])] L

/-- `tail L` is the Markov trace `trWord` (which equals every Markov trace,
`isMarkovTrace_eq_trWord`) summed over the positive-word expansion of the letters. -/
theorem tail_eq_trWord (L : List (K × ℕ)) :
    tail z h L = ((subwords L).map fun p => p.1 * trWord z h 3 (p.2.map Int.ofNat)).sum := by
  have := P_subwords z h 4 [(1, [0,1,2,3])] L []
  simp only [mulGens, List.foldl_nil, List.nil_append] at this
  rw [tail, ME_eq_P, this]
  congr 1; apply List.map_congr_left; intro p _
  simp [trWord, tsum, mulGens, List.map_map, Function.comp_def, List.range, List.range.loop]

/-- Expand a tail trace to a rational function of `z, h`: run the merging evaluator on the
concrete word, then the recursive trace on each concrete basis permutation. -/
macro "tail_eval" : tactic => `(tactic| (
  simp only [tail, ME, protonW, neutronW, V3w, lS, lI, lA, List.cons_append, List.nil_append,
    List.foldl_cons, List.foldl_nil]
  simp (config := {decide := true}) only [stepL, collect, addTerm, mulGen, swapAt, List.flatMap_cons,
    List.flatMap_nil, List.map_cons, List.map_nil, List.cons_append, List.nil_append, List.foldr_cons,
    List.foldr_nil, List.getD_cons_zero, List.getD_cons_succ, List.set_cons_zero, List.set_cons_succ,
    List.append_nil, ite_true, ite_false, mul_zero, zero_mul, add_zero, zero_add, mul_one, one_mul]
  simp only [tsum, List.map_cons, List.map_nil, List.sum_cons, List.sum_nil, mul_zero, zero_mul, add_zero, zero_add, mul_one, one_mul]
  simp (config := {decide := true}) only [trB_zero, trB_cons, mulGens, mulGen, swapAt, List.range', List.idxOf,
    List.take, List.foldl_cons, List.foldl_nil, List.flatMap_cons, List.flatMap_nil, List.map_cons,
    List.map_nil, List.sum_cons, List.sum_nil, List.getD_cons_zero, List.getD_cons_succ,
    List.set_cons_zero, List.set_cons_succ, List.reverse_cons, List.reverse_nil, List.cons_append,
    List.nil_append, List.append_nil, ite_true, ite_false, List.findIdx_cons, List.findIdx_nil,
    List.take_succ_cons, List.take_zero, cond_true, cond_false, Nat.reduceBEq, beq_self_eq_true, Nat.reduceSub, Nat.reduceAdd]
  field_simp
  ring))

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem proton_free (h2 : (2 : K) ≠ 0) : 4 * tail z h (protonW h 1) =
    -(-h^10*z + h^9*z^2 - h^9 - 5*h^8*z + 5*h^7*z^2 - 5*h^7 - 9*h^6*z + 9*h^5*z^2 - 9*h^5
      - 5*h^4*z + 4*h^3*z^2 - 5*h^3 + h^2*z - 6*h*z^2 + 2*h - 4*z) := by
  tail_eval

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem neutron_free (h2 : (2 : K) ≠ 0) : 4 * tail z h (neutronW h 1) =
    -(h^2+4)*(-h^8*z + h^7*z^2 - h^7 - 3*h^6*z + 3*h^5*z^2 - 3*h^5 - 2*h^4*z + 2*h^3*z^2
      - 2*h^3 + h^2*z - h*z^2 + h - z) := by
  tail_eval

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem bond_into_proton (h2 : (2 : K) ≠ 0) :
    4 * (tail z h (protonW h 1 ++ V3w h 0) - tail z h (protonW h 1)) =
      h^4*(z^2-h*z-1)*(-h^7+h^6*z-4*h^5+3*h^4*z-6*h^3+2*h^2*z-3*h-2*z) := by
  tail_eval

set_option maxRecDepth 100000 in
set_option maxHeartbeats 0 in
theorem bond_into_neutron (h2 : (2 : K) ≠ 0) :
    4 * (tail z h (neutronW h 1 ++ V3w h 0) - tail z h (neutronW h 1)) =
      h^5*(h^2+1)*(h^2+4)*(h*z-h^2-1)*(z^2-h*z-1) := by
  tail_eval


theorem four_ne_zero_of_two (h2 : (2 : K) ≠ 0) : (4 : K) ≠ 0 := by
  have : (4 : K) = 2 * 2 := by norm_num
  rw [this]; exact mul_ne_zero h2 h2

/-- The bond into a proton leaves the trace unchanged when `z² - h z - 1 = 0`
(that is `z = q` or `z = -q⁻¹`). -/
theorem bond_into_proton_vanishes (h2 : (2 : K) ≠ 0) (hz : z ^ 2 - h * z - 1 = 0) :
    tail z h (protonW h 1 ++ V3w h 0) = tail z h (protonW h 1) := by
  have e := bond_into_proton z h h2
  rw [hz, mul_zero, zero_mul] at e
  exact sub_eq_zero.mp ((mul_eq_zero.mp e).resolve_left (four_ne_zero_of_two h2))

/-- The bond into a neutron leaves the trace unchanged when `z² - h z - 1 = 0`. -/
theorem bond_into_neutron_vanishes (h2 : (2 : K) ≠ 0) (hz : z ^ 2 - h * z - 1 = 0) :
    tail z h (neutronW h 1 ++ V3w h 0) = tail z h (neutronW h 1) := by
  have e := bond_into_neutron z h h2
  rw [hz, mul_zero] at e
  exact sub_eq_zero.mp ((mul_eq_zero.mp e).resolve_left (four_ne_zero_of_two h2))

end Tail
end QOU.LightNucleiBond
