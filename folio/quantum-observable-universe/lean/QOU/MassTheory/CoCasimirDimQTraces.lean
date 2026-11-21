import QOU.MassTheory.CoCasimirHeckeBridge
import QOU.SchurWeyl.HeckeSchurElements
import QOU.SchurWeyl.MolienBalancedForm
import QOU.SchurWeyl.SpinSectorMeasure

/-!
# Which trace each `dim_q` belongs to

The surviving-block co-Casimir `C° = Σ_{τ(p_λ) ≠ 0} p_λ / (dim_q(λ) · τ(p_λ))` takes `dim_q` as
block data. This file says where the two candidate dimensions come from, by computing what two
traces on `H_{n+1}(q)` assign to one **primitive** idempotent of the block `λ`.

In a pivotal category the quantum dimension of an object cut out by an idempotent `e` is the
quantum trace of `e`. Here `e = e_{λ,i}` is the preimage under the Wedderburn isomorphism `Ψ` of
the matrix unit `E_{ii}` in block `λ` (`primIdem`).

## The mass definition's trace: the `sl₂` dimension

`def:mass-identity` takes the Frobenius form to be the Jones–Markov trace of `H_n(q)` acting on
`V^{⊗n}`, `V = R²`, and its framing-corrected form multiplies that trace by `(q + q⁻¹)^n`, the
unnormalised quantum trace. On a primitive idempotent of a two-row block `(m, k)`:

* `markov_primIdem`: every Markov trace at `z_D` gives `T(e_{λ,i}) = w_λ`, the convention-D weight;
* `quantumDim_primIdem_twoRow`:
  `(q − q⁻¹) · (q + q⁻¹)^{n+1} · T(e_{λ,i}) = q^{m−k+1} − q^{−(m−k+1)}`,
  i.e. `[2]_q^{n+1} · T(e_{λ,i}) = [m − k + 1]_q`, the quantum dimension of the spin
  `(m − k)/2` simple of `U_q(sl₂)`.

`tr_cHecke_quantumDim` evaluates `C°` with this dimension:
`T(C°) = Σ_{λ ⊢ n+1, ℓ(λ) ≤ 2} 1 / ([2]_q^{n+1} · w_λ)`.

## The canonical trace: the hook formula

The symmetrising trace `τ₀(T_w) = δ_{w,1}` (`HeckeCoset.symTrace`) is a different Frobenius form.
`symTrace_primIdem`: `τ₀(e_{λ,i}) = q^{−κ(λ)} / ∏_{x ∈ λ} [h(x)]_q`, with `κ` the content sum.
Multiplying by `[n+1]_q!` gives `q^{−κ(λ)} · [n+1]_q! / ∏ [h(x)]_q`
(`qFact_mul_symTrace_primIdem`). That is the q-hook-length formula `dim_q` used in production,
times the twist `q^{−κ(λ)}`.

So the hook formula is the per-simple weight of `τ₀` (up to `q^{−κ}`), and the `sl₂` dimension is
the per-simple weight of the convention-D Markov trace. `def:mass-identity` uses the second. The
two are not proportional (`CoCasimirDimQNotForced`).

## What is proved and what is not

Everything above is a theorem about the two traces. That Term 4 of the mass formula should be
built from the mass definition's own trace is a modelling reading of `def:mass-identity`, not a
theorem. This file does not connect the diagram hook product here to the list-based
`QOU.Mass.dimQ` used by the production code; the two encode the same hook-length formula with
different hook bookkeeping.

## Base ring (§7c)

Generic `[Field K]`, `q ≠ 0`, `q` not a root of unity. No ordering, no `ℝ`.

LaTeX label: `thm:cocasimir-dimq-traces`
-/

namespace QOU.MassTheory.CoCasimirHecke

open Finset QOU.SchurWeyl QOU.MassTheory.CoCasimirSurviving
open QOU.Mathlib (StandardYoungTableau partitionShape)

noncomputable section

open Classical

variable {K : Type*} [Field K]
variable (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q) (n : ℕ)

