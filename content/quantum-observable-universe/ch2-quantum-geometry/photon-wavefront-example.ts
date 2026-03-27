import { example } from "../../schema/builders";

export default example({
  interprets: "def:localized-knot",
  label: "ex:photon-wavefront",
  title: "Continuing example: photon wavefront through a double slit",
  tags: ["photon", "wavefront", "double-slit", "empty-knot", "diffraction"],
  uses: [
    "rem:wavefront-propagation",
    "rem:instanton-on-shell",
    "def:localized-knot",
    "def:categorical-dirac-operator",
    "def:substrate-parameter",
  ],
});
