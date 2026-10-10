import { definition } from "../../schema/builders";

export default definition({
  label: "def:local-q-zeta-function",
  title: "Local $q$-zeta function of Bring's curve",
  lean: { ref: "qou:QOU.AlgebraicSubstrate.LocalQZetaFunction",
    validation: "not_checked",
  },
  uses: ["def:brings-coordinate-ring", "def:substrate-parameter-planck"],
  defines: ["local-q-zeta-function"],
  tags: [
    "zeta-function",
    "local",
    "brings-curve",
    "characteristic-polynomial",
    "frobenius-endomorphism",
  ],
});
