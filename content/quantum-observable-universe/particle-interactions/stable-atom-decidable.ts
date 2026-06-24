import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:stable-atom-decidable",
  proofs: ["prf:stable-atom-decidable"],
  title: "Stability is decidable for any (Z, N) at fixed q",
  lean: { ref: "qou:QOU.BraidKnot.StableAtom.decidable",
    validation: "not_checked",
  },
  tags: ["decidability", "stability", "ilp", "atom"],
});
