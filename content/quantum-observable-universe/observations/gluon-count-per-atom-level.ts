import { remark } from "../../schema/builders";

export default remark({
  label: "rem:gluon-count-per-atom-level",
  title:
    "Per-nucleon gluon count is $1 \\sigma_0$ at the atom-level SDP (not $2 \\sigma_0$)",
  interprets: "prop:mass-endomorphism-tower",
  uses: [
    "prop:mass-endomorphism-tower",
    "prop:atomic-braid-mass",
    "prop:confinement-sdp",
  ],
  tags: [
    "gluon",
    "atom-level-sdp",
    "confinement",
    "nucleon-structure",
  ],
});
