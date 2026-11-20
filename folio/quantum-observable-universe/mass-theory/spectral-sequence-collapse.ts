import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:spectral-sequence-collapse",
  title: "Limit page of the GB spectral sequence for semisimple $H_n(R, q)$",
  lean: {
    ref: "qou:QOU.WedderburnMass.centralIdempotent_idem",
    validation: "not_checked",
  },
  uses: ["prop:gb-spectral-sequence"],
  authorNotes: [
    {
      kind: "note",
      date: "2026-11-20",
      body: "`uses` repointed from the curvature-rank stratification (now `conj:curvature-rank-gb-stratification`) to `prop:gb-spectral-sequence` (bean `qou-6qbv`). The statement and its proof use only the spectral sequence of the filtered Hochschild complex and Hochschild's vanishing theorem for separable algebras; the stratification is cited only in the proof's corollary paragraph. With the length filtration the statement is consistent with the exact $n = 3$ computation: $E_\\infty$ is the rank-3 centre in degree $0$ while $d_2$ and $d_4$ are nonzero, so the sequence does not collapse at $E_1$ or $E_2$.",
    },
    {
      kind: "caveat",
      date: "2026-11-16",
      body: "The statement said the GB spectral sequence collapses at $E_1$, and the proof's practical consequence said all differentials vanish. Vanishing of $\\mathrm{HH}^k$ for $k \\geq 1$ only fixes the limit page ($E_\\infty$ concentrated in total degree 0); it does not force $d_r = 0$. Also: the statement now requires $R$ a field with $H_n(R,q)$ semisimple and separable; the vanishing theorem is Hochschild's for separable algebras, not Whitehead's lemma; and the Lean docstring's `Σ w_λ = 1` was corrected to the classical weights only.",
    },
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
