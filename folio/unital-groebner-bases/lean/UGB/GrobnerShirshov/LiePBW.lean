import UGB.GrobnerShirshov.SplayPBW
import Mathlib.Algebra.Lie.Basic
import Mathlib.LinearAlgebra.Basis.Basic

set_option linter.unusedSectionVars false

/-!
# PBW for a Lie algebra with a finite ordered basis (Gröbner–Shirshov route)

The splay system of a Lie algebra: generators `G` (a finite, ranked basis),
one rule `x y ↦ y x + [x, y]` for each `x ≫ y`, with `[x, y] = Σ_e c^e_{xy} e`.

`jacobiCondition` proves the composition condition of `SplayPBW` from the
**Jacobi identity** on the structure constants: modulo the rules below `a b c`,
each commutator `x e − e x` in the Jacobi element becomes `[x, e]`, and what is
left is the coordinate form of `[a,[b,c]] + [b,[c,a]] + [c,[a,b]] = 0`.

`LieConstants.ofBasis` takes the structure constants from a Mathlib
`LieAlgebra` with a basis, so the Jacobi identity used is Mathlib's
`lie_jacobi`, not an assumption.

`normalFormBasis` is the PBW theorem in this setting: for any admissible order
that is degree-first and orders the two-letter words by rank, the sorted words
form a `k`-basis of `k⟨G⟩ / (x y − y x − [x, y])`.

**Not done here**: identifying that quotient with Mathlib's
`UniversalEnvelopingAlgebra` (it is the standard presentation of `U(L)`, but the
isomorphism is not formalised), and constructing the deg-lex order on a general
ranked alphabet (it is taken as an `AdmissibleOrder` with the two properties
used).
-/

namespace UGB.GrobnerShirshov.Splay

open UGB.GrobnerShirshov UGB.GrobnerShirshov.Diamond

universe u v w

variable {G : Type u} [DecidableEq G] [Fintype G] {k : Type v} [CommRing k]

/-- Structure constants of a Lie algebra on the basis `G`:
    `[x, y] = Σ_e c x y e • e`. -/
structure LieConstants (G : Type u) [Fintype G] (k : Type v) [CommRing k] where
  /-- The structure constants. -/
  c : G → G → G → k
  /-- Alternating: `[x, x] = 0`. -/
  alt : ∀ x e, c x x e = 0
  /-- Antisymmetry. -/
  skew : ∀ x y e, c y x e = -c x y e
  /-- **Jacobi**, in coordinates: `[a,[b,d]] + [b,[d,a]] + [d,[a,b]] = 0`. -/
  jacobi : ∀ a b d f : G,
    ∑ e, (c b d e * c a e f + c d a e * c b e f + c a b e * c d e f) = 0

namespace LieConstants

variable (L : LieConstants G k)

/-- The bracket of two generators, in the free algebra. -/
noncomputable def br (x y : G) : MA G k := ∑ e, L.c x y e • (ofW [e] : MA G k)

theorem br_skew (x y : G) : L.br y x = -L.br x y := by
  unfold br
  rw [← Finset.sum_neg_distrib]
  refine Finset.sum_congr rfl (fun e _ => ?_)
  rw [L.skew x y e, neg_smul]

theorem br_self (x : G) : L.br x x = 0 := by
  simp only [br, L.alt, zero_smul, Finset.sum_const_zero]

theorem br_support {x y : G} {w : FreeMonoid G} (hw : w ∈ (L.br x y).support) :
    (FreeMonoid.toList w).length = 1 := by
  classical
  unfold br at hw
  obtain ⟨e, -, he⟩ := Finset.mem_biUnion.mp (Finsupp.support_finset_sum hw)
  have he' := Finsupp.support_smul he
  unfold ofW at he'
  have := Finsupp.support_single_subset he'
  rw [Finset.mem_singleton] at this
  rw [this, FreeMonoid.toList_ofList]; rfl

/-- The commutator defect `x y − y x − [x, y]`. -/
noncomputable def K (x y : G) : MA G k := ofW [x] * ofW [y] - ofW [y] * ofW [x] - L.br x y

/-- `c · (x·br y z − br y z·x)` expanded over the basis. -/
theorem comm_br (x y z : G) :
    ofW [x] * L.br y z - L.br y z * ofW [x] =
      ∑ e, L.c y z e • (ofW [x] * ofW [e] - ofW [e] * ofW [x]) := by
  simp only [br, Finset.mul_sum, Finset.sum_mul, ← Finset.sum_sub_distrib, mul_smul_comm,
    smul_mul_assoc, smul_sub]

