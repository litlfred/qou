import Mathlib.Tactic
import Mathlib.Algebra.Lie.OfAssociative
import Mathlib.LinearAlgebra.TensorProduct.Basic

/-!
# Bridge A, step A3 — infinitesimal pure braid relations and flatness for every `n`

Audit `qou-derivation-chain/derivation-chain-audit-2026-11-15.md`, §2.5 (gap G2.2) and §8
step 8. The content block `def:kz-connection-sl2` proves the relations for the `𝔰𝔩₂`
fundamental residues `s_{ij} − ½` in `R[S_n]`, and the equivalence *relations ⇔ flat* at
three points only; its docstring records that the general-`n` bookkeeping "is not
formalised". This file supplies both missing pieces.

## Part I — the relations from invariance of `Ω` (any Lie algebra, any `n`)

`L` is a Lie algebra over a commutative ring `R` and `Ω ∈ L ⊗ L` is **invariant**:
`(ad z ⊗ 1 + 1 ⊗ ad z) Ω = 0` for every `z ∈ L`, i.e. `Ω` commutes with the coproduct
`Δ(z) = z ⊗ 1 + 1 ⊗ z`. `SlotReps` is a family of Lie representations `ρ_i : L → A`,
`i ∈ Fin n`, into one associative algebra `A`, whose images in different slots commute
(the motivating case is `A = End(V₁ ⊗ ⋯ ⊗ Vₙ)` with `ρ_i` acting in factor `i`). Put
`Ω_{ij} = (ρ_i ⊗ ρ_j)(Ω)`. Then (`casimir_isFlat`)

* `[Ω_{ij}, Ω_{kl}] = 0` for `{i, j} ∩ {k, l} = ∅`;
* `[Ω_{ij}, Ω_{ik} + Ω_{jk}] = 0` for `i, j, k` distinct.

The proof is the textbook one and is purely algebraic: `Ω_{ik} + Ω_{jk} = ((ρ_i + ρ_j) ⊗ ρ_k)(Ω)`,
and `Ω_{ij}` commutes with `ρ_i(z) + ρ_j(z)` (that is invariance, `commute_slot_coproduct`)
and with `ρ_k` (disjoint slots). Symmetry of `Ω` is **not** used, and no basis of `L` is
chosen: the argument is by induction on the tensor `Ω`.

## Part II — relations ⇒ zero curvature, for every `n`

For residues `M : Fin n → Fin n → A` with `M i j = M j i`, and the logarithmic forms
`ω_{ij} = d log(z_i − z_j)` (`omegaAt`), the connection form is
`ω = ½ Σ_{i,j} ω_{ij} M_{ij} = Σ_{i<j} ω_{ij} M_{ij}` (the diagonal drops out because
`ω_{ii} = 0`). `curvature_zero_of_isFlat` proves `ω(u)ω(v) − ω(v)ω(u) = 0` at every
configuration with distinct coordinates, for all tangent vectors, from the two relations and
the Arnold relation. With each `ω_{ij}` closed, this is `dω − ω ∧ ω = 0`.

The bookkeeping avoids filtered sums. The double sum over ordered pairs of pairs collapses,
term by term, onto the four "one shared index" patterns (`term_split`), each of which is the
same triple sum `S = Σ_{a,b,c} ω_{ab}(u) ω_{ac}(v) [M_{ab}, M_{ac}]`. That sum is invariant
under the six permutations of `(a, b, c)`, so `6S` is the sum over triples of the
`S₃`-orbit sum, and each orbit sum is the three-point curvature, which the Arnold relation and
the braid relations kill (`orbit_sum_zero`).

Combined with Part I (`casimir_curvature_zero`): **for every Lie algebra, every invariant
`Ω`, every family of slot representations and every `n`, the KZ-type connection
`Σ_{i<j} Ω_{ij} d log(z_i − z_j)` is flat.** This is the algebraic half of Drinfeld–Kohno;
the monodromy half (holonomy = `R`-matrix representation) is not touched here.

Base ring §7c: Part I over any `CommRing R`; Part II over any field `k` of characteristic
zero (division by `z_i − z_j`, and by `6`). Nothing archimedean.

-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987), §1.1.
-- Ref: [drinfeld1991] Drinfeld, Leningrad Math. J. 2 (1991), §2.
-- Ref: [leitner2026] mass-endomorphism/kz-connection-sl2.md (the `n = 3` case).
-/

namespace QOU.Mass.InfinitesimalPureBraid

open TensorProduct

