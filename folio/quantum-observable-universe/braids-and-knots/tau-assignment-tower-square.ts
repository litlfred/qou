import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:tau-assignment-tower-square",
  lean: {
    ref: "qou:QOU.Machinery.HeckeGeneral.tauAssignment_tower_natural",
    validation: "not_checked",
  },
  title:
    "The $\\tau$-assignment tower square: $H_3 \\hookrightarrow H_4$ compatibility",
  tags: [
    "hecke-algebra",
    "markov-trace",
    "monodromy",
    "tower-inclusion",
    "hodge-lift",
  ],
  uses: ["thm:jones-markov-trace", "prop:coxeter-parabolic-transversal"],
  cites: ["jones1987", "kassel1995"],
});
