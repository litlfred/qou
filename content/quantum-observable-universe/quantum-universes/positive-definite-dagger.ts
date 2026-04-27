import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:positive-definite-dagger",
  title: "Frobenius dagger is positive-definite",
  lean: { ref: "qou:QOU.frobenius_dagger_positive_definite",
    validation: "not_checked",
  },
  uses: [
    "def:involutive-structure",
    "def:frobenius-pairing",
  ],
  proofs: ["prf:positive-definite-dagger"],
  tags: ["category-theory", "positive-definite", "frobenius"],
  rendered: [
    { mime: "image/svg+xml", url: "rendered/positive-definite-dagger-0.svg", blockIndex: 0, hash: "60707ebb7060" },
  ],
});