/-- The infinitesimal pure braid relations on a family of residues (the same predicate as
`QOU.Mass.KZConnectionSl2.IsFlatLogConnection`, restated so this library file does not import
a content-block sibling). -/
def IsFlatLogConnection {A : Type*} [Ring A] {n : ℕ} (M : Fin n → Fin n → A) : Prop :=
  (∀ i j k l : Fin n, i ≠ k → i ≠ l → j ≠ k → j ≠ l →
      M i j * M k l = M k l * M i j) ∧
  (∀ i j k : Fin n, i ≠ j → i ≠ k → j ≠ k →
      M i j * (M i k + M j k) = (M i k + M j k) * M i j)

/-! ## Part I -/

section PartI

variable {R : Type*} [CommRing R] {L : Type*} [LieRing L] [LieAlgebra R L]
variable {A : Type*} [Ring A] [Algebra R A]

/-- `(f ⊗ g)(Ω)` read in `A`: the bilinear map `(u, v) ↦ f u * g v` applied to `Ω`. -/
def pairOp (f g : L →ₗ[R] A) : L ⊗[R] L →ₗ[R] A :=
  TensorProduct.lift ((LinearMap.mul R A).compl₁₂ f g)

@[simp] theorem pairOp_tmul (f g : L →ₗ[R] A) (u v : L) : pairOp f g (u ⊗ₜ v) = f u * g v := by
  simp [pairOp]

