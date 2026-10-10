import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:chirality-residue-mass-term",
  label: "rem:chirality-residue-mass-term-interpretation",
  title: "Physical interpretation: the chirality channel as confining background",
  tags: ["chirality", "confinement", "mass-tower", "binding-energy", "gauge-invariant"],
  uses: [
    "prop:chirality-residue-mass-term",
    "rem:confinement-curvature-rank",
  ],
});
