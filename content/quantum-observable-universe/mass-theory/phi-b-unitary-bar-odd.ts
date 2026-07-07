import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:phi-b-unitary-bar-odd",
  title: "Unitary phases are bar-odd: the fibre-saddle rigidity",
  is_mathematics: true,
  lean: { ref: "qou:QOU.QBeta.IsSigmaUnitary.sq_eq_one_of_bar_even" },
  computation: {
    engine: "python+mpmath",
    script: "computations/qbeta/qbeta_fmap_phi_b_root_of_unity_reference.py"
  },
  uses: [
    "prop:phi-b-bar-parity-decomposition"
  ]
});
