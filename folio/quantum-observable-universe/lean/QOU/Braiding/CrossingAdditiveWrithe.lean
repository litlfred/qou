import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.Module.Defs
import Mathlib.Algebra.Field.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.Tactic.Abel
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Crossing-additive braid functionals are multiples of the writhe

A *crossing-additive* functional on braid words assigns a value `a i` to each
positive letter `σᵢ` and `b i` to each negative letter `σᵢ⁻¹`, and adds them up.
This file proves that if such a functional is a function on **braids** — that
is, invariant under free cancellation `σᵢσᵢ⁻¹ = 1` and under the braid relation
`σᵢσⱼσᵢ = σⱼσᵢσⱼ` for adjacent generators — then it is `c · w`, a multiple of
the writhe `w`.

This is the abelianisation `B_n^{ab} ≅ ℤ` read on additive functionals, stated
over any additive commutative group `A` (no ordering, no analysis).

**Consequence (scope (b)).** The crossing energy of `def:crossing-energy`,
`E = q·n₊ − q⁻¹·n₋`, assigns `a = q`, `b = −q⁻¹`. Free cancellation forces
`b = −a`, i.e. `q − q⁻¹ = 0`, so for `q² ≠ 1` the crossing energy is **not** a
function on braids (`crossingEnergy_not_cancellation_invariant`). Writing
`E = w·cosh λ + ℓ·sinh λ`, the part a braid invariant such as a Markov trace
can see is the writhe part; the `ℓ·sinh λ` part counts letters, i.e. word
length, which is a property of the word (a computational cost), not of the braid.

Bean `qou-078y`; write-up `qou-crossing-energy/result.md` §1.

## Indexing

Letters are `Fin n × Bool`: `(i, true) = σᵢ`, `(i, false) = σᵢ⁻¹`, with
`σᵢ` for `i : Fin n`. The sign is explicit, so `σ₀⁻¹` is representable (the
signed-integer encoding `-(i : ℤ)` cannot distinguish `σ₀⁻¹` from `σ₀`).
-/

namespace QOU.Braiding.CrossingAdditive

/-- A braid letter: generator index and sign (`true` = positive crossing). -/
abbrev Letter (n : ℕ) := Fin n × Bool

section Additive

variable {A : Type*} [AddCommGroup A] {n : ℕ}

/-- The crossing-additive functional with weights `a` on positive letters and
`b` on negative letters. -/
def energy (a b : Fin n → A) (w : List (Letter n)) : A :=
  (w.map fun l => if l.2 then a l.1 else b l.1).sum

/-- The writhe: number of positive letters minus number of negative letters. -/
def writhe (w : List (Letter n)) : ℤ :=
  (w.map fun l => if l.2 then (1 : ℤ) else -1).sum

@[simp] theorem energy_nil (a b : Fin n → A) : energy a b [] = 0 := rfl

@[simp] theorem energy_cons (a b : Fin n → A) (l : Letter n) (w : List (Letter n)) :
    energy a b (l :: w) = (if l.2 then a l.1 else b l.1) + energy a b w := by
  simp [energy]

theorem energy_append (a b : Fin n → A) (u v : List (Letter n)) :
    energy a b (u ++ v) = energy a b u + energy a b v := by
  simp [energy]

@[simp] theorem writhe_nil : writhe ([] : List (Letter n)) = 0 := rfl

@[simp] theorem writhe_cons (l : Letter n) (w : List (Letter n)) :
    writhe (l :: w) = (if l.2 then (1 : ℤ) else -1) + writhe w := by
  simp [writhe]

/-- Invariance under free cancellation, in every context:
`u σᵢ^ε σᵢ^{−ε} v` and `u v` have the same value. -/
def CancellationInvariant (a b : Fin n → A) : Prop :=
  ∀ (u v : List (Letter n)) (i : Fin n) (t : Bool),
    energy a b (u ++ [(i, t), (i, !t)] ++ v) = energy a b (u ++ v)

/-- Invariance under the braid relation for adjacent generators, in every
context: `u σᵢσⱼσᵢ v` and `u σⱼσᵢσⱼ v` have the same value when `j = i + 1`. -/
def BraidInvariant (a b : Fin n → A) : Prop :=
  ∀ (u v : List (Letter n)) (i j : Fin n), j.val = i.val + 1 →
    energy a b (u ++ [(i, true), (j, true), (i, true)] ++ v)
      = energy a b (u ++ [(j, true), (i, true), (j, true)] ++ v)

/-- Free cancellation forces the negative weight to be minus the positive one. -/
theorem neg_weight_of_cancellation {a b : Fin n → A}
    (h : CancellationInvariant a b) (i : Fin n) : b i = -a i := by
  have := h [] [] i true
  simp [energy] at this
  exact eq_neg_of_add_eq_zero_right this

