import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:markov-pair-z2",
  title:
    "All-pairs Markov-trace identity $\\mathrm{tr}_M(\\sigma_i\\sigma_j) = z^2$",
  tags: [
    "markov-trace",
    "hecke-algebra",
    "pair-factorization",
    "jet-tower",
  ],
  lean: {
    ref: "qou:QOU.Hecke.markov_pair_z2",
    validation: "not_checked",
  },
  uses: ["rem:mass-endomorphism-jet-tower"],
  cites: ["kassel1995", "jones1987"],
  computation: {
    engine: "sympy",
    script: "computations/markov/markov_peel_atomic_witness.py",
    witness: "computations/markov/markov-peel-atomic-tr-m.witness.json",
    consumers: [
      "computations/cross_check_trM_1ppb.py",
      "computations/cross_check_trM_wenzl_lr_1ppb.py",
      "computations/sweeps/paper_six_term_isotope_sweep.py",
    ],
    status: "verified",
  },
});