/-- The bracket part of the Jacobi element vanishes, by the Jacobi identity. -/
theorem bracket_part_zero (a b d : G) :
    ∑ e, (L.c b d e • L.br a e + L.c a b e • L.br d e + L.c a d e • L.br e b) = 0 := by
  simp only [br, Finset.smul_sum, smul_smul, ← Finset.sum_add_distrib]
  rw [Finset.sum_comm]
  refine Finset.sum_eq_zero (fun f _ => ?_)
  simp only [← add_smul]
  rw [← Finset.sum_smul]
  convert zero_smul k (ofW [f] : MA G k) using 2
  rw [← L.jacobi a b d f]
  refine Finset.sum_congr rfl (fun e _ => ?_)
  rw [L.skew e b f, L.skew a d e]
  ring

/-- **The Jacobi element is a combination of commutator defects.** -/
theorem jacobi_eq (a b d : G) :
    ofW [a] * L.br b d - L.br b d * ofW [a] + ofW [d] * L.br a b - L.br a b * ofW [d]
        + L.br a d * ofW [b] - ofW [b] * L.br a d =
      ∑ e, (L.c b d e • L.K a e + L.c a b e • L.K d e + L.c a d e • L.K e b) := by
  have h1 := L.comm_br a b d
  have h2 := L.comm_br d a b
  have h3 := L.comm_br b a d
  have hz := L.bracket_part_zero a b d
  have e : ofW [a] * L.br b d - L.br b d * ofW [a] + ofW [d] * L.br a b - L.br a b * ofW [d]
        + L.br a d * ofW [b] - ofW [b] * L.br a d =
      (ofW [a] * L.br b d - L.br b d * ofW [a]) + (ofW [d] * L.br a b - L.br a b * ofW [d])
        - (ofW [b] * L.br a d - L.br a d * ofW [b]) := by abel
  rw [e, h1, h2, h3, ← sub_zero (∑ e, _), ← hz]
  simp only [K, smul_sub, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun e _ => ?_)
  abel

end LieConstants

/-! ## The splay data of a Lie algebra -/

variable {ord : AdmissibleOrder G}

/-- The rule-carrying pairs: `(x, y)` with `rk y < rk x`. -/
noncomputable def liePairs (rk : G → ℕ) : List (G × G) :=
  (Finset.univ.filter (fun p : G × G => rk p.2 < rk p.1)).toList

theorem mem_liePairs {rk : G → ℕ} {p : G × G} : p ∈ liePairs rk ↔ rk p.2 < rk p.1 := by
  simp [liePairs]

/-- The splay data of a Lie algebra, for a ranked basis and an admissible order
    that is degree-first and orders two-letter words by rank. -/
noncomputable def LieConstants.splay (L : LieConstants G k) (rk : G → ℕ)
    (hne : ∃ x y : G, rk y < rk x)
    (hdeg : ∀ x y : Monomial G, x.length < y.length → ord.lt x y)
    (hgen : ∀ x y : G, rk y < rk x → ord.lt [y, x] [x, y]) : SplayData G k ord where
  pairs := liePairs rk
  pairs_ne := by
    obtain ⟨x, y, h⟩ := hne
    intro h0
    have : (x, y) ∈ liePairs rk := mem_liePairs.mpr h
    rw [h0] at this; simp at this
  π := L.br
  cf _ _ := 1
  swap_lt p hp := hgen _ _ (mem_liePairs.mp hp)
  pi_lt p _ w hw := hdeg _ _ (by rw [L.br_support hw]; simp)
  trans a b c hab hbc := mem_liePairs.mpr
    (lt_trans ((mem_liePairs (p := (b, c))).mp hbc) ((mem_liePairs (p := (a, b))).mp hab))

variable [Nontrivial k]

