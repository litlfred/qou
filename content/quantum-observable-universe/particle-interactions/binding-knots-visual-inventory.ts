import { remark } from "../../schema/builders";

export default remark({
  label: "rem:binding-knots-visual-inventory",
  title: "Visual inventory of binding knots",
  interprets: "prop:knot-particle-correspondence",
  tags: [
    "knot",
    "diagram",
    "visual",
    "inventory",
    "unknot",
    "hopf-link",
    "trefoil",
    "figure-eight",
    "borromean",
    "braid-word",
  ],
  uses: [
    "rem:knot-particle-dictionary",
    "def:localized-knot",
    "def:atomic-braid",
    "def:borromean-baryon",
  ],
});
