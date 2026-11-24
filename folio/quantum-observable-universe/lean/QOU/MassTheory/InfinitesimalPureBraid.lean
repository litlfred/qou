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

Part III proves the converse for every `n` (`isFlat_of_curvature_zero`), so flatness and the
relations are equivalent (`curvature_zero_iff_isFlat`).

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
    connForm M z (fun _ : Fin n => (1 : k)) = 0 := by
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

/-! ### The transverse part

`ω` is additive in the tangent vector, kills translations, and is homogeneous of degree `−1`
in the base point. So on the quotient of the tangent space by `span{T, E}` (translations and
the Euler field) the transverse part `ω(u) mod k·ι_E ω` is well defined: shifting `u` by
`a·E + b·T` shifts `ω(u)` by `a·ι_E ω` only (`connForm_add_euler_translation`). -/

theorem connForm_add (M : Fin n → Fin n → A) (z u w : Fin n → k) :
    connForm M z (u + w) = connForm M z u + connForm M z w := by
  unfold connForm omegaAt
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun p _ => ?_
  rw [← add_smul]; congr 1
  simp only [Pi.add_apply]; ring

theorem connForm_add_euler_translation (M : Fin n → Fin n → A) (z u : Fin n → k) (a b : k) :
    connForm M z (u + a • z + b • (fun _ : Fin n => (1 : k))) =
      connForm M z u + a • connForm M z z := by
  rw [connForm_add, connForm_add, connForm_smul, connForm_smul, connForm_translation, smul_zero,
    add_zero]

/-- Homogeneity: `ω` at the dilated point `c·z` is `c⁻¹ ω` at `z`. -/
theorem connForm_dilate (M : Fin n → Fin n → A) (z u : Fin n → k) (c : k) :
    connForm M (c • z) u = c⁻¹ • connForm M z u := by
  unfold connForm omegaAt
  rw [Finset.smul_sum]
  refine Finset.sum_congr rfl fun p _ => ?_
  rw [smul_smul]; congr 1
  simp only [Pi.smul_apply, smul_eq_mul, div_eq_mul_inv]
  rw [← mul_sub, mul_inv]; ring

/-- Translation invariance in the base point. -/
theorem connForm_shift (M : Fin n → Fin n → A) (z u : Fin n → k) (b : k) :
    connForm M (z + b • (fun _ : Fin n => (1 : k))) u = connForm M z u := by
  simp [connForm, omegaAt]

end PartII

/-! ## Part III — zero curvature ⇒ relations, for every `n`

The converse of Part II, so that flatness and the relations are **equivalent** for every `n`
(the content block proves this at `n = 3` only). The argument is purely algebraic: `ω(e_i)` is
the residue sum `Σ_b (z_i − z_b)⁻¹ M_{ib}` (`connForm_single`), and moving a single point `z_m`
turns `[ω(e_i), ω(e_j)] = 0` into a rational function of one variable with simple poles. Clearing
denominators and Lagrange interpolation at three fresh points (`pole_two`; `pole_one` for one
pole) isolates each pole coefficient. The pole at `z_m = z_i` gives `first_residue`; moving a
fourth point `z_{m'}` inside it gives `disjoint_commute`; and with those, `first_residue`
collapses to `[M_{ab}, M_{ac} + M_{bc}] = 0`. Configurations are sampled at `i ↦ (i : k)` and its
one-point updates, so only `CharZero k` (for an infinite supply of fresh points) is used. No
limits, no analysis.
-/

section Converse

variable {k : Type*} [Field k] {A : Type*} [Ring A] [Algebra k A] {n : ℕ}

/-- A function of `s` of the form `K₀ + (a − s)⁻¹ K₁` vanishing at two distinct points
has `K₁ = 0`. -/
theorem pole_one {a s₁ s₂ : k} {K₀ K₁ : A} (h12 : s₁ ≠ s₂)
    (e1 : K₀ + (a - s₁)⁻¹ • K₁ = 0) (e2 : K₀ + (a - s₂)⁻¹ • K₁ = 0) : K₁ = 0 := by
  have hd : (a - s₁)⁻¹ - (a - s₂)⁻¹ ≠ 0 := by
    rw [sub_ne_zero]; intro h
    exact h12 (by have := inv_injective h; linear_combination -this)
  have : ((a - s₁)⁻¹ - (a - s₂)⁻¹) • K₁ = 0 := by
    rw [sub_smul]; linear_combination (norm := module) e1 - e2
  exact (smul_eq_zero.1 this).resolve_left hd

