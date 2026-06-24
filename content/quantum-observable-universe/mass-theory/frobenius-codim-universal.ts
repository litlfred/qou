import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:frobenius-codim-universal",
  proofs: ["prf:frobenius-codim-universal"],
  title:
    "Universal Frobenius co-dimension trace: $\\tau(C_{\\dim_q}) = \\sum_\\lambda 1/\\dim_q(\\lambda)$",
  lean: {
    ref: "qou:QOU.BraidKnot.frobenius_codim_universal",
    validation: "not_checked",
  },
  uses: ["prop:hook-weight-derivation"],
  cites: ["kassel1995"],
  tags: [
    "frobenius",
    "co-casimir",
    "self-dual",
    "quantum-dimension",
    "universal",
    "tqft",
    "theorem",
  ],
});
