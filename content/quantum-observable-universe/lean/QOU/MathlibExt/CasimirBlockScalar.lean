import QOU.MathlibExt.TraceIsWeighted

/-!
# QOU.MathlibExt.CasimirBlockScalar — the Casimir of a weighted trace, block by block

On `A = ∏_i M_{d_i}(K)` with a weighted trace `weightedTrace c`, the matrix
units have an explicit dual family and the resulting Casimir is a scalar on each
block.  The scalar is `d_i / c_i` — **not** `1 / c_i`; the dimension factor comes
from the `b`-summation and is easy to drop by eye.

## Where the value comes from

`τ(E^{(i)}_{ab} · E^{(j)}_{cd}) = δ_{ij} c_i δ_{bc} δ_{ad}`, so the dual of
`E^{(i)}_{ab}` is `c_i⁻¹ E^{(i)}_{ba}`.  Then

  `Σ_{a,b} E_{ab} · c_i⁻¹ E_{ba} = c_i⁻¹ Σ_{a,b} E_{aa} = (d_i / c_i) · 1`,

since `E_{ab} E_{ba} = E_{aa}` and the inner sum over `b` contributes `d_i`
copies of each `E_{aa}`.

## What this is for

`QOU.Hecke.TauDualBasis` proves the `T_w`-Casimir `Σ_w T_w T^∨_w` is central.
This file computes what a Casimir *is*, in the one basis where it is a finite
calculation.  Connecting the two needs **basis-independence of the Casimir** —
that `Σ b_i b_i^∨` is the same element for any dual pair — which is not proved
here and is the next brick.  Its proof is two lines given both expansions, and
both expansions are available on the `T_w` side; what is missing is the
matching pair of expansions for the pulled-back matrix units.

So this file supplies the **arithmetic**, and deliberately claims nothing about
`Σ_w T_w T^∨_w` itself.

## What is proved

* `blockUnitDual` — the dual family `c_i⁻¹ · E^{(i)}_{ba}`.
* `weightedTrace_blockUnit_mul_blockUnitDual` — it is dual: the pairing is
  `δ`.  Off-diagonal needs no hypothesis on `c`; only the diagonal does.
* `blockUnit_mul_blockUnitDual_block` — the `i`-block of a unit against its own
  dual is `c_i⁻¹ E_aa`, independently of `b`.
* `sum_single_diag_eq_one` — the diagonal units sum to `1`.
* `blockUnit_mul_blockUnitDual_sum_block` — **the per-block Casimir sum is
  `(d_i / c_i) • 1`.**

Assembling those blocks into a single element of the product, and identifying
it with `Σ_w T_w T^∨_w`, both wait on basis-independence; neither is claimed.

Generic over `[Field K]` per §7c; nothing archimedean and nothing Hecke-specific.
-/

namespace QOU.MathlibExt

open Matrix

section Casimir

variable {K : Type*} [Field K]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]

/-- **The dual of the matrix unit `E^{(i)}_{ab}`** under `weightedTrace c`:
    `c_i⁻¹ · E^{(i)}_{ba}` — transposed within the block, and rescaled. -/
def blockUnitDual (c : ι → K) (i : ι) (a b : J i) : ∀ j, Matrix (J j) (J j) K :=
  (c i)⁻¹ • blockUnit (K := K) (J := J) i b a

/-- **The pairing is `δ`.**  As with `TwDual` on the Hecke side, only the
    diagonal case spends the hypothesis `c i ≠ 0`. -/
