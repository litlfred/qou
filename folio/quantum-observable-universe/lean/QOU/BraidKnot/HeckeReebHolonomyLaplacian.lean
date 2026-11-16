import QOU.BraidKnot.HeckeBoundedSeminormalWeight

/-!
# The Reeb-holonomy Laplacian: an operator whose block eigenvalue is `Σ [c][c+1]`

`docs/audits/2026-11-15-q-laplacian-eigenvalue-derivation.md` closed the algebraic half of the
claim "`Δ_ξ` acts on `V_λ` by `Σ_{□∈λ} [c(□)][c(□)+1]`" (`QOU.SchurWeyl.ContentCasimir`) and found an
obstruction to the geometric half: the `Δ_ξ` of `rem:q-laplacian-expansion` has no `q` in it, so its
spectrum cannot move with `q`, while `Σ[c][c+1]` does.

This file supplies the algebraic side of an operator that is *not* hit by that obstruction, because
it depends on `q` through a step length.  It is the content Casimir written in terms of **relative
full twists**, i.e. in terms of the holonomies that the braiding attaches to rotating a cluster of
strands.

## What is proved (any field, bounded presentation `HeckeGeneratorsBelow`)

1. **`Lₖ` is a relative full twist** (`fullTwistB_succ_eq_mul_jmRawB`):
   `Δ²_{k+1} = Δ²_k · L_{k+1}`, where `Δ²_k = (σ₀⋯σ_{k−1})^{k+1}` is the full twist of the first
   `k+1` strands.  This is a corollary of `jmProdB_eq_deltaB_pow`; nothing new is used.
2. **The inverse Murphy element** `jmRawInvB` (built from `σ⁻¹ = σ − (q − q⁻¹)`, which the Hecke
   relation supplies) is a two-sided inverse of `jmRawB` (`jmRawInvB_mul_jmRawB`,
   `jmRawB_mul_jmRawInvB`).
3. **The Reeb-holonomy Laplacian** `reebLaplacianB H m = Σ_{k<m} (q·Lₖ + q⁻¹·Lₖ⁻¹ − (q + q⁻¹))`
   acts on any Jucys–Murphy weight vector with `Lₖ ↦ aₖ²`, `aₖbₖ = 1`, by
   `Σ_k (aₖ − bₖ)(q·aₖ − q⁻¹·bₖ)` (`reebLaplacianB_smul_of_weight`).  At `aₖ = q^{cₖ}` this is
   `(q − q⁻¹)² Σ_k [cₖ][cₖ + 1]`.  The `Lₖ⁻¹` eigenvalue is derived, not assumed.
4. **Reflection symmetry of one cell** (`reebStep_reflect`): the per-cell value is unchanged under
   `c ↦ −c − 1` (`a ↦ q⁻¹b`, `b ↦ qa`).  So `[c][c+1]` depends on `c` only through the spin
   `j = c` or `j = −c − 1`, whichever is `≥ 0`: it is the `U_q(𝔰𝔩₂)` Casimir value `[j][j+1]`.

## Why "Laplacian", and why the obstruction does not apply

Write `q = e^h`.  On a weight vector `Lₖ = e^{2h Xₖ}` with `Xₖ` acting by the content `cₖ`, and
`q·Lₖ + q⁻¹·Lₖ⁻¹ − (q + q⁻¹) = 2 cosh(h(2Xₖ + 1)) − 2 cosh h`.  This is a symmetric second
difference of step `h` in the variable `Xₖ + ½`, and divided by `(q − q⁻¹)²` it tends to
`Xₖ(Xₖ + 1) = (Xₖ + ½)² − ¼` as `h → 0` (checked exactly on the regular representations of `H₂`
and `H₃`; this limit is analytic and is not formalised here).  So the operator is a finite-step
Laplacian whose step is `h`, and its spectrum moves with `q` for that reason.  The obstruction in
the audit is about a `q`-independent operator and does not apply.

## What is NOT proved here

* **Centrality** is proved for the same element on the other Hecke presentation
  (`QOU.SchurWeyl.contentCasimir_comm_σ`).  It is not re-proved on `HeckeGeneratorsBelow`.
* **That every `V_λ` has a JM weight basis with eigenvalues `q^{2c}`** is the seminormal form
  ([ram1997] Thm 4.1); here it is a hypothesis, as in `ContentCasimir`.