theorem pairOp_add_left (f f' g : L →ₗ[R] A) (Ω : L ⊗[R] L) :
    pairOp (f + f') g Ω = pairOp f g Ω + pairOp f' g Ω := by
  induction Ω using TensorProduct.induction_on with
  | zero => simp
  | tmul u v => simp [add_mul]
  | add x y hx hy => simp only [map_add, hx, hy]; abel

/-- If `a` commutes with every `f u` and every `g v`, it commutes with `(f ⊗ g)(Ω)`. -/
theorem commute_pairOp {a : A} {f g : L →ₗ[R] A} (hf : ∀ u, Commute a (f u))
    (hg : ∀ v, Commute a (g v)) (Ω : L ⊗[R] L) : Commute a (pairOp f g Ω) := by
  induction Ω using TensorProduct.induction_on with
  | zero => simp
  | tmul u v => simpa using (hf u).mul_right (hg v)
  | add x y hx hy => simpa only [map_add] using hx.add_right hy

/-- The coproduct action of `z` on `L ⊗ L`: `ad z ⊗ 1 + 1 ⊗ ad z`. -/
def adPair (z : L) : L ⊗[R] L →ₗ[R] L ⊗[R] L :=
  TensorProduct.map (LieAlgebra.ad R L z : L →ₗ[R] L) LinearMap.id +
    TensorProduct.map LinearMap.id (LieAlgebra.ad R L z : L →ₗ[R] L)

/-- `Ω` is invariant: it commutes with the coproduct, `(ad z ⊗ 1 + 1 ⊗ ad z) Ω = 0`. -/
def IsInvariant (Ω : L ⊗[R] L) : Prop := ∀ z : L, adPair (R := R) z Ω = 0

/-- Lie representations of `L` in `n` slots of one algebra, commuting across slots. -/
structure SlotReps (R L A : Type*) [CommRing R] [LieRing L] [LieAlgebra R L] [Ring A]
    [Algebra R A] (n : ℕ) where
  /-- The action in slot `i`. -/
  ρ : Fin n → L →ₗ[R] A
  /-- Each `ρ i` is a Lie map into the commutator algebra. -/
  map_lie : ∀ i x y, ρ i ⁅x, y⁆ = ρ i x * ρ i y - ρ i y * ρ i x
  /-- Different slots commute. -/
  slot_comm : ∀ i j, i ≠ j → ∀ x y, Commute (ρ i x) (ρ j y)

namespace SlotReps

variable {n : ℕ} (S : SlotReps R L A n)

/-- The residue `Ω_{ij} = (ρ_i ⊗ ρ_j)(Ω)`. -/
def omega (Ω : L ⊗[R] L) (i j : Fin n) : A := pairOp (S.ρ i) (S.ρ j) Ω

/-- **Invariance in slots `i, j`.** The commutator of `ρ_i z + ρ_j z` with `Ω_{ij}` is the
image of `(ad z ⊗ 1 + 1 ⊗ ad z) Ω`. -/
theorem commutator_slot_coproduct {i j : Fin n} (hij : i ≠ j) (z : L) (Ω : L ⊗[R] L) :
    (S.ρ i z + S.ρ j z) * S.omega Ω i j - S.omega Ω i j * (S.ρ i z + S.ρ j z) =
      pairOp (S.ρ i) (S.ρ j) (adPair z Ω) := by
  unfold omega
  induction Ω using TensorProduct.induction_on with
  | zero => simp
  | tmul u v =>
    have h1 : S.ρ j z * S.ρ i u = S.ρ i u * S.ρ j z := (S.slot_comm j i hij.symm z u).eq
    have h2 : S.ρ j v * S.ρ i z = S.ρ i z * S.ρ j v := (S.slot_comm j i hij.symm v z).eq
    simp only [adPair, LinearMap.add_apply, TensorProduct.map_tmul, LinearMap.id_apply,
      LieAlgebra.ad_apply, map_add, pairOp_tmul, S.map_lie]
    calc (S.ρ i z + S.ρ j z) * (S.ρ i u * S.ρ j v) - S.ρ i u * S.ρ j v * (S.ρ i z + S.ρ j z)
        = S.ρ i z * S.ρ i u * S.ρ j v + (S.ρ j z * S.ρ i u) * S.ρ j v
            - S.ρ i u * (S.ρ j v * S.ρ i z) - S.ρ i u * S.ρ j v * S.ρ j z := by noncomm_ring
      _ = _ := by rw [h1, h2]; noncomm_ring
  | add x y hx hy =>
    simp only [map_add, mul_add, add_mul] at hx hy ⊢
    rw [← hx, ← hy]; noncomm_ring

/-- With `Ω` invariant, `Ω_{ij}` commutes with the coproduct image `ρ_i z + ρ_j z`. -/
theorem commute_slot_coproduct {Ω : L ⊗[R] L} (hΩ : IsInvariant Ω) {i j : Fin n} (hij : i ≠ j)
    (z : L) : Commute (S.omega Ω i j) (S.ρ i z + S.ρ j z) := by
  have h := S.commutator_slot_coproduct hij z Ω
  rw [hΩ z, map_zero, sub_eq_zero] at h
  exact h.symm

/-- `Ω_{ij}` commutes with anything acting only in a third slot. -/
theorem commute_third_slot (Ω : L ⊗[R] L) {i j k : Fin n} (hik : i ≠ k) (hjk : j ≠ k) (w : L) :
    Commute (S.omega Ω i j) (S.ρ k w) :=
  (commute_pairOp (fun u => (S.slot_comm k i hik.symm w u))
    (fun v => (S.slot_comm k j hjk.symm w v)) Ω).symm

/-- **The infinitesimal pure braid relations for every `n`**, from invariance of `Ω` alone. -/
theorem casimir_isFlat {Ω : L ⊗[R] L} (hΩ : IsInvariant Ω) : IsFlatLogConnection (S.omega Ω) := by
  refine ⟨fun i j k l hik hil hjk hjl => ?_, fun i j k hij hik hjk => ?_⟩
  · -- disjoint slots
    exact (commute_pairOp (fun u => S.commute_third_slot Ω hik hjk u)
      (fun v => S.commute_third_slot Ω hil hjl v) Ω).eq
  · have hsum : S.omega Ω i k + S.omega Ω j k = pairOp (S.ρ i + S.ρ j) (S.ρ k) Ω := by
      simp only [omega, pairOp_add_left]
    rw [hsum]
    exact (commute_pairOp (fun u => S.commute_slot_coproduct hΩ hij u)
      (fun v => S.commute_third_slot Ω hik hjk v) Ω).eq

end SlotReps

end PartI

/-! ## Part II -/

section PartII

variable {k : Type*} [Field k] {A : Type*} [Ring A] [Algebra k A] {n : ℕ}

/-- `d log(z_i − z_j)` at `z`, on the tangent vector `u`. On the diagonal it is `0`. -/
def omegaAt (z u : Fin n → k) (i j : Fin n) : k := (u i - u j) / (z i - z j)

theorem omegaAt_symm (z u : Fin n → k) (i j : Fin n) : omegaAt z u j i = omegaAt z u i j := by
  unfold omegaAt; rw [← neg_sub (u i), ← neg_sub (z i), neg_div_neg_eq]

@[simp] theorem omegaAt_self (z u : Fin n → k) (i : Fin n) : omegaAt z u i i = 0 := by
  simp [omegaAt]

/-- The connection form `ω(u) = ½ Σ_{i,j} ω_{ij}(u) M_{ij}` (`= Σ_{i<j}` for symmetric `M`). -/
def connForm (M : Fin n → Fin n → A) (z u : Fin n → k) : A :=
  ∑ p : Fin n × Fin n, ((2 : k)⁻¹ * omegaAt z u p.1 p.2) • M p.1 p.2

/-- The quadratic part of the curvature, `(ω ∧ ω)(u, v) = ω(u)ω(v) − ω(v)ω(u)`. -/
def omegaWedgeOmega (M : Fin n → Fin n → A) (z u v : Fin n → k) : A :=
  connForm M z u * connForm M z v - connForm M z v * connForm M z u

/-- One term of `ω ∧ ω`: `ω_{ij}(u) ω_{lm}(v) [M_{ij}, M_{lm}]`. -/
def term (M : Fin n → Fin n → A) (z u v : Fin n → k) (i j l m : Fin n) : A :=
  (omegaAt z u i j * omegaAt z v l m) • (M i j * M l m - M l m * M i j)

theorem omegaWedgeOmega_eq_sum (M : Fin n → Fin n → A) (z u v : Fin n → k) :
    omegaWedgeOmega M z u v =
      (4 : k)⁻¹ • ∑ p : Fin n × Fin n, ∑ p' : Fin n × Fin n, term M z u v p.1 p.2 p'.1 p'.2 := by
  unfold omegaWedgeOmega connForm term
  rw [Finset.sum_mul_sum, Finset.sum_mul_sum]
  conv_lhs => arg 2; rw [Finset.sum_comm]
  rw [← Finset.sum_sub_distrib, Finset.smul_sum]
  refine Finset.sum_congr rfl fun p _ => ?_
  rw [← Finset.sum_sub_distrib, Finset.smul_sum]
  refine Finset.sum_congr rfl fun p' _ => ?_
  simp only [smul_mul_smul_comm, smul_sub, smul_smul]
  have h4 : (4 : k)⁻¹ = 2⁻¹ * 2⁻¹ := by rw [← mul_inv]; norm_num
  rw [h4]
  congr 1 <;> congr 1 <;> ring

variable (M : Fin n → Fin n → A) (z u v : Fin n → k)

/-- The triple summand `f(a, b, c) = ω_{ab}(u) ω_{ac}(v) [M_{ab}, M_{ac}]`. -/
def tri (a b c : Fin n) : A := term M z u v a b a c

section Split

variable {M}
variable (hsym : ∀ i j, M i j = M j i) (hM : IsFlatLogConnection M)
include hsym hM

/-- **Term split.** Each term of `ω ∧ ω` equals the sum of its four "shared index" parts:
disjoint pairs vanish by the first relation, and a pair of pairs sharing both indices gives a
zero commutator. -/
theorem term_split (i j l m : Fin n) :
    term M z u v i j l m =
      (if i = l then term M z u v i j l m else 0) + (if i = m then term M z u v i j l m else 0) +
      (if j = l then term M z u v i j l m else 0) + (if j = m then term M z u v i j l m else 0) := by
  by_cases hij : i = j
  · subst hij; simp [term]
  by_cases hlm : l = m
  · subst hlm; simp [term]
  have hsame : i = l → j = m → term M z u v i j l m = 0 := by
    intro h h'; rw [term, ← h, ← h', sub_self, smul_zero]
  have hswap : i = m → j = l → term M z u v i j l m = 0 := by
    intro h h'; rw [term, ← h, ← h', hsym j i, sub_self, smul_zero]
  split_ifs with h1 h2 h3 h4 h4 h3 h4 h4 h2 h3 h4 h4 h3 h4 h4
  all_goals first
    | (exfalso; subst_vars; contradiction)
    | (rw [hsame ‹_› ‹_›]; simp)
    | (rw [hswap ‹_› ‹_›]; simp)
    | (unfold term; rw [hM.1 i j l m ‹_› ‹_› ‹_› ‹_›, sub_self, smul_zero]; simp)
    | simp

