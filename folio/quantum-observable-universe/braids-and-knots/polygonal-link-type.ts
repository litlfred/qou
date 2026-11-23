import { definition } from "../../schema/builders";

/**
 * The meaning of "link type" in this paper: the Delta-equivalence (PL ambient
 * isotopy) class of a polygonal link. Added so that "isotopic" in the
 * Alexander--Markov remarks names a category (issue #8902). No sibling .lean:
 * the definition lives in the library tree (no-shadowing rule, AGENTS.md §0a).
 */
export default definition({
  label: "def:polygonal-link-type",
  title: "Polygonal links and link types",
  defines: ["polygonal-link", "link-type"],
  lean: { ref: "qou:QOU.MathlibExt.PL.PolygonalLinkType" },
  cites: ["lickorish1997", "rolfsen"],
  tags: ["link-type", "polygonal-link", "pl-topology", "delta-move", "ambient-isotopy"],
});
