import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:degree-one-braid-trivial-volume",
  title:
    "Braid words of a degree-one element have non-hyperbolic closures",
  lean: {
    ref: "qou:QOU.Photon.linearVol_eq_zero_of_mem_span",
    validation: "not_checked",
  },
  cites: ["kashaev1997"],
  tags: [
    "photon",
    "masslessness",
    "degree-one",
    "archimedean",
    "unknot",
  ],
  authorNotes: [
    {
      kind: "caveat",
      date: "2026-11-16",
      body:
        "**Restated 2026-11-16 (QA finding: da-non-sequitur, critical).** The block " +
        "claimed $\\tau_{\\mathrm{arch}}(\\mathrm{tr}_M(\\gamma)) = 0$ by linearity of a volume " +
        "map on the Hecke algebra. No such map exists: positive permutation braids span " +
        "$H_3(q)$ and close to non-hyperbolic links, so a linear volume would vanish on " +
        "$4_1$, whose volume is $2.0299$. The claim is now word-level. The Lean sibling, " +
        "which assumed an additive volume vanishing on each summand, now proves the " +
        "span obstruction instead. No compute impact.",
    },
  ],
  computation: {
    engine: "mpmath",
    script: "computations/derive_m_baryon_volume_form.py",
    witness: "computations/m-baryon-volume-form.witness.json",
    status: "verified",
  },
});
