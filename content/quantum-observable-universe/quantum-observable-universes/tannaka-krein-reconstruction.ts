import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:tannaka-krein-reconstruction",
  title:
    "Tannaka--Krein reconstruction of the quantum gauge group",
  cites: ["woronowicz1988", "deligne1990", "tannaka1939", "kassel1995"],
  tags: ["tannaka-krein", "reconstruction", "hopf-algebra", "fibre-functor"],
  lean: {
    decl: "QOU.tannaka_krein_reconstruction",
    validation: "not_checked",
  },
  uses: [
    "def:quantum-observable-universe",
    "thm:su2-emergence",
    "prop:braiding-eigenvalue-extraction",
  ],
});
