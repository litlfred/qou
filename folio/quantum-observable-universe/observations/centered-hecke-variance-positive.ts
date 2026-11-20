import { proposition } from "../../schema/builders";

export default proposition({
  label: "prop:centered-hecke-variance-positive",
  title:
    "Centred Hecke transfer matrix has strictly positive variance for every $q > 0$",
  lean: { ref: "qou:QOU.Observations.centered_hecke_variance_positive", validation: "not_checked" },
  uses: [
    "thm:jones-markov-trace",
    "rem:non-commutative-probability-dictionary",
  ],
  tags: [
    "q-clt",
    "variance",
    "wenzl-positivity",
    "established",
  ],
  proofs: ["prf:centered-hecke-variance-positive"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Positivity of the Temperley–Lieb tracial state isformalized in `QOU.SchurWeyl.ocneanuWeight_conventionD_pos_of_two_rows`." },
    {
      kind: "status",
      body: "**Provable arithmetic.** The proof in `prf:centered-hecke-variance-positive` is direct algebra: under convention D the variance is $(q^4+q^2+1)/(q^2+1)^2$, a ratio of manifestly positive polynomials, minimised at $q = 1$ where it equals $3/4$. (Superseded 2026-08-09: the earlier route ran through $(q^{1/2}+q^{-1/2})^2 > 4$ ⟹ Wenzl regime ⟹ variance positive, which was convention-C-specific.)",
    },
    {
      kind: "note",
      date: "2026-08-09",
      body: "**Convention D restatement — the result strengthens.** This block was stated on the excised convention C, $z = 1/(q^{1/2}+q^{-1/2})$, and quoted $\\mathrm{Var}(\\sigma_i) \\approx 0.855$ at $q_0$; the correct value is $0.75270211325196540159$. Three things change. (i) The **hypothesis weakens**: positivity is now unconditional on $q > 0$, where under C it needed the Wenzl regime and the proposition was declared vacuous outside it. (ii) The **bound sharpens**: $3/4$ is attained, at $q = 1$, rather than being a strict lower bound. (iii) The variance turns out to be a known object — $\\mathrm{Var}(\\sigma_i) = y_{(3)} + y_{(2,1)} = \\mu_+$, the isospin-triplet Wenzl weight, identically in $q$, and equal in magnitude to the extreme eigenvalues $\\pm 0.75270211$ of the Markov–Gram form on the bilinear pairing at $q_0$. **Not settled here:** the Wenzl positivity threshold under D. The dropped hypothesis was doing double duty — algebraic (unnecessary, and removed) and probabilistic (the condition making $\\mathrm{tr}_M$ a positive functional, so that this number is the variance of a tracial state). The latter is recorded as a dated open note on the statement and gates the $q$-CLT reading in the interpretation sidecar. The Lean sibling `QOU.Observations.centered_hecke_variance_positive` still carries the C statement and needs the same restatement.",
    },
  ],
});
