import { conjecture } from "../../schema/builders";

export default conjecture({
  label: "conj:p-from-braid-mirror",
  title:
    "Parity $P$ as mirror reflection of the braid diagram (writhe sign flip)",
  lean: {
    ref: "qou:QOU.BraidsAndKnots.PFromBraidMirror",
    validation: "not_checked",
  },
  uses: [
    "conj:cpt-d6-d7-d8-closure",
    "def:bar-involution",
    "conj:cpt-orbit-closure-density",
    "prop:chirality-writhe-ribbon-derivation",
  ],
  cites: [
    "kassel1995",
    "jones1987",
    "kauffman1991",
  ],
  tags: [
    "tier:S",
    "parity",
    "duality-d7",
    "braid-mirror",
    "writhe",
    "cpt-decomposition",
    "axiom-class",
    "open-problem",
    "conditional-on-class",
  ],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body:
        "Lean names moved out of the prose (voice drain, epic `qou-d4kh`): sketched as `class PFromBraidMirror (M) [BrCategory M] [Hecke M]` with fields `p_action`, `p_involution`, `p_on_generator`, `p_preserves_q`, `bar_eq_p_c_t`.",
    },
  ],
});
