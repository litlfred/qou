import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:algebraic-volume-specialization",
  title: "Specialisation of the algebraic quantum volume",
  uses: [
    "def:algebraic-quantum-volume",
    "def:habiro-ring",
    "prop:binding-scale-catalan",
    "thm:topological-mass",
  ],
});
