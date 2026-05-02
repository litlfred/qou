import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:force-carrier-knot-vs-link-dichotomy",
  title:
    "Saturating force-carriers are knots; broken-symmetry mediators are links",
  uses: [
    "prop:force-carrier-bring-uniqueness",
    "def:rigid-monoidal-category",
    "def:frobenius-hopf-substrate",
    "rem:hecke-algebra-from-braiding",
  ],
  tags: [
    "force-carrier",
    "matter-vs-force",
    "knot-vs-link",
    "saturation",
    "host-surface",
    "structural-premise",
    "open-problem",
  ],
});
