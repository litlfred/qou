import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:explicit-central-idempotent-lagrange",
  renamedFrom: ["conj:explicit-central-idempotent"],
  title:
    "Murphy–Lagrange completeness, orthogonality, and transpose pairing from joint-eigenbasis interpolation",
  lean: {
    ref: "qou:QOU.MassEndomorphism.MurphyLagrangeCentralIdempotents.shapeCentralEnd_mul",
    sorryFree: true,
    validation: "leanok",
  },
  uses: [
    "prop:jucys-murphy-central-elements-qou",
    "prop:hoefsmit-seminormal-form",
  ],
  cites: ["murphy1981", "dipper-james1986", "ram1997"],
  tags: [
    "central-idempotent",
    "murphy-elements",
    "lagrange-interpolation",
    "hecke-algebra",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Proved unconditionally in `QOU.MassEndomorphism.MurphyLagrangeCentralIdempotents` (`shapeCentralEnd_sum_eq_one`, `shapeCentralEnd_mul`, `shapeCentralEnd_idem`, `qContent_transpose_eq_inv`, `conj_shapeCentralEnd_eq_transpose`, `conj_shapeCentralEnd_self_conjugate`).",
    },
  ],
});
