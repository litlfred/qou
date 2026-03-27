import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:substrate-parameter",
  label: "rem:q-deformed-double-slit",
  title: "Macroscopic scattering and the $q$-deformed double slit",
  uses: [
    "def:substrate-parameter",
    "prop:local-substrate-q",
    "def:localized-knot",
    "def:categorical-dirac-operator",
    "prop:variational-equations",
    "def:categorical-instanton",
    "rem:wavefront-propagation",
    "rem:instanton-on-shell",
    "ex:photon-wavefront",
    "def:fermion-boson-decomposition",
  ],
  tags: ["double-slit", "q-deformation", "scattering", "reeb", "torsion", "dirac", "wavefront"],
  simulator: { ref: "sim:q-double-slit" },
});