/-- `ω ∧ ω` is the triple sum `Σ_{a,b,c} ω_{ab}(u) ω_{ac}(v) [M_{ab}, M_{ac}]`. -/
theorem omegaWedgeOmega_eq_tri [CharZero k] :
    omegaWedgeOmega M z u v = ∑ a, ∑ b, ∑ c, tri M z u v a b c := by
  rw [omegaWedgeOmega_eq_sum]
  have hsplit : ∀ p p' : Fin n × Fin n, term M z u v p.1 p.2 p'.1 p'.2 = _ :=
    fun p p' => term_split z u v hsym hM p.1 p.2 p'.1 p'.2
  rw [Finset.sum_congr rfl fun p _ => Finset.sum_congr rfl fun p' _ => hsplit p p']
  simp only [Finset.sum_add_distrib]
  simp only [Fintype.sum_prod_type]
  -- the four shared-index sums, each equal to the triple sum
  have e1 : ∑ i, ∑ j, ∑ l, ∑ m, (if i = l then term M z u v i j l m else 0) =
      ∑ a, ∑ b, ∑ c, tri M z u v a b c := by
    refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ => ?_
    rw [Finset.sum_comm]
    simp [tri]
  have e2 : ∑ i, ∑ j, ∑ l, ∑ m, (if i = m then term M z u v i j l m else 0) =
      ∑ a, ∑ b, ∑ c, tri M z u v a b c := by
    refine Finset.sum_congr rfl fun i _ => Finset.sum_congr rfl fun j _ =>
      Finset.sum_congr rfl fun l _ => ?_
    simp only [Finset.sum_ite_eq, Finset.mem_univ, if_true, tri, term]
    rw [omegaAt_symm z v l i, hsym l i]
  have e3 : ∑ i, ∑ j, ∑ l, ∑ m, (if j = l then term M z u v i j l m else 0) =
      ∑ a, ∑ b, ∑ c, tri M z u v a b c := by
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun j _ => Finset.sum_congr rfl fun i _ => ?_
    rw [Finset.sum_comm]
    simp only [Finset.sum_ite_eq, Finset.mem_univ, if_true, tri, term]
    refine Finset.sum_congr rfl fun m _ => ?_
    rw [omegaAt_symm z u i j, hsym i j]
  have e4 : ∑ i, ∑ j, ∑ l, ∑ m, (if j = m then term M z u v i j l m else 0) =
      ∑ a, ∑ b, ∑ c, tri M z u v a b c := by
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun j _ => Finset.sum_congr rfl fun i _ =>
      Finset.sum_congr rfl fun l _ => ?_
    simp only [Finset.sum_ite_eq, Finset.mem_univ, if_true, tri, term]
    rw [omegaAt_symm z u i j, omegaAt_symm z v l j, hsym i j, hsym l j]
  rw [e1, e2, e3, e4]
  set S := ∑ a, ∑ b, ∑ c, tri M z u v a b c
  rw [show S + S + S + S = (4 : k) • S by module, smul_smul,
    inv_mul_cancel₀ (by norm_num : (4 : k) ≠ 0), one_smul]