/-- A function of `s` of the form `K₀ + (a − s)⁻¹ K₁ + (b − s)⁻¹ K₂`, `a ≠ b`, vanishing at
three distinct points off `{a, b}` has `K₁ = 0`. -/
theorem pole_two {a b s₁ s₂ s₃ : k} {K₀ K₁ K₂ : A} (hab : a ≠ b) (h12 : s₁ ≠ s₂) (h13 : s₁ ≠ s₃)
    (h23 : s₂ ≠ s₃) (h1a : s₁ ≠ a) (h2a : s₂ ≠ a) (h3a : s₃ ≠ a) (h1b : s₁ ≠ b) (h2b : s₂ ≠ b)
    (h3b : s₃ ≠ b)
    (e1 : K₀ + (a - s₁)⁻¹ • K₁ + (b - s₁)⁻¹ • K₂ = 0)
    (e2 : K₀ + (a - s₂)⁻¹ • K₁ + (b - s₂)⁻¹ • K₂ = 0)
    (e3 : K₀ + (a - s₃)⁻¹ • K₁ + (b - s₃)⁻¹ • K₂ = 0) : K₁ = 0 := by
  -- clear denominators: q(s) = (a−s)(b−s)K₀ + (b−s)K₁ + (a−s)K₂ vanishes at s₁, s₂, s₃
  have q : ∀ s : k, s ≠ a → s ≠ b → K₀ + (a - s)⁻¹ • K₁ + (b - s)⁻¹ • K₂ = 0 →
      ((a - s) * (b - s)) • K₀ + (b - s) • K₁ + (a - s) • K₂ = 0 := by
    intro s hsa hsb e
    have ha : a - s ≠ 0 := sub_ne_zero.2 (Ne.symm hsa)
    have hb : b - s ≠ 0 := sub_ne_zero.2 (Ne.symm hsb)
    have := congrArg (fun x => ((a - s) * (b - s)) • x) e
    simp only [smul_add, smul_smul, smul_zero] at this
    rw [← this]
    congr 2
    · field_simp
    · field_simp
  have q1 := q _ h1a h1b e1
  have q2 := q _ h2a h2b e2
  have q3 := q _ h3a h3b e3
  -- Lagrange: D · q(a) = Σ N_r(a) q(s_r), and q(a) = (b − a) K₁
  have key : ((s₁ - s₂) * (s₁ - s₃) * (s₂ - s₃) * (b - a)) • K₁ = 0 := by
    linear_combination (norm := module)
      ((a - s₂) * (a - s₃) * (s₂ - s₃)) • q1 - ((a - s₁) * (a - s₃) * (s₁ - s₃)) • q2 +
        ((a - s₁) * (a - s₂) * (s₁ - s₂)) • q3
  have hD : (s₁ - s₂) * (s₁ - s₃) * (s₂ - s₃) * (b - a) ≠ 0 := by
    exact mul_ne_zero (mul_ne_zero (mul_ne_zero (sub_ne_zero.2 h12) (sub_ne_zero.2 h13))
      (sub_ne_zero.2 h23)) (sub_ne_zero.2 (Ne.symm hab))
  exact (smul_eq_zero.1 key).resolve_left hD

/-- `ω(e_a) = Σ_b (z_a − z_b)⁻¹ M_{ab}`: the residue sum at the point `a`. -/
def resid (M : Fin n → Fin n → A) (z : Fin n → k) (a : Fin n) : A := ∑ b, (z a - z b)⁻¹ • M a b

theorem connForm_single [CharZero k] {M : Fin n → Fin n → A} (hsym : ∀ i j, M i j = M j i) (z : Fin n → k)
    (a : Fin n) : connForm M z (Pi.single a 1) = resid M z a := by
  unfold connForm resid omegaAt
  rw [Fintype.sum_prod_type]
  simp only [Pi.single_apply, sub_div, mul_sub, sub_smul, Finset.sum_sub_distrib, ite_div,
    zero_div, mul_ite, mul_zero, ite_smul, zero_smul, one_div, Finset.sum_ite_eq',
    Finset.mem_univ, if_true]
  rw [Finset.sum_eq_single a (fun b _ hb => by simp [hb]) (by simp)]
  simp only [if_true, ← Finset.sum_sub_distrib]
  refine Finset.sum_congr rfl fun b _ => ?_
  rw [hsym b a, ← neg_sub (z a) (z b), inv_neg, mul_neg, neg_smul, sub_neg_eq_add, ← add_smul]
  congr 1; rw [← add_mul, ← two_mul, mul_inv_cancel₀ two_ne_zero, one_mul]

