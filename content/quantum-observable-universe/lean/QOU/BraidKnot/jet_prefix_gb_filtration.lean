import Mathlib.Tactic

/-!
# QOU.BraidKnot.jet_prefix_gb_filtration

**Canonical declaration** for content block
[`prop:jet-prefix-gb-filtration`](../../../quantum-observable-universe/braids-and-knots/jet-prefix-gb-filtration.md): *QOU.BraidKnot.jet_prefix_gb_filtration*.

This module states the manuscript claim over a context class so the `lean.ref` URI resolves to a real, compiling declaration in the `qou` Lake package (§3b-conditional). See the declaration docstring below for what the term discharges versus what is carried as a context-class axiom.
-/

namespace QOU.BraidKnot


/-- Abstract context for the `jet_prefix_gb_filtration` claim —
    manuscript-themed typed fields below; the residual `claim` field
    encodes the GB-filtration-jet-prefix proposition (truncated in the
    sibling .md). -/
class JetPrefixGbFiltrationContext where
  /-- The categorical object / monoidal structure. -/
  CategoricalObj : Type
  /-- The jet order index. -/
  JetOrder : ℕ
  /-- The GB-filtration depth. -/
  GbDepth : ℕ
  /-- Manuscript claim: the jet-prefix filtration order coincides with
      the GB-filtration depth. -/
  claim_jet_prefix_eq_gb_depth : JetOrder = GbDepth

/-- **Proposition statement** (from manuscript):

Define the

    The Lean encoding below states the manuscript claim over a context class and discharges it from the class's fields (§3b-conditional). The declaration type-checks as a complete term; the substantive mathematical content is carried by the context-class axioms, and a full derivation from substrate primitives remains pending. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/jet-prefix-gb-filtration.ts
def jet_prefix_gb_filtration [ctx : JetPrefixGbFiltrationContext] :
    ctx.JetOrder = ctx.GbDepth := ctx.claim_jet_prefix_eq_gb_depth

end QOU.BraidKnot