end Split

/-- **Arnold relation** at a configuration with `z_a, z_b, z_c` distinct. -/
theorem arnold {a b c : Fin n} (hab : z a ≠ z b) (hac : z a ≠ z c) (hbc : z b ≠ z c) :
    (omegaAt z u a b * omegaAt z v a c - omegaAt z v a b * omegaAt z u a c)
      - (omegaAt z u a b * omegaAt z v b c - omegaAt z v a b * omegaAt z u b c)
      + (omegaAt z u a c * omegaAt z v b c - omegaAt z v a c * omegaAt z u b c) = 0 := by
  have h1 : z a - z b ≠ 0 := sub_ne_zero.2 hab
  have h2 : z a - z c ≠ 0 := sub_ne_zero.2 hac
  have h3 : z b - z c ≠ 0 := sub_ne_zero.2 hbc
  unfold omegaAt
  field_simp
  ring

/-- The `S₃`-orbit of a triple summand: the three-point curvature. -/
def orbit (a b c : Fin n) : A :=
  tri M z u v a b c + tri M z u v a c b + tri M z u v b a c + tri M z u v b c a +
    tri M z u v c a b + tri M z u v c b a

variable {M}

/-- **The three-point curvature vanishes** for every triple, given the relations, symmetric
residues and distinct coordinates. -/
theorem orbit_zero (hsym : ∀ i j, M i j = M j i) (hM : IsFlatLogConnection M)
    (hz : Function.Injective z) (a b c : Fin n) : orbit M z u v a b c = 0 := by
  by_cases hab : a = b
  · subst hab; simp [orbit, tri, term, hsym]
  by_cases hac : a = c
  · subst hac; simp [orbit, tri, term, hsym]
  by_cases hbc : b = c
  · subst hbc; simp [orbit, tri, term, hsym]
  set X := M a b
  set Y := M a c
  set Z := M b c
  have r1 := hM.2 a b c hab hac hbc
  have r2 := hM.2 a c b hac hab (Ne.symm hbc)
  rw [show M c b = Z from hsym c b] at r2
  -- [X, Z] = -[X, Y] and [Y, Z] = [X, Y]
  have hXZ : X * Z - Z * X = -(X * Y - Y * X) := by
    rw [mul_add, add_mul] at r1; rw [eq_neg_iff_add_eq_zero]
    calc X * Z - Z * X + (X * Y - Y * X) = (X * Y + X * Z) - (Y * X + Z * X) := by abel
      _ = 0 := by rw [r1, sub_self]
  have hYZ : Y * Z - Z * Y = X * Y - Y * X := by
    rw [mul_add, add_mul] at r2
    rw [← sub_eq_zero]
    calc Y * Z - Z * Y - (X * Y - Y * X) = (Y * X + Y * Z) - (X * Y + Z * Y) := by abel
      _ = 0 := by rw [r2, sub_self]
  have hA := arnold z u v (hz.ne hab) (hz.ne hac) (hz.ne hbc)
  have expand0 : orbit M z u v a b c =
      (omegaAt z u a b * omegaAt z v a c - omegaAt z v a b * omegaAt z u a c) • (X * Y - Y * X)
      + (omegaAt z u a b * omegaAt z v b c - omegaAt z v a b * omegaAt z u b c) • (X * Z - Z * X)
      + (omegaAt z u a c * omegaAt z v b c - omegaAt z v a c * omegaAt z u b c) •
          (Y * Z - Z * Y) := by
    unfold orbit tri term
    rw [omegaAt_symm z u a b, omegaAt_symm z v a b, omegaAt_symm z u a c, omegaAt_symm z v a c,
      omegaAt_symm z u b c, omegaAt_symm z v b c, hsym b a, hsym c a, hsym c b]
    module
  have expand : orbit M z u v a b c =
      ((omegaAt z u a b * omegaAt z v a c - omegaAt z v a b * omegaAt z u a c)
        - (omegaAt z u a b * omegaAt z v b c - omegaAt z v a b * omegaAt z u b c)
        + (omegaAt z u a c * omegaAt z v b c - omegaAt z v a c * omegaAt z u b c)) •
      (X * Y - Y * X) := by
    rw [expand0, hXZ, hYZ]; module
  rw [expand, hA, zero_smul]

