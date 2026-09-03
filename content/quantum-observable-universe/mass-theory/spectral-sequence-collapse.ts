import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:spectral-sequence-collapse",
  title: "GB spectral sequence collapses at E_1 (semisimple cohomology vanishing)",
  lean: {
    ref: "qou:QOU.WedderburnMass.centralIdempotent_idem",
    validation: "not_checked",
  },
  uses: ["prop:curvature-rank-gb-stratification"],
  authorNotes: [
    {
      kind: "status",
      date: "2026-08-26",
      body:
        "**The Lean does not prove this block's statement.** The `.md` asserts " +
        "the GB spectral sequence collapses at `E_1` with everything in `Z(A)`. " +
        "The Lean sibling proves `e * e = e` — the `SemisimpleAlgebra.e_idem` " +
        "class field — and nothing more. It was named " +
        "`spectral_sequence_collapses_to_centre` until 2026-08-26; it is now " +
        "`centralIdempotent_idem`, so the name no longer overstates it.\n\n" +
        "The underlying mathematics is not in doubt for the finite Hecke " +
        "algebra: `H_n(R,q)` is semisimple at generic `q`, so Whitehead's lemma " +
        "gives `HH^k = 0` for `k >= 1`. What is missing is a Lean *statement*, " +
        "and two things block writing one — Mathlib has no Hochschild-cohomology " +
        "framework, and there is no defined filtration to collapse (all three " +
        "corpus readings of `J^bullet` are excluded).\n\n" +
        "**Open question this block does not settle:** whether it should stay a " +
        "`proposition`. Demoting it to `conjecture` would be honest but would " +
        "propagate under §3b to every consumer. That is an author call, tracked " +
        "in bean `qou-cq5g`.",
      see: "docs/audits/2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md",
    },
  ],
});
