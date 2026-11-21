import { remark } from "../../schema/builders";

export default remark({
  label: "rem:einstein-nonsymmetric-metric-comparison",
  title:
    "Position against Einstein's non-symmetric field theory",
  interprets: "prop:crossing-energy-decomposition",
  authorNotes: [
    {
      kind: "note",
      date: "2026-07-29",
      body:
        "Added after a corpus survey found the non-symmetric field-theory programme absent from every grep path. Comparison rationale, the three structural differences, and the retraction of an earlier (incorrect) reading of the $T_{2,9}$/$T_{3,5}$ selection as fitted are recorded in `docs/audits/2026-07-29-einstein-asymmetric-metric-vs-qou.md`.",
      see: "docs/audits/2026-07-29-einstein-asymmetric-metric-vs-qou.md",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): Gravitation in this framework is the geometry of the [acoustic metric](#rem:madelung-acoustic-metric) of the Madelung brane flow, which is symmetric." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): 3. *The $q$-deformation of the metric is conformal, not antisymmetric.* The parameter $q$ does act on a metric in the [contact deformation](#rem:q-metric-contact-deformation), interpolating the Levi-Civita connection to its Reeb projection. That deformation is conformal and contact-theoretic; it does not add an antisymmetric part." },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): **Note on terminology.**\nThe torsion appearing in the [substrate parameter axiom](#rem:substrate-gm-torsion) is the torsion subgroup $\\mu_\\infty \\subset \\mathbb{G}_m$ of roots of unity, which the substrate section must avoid. It is unrelated to the torsion tensor of an affine connection used in Einstein--Cartan theory and in nonsymmetric gravitational theory." },
  ],
  uses: [
    "prop:crossing-energy-decomposition",
    "def:crossing-energy",
    "ex:braid-group-su2",
    "rem:crossing-energy-interpretation",
    "prop:em-coupling-projection",
    "rem:madelung-acoustic-metric",
    "rem:q-metric-contact-deformation",
    "rem:substrate-gm-torsion",
    "rem:lqg-adm-ashtekar-comparison",
  ],
  cites: [
    "einstein1925",
    "einstein1946",
    "einstein1955",
    "schrodinger1950",
    "damour1993",
    "moffat1995",
  ],
  tags: [
    "einstein",
    "nonsymmetric-metric",
    "unified-field-theory",
    "electromagnetism",
    "crossing-energy",
    "braiding",
    "comparison",
  ],
});
