import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:ugb-s-poly-decomposition",
  title: "S-polynomial decomposition",
  lean: { ref: "ugb:UGB.BuchbergerPBW.s_poly_decomposition", validation: "not_checked" },
  tags: ["groebner-basis", "s-polynomial"],
  uses: ["def:unital-groebner-basis", "def:admissible-system"],
});
