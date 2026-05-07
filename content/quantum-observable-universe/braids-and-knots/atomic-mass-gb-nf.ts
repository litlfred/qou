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
    engine: "mpmath",
    script: "folio-assistant/computations/atomic_braid_mass_table.py",
    witness: [
      "folio-assistant/computations/atomic-braid-mass-table-modes-sweep.witness.json",
      "folio-assistant/computations/atomic-braid-mass-table.witness.json",
    ],
    status: "experimental",
  },
});
