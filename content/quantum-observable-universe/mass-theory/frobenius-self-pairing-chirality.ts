import { definition } from "../../schema/builders";

export default definition({
  label: "def:frobenius-self-pairing-chirality",
  title:
    "Frobenius self-pairing chirality factor $a_K(\\beta) = \\tau(\\beta\\beta^{\\ast})/\\tau(1)$",
  lean: {
    ref: "qou:QOU.BraidKnot.chiralityFactor",
    validation: "not_checked",
  },
  uses: [],
  cites: ["jones1987"],
  tags: [
    "chirality",
    "frobenius",
    "self-pairing",
    "antipode",
    "categorical",
  ],
});
