import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:categorical-mass-markov",
  title: "Categorical mass as Markov trace",
  uses: [],
  tags: [
    "mass",
    "categorical-trace",
    "markov-trace",
    "frobenius",
    "nakayama",
    "hecke-algebra",
  ],
  lean: { ref: "qou:QOU.CategoricalMassMarkov",
    validation: "not_checked",
  },
  computation: {
    engine: "python",
    script: "computations/canonical_isospin_pyhecke.py",
    witness:
      "computations/canonical-isospin-pyhecke.witness.json",
    status: "verified",
    requires: ["pyhecke"],
  },
  authorNotes: [
    {
      kind: "note",
      body:
        "Lean sibling is archimedean by construction (AGENTS.md §7c): Term 1 of the unified mass formula is the real absolute value `term_one := |tr_M T_w|` (in MeV), so the Markov algebra is typed over `Module ℝ` with `tr_M : A →ₗ[ℝ] ℝ`. The ordering/absolute-value content lives on the observable side of the substrate→archimedean wall — the mass is a genuine real observable, not a gratuitous ℝ-specialisation of otherwise-generic Markov-trace combinatorics.",
    },
  ],
});
