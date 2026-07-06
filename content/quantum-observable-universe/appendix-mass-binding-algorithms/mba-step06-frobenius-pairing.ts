import { algorithm } from "../../schema/builders";

export default algorithm({
  label: "alg:frobenius-pairing",
  title: "Frobenius pairing $\\langle a, b\\rangle_F$ and self-duality $\\Psi = S^2 = \\mathrm{id}$",
  uses: [
    "def:frobenius-pairing",
    "prop:frobenius-pairing-exists",
    "prop:frobenius-pairing-unique",
  ],
  computation: {
    engine: "python",
    script: "computations/audit_frobenius_pairing.py",
    status: "verified",
  },
  tags: [
    "mba",
    "step-6",
    "frobenius-pairing",
    "self-duality",
    "rigid-monoidal",
    "canonical-chain",
  ],
});
