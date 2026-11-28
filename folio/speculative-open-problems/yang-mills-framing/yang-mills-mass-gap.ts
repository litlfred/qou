import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:yang-mills-mass-gap",
  title: "Categorical Yang--Mills existence and mass-gap dictionary conjecture",
  lean: {
    ref: "qou:QOU.LiftingDescent.MassGap.YangMillsMassGap",
    validation: "not_checked",
  },
  tags: [
    "tier:famous",
    "yang-mills",
    "mass-gap",
    "vacuum",
    "spectral-gap",
    "millennium",
    "kummer",
    "gm-torsion",
  ],
  cites: ["jaffe2006", "leitner2026"],
  uses: [
    "quantum-observable-universe:prop:vacuum-state",
    "quantum-observable-universe:prop:crossing-energy-gap",
    "quantum-observable-universe:rem:aether-gm-torsion",
    "quantum-observable-universe:rem:kummer-filtration-obstruction",
    "quantum-observable-universe:thm:qou-obstruction-reduction",
  ],
});
