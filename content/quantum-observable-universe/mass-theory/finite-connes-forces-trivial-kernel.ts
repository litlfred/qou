import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:finite-connes-forces-trivial-kernel",
  title:
    "Finite Connes distance forces a trivial kernel --- hence the quotient by the radical",
  lean: {
    ref: "qou:QOU.QBeta.GramSignature.finite_distance_forces_trivial_kernel",
    validation: "not_checked",
  },
  uses: ["prop:gram-degeneracy-blocks-connes"],
  tags: ["connes-distance", "radical-quotient", "temperley-lieb"],
});
