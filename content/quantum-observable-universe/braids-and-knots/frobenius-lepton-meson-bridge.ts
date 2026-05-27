import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:frobenius-lepton-meson-bridge",
  title:
    "Frobenius restriction: $V_{(2,1)} \\!\\downarrow_{H_2} = V_{(2)} \\oplus V_{(1,1)}$",
  lean: { ref: "qou:QOU.BraidsAndKnots.standard_restricts_to_both_leptons" },
  uses: [
    "prop:lepton-meson-torus-knot-dictionary",
    "prop:c-equals-bar-iff-all-1dim",
    "def:categorical-meson",
  ],
  cites: [
    "wenzl1988hecke",
    "jones1987",
  ],
  tags: [
    "frobenius-reciprocity",
    "branching",
    "lepton",
    "meson",
    "standard-representation",
    "entanglement",
    "hoefsmit",
  ],
});
