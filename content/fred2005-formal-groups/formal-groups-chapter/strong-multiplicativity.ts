import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:strong-multiplicativity",
  title: "Strong multiplicativity",
  lean: { ref: "fred2005:Fred2005.strong_multiplicativity_holds",
    validation: "not_checked",
  },
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-07",
      body: "The Lean backing `Fred2005.strong_multiplicativity_holds` is a named accessor for the `comul_hom` field of `NoncommutativeFormalGroup` — it projects the structure's own defining axiom. That was recorded in the Lean docstring on 2026-07-18, when the declaration's misleading unused hypotheses were removed; this block's prose still asserted the stronger [fred2005, Thm 4.12] claim (\"preserved under the GS deformation at every filtration degree\") until 2026-09-07. The statement now separates the two.",
      see: "docs/audits/2026-09-07-self-assuming-projection-reaches-the-paper.md",
    },
  ],
  tags: ["strong-multiplicativity", "frobenius", "comultiplication"],
  uses: [
    "def:non-commutative-formal-group",
    "def:grobner-shirshov-basis",
  ],
  cites: ["fred2005"],
});
