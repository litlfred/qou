import { definition } from "../../schema/builders";

export default definition({
  label: "def:ew-interface-knot",
  title:
    "Electroweak interface knot $\\Delta_I$: categorical analog of inter-nucleon coupling",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.ew_interface_knot",
    validation: "not_checked",
  },
  uses: [
    "conj:hoefsmit-ew-cell-content",
    "conj:categorical-higgs-mechanism",
    "conj:categorical-linking-operation",
    "prop:atomic-mass-gb-nf",
    "rem:hecke-algebra-from-braiding",
  ],
  tags: [
    "interface-knot",
    "delta-I",
    "ew-coupling",
    "higgs-vev",
    "non-far-commutative",
    "categorical-physics",
  ],
});
