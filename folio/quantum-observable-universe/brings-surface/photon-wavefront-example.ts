import { example } from "../../schema/builders";

export default example({
  interprets: "def:localized-knot",
  label: "ex:photon-wavefront",
  title: "Continuing example: photon wavefront through a double slit",
  tags: ["photon", "wavefront", "double-slit", "empty-knot", "diffraction", "color-content"],
  uses: [
    "rem:wavefront-propagation",
    "rem:instanton-on-shell",
    "rem:knot-basis-color-content",
  ],
});
