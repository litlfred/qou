import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:wigner-coefficient-derivation",
  proofs: ["prf:wigner-coefficient-derivation"],
  title: "Wigner coefficient $[5]_q! \\cdot m_e$ from Frobenius reciprocity",
  lean: { ref: "qou:QOU.BraidKnot.wigner_coefficient", validation: "not_checked" },
  uses: ["prop:wedderburn-trace-identity"],
  tags: ["wigner", "isospin", "casimir", "quantum-factorial", "frobenius-reciprocity"],
});
