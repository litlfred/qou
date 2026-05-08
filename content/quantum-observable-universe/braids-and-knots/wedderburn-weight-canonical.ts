import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wedderburn-weight-canonical",
  title:
    "Canonical Wedderburn-block weight $w_\\lambda$ and three named scalings",
  tags: [
    "wedderburn",
    "weight",
    "canonical",
    "bw",
    "shadow-price",
    "wenzl-bridge",
    "consolidation",
  ],
  uses: [
    "thm:wedderburn-mass-formula",
    "thm:jones-markov-trace",
    "prop:wedderburn-as-noncomm-fourier",
  ],
  cites: ["jones1985", "wenzl1988", "kassel1995"],
  lean: { ref: "qou:QOU.BraidKnot.wedderburnWeightCanonical" },
});
