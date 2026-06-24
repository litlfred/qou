import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:em-spectral-completeness",
  proofs: ["prf:em-spectral-completeness"],
  title:
    "Two-strand spectral completeness over a commutative ring $R$",
  lean: {
    ref: "qou:QOU.Archimedean.em_spectral_completeness",
    validation: "not_checked",
  },
  uses: ["prop:wedderburn-trace-identity"],
  tags: [
    "spectral-completeness",
    "wedderburn",
    "central-idempotent",
    "frobenius",
    "commutative-ring",
    "two-strand",
    "gauge-channel",
    "uniqueness",
  ],
});
