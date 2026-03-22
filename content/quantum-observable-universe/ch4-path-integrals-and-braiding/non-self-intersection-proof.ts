import { proof } from "../../schema/builders";

export default proof({
  label: "prf:non-self-intersection",
  title: "Proof of Obstruction to self-intersection",
  uses: ["cor:non-self-intersection", "prop:mobius-energy", "rem:r-matrix-braiding"],
  lean: {
    decl: "QOU.NonSelfIntersection",
    validation: "not_checked",
  },
});
