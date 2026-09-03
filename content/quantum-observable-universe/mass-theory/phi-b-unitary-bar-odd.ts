import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phi-b-unitary-bar-odd",
  title: "Unitary phases are bar-odd: the fibre-saddle rigidity",
  // See `toroidal-harmonics-delta-lambda.ts` — `is_mathematics` is not a
  // schema field, so as a top-level key it was silently stripped. `meta` is
  // the declared escape hatch and keeps the declaration.
  meta: { is_mathematics: true },
  lean: { ref: "qou:QOU.QBeta.IsSigmaUnitary.sq_eq_one_of_bar_even" },
  computation: {
    engine: "python+mpmath",
    script: "computations/qbeta/qbeta_fmap_phi_b_root_of_unity_reference.py",
    status: "not_run"
  },
  uses: [
    "prop:phi-b-bar-parity-decomposition"
  ]
});