/-- **Flatness for every `n`.** For symmetric residues satisfying the infinitesimal pure
braid relations, `(ω ∧ ω)(u, v) = 0` at every configuration of distinct points, for all
tangent vectors `u, v`. -/
theorem curvature_zero_of_isFlat [CharZero k] (hsym : ∀ i j, M i j = M j i)
    (hM : IsFlatLogConnection M) (hz : Function.Injective z) :
    omegaWedgeOmega M z u v = 0 := by
  rw [omegaWedgeOmega_eq_tri z u v hsym hM]
  set S := ∑ a, ∑ b, ∑ c, tri M z u v a b c with hS
  -- `S` is invariant under the six coordinate permutations
  have sw12 : ∀ g : Fin n → Fin n → Fin n → A,
      ∑ a, ∑ b, ∑ c, g b a c = ∑ a, ∑ b, ∑ c, g a b c := fun g => Finset.sum_comm
  have sw23 : ∀ g : Fin n → Fin n → Fin n → A,
      ∑ a, ∑ b, ∑ c, g a c b = ∑ a, ∑ b, ∑ c, g a b c :=
    fun g => Finset.sum_congr rfl fun a _ => Finset.sum_comm
  have p1 : ∑ a, ∑ b, ∑ c, tri M z u v a c b = S := sw23 (tri M z u v)
  have p2 : ∑ a, ∑ b, ∑ c, tri M z u v b a c = S := sw12 (tri M z u v)
  have p3 : ∑ a, ∑ b, ∑ c, tri M z u v b c a = S :=
    (sw12 fun x y w => tri M z u v x w y).trans p1
  have p4 : ∑ a, ∑ b, ∑ c, tri M z u v c a b = S :=
    (sw23 fun x y w => tri M z u v y x w).trans p2
  have p5 : ∑ a, ∑ b, ∑ c, tri M z u v c b a = S :=
    (sw23 fun x y w => tri M z u v y w x).trans p3
  have h6 : (6 : k) • S = 0 := by
    have : ∑ a, ∑ b, ∑ c, orbit M z u v a b c = 0 := by
      simp [orbit_zero z u v hsym hM hz]
    simp only [orbit, Finset.sum_add_distrib, p1, p2, p3, p4, p5] at this
    rw [← this]; module
  have h6' : (6 : k) ≠ 0 := by norm_num
  exact (smul_eq_zero.1 h6).resolve_left h6'