* **The geometric reading**: that `Δ²_k` is the holonomy of the Reeb (rotation) loop of the cluster
  of the first `k + 1` points.  That needs Bridge A: the `n`-body base with `ξ` the Euler field (P1
  of `a2-lagrangian-kz.md`) and Drinfeld–Kohno.  This file is the algebra that reading would use.

Refs: [ram1997] Theorem 4.1; [murphy1992]; [jones1987].
-/

namespace QOU.BraidKnot.Hecke

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R} {n : ℕ}

/-! ## §1  `Lₖ` is a relative full twist -/

/-- **Relative full twist.**  `Δ²_{k+1} = Δ²_k · L_{k+1}`: the Murphy element `L_{k+1}` is the full
twist of the first `k + 2` strands divided by the full twist of the first `k + 1`. -/
theorem fullTwistB_succ_eq_mul_jmRawB (H : HeckeGeneratorsBelow R A q n) (k : ℕ)
    (hk : k + 1 < n) :
    deltaB H (k + 1) ^ (k + 2) = deltaB H k ^ (k + 1) * jmRawB H (k + 1) := by
  rw [← jmProdB_eq_deltaB_pow H (k + 1) hk, ← jmProdB_eq_deltaB_pow H k (by omega), jmProdB_succ]

/-! ## §2  Inverse Murphy elements -/

/-- The inverse generator supplied by the Hecke relation, `σᵢ⁻¹ = σᵢ − (q − q⁻¹)`. -/
def σInvB (H : HeckeGeneratorsBelow R A q n) (i : ℕ) : A := H.σ i - algebraMap R A (q - q⁻¹)

/-- **Inverse Murphy elements**: `L₀⁻¹ = 1`, `L_{i+1}⁻¹ = σᵢ⁻¹ Lᵢ⁻¹ σᵢ⁻¹`. -/
def jmRawInvB (H : HeckeGeneratorsBelow R A q n) : ℕ → A
  | 0 => 1
  | (i + 1) => σInvB H i * jmRawInvB H i * σInvB H i

theorem jmRawInvB_mul_jmRawB (H : HeckeGeneratorsBelow R A q n) :
    ∀ k, k < n → jmRawInvB H k * jmRawB H k = 1
  | 0, _ => by simp [jmRawInvB]
  | (i + 1), hk => by
      have hs : σInvB H i * H.σ i = 1 := sub_mul_hecke_eq_one (H.hecke i hk)
      have ih := jmRawInvB_mul_jmRawB H i (by omega)
      show σInvB H i * jmRawInvB H i * σInvB H i * (H.σ i * jmRawB H i * H.σ i) = 1
      calc σInvB H i * jmRawInvB H i * σInvB H i * (H.σ i * jmRawB H i * H.σ i)
          = σInvB H i * jmRawInvB H i * (σInvB H i * H.σ i) * jmRawB H i * H.σ i := by
            noncomm_ring
        _ = σInvB H i * (jmRawInvB H i * jmRawB H i) * H.σ i := by rw [hs]; noncomm_ring
        _ = 1 := by rw [ih, mul_one, hs]

theorem jmRawB_mul_jmRawInvB (H : HeckeGeneratorsBelow R A q n) :
    ∀ k, k < n → jmRawB H k * jmRawInvB H k = 1
  | 0, _ => by simp [jmRawInvB]
  | (i + 1), hk => by
      have hs : H.σ i * σInvB H i = 1 := hecke_mul_sub_eq_one (H.hecke i hk)
      have ih := jmRawB_mul_jmRawInvB H i (by omega)
      show H.σ i * jmRawB H i * H.σ i * (σInvB H i * jmRawInvB H i * σInvB H i) = 1
      calc H.σ i * jmRawB H i * H.σ i * (σInvB H i * jmRawInvB H i * σInvB H i)
          = H.σ i * jmRawB H i * (H.σ i * σInvB H i) * jmRawInvB H i * σInvB H i := by
            noncomm_ring
        _ = H.σ i * (jmRawB H i * jmRawInvB H i) * σInvB H i := by rw [hs]; noncomm_ring
        _ = 1 := by rw [ih, mul_one, hs]

/-! ## §3  The per-cell value and its reflection symmetry -/

/-- The per-cell value of the Laplacian on a weight with `L ↦ a²`, `L⁻¹ ↦ b²`:
`q a² + q⁻¹ b² − (q + q⁻¹)`. -/
def reebStep (q qi a b : R) : R := q * a ^ 2 + qi * b ^ 2 - (q + qi)

