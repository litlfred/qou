import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:hecke-1d-irrep-closed-form-character",
  lean: {
    ref: "qou:QOU.BraidKnot.hecke_1d_irrep_closed_form_character",
    validation: "not_checked",
  },
  title:
    "Universal closed form for 1-d Hecke irrep characters: $\\chi^{(n)}_q(\\beta) = q^w \\cdot ([2]_q/2)^m$ and $\\chi^{(1^n)}_q(\\beta) = (-q^{-1})^w \\cdot (-[2]_q/2)^m$ for typed braids of any $n$",
  uses: [
    "prop:q-beta-cos-resummation",
  ],
  cites: [
    "wenzl1988",
    "jones1985",
  ],
  tags: [
    "hecke-algebra",
    "1d-irrep",
    "closed-form",
    "universal-formula",
    "writhe",
    "averaged-crossings",
    "substrate-derivable",
    "tau-M-decomposition",
    "1ppb-roadmap",
  ],
  computation: {
    engine: "python+mpmath",
    script: "computations/probe_q_beta_operator_valued_N2.py",
    witness: ["computations/q-beta-operator-valued-N2.witness.json"],
    status: "experimental",
  },
});
