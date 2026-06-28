import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-neutron-properties",
  interprets: "def:categorical-neutron",
  title: "Neutron: NF construction, mass, transition, and charge",
  tags: ["neutron", "hadron", "baryon", "color-tube", "knot", "categorical"],
  uses: [
    "def:categorical-neutron",
    "def:categorical-proton",
    "def:up-quark",
    "def:down-quark",
  ],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
});
