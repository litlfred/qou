import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:kelvin-dispersion-derivation",
  label: "rem:kelvin-dispersion-derivation-interpretation",
  title: "Exact $q$-derivative yields doubly-exponential UV suppression",
  uses: ["prop:kelvin-dispersion-derivation"],
  authorNotes: [
    {
      kind: "note",
      body: "Mathematical novelty: evaluating D_q against classical Kelvin-wave dispersion generates doubly-exponential UV suppression (τ_k ~ q^{-2k}) uniform in the fluid bulk without phenomenological regularisation or ad-hoc cutoffs.",
    },
  ],
});
