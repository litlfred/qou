import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:coxeter-geometric-representation",
  lean: {
    ref: "qou:QOU.Machinery.CoxeterParabolic.simple_injective",
    validation: "not_checked",
  },
  title:
    "The geometric representation: simple-injectivity at every Coxeter system",
  tags: [
    "coxeter",
    "geometric-representation",
    "faithfulness",
    "chebyshev",
    "hecke-algebra",
  ],
  uses: [
    "prop:coxeter-tits-residue-collapse",
    "prop:coxeter-parabolic-transversal",
  ],
  cites: ["kassel1995", "jones1987"],
});
