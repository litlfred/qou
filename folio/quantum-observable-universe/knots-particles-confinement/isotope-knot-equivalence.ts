import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:isotope-knot-equivalence",
  title: "A reflexive, symmetric, transitive isotope relation is an equivalence",
  lean: { ref: "qou:QOU.BraidKnot.IsotopeKnot.equivalence",
    validation: "not_checked",
  },
  uses: ["def:isotope-knot"],
  tags: ["equivalence-relation", "isotope", "atom-knot"],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-22",
      body: "**Statement restated 2026-11-22 to what the Lean proves (owner ruling, round-trip pass 3).** `EquivalenceContext` carries reflexivity, symmetry and transitivity of `isotope` as fields (`claim_reflexivity`, `claim_symmetry`, `claim_transitivity`) on an abstract type; the theorem assembles them into `Equivalence`. Nothing connects `isotope` to the NF block decomposition of def:isotope-knot. The former statement asserted the isotope relation itself is an equivalence. The audit also noticed that def:isotope-knot requires N₁ ≠ N₂, which as written makes the relation irreflexive; a real proof would need the definition to allow N₁ = N₂ (or to take the reflexive closure). Found by the blind round-trip audit (docs/audits/2026-11-22-roundtrip-blind-audit-pass3.md, block P18).",
    },
  ],
});
