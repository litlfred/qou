import { remark } from "../../schema/builders";

export default remark({
  label: "rem:qou-motivic-galois-instance-verification",
  title: "Construction, verification, and coherence of the QOU $\\mathrm{Frob}_p$ instance",
  interprets: "conj:qou-motivic-galois-instance",
  tags: ["motivic-galois", "frobenius", "habiro", "weil-purity", "coherence"],
  uses: [
    "conj:qou-motivic-galois-instance",
    "def:motivic-galois-character",
  ],
  cites: ["habiro2002", "yekutieli2010"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-08-08",
      body: "This instance is what discharges GAP 5b of `docs/audits/family-4-motivic-path.md`. That audit is a branch-local working note, so the published prose now states the mathematical consequence (downstream theorems consume the explicit QOU instance instead of carrying `def:motivic-galois-character` as an `[instance]` hypothesis) without citing it.",
    },
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "Retargeted `interprets` / `uses` from `def:` to " +
        "`conj:qou-motivic-galois-instance` — the block it interprets was " +
        "reclassified `definition()` → `conjecture()` (bean `qou-s0ip`).",
    },
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "Corrected two claims this remark had been carrying since " +
        "2026-08-12. (1) The \"Lean instance\" bullet linked to a co-located " +
        "`qou-motivic-galois-instance.lean` that was deleted that day, and " +
        "described an `almost_everywhere_nontrivial` field that was removed " +
        "from `MotivicGaloisCharacter` the same day. (2) \"Downstream " +
        "consumers\" stated the perpetual obstruction \"becomes an " +
        "unconditional theorem\" as a present fact; it is conditional on an " +
        "instance that does not exist. The unconditional result that does " +
        "exist reaches the obstruction by a different route " +
        "(`MotivicPerpetualObstructionFromTrace.lean`, prime-ideal collapse) " +
        "and constructs no instance.",
    },
    {
      kind: "note",
      date: "2026-08-23",
      body:
        "The anchor here was `#conj:motivic-perpetual-obstruction`, which " +
        "resolved to nothing: `motivic-perpetual-obstruction.ts` declared " +
        "`theorem({ label: \"conj:...\" })`, a kind/prefix mismatch that made " +
        "the block fail schema validation and never register its label, so " +
        "~14 blocks referenced a label no block owned. Not replayed by hand " +
        "at the time, because `main` had already renamed it to " +
        "`thm:motivic-perpetual-obstruction` and 17 of the 18 affected files " +
        "differed from `main` by that rename alone. It came in with the merge " +
        "of `main`, and the anchor here now points at `thm:`.",
    },
  ],
});