/-! ### The Euler (radial) direction, for Bridge B

Along the Euler field `E = Σ z_i ∂_i` (tangent vector `u = z`) every `ω_{ij}` with `i ≠ j`
equals `1`, so `ι_E ω = Σ_{i<j} M_{ij}` is a **constant** element of `A`. Flatness then makes
it commute with `ω(u)` for every tangent vector `u`: the radial component of the connection
splits off as a central (parallel) term. Over `ℂ` the rotation field `i·E` (the Reeb field of
the link of the configuration space) gives `ι_{iE} ω = i·Σ_{i<j} M_{ij}` by linearity in the
tangent vector (`connForm_smul`). Translations `Σ ∂_i` contract to `0` (`connForm_translation`).
-/

theorem omegaAt_euler (z : Fin n → k) (hz : Function.Injective z) (i j : Fin n) :
    omegaAt z z i j = if i = j then 0 else 1 := by
  split_ifs with h
  · subst h; simp
  · exact div_self (sub_ne_zero.2 (hz.ne h))

theorem connForm_smul (M : Fin n → Fin n → A) (z u : Fin n → k) (c : k) :
    connForm M z (c • u) = c • connForm M z u := by
  unfold connForm omegaAt
  rw [Finset.smul_sum]
  refine Finset.sum_congr rfl fun p _ => ?_
  rw [smul_smul]; congr 1
  simp only [Pi.smul_apply, smul_eq_mul]; ring

theorem connForm_translation (M : Fin n → Fin n → A) (z : Fin n → k) :
    connForm M z (fun _ => 1) = 0 := by
  simp [connForm, omegaAt]

/-- `ι_E ω = ½ Σ_{i ≠ j} M_{ij}`, independent of the point `z`. -/
theorem connForm_euler (M : Fin n → Fin n → A) (z : Fin n → k) (hz : Function.Injective z) :
    connForm M z z = ∑ p : Fin n × Fin n, (if p.1 = p.2 then (0 : k) else 2⁻¹) • M p.1 p.2 := by
  unfold connForm
  refine Finset.sum_congr rfl fun p _ => ?_
  rw [omegaAt_euler z hz]; split_ifs <;> simp

/-- **The radial component is central for the connection.** For a flat logarithmic
connection, `ι_E ω` commutes with `ω(u)` for every tangent vector `u`. -/
theorem euler_commute [CharZero k] {M : Fin n → Fin n → A} (hsym : ∀ i j, M i j = M j i)
    (hM : IsFlatLogConnection M) (z : Fin n → k) (hz : Function.Injective z) (u : Fin n → k) :
    Commute (connForm M z u) (connForm M z z) :=
  sub_eq_zero.1 (curvature_zero_of_isFlat z u z hsym hM hz)

end PartII

/-! ## Part I + Part II -/

/-- **Every KZ-type connection is flat, for every `n`.** For a Lie algebra `L` over a field `k`
of characteristic zero, an invariant symmetric `Ω ∈ L ⊗ L`, and slot representations `ρ`, the
connection `ω = Σ_{i<j} Ω_{ij} d log(z_i − z_j)` has `ω ∧ ω = 0` on the configuration space. -/
theorem casimir_curvature_zero {k : Type*} [Field k] [CharZero k] {L : Type*} [LieRing L]
    [LieAlgebra k L] {A : Type*} [Ring A] [Algebra k A] {n : ℕ} (S : SlotReps k L A n)
    {Ω : L ⊗[k] L} (hΩ : IsInvariant Ω) (hsym : ∀ i j, S.omega Ω i j = S.omega Ω j i)
    (z : Fin n → k) (hz : Function.Injective z) (u v : Fin n → k) :
    omegaWedgeOmega (S.omega Ω) z u v = 0 :=
  curvature_zero_of_isFlat z u v hsym (S.casimir_isFlat hΩ) hz

/-! ## The `𝔰𝔩₂` KZ residues, every `n`

The residues of the content block `def:kz-connection-sl2` are `s_{ij} − ½` in `k[S_n]`
(on `ℂ² ⊗ ℂ²` the split Casimir is the flip minus `½`). Their relations are
`QOU.Mass.KZConnectionSl2.kz_isFlat`; that file is a content-block sibling, not a library
module, so the two transposition identities are repeated here. With Part II this is the
general-`n` flatness the block's docstring leaves unformalised. Any representation of `S_n`
(in particular `S_n → End(V^{⊗n})` permuting factors) is an algebra map out of `k[S_n]` and
carries the zero curvature with it. -/

