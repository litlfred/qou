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
        "Not fixed here, and not a defect of this cluster: the anchor " +
        "`#conj:motivic-perpetual-obstruction` resolves to nothing on this " +
        "branch, and `run-validate` reports it from ~14 blocks. The cause is " +
        "branch staleness, not content — `motivic-perpetual-obstruction.ts` " +
        "declares `theorem({ label: \"conj:...\" })`, a kind/prefix mismatch " +
        "that makes the block fail schema validation and never register its " +
        "label. `main` fixed it by renaming the label to " +
        "`thm:motivic-perpetual-obstruction`; 17 of the 18 files still " +
        "carrying `conj:` here differ from `main` by that rename and nothing " +
        "else. Deliberately not replayed by hand — it lands when this branch " +
        "is brought up to `main`, and hand-replaying it would only " +
        "manufacture a conflict.",
    },
  ],
});
