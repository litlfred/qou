import { lemma } from "../../schema/builders";

export default lemma({
  label: "lem:bring-map-euler-characteristic",
  lean: { ref: "qou:QOU.BringsSurface.BringMapChain.bring_chi" },
  title: "Euler characteristic of the Bring map",
  tags: ["euler-characteristic", "brings-surface", "combinatorial-map"],
  uses: ["lem:brings-euler-characteristic"],
  proofs: ["prf:bring-map-euler-characteristic"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-11-27",
      body:
        "**Owner ruling 2026-11-27 (\"Start from the finite map\"):** the χ = −6 chain starts from this finite map, not from a compact Riemann surface. The smooth surface is a model of the map. The route from a Riemann surface to the map (Radó's theorem, monodromy) is kept as a backup: beans `qou-0nr6`, `qou-gu23`. Lean: `QOU/BringsSurface/BringMapChain.lean`; combinatorial lift: `MathlibExt/VoltageLift.lean`.",
    },
  ],
});
