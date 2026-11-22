import { remark } from "../../schema/builders";

export default remark({
  authorNotes: [
    {
      kind: "note",
      date: "2026-09-04",
      body:
        "The final paragraph previously read that the ambient $S^3$ *must not be confused with* " +
        "the group manifold $\\mathrm{SU}(2) \\cong S^3$. `docs/audits/2026-06-28-ed-ambient-s3-" +
        "gauge-embedding-wlambda-scope.md` §(i) asserts the opposite ('the ambient volume-$S^3$ is " +
        "the gauge-group $SU(2)$ itself') and claims to sharpen this remark, and `def:reeb-bundle` " +
        "states the Hopf fibration $S^3 \\to \\mathcal{S}_p \\cong S^2$ without drawing the " +
        "conclusion. Only this remark and `def:reeb-bundle` render; the audit does not. The paragraph " +
        "now records the tension instead of asserting either side — the identification is an open " +
        "question for the author, not a typo. See `docs/audits/2026-09-04-w-derived-not-postulated-" +
        "degree-of-the-volume-form.md` §3, §7.",
    },
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the reading-order drain (qou-d4kh, owner ruling: every chapter strict): : the [Reeb bundle](#def:reeb-bundle) presents a three-sphere as the total space of the Hopf fibration $S^3 \\to \\mathcal{S}_p \\cong S^2$, which is the coset projection $\\mathrm{SU}(2) \\to \\mathrm{SU}(2)/U(1)$, and under that reading the two are the same object. The identification is not settled here" },
  ],
  label: "rem:markov-trace-ambient-s3",
  title:
    "The ambient three-sphere $S^3$ is the target of the Alexander--Markov correspondence: $\\mathrm{tr}_M$ is by construction a link invariant in $S^3$",
  interprets: "thm:jones-markov-trace",
  uses: ["thm:jones-markov-trace"],
  cites: ["alexander1923", "markov1936", "jones1987"],
  tags: [
    "markov-trace",
    "ambient-manifold",
    "three-sphere",
    "alexander-markov",
    "knot-complement",
    "categorical-topology",
  ],
});
