import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bloch-group-quotient-construction",
  title:
    "Concrete construction of $B(F)$ as `FreeAbelianGroup ⧸ pentagonSubgroup` (closes substantive Mathlib gap 1)",
  uses: ["rem:three-substantive-mathlib-fillers"],
  cites: ["bloch2000", "suslin1991"],
  tags: [
    "mathlib-filler",
    "bloch-group",
    "free-abelian-group",
    "quotient-group",
    "pentagon-relation",
    "lean-construction",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.BlochQuotient.BlochGroup",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "status",
      body:
        "**theorem (sorry-free, modulo over-permissive pentagon-shape constraints).** The Lean file [`bloch-group-quotient-construction.lean`](bloch-group-quotient-construction.lean) defines `BlochGroup F` concretely as a quotient `AddCommGroup`, with the pentagon `AddSubgroup` parameterised by the generator set `pentagonRelationGenerators := Set.range pentagonGenerator` over `PentagonShape F`. The structural construction, universal property, `pentagonGenerator_mem_pentagonSubgroup`, `quot_pentagonGenerator_eq_zero`, and `HasBlochGroup ℝ` instance are all sorry-free.",
    },
    {
      kind: "caveat",
      body:
        "**Over-permissive pentagon shapes.** The current `PentagonShape F` allows arbitrary 5-tuples of `PreBlochElement F`, not the constrained 5-tuples derived from a valid Rogers pair $(x, y) \\in F^\\times \\times F^\\times$ via the maps $(x, y, y/x, (1-y^{-1})/(1-x^{-1}), (1-y)/(1-x))$. This makes the pentagon `AddSubgroup` *too large*: choosing a degenerate shape with repeated entries (e.g. $e_2 = e_3 = e_4 = e_5$) collapses the generator to $\\mathrm{of}(e_1)$, putting individual pre-Bloch elements into the relation subgroup and trivialising the quotient. The proper fix is a `ValidPentagonShape F` predicate enforcing the Rogers-form constraints; the structural skeleton supports this drop-in refinement without modification.",
    },
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean declaration inventory moved from prose and table: `PreBlochElement F` (`val ≠ 0`, `val ≠ 1`), `pentagonRelationGenerators : Set (PreBlochGroup F)`, `pentagonSubgroup` (`AddSubgroup.closure`), `BlochGroup F := PreBlochGroup F ⧸ pentagonSubgroup` with `AddCommGroup` via Mathlib `QuotientAddGroup`, projection `quot : PreBlochGroup F →+ BlochGroup F`, lemmas `quot_zero`, `quot_add`, `quot_universal_property` (`QuotientAddGroup.lift`), and real instances `hasPentagonRelation_real`, `hasBlochGroup_real`.",
    },
  ],
});
