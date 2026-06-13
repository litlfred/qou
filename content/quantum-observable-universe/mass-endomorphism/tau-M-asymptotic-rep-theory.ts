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
    "prop:hoefsmit-V21-cos-symmetrization",
    "prop:habiro-residue-sum-equivalence",
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
    engine: "python+mpmath",
    script: "folio-assistant/computations/probe_q_beta_operator_valued_N2.py",
    status: "experimental",
  },
  authorNotes: [
    {
      kind: "status",
      body: "The exponential-asymptotic form above is a **rep-theoretic\nprediction**, validated at $k = 0, 1, 2$ at $q_0$ to ${\\leq} 25$ ppm\nprecision. The $c_k^{(\\lambda)}(b_\\lambda)$ coefficients beyond $k = 2$\nare open R&D — pinning them down requires either:\n\n- Full Kashiwara crystal-graph matrix-exponential machinery\n (per-irrep $\\exp(\\tilde f_1)$ computation);\n- JM symmetric-function expansion with explicit $c_T(k)$ tabulation;\n- Macdonald $(q, q^2)$ specialisation evaluations;\n- Habiro-residue Borel resummation at chosen $\\zeta_N$.\n\n's N=1 result + N=2 partial result together establish that\nthe structural form is correct; refining the $c_k$ coefficients to\n1 ppb requires per-anchor follow-up probes.",
    },
  ],
});
