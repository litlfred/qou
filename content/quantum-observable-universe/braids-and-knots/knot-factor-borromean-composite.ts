import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:knot-factor-borromean-composite",
  title:
    "Borromean-$k$ composite knot factor is $a = (1 - h^2)^k$",
  lean: {
    ref: "qou:QOU.BraidKnot.knot_factor_borromean",
    validation: "not_checked",
  },
  uses: ["cor:knot-factor-amphicheiral"],
  tags: [
    "knot-factor",
    "borromean",
    "brunnian",
    "helium-4",
    "composite",
    "tensor-product",
  ],
});
