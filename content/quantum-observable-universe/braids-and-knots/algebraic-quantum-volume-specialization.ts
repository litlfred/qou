import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:algebraic-volume-specialization",
  lean: {
    decl: "QOU.BraidsAndKnots.algebraic_volume_specialization",
    validation: "not_checked",
  },
  title: "Specialisation of the algebraic quantum volume",
  uses: [
    "def:algebraic-quantum-volume",
    "def:habiro-ring",
    "prop:binding-scale-catalan",
    "thm:topological-mass",
  ],
});
