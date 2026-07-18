import { remark } from "../../schema/builders";

export default remark({
  label: "rem:photon-ir-zero-mode-bring-mechanism",
  title: "Hodge mechanism, dimensional reduction, and Habiro placement of the photon IR zero-mode",
  interprets: "prop:photon-ir-zero-mode-bring",
  uses: [
    "prop:photon-ir-zero-mode-bring",
    "prop:force-carrier-bring-uniqueness",
    "prop:jet-sw-tau-decomposition",
    "prop:alpha-em-habiro-bar-involution",
  ],
  tags: ["alpha-em", "bring-surface", "hodge", "habiro", "photon-zero-mode"],
});
