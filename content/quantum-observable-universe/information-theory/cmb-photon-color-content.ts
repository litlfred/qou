import { remark } from "../../schema/builders";

export default remark({
  interprets: "def:cmb-boundary-datum",
  label: "rem:cmb-photon-color-content",
  title:
    "The CMB as photon color content surviving the horizon",
  tags: [
    "cmb",
    "photon",
    "color-content",
    "polarization",
    "jet-horizon",
    "hecke-algebra",
    "boundary-datum",
  ],
  uses: [
    "def:cmb-boundary-datum",
    "rem:breit-wheeler-vertex",
  ],
});
