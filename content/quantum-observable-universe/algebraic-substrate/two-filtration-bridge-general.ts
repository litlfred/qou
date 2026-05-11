import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:two-filtration-bridge-general",
  title:
    "Two-filtration bridge map in full generality: bar-class determines iterated-integral depth (self-conj $\\to$ 2, chiral pair $\\to$ 3) for all partitions",
  uses: [
    "conj:two-filtration-bridge",
    "prop:two-filtration-bridge-small-cases",
    "rem:chirality-period-pairing",
    "prop:joint-galois-braid-discharged",
    "prop:hecke-baer-star-generic",
    "prop:explicit-central-idempotent",
    "prop:cyclotomic-cl3-orbit-sum-general",
    "prop:cyclotomic-trilog-imaginary-closed-form",
  ],
  cites: ["bloch2000"],
  tags: [
    "two-filtration-bridge",
    "general-partitions",
    "bar-eigenspace",
    "self-conjugate",
    "chiral-pair",
    "graded-mikusinski",
    "theorem-level",
  ],
});
