/-!
# QOU.BraidKnot.WenzlAOperator — the Wenzl A-operator A^λ_{μν}(I)

Content-sibling formalisation of `def:wenzl-A-operator`
(`mass-theory/wenzl-A-operator.md`).  Names the operator data of
Wenzl 1988 Sub-lemma 2.1: for `λ ⊢ n = n₁ + n₂` and an inter-block
interface generator `I = σ_{n₁} ∈ H_n(q)`, its `(μ, ν)`-block is

    A^λ_{μν}(I) ∈ End(V_μ ⊗ V_ν)^{⊕ c^λ_{μν}}

where `c^λ_{μν}` is the Littlewood–Richardson coefficient
(`prop:lr-coefficient-hecke`).  The operator-valued Sub-lemma 2.1
(`prop:crystal-r-matrix-sub-lemma`) reads its `q → 0` pole order, and
the combiner convergence (`prop:operator-valued-combiner-convergence`)
accumulates its per-peel contributions.

The canonical numerical realisation is the bilinear-system extract
`folio-assistant/computations/a_operator/A_operator_extract_at_level.py`,
whose witnesses `A-operator-extract-h{n}-{iface}.witness.json` carry the
matrix entries.  This is a naming/structure block (no semantic claim
beyond the existence of the operator data), so it introduces no `sorry`.

Ref: [manuscript] prop:lr-coefficient-hecke
     [manuscript] prop:crystal-r-matrix-sub-lemma
     [wenzl1988] Wenzl, Invent. Math. 92 (1988) 349-383
     [hoefsmit1974] http://hdl.handle.net/2429/19407
-/

import Mathlib.Data.Nat.Basic

namespace QOU.BraidKnot

/-- Partition (weakly-decreasing part list); doc-sibling local alias. -/
abbrev WenzlPartition := List Nat

/-- **Wenzl A-operator** (`def:wenzl-A-operator`).

    Per Wenzl 1988 Sub-lemma 2.1, each inter-block interface generator
    `I = σ_{n₁}` decomposes per Wedderburn `(μ, ν)`-block as
    `A^λ_{μν}(I) ∈ End(V_μ ⊗ V_ν)^{⊕ c^λ_{μν}}`, with `c^λ_{μν}` the
    Littlewood–Richardson coefficient.  The class abstracts the operator
    data as a map from `(λ, μ, ν, interface-label)` to the block-operator
    slot together with its LR multiplicity; the bilinear-system extract
    supplies the concrete `End(V_μ ⊗ V_ν)^{⊕ c}` matrix entries. -/
class WenzlAOperator where
  /-- `A^λ_{μν}(I)`: the `(μ, ν)`-block operator slot of interface `I`,
      indexed by `(λ, μ, ν, interface-label)`.  The codomain is a
      placeholder; the numerical extract carries the endomorphism. -/
  block : WenzlPartition → WenzlPartition → WenzlPartition → String → Unit
  /-- LR multiplicity `c^λ_{μν}` — the dimension of the multiplicity
      space the block operator acts on. -/
  lrMultiplicity : WenzlPartition → WenzlPartition → WenzlPartition → Nat

end QOU.BraidKnot
