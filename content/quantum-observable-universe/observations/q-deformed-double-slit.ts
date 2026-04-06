import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:local-substrate-q",
  label: "rem:q-deformed-double-slit",
  title: "Macroscopic scattering and the $q$-deformed double slit",
  uses: [
    "prop:local-substrate-q",
    "ex:photon-wavefront",
  ],
  tags: ["double-slit", "q-deformation", "scattering", "reeb", "torsion", "dirac", "wavefront"],
  simulator: { ref: "sim:q-double-slit" },
});
