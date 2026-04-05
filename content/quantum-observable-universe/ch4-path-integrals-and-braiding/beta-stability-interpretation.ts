import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:beta-stability",
  label: "rem:beta-stability-interpretation",
  title: "Derivation, verification, and limiting behaviour of beta-stability",
  tags: [
    "stability",
    "beta-decay",
    "valley-of-stability",
    "derivation",
  ],
  uses: ["prop:beta-stability", "def:skein-binding-lagrangian", "prose:knot-periodic-table"],
});
