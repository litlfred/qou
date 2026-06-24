import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:toffoli-transfer-matrix",
  proofs: ["prf:toffoli-transfer-matrix"],
  lean: { ref: "qou:QOU.Information.toffoli_transfer_matrix", validation: "not_checked" },
  title:
    "The massive Toffoli transfer matrix $M(q)$ and the q-AND polynomial $P_{7,6}(q)$",
  tags: [
    "toffoli",
    "transfer-matrix",
    "q-AND",
    "hecke-algebra",
    "destructive-interference",
    "planck-computation",
    "braiding",
  ],
  uses: [
    "prop:skein-polynomial-transfer-matrix",
    "rem:discrete-planck-step",
  ],
});
