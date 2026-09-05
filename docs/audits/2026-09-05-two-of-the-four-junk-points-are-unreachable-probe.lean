import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

/-!
# Two of the four junk points are UNREACHABLE — a correction to my own step-1 claim

PR #6839 reported *"the weaker-form count is FOUR, not the two anticipated"* and listed
four junk points in the archimedean twins. That count is **wrong in context**, and this
file is the correction.

`QOU.ArchimedeanSubstrateField` (`QuantumObservableUniverse/SubstrateParameter.lean:88`)
carries an axiom:

```lean
field_ge_one : ∀ (p : M), 1 ≤ field p
```

Every archimedean twin in `MathConstants.lean` takes an `ArchimedeanSubstrateField` and
evaluates at `sp.field p`. So `q ≥ 1` **always**, and a junk point at `q < 1` cannot be
reached through the library's own API.

| junk point | reachable under `1 ≤ q`? | verdict |
|---|---|---|
| `operationalEntropy` at `q = 0` | **no** | latent, not a live defect |
| `gravitationalConstant`'s `S_cell` at `q = 1/2` | **no** | latent, not a live defect |
| `speedOfLight` at `q = 1` | **YES** | **live defect** |
| `informationBandwidth` at `q = 1` | **YES** (and no structure constrains it there) | **live defect** |

**What I got wrong, and how.** I read the definitions and computed their junk points
correctly, then reported all four as defects without reading the *type's* axioms. The
corpus's own rule for this is the arity/claim-shape discipline — resolve the symbols to
their declarations and check what is actually being quantified over. A junk value at an
argument the type forbids is not a defect; it is unreachable code.

**What survives, and it is sharper than before.** `q = 1` satisfies `1 ≤ q`, and
`SubstrateParameter.lean`'s own docstring says *"`q(p) = 1` is the classical limit"* —
so it is not merely reachable but a named, meaningful point of the model. And
`speedOfLight`'s own docstring says it *"diverges at classicality (q → 1)"*. The
declaration returns `0` there. That is a live defect at a distinguished point, which
is a stronger finding than one of four generic ones.

-- Ref: [manuscript] §9/information-speed-of-light, §9/information-bandwidth
-/

namespace JunkReachability

/-- The classicality bound, as the structure states it. -/
structure SubstrateLike (M : Type*) where
  field : M → ℝ
  field_ge_one : ∀ p, 1 ≤ field p

/-! ## Unreachable: `q = 0` and `q = 1/2` are excluded by the bound -/

theorem zero_unreachable {M : Type*} (sp : SubstrateLike M) (p : M) :
    sp.field p ≠ 0 := by
  have h := sp.field_ge_one p
  linarith

theorem half_unreachable {M : Type*} (sp : SubstrateLike M) (p : M) :
    sp.field p ≠ 1 / 2 := by
  have h := sp.field_ge_one p
  intro hc
  rw [hc] at h
  norm_num at h

/-! ## Reachable: `q = 1` satisfies the bound

Not merely consistent with it — the bound is `1 ≤ q`, so `q = 1` is its boundary, and
the structure's docstring names it the classical limit. -/

/-- A substrate sitting exactly at classicality is a legitimate inhabitant. -/
def classicalSubstrate : SubstrateLike Unit where
  field := fun _ => 1
  field_ge_one := by intro p; norm_num

theorem one_is_reachable : classicalSubstrate.field () = 1 := rfl

/-- **The live defect, at the boundary the structure names.** `c_q = 1/(q−1)` is
documented to diverge as `q → 1`; evaluated at the classical substrate it returns `0`. -/
theorem speedOfLight_zero_at_classicality :
    (1 : ℝ) / (classicalSubstrate.field () - 1) = 0 := by
  show (1 : ℝ) / (1 - 1) = 0
  norm_num

end JunkReachability
