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
    "prop:hecke-branching-trace-decomposition",
    "prop:q-beta-cos-resummation",
    "rem:operator-valued-interface",
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
    witness: [
      "../../folio-assistant/computations/q-beta-1d-irrep-universal-closed-form.witness.json",
      "../../folio-assistant/computations/q-beta-three-irrep-closed-form.witness.json",
    ],
  },
});
