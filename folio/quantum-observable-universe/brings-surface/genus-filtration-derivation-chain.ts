import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:genus-filtration-ideal",
  label: "rem:genus-filtration-derivation-chain",
  title:
    "The derivation chain from $H_n(q)$ to Bring's surface, and where it breaks",
  tags: [
    "derivation-chain",
    "brings-surface",
    "genus",
    "hecke",
  ],
  uses: ["prop:genus-filtration-ideal", "rem:torus-evaluation-block-rank"],
  authorNotes: [
    {
      kind: "refined-framing",
      date: "2026-09-15",
      body: "**Retitled and the non-circularity claim withdrawn.** The block opened *\"the full argument is non-circular\"* and closed *\"Bring's surface is a consequence of the algebra, not an input\"*, both resting on step 3 (the evaluation matrix reaching rank 5 at `g = 4`). Step 3 is false: the matrix is block-diagonal and its rank is capped at `2 + 2 = 4` for every `q` (`rem:torus-evaluation-block-rank`). Step 1 *is* independently derived — `QOU.SU2EmergenceRankForced.su2_emergence_rank_forced` gets `dim V = 2` and `G <= SU(2)` from the volume axiom with no chi input, sorry-free — so the chain is not circular at step 1; it is incomplete at step 3. Bean `qou-r3wu`.",
    },
  ],
});
