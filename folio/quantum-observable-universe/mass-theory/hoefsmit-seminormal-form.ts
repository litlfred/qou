import { proposition } from "../../schema/builders";

export default proposition({
  authorNotes: [
    { kind: "note", body: "Lean sibling: archimedean specialisation over $\\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data." },
  ],
  label: "prop:hoefsmit-seminormal-form",
  title:
    "Hoefsmit seminormal matrices as $R$-matrix evaluations in $H_n(q)$",
  lean: { ref: "qou:QOU.BraidKnot.hoefsmit_seminormal_form",
    validation: "not_checked",
  },
  uses: [
  ],
  cites: ["hoefsmit1974", "wenzl1988",
    "rutherford1948",
    "young1901",
  ],
  tags: [
    "hoefsmit",
    "seminormal",
    "r-matrix",
    "wedderburn-artin",
    "young-tableaux",
    "representation-theory",
  ],
  computation: {
    engine: "mpmath",
    script: "computations/probes/hoefsmit_seminormal_form_probe.py",
    witness: "computations/probes/hoefsmit-seminormal-form-probe.witness.json",
    status: "verified",
  },
});
