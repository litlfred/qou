import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:bar-apply-transfer",
  proofs: ["prf:bar-apply-transfer"],
  title:
    "Bar-transfer principle: one-sided bounds on bar-invariant properties extend for free",
  tags: [
    "bar-involution",
    "skew-symmetry",
    "transfer-principle",
    "stability-margin",
    "proof-reuse",
  ],
  lean: {
    ref: "qou:QOU.Archimedean.BarApplyTransfer.bar_apply_transfer",
    validation: "not_checked",
  },
  uses: ["prop:bar-t-duality-substrate"],
});
