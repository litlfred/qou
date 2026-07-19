import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:qdifference-kernel-prolongation-symbol",
  lean: {
    ref: "qou:QOU.Mass.QDifferenceKernelIsProlongationSymbol",
    validation: "validated",
  },
  title: "The q-difference kernel R is the jet-prolongation operator symbol",
  uses: [
    "prop:binding-genfun-qdifference",
    "prop:mi-sw-abelianisation",
    "prop:sw-period-residue-sum",
  ],
  tags: [
    "tier:keystone",
    "binding",
    "q-difference",
    "seiberg-witten",
    "jet-prolongation",
    "keystone",
    "step-9b",
  ],
});