section KZsl2

open Equiv

variable {k : Type*} [Field k] {n : ℕ}

/-- The `𝔰𝔩₂` KZ residue `s_{ij} − ½` in `k[S_n]`. -/
noncomputable def kzResidue (i j : Fin n) : MonoidAlgebra k (Perm (Fin n)) :=
  MonoidAlgebra.of k (Perm (Fin n)) (swap i j) - algebraMap k _ (2⁻¹ : k)

private lemma swap_mul_swap_eq {i j l : Fin n} (hil : i ≠ l) (hjl : j ≠ l) :
    swap i j * swap i l = swap j l * swap i j := by
  have h := swap_apply_apply (swap i j) i l
  rw [swap_apply_left, swap_apply_of_ne_of_ne hil.symm hjl.symm] at h
  rw [h, swap_inv, mul_assoc, mul_assoc, swap_mul_self, mul_one]

private lemma swap_mul_swap_eq' {i j l : Fin n} (hil : i ≠ l) (hjl : j ≠ l) :
    swap i j * swap j l = swap i l * swap i j := by
  have h := swap_apply_apply (swap i j) j l
  rw [swap_apply_right, swap_apply_of_ne_of_ne hil.symm hjl.symm] at h
  rw [h, swap_inv, mul_assoc, mul_assoc, swap_mul_self, mul_one]

private lemma swap_comm_disj {i j l m : Fin n} (hil : i ≠ l) (him : i ≠ m) (hjl : j ≠ l)
    (hjm : j ≠ m) : swap i j * swap l m = swap l m * swap i j := by
  have h := swap_apply_apply (swap i j) l m
  rw [swap_apply_of_ne_of_ne hil.symm hjl.symm, swap_apply_of_ne_of_ne him.symm hjm.symm] at h
  conv_rhs => rw [h]
  rw [swap_inv, mul_assoc, mul_assoc, swap_mul_self, mul_one]

private lemma commute_sub_central {X Y : MonoidAlgebra k (Perm (Fin n))} (h : Commute X Y)
    (a b : k) : Commute (X - algebraMap k _ a) (Y - algebraMap k _ b) :=
  (h.sub_right (Algebra.commute_algebraMap_right b X)).sub_left
    ((Algebra.commute_algebraMap_left a Y).sub_right (Algebra.commute_algebraMap_left a _))

theorem kzResidue_symm (i j : Fin n) : kzResidue (k := k) i j = kzResidue j i := by
  simp [kzResidue, swap_comm]

/-- The `𝔰𝔩₂` KZ residues satisfy the infinitesimal pure braid relations, every `n`. -/
theorem kzResidue_isFlat : IsFlatLogConnection (kzResidue (k := k) (n := n)) := by
  refine ⟨fun i j l m hil him hjl hjm => ?_, fun i j l hij hil hjl => ?_⟩
  · refine (commute_sub_central ?_ _ _).eq
    rw [Commute, SemiconjBy, ← map_mul, ← map_mul, swap_comm_disj hil him hjl hjm]
  · have hsum : kzResidue (k := k) i l + kzResidue j l =
        (MonoidAlgebra.of k (Perm (Fin n)) (swap i l) + MonoidAlgebra.of k (Perm (Fin n)) (swap j l)) - algebraMap k _ (2⁻¹ + 2⁻¹ : k) := by
      simp only [kzResidue, map_add]; abel
    rw [hsum]
    refine (commute_sub_central ?_ _ _).eq
    rw [Commute, SemiconjBy, mul_add, add_mul, ← map_mul, ← map_mul, ← map_mul, ← map_mul,
      swap_mul_swap_eq hil hjl, swap_mul_swap_eq' hil hjl, add_comm]

/-- **The `𝔰𝔩₂` KZ connection is flat on `n` points, for every `n`.** -/
theorem kz_sl2_curvature_zero [CharZero k] (z : Fin n → k) (hz : Function.Injective z) (u v : Fin n → k) :
    omegaWedgeOmega (kzResidue (k := k) (n := n)) z u v = 0 :=
  curvature_zero_of_isFlat z u v kzResidue_symm kzResidue_isFlat hz

end KZsl2

end QOU.Mass.InfinitesimalPureBraid
