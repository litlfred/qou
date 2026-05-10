import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:mostow-confinement",
  label: "rem:algebraic-geometric-rigidity-pairing",
  title:
    "Algebraic and geometric rigidity: SDPSlaterUniqueness paired with MostowRigidity",
  uses: [
    "prop:confinement-sdp",
    "conj:gb-reduction-pl-thimble-bijection",
    "def:archimedean-realization-functor",
  ],
  cites: ["mostow1968", "thurston1978", "boyd-vandenberghe-2004"],
  tags: [
    "interpretation",
    "rigidity",
    "sdp-uniqueness",
    "mostow-rigidity",
    "conditional-class",
    "encounter",
  ],
});
