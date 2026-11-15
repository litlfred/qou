import { remark } from "../../schema/builders";

export default remark({
  label: "rem:spatial-realization-base-generality",
  title: "The base of the spatial realisation: the properties used and the case excluded",
  interprets: "def:spatial-realization-functor",
  uses: [
    "def:spatial-realization-functor",
    "def:categorical-point",
    "def:categorical-reeb",
  ],
  foreshadows: ["rem:hkr-theorem", "rem:yekutieli-setting-explicit"],
  cites: ["hartshorne-1977", "hkr-1962", "orlik-wagreich1971"],
  tags: ["spatial-realization", "smoothness", "kahler-differentials", "base-manifold", "generality", "singular-base"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-09-15",
      body:
        "Written in answer to the owner's question (2026-09-15) why the target of the spatial realisation is asserted to be an ordinary smooth manifold rather than something more general. The remark separates what the definition asserts from what the downstream constructions use, and names the categorical condition (Ω¹(A) dualisable of constant rank) that would replace the assertion. Rewording the definition itself is a content change to a definition block and is left for the owner; nothing is altered here. The singular-base paragraph rests on bean `qou-rydq` (the link of the Bring cone is a Seifert manifold with infinite fundamental group) and the arithmetic in `QOU/Brings/BringConeLinkEulerNumber.lean`.",
    },
  ],
});
