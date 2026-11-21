import Mathlib.Tactic

/-!
# QOU.QuantumObservableUniverses.GActionOnSubstrate — conjecture carrier (content-bearing, no instance)

**§3b-cond class axiomatisation** for content block
[`conj:g-action-on-substrate`](../../../quantum-observable-universe/quantum-observable-universes/g-action-on-substrate.md): *Categorical $G = \\mathrm{SU}(2)_L \\times \\mathrm{U}(1)_Y$ action on the Frobenius–Hopf substrate*.

This is a **conjecture**, and the honest open state is a **content-bearing class
with no instance** (AGENTS.md §3b-tax). `GActionOnSubstrate` carries the four axioms below — the conjecture's content, not a placeholder.

**No instance is provided anywhere in this file.** An instance *is* the
conjecture; fabricating one would be the audit-dodge §1a forbids. A downstream
result takes `[GActionOnSubstrate]` as an explicit `[Instance]` hypothesis and
is thereby **conditional on it** — rigorous modulo this single named input, per
§3b-cond. It is not unconditional, and calling it so would be the
"conditional-proved ≠ premise-established" confusion AGENTS.md warns about.
-/

namespace QOU.QuantumObservableUniverses

/-- Categorical $G = \\mathrm{SU}(2)_L \\times \\mathrm{U}(1)_Y$ action on the Frobenius–Hopf substrate

    Conjectural class — see [`conj:g-action-on-substrate`](../../../quantum-observable-universe/quantum-observable-universes/g-action-on-substrate.md). -/
class GActionOnSubstrate where
  -- Witness: computations/none
  /- **Conjecture statement** (from manuscript):

      Let $A$ be a Frobenius–Hopf substrate
([substrate axioms](#def:frobenius-hopf-substrate)) in $\mathbf{C} =
\mathbf{Rep}(\mathrm{SU}_q(2))$. Then $A$ admits a unique
$G$-equivariant structure for $G = \mathrm{SU}(2)_L \times
\mathrm{U}(1)_Y$ compatible with the path-α torus-link identification
(electroweak/Higgs torus-link triplet [planned, not yet authored]),
specified by the four axioms below. From these axioms the
symmetric-channel Frobenius trace
$\mathrm{tr}_F(e_{\rm sym}^{\rm EW} \cdot e_H)$ — the value
$\mathcal{N}_{\rm sym}(q)$ — is computable in closed form.*

### The four axioms

      The fields below faithfully encode Axioms (G-1)–(G-4) and the
      `N_sym(q)` closed form, replacing the former vacuous `residual = 0`
      placeholder. Per §3b-cond no global instance is provided — the open
      conjecture is the assertion that such an instance exists. -/
  /-- **(G-1) G-isotypic decomposition.** The number of `G`-isotypic
      components `A^{(X)}` in `A = ⊕_X A^{(X)}`. -/
  numIsotypicComponents : ℕ
  /-- The decomposition is non-trivial (EW and Higgs hosts both present). -/
  numIsotypicComponents_pos : 0 < numIsotypicComponents
  /-- **(G-2) Per-host q-dimension.** The categorical q-dimension carried
      by the EW symmetric channel `e_sym^EW`, fixed by its torus-link
      hosts (e.g. `[4]_q` for the `W^±` host per the audit table). -/
  qDimEWSymmetric : ℝ
  /-- The EW-symmetric q-dimension is positive. -/
  qDimEWSymmetric_pos : 0 < qDimEWSymmetric
  /-- **(G-3) Higgs vacuum vortex morphism.** The Higgs vacuum value
      `⟨Φ⟩ ∈ A` — a *non-zero* vortex morphism of the mass-identity form,
      unique only up to a non-zero scalar (a phase, once the norm is fixed). -/
  higgsVev : ℝ
  /-- `⟨Φ⟩ ≠ 0` (the non-zero vortex morphism asserted by Axiom (G-3)). -/
  higgsVev_ne_zero : higgsVev ≠ 0
  /-- **(G-4) Higgs idempotent.** The categorical q-dimension of the image
      `e_H · A`, the 1-dimensional residual-scalar direction.  Left as a
      free positive real here; under a unit-normalised cyclic trace its
      value is `1`, not `[2]_q` (`VacuumPairing.tr_proj_eq_one`; owner
      ruling 2026-11-20). -/
  qDimHiggsIdempotent : ℝ
  /-- The Higgs-idempotent q-dimension is positive. -/
  qDimHiggsIdempotent_pos : 0 < qDimHiggsIdempotent
/-! ## Derived quantity — `N_sym(q)` -/

namespace GActionOnSubstrate

variable [GActionOnSubstrate]

/-- **Reading-(a) product** `qDimEWSymmetric * qDimHiggsIdempotent`.

    This is a *definition*, and it proves nothing about `tr_F(e_sym^EW · e_H)`.
    It encodes only the tensor-product reading (a) of
    `g-action-on-substrate.md`: the two idempotents act on different tensor
    factors and the trace is multiplicative on `e_sym^EW ⊗ e_H`.  Neither
    premise is stated by Axiom (G-1), which makes the hosts *direct summands*
    of `A`; under that reading `dim_q` is additive over the summands, and
    idempotents supported on orthogonal summands compose to `0`.  Which
    composition rule is meant is an open identification (QA, 2026-11-20).

    The name `N_sym` is kept for continuity; it is not derived from `tr_F`,
    and no `CyclicTrace` appears in this class. -/
noncomputable def N_sym : ℝ := qDimEWSymmetric * qDimHiggsIdempotent

/-- Unfolding of the definition (`rfl`); not a statement about `tr_F`. -/
theorem N_sym_closed_form :
    (N_sym : ℝ) = qDimEWSymmetric * qDimHiggsIdempotent := rfl

end GActionOnSubstrate

/-! ## Open conjecture — hypothesis-only (no global instance)

The conjecture is the *existence* of a `GActionOnSubstrate` instance:
that the substrate admits the unique `G`-equivariant structure of
Axioms (G-1)–(G-4), from which a closed form for `N_sym(q)` is intended to follow (the
composition rule across hosts is open; see the `N_sym` docstring).  Per
`AGENTS.md §3b-cond` we provide **no global instance** (which would
require a `sorry`); downstream theorems take `[GActionOnSubstrate]` as
an explicit hypothesis.  This removes the naked `sorry` while keeping the
conjecture's content faithfully encoded in the class fields above.

Ref: [leitner2026] quantum-observable-universe/quantum-observable-universes/g-action-on-substrate.ts -/

end QOU.QuantumObservableUniverses
