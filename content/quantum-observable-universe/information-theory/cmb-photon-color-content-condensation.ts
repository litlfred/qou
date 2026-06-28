import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:cmb-boundary-datum",
  label: "rem:cmb-photon-color-content-condensation",
  title: "CMB condensation into particles via the Hecke self-energy",
  tags: [
    "cmb",
    "condensation",
    "reeb-flow",
    "hecke-algebra",
  ],
  uses: [
    "def:cmb-boundary-datum",
    "rem:breit-wheeler-vertex",
  ],
});
