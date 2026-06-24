import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:qbeta-z-recursion-to-ck-recursion-bridge",
  title:
    "Bridge: $z$-Taylor recursion vs $c_k$ ladder recursion — structural correspondence",
  uses: [
    "prop:qbeta-per-block-chi-closed-forms",
    "prop:q-beta-c-k-recursion-from-habiro-q-difference",
  ],
  cites: ["habiro2004", "wenzl1988"],
  tags: [
    "qbeta",
    "z-recursion",
    "ck-recursion",
    "bridge",
    "pre-archimedean",
    "structural",
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.z_recursion_forward_form",
  },
});
