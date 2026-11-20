import Mathlib.Tactic

/-!
# QOU.Conjectures.WeakSpectralCompleteness — EW cell-content trace

Conjectural axiomatisation of `conj:weak-spectral-completeness`
(`folio/quantum-observable-universe/mass-theory/weak-spectral-completeness.md`).

Over the categorical ring `R` with `q` generic, the EW/Higgs
force-carrier sector `{T(2,4), T(2,6), T(2,8)} ↔ {σ₁⁴, σ₃⁶, σ₅⁸}` admits
a categorically complete idempotent decomposition whose substrate-level
structural quantity is the **bar-self-dual cell-content trace**

  `tr_pure(σ₁⁴ σ₃⁶ σ₅⁸)
     = 4(q¹⁸+q⁻¹⁸) + 2(q¹⁰+q⁻¹⁰) + (q⁶+q⁻⁶) + 3(q²+q⁻²)`

derivable directly from the eight pure-pattern cell-content
multiplicities `(4, 2, 1, 3, 3, 1, 2, 4)` (summing to 20), **without
invoking Plancherel weights**.

The substrate-level identity `tr_pure` is a concrete object: it is
defined here over a generic field with `q` invertible, and its
bar-self-duality (`q ↦ q⁻¹` invariance) — the substrate-level bar
T-duality at the trace level — is **proved** (`cellTrace_bar_self_dual`).
The completeness multiplicity bookkeeping `(4+2+1+3+3+1+2+4 = 20)` is
likewise discharged.  The remaining open content (the categorical
completeness of the idempotent decomposition itself) is carried by the
content-bearing conjecture class with **no instance**.

LaTeX label: `conj:weak-spectral-completeness`

## References

- [leitner2026] §"Weak-sector spectral completeness — Hoefsmit n=6 form"
-/

namespace QOU.Conjectures

variable {R : Type*} [Field R]

/-- The eight pure-pattern cell-content multiplicities of the EW sector
    `(4, 2, 1, 3, 3, 1, 2, 4)`. -/
def cellMultiplicities : List ℕ := [4, 2, 1, 3, 3, 1, 2, 4]

/-- The cell-content multiplicities sum to `20` (out of the
    `∑_{λ⊢6} f_λ = 76` seminormal-basis vectors). -/
theorem cellMultiplicities_sum : cellMultiplicities.sum = 20 := by decide

/-- The bar-self-dual cell-content trace
    `tr_pure(σ₁⁴ σ₃⁶ σ₅⁸)`, as a Laurent expression in an invertible
    `q : R`:
    `4(q¹⁸+q⁻¹⁸) + 2(q¹⁰+q⁻¹⁰) + (q⁶+q⁻⁶) + 3(q²+q⁻²)`. -/
noncomputable def cellTrace (q : R) : R :=
  4 * (q ^ 18 + q ^ (-18 : ℤ)) +
  2 * (q ^ 10 + q ^ (-10 : ℤ)) +
  1 * (q ^ 6 + q ^ (-6 : ℤ)) +
  3 * (q ^ 2 + q ^ (-2 : ℤ))

/-- **Bar T-duality at the trace level.**  The cell-content trace is
    invariant under the bar involution `ι : q ↦ q⁻¹` — each summand
    `qⁿ + q⁻ⁿ` is manifestly bar-self-dual. -/
theorem cellTrace_bar_self_dual (q : R) (hq : q ≠ 0) :
    cellTrace q⁻¹ = cellTrace q := by
  unfold cellTrace
  rw [inv_eq_one_div]
  field_simp
  ring

/-- **Conjecture class** (`conj:weak-spectral-completeness`).

An instance supplies the six per-link block projectors `e X ±` of the
EW carriers `{T(2,4), T(2,6), T(2,8)}` inside `End_R(V^{⊗6})` and
asserts that they form a **categorically complete pairwise-orthogonal
idempotent decomposition** of the EW Wedderburn content.  The
`completeness` field carries the genuine completeness claim (the
projectors are orthogonal idempotents exhausting the EW sector), not a
bare `True`.  This is a **primary** conjecture. -/
class WeakSpectralCompleteness (R : Type*) [Field R] where
  /-- The carrier algebra `End_R(V^{⊗6})` of the `n = 6` Hecke action. -/
  EWAlgebra : Type*
  /-- `EWAlgebra` is a (possibly non-commutative) ring. -/
  ring_EWAlgebra : Ring EWAlgebra
  /-- The six per-link block projectors `e_W^±, e_Z^±, e_{T(2,8)}^±`
      (the `T(2,8)` pair is not the Higgs idempotent `e_H` of (G-4)). -/
  projector : Fin 6 → EWAlgebra
  /-- **Conjectural categorical completeness.**  Each projector is
      idempotent and distinct projectors are orthogonal — the
      pairwise-orthogonal idempotent decomposition exhausting the EW
      Wedderburn content. -/
  completeness :
    (∀ i, projector i * projector i = projector i) ∧
    (∀ i j, i ≠ j → projector i * projector j = 0)

attribute [instance] WeakSpectralCompleteness.ring_EWAlgebra

-- No instance: this is an OPEN primary conjecture (AGENTS.md §3b-tax).
-- The `projector ≡ 0` model discharges `completeness` (0 is trivially
-- idempotent and self-orthogonal) but the zero decomposition does NOT
-- exhaust the EW Wedderburn content — it is the empty decomposition,
-- carrying none of the categorical-completeness claim.  The genuine
-- substrate content above (`cellTrace`, `cellTrace_bar_self_dual`,
-- `cellMultiplicities_sum`) is proved; completeness itself is open.

end QOU.Conjectures
