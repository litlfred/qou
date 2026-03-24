import { corollary } from "../../schema/builders";

export default corollary({
  label: "cor:mass-identity-C",
  lean: { decl: "QOU.MassIdentityC" },
  title: "Archimedean realisation: nonabelian multiplicative integration",
  tags: ["archimedean", "mass", "multiplicative-integral", "yekutieli"],
  uses: [
    "ex:c-quantum-observable-universe",
    "def:mass-identity",
  ],
});
