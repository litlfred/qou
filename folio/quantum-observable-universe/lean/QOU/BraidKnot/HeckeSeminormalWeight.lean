import QOU.BraidKnot.HeckeFullTwistProduct

/-!
# The twist on a Jucys–Murphy weight vector

`KeystoneJucysMurphyTwist` carries the general-`λ` twist conditionally, on a class
`JucysMurphySpectrum` whose one assumption is about the **composite** object:

    fullTwistScalar = ∏ i, q ^ (2 · content (e i))

That is not the statement the seminormal-form literature proves.  What it proves is a statement
about the **constituents** — that each `Lₖ` acts on a standard-tableau basis vector by
`q^{2·content}` — from which the product statement follows only because `∏Lᵢ = Δ²`.

`HeckeFullTwistProduct.jmProd_eq_delta_pow` now supplies that step for every `n`, so this file
makes the replacement:

* **assumed** — `IsJMWeight`: `Lₖ · v = cₖ · v` for `k < n`.  Per-element, the textbook hypothesis.
* **derived** — `fullTwist_smul_of_weight`: `Δ² · v = (∏ cₖ) · v`.
* **derived** — `fullTwist_smul_eq_theta_sq`: with `cₖ = q^{2·content}`, `Δ² · v = θ_λ² · v`.

It also derives the class field itself: `twist_scalar_eq_theta_sq` says that if the twist acts on a
nonzero weight vector by *some* scalar, that scalar **is** `θ_λ²`.

## Non-vacuity

A conditional theorem is worth what its hypothesis is inhabited.  `scalar_isJMWeight` exhibits an
instance — the one-dimensional representation `σᵢ ↦ q` with the one-row tableau — and
`scalar_fullTwist_eq_single_row` checks that the value the general theorem then returns is
`q^{n(n−1)}`, which `KeystoneHeckeRootsForceTwist.theta_single_row_sq` obtains from the two roots of
the Hecke relation with no Jucys–Murphy input at all.  Two routes, same answer.

## What this does and does not change

It does **not** prove the seminormal form.  The eigenvalue hypothesis is still an assumption for
`dim V_λ > 1` — the instance above is one-dimensional and demonstrates only that the hypothesis is
satisfiable, not that it holds in general — and the general-`λ` twist is still conditional.  What
changes is *which* thing is assumed: an assumption about a product of `n` operators becomes an
assumption about each operator separately, and the passage between them is now proved rather than
bundled into the same class field.

The scalar hypothesis is per-vector and carries no positivity, ordering, or archimedean content, so
everything here stays over a generic `[Field R]` and `[Ring A]` per §7c — no `ℝ`.

Refs:
- [wenzl1988] Hecke algebra representations (seminormal form).
-/

namespace QOU.BraidKnot.Hecke

open Finset QOU.BraidKnot.Keystone QOU.MathlibExt.QPartitionCombinatorics

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R}
variable {V : Type*} [AddCommGroup V] [Module A V] [Module R V] [IsScalarTower R A V]

/-- **A Jucys–Murphy weight vector**: every `Lₖ` with `k < n` acts on `v` by a scalar `cₖ`.

This is the seminormal form's defining property of a standard-tableau basis vector, stated without
constructing the basis. -/
def IsJMWeight (H : HeckeGenerators R A q) (v : V) (c : ℕ → R) (n : ℕ) : Prop :=
  ∀ k, k < n → jmRaw H k • v = c k • v

/-- **The ordered product of the JM elements acts by the product of the eigenvalues.**

Induction on `n`.  The step needs the eigenvalue scalar to commute past `jmProd`, which it does
because `Algebra R A` puts the image of `algebraMap` in the centre. -/
theorem jmProd_smul_of_weight (H : HeckeGenerators R A q) (v : V) (c : ℕ → R) :
    ∀ n : ℕ, IsJMWeight H v c n → jmProd H n • v = (∏ k ∈ Finset.range n, c k) • v := by
  intro n
  induction n with
  | zero => intro _; simp [jmProd]
  | succ m ih =>
      intro hw
      have hm := ih fun k hk => hw k (by omega)
      rw [jmProd_succ, mul_smul, hw m (by omega), smul_comm, hm, smul_smul,
        Finset.prod_range_succ, mul_comm]

/-- **The full twist acts on a JM weight vector by the product of its eigenvalues.**

`Δ² = (delta m)^{m+1}` by `jmProd_eq_delta_pow`, so the composite statement the old class assumed is
now a consequence of the per-element one. -/
theorem fullTwist_smul_of_weight (H : HeckeGenerators R A q) (v : V) (c : ℕ → R) (m : ℕ)
    (hw : IsJMWeight H v c (m + 1)) :
    (delta H m ^ (m + 1)) • v = (∏ k ∈ Finset.range (m + 1), c k) • v := by
  rw [← jmProd_eq_delta_pow]
  exact jmProd_smul_of_weight H v c (m + 1) hw

