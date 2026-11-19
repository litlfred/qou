import { proposition } from "../../schema/builders";

/**
 * Rewritten 2026-08-21 (bean qou-6y28). The original imported `ContentBlock`
 * from "../../pipeline/content-block" — a module that has NEVER existed here
 * (`git log --all` on that path returns zero commits) — and called it as a
 * constructor. It never imported, so the block never rendered and no
 * per-block checker ever saw it, from 649f5eb701 (2026-06-28) onward.
 *
 * Its `dependencies` are NOT carried over, because neither label exists:
 *
 *     def:q-reeb-flow    no such label. The closest real ones are
 *                        `def:categorical-q-reeb-flow` and
 *                        `def:q-reeb-flow-on-color-coords`.
 *     def:markov-trace   no such label, and no `def:` block for the Markov
 *                        trace exists at all — only `prop:` statements.
 *
 * Picking a replacement would be guessing at what the author meant, and a
 * `uses[]` edge is a claim about the dependency structure. `uses` is
 * optional, so this manifest asserts only what is checkable and leaves the
 * edges to whoever knows the intent. Both nonexistent labels are recorded
 * here rather than dropped silently, because they are evidence about how
 * the block was authored: against an invented API AND invented labels.
 *
 * NOT wired into the chapter manifest. Its claim — the Lever-3
 * normalisation B(K) = rho * S(K) on a Markov-weighted q-Reeb phase sum —
 * has never been reviewed, and wiring unreviewed content into the paper is
 * a content decision, not a manifest repair.
 */
export default proposition({
  label: "prop:atomic-q-reeb-universal-rho",
  title: "Universal-ρ normalisation on the atomic q-Reeb object (Lever 3)",
  lean: {
    ref: "qou:QOU.MassTheory.AtomicQReebUniversalRho.lever3_mirror_ratio_rho_independent",
    sorryFree: true,
    validation: "leanok",
  },
  tags: ["mass-theory", "q-reeb", "binding", "lever-3"],
  computation: {
    engine: "mpmath",
    script: "computations/binding_reeb_ratio_rho_free.py",
    witness: "computations/binding-reeb-ratio-rho-free.witness.json",
    status: "verified",
  },
});
