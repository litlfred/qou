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
    // Declared by the .md banner and bound in the Lean (theorem at :305 binds [inst : BorromeanQuark]),
    // but absent here and unreachable in the uses[] graph at any depth
    // until 2026-08-30 — the dependency was recorded in prose only
    // (bean `qou-s3zd`). Not transitively reachable, so not redundant.
    "conj:borromean-quark",
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
    script:
      "computations/probes/hecke_1d_irrep_closed_form_character_probe.py",
    witness: [
      "computations/probes/hecke-1d-irrep-closed-form-character-probe.witness.json",
    ],
    status: "experimental",
  },
});
