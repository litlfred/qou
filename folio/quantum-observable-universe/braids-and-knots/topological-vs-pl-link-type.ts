import { remark } from "../../schema/builders";

/**
 * Relation between topological links and the PL link types of
 * def:polygonal-link-type (issue #8902). The C^1 comparison is proved in Lean;
 * the topological comparison is cited (Moise, Bing) and enters the Lean only
 * as the named hypothesis MoiseBing.
 */
export default remark({
  label: "rem:topological-vs-pl-link-type",
  title: "Topological links and polygonal link types",
  interprets: "def:polygonal-link-type",
  uses: ["def:polygonal-link-type"],
  cites: ["moise1952", "bing1954", "lickorish1997", "rolfsen"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-22",
      body: "Lean status (#8902): $\\Delta$-equivalence $\\Rightarrow$ PL ambient isotopy is proved (`DeltaEquiv.plAmbientIsotopic`); the converse, PL ambient isotopy $\\Rightarrow$ $\\Delta$-equivalence, is being formalised on PR #9067 and is cited (Reidemeister, Lickorish Ch. 1) until it lands. `MoiseBing` is a named hypothesis, not an axiom.",
    },
  ],
  lean: { ref: "qou:QOU.MathlibExt.PL.AmbientIsotopic.linkType_eq_of_moiseBing" },
  tags: ["link-type", "tame-link", "moise", "ambient-isotopy", "pl-topology"],
});