/-- The braid relation forces adjacent positive weights to agree. -/
theorem weight_eq_of_braid {a b : Fin n → A} (h : BraidInvariant a b)
    (i j : Fin n) (hij : j.val = i.val + 1) : a i = a j := by
  have h' := h [] [] i j hij
  simp only [List.nil_append, List.append_nil, energy_cons, energy_nil, ite_true,
    add_zero] at h'
  have key : a i - a j = (a i + (a j + a i)) - (a j + (a i + a j)) := by abel
  rw [h', sub_self] at key
  exact sub_eq_zero.mp key

/-- All positive weights equal the weight of `σ₀` when the braid relation holds. -/
theorem weight_eq_zero_index {m : ℕ} {a b : Fin (m + 1) → A} (h : BraidInvariant a b) :
    ∀ i : Fin (m + 1), a i = a 0 := by
  intro ⟨k, hk⟩
  induction k with
  | zero => rfl
  | succ k ih =>
    have hk' : k < m + 1 := Nat.lt_of_succ_lt hk
    rw [← ih hk']
    exact (weight_eq_of_braid h ⟨k, hk'⟩ ⟨k + 1, hk⟩ rfl).symm

/-- If every positive weight is `c` and every negative weight is `−c`, the
functional is `writhe • c`. -/
theorem energy_eq_writhe_smul (c : A) (a b : Fin n → A) (ha : ∀ i, a i = c)
    (hb : ∀ i, b i = -c) (w : List (Letter n)) : energy a b w = writhe w • c := by
  induction w with
  | nil => simp
  | cons l w ih =>
    rw [energy_cons, writhe_cons, ih, add_zsmul]
    cases l.2 <;> simp [ha, hb]

/-- **Exclusion theorem.** A crossing-additive functional that is invariant
under free cancellation and the braid relation is a multiple of the writhe. -/
theorem energy_eq_writhe_smul_of_invariant {m : ℕ} {a b : Fin (m + 1) → A}
    (hc : CancellationInvariant a b) (hb : BraidInvariant a b) :
    ∀ w, energy a b w = writhe w • a 0 :=
  energy_eq_writhe_smul (a 0) a b (weight_eq_zero_index hb)
    (fun i => by rw [neg_weight_of_cancellation hc i, weight_eq_zero_index hb i])

/-- Conversely, every multiple of the writhe is invariant under both moves. -/
theorem writhe_smul_invariant (c : A) :
    CancellationInvariant (n := n) (fun _ => c) (fun _ => -c) ∧
    BraidInvariant (n := n) (fun _ => c) (fun _ => -c) := by
  constructor
  · intro u v i t
    simp only [energy_append, energy_cons, energy_nil]
    cases t <;> simp
  · intro u v i j _
    simp only [energy_append, energy_cons, energy_nil]

end Additive

section CrossingEnergy

variable {R : Type*} [Field R]

/-- The crossing energy `E = q·n₊ − q⁻¹·n₋` of `def:crossing-energy`, as a
crossing-additive functional: weight `q` on `σᵢ`, weight `−q⁻¹` on `σᵢ⁻¹`. -/
def crossingEnergy {n : ℕ} (q : R) (w : List (Letter n)) : R :=
  energy (fun _ => q) (fun _ => -q⁻¹) w

/-- **The crossing energy is not a braid function away from `q² = 1`.**
If it is invariant under free cancellation, then `q² = 1`. -/
theorem sq_eq_one_of_crossingEnergy_cancellation_invariant {m : ℕ} {q : R}
    (hq : q ≠ 0)
    (h : CancellationInvariant (n := m + 1) (A := R) (fun _ => q) (fun _ => -q⁻¹)) :
    q ^ 2 = 1 := by
  have hb := neg_weight_of_cancellation h 0
  simp only [neg_inj] at hb
  -- hb : q⁻¹ = q
  have : q * q = 1 := by
    calc q * q = q * q⁻¹ := by rw [hb]
      _ = 1 := mul_inv_cancel₀ hq
  simpa [sq] using this

/-- Contrapositive form: for `q ≠ 0` with `q² ≠ 1` the crossing energy is not
invariant under free cancellation, so it is a function of the word, not of the
braid. -/
theorem crossingEnergy_not_cancellation_invariant {m : ℕ} {q : R}
    (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) :
    ¬ CancellationInvariant (n := m + 1) (A := R) (fun _ => q) (fun _ => -q⁻¹) :=
  fun h => hq2 (sq_eq_one_of_crossingEnergy_cancellation_invariant hq h)

/-- The crossing energy splits into a writhe part and a length part:
`E = w · (q + q⁻¹)/2 + ℓ · (q − q⁻¹)/2` (char ≠ 2). With `q = e^λ` this is
`w cosh λ + ℓ sinh λ`. Only the first summand is a braid function. -/
theorem crossingEnergy_eq_writhe_add_length {n : ℕ} (q : R) (h2 : (2 : R) ≠ 0)
    (w : List (Letter n)) :
    crossingEnergy q w
      = (writhe w : R) * ((q + q⁻¹) / 2) + (w.length : R) * ((q - q⁻¹) / 2) := by
  unfold crossingEnergy
  induction w with
  | nil => simp
  | cons l w ih =>
    rw [energy_cons, ih, writhe_cons, List.length_cons]
    cases l.2 <;> (simp only [Bool.false_eq_true, ite_false, ite_true]; push_cast; field_simp; ring)

end CrossingEnergy

end QOU.Braiding.CrossingAdditive
