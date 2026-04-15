import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:local-substrate-q",
  label: "rem:q-deformed-double-slit",
  title: "Macroscopic scattering and the $q$-deformed double slit",
  uses: [
    "prop:local-substrate-q",
    "ex:photon-wavefront",
    "rem:knot-basis-color-content",
    "rem:breit-wheeler-vertex",
    "def:double-slit-q-phase",
  ],
  tags: ["double-slit", "q-deformation", "scattering", "reeb", "torsion", "dirac", "wavefront", "color-content"],
  simulator: { ref: "sim:q-double-slit" },
  rendered: [
    { mime: "image/svg+xml", url: "rendered/q-deformed-double-slit-0.svg", blockIndex: 0, hash: "e42bbb900922" },
  ],

});
