import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:borromean-baryon-mass-formula",
  title:
    "Borromean baryon mass formula with common Borromean term $\\mathfrak{m}_{\\mathcal{B}_3}(q_0)$",
  lean: {
    ref: "qou:QOU.Borromean.MassFormula",
    validation: "not_checked",
  },
  computation: {
    engine: "mpmath",
    script:
      "computations/derive_m_baryon_volume_form.py",
    witness:
      "computations/m-baryon-volume-form.witness.json",
    status: "verified",
  },
  uses: [
    "def:borromean-baryon",
    "def:typed-crossing-operator",
    "prop:graded-hecke-energy-truncation-bound",
  ],
  cites: [
    "thurston1978",
    "kashaev1997",
    "murakami-murakami2001",
    "codata2022",
  ],
  tags: [
    "tier:E",
    "borromean",
    "baryon",
    "mass-formula",
    "topological-mass",
    "lambda-scale",
    "common-scale",
    "open-problem",
    "substrate-only",
    "vol-form",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      /* <!-- literal-source: hyperbolic volume of Borromean link 8*Catalan = 7.32772475 (8-dp Lean constant volBorromean) --> */
      body: `**Base ring (§7c) — \`ℝ\` is load-bearing.** \`volBorromean := 7.32772474\` and \`vol_4_1 := 2.0298832128\` are decimal hyperbolic volumes, and \`BorromeanCommonScale\` carries \`positive : value > 0\`. Decimal geometric constants and an ordering field are archimedean by construction — this block sits on the observable side of the wall, where a mass formula belongs.`,
    },
  ],
});
