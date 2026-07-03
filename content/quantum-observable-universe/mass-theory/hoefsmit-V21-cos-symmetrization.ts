import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hoefsmit-V21-cos-symmetrization",
  lean: {
    ref: "qou:QOU.BraidKnot.hoefsmit_V21_cos_symmetrization",
    validation: "not_checked",
  },
  title:
    "Hoefsmit seminormal matrix for $V_{(2,1)}$ + Markov-symmetrized cos character: $\\chi^{(2,1),\\mathrm{symm}}_q(\\beta) = \\mathrm{tr}\\,\\rho_{(2,1)}(\\beta) \\cdot \\cos((z-1)h/2)$",
  uses: ["prop:hecke-1d-irrep-closed-form-character"],
  cites: [
    "hoefsmit1974",
    "wenzl1988",
    "jones1985",
  ],
  tags: [
    "hecke-algebra",
    "hoefsmit-seminormal",
    "2d-irrep",
    "markov-symmetrization",
    "cos-resummation",
    "V_(2,1)",
    "non-trivial-markov-machinery",
    "1ppb-roadmap",
  ],
  computation: {
    engine: "mpmath",
    // Verifies the Hoefsmit V_(2,1) closed forms (d1, d2, b^2 =
    // (h^2+3)/(h^2+4)), the Hecke + braid relations of the explicit
    // matrices, and the proton trace cross-validation. The
    // cos-symmetrized character remains conditional on
    // prop:q-beta-cos-resummation (former probe
    // probe_q_beta_operator_valued_N2.py was deleted).
    script: "computations/hoefsmit_b_squared_reconciliation.py",
    witness: "computations/hoefsmit-b-squared-reconciliation.witness.json",
    status: "experimental",
  },
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
    {
      kind: "status",
      body: "- **The Hoefsmit V_(2,1) matrices are explicit closed forms in $q$**:\n  $d_1 = q^3/(q^2+1), d_2 = -q^{-1}/(q^2+1), b^2 = d_1 d_2 + 1$.\n  These are *substrate-derivable* — no empirical inputs.\n- **The cos-symmetrized character is conditional** on\n  [`prop:q-beta-cos-resummation`](#prop:q-beta-cos-resummation)'s\n  eigenphase identification.\n- **The full decomposition is verified bit-exact at 50 dps** via\n  [`probe_q_beta_three_irrep_closed_form.py`](../../computations/probe_q_beta_three_irrep_closed_form.py)\n  and\n  [`probe_q_beta_1d_irrep_universal.py`](../../computations/probe_q_beta_1d_irrep_universal.py).",
    },
  ],
});
