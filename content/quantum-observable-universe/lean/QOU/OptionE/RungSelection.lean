import QOU.OptionE.CrystalGraph
import Mathlib.Data.Nat.Basic

/-!
# `QOU.OptionE.RungSelection` — Canonical rung-selection at k ≥ 3

**Option E infrastructure file 2/4** — canonical (non-fitted)
rung-selection function from crystal-graph data.

The k=2 truncation of the τ_M Kashiwara derivation drops k ≥ 3
rungs as "non-canonical" — meaning no derivation rule from
substrate gives them. Option E's substantive content is to
**derive** the k ≥ 3 rungs canonically from crystal-graph
structure.

## Candidate rule (this file)

Given a crystal graph `Γ` for partition `λ ⊢ n`, the canonical
rung-selection function `kCan : CrystalVertex → ℕ` is determined
by the **depth** of the vertex in the crystal's directed-graph
structure (= max distance from a source vertex along directed
edges).

The substrate-derivation property requires:

1. `kCan` depends ONLY on the crystal-graph topology, NOT on
   AME measurements.
2. `kCan(v) ≥ 3` for vertices below the k=2 horizon in the
   crystal's longitudinal grading.
3. The induced Δ_λ derived from `kCan`-weighted sums closes the
   AME light-isotope binding-energies at the 10% threshold.

This file provides the framework + a candidate rule. Verification
that the candidate rule actually closes deuteron lives in
`DeuteronVerification.lean`.

Refs:
- [manuscript] docs/audits/2026-05-18-delta-lambda-gating-context.md
- [kashiwara1991] DOI 10.1215/S0012-7094-91-06321-0
-/

namespace QOU.OptionE.RungSelection

open QOU.OptionE.CrystalGraph

/-- **Canonical rung-selection function** signature: given a
    crystal vertex, return its canonical rung index. -/
structure RungRule (n : ℕ) where
  /-- The rung assignment: vertex → rung index. -/
  k : CrystalVertex n → ℕ
  /-- Substrate-derivation property: the rule depends only on
      crystal-graph topology (not on AME data). Encoded
      abstractly: the rule does not directly reference any real-
      valued AME constant. -/
  substrate_derived : Prop

/-- **Candidate rule (depth-based)**: for each vertex `v`, the
    rung `k(v)` is the depth of `v` in the crystal graph,
    counted from the source. The depth function is defined
    abstractly here; concrete values come from per-partition
    crystal-graph data. -/
def depthBasedRule (n : ℕ) (Γ : CrystalGraph n) : RungRule n where
  k v := v.idx + 1  -- placeholder depth function; concrete:
                    -- depth = max distance from source along edges
  substrate_derived := True  -- placeholder; concrete: derivable from Γ

/-- **Verification**: the depth-based rule assigns rung 1 to the
    source vertex (idx 0), rung 2 to the next, etc. -/
theorem depthBasedRule_source_rung
    (n : ℕ) (Γ : CrystalGraph n) :
    (depthBasedRule n Γ).k ⟨0⟩ = 1 := by
  unfold depthBasedRule
  rfl

/-- The depth-based rule assigns rung 2 to vertex with idx 1. -/
theorem depthBasedRule_second_rung
    (n : ℕ) (Γ : CrystalGraph n) :
    (depthBasedRule n Γ).k ⟨1⟩ = 2 := by
  unfold depthBasedRule
  rfl

/-- **Verification**: the depth-based rule assigns rung 3 to the third vertex
    (idx 2), continuing the `source_rung` / `second_rung` pattern.

    NOTE: on the current **placeholder** depth function `k v := v.idx + 1` this
    holds for every `Γ`; the previous `depthBasedRule_reaches_k3` carried an
    **unused** `h : 3 ≤ Γ.vertexCount` and a "k ≥ 3 reach property" docstring it
    did not establish. The substantive "substrate-derived k ≥ 3" content — that
    the *concrete* crystal-graph depth reaches 3 below the k = 2 horizon — is the
    open Option-E goal (property 2 in the header), not this placeholder unfolding. -/
theorem depthBasedRule_third_rung
    (n : ℕ) (Γ : CrystalGraph n) :
    (depthBasedRule n Γ).k ⟨2⟩ = 3 := by
  unfold depthBasedRule
  rfl

end QOU.OptionE.RungSelection
