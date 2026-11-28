import { definition } from "../../schema/builders";

export default definition({
  label: "def:collatz-contact-boundary",
  lean: {
    ref: "qou:QOU.Core.AlgebraicSubstrate.CollatzContactBoundary",
    validation: "not_checked",
  },
  title:
    "Collatz contact boundary and orbit contact average",
  uses: [
    "def:two-q-adic-valuation",
    "conj:q-collatz",
  ],
  tags: [
    "collatz",
    "contact-order",
    "boundary",
    "skein-module",
    "orbit-average",
  ],
  authorNotes: [
    { kind: "refined-framing", date: "2026-11-28", body: "Removed 'above the boundary converge; below diverge' (false: the fundamental cycle has <v>=1). Convention note added." },
  ],
});
