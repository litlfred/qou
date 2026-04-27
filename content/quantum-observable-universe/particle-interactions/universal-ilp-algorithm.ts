import { definition } from "../../schema/builders";

/**
 * Universal ILP algorithm for operator selection at every level.
 *
 * The same algorithm derives confinement (B₃), gluon (2σ₀),
 * electron attachment (σ₁⁻¹), and molecular bonding (inv trefoil).
 */
export default definition({
  label: "def:universal-ilp-algorithm",
  title: "Universal ILP algorithm for operator selection",
  lean: { ref: "qou:QOU.Interactions.UniversalILP",
    validation: "not_checked",
  },
  uses: [
    "prop:q-integer-mass-formula",
    "def:molecular-braid",
  ],
  tags: [
    "ILP",
    "operator-selection",
    "confinement",
    "gluon",
    "covalent-bond",
    "universal",
    "algorithm",
  ],
});
