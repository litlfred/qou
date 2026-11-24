import { definition } from "../../schema/builders";

export default definition({
  label: "def:kz-connection-sl2",
  lean: { ref: "qou:QOU.Mass.KZConnectionSl2.kzResidue", validation: "not_checked" },
  title: "The $\\mathfrak{sl}_2$ Knizhnik--Zamolodchikov connection and its flatness",
  tags: ["kz-connection", "flat-connection", "braid-group", "drinfeld-kohno"],
  uses: ["prop:categorical-mass-markov"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-10-11",
      body:
        "**Added for goal milestone qou-ywyq (bean qou-d0qq).** Before this block the corpus had no " +
        "definition of the Knizhnik--Zamolodchikov connection, and its one flat-connection definition, " +
        "`def:q-flat-connection`, is formalised as `QOU.QFlatConnection := trivial`. Here flatness is the " +
        "infinitesimal pure braid relations, proved for the KZ residues (`kz_isFlat`) and shown false for " +
        "another residue family (`not_isFlat_example`), so the predicate has content. The reduction of " +
        "$d\\omega - \\omega\\wedge\\omega = 0$ to those relations via the Arnold relation is proved in both " +
        "directions for three points (`curvature_zero_of_isFlat`, `relations_of_curvature_zero`, " +
        "`kz_curvature_zero`); general $n$ is cited (Kohno 1987, section 1.1). This block does not claim the framework's substrate " +
        "connection is this connection; that is open (bean qou-d0qq).",
    },
  ],
});