theorem sum_split (f : Fin n → A) (m : Fin n) :
    ∑ b, f b = f m + ∑ b, if b = m then 0 else f b := by
  have : ∀ b, f b = (if b = m then f b else 0) + (if b = m then 0 else f b) := by
    intro b; split_ifs <;> simp
  conv_lhs => rw [Finset.sum_congr rfl fun b _ => this b]
  rw [Finset.sum_add_distrib, Finset.sum_ite_eq']; simp

omit [Field k] in
theorem update_injective [DecidableEq k] {z : Fin n → k} (hz : Function.Injective z) {s : k}
    (hs : s ∉ Finset.univ.image z) (m : Fin n) : Function.Injective (Function.update z m s) := by
  have hne : ∀ b, z b ≠ s := fun b hb => hs (Finset.mem_image.2 ⟨b, Finset.mem_univ _, hb⟩)
  intro a b h
  by_cases ha : a = m <;> by_cases hb : b = m
  · rw [ha, hb]
  · rw [ha, Function.update_self, Function.update_of_ne hb] at h; exact absurd h.symm (hne b)
  · rw [hb, Function.update_self, Function.update_of_ne ha] at h; exact absurd h (hne a)
  · rw [Function.update_of_ne ha, Function.update_of_ne hb] at h; exact hz h

/-- `ω(e_a)` with the term at `m` removed. -/
def residOff (M : Fin n → Fin n → A) (z : Fin n → k) (a m : Fin n) : A :=
  ∑ b, (if b = m then (0 : k) else (z a - z b)⁻¹) • M a b

theorem resid_update {M : Fin n → Fin n → A} (z : Fin n → k) {a m : Fin n} (ham : a ≠ m)
    (s : k) : resid M (Function.update z m s) a = residOff M z a m + (z a - s)⁻¹ • M a m := by
  unfold resid residOff
  rw [sum_split _ m, add_comm, Function.update_self, Function.update_of_ne ham]
  congr 1
  refine Finset.sum_congr rfl fun b _ => ?_
  split_ifs with hb
  · simp
  · rw [Function.update_of_ne hb]

/-- **First residue.** If `[ω(e_i), ω(e_j)] = 0` on all of configuration space, then for every
`m ∉ {i, j}` the coefficient of the pole at `z_m = z_i` vanishes:
`[M_{im}, ω(e_j) − (pole at m)] + (z_j − z_i)⁻¹ [M_{im}, M_{jm}] = 0`. -/
theorem first_residue [CharZero k] [DecidableEq k] {M : Fin n → Fin n → A}
    (hR : ∀ z : Fin n → k, Function.Injective z → ∀ a b,
      resid M z a * resid M z b = resid M z b * resid M z a)
    {i j m : Fin n} (hij : i ≠ j) (him : i ≠ m) (hjm : j ≠ m) (z : Fin n → k)
    (hz : Function.Injective z) :
    M i m * residOff M z j m - residOff M z j m * M i m +
      (z j - z i)⁻¹ • (M i m * M j m - M j m * M i m) = 0 := by
  set Xi := residOff M z i m
  set Xj := residOff M z j m
  set P := M i m
  set Q := M j m
  have zij : z i ≠ z j := hz.ne hij
  -- the identity at a fresh value `s` of `z_m`
  have hs : ∀ s : k, s ∉ Finset.univ.image z →
      (Xi * Xj - Xj * Xi) + (z i - s)⁻¹ • (P * Xj - Xj * P +
        (z j - z i)⁻¹ • (P * Q - Q * P)) +
        (z j - s)⁻¹ • (Xi * Q - Q * Xi - (z j - z i)⁻¹ • (P * Q - Q * P)) = 0 := by
    intro s hsT
    have hne : ∀ b, z b ≠ s := fun b hb => hsT (Finset.mem_image.2 ⟨b, Finset.mem_univ _, hb⟩)
    have h := hR _ (update_injective hz hsT m) i j
    rw [resid_update z him, resid_update z hjm, ← sub_eq_zero] at h
    have hαβ : (z i - s)⁻¹ * (z j - s)⁻¹ =
        (z j - z i)⁻¹ * (z i - s)⁻¹ - (z j - z i)⁻¹ * (z j - s)⁻¹ := by
      have h1 : z i - s ≠ 0 := sub_ne_zero.2 (hne i)
      have h2 : z j - s ≠ 0 := sub_ne_zero.2 (hne j)
      have h3 : z j - z i ≠ 0 := sub_ne_zero.2 zij.symm
      field_simp; ring
    rw [← h]
    simp only [add_mul, mul_add, smul_mul_assoc, mul_smul_comm, smul_smul, smul_add, smul_sub,
      hαβ, mul_comm (z j - s)⁻¹ (z i - s)⁻¹]
    module
  -- three fresh values
  obtain ⟨s₁, h1⟩ := Infinite.exists_notMem_finset (Finset.univ.image z)
  obtain ⟨s₂, h2⟩ := Infinite.exists_notMem_finset (insert s₁ (Finset.univ.image z))
  obtain ⟨s₃, h3⟩ := Infinite.exists_notMem_finset (insert s₂ (insert s₁ (Finset.univ.image z)))
  simp only [Finset.mem_insert, not_or] at h2 h3
  have mem : ∀ b, z b ∈ Finset.univ.image z := fun b => Finset.mem_image_of_mem z (Finset.mem_univ b)
  have nz : ∀ {s : k}, s ∉ Finset.univ.image z → ∀ b, s ≠ z b := fun hs b h => hs (h ▸ mem b)
  exact pole_two zij (Ne.symm h2.1) (Ne.symm h3.2.1) (Ne.symm h3.1) (nz h1 i) (nz h2.2 i)
    (nz h3.2.2 i) (nz h1 j) (nz h2.2 j) (nz h3.2.2 j) (hs _ h1) (hs _ h2.2) (hs _ h3.2.2)

theorem residOff_update {M : Fin n → Fin n → A} (z : Fin n → k) {j m m' : Fin n} (hjm' : j ≠ m')
    (hmm' : m ≠ m') (s : k) :
    residOff M (Function.update z m' s) j m =
      (∑ b, (if b = m' then (0 : A) else (if b = m then (0 : k) else (z j - z b)⁻¹) • M j b)) +
        (z j - s)⁻¹ • M j m' := by
  unfold residOff
  rw [sum_split _ m', add_comm, if_neg hmm'.symm, Function.update_self,
    Function.update_of_ne hjm']
  congr 1
  refine Finset.sum_congr rfl fun b _ => ?_
  split_ifs with h1 h2 <;> simp_all [Function.update_of_ne]

/-- The point-sample used to reach configuration space. -/
theorem natCast_injective [CharZero k] : Function.Injective (fun i : Fin n => ((i : ℕ) : k)) :=
  Nat.cast_injective.comp Fin.val_injective

/-- **Second residue: disjoint commutators vanish.** -/
theorem disjoint_commute [CharZero k] [DecidableEq k] {M : Fin n → Fin n → A}
    (hR : ∀ z : Fin n → k, Function.Injective z → ∀ a b,
      resid M z a * resid M z b = resid M z b * resid M z a)
    {i j m m' : Fin n} (hij : i ≠ j) (him : i ≠ m) (hjm : j ≠ m) (him' : i ≠ m') (hjm' : j ≠ m')
    (hmm' : m ≠ m') : M i m * M j m' = M j m' * M i m := by
  set z : Fin n → k := fun i => ((i : ℕ) : k)
  have hz : Function.Injective z := natCast_injective
  have zij : z i ≠ z j := hz.ne hij
  obtain ⟨R2, hR2⟩ : ∃ R2 : A, R2 = ∑ b, (if b = m' then (0 : A) else
      (if b = m then (0 : k) else (z j - z b)⁻¹) • M j b) := ⟨_, rfl⟩
  have hs : ∀ s : k, s ∉ Finset.univ.image z →
      (M i m * R2 - R2 * M i m + (z j - z i)⁻¹ • (M i m * M j m - M j m * M i m)) +
        (z j - s)⁻¹ • (M i m * M j m' - M j m' * M i m) = 0 := by
    intro s hsT
    have h := first_residue hR hij him hjm _ (update_injective hz hsT m')
    rw [residOff_update z hjm' hmm', Function.update_of_ne hjm', Function.update_of_ne him',
      ← hR2] at h
    rw [← h]
    simp only [mul_add, add_mul, smul_mul_assoc, mul_smul_comm]
    module
  obtain ⟨s₁, h1⟩ := Infinite.exists_notMem_finset (Finset.univ.image z)
  obtain ⟨s₂, h2⟩ := Infinite.exists_notMem_finset (insert s₁ (Finset.univ.image z))
  simp only [Finset.mem_insert, not_or] at h2
  exact sub_eq_zero.1 (pole_one (Ne.symm h2.1) (hs _ h1) (hs _ h2.2))

/-- **Flat ⇒ relations, every `n`.** If `ω ∧ ω = 0` at every configuration of distinct points
for all tangent vectors, the residues satisfy the infinitesimal pure braid relations. The
diagonal residues `M_{ii}` never enter `ω` (`ω_{ii} = 0`), so they are unconstrained by
curvature; the relations that mention them hold when they are central (`hdiag`). -/
theorem isFlat_of_curvature_zero [CharZero k] {M : Fin n → Fin n → A}
    (hsym : ∀ i j, M i j = M j i) (hdiag : ∀ i a b, M i i * M a b = M a b * M i i)
    (hF : ∀ z : Fin n → k, Function.Injective z → ∀ u v, omegaWedgeOmega M z u v = 0) :
    IsFlatLogConnection M := by
  classical
  have hR : ∀ z : Fin n → k, Function.Injective z → ∀ a b,
      resid M z a * resid M z b = resid M z b * resid M z a := by
    intro z hz a b
    have h := hF z hz (Pi.single a 1) (Pi.single b 1)
    rw [omegaWedgeOmega, connForm_single hsym, connForm_single hsym] at h
    exact sub_eq_zero.1 h
  refine ⟨fun i j l m hil him hjl hjm => ?_, fun a b c hab hac hbc => ?_⟩
  · by_cases hij : i = j
    · subst hij; exact hdiag i l m
    by_cases hlm : l = m
    · subst hlm; exact (hdiag l i j).symm
    exact disjoint_commute hR hil hij (Ne.symm hjl) him hlm hjm
  · -- `[M_ab, M_ac + M_bc] = 0` from the first residue at `(i, m, j) = (a, b, c)`
    set z : Fin n → k := fun i => ((i : ℕ) : k)
    have hz : Function.Injective z := natCast_injective
    have h := first_residue hR hac hab (Ne.symm hbc) z hz
    have hX : M a b * residOff M z c b - residOff M z c b * M a b =
        (z c - z a)⁻¹ • (M a b * M c a - M c a * M a b) := by
      unfold residOff
      rw [Finset.mul_sum, Finset.sum_mul, ← Finset.sum_sub_distrib,
        Finset.sum_eq_single a]
      · rw [if_neg hab.symm.symm, mul_smul_comm, smul_mul_assoc, smul_sub]
      · intro d _ hda
        by_cases hdb : d = b
        · simp [hdb]
        by_cases hdc : d = c
        · simp [hdc]
        rw [if_neg hdb, mul_smul_comm, smul_mul_assoc, ← smul_sub,
          disjoint_commute hR hac hab (Ne.symm hbc) (Ne.symm hda) (Ne.symm hdc) (Ne.symm hdb), sub_self,
          smul_zero]
      · simp
    rw [hX, ← smul_add] at h
    have hca : z c - z a ≠ 0 := sub_ne_zero.2 (hz.ne hac.symm)
    have h' := (smul_eq_zero.1 h).resolve_left (inv_ne_zero hca)
    rw [hsym c a, hsym c b] at h'
    rw [← sub_eq_zero, ← h']
    noncomm_ring

/-- **Flatness ⇔ the infinitesimal pure braid relations, for every `n`.** For symmetric residues
whose diagonal entries are central, `ω ∧ ω = 0` on all of configuration space iff the residues
satisfy the relations. -/
theorem curvature_zero_iff_isFlat [CharZero k] {M : Fin n → Fin n → A}
    (hsym : ∀ i j, M i j = M j i) (hdiag : ∀ i a b, M i i * M a b = M a b * M i i) :
    (∀ z : Fin n → k, Function.Injective z → ∀ u v, omegaWedgeOmega M z u v = 0) ↔
      IsFlatLogConnection M :=
  ⟨isFlat_of_curvature_zero hsym hdiag, fun hM z hz u v => curvature_zero_of_isFlat z u v hsym hM hz⟩

end Converse

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
        (MonoidAlgebra.of k (Perm (Fin n)) (swap i l) +
          MonoidAlgebra.of k (Perm (Fin n)) (swap j l)) - algebraMap k _ (2⁻¹ + 2⁻¹ : k) := by
      simp only [kzResidue, map_add]; abel
    rw [hsum]
    refine (commute_sub_central ?_ _ _).eq
    rw [Commute, SemiconjBy, mul_add, add_mul, ← map_mul, ← map_mul, ← map_mul, ← map_mul,
      swap_mul_swap_eq hil hjl, swap_mul_swap_eq' hil hjl, add_comm]

/-- **The `𝔰𝔩₂` KZ connection is flat on `n` points, for every `n`.** -/
theorem kz_sl2_curvature_zero [CharZero k] (z : Fin n → k) (hz : Function.Injective z)
    (u v : Fin n → k) :
    omegaWedgeOmega (kzResidue (k := k) (n := n)) z u v = 0 :=
  curvature_zero_of_isFlat z u v kzResidue_symm kzResidue_isFlat hz

end KZsl2

end QOU.Mass.InfinitesimalPureBraid