/-- Every commutator defect lies below any word of length `3`. -/
theorem LieConstants.K_mem (L : LieConstants G k) (rk : G → ℕ) (hrk : Function.Injective rk)
    (hne : ∃ x y : G, rk y < rk x)
    (hdeg : ∀ x y : Monomial G, x.length < y.length → ord.lt x y)
    (hgen : ∀ x y : G, rk y < rk x → ord.lt [y, x] [x, y]) (v : Monomial G)
    (hv : v.length = 3) (x y : G) :
    JM ord (L.splay rk hne hdeg hgen).sys v (L.K x y) := by
  set d := L.splay rk hne hdeg hgen
  have hlt : ∀ a b : G, ord.lt ([] ++ [a, b] ++ []) v := fun a b => hdeg _ _ (by simp [hv])
  rcases lt_trichotomy (rk y) (rk x) with h | h | h
  · have := d.jm_rule (v := v) ⟨(x, y), mem_liePairs.mpr h⟩ [] [] (hlt x y)
    simp only [ofW_nil, one_mul, mul_one] at this
    convert this using 1
    simp only [LieConstants.K, SplayData.relMA, ← ofW_append, List.cons_append, List.nil_append]
    show _ = ofW [x, y] - (1 : k) • ofW [y, x] - L.br x y
    rw [one_smul]
  · rw [hrk h]
    simp only [LieConstants.K, sub_self, L.br_self]
    exact JM.zero
  · have := d.jm_rule (v := v) ⟨(y, x), mem_liePairs.mpr h⟩ [] [] (hlt y x)
    simp only [ofW_nil, one_mul, mul_one] at this
    convert this.neg using 1
    simp only [LieConstants.K, SplayData.relMA, ← ofW_append, List.cons_append, List.nil_append]
    show _ = -(ofW [y, x] - (1 : k) • ofW [x, y] - L.br y x)
    rw [one_smul, L.br_skew]; abel

/-- **The Jacobi identity discharges the composition condition.** -/
theorem LieConstants.jacobiCondition (L : LieConstants G k) (rk : G → ℕ)
    (hrk : Function.Injective rk) (hne : ∃ x y : G, rk y < rk x)
    (hdeg : ∀ x y : Monomial G, x.length < y.length → ord.lt x y)
    (hgen : ∀ x y : G, rk y < rk x → ord.lt [y, x] [x, y]) :
    (L.splay rk hne hdeg hgen).JacobiCondition := by
  intro a b c _ _
  have e : (L.splay rk hne hdeg hgen).jacobi a b c = ofW [a] * L.br b c - L.br b c * ofW [a]
      + ofW [c] * L.br a b - L.br a b * ofW [c] + L.br a c * ofW [b] - ofW [b] * L.br a c := by
    simp only [SplayData.jacobi, LieConstants.splay, mul_one, one_smul]
  rw [e, L.jacobi_eq a b c]
  have hK := L.K_mem rk hrk hne hdeg hgen [a, b, c] rfl
  exact JM.sum _ _ (fun e _ => (((hK a e).smul _).add ((hK c e).smul _)).add ((hK e b).smul _))

/-- **PBW for a Lie algebra with a finite ranked basis.** The sorted words are a
    `k`-basis of `k⟨G⟩ / (x y − y x − [x, y])`. -/
theorem LieConstants.normalFormBasis [DecidableEq k] (L : LieConstants G k) (rk : G → ℕ)
    (hrk : Function.Injective rk) (hne : ∃ x y : G, rk y < rk x)
    (hdeg : ∀ x y : Monomial G, x.length < y.length → ord.lt x y)
    (hgen : ∀ x y : G, rk y < rk x → ord.lt [y, x] [x, y]) :
    NormalFormBasis ord (L.splay rk hne hdeg hgen).sys :=
  (L.splay rk hne hdeg hgen).normalFormBasis (L.jacobiCondition rk hrk hne hdeg hgen)

/-! ## Structure constants from a Mathlib Lie algebra -/

/-- The structure constants of a Lie algebra with a finite basis. Their Jacobi
    identity is Mathlib's `lie_jacobi`. -/
noncomputable def LieConstants.ofBasis {L : Type w} [LieRing L] [LieAlgebra k L]
    (B : Module.Basis G k L) : LieConstants G k where
  c x y e := B.repr ⁅B x, B y⁆ e
  alt x e := by simp
  skew x y e := by rw [← lie_skew, map_neg, Finsupp.neg_apply]
  jacobi a b d f := by
    have key : ∀ x y z : G, ∑ e, B.repr ⁅B y, B z⁆ e * B.repr ⁅B x, B e⁆ f =
        B.repr ⁅B x, ⁅B y, B z⁆⁆ f := by
      intro x y z
      conv_rhs => rw [← B.sum_repr ⁅B y, B z⁆]
      rw [lie_sum, map_sum, Finsupp.finset_sum_apply]
      refine Finset.sum_congr rfl (fun e _ => ?_)
      rw [lie_smul, map_smul, Finsupp.smul_apply, smul_eq_mul]
    rw [Finset.sum_add_distrib, Finset.sum_add_distrib, key, key, key, ← Finsupp.add_apply,
      ← Finsupp.add_apply, ← map_add, ← map_add, lie_jacobi, map_zero, Finsupp.zero_apply]

