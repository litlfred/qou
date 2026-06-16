import { example } from "../../schema/builders";

export default example({
  label: "ex:hadron-proton",
  title: "The proton as a Borromean hadron",
  interprets: "def:hadron",
  uses: ["ex:crossing-energy-trefoil"],
  tags: ["hadron", "proton", "borromean", "example"],
  computation: {
    engine: "python",
    script: "computations/codata_masses.py",
    witness: "computations/codata-masses.witness.json",
    status: "verified",
  },
});
