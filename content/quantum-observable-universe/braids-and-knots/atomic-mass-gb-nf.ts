import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:atomic-mass-gb-nf",
  title: "Atomic mass as Markov trace of the Gröbner–Shirshov normal form",
  uses: [
    "prop:categorical-mass-markov",
    "prop:alpha-shift-torus-knot",
    "prop:hecke-branching-trace-decomposition",
    "prop:rho-k-graded-expansion",
    "def:atomic-braid",
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
    engine: "markov_peel+mpmath",
    script: "folio-assistant/computations/canonical_mass_table_extended.py",
    witness: [
      "folio-assistant/computations/canonical-mass-table-extended.witness.json",
    ],
    status: "experimental",
  },
});
