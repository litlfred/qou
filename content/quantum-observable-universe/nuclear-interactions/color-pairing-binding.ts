import { remark } from "../../schema/builders";

/**
 * Photon color content and degree-2 binding.
 */
export default remark({
  label: "rem:color-pairing-binding",
  title: "Degree-2 color pairing as binding energy",
  interprets: "thm:wedderburn-mass-formula",
  uses: ["def:color-tube-coordinates"],
});
