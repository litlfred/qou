import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:knot-factor-amphicheiral",
  title:
    "Amphicheiral knot factor reduces to $a = 1 - h^2$",
  lean: {
    ref: "qou:QOU.BraidKnot.knot_factor_amphicheiral",
    validation: "not_checked",
  },
  uses: ["prop:knot-factor-spectral-form"],
  tags: [
    "knot-factor",
    "amphicheiral",
    "figure-eight",
    "alternating-block",
    "tritium",
    "helium-3",
  ],
});