/-- The per-cell value in product form, `(a − b)(q a − q⁻¹ b)` (`= (q − q⁻¹)² [c][c+1]` at
`a = q^c`). -/
theorem reebStep_eq_mul (q qi a b : R) (hab : a * b = 1) :
    reebStep q qi a b = (a - b) * (q * a - qi * b) := by
  unfold reebStep
  linear_combination (q + qi) * hab

/-- **Reflection `c ↦ −c − 1`.**  Replacing `(a, b) = (q^c, q^{−c})` by `(q^{−c−1}, q^{c+1})
= (q⁻¹ b, q a)` leaves the per-cell value unchanged. -/
theorem reebStep_reflect (q qi a b : R) (hq : q * qi = 1) :
    reebStep q qi (qi * b) (q * a) = reebStep q qi a b := by
  unfold reebStep
  linear_combination (qi * b ^ 2 + q * a ^ 2) * hq

/-! ## §4  The Laplacian and its eigenvalue on a weight vector -/

/-- **The Reeb-holonomy Laplacian** on the first `m` strands, denominators cleared by `(q − q⁻¹)²`:
`Σ_{k<m} (q·Lₖ + q⁻¹·Lₖ⁻¹ − (q + q⁻¹))`.  By §1 each `Lₖ` is the relative full twist
`(Δ²_{k−1})⁻¹ Δ²_k`. -/
noncomputable def reebLaplacianB (H : HeckeGeneratorsBelow R A q n) (m : ℕ) : A :=
  ∑ k ∈ Finset.range m,
    (q • jmRawB H k + q⁻¹ • jmRawInvB H k - algebraMap R A (q + q⁻¹))

variable {V : Type*} [AddCommGroup V] [Module A V] [Module R V] [IsScalarTower R A V]

/-- On a weight vector the inverse Murphy element acts by the inverse eigenvalue. -/
theorem jmRawInvB_smul_of_weight (H : HeckeGeneratorsBelow R A q n) {k : ℕ} (hk : k < n)
    (v : V) (a b : R) (hab : a * b = 1) (hv : jmRawB H k • v = a ^ 2 • v) :
    jmRawInvB H k • v = b ^ 2 • v := by
  have h1 : jmRawInvB H k • (jmRawB H k • v) = v := by
    rw [← mul_smul, jmRawInvB_mul_jmRawB H k hk, one_smul]
  rw [hv, smul_comm] at h1
  have hb : b ^ 2 * a ^ 2 = 1 := by rw [← mul_pow, mul_comm, hab, one_pow]
  calc jmRawInvB H k • v
      = (b ^ 2 * a ^ 2) • jmRawInvB H k • v := by rw [hb, one_smul]
    _ = b ^ 2 • (a ^ 2 • jmRawInvB H k • v) := by rw [mul_smul]
    _ = b ^ 2 • v := by rw [h1]

/-- **Block eigenvalue of the Reeb-holonomy Laplacian.**  If each `Lₖ` (`k < m ≤ n`) acts on `v`
by `aₖ²` with `aₖ bₖ = 1`, the Laplacian acts by `Σ_k (aₖ − bₖ)(q aₖ − q⁻¹ bₖ)`, which is
`(q − q⁻¹)² Σ_k [cₖ][cₖ + 1]` at `aₖ = q^{cₖ}`. -/
theorem reebLaplacianB_smul_of_weight (H : HeckeGeneratorsBelow R A q n) (hq : q ≠ 0)
    (m : ℕ) (hm : m ≤ n) (v : V) (a b : ℕ → R) (hab : ∀ k, a k * b k = 1)
    (hw : IsJMWeightB H v (fun k => a k ^ 2) m) :
    reebLaplacianB H m • v
      = (∑ k ∈ Finset.range m, (a k - b k) * (q * a k - q⁻¹ * b k)) • v := by
  unfold reebLaplacianB
  rw [Finset.sum_smul, Finset.sum_smul]
  refine Finset.sum_congr rfl fun k hk => ?_
  have hkm : k < m := Finset.mem_range.mp hk
  have hfwd : jmRawB H k • v = a k ^ 2 • v := hw k hkm
  have hinv := jmRawInvB_smul_of_weight H (by omega) v (a k) (b k) (hab k) hfwd
  have hqq : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  rw [sub_smul, add_smul, smul_assoc, smul_assoc, hfwd, hinv, algebraMap_smul, smul_smul,
    smul_smul, ← add_smul, ← sub_smul, ← reebStep_eq_mul q q⁻¹ (a k) (b k) (hab k)]
  unfold reebStep
  ring_nf

end QOU.BraidKnot.Hecke
