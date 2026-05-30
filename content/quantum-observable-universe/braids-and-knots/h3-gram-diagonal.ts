import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:frobenius-gram-matrix",
  label: "rem:h3-gram-diagonal",
  title:
    "Symbolic diagonal of the Frobenius Gram matrix on $H_3(R, q)$",
  tags: [
    "hecke-algebra",
    "h3",
    "frobenius-gram-matrix",
    "markov-trace",
    "delta-lambda-closure",
    "option-e",
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.H3GramDiagonal",
    validation: "not_checked",
  },
  uses: ["prop:frobenius-gram-matrix"],
  cites: ["halverson_ram_1998", "jones1985", "wenzl1988"],
});
