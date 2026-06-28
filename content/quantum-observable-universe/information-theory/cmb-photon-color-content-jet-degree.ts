import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:cmb-boundary-datum",
  label: "rem:cmb-photon-color-content-jet-degree",
  title: "Jet-degree decomposition of the photon color content",
  tags: [
    "photon",
    "jet-horizon",
    "color-content",
    "hecke-algebra",
  ],
  uses: [
    "def:cmb-boundary-datum",
    "rem:breit-wheeler-vertex",
  ],
});
