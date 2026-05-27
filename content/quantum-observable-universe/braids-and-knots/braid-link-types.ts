import { remark } from "../../schema/builders";

export default remark({
  label: "rem:braid-link-types",
  title:
    "Track C Step A: concrete Lean Braid/Link types; the 2-strand case fully discharges Atom 1 of `rem:markov-closure-map-axiomatic` ($\\widehat{\\sigma^2} = $ Hopf link), and composes to a fully Lean-proved chain $\\sigma^2 \\to $ Hopf $\\to -2$",
  interprets: "rem:markov-closure-map-axiomatic",
  uses: [
    "prop:q-beta-c3-hopf-three-fold-markov",
    "rem:markov-closure-map-axiomatic",
    "rem:F3-eps6-leading-eq-neg-2b-cubed",
  ],
  cites: ["jones1985"],
  tags: [
    "lean-infrastructure",
    "track-C-step-A",
    "braid-group",
    "link-type",
    "markov-closure",
    "hopf-link-explicit",
    "class-discharge",
  ],
});
