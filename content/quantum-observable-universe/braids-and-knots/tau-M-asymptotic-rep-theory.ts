import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:tau-M-asymptotic-rep-theory",
  lean: {
    ref: "qou:QOU.BraidKnot.tau_M_asymptotic_rep_theory",
    validation: "not_checked",
  },
  title:
    "$\\tau_M^{V_\\lambda}(\\beta) = \\mathrm{Tr}\\,\\rho_\\lambda(\\beta) \\cdot \\exp(-\\frac{1}{2} \\sum_k c_k^{(\\lambda)}(b_\\lambda) \\hbar_q^{2k})$: representation-theoretic asymptotic expansion of the Markov-traced character",
  uses: [
    "prop:hecke-1d-irrep-closed-form-character",
    "prop:q-beta-cos-resummation",
    "prop:hoefsmit-V21-cos-symmetrization",
    "prop:habiro-residue-sum-equivalence",
    "prop:beta-decay-transfer-matrix",
  ],
  cites: [
    "kashiwara1990",
    "macdonald1995",
    "habiro2002",
    "jones1985",
    "wenzl1988",
    "hoefsmit1974",
  ],
  tags: [
    "hecke-algebra",
    "asymptotic-expansion",
    "kashiwara-crystal",
    "jucys-murphy",
    "macdonald-polynomial",
    "habiro-residue",
    "rep-theory-prediction",
    "1ppb-roadmap",
  ],
  computation: {
    witness: [
      "../../folio-assistant/computations/q-beta-operator-valued-N1.witness.json",
      "../../folio-assistant/computations/q-beta-operator-valued-N2.witness.json",
      "../../folio-assistant/computations/q-beta-three-irrep-closed-form.witness.json",
    ],
  },
});
