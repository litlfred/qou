import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:local-substrate-q",
  label: "rem:q-deformed-double-slit",
  title: "Macroscopic scattering and the $q$-deformed double slit",
  uses: [
    "ex:photon-wavefront",
    "rem:breit-wheeler-vertex",
    "def:double-slit-q-phase",
  ],
  tags: ["double-slit", "q-deformation", "scattering", "reeb", "torsion", "dirac", "wavefront", "color-content"],
  simulator: { ref: "sim:q-double-slit" },
});
