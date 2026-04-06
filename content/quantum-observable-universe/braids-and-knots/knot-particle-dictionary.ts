import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:knot-particle-correspondence",
  label: "rem:knot-particle-dictionary",
  title: "Knot–particle dictionary",
  tags: [
    "knot",
    "particle",
    "dictionary",
    "mass",
    "borromean",
    "fermion",
    "boson",
    "torus-knot",
    "jones-polynomial",
  ],
  uses: [
    "def:localized-knot",
    "def:hadron",
    "prop:fermion-boson-knot-link",
    "rem:building-block-knots",
    "def:borromean-baryon",
  ],
});
