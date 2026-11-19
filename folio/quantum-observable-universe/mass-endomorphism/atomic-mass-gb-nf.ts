import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:atomic-mass-gb-nf",
  title: "Atomic mass as Markov trace of the Gröbner–Shirshov normal form",
  uses: [
    "prop:alpha-shift-torus-knot",
    "unital-groebner-bases:cor:pbw",
  ],
  cites: ["kassel1995", "jones1987"],
  tags: [
    "mass",
    "atomic-mass",
    "markov-trace",
    "groebner-shirshov",
    "normal-form",
    "hecke-algebra",
    "categorical-density",
  ],
  lean: {
    ref: "qou:QOU.BraidKnot.atomicMassGBNF",
    validation: "not_checked",
  },
  computation: {
    engine: "python+mpmath",
    script: "computations/canonical_mass_table_extended.py",
    witness: [
      "computations/canonical-mass-table-extended.witness.json",
    ],
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", body: "Archimedean specialisation over R (§7c)." },
  ],
});
