import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:em-spectral-completeness",
  title:
    "Two-strand spectral completeness over a commutative ring $R$",
  lean: {
    ref: "qou:QOU.Archimedean.em_spectral_completeness",
    validation: "not_checked",
  },
  uses: ["prop:wedderburn-trace-identity"],
  computation: {
    engine: "python",
    script: "computations/rt_c23_singlet_sign_core.py",
    witness: "computations/rt-c23-singlet-sign-core.witness.json",
    status: "verified",
  },
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
