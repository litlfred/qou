/-
# `U(1) = 3·lk` for every three-strand braid closure

Thread "Derive the electron's categorical weight", fifth part (2026-11-27, owner card: "Prove
3·lk for all 3-strand links"). Audit: `docs/audits/2026-11-27-electron-categorical-weight.md` §11.

`QOU.Transcendental.MassTheory.RingMassLinkingNumber` proved `U(1) = 3·lk` for the two-strand
torus links. Here the statement is proved for **every** word in `σ₁^{±1}, σ₂^{±1}` on three
strands. That includes the electron `σ₁σ₂σ₁`, the muon `(σ₁σ₂⁻¹)²` and the proton `(σ₁σ₂⁻¹)³`.

**First-order jet at `q = 1`.** The convention-D Hecke matrices (`WeightSpaceMarkov.r21a/r21b`)
have value `s₁ = !![1,1;0,−1]`, `s₂ = !![−1,0;1,1]` at `q = 1`, and derivative `+I`. Their
inverses `σ⁻¹ = σ − (q − q⁻¹)` have derivative `−I`. So a letter of sign `e` has jet `(sᵢ, e·I)`.
For a word `w` the jet of `ρ_q(w)` is `(P w, Q w)` with the Leibniz recursion (`P`, `Q`).
`Q_eq_sum`: `Q w = Σⱼ eⱼ · P(w with letter j deleted)`. That the jet is the real derivative is
proved in `QOU.Transcendental.MassTheory.RingMassLinkingThreeStrand`.

**Ring mass.** `m_q(w) = [2]³ q^{−2·wr} (y₃ q^{wr} + y₂₁ tr ρ_q(w))`. `[2]`, `y₃`, `y₂₁` have
derivative `0` at `q = 1` (they are even in `log q`). So the value is `m0 w = 4 + 2 tr P` and the
derivative is `m1 w = −4·wr − 4·wr·tr P + 2 tr Q`.

**Components and linking.** `perm w ∈ S₃` is the strand permutation, and the closure has one
component per orbit (`comps`). Deleting letter `j` is the oriented smoothing of crossing `j`, and
it merges two components exactly when the two strands at that crossing lie in different
components (`merge_iff_not_sameOrbit`). `linkSum w = Σ_{j inter-component} eⱼ = 2·lk`.

* `m0_eq`: `m(1) = 2^c`.
* `two_mul_m1`: `2·m′(1) = −3·m(1)·linkSum`. So `U(1) = −m′(1)/m(1) = (3/2)·linkSum = 3·lk`.

Everything is over `ℤ`, with no measured value.
-/
import Mathlib.Data.Matrix.Basic
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic

namespace QOU.Observations.RingMassLinkingThreeStrand

open Matrix

/-! ### `S₃` as an explicit enumeration -/

/-- The six elements of `S₃`. `a = (0 1)`, `b = (1 2)`, `c = (0 2)`, `r: 0↦1↦2↦0`, `r2 = r⁻¹`. -/
inductive S3 | e | a | b | c | r | r2
  deriving DecidableEq, Fintype, Repr

namespace S3

/-- The action on `{0, 1, 2}`. -/
def act : S3 → Fin 3 → Fin 3
  | e, k => k
  | a, k => ![1, 0, 2] k
  | b, k => ![0, 2, 1] k
  | c, k => ![2, 1, 0] k
  | r, k => ![1, 2, 0] k
  | r2, k => ![2, 0, 1] k

/-- Decode a map from its images of `0` and `1`. -/
def ofImages (x y : Fin 3) : S3 :=
  match x, y with
  | 0, 1 => e | 1, 0 => a | 0, 2 => b | 2, 1 => c | 1, 2 => r | 2, 0 => r2
  | _, _ => e

/-- Composition `(g * h)(k) = g (h k)`. -/
def mul (g h : S3) : S3 := ofImages (g.act (h.act 0)) (g.act (h.act 1))

instance : Mul S3 := ⟨mul⟩

theorem act_mul (g h : S3) (k : Fin 3) : (g * h).act k = g.act (h.act k) := by
  revert g h k; decide

theorem mul_assoc' (g h k : S3) : g * h * k = g * (h * k) := by
  revert g h k; decide

/-- Inverse. -/
def inv : S3 → S3 | r => r2 | r2 => r | g => g

theorem inv_mul (g : S3) : inv g * g = e := by revert g; decide
theorem mul_inv (g : S3) : g * inv g = e := by revert g; decide
theorem e_mul (g : S3) : e * g = g := by revert g; decide

theorem mul_conj_mul (g t p : S3) : g * (t * p) = g * t * inv g * (g * p) := by
  revert g t p; decide

/-- Fixed points. -/
def fix (g : S3) : ℕ := (Finset.univ.filter fun k : Fin 3 => g.act k = k).card

/-- Same orbit of `⟨g⟩` (orbits in `S₃` have at most three points). -/
def SameOrbit (g : S3) (u v : Fin 3) : Prop := v = u ∨ v = g.act u ∨ v = g.act (g.act u)

instance (g : S3) (u v : Fin 3) : Decidable (SameOrbit g u v) := by
  unfold SameOrbit; infer_instance

/-- Number of orbits = number of components of the closure: points that are minimal in their
orbit. -/
def comps (g : S3) : ℕ :=
  (Finset.univ.filter fun k : Fin 3 => k ≤ g.act k ∧ k ≤ g.act (g.act k)).card

/-- The transpositions, with their two points. -/
def IsSwap (t : S3) (u v : Fin 3) : Prop :=
  u ≠ v ∧ t.act u = v ∧ t.act v = u ∧ ∀ k, k ≠ u → k ≠ v → t.act k = k

instance (t : S3) (u v : Fin 3) : Decidable (IsSwap t u v) := by
  unfold IsSwap; infer_instance

theorem swap_mul_self (t : S3) (u v : Fin 3) (h : IsSwap t u v) : t * t = e := by
  revert t u v; decide

/-- Conjugating a transposition by `g` moves its points by `g`. -/
theorem swap_conj (g t : S3) (u v : Fin 3) (h : IsSwap t u v) :
    IsSwap (g * t * inv g) (g.act u) (g.act v) := by
  revert g t u v; decide

/-- **Smoothing merges two components iff the strands lie in different components.** -/
theorem merge_iff_not_sameOrbit (g t : S3) (u v : Fin 3) (ht : IsSwap t u v) :
    comps (t * g) + 1 = comps g ↔ ¬ SameOrbit g u v := by
  revert g t u v; decide

end S3

/-! ### The standard representation at `q = 1` -/

abbrev Mat := Matrix (Fin 2) (Fin 2) ℤ

/-- `ρ` at `q = 1` on `S₃` (the reduced standard representation, convention D). -/
def rho : S3 → Mat
  | .e => 1
  | .a => !![1, 1; 0, -1]
  | .b => !![-1, 0; 1, 1]
  | .c => !![0, -1; -1, 0]
  | .r => !![0, 1; -1, -1]
  | .r2 => !![-1, -1; 1, 0]

theorem rho_mul (g h : S3) : rho (g * h) = rho g * rho h := by
  cases g <;> cases h <;>
    (ext i j; fin_cases i <;> fin_cases j <;> rfl)

/-- `tr ρ(g) = fix(g) − 1`, the reduced standard character. -/
theorem trace_rho (g : S3) : (rho g).trace = (g.fix : ℤ) - 1 := by
  cases g <;> rfl

/-! ### Words, value and jet -/

/-- A letter: `first = true` for `σ₁`, `pos = false` for an inverse. -/
structure Letter where
  first : Bool
  pos : Bool

def Letter.gen (l : Letter) : S3 := if l.first then .a else .b
def Letter.sgn (l : Letter) : ℤ := if l.pos then 1 else -1

/-- Strand permutation of a word. -/
def perm : List Letter → S3
  | [] => .e
  | l :: w => l.gen * perm w

/-- Value at `q = 1` of `ρ_q(w)`. -/
def P : List Letter → Mat
  | [] => 1
  | l :: w => rho l.gen * P w

/-- First-order part: the letter `l` has jet `(ρ(gen l), sgn l · I)`, Leibniz rule. -/
def Q : List Letter → Mat
  | [] => 0
  | l :: w => rho l.gen * Q w + l.sgn • P w

def writhe (w : List Letter) : ℤ := (w.map Letter.sgn).sum

theorem P_eq_rho (w : List Letter) : P w = rho (perm w) := by
  induction w with
  | nil => rfl
  | cons l w ih => simp [P, perm, ih, rho_mul]

/-- **`Q w = Σⱼ eⱼ · P(w with letter j deleted)`.** -/
theorem Q_eq_sum (w : List Letter) :
    Q w = ∑ j : Fin w.length, (w.get j).sgn • P (w.eraseIdx j) := by
  induction w with
  | nil => simp [Q]
  | cons l w ih =>
    show _ = ∑ j : Fin (w.length + 1), ((l :: w).get j).sgn • P ((l :: w).eraseIdx j)
    rw [Fin.sum_univ_succ]
    simp only [Q, ih, Finset.mul_sum, List.get_eq_getElem, Fin.val_zero,
      List.getElem_cons_zero, List.eraseIdx_cons_zero, Fin.val_succ, List.getElem_cons_succ,
      List.eraseIdx_cons_succ, P, mul_smul_comm]
    rw [add_comm]

/-- Deleting letter `j` multiplies the permutation by a transposition on the left. -/
theorem perm_eraseIdx (w : List Letter) (j : Fin w.length) :
    ∃ t u v, S3.IsSwap t u v ∧ perm w = t * perm (w.eraseIdx j) := by
  induction w with
  | nil => exact j.elim0
  | cons l w ih =>
    cases j using Fin.cases with
    | zero =>
      obtain ⟨u, v, h⟩ : ∃ u v, S3.IsSwap l.gen u v := by
        unfold Letter.gen; split <;> decide
      exact ⟨l.gen, u, v, h, by simp [perm]⟩
    | succ j =>
      obtain ⟨t, u, v, h, hp⟩ := ih j
      refine ⟨l.gen * t * S3.inv l.gen, l.gen.act u, l.gen.act v, S3.swap_conj _ _ _ _ h, ?_⟩
      simp only [Fin.val_succ, List.eraseIdx_cons_succ, perm, hp]
      exact S3.mul_conj_mul _ _ _

/-- Crossing `j` joins two different components: smoothing it merges them. -/
def Inter (w : List Letter) (j : Fin w.length) : Prop :=
  S3.comps (perm (w.eraseIdx j)) + 1 = S3.comps (perm w)

instance (w : List Letter) (j : Fin w.length) : Decidable (Inter w j) := by
  unfold Inter; infer_instance

/-- `Σ_{j inter-component} eⱼ = 2·lk`. -/
def linkSum (w : List Letter) : ℤ :=
  ∑ j : Fin w.length, if Inter w j then (w.get j).sgn else 0

/-- Value of the ring mass at `q = 1`. -/
def m0 (w : List Letter) : ℤ := 4 + 2 * (P w).trace

/-- Derivative of the ring mass at `q = 1` (jet; see the Transcendental bridge). -/
def m1 (w : List Letter) : ℤ :=
  -4 * writhe w - 4 * writhe w * (P w).trace + 2 * (Q w).trace

/-- `4 + 2 tr ρ(g) = 2^{comps g}`. -/
theorem four_add_two_trace (g : S3) : 4 + 2 * (rho g).trace = 2 ^ S3.comps g := by
  rw [trace_rho]; revert g; decide

/-- **`m(1) = 2^c`.** -/
theorem m0_eq (w : List Letter) : m0 w = 2 ^ S3.comps (perm w) := by
  rw [m0, P_eq_rho, four_add_two_trace]

/-- The per-crossing identity over `S₃`. -/
theorem crossing_term (g t : S3) (u v : Fin 3) (ht : S3.IsSwap t u v) :
    2 * (-4 - 4 * (rho g).trace + 2 * (rho (t * g)).trace)
      = if S3.comps (t * g) + 1 = S3.comps g then -3 * 2 ^ S3.comps g else 0 := by
  rw [trace_rho, trace_rho]; revert g t u v; decide

theorem writhe_eq_sum (w : List Letter) : writhe w = ∑ j : Fin w.length, (w.get j).sgn := by
  induction w with
  | nil => simp [writhe]
  | cons l w ih =>
    show _ = ∑ j : Fin (w.length + 1), ((l :: w).get j).sgn
    rw [Fin.sum_univ_succ]
    simp only [writhe, List.map_cons, List.sum_cons] at ih ⊢
    rw [ih]
    simp

/-- **`2·m′(1) = −3·m(1)·linkSum`**, i.e. `U(1) = 3·lk`. -/
theorem two_mul_m1 (w : List Letter) : 2 * m1 w = -3 * m0 w * linkSum w := by
  have hQ : (Q w).trace = ∑ j : Fin w.length, (w.get j).sgn * (P (w.eraseIdx j)).trace := by
    rw [Q_eq_sum, Matrix.trace_sum]
    refine Finset.sum_congr rfl fun j _ => ?_
    rw [Matrix.trace_smul, smul_eq_mul]
  have key : ∀ j : Fin w.length,
      2 * ((w.get j).sgn * (-4 - 4 * (P w).trace + 2 * (P (w.eraseIdx j)).trace))
        = -3 * m0 w * (if Inter w j then (w.get j).sgn else 0) := by
    intro j
    obtain ⟨t, u, v, h, hp⟩ := perm_eraseIdx w j
    have hinv : perm (w.eraseIdx j) = t * perm w := by
      rw [hp, ← S3.mul_assoc', S3.swap_mul_self t u v h, S3.e_mul]
    have := crossing_term (perm w) t u v h
    by_cases hi : Inter w j
    · have hi' : S3.comps (t * perm w) + 1 = S3.comps (perm w) := by
        have := hi; unfold Inter at this; rwa [hinv] at this
      rw [if_pos hi, m0_eq, P_eq_rho, P_eq_rho, hinv]
      rw [if_pos hi'] at this
      linear_combination (w.get j).sgn * this
    · have hi' : ¬ S3.comps (t * perm w) + 1 = S3.comps (perm w) := by
        intro h'; apply hi; unfold Inter; rwa [hinv]
      rw [if_neg hi, m0_eq, P_eq_rho, P_eq_rho, hinv]
      rw [if_neg hi'] at this
      linear_combination (w.get j).sgn * this
  unfold m1 linkSum
  rw [hQ, writhe_eq_sum]
  have : 2 * (-4 * ∑ j : Fin w.length, (w.get j).sgn
      - 4 * (∑ j : Fin w.length, (w.get j).sgn) * (P w).trace
      + 2 * ∑ j : Fin w.length, (w.get j).sgn * (P (w.eraseIdx j)).trace)
      = ∑ j : Fin w.length,
          2 * ((w.get j).sgn * (-4 - 4 * (P w).trace + 2 * (P (w.eraseIdx j)).trace)) := by
    simp only [Finset.mul_sum, Finset.sum_mul, ← Finset.sum_sub_distrib,
      ← Finset.sum_add_distrib]
    refine Finset.sum_congr rfl fun j _ => by ring
  rw [this, Finset.mul_sum]
  exact Finset.sum_congr rfl fun j _ => key j

/-! ### The corpus words -/

def s1 : Letter := ⟨true, true⟩
def s2 : Letter := ⟨false, true⟩
def s2i : Letter := ⟨false, false⟩

/-- Electron `σ₁σ₂σ₁` (Hopf ⊔ nothing: two components, `lk = 1`). -/
theorem electron_linkSum : linkSum [s1, s2, s1] = 2 ∧ S3.comps (perm [s1, s2, s1]) = 2 := by
  decide

/-- Muon `(σ₁σ₂⁻¹)²` (4₁, a knot). -/
theorem muon_linkSum : linkSum [s1, s2i, s1, s2i] = 0 ∧ S3.comps (perm [s1, s2i, s1, s2i]) = 1 := by
  decide

/-- Proton `(σ₁σ₂⁻¹)³` (Borromean: three components, all `lk = 0`). -/
theorem proton_linkSum :
    linkSum [s1, s2i, s1, s2i, s1, s2i] = 0 ∧ S3.comps (perm [s1, s2i, s1, s2i, s1, s2i]) = 3 := by
  decide

/-- Control `σ₁⁴σ₂` (`T(2,4)`, `lk = 2`). -/
theorem t24_linkSum : linkSum [s1, s1, s1, s1, s2] = 4 := by
  decide

end QOU.Observations.RingMassLinkingThreeStrand
