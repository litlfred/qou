import { definition } from "../../schema/builders";

/**
 * Discrete confinement layer L_k = (A_k, c_k, admissible_k), LP reduced cost,
 * confined motif, and functorial Dantzig-Wolfe column promotion L_k -> L_{k+1}.
 */
export default definition({
  label: "def:iterated-confinement-layer",
  title:
    "Confinement layer, confined motif, and functorial column promotion",
  lean: {
    ref: "qou:QOU.MathlibInfra.ConfinementLayerTower.ConfinementLayer",
    validation: "not_checked",
  },
  uses: [
    "def:molecular-braid",
    "def:electron-shell-braid-capacity",
  ],
  cites: [
    "dantzig-wolfe1960",
    "benders1962",
    "deloera-hemmecke-koeppe2013",
  ],
  tags: [
    "confinement-tower",
    "column-generation",
    "LP-dual",
    "reduced-cost",
    "renormalization",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-23",
      body:
        "Formalized over generic `[CommRing K]` / `[CommRing K] [LinearOrder K] [IsStrictOrderedRing K]` " +
        "(`ConfinementLayer`, `reducedCost`, `ConfinementLayer.IsConfinedMotif`, `promoteLayer`, " +
        "`promoteLayer_charge_conservation`) in `QOU.MathlibInfra.ConfinementLayerTower` (bean qou-5lct, §7c).",
    },
  ],
});