/-- **Any weighted seminormal trace is a weighted block trace through `Ψ`.** -/
theorem tr_Ψ_weight (w : YoungDiagram → K) (x : Hecke K q q⁻¹ n) :
    tr (fun lam => w (partitionShape lam)) (Ψ q hq0 hq2 n x)
      = SeminormalRep.wtraceW q hq0 hq2 w n x := by
  rw [SeminormalRep.wtraceW_apply]
  unfold tr
  refine Fintype.sum_equiv (QOU.Mathlib.partitionShapeEquiv (n + 1)) _ _ (fun lam => ?_)
  rw [Ψ_apply]
  exact congrArg₂ (· * ·) rfl (trace_reindex_self _ _)

/-- The primitive idempotent `e_{λ,i} = Ψ⁻¹(E_{ii}` in block `λ`). -/
def primIdem (lam : Nat.Partition (n + 1)) (i : Fin (dim n lam)) : Hecke K q q⁻¹ n :=
  (Ψ q hq0 hq2 n).symm (Pi.single lam (Matrix.single i i 1))

theorem primIdem_mul_self (lam : Nat.Partition (n + 1)) (i : Fin (dim n lam)) :
    primIdem q hq0 hq2 n lam i * primIdem q hq0 hq2 n lam i = primIdem q hq0 hq2 n lam i := by
  unfold primIdem
  rw [← map_mul, ← Pi.single_mul, Matrix.single_mul_single_same, one_mul]

theorem primIdem_ne_zero (lam : Nat.Partition (n + 1)) (i : Fin (dim n lam)) :
    primIdem q hq0 hq2 n lam i ≠ 0 := by
  unfold primIdem
  rw [map_ne_zero_iff _ (Ψ q hq0 hq2 n).symm.injective]
  intro h
  have := congrFun h lam
  rw [Pi.single_eq_same, Pi.zero_apply] at this
  have h2 := congrFun (congrFun this i) i
  simp at h2

/-- The block trace of a block matrix unit is the block's weight. -/
theorem tr_single_single (w : Nat.Partition (n + 1) → K) (lam : Nat.Partition (n + 1))
    (i : Fin (dim n lam)) :
    tr w (Pi.single lam (Matrix.single i i (1 : K)) : Blocks K (dim n)) = w lam := by
  unfold tr
  rw [Finset.sum_eq_single lam]
  · rw [Pi.single_eq_same, Matrix.trace_single_eq_same, mul_one]
  · intro μ _ hμ
    rw [Pi.single_eq_of_ne hμ, Matrix.trace_zero, mul_zero]
  · intro h
    exact absurd (Finset.mem_univ lam) h

/-- **Any weighted seminormal trace takes the value `w_λ` on a primitive idempotent of `λ`.** -/
theorem wtraceW_primIdem (w : YoungDiagram → K) (lam : Nat.Partition (n + 1))
    (i : Fin (dim n lam)) :
    SeminormalRep.wtraceW q hq0 hq2 w n (primIdem q hq0 hq2 n lam i) = w (partitionShape lam) := by
  rw [← tr_Ψ_weight, primIdem, AlgEquiv.apply_symm_apply]
  exact tr_single_single n (fun lam => w (partitionShape lam)) lam i