theorem weightedTrace_blockUnit_mul_blockUnitDual (c : ι → K) (hc : ∀ i, c i ≠ 0)
    (i : ι) (a b : J i) (a' b' : J i) :
    weightedTrace c (blockUnit (K := K) (J := J) i a b
        * blockUnitDual (K := K) (J := J) c i a' b')
      = if (a, b) = (a', b') then 1 else 0 := by
  classical
  rw [blockUnitDual, weightedTrace]
  rw [Finset.sum_eq_single i]
  · rw [Pi.mul_apply, Pi.smul_apply, blockUnit_self, blockUnit_self,
      Matrix.mul_smul, Matrix.trace_smul, trace_single_mul_single, smul_eq_mul]
    by_cases h : ((a, b) : J i × J i) = (a', b')
    · obtain ⟨rfl, rfl⟩ := Prod.mk.injEq .. ▸ h
      simp [hc i]
    · have hba : ¬ (((b, a) : J i × J i) = (b', a')) := fun hc' =>
        h (by simpa [Prod.ext_iff, and_comm] using hc')
      rw [if_neg h, if_neg hba, mul_zero, mul_zero]
  · intro j _ hj
    rw [Pi.mul_apply, Pi.smul_apply, blockUnit_of_ne _ _ _ hj, zero_mul,
      Matrix.trace_zero, mul_zero]
  · intro h
    exact absurd (Finset.mem_univ i) h

omit [Fintype ι] in
/-- The `i`-block of a matrix unit against its own dual: `E_ab · c_i⁻¹ E_ba
    = c_i⁻¹ E_aa`, for **every** `b`.  That the answer does not depend on `b` is
    what produces the dimension factor below. -/
theorem blockUnit_mul_blockUnitDual_block (c : ι → K) (i : ι) (a b : J i) :
    (blockUnit (K := K) (J := J) i a b * blockUnitDual (K := K) (J := J) c i a b) i
      = (c i)⁻¹ • Matrix.single a a (1 : K) := by
  rw [blockUnitDual, Pi.mul_apply, Pi.smul_apply, blockUnit_self, blockUnit_self,
    Matrix.mul_smul, Matrix.single_mul_single_same, mul_one]

omit [Fintype ι] [DecidableEq ι] in
/-- The sum of the diagonal matrix units is the identity. -/
theorem sum_single_diag_eq_one (i : ι) :
    (∑ x : J i, Matrix.single x x (1 : K)) = 1 := by
  ext r s
  rw [Matrix.sum_apply, Matrix.one_apply, Finset.sum_eq_single r]
  · simp [Matrix.single]
  · intro x _ hx; simp [Matrix.single, hx]
  · intro h; exact absurd (Finset.mem_univ r) h

omit [Fintype ι] in
/-- **The per-block Casimir sum.**  `Σ_{a,b} E_ab · c_i⁻¹ E_ba = (d_i / c_i) · 1`.

    The dimension factor is the `b`-summation: by
    `blockUnit_mul_blockUnitDual_block` the summand does not depend on `b` at
    all, so each `E_aa` is counted `d_i` times.  It is easy to drop by eye, and
    it is why the block scalar is `d_i / c_i` rather than `1 / c_i`. -/
theorem blockUnit_mul_blockUnitDual_sum_block (c : ι → K) (i : ι) :
    (∑ a : J i, ∑ b : J i,
        (blockUnit (K := K) (J := J) i a b
          * blockUnitDual (K := K) (J := J) c i a b) i)
      = ((Fintype.card (J i) : K) / c i) • (1 : Matrix (J i) (J i) K) := by
  calc (∑ a : J i, ∑ b : J i,
          (blockUnit (K := K) (J := J) i a b
            * blockUnitDual (K := K) (J := J) c i a b) i)
      = ∑ _a : J i, ∑ _b : J i, (c i)⁻¹ • Matrix.single _a _a (1 : K) := by
        simp only [blockUnit_mul_blockUnitDual_block]
    _ = ∑ a : J i, ((Fintype.card (J i) : K) * (c i)⁻¹) • Matrix.single a a (1 : K) := by
        refine Finset.sum_congr rfl fun a _ => ?_
        rw [Finset.sum_const, Finset.card_univ, MulAction.mul_smul,
          Nat.cast_smul_eq_nsmul]
    _ = ((Fintype.card (J i) : K) * (c i)⁻¹) • ∑ a : J i, Matrix.single a a (1 : K) := by
        rw [Finset.smul_sum]
    _ = ((Fintype.card (J i) : K) / c i) • (1 : Matrix (J i) (J i) K) := by
        rw [sum_single_diag_eq_one (J := J) i, div_eq_mul_inv]

end Casimir

end QOU.MathlibExt
