import { definition } from "../../schema/builders";

export default definition({
  label: "def:local-shadow-ordering",
  title: "Local shadow-price ordering $\\preceq_q$",
  lean: {
    decl: "QOU.BraidKnot.LocalShadowOrdering",
    validation: "not_checked",
  },
  uses: [
    "def:knot-operator-energy",
    "prop:bw-coefficient-shadow-price",
    "def:confinement-level",
    "def:unstable-atom",
    "prop:mass-endomorphism-tower",
  ],
  tags: [
    "ordering",
    "shadow-price",
    "open-neighborhood",
    "continuity",
    "phase-boundary",
  ],
});
