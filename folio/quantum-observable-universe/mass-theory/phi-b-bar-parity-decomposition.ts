import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phi-b-bar-parity-decomposition",
  title: "Bar-parity (sinh/cosh) decomposition under the bar involution",
  // See `toroidal-harmonics-delta-lambda.ts` — `is_mathematics` is not a
  // schema field, so as a top-level key it was silently stripped. `meta` is
  // the declared escape hatch and keeps the declaration.
  meta: { is_mathematics: true },
  lean: { ref: "qou:QOU.QBeta.bar_parity_decomposition" },
  uses: []
});
