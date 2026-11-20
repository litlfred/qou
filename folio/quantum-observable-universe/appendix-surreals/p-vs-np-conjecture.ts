import { conjecture } from "../../schema/builders";

export default conjecture({
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): It is formulated in the Reeb--surreal framework but lacks a Lean formalisation. A formal proof would ..." },
    {
      kind: "note",
      date: "2026-08-08",
      body:
        "**§7c base-ring note.** The Lean class `PvsNPQou` carries " +
        "`strict_separation : ∀ (eps : ℝ), 0 < eps → ∃ s : ℝ, 0 < s ∧ s ≤ eps` " +
        "and `noncompressible : ∃ s0 : ℝ, 0 < s0`. The `eps` is the **Reeb " +
        "infinitesimal** of the `ε → 0` non-compressibility limit, and the " +
        "quantifier alternation `∀ eps > 0, ∃ s` is an archimedean smallness " +
        "statement: it is exactly the ordering on `ℝ` that gives it content. " +
        "Over a generic ring there is no `0 <` to quantify, so `ℝ` is " +
        "load-bearing rather than gratuitous.",
    },
  ],
  label: "conj:p-vs-np-qou",
  title:
    "P vs NP in the QOU: classical-limit separation of BQP-width classes",
  lean: {
    ref: "qou:QOU.AlgebraicSubstrate.PvsNPQou",
    validation: "not_checked",
  },
  uses: [
    "def:reeb-epsilon",
    "prop:surreal-rate-calculus",
  ],
  tags: [
    "tier:famous",
    "p-vs-np",
    "millennium-problem",
    "complexity",
    "bqp",
    "reeb-period",
    "classical-limit",
    "surreal",
    "speculative",
  ],
  cites: ["cook1971", "freedman2003"],
});