/-! ## The rank deg-lex order (so the order hypotheses are met) -/

section RankDegLex

/-- Big-endian base-`B` value of a digit list. -/
def enc (B : ℕ) : List ℕ → ℕ
  | [] => 0
  | x :: xs => x * B ^ xs.length + enc B xs

theorem enc_append (B : ℕ) (a b : List ℕ) : enc B (a ++ b) = enc B a * B ^ b.length + enc B b := by
  induction a with
  | nil => simp [enc]
  | cons x xs ih =>
    simp only [List.cons_append, enc, List.length_append, ih, pow_add]
    ring

theorem enc_lt {B : ℕ} {l : List ℕ} (h : ∀ x ∈ l, x < B) : enc B l < B ^ l.length := by
  induction l with
  | nil => simp [enc]
  | cons x xs ih =>
    have hx := h x (by simp)
    have ih' := ih (fun y hy => h y (by simp [hy]))
    simp only [enc, List.length_cons, pow_succ]
    calc x * B ^ xs.length + enc B xs < x * B ^ xs.length + B ^ xs.length := by omega
      _ = (x + 1) * B ^ xs.length := by ring
      _ ≤ B * B ^ xs.length := Nat.mul_le_mul_right _ hx
      _ = B ^ xs.length * B := by ring

theorem enc_inj {B : ℕ} : ∀ {a b : List ℕ}, a.length = b.length → (∀ x ∈ a, x < B) →
    (∀ x ∈ b, x < B) → enc B a = enc B b → a = b
  | [], [], _, _, _, _ => rfl
  | x :: xs, y :: ys, hl, ha, hb, he => by
    simp only [List.length_cons, Nat.add_right_cancel_iff] at hl
    simp only [enc] at he
    have h1 := enc_lt (fun z hz => ha z (List.mem_cons_of_mem _ hz))
    have h2 := enc_lt (fun z hz => hb z (List.mem_cons_of_mem _ hz))
    rw [← hl] at h2 he
    have hpos : 0 < B ^ xs.length := by
      rcases Nat.eq_zero_or_pos (B ^ xs.length) with h | h
      · omega
      · exact h
    have hxy : x = y := by
      have e1 : (x * B ^ xs.length + enc B xs) / B ^ xs.length = x := by
        rw [Nat.add_comm, Nat.add_mul_div_right _ _ hpos, Nat.div_eq_of_lt h1, zero_add]
      have e2 : (y * B ^ xs.length + enc B ys) / B ^ xs.length = y := by
        rw [Nat.add_comm, Nat.add_mul_div_right _ _ hpos, Nat.div_eq_of_lt h2, zero_add]
      rw [← e1, ← e2, he]
    subst hxy
    have hxs : enc B xs = enc B ys := by omega
    have := enc_inj hl (fun z hz => ha z (List.mem_cons_of_mem _ hz))
      (fun z hz => hb z (List.mem_cons_of_mem _ hz)) hxs
    rw [this]

variable (rk : G → ℕ)

/-- The base: one more than the largest rank. -/
def rkBase : ℕ := Finset.univ.sup rk + 1

theorem rk_lt_base (g : G) : rk g < rkBase rk :=
  Nat.lt_succ_of_le (Finset.le_sup (f := rk) (Finset.mem_univ g))

/-- The code of a word: its ranks read in base `rkBase`. -/
def code (w : Monomial G) : ℕ := enc (rkBase rk) (w.map rk)

theorem code_lt_digits (w : Monomial G) : ∀ x ∈ w.map rk, x < rkBase rk := by
  intro x hx
  obtain ⟨g, -, rfl⟩ := List.mem_map.mp hx
  exact rk_lt_base rk g

/-- Deg-lex by rank: shorter words first, then by code. -/
def rdlLt (a b : Monomial G) : Prop :=
  a.length < b.length ∨ (a.length = b.length ∧ code rk a < code rk b)

