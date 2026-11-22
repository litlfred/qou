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
  cites: ["moise1952", "bing1954", "lickorish1997"],
  lean: { ref: "qou:QOU.MathlibExt.PL.AmbientIsotopic.linkType_eq_of_moiseBing" },
  tags: ["link-type", "tame-link", "moise", "ambient-isotopy", "pl-topology"],
});