/-- **The convention-D Markov trace of a primitive idempotent is the block weight.** -/
theorem markov_primIdem (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (lam : Nat.Partition (n + 1)) (i : Fin (dim n lam)) :
    T.tr n (primIdem q hq0 hq2 n lam i) = wD q n lam := by
  rw [markov_eq_tr q hq0 hq2 n (GenericParameter.sq_add_one_ne_zero hq2)
      (gen_of_notRootOfUnity hq2) T, primIdem, AlgEquiv.apply_symm_apply]
  exact tr_single_single n (wD q n) lam i

/-- **The quantum trace of a primitive idempotent is the `U_q(sl₂)` dimension.** On a two-row
block `(m, k)`, `(q − q⁻¹) · (q + q⁻¹)^{n+1} · T(e_{λ,i}) = q^{m−k+1} − q⁻¹^{m−k+1}`, i.e.
`[2]_q^{n+1} · T(e_{λ,i}) = [m − k + 1]_q`. -/
theorem quantumDim_primIdem_twoRow
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (lam : Nat.Partition (n + 1)) (i : Fin (dim n lam)) {m k : ℕ} (hkm : k ≤ m)
    (hshape : partitionShape lam = twoRow m k hkm) :
    (q - q⁻¹) * (q + q⁻¹) ^ (n + 1) * T.tr n (primIdem q hq0 hq2 n lam i)
      = q ^ (m - k + 1) - q⁻¹ ^ (m - k + 1) := by
  have hcard : m + k = n + 1 := by
    have h1 := QOU.Mathlib.partitionShape_card lam
    rw [hshape, card_twoRow] at h1
    exact h1
  have hgenN : ∀ i : ℕ, 0 < i → (q ^ 2 : K) ^ i ≠ 1 := fun i hi => by
    have := gen_of_notRootOfUnity hq2 (i : ℤ) (by exact_mod_cast hi.ne')
    rwa [zpow_natCast] at this
  have hW := SpinSector.ocneanuWeight_twoRow_conventionD q hq0 (GenericParameter.sq_add_one_ne_zero hq2)
    hgenN hkm
  rw [markov_primIdem, wD, hshape, ← hcard, ← hW]
  ring

/-- **Term 4 with the mass definition's own dimension.** Take `dim_q(λ) = [2]_q^{n+1} · w_λ`,
the quantum trace of a primitive idempotent of `λ`. Then every Markov trace at `z_D` gives
`T(C°) = Σ_{λ ⊢ n+1, ℓ(λ) ≤ 2} 1 / dim_q(λ)`. -/
theorem tr_cHecke_quantumDim
    (T : HeckeCoset.MarkovTraceFamily K q q⁻¹ (q ^ 3 / (q ^ 2 + 1)))
    (hd : ∀ lam, (dim n lam : K) ≠ 0) :
    T.tr n (cHecke q hq0 hq2 n (fun lam => (q + q⁻¹) ^ (n + 1) * wD q n lam))
      = ∑ lam ∈ univ.filter (fun lam : Nat.Partition (n + 1) =>
          (partitionShape lam).colLen 0 ≤ 2), 1 / ((q + q⁻¹) ^ (n + 1) * wD q n lam) := by
  have hq21 := GenericParameter.sq_add_one_ne_zero hq2
  have hgen := gen_of_notRootOfUnity hq2
  have h2 : q + q⁻¹ ≠ 0 := by
    intro h
    apply hq21
    have : q * (q + q⁻¹) = q ^ 2 + 1 := by field_simp
    rw [h, mul_zero] at this
    exact this.symm
  refine tr_cHecke q hq0 hq2 n hq21 hgen T _ hd (fun lam hlam => ?_)
  exact mul_ne_zero (pow_ne_zero _ h2) ((wD_ne_zero_iff q hq0 n hq21 hgen lam).mpr hlam)

/-- **The symmetrising trace of a primitive idempotent.**
`τ₀(e_{λ,i}) = q^{−κ(λ)} / ∏_{x ∈ λ} [h(x)]_q`. -/
theorem symTrace_primIdem (lam : Nat.Partition (n + 1)) (i : Fin (dim n lam)) :
    HeckeCoset.symTrace q q⁻¹ n (primIdem q hq0 hq2 n lam i)
      = q ^ (-molienContentSum (partitionShape lam))
          / ∏ x ∈ (partitionShape lam).cells,
              QOU.QInteger.qIntBal q (QOU.QBeta.WenzlWeight.hook (partitionShape lam) x) := by
  rw [← SeminormalRep.molien_eq_symTrace q hq0 hq2 n, wtraceW_primIdem,
    molienWeight_eq_balanced q hq0 (GenericParameter.sq_ne_one hq2)]

/-- **The hook formula is the symmetrising trace's weight, up to `q^{−κ}`.**
`[n+1]_q! · τ₀(e_{λ,i}) = q^{−κ(λ)} · [n+1]_q! / ∏_{x ∈ λ} [h(x)]_q`. -/
theorem qFact_mul_symTrace_primIdem (lam : Nat.Partition (n + 1)) (i : Fin (dim n lam)) :
    (∏ j ∈ range (n + 1), QOU.QInteger.qIntBal q (j + 1))
        * HeckeCoset.symTrace q q⁻¹ n (primIdem q hq0 hq2 n lam i)
      = q ^ (-molienContentSum (partitionShape lam))
          * ((∏ j ∈ range (n + 1), QOU.QInteger.qIntBal q (j + 1))
            / ∏ x ∈ (partitionShape lam).cells,
                QOU.QInteger.qIntBal q (QOU.QBeta.WenzlWeight.hook (partitionShape lam) x)) := by
  rw [symTrace_primIdem]
  ring

end

end QOU.MassTheory.CoCasimirHecke