theorem code_append (a b : Monomial G) :
    code rk (a ++ b) = code rk a * rkBase rk ^ b.length + code rk b := by
  simp only [code, List.map_append, enc_append, List.length_map]

/-- The **rank deg-lex order**, as an admissible order. -/
def rankDegLex (hrk : Function.Injective rk) : AdmissibleOrder G where
  lt := rdlLt rk
  trichotomy a b := by
    unfold rdlLt
    rcases lt_trichotomy a.length b.length with h | h | h
    · exact Or.inl (Or.inl h)
    · rcases lt_trichotomy (code rk a) (code rk b) with h' | h' | h'
      · exact Or.inl (Or.inr ⟨h, h'⟩)
      · right; left
        have := enc_inj (by simpa using h) (code_lt_digits rk a) (code_lt_digits rk b) h'
        exact List.map_injective_iff.mpr hrk this
      · exact Or.inr (Or.inr (Or.inr ⟨h.symm, h'⟩))
    · exact Or.inr (Or.inr (Or.inl h))
  wf := Subrelation.wf
    (fun {a b} (h : rdlLt rk a b) => by
      show Prod.Lex (· < ·) (· < ·) (a.length, code rk a) (b.length, code rk b)
      rcases h with h | ⟨h1, h2⟩
      · exact Prod.Lex.left _ _ h
      · rw [h1]; exact Prod.Lex.right _ h2)
    (InvImage.wf (fun a => (a.length, code rk a)) (Nat.lt_wfRel.wf.prod_lex Nat.lt_wfRel.wf))
  left_compat a b c h := by
    unfold rdlLt at h ⊢
    rcases h with h | ⟨h1, h2⟩
    · left; simp; omega
    · right
      refine ⟨by simp [h1], ?_⟩
      rw [code_append, code_append, h1]
      omega
  right_compat a b d h := by
    unfold rdlLt at h ⊢
    rcases h with h | ⟨h1, h2⟩
    · left; simp; omega
    · right
      refine ⟨by simp [h1], ?_⟩
      rw [code_append, code_append]
      have hpos : 0 < rkBase rk ^ d.length := Nat.pow_pos (Nat.succ_pos _)
      have := Nat.mul_lt_mul_of_pos_right h2 hpos
      omega

theorem rankDegLex_deg (hrk : Function.Injective rk) (x y : Monomial G)
    (h : x.length < y.length) : (rankDegLex rk hrk).lt x y := Or.inl h

theorem rankDegLex_gen (hrk : Function.Injective rk) (x y : G) (h : rk y < rk x) :
    (rankDegLex rk hrk).lt [y, x] [x, y] := by
  right
  refine ⟨rfl, ?_⟩
  have hx := rk_lt_base rk x
  simp only [code, List.map_cons, List.map_nil, enc, List.length_cons, List.length_nil,
    pow_zero, mul_one, zero_add, pow_one, add_zero]
  calc rk y * rkBase rk + rk x < rk y * rkBase rk + rkBase rk := by omega
    _ = (rk y + 1) * rkBase rk := by ring
    _ ≤ rk x * rkBase rk := Nat.mul_le_mul_right _ h
    _ ≤ rk x * rkBase rk + rk y := Nat.le_add_right _ _

end RankDegLex

/-- **PBW, Gröbner–Shirshov route.** For a Lie algebra `L` over a nontrivial
    commutative ring with a finite basis `B` indexed by a ranked set `G` with at
    least two elements, the sorted words in `G` are a `k`-basis of
    `k⟨G⟩ / (x y − y x − [x, y])` under the rank deg-lex order. Its Jacobi input
    is Mathlib's `lie_jacobi`. -/
theorem lie_pbw [Nontrivial k] [DecidableEq k] {L : Type w} [LieRing L] [LieAlgebra k L]
    (B : Module.Basis G k L) (rk : G → ℕ) (hrk : Function.Injective rk)
    (hne : ∃ x y : G, rk y < rk x) :
    NormalFormBasis (rankDegLex rk hrk)
      ((LieConstants.ofBasis B).splay rk hne (rankDegLex_deg rk hrk) (rankDegLex_gen rk hrk)).sys :=
  (LieConstants.ofBasis B).normalFormBasis rk hrk hne _ _

end UGB.GrobnerShirshov.Splay
