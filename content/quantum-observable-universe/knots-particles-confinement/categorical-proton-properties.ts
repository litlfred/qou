import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-proton-properties",
  interprets: "def:categorical-proton",
  title: "Proton: NF construction, mass, charge, and computational backing",
  tags: ["proton", "hadron", "baryon", "color-tube", "knot", "categorical"],
  uses: ["def:categorical-proton", "conj:borromean-quark"],
  cites: ["manuscript"],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
});
