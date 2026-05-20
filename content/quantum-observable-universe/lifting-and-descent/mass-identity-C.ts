import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:mass-identity-C",
  lean: { ref: "qou:QOU.MassIdentityC", validation: "not_checked" },
  title: "Archimedean realisation: nonabelian multiplicative integration",
  proofs: ["prf:mass-identity-C"],
  tags: ["archimedean", "mass", "multiplicative-integral", "yekutieli"],
  uses: [
    "ex:c-quantum-observable-universe",
    "def:mass-identity",
  ],
  cites: [
    "yekutieli2015",
  ],
});
