import { remark } from "../../schema/builders";

export default remark({
  label: "rem:three-substantive-mathlib-fillers",
  title:
    "Three substantive Mathlib gaps: BlochGroup quotient, $\\mathrm{Cl}_2$ pentagon, Faddeev-Kashaev limit",
  interprets: "rem:mass-tower-deeper-fillers",
  uses: ["rem:mass-tower-deeper-fillers"],
  cites: [
    "bloch2000",
    "suslin1991",
    "borel1974",
    "zagier1986",
    "faddeev1994",
    "kashiwara1991",
  ],
  tags: [
    "mathlib-filler",
    "substantive-gap",
    "bloch-group",
    "pentagon-identity",
    "faddeev-kashaev",
    "free-abelian-group",
    "lean-infrastructure",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-19",
      body: "Lean/Mathlib formalisation (`three-substantive-mathlib-fillers.lean`): (1) Bloch group carrier `PreBlochElement F`, `PreBlochGroup F := FreeAbelianGroup (PreBlochElement F)`, `HasPentagonRelation F`, `HasBlochGroup F`; (2) Clausen pentagon class `Cl_2_PentagonHolds` and boundary theorem `Cl_2_pentagon_at_zero`; (3) Faddeev-Kashaev limit class `FaddeevKashaevQuasiClassicalLimit x` (extending `ArchimedeanLimit`) and boundary theorem `faddeev_kashaev_at_zero`; combined in `HasAllSubstantiveFillers F` with `three_substantive_fillers_synthesis_consistent`.",
    },
  ],
});