/-! ## Specialising to the content eigenvalues -/

/-- Entry `k` of a tableau on `m+1` cells, as an index.  The `% (m+1)` is a totality device only:
every use is at `k < m+1`, where `entryIdx_of_lt` says it is the identity. -/
def entryIdx (m k : ℕ) : Fin (m + 1) := ⟨k % (m + 1), Nat.mod_lt k (Nat.succ_pos m)⟩

@[simp] theorem entryIdx_val (m : ℕ) (i : Fin (m + 1)) : entryIdx m i.val = i :=
  Fin.ext (Nat.mod_eq_of_lt i.isLt)

theorem entryIdx_of_lt {m k : ℕ} (h : k < m + 1) : entryIdx m k = ⟨k, h⟩ :=
  Fin.ext (Nat.mod_eq_of_lt h)

/-- The JM eigenvalue function attached to a tableau: `k ↦ q^{2·content}` of the cell holding `k`. -/
noncomputable def jmEigen (q : R) {l : Partition} {m : ℕ}
    (e : Fin (m + 1) ≃ {c // c ∈ cells l}) : ℕ → R :=
  fun k => q ^ (2 * cellContent (e (entryIdx m k)).1.1 (e (entryIdx m k)).1.2)

/-- The eigenvalues multiply to `θ_λ²`, for **every** tableau — the same tableau-independence
`sum_content_of_equiv` supplies, transported through `prod_zpow_eq_zpow_sum`. -/
theorem prod_jmEigen (q : R) (hq : q ≠ 0) {l : Partition} {m : ℕ}
    (e : Fin (m + 1) ≃ {c // c ∈ cells l}) :
    ∏ k ∈ Finset.range (m + 1), jmEigen q e k = (theta q l) ^ 2 := by
  rw [← Fin.prod_univ_eq_prod_range]
  have hcast : ∀ i : Fin (m + 1),
      jmEigen q e i.val = q ^ (2 * cellContent (e i).1.1 (e i).1.2) := by
    intro i
    unfold jmEigen
    rw [entryIdx_val]
  rw [Finset.prod_congr rfl fun i _ => hcast i, prod_zpow_eq_zpow_sum _ q hq]
  have hsum : ∑ i : Fin (m + 1), 2 * cellContent (e i).1.1 (e i).1.2 = 2 * contentSum l := by
    rw [← Finset.mul_sum, sum_content_of_equiv e]
  rw [hsum]
  unfold theta
  rw [← zpow_natCast (q ^ contentSum l) 2, ← zpow_mul]
  congr 1
  push_cast
  ring

/-- **The general-`λ` twist, from the per-element Jucys–Murphy spectrum.**

If each `Lₖ` acts on `v` by `q^{2·content of the cell holding k}`, then the full twist acts by
`θ_λ² = q^{2c(λ)}` — for every partition, and independently of which tableau `e` is.

The remaining assumption is `IsJMWeight` with the content eigenvalues.  That is the seminormal-form
theorem and it is **not** proved here; what is no longer assumed is the passage from the individual
eigenvalues to the twist. -/
theorem fullTwist_smul_eq_theta_sq (H : HeckeGenerators R A q) (hq : q ≠ 0)
    {l : Partition} {m : ℕ} (e : Fin (m + 1) ≃ {c // c ∈ cells l}) (v : V)
    (hw : IsJMWeight H v (jmEigen q e) (m + 1)) :
    (delta H m ^ (m + 1)) • v = ((theta q l) ^ 2) • v := by
  rw [fullTwist_smul_of_weight H v _ m hw, prod_jmEigen q hq e]

/-- **The twist scalar is pinned, not merely permitted.**

If the full twist acts on a nonzero weight vector by *some* scalar `s`, that scalar **is** `θ_λ²`.
This is the bridge to `KeystoneJucysMurphyTwist.JucysMurphySpectrum`: its `fullTwistScalar_eq` field
asserts exactly this equation, and here it is a consequence of the per-element eigenvalues rather
than a separate assumption.

`NoZeroSMulDivisors R V` is what turns "acts the same way on `v`" into "is the same scalar"; it is
stated as a hypothesis rather than derived so that nothing here depends on `V` being a vector
space. -/
theorem twist_scalar_eq_theta_sq [NoZeroSMulDivisors R V] (H : HeckeGenerators R A q) (hq : q ≠ 0)
    {l : Partition} {m : ℕ} (e : Fin (m + 1) ≃ {c // c ∈ cells l}) (v : V) (hv : v ≠ 0) (s : R)
    (hw : IsJMWeight H v (jmEigen q e) (m + 1))
    (hs : (delta H m ^ (m + 1)) • v = s • v) :
    s = (theta q l) ^ 2 := by
  have h := (fullTwist_smul_eq_theta_sq H hq e v hw).symm.trans hs
  have hz : (s - (theta q l) ^ 2) • v = 0 := by
    rw [sub_smul, h, sub_self]
  rcases smul_eq_zero.mp hz with hc | hcv
  · linear_combination (norm := ring_nf) hc
  · exact absurd hcv hv

/-! ## Non-vacuity, and a falsifiability check against an independent route

A conditional theorem is worth only as much as its hypothesis is inhabited.  This section exhibits
an instance and checks that the conclusion it delivers agrees with a result proved by a completely
different argument. -/

/-- The **one-dimensional Hecke representation** `σᵢ ↦ q` — the `+q` root of the Hecke relation,
the same branch `KeystoneHeckeRootsForceTwist` uses for the one-row block. -/
def scalarGenerators (q : R) (hq : q ≠ 0) : HeckeGenerators R R q where
  σ := fun _ => q
  σinv := fun _ => q⁻¹
  mul_σinv := fun _ => mul_inv_cancel₀ hq
  σinv_mul := fun _ => inv_mul_cancel₀ hq
  hecke := fun _ => by
    simp only [Algebra.algebraMap_self, RingHom.id_apply, sub_mul]
    rw [inv_mul_cancel₀ hq]
    ring
  braid := fun _ => by ring
  far := fun _ _ _ => by ring

/-- In that representation `Lₖ = q^{2k}` — the JM spectrum of the one-row block, on the nose. -/
theorem scalar_jmRaw (q : R) (hq : q ≠ 0) (k : ℕ) :
    jmRaw (scalarGenerators q hq) k = q ^ (2 * k) := by
  induction k with
  | zero => simp
  | succ i ih =>
      rw [jmRaw_succ, ih]
      show q * q ^ (2 * i) * q = q ^ (2 * (i + 1))
      ring

/-- The one-row tableau of shape `[m+1]`: entry `k` sits in cell `(0, k)`. -/
def rowTableau (m : ℕ) : Fin (m + 1) ≃ {c // c ∈ cells [m + 1]} where
  toFun i := ⟨(0, i.val), mem_cells.mpr ⟨Nat.zero_lt_one, i.isLt⟩⟩
  invFun c := ⟨c.1.2, by
    obtain ⟨h1, h2⟩ := mem_cells.mp c.2
    have hlt : c.1.1 < 1 := h1
    have hz : c.1.1 = 0 := by omega
    rw [hz] at h2
    exact h2⟩
  left_inv := fun _ => rfl
  right_inv := by
    rintro ⟨⟨i, j⟩, hc⟩
    have hlt : i < 1 := (mem_cells.mp hc).1
    have hi : i = 0 := by omega
    subst hi
    rfl

/-- **The hypothesis is satisfied.**  `v = 1` in the one-dimensional representation is a
Jucys–Murphy weight vector for the one-row tableau, with exactly the content eigenvalues. -/
theorem scalar_isJMWeight (q : R) (hq : q ≠ 0) (m : ℕ) :
    IsJMWeight (scalarGenerators q hq) (1 : R) (jmEigen q (rowTableau m)) (m + 1) := by
  intro k hk
  have hcell : (rowTableau m (entryIdx m k)).1 = (0, k) := by
    rw [entryIdx_of_lt hk]; rfl
  simp only [smul_eq_mul, mul_one, jmEigen, hcell, scalar_jmRaw, cellContent]
  rw [show ((k : ℤ) - (0 : ℕ)) = (k : ℤ) by push_cast; ring]
  rw [← zpow_natCast q (2 * k)]
  congr 1

/-- **The falsifiability check.**  Feeding that instance to the general theorem gives
`q^{n(n−1)}` — which is what `theta_single_row_sq` obtains from the two roots of the Hecke relation,
with no Jucys–Murphy input at all.  The two routes agree, so the general statement is constrained by
an independently-proved case rather than free. -/
theorem scalar_fullTwist_eq_single_row (q : R) (hq : q ≠ 0) (m : ℕ) :
    (delta (scalarGenerators q hq) m ^ (m + 1)) • (1 : R) = q ^ fullTwistLength (m + 1) := by
  rw [fullTwist_smul_eq_theta_sq (scalarGenerators q hq) hq (rowTableau m) (1 : R)
    (scalar_isJMWeight q hq m), theta_single_row_sq, smul_eq_mul, mul_one]

end QOU.BraidKnot.Hecke
