import { remark } from "../../schema/builders";

export default remark({
  label: "rem:physics-names-knot-operations",
  title: "Physics names $\\leftrightarrow$ categorical knot operations (table; depends on $q_0$)",
  interprets: "prop:confinement-categorical",
  uses: [
    "rem:borromean-baryon-interpretation",
    "prop:chirality-residue-mass-term",
    "cor:gauge-coupling-uniqueness",
    "conj:cp-violation-spectral-form",
  ],
  authorNotes: [
    {
      kind: "caveat",
      body: "Lookup table stored in physics-names.json; the SDP discovery run behind w_{(3,3,3,3)}(q_0) ~ 0.024 is not currently reproducible from repository scripts. Categorical interface references: prop:em-spectral-completeness, cor:gauge-coupling-uniqueness, prop:chirality-residue-mass-term.",
    },
  ],
  computation: {
    engine: "snappea",
    script: "computations/substrate/knot_volumes.py",
    witness: "computations/substrate/knot-volumes.witness.json",
    status: "verified",
  },
});
